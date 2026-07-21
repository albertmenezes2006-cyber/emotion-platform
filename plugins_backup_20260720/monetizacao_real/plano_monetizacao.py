
from plugins.plugin_base import PluginBase
from fastapi import APIRouter
import os, logging
logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/monetizacao", tags=["Monetizacao"])
BASE = os.getenv("BASE_URL","https://emotion-platform-albert.onrender.com")

@router.get("/plano")
async def plano():
    return {
        "metas":{"mrr_6m":"R$ 5.000","clientes":200,"cac":"R$ 50","ltv":"R$ 360"},
        "receitas":{
            "saas":{"descricao":"Planos mensais Free/Pro/Clinica/Enterprise","meta":"R$ 3.000/mes"},
            "api":{"descricao":"Pay-per-use R$ 0,05-0,10 por chamada","meta":"R$ 1.000/mes"},
            "white_label":{"descricao":"Plataforma com marca do cliente","meta":"R$ 5.000/cliente"},
            "relatorios":{"descricao":"PDF clinico R$ 19,90 por relatorio","meta":"R$ 500/mes"},
            "afiliados":{"descricao":"30% comissao para psicologos parceiros","meta":"R$ 1.000/mes"},
            "cursos":{"descricao":"Certificacoes IA + saude mental R$ 197-997","meta":"R$ 2.000/mes"},
        }
    }

@router.get("/acoes")
async def acoes():
    return {
        "hoje":[
            {"acao":"Criar conta Stripe","link":"https://stripe.com","tempo":"30 min"},
            {"acao":"Google Analytics 4","link":"https://analytics.google.com","tempo":"15 min"},
            {"acao":"UptimeRobot","link":"https://uptimerobot.com","tempo":"10 min"},
        ],
        "semana":[
            {"acao":"Dominio proprio","link":"https://registro.br","custo":"R$ 40/ano"},
            {"acao":"Lancar Product Hunt","link":"https://producthunt.com","tempo":"2h"},
            {"acao":"Post LinkedIn","link":"https://linkedin.com","tempo":"30 min"},
        ],
        "mes":[
            {"acao":"10 clientes beta","meta":"feedback real"},
            {"acao":"Primeira receita","meta":"R$ 500 MRR"},
        ]
    }

@router.get("/status")
async def status():
    return {"status":"online",
            "stripe_ativo":bool(os.getenv("STRIPE_SECRET_KEY","")),
            "analytics_ativo":bool(os.getenv("GA4_ID","")),
            "links":{"stripe_guia":BASE+"/api/v1/stripe-setup/guia","acoes":BASE+"/api/v1/monetizacao/acoes"}}

class PlanoMonetizacaoPlugin(PluginBase):
    name="plano_monetizacao"; version="1.0.0"; description="Plano monetizacao"; category="monetizacao_real"
    def setup(self,app): app.include_router(router); logger.info("[Monetizacao] OK")
    def health_check(self): return {"status":"healthy"}

plugin = PlanoMonetizacaoPlugin()
