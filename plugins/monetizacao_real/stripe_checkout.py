"""
Plugin: Stripe Checkout Real — 4 planos com checkout funcional
Padrão: PluginBase + plugin = StripeCheckoutPlugin()
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
import os, logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/stripe-checkout", tags=["stripe_checkout"])

STRIPE_SECRET  = os.getenv("STRIPE_SECRET_KEY", "")
STRIPE_WEBHOOK = os.getenv("STRIPE_WEBHOOK_SECRET", "")
BASE_URL       = os.getenv("BASE_URL", "https://emotion-platform-albert.onrender.com")

PLANOS = {
    "free":       {"nome": "Free",       "preco": 0,     "features": ["5 avaliações/mês", "Chat básico"],                                    "price_id": ""},
    "pro":        {"nome": "Pro",        "preco": 2990,  "features": ["Avaliações ilimitadas", "Chat IA avançado", "Relatórios PDF"],         "price_id": os.getenv("STRIPE_PRICE_PRO", "")},
    "clinica":    {"nome": "Clínica",    "preco": 9990,  "features": ["Tudo do Pro", "Multi-pacientes", "API acesso", "LGPD compliant"],      "price_id": os.getenv("STRIPE_PRICE_CLINICA", "")},
    "enterprise": {"nome": "Enterprise", "preco": 29990, "features": ["Tudo da Clínica", "White-label", "SLA 99.9%", "Onboarding dedicado"], "price_id": os.getenv("STRIPE_PRICE_ENTERPRISE", "")},
}

class CheckoutReq(BaseModel):
    plano: str
    email: str

@router.get("/planos")
async def listar_planos():
    return {"planos": [
        {"id": k, "nome": v["nome"],
         "preco_centavos": v["preco"],
         "preco_display": f"R$ {v['preco']/100:.2f}".replace(".",",") if v["preco"] > 0 else "Grátis",
         "features": v["features"],
         "stripe_configurado": bool(v["price_id"])}
        for k, v in PLANOS.items()
    ]}

@router.post("/checkout")
async def criar_checkout(req: CheckoutReq):
    if req.plano == "free":
        return {"url": f"{BASE_URL}/app/dashboard", "plano": "free", "msg": "Plano gratuito ativado!"}
    if not STRIPE_SECRET:
        raise HTTPException(503, "Stripe não configurado. Adicione STRIPE_SECRET_KEY no Render.")
    plano = PLANOS.get(req.plano)
    if not plano:
        raise HTTPException(404, f"Plano '{req.plano}' não encontrado")
    if not plano["price_id"]:
        raise HTTPException(503, f"Price ID do plano '{req.plano}' não configurado no Render")
    try:
        import stripe
        stripe.api_key = STRIPE_SECRET
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            customer_email=req.email,
            line_items=[{"price": plano["price_id"], "quantity": 1}],
            mode="subscription",
            success_url=f"{BASE_URL}/app/dashboard?plano={req.plano}&success=1",
            cancel_url=f"{BASE_URL}/app/planos?cancelled=1",
            metadata={"plano": req.plano, "email": req.email}
        )
        return {"url": session.url, "session_id": session.id, "plano": req.plano}
    except Exception as e:
        raise HTTPException(500, f"Erro Stripe: {e}")

@router.post("/webhook")
async def stripe_webhook(request: Request):
    if not STRIPE_WEBHOOK:
        return {"status": "webhook_secret_nao_configurado"}
    payload = await request.body()
    sig = request.headers.get("stripe-signature", "")
    try:
        import stripe
        stripe.api_key = STRIPE_SECRET
        event = stripe.Webhook.construct_event(payload, sig, STRIPE_WEBHOOK)
    except Exception as e:
        raise HTTPException(400, str(e))
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        email   = session.get("customer_email", "")
        plano   = session.get("metadata", {}).get("plano", "pro")
        logger.info(f"[Stripe] ✅ Pagamento confirmado: {email} → {plano}")
    return {"status": "ok", "event": event["type"]}

@router.get("/configuracao")
async def config_status():
    return {
        "stripe_secret":    "✅ configurado" if STRIPE_SECRET  else "❌ falta STRIPE_SECRET_KEY",
        "stripe_webhook":   "✅ configurado" if STRIPE_WEBHOOK else "❌ falta STRIPE_WEBHOOK_SECRET",
        "price_pro":        "✅" if PLANOS["pro"]["price_id"]        else "❌ falta STRIPE_PRICE_PRO",
        "price_clinica":    "✅" if PLANOS["clinica"]["price_id"]    else "❌ falta STRIPE_PRICE_CLINICA",
        "price_enterprise": "✅" if PLANOS["enterprise"]["price_id"] else "❌ falta STRIPE_PRICE_ENTERPRISE",
        "dica": "Configure as env vars no painel do Render"
    }

class StripeCheckoutPlugin(PluginBase):
    name        = "stripe_checkout"
    version     = "2.0.0"
    description = "Stripe Checkout com 4 planos reais"
    category    = "monetizacao_real"

    def setup(self, app):
        app.include_router(router)
        logger.info("[stripe_checkout] ✅ OK")

    def health_check(self):
        return {"status": "healthy", "plugin": self.name,
                "stripe_configurado": bool(STRIPE_SECRET)}

plugin = StripeCheckoutPlugin()
