"""
Plugin: Mobile API — Endpoints otimizados para React Native / Flutter
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException, Header
from datetime import datetime
from plugins.db_manager import SimpleDB
import uuid, json, logging, os

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/mobile/v1", tags=["mobile_api"])

_sessions_mobile = SimpleDB("mobile_sessions")
_push_tokens = SimpleDB("mobile_push_tokens")

class MobileEndpointsPlugin(PluginBase):
    name = "mobile_endpoints"; version = "2.0.0"
    description = "APIs otimizadas para React Native e Flutter"; category = "mobile_api"
    def setup(self, app): app.include_router(router); logger.info("[mobile_endpoints] OK")
    def health_check(self): return {"status":"healthy","push_tokens":_push_tokens.count()}

@router.get("/init")
async def init_mobile(
    platform: str = "ios",
    app_version: str = "1.0.0",
    device_id: str = ""
):
    """Inicialização do app mobile — retorna config completa"""
    return {
        "status": "ok",
        "plataforma": platform,
        "app_version": app_version,
        "api_version": "v1",
        "base_url": os.getenv("BASE_URL", "https://emotion-platform-albert.onrender.com"),
        "features": {
            "chat_ia": True,
            "avaliacao_phq9": True,
            "avaliacao_gad7": True,
            "diario_emocional": True,
            "agenda": True,
            "prontuario": True,
            "push_notifications": True,
            "biometria": True,
            "offline_mode": False
        },
        "config": {
            "chat_max_chars": 500,
            "diario_max_chars": 2000,
            "timeout_ms": 30000,
            "retry_attempts": 3
        },
        "links": {
            "termos": "/termos",
            "privacidade": "/privacidade",
            "suporte": "mailto:albertmenezes2006@gmail.com"
        },
        "ts": datetime.utcnow().isoformat()
    }

@router.post("/push/registrar")
async def registrar_push_token(user_id: str, token: str, platform: str = "ios"):
    """Registra token de push notification"""
    _push_tokens.create(nome=f"Push {user_id}", user_id=user_id,
                        valor=token, categoria=platform,
                        dados=json.dumps({"token":token,"platform":platform,
                                         "ts":datetime.utcnow().isoformat()}))
    return {"status": "token registrado", "platform": platform}

@router.get("/home/{user_id}")
async def home_mobile(user_id: str):
    """Tela home do app — dados consolidados"""
    hora = datetime.utcnow().hour
    saudacao = "Bom dia" if hora < 12 else "Boa tarde" if hora < 18 else "Boa noite"

    return {
        "saudacao": saudacao,
        "user_id": user_id,
        "widgets": [
            {
                "tipo": "humor_rapido",
                "titulo": "Como você está?",
                "subtitulo": "Registre seu humor agora",
                "acao": "/app/diario",
                "cor": "#6C63FF"
            },
            {
                "tipo": "avaliacao",
                "titulo": "Avaliação Rápida",
                "subtitulo": "PHQ-9 em 3 minutos",
                "acao": "/app/avaliacao",
                "cor": "#FF6584"
            },
            {
                "tipo": "chat",
                "titulo": "Chat com IA",
                "subtitulo": "Suporte emocional 24/7",
                "acao": "/app/chat",
                "cor": "#43D787"
            }
        ],
        "dica_do_dia": _dica_do_dia(),
        "streak_dias": 1,
        "ts": datetime.utcnow().isoformat()
    }

@router.post("/humor/rapido")
async def registrar_humor_rapido(user_id: str, humor: int, emocao: str = "neutro"):
    """Registro rápido de humor (widget home do app)"""
    if not 1 <= humor <= 10:
        raise HTTPException(400, "Humor deve ser entre 1 e 10")
    return {
        "status": "registrado",
        "humor": humor,
        "emocao": emocao,
        "mensagem": "Continue assim! 🌟" if humor >= 7 else "Estamos aqui por você 💙",
        "ts": datetime.utcnow().isoformat()
    }

@router.get("/feed/{user_id}")
async def feed_mobile(user_id: str, page: int = 1, limit: int = 20):
    """Feed de conteúdo personalizado para o app"""
    conteudos = [
        {"id":"1","tipo":"dica","titulo":"Respiração 4-7-8","desc":"Inspire 4s, segure 7s, expire 8s para reduzir ansiedade","emoji":"🌬️","leitura_min":2},
        {"id":"2","tipo":"artigo","titulo":"Por que o sono importa","desc":"Sono e saúde mental: conexões essenciais","emoji":"😴","leitura_min":5},
        {"id":"3","tipo":"exercicio","titulo":"Mindfulness de 5 min","desc":"Técnica rápida de atenção plena","emoji":"🧘","leitura_min":5},
        {"id":"4","tipo":"avaliacao","titulo":"Você fez sua avaliação semanal?","desc":"PHQ-9 + GAD-7 — 5 minutos","emoji":"📊","leitura_min":3},
        {"id":"5","tipo":"video","titulo":"TCC: reestruturação cognitiva","desc":"Aprenda a identificar pensamentos automáticos","emoji":"🎥","leitura_min":10},
    ]
    start = (page-1)*limit
    return {
        "page": page,
        "total": len(conteudos),
        "items": conteudos[start:start+limit],
        "has_more": start+limit < len(conteudos)
    }

@router.get("/notificacoes/{user_id}")
async def notificacoes_mobile(user_id: str):
    """Lista notificações do usuário"""
    return {
        "total": 2,
        "nao_lidas": 1,
        "notificacoes": [
            {"id":"1","titulo":"Hora da sua avaliação semanal","corpo":"Faça seu PHQ-9 de hoje","lida":False,"ts":datetime.utcnow().isoformat(),"tipo":"avaliacao"},
            {"id":"2","titulo":"Dica do dia","corpo":"Pratique gratidão: anote 3 coisas boas de hoje","lida":True,"ts":datetime.utcnow().isoformat(),"tipo":"dica"},
        ]
    }

@router.get("/sdk/config")
async def sdk_config():
    """Configuração para SDK React Native / Flutter"""
    base = os.getenv("BASE_URL","https://emotion-platform-albert.onrender.com")
    return {
        "base_url": base,
        "endpoints": {
            "auth_login": f"{base}/api/v1/auth/login",
            "auth_cadastro": f"{base}/api/v1/auth/cadastrar",
            "auth_me": f"{base}/api/v1/auth/me",
            "chat": f"{base}/api/v1/chat-ia/mensagem",
            "phq9_perguntas": f"{base}/api/v1/phq9/perguntas",
            "phq9_aplicar": f"{base}/api/v1/phq9/aplicar",
            "gad7_perguntas": f"{base}/api/v1/gad7/perguntas",
            "gad7_aplicar": f"{base}/api/v1/gad7/aplicar",
            "diario_entrada": f"{base}/api/v1/diario-emocional/entrada",
            "diario_historico": f"{base}/api/v1/diario-emocional/historico",
            "agenda_agendar": f"{base}/api/v1/agenda-real/sessao/agendar",
            "mobile_home": f"{base}/api/mobile/v1/home",
            "mobile_feed": f"{base}/api/mobile/v1/feed",
            "planos": f"{base}/api/v1/stripe/planos",
        },
        "versao_api": "2.0.0",
        "docs": f"{base}/docs"
    }

def _dica_do_dia() -> dict:
    from datetime import date
    dicas = [
        {"titulo":"Respiração 4-7-8","texto":"Inspire 4s → Segure 7s → Expire 8s. Repita 4x.","emoji":"🌬️"},
        {"titulo":"Gratidão","texto":"Anote 3 coisas pelas quais você é grato hoje.","emoji":"🙏"},
        {"titulo":"Movimento","texto":"10 minutos de caminhada melhora o humor em até 30%.","emoji":"🚶"},
        {"titulo":"Hidratação","texto":"Desidratação leve afeta cognição e humor. Beba água!","emoji":"💧"},
        {"titulo":"Sono","texto":"Durma 7-9h. O sono consolida memórias e regula emoções.","emoji":"😴"},
        {"titulo":"Conexão","texto":"Fale com alguém de confiança. Conexão social protege a saúde mental.","emoji":"❤️"},
        {"titulo":"Mindfulness","texto":"Pause. Respire. Observe o momento presente sem julgamento.","emoji":"🧘"},
    ]
    idx = date.today().toordinal() % len(dicas)
    return dicas[idx]

plugin = MobileEndpointsPlugin()
