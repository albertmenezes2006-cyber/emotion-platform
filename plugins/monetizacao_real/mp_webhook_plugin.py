import os
import hmac
import hashlib
from fastapi import APIRouter, Request, HTTPException
from plugins.plugin_base import PluginBase
import mercadopago
import psycopg2

router = APIRouter(prefix="/api/v1/mp-webhook", tags=["Webhook"])

import hmac
import hashlib

def validar_assinatura(request: Request, body: bytes):
    secret = os.getenv("MP_WEBHOOK_SECRET")
    if not secret:
        return True
    assinatura = request.headers.get("x-signature", "")
    if not assinatura:
        return False
    hash_calc = hmac.new(
        secret.encode(),
        body,
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(hash_calc, assinatura)


def get_sdk():
    token = os.getenv("MP_ACCESS_TOKEN")
    if not token:
        raise Exception("MP_ACCESS_TOKEN nao configurado")
    return mercadopago.SDK(token)

def get_db():
    return psycopg2.connect(os.getenv("DATABASE_URL"))

def upgrade_usuario(email: str, plano: str = "pro"):
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "UPDATE auth_usuarios SET plano=%s WHERE email=%s",
            (plano, email)
        )
        conn.commit()
        cur.close()
        conn.close()
        print(f"✅ Usuario {email} atualizado para {plano}")
        return True
    except Exception as e:
        print(f"❌ Erro ao atualizar usuario: {e}")
        return False

async def enviar_telegram(msg: str):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        return
    try:
        import httpx
        async with httpx.AsyncClient() as client:
            await client.post(
                f"https://api.telegram.org/bot{token}/sendMessage",
                json={"chat_id": chat_id, "text": msg}
            )
    except:
        pass

@router.post("/notificacao")
async def receber_webhook(request: Request):
    try:
        data = await request.json()
        # Log para debug
        print(f"🔔 Webhook recebido: {data}")
        tipo = data.get("type", "")
        
        if tipo != "payment":
            return {"status": "ignorado", "tipo": tipo}
        
        payment_id = data["data"]["id"]
        sdk = get_sdk()
        res = sdk.payment().get(payment_id)
        
        if res["status"] != 200:
            return {"status": "erro_mp"}
        
        payment = res["response"]
        status = payment.get("status", "")
        email = payment.get("payer", {}).get("email", "")
        valor = payment.get("transaction_amount", 0)
        descricao = payment.get("description", "")
        
        if status == "approved":
            plano = "clinica" if valor >= 99 else "pro"
            upgrade_usuario(email, plano)
            
            # Envia email de confirmacao
            try:
                from plugins.notificacoes.email_service import email_pagamento_aprovado
                email_pagamento_aprovado(email, plano, valor, str(payment_id))
            except Exception as e:
                print(f"Erro email: {e}")
            
            await enviar_telegram(
                f"💰 PAGAMENTO APROVADO!\n\n"
                f"Email: {email}\n"
                f"Valor: R$ {valor:.2f}\n"
                f"Plano: {plano}\n"
                f"ID: {payment_id}"
            )
        
        return {"status": "ok", "payment_status": status}
    
    except Exception as e:
        print(f"Webhook erro: {e}")
        return {"status": "erro", "detail": str(e)}

@router.get("/testar")
async def testar_webhook():
    return {
        "status": "ok",
        "webhook_url": f"{os.getenv('BASE_URL', '')}/api/v1/mp-webhook/notificacao",
        "instrucao": "Configure essa URL no painel do Mercado Pago em Webhooks"
    }


class MpWebhookPlugin(PluginBase):
    name = "mp_webhook_plugin"
    def setup(self, app):
        app.include_router(router)

plugin = MpWebhookPlugin()
