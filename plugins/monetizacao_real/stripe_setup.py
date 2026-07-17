
from plugins.plugin_base import PluginBase
from fastapi import APIRouter
import os, logging
logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/stripe-setup", tags=["Stripe Setup"])
SK = os.getenv("STRIPE_SECRET_KEY","")
BASE = os.getenv("BASE_URL","https://emotion-platform-albert.onrender.com")

@router.get("/status")
async def status():
    return {"stripe_ok":bool(SK),"status":"ativo" if SK else "falta STRIPE_SECRET_KEY",
            "planos":{"pro":{"preco":"R$ 29,90/mes","env":"STRIPE_PRICE_PRO","ok":bool(os.getenv("STRIPE_PRICE_PRO",""))},
                      "clinica":{"preco":"R$ 99,90/mes","env":"STRIPE_PRICE_CLINICA","ok":bool(os.getenv("STRIPE_PRICE_CLINICA",""))},
                      "enterprise":{"preco":"R$ 299,90/mes","env":"STRIPE_PRICE_ENTERPRISE","ok":bool(os.getenv("STRIPE_PRICE_ENTERPRISE",""))}}}

@router.get("/guia")
async def guia():
    return {"titulo":"Ativar Stripe Real","stripe":"https://stripe.com",
            "cartao_teste":"4242 4242 4242 4242","webhook":BASE+"/api/v1/stripe-checkout/webhook",
            "env_vars":["STRIPE_SECRET_KEY=sk_live_xxx","STRIPE_WEBHOOK_SECRET=whsec_xxx",
                        "STRIPE_PRICE_PRO=price_xxx","STRIPE_PRICE_CLINICA=price_xxx","STRIPE_PRICE_ENTERPRISE=price_xxx"]}

class StripeSetupPlugin(PluginBase):
    name="stripe_setup"; version="1.0.0"; description="Guia Stripe"; category="monetizacao_real"
    def setup(self,app): app.include_router(router); logger.info("[StripeSetup] OK")
    def health_check(self): return {"status":"healthy","stripe_ok":bool(SK)}

plugin = StripeSetupPlugin()
