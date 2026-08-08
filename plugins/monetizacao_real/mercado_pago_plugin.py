import os
from fastapi import APIRouter, Request, HTTPException
import mercadopago

router = APIRouter(prefix="/api/v1/pagamento", tags=["Pagamentos"])

def get_sdk():
    token = os.getenv("MP_ACCESS_TOKEN")
    if not token:
        raise HTTPException(status_code=500, detail="MP_ACCESS_TOKEN nao configurado")
    return mercadopago.SDK(token)

@router.post("/pix/gerar")
async def gerar_pagamento_pix(email: str, valor: float):
    try:
        sdk = get_sdk()
        payment_data = {
            "transaction_amount": float(valor),
            "description": "Assinatura EmotionAI Pro",
            "payment_method_id": "pix",
            "payer": {"email": email}
        }
        res = sdk.payment().create(payment_data)
        if res["status"] != 201:
            raise HTTPException(status_code=400, detail="Erro ao criar pagamento")
        p = res["response"]
        return {
            "id": p["id"],
            "status": p["status"],
            "qr_code": p["point_of_interaction"]["transaction_data"]["qr_code"],
            "qr_code_base64": p["point_of_interaction"]["transaction_data"]["qr_code_base64"]
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/webhook")
async def receber_notificacao(request: Request):
    data = await request.json()
    if data.get("type") == "payment":
        payment_id = data["data"]["id"]
        sdk = get_sdk()
        res = sdk.payment().get(payment_id)
        if res["response"]["status"] == "approved":
            print(f"Pagamento {payment_id} aprovado!")
    return {"status": "ok"}

from plugins.plugin_base import PluginBase

class MercadoPagoPlugin(PluginBase):
    name = "mercado_pago_plugin"
    def setup(self, app):
        app.include_router(router)

plugin = MercadoPagoPlugin()
