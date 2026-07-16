"""Plugin: Diário Emocional Real — com análise e persistência"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
from plugins.db_manager import SimpleDB
import uuid, json, logging, re

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/diario-emocional", tags=["autocuidado"])

_entradas = SimpleDB("diario_emocional")

EMOCOES = {
    "alegria": {"valencia": 0.9, "cor": "#FFD700", "emoji": "😊"},
    "gratidao": {"valencia": 0.85, "cor": "#90EE90", "emoji": "🙏"},
    "serenidade": {"valencia": 0.8, "cor": "#87CEEB", "emoji": "😌"},
    "interesse": {"valencia": 0.7, "cor": "#FFA500", "emoji": "🤔"},
    "esperanca": {"valencia": 0.75, "cor": "#98FB98", "emoji": "🌱"},
    "neutro": {"valencia": 0.5, "cor": "#C0C0C0", "emoji": "😐"},
    "ansiedade": {"valencia": 0.25, "cor": "#FFB347", "emoji": "😰"},
    "tristeza": {"valencia": 0.2, "cor": "#6495ED", "emoji": "😢"},
    "raiva": {"valencia": 0.15, "cor": "#FF6347", "emoji": "😠"},
    "medo": {"valencia": 0.1, "cor": "#9370DB", "emoji": "😨"},
    "desespero": {"valencia": 0.05, "cor": "#8B0000", "emoji": "😱"},
}

class DiarioRealPlugin(PluginBase):
    name = "diario_real"; version = "2.0.0"
    description = "Diário emocional com análise e persistência real"; category = "autocuidado"
    def setup(self, app): app.include_router(router); logger.info("[diario_real] OK")
    def health_check(self): return {"status": "healthy", "entradas": _entradas.count()}

@router.post("/entrada")
async def criar_entrada(
    user_id: str,
    texto: str,
    emocao_principal: str = "neutro",
    intensidade: float = 5.0,
    humor_geral: float = 5.0,
    tags: str = "",
    privado: bool = True
):
    if not texto or len(texto.strip()) < 3:
        raise HTTPException(400, "Texto muito curto")
    if emocao_principal not in EMOCOES:
        emocao_principal = "neutro"
    intensidade = max(0.0, min(10.0, intensidade))
    humor_geral = max(0.0, min(10.0, humor_geral))

    emocao_info = EMOCOES[emocao_principal]
    palavras = len(texto.split())

    # Análise simples de sentimento
    pos_words = ["feliz", "amor", "grato", "alegre", "bem", "ótimo", "paz", "esperança"]
    neg_words = ["triste", "ansioso", "medo", "raiva", "ruim", "horrível", "sozinho"]
    texto_lower = texto.lower()
    score_pos = sum(1 for w in pos_words if w in texto_lower)
    score_neg = sum(1 for w in neg_words if w in texto_lower)
    sentimento_texto = "positivo" if score_pos > score_neg else "negativo" if score_neg > score_pos else "neutro"

    entrada = {
        "id": str(uuid.uuid4())[:8],
        "user_id": user_id,
        "texto": texto[:2000],
        "emocao_principal": emocao_principal,
        "emocao_emoji": emocao_info["emoji"],
        "emocao_cor": emocao_info["cor"],
        "intensidade": intensidade,
        "humor_geral": humor_geral,
        "valencia": emocao_info["valencia"],
        "tags": [t.strip() for t in tags.split(",") if t.strip()],
        "palavras": palavras,
        "sentimento_detectado": sentimento_texto,
        "privado": privado,
        "data": datetime.utcnow().isoformat()
    }

    _entradas.create(
        nome=f"Diário {user_id}",
        user_id=user_id,
        valor=emocao_principal,
        dados=json.dumps(entrada),
        categoria=emocao_principal
    )

    return {
        "status": "entrada registrada",
        "entrada": entrada,
        "insight": _gerar_insight(emocao_principal, intensidade, humor_geral)
    }

@router.get("/historico/{user_id}")
async def historico(user_id: str, limite: int = 30):
    entradas_raw = _entradas.list(user_id=user_id, limite=limite)
    entradas = []
    for e in entradas_raw:
        try:
            dados = json.loads(e.get("dados", "{}"))
            entradas.append(dados)
        except Exception:
            pass

    if entradas:
        valencias = [e.get("valencia", 0.5) for e in entradas]
        media_valencia = sum(valencias) / len(valencias)
        humores = [e.get("humor_geral", 5) for e in entradas]
        media_humor = sum(humores) / len(humores)
        emocoes_count = {}
        for e in entradas:
            em = e.get("emocao_principal", "neutro")
            emocoes_count[em] = emocoes_count.get(em, 0) + 1
        emocao_freq = max(emocoes_count, key=emocoes_count.get)
    else:
        media_valencia = 0.5
        media_humor = 5.0
        emocoes_count = {}
        emocao_freq = "neutro"

    return {
        "user_id": user_id,
        "total_entradas": len(entradas),
        "periodo": f"{limite} mais recentes",
        "resumo": {
            "media_valencia": round(media_valencia, 3),
            "media_humor": round(media_humor, 2),
            "emocao_mais_frequente": emocao_freq,
            "distribuicao_emocoes": emocoes_count,
            "bem_estar_geral": "positivo" if media_valencia > 0.6 else "negativo" if media_valencia < 0.4 else "neutro"
        },
        "entradas": entradas
    }

@router.get("/emocoes/disponiveis")
async def emocoes():
    return {"emocoes": EMOCOES}

@router.get("/insight/{user_id}")
async def insight_semanal(user_id: str):
    entradas_raw = _entradas.list(user_id=user_id, limite=7)
    if not entradas_raw:
        return {"user_id": user_id, "insight": "Comece registrando suas emoções diariamente!"}
    return {
        "user_id": user_id,
        "periodo": "últimos 7 registros",
        "insight": "Seu padrão emocional está sendo monitorado. Continue registrando!",
        "recomendacoes": [
            "Pratique mindfulness por 10 minutos ao dia",
            "Identifique seus gatilhos emocionais",
            "Celebre suas pequenas conquistas"
        ]
    }

def _gerar_insight(emocao: str, intensidade: float, humor: float) -> str:
    if emocao in ["alegria", "gratidao", "serenidade"] and humor >= 7:
        return "Você está num momento positivo. Continue cultivando essas emoções! 🌟"
    elif emocao in ["ansiedade", "medo"] and intensidade >= 7:
        return "Ansiedade intensa detectada. Tente respiração 4-7-8 agora. 🧘"
    elif emocao in ["tristeza", "desespero"]:
        return "Momento difícil. Lembre: é temporário. Considere contato com seu terapeuta. 💙"
    elif emocao == "raiva" and intensidade >= 6:
        return "Raiva elevada. Técnica: conte até 10 antes de agir. 🌬️"
    else:
        return "Obrigado por registrar. A autoconsciência é o primeiro passo! 📝"

plugin = DiarioRealPlugin()
