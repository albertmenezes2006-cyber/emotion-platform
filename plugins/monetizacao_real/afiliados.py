"""Plugin: Programa de Afiliados 30% comissao"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from plugins.db_manager import SimpleDB
import os, logging, secrets
from datetime import datetime

logger     = logging.getLogger(__name__)
router     = APIRouter(prefix="/api/v1/afiliados", tags=["Monetizacao"])
_afiliados = SimpleDB("afiliados")
BASE       = os.getenv("BASE_URL", "https://emotion-platform-albert.onrender.com")
COMISSAO   = 30

class AfiliadoReq(BaseModel):
    nome:      str
    email:     str
    profissao: str = "Psicologo"

@router.post("/cadastrar")
async def cadastrar(req: AfiliadoReq):
    codigo = "AF" + secrets.token_hex(4).upper()
    _afiliados.set(codigo, {
        "codigo": codigo, "nome": req.nome, "email": req.email,
        "profissao": req.profissao, "cliques": 0, "vendas": 0,
        "comissao_total": 0, "criado": datetime.now().isoformat()
    })
    link = f"{BASE}?ref={codigo}"
    return {
        "codigo": codigo,
        "link_afiliado": link,
        "comissao": f"{COMISSAO}% de cada venda",
        "ganhos_exemplo": {
            "1_pro": f"R$ {29.90 * COMISSAO / 100:.2f}/mes",
            "1_clinica": f"R$ {99.90 * COMISSAO / 100:.2f}/mes",
            "10_pro": f"R$ {29.90 * COMISSAO / 100 * 10:.2f}/mes",
        },
        "material": BASE + "/api/v1/afiliados/material/" + codigo,
        "dashboard": BASE + "/api/v1/afiliados/dashboard/" + codigo
    }

@router.get("/dashboard/{codigo}")
async def dashboard(codigo: str):
    af = _afiliados.get(codigo)
    if not af:
        raise HTTPException(404, "Afiliado nao encontrado")
    return {
        "afiliado": af.get("nome"),
        "codigo": codigo,
        "link": f"{BASE}?ref={codigo}",
        "cliques": af.get("cliques", 0),
        "vendas": af.get("vendas", 0),
        "comissao_total": f"R$ {af.get('comissao_total', 0):.2f}"
    }

@router.get("/material/{codigo}")
async def material(codigo: str):
    af = _afiliados.get(codigo)
    if not af:
        raise HTTPException(404, "Afiliado nao encontrado")
    link = f"{BASE}?ref={codigo}"
    return {
        "seu_link": link,
        "qr_code": f"https://api.qrserver.com/v1/create-qr-code/?size=256x256&data={link}&color=7c3aed",
        "textos": {
            "whatsapp": f"Conhecem essa plataforma de saude mental com IA? PHQ-9, GAD-7 gratis! {link}",
            "instagram": f"Ferramenta incrivel de saude mental com IA em PT-BR! {link}",
        },
        "comissao": f"{COMISSAO}% de cada venda pelo seu link"
    }

@router.get("/status")
async def status():
    return {"status": "online", "comissao": f"{COMISSAO}%",
            "pagamento": "mensal", "minimo_saque": "R$ 50,00",
            "cadastro": BASE + "/api/v1/afiliados/cadastrar"}

class AfiliadosPlugin(PluginBase):
    name = "afiliados"
    version = "1.0.0"
    description = f"Programa afiliados {COMISSAO}% comissao"
    category = "monetizacao_real"
    def setup(self, app):
        app.include_router(router)
        logger.info("[Afiliados] OK")
    def health_check(self):
        return {"status": "healthy", "comissao": f"{COMISSAO}%"}

plugin = AfiliadosPlugin()
