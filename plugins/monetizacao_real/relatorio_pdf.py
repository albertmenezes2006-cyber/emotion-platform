"""Plugin: Relatorio PDF Pago R$19,90"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
import os, logging
from datetime import datetime

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/relatorio-pdf", tags=["Monetizacao"])
BASE   = os.getenv("BASE_URL", "https://emotion-platform-albert.onrender.com")
SK     = os.getenv("STRIPE_SECRET_KEY", "")

class RelatorioPedido(BaseModel):
    user_id:    str = "anonimo"
    email:      str
    nome:       str = "Paciente"
    phq9_score: int = 0
    gad7_score: int = 0

def nivel_phq9(s):
    if s <= 4:  return "Minimo"
    if s <= 9:  return "Leve"
    if s <= 14: return "Moderado"
    if s <= 19: return "Moderadamente Grave"
    return "Grave"

def nivel_gad7(s):
    if s <= 4:  return "Minimo"
    if s <= 9:  return "Leve"
    if s <= 14: return "Moderado"
    return "Grave"

def gerar_html(nome, phq9, gad7):
    data = datetime.now().strftime("%d/%m/%Y")
    n9   = nivel_phq9(phq9)
    n7   = nivel_gad7(gad7)
    return f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<title>Relatorio Clinico — {nome}</title>
<style>
body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 40px; }}
.header {{ background: #7c3aed; color: white; padding: 30px; border-radius: 12px; text-align: center; margin-bottom: 30px; }}
.score-box {{ background: #f8f9fa; border-radius: 12px; padding: 20px; margin: 20px 0; border-left: 5px solid #7c3aed; }}
.score {{ font-size: 48px; font-weight: bold; color: #7c3aed; }}
.nivel {{ font-size: 20px; color: #333; margin: 10px 0; }}
.rec {{ background: #e8f5e9; border-radius: 8px; padding: 15px; margin: 10px 0; }}
.footer {{ text-align: center; color: #666; font-size: 12px; margin-top: 40px; border-top: 1px solid #ddd; padding-top: 20px; }}
</style></head><body>
<div class="header">
  <h1>Emotion Intelligence Platform</h1>
  <h2>Relatorio Clinico de Avaliacao Emocional</h2>
  <p>Paciente: {nome} | Data: {data}</p>
</div>
<h2>Avaliacao PHQ-9 — Depressao</h2>
<div class="score-box">
  <div class="score">{phq9}/27</div>
  <div class="nivel">Nivel: <strong>{n9}</strong></div>
  <p>PHQ-9 e uma ferramenta validada para rastreamento de depressao.</p>
</div>
<h2>Avaliacao GAD-7 — Ansiedade</h2>
<div class="score-box">
  <div class="score">{gad7}/21</div>
  <div class="nivel">Nivel: <strong>{n7}</strong></div>
  <p>GAD-7 e uma ferramenta validada para rastreamento de ansiedade.</p>
</div>
<h2>Recomendacoes</h2>
<div class="rec">Consulte um profissional de saude mental para interpretacao completa.</div>
<div class="rec">Mantenha um diario emocional para acompanhar seu progresso.</div>
<div class="rec">Pratique tecnicas de mindfulness e respiracao diariamente.</div>
<div class="footer">
  <p>Emotion Intelligence Platform — {BASE}</p>
  <p>Este relatorio e informativo e nao substitui avaliacao clinica profissional.</p>
</div>
</body></html>"""

@router.get("/preview", response_class=HTMLResponse)
async def preview(phq9: int = 7, gad7: int = 5, nome: str = "Paciente Teste"):
    return HTMLResponse(gerar_html(nome, phq9, gad7))

@router.post("/gerar")
async def gerar(req: RelatorioPedido):
    if not SK:
        return {"msg": "Stripe nao configurado", "preview": BASE + "/api/v1/relatorio-pdf/preview"}
    try:
        import stripe
        stripe.api_key = SK
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            customer_email=req.email,
            line_items=[{"price_data": {
                "currency": "brl",
                "unit_amount": 1990,
                "product_data": {"name": "Relatorio PDF Clinico PHQ-9 + GAD-7"}
            }, "quantity": 1}],
            mode="payment",
            success_url=BASE + "/api/v1/relatorio-pdf/preview?nome=" + req.nome + "&phq9=" + str(req.phq9_score) + "&gad7=" + str(req.gad7_score),
            cancel_url=BASE + "/app/avaliacao",
        )
        return {"checkout_url": session.url, "preco": "R$ 19,90"}
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get("/status")
async def status():
    return {"status": "online", "preco": "R$ 19,90", "stripe_ok": bool(SK),
            "preview": BASE + "/api/v1/relatorio-pdf/preview"}

class RelatorioPDFPlugin(PluginBase):
    name = "relatorio_pdf"
    version = "1.0.0"
    description = "Relatorio PDF pago R$19,90"
    category = "monetizacao_real"
    def setup(self, app):
        app.include_router(router)
        logger.info("[RelatorioPDF] OK")
    def health_check(self):
        return {"status": "healthy", "preco": "R$19,90"}

plugin = RelatorioPDFPlugin()
