"""Plugin: API Pay-per-use com creditos"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel
from plugins.db_manager import SimpleDB
import os, logging, secrets
from datetime import datetime

logger   = logging.getLogger(__name__)
router   = APIRouter(prefix="/api/v1/credits", tags=["Monetizacao"])
_credits = SimpleDB("api_credits")
BASE     = os.getenv("BASE_URL", "https://emotion-platform-albert.onrender.com")
SK       = os.getenv("STRIPE_SECRET_KEY", "")

PACOTES = {
    "trial":    {"credits": 10,   "preco": 0,    "descricao": "10 chamadas gratis"},
    "starter":  {"credits": 100,  "preco": 990,  "descricao": "100 chamadas API"},
    "pro":      {"credits": 500,  "preco": 3990, "descricao": "500 chamadas API"},
    "business": {"credits": 2000, "preco": 9990, "descricao": "2000 chamadas API"},
}

def gerar_key():
    return "ek_" + secrets.token_urlsafe(24)

class KeyReq(BaseModel):
    email:  str
    pacote: str = "trial"

@router.post("/gerar-key")
async def gerar(req: KeyReq):
    p = PACOTES.get(req.pacote, PACOTES["trial"])
    if p["preco"] == 0:
        key = gerar_key()
        _credits.set(key, {"email": req.email, "credits": p["credits"],
                           "pacote": req.pacote, "criado": datetime.now().isoformat()})
        return {"api_key": key, "credits": p["credits"],
                "msg": f"Trial com {p['credits']} creditos gratis!",
                "como_usar": "Header: X-API-Key: " + key}
    if not SK:
        raise HTTPException(503, "Stripe nao configurado")
    try:
        import stripe
        stripe.api_key = SK
        key = gerar_key()
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            customer_email=req.email,
            line_items=[{"price_data": {"currency": "brl", "unit_amount": p["preco"],
                "product_data": {"name": f"API Credits — {p['descricao']}"}}, "quantity": 1}],
            mode="payment",
            success_url=BASE + f"/api/v1/credits/ativar?email={req.email}&pacote={req.pacote}&key={key}",
            cancel_url=BASE + "/api/v1/credits/planos",
        )
        return {"checkout_url": session.url, "pacote": req.pacote,
                "credits": p["credits"], "preco": f"R$ {p['preco']/100:.2f}"}
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get("/ativar")
async def ativar(email: str, pacote: str, key: str):
    p = PACOTES.get(pacote, PACOTES["starter"])
    _credits.set(key, {"email": email, "credits": p["credits"],
                       "pacote": pacote, "criado": datetime.now().isoformat()})
    return {"api_key": key, "credits": p["credits"], "msg": "Ativado!"}

@router.get("/saldo")
async def saldo(x_api_key: str = Header(...)):
    data = _credits.get(x_api_key)
    if not data:
        raise HTTPException(401, "API Key invalida")
    return {"email": data.get("email"), "credits": data.get("credits", 0),
            "pacote": data.get("pacote")}

@router.get("/planos")
async def planos():
    return {"planos": [{"id": k, "credits": v["credits"],
                        "preco": f"R$ {v['preco']/100:.2f}" if v["preco"] > 0 else "Gratis",
                        "descricao": v["descricao"]} for k, v in PACOTES.items()]}

@router.get("/status")
async def status():
    return {"status": "online", "modelo": "pay-per-use",
            "preco_por_chamada": "R$ 0,10", "trial": "10 creditos gratis"}

class APICreditsPlugin(PluginBase):
    name = "api_credits"
    version = "1.0.0"
    description = "API Pay-per-use com creditos"
    category = "monetizacao_real"
    def setup(self, app):
        app.include_router(router)
        logger.info("[APICredits] OK")
    def health_check(self):
        return {"status": "healthy"}

plugin = APICreditsPlugin()
