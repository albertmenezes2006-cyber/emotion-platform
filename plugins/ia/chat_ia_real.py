"""Plugin: Chat IA Real — Groq + Gemini + fallback inteligente"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
from plugins.db_manager import SimpleDB
import os, uuid, json, logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/chat-ia", tags=["ia"])
_conversas = SimpleDB("chat_ia_v2")

SYSTEM = (
    "Voce e um assistente de saude mental empatico. "
    "Responda em portugues brasileiro. "
    "Use tecnicas de TCC, DBT e Mindfulness. "
    "Em crises: indique CVV 188 e SAMU 192. "
    "Maximo 250 palavras por resposta. "
    "NAO substitua profissionais de saude mental."
)

CRISIS_WORDS = [
    "suicidio", "suicídio", "me matar", "não quero viver",
    "nao quero viver", "acabar com tudo", "me machucar"
]

FALLBACKS = {
    "ansio": "Entendo que voce esta sentindo ansiedade. Tente a respiracao 4-7-8:\n\n1. Expire completamente\n2. Inspire pelo nariz por 4 segundos\n3. Segure por 7 segundos\n4. Expire pela boca por 8 segundos\n\nRepita 4 vezes. Isso ativa o sistema nervoso parassimpatico e reduz a ansiedade. Como esta se sentindo?",
    "trist": "Sinto muito que voce esta passando por isso. A tristeza e uma emocao valida e temporaria. Voce nao precisa enfrentar isso sozinho. Me conta mais: o que esta acontecendo?",
    "dormir": "Problemas de sono sao muito comuns. Dicas baseadas em evidencias:\n• Evite telas 1h antes de dormir\n• Mantenha horario fixo\n• Quarto escuro e fresco (18-20 graus)\n• Tecnica de relaxamento muscular progressivo\n\nO que passa pela sua cabeca quando tenta dormir?",
    "respiracao": "Tecnica 4-7-8:\n1. Expire completamente\n2. Inspire pelo nariz: 4 segundos\n3. Segure: 7 segundos\n4. Expire pela boca: 8 segundos\nRepita 4 vezes. Quer tentar agora?",
    "mindf": "Mindfulness em 5 minutos:\n1. Sente-se confortavelmente\n2. Feche os olhos\n3. Foque na respiracao\n4. Quando pensamentos vierem, observe e volte\n5. Sem julgamentos\n\nComecar com 5 min por dia ja traz beneficios. Quer que eu te guie?",
    "default": "Estou aqui para te ouvir. Me conta mais sobre o que esta sentindo? Quanto mais compartilhar, melhor posso te ajudar."
}


class ChatIaRealPlugin(PluginBase):
    name = "chat_ia_real"
    version = "3.0.0"
    description = "Chat IA com Groq, Gemini e fallback inteligente"
    category = "ia"

    def setup(self, app):
        app.include_router(router)
        groq_ok = bool(os.getenv("GROQ_API_KEY"))
        gemini_ok = bool(os.getenv("GEMINI_API_KEY"))
        mistral_ok = bool(os.getenv("MISTRAL_API_KEY"))
        logger.info(f"[chat_ia_real] OK — Groq:{groq_ok} Gemini:{gemini_ok} Mistral:{mistral_ok}")

    def health_check(self):
        return {
            "status": "healthy",
            "groq": bool(os.getenv("GROQ_API_KEY")),
            "gemini": bool(os.getenv("GEMINI_API_KEY")),
            "mistral": bool(os.getenv("MISTRAL_API_KEY")),
            "conversas": _conversas.count()
        }


@router.get("/modelos/disponiveis")
async def modelos_disponiveis():
    return {"modelos": [
        {"id":"groq","nome":"Groq LLaMA3","disponivel":bool(os.getenv("GROQ_API_KEY")),"velocidade":"muito_rapida"},
        {"id":"gemini","nome":"Google Gemini","disponivel":bool(os.getenv("GEMINI_API_KEY")),"velocidade":"rapida"},
        {"id":"mistral","nome":"Mistral","disponivel":bool(os.getenv("MISTRAL_API_KEY")),"velocidade":"rapida"},
        {"id":"openrouter","nome":"OpenRouter","disponivel":bool(os.getenv("OPENROUTER_API_KEY")),"velocidade":"variavel"},
        {"id":"fallback","nome":"Respostas base","disponivel":True,"velocidade":"instantanea"},
    ]}


async def _chamar_groq(mensagem: str) -> str:
    import httpx
    key = os.getenv("GROQ_API_KEY","")
    if not key:
        return ""
    msgs = [
        {"role":"system","content":SYSTEM},
        {"role":"user","content":mensagem}
    ]
    try:
        async with httpx.AsyncClient(timeout=20) as c:
            r = await c.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={"Authorization": "Bearer " + key},
                json={"model":"llama3-8b-8192","messages":msgs,"max_tokens":350,"temperature":0.7}
            )
            if r.status_code == 200:
                return r.json()["choices"][0]["message"]["content"]
            else:
                logger.warning(f"Groq status {r.status_code}: {r.text[:100]}")
    except Exception as e:
        logger.warning(f"Groq error: {e}")
    return ""


async def _chamar_gemini(mensagem: str) -> str:
    import httpx
    key = os.getenv("GEMINI_API_KEY","")
    if not key:
        return ""
    prompt = SYSTEM + "\n\nUsuario: " + mensagem
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=" + key
    try:
        async with httpx.AsyncClient(timeout=20) as c:
            r = await c.post(url, json={
                "contents":[{"parts":[{"text":prompt}]}],
                "generationConfig":{"maxOutputTokens":350,"temperature":0.7}
            })
            if r.status_code == 200:
                return r.json()["candidates"][0]["content"]["parts"][0]["text"]
            else:
                logger.warning(f"Gemini status {r.status_code}: {r.text[:100]}")
    except Exception as e:
        logger.warning(f"Gemini error: {e}")
    return ""


async def _chamar_mistral(mensagem: str) -> str:
    import httpx
    key = os.getenv("MISTRAL_API_KEY","")
    if not key:
        return ""
    msgs = [
        {"role":"system","content":SYSTEM},
        {"role":"user","content":mensagem}
    ]
    try:
        async with httpx.AsyncClient(timeout=20) as c:
            r = await c.post(
                "https://api.mistral.ai/v1/chat/completions",
                headers={"Authorization": "Bearer " + key},
                json={"model":"mistral-small-latest","messages":msgs,"max_tokens":350}
            )
            if r.status_code == 200:
                return r.json()["choices"][0]["message"]["content"]
            else:
                logger.warning(f"Mistral status {r.status_code}: {r.text[:100]}")
    except Exception as e:
        logger.warning(f"Mistral error: {e}")
    return ""


async def _chamar_openrouter(mensagem: str) -> str:
    import httpx
    key = os.getenv("OPENROUTER_API_KEY","")
    if not key:
        return ""
    msgs = [
        {"role":"system","content":SYSTEM},
        {"role":"user","content":mensagem}
    ]
    try:
        async with httpx.AsyncClient(timeout=25) as c:
            r = await c.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": "Bearer " + key,
                    "HTTP-Referer": "https://emotion-platform-albert.onrender.com"
                },
                json={"model":"meta-llama/llama-3.1-8b-instruct:free","messages":msgs,"max_tokens":350}
            )
            if r.status_code == 200:
                return r.json()["choices"][0]["message"]["content"]
            else:
                logger.warning(f"OpenRouter status {r.status_code}: {r.text[:100]}")
    except Exception as e:
        logger.warning(f"OpenRouter error: {e}")
    return ""


def _fallback(mensagem: str) -> str:
    baixo = mensagem.lower()
    for chave, resposta in FALLBACKS.items():
        if chave != "default" and chave in baixo:
            return resposta
    return FALLBACKS["default"]


@router.post("/mensagem")
async def enviar_mensagem(
    user_id: str = "anonimo",
    mensagem: str = "",
    historico_conversa: list = None,
    modelo: str = "auto"
):
    if not mensagem or len(mensagem.strip()) < 1:
        raise HTTPException(400, "Mensagem vazia")

    mensagem = mensagem.strip()
    resposta = None
    modelo_usado = None

    # Ordem de tentativa
    if modelo == "groq":
        ordem = ["groq"]
    elif modelo == "gemini":
        ordem = ["gemini"]
    elif modelo == "mistral":
        ordem = ["mistral"]
    elif modelo == "openrouter":
        ordem = ["openrouter"]
    else:
        # Auto: tentar todos na ordem de velocidade
        ordem = ["groq", "mistral", "gemini", "openrouter"]

    chamadas = {
        "groq": (_chamar_groq, "groq/llama3-8b"),
        "gemini": (_chamar_gemini, "gemini-1.5-flash"),
        "mistral": (_chamar_mistral, "mistral-small"),
        "openrouter": (_chamar_openrouter, "openrouter/llama3"),
    }

    for mod_id in ordem:
        if resposta:
            break
        fn, nome = chamadas[mod_id]
        try:
            texto = await fn(mensagem)
            if texto and len(texto.strip()) > 5:
                resposta = texto.strip()
                modelo_usado = nome
                logger.info(f"Chat respondido via {nome}")
        except Exception as e:
            logger.warning(f"Falha {mod_id}: {e}")

    # Fallback inteligente
    if not resposta:
        resposta = _fallback(mensagem)
        modelo_usado = "fallback"
        logger.info("Chat usando fallback inteligente")

    # Detectar crise
    is_crisis = any(w in mensagem.lower() for w in CRISIS_WORDS)
    if is_crisis:
        aviso = "🚨 EMERGENCIA: CVV 188 (24h gratuito) | SAMU 192\n\n"
        resposta = aviso + resposta
        logger.warning(f"CRISE DETECTADA user={user_id}: {mensagem[:80]}")

    # Salvar conversa
    try:
        _conversas.create(
            nome="Chat " + user_id,
            user_id=user_id,
            valor=modelo_usado or "?",
            dados=json.dumps({
                "msg": mensagem[:200],
                "resp": resposta[:200],
                "modelo": modelo_usado,
                "crise": is_crisis
            }),
            categoria="crise" if is_crisis else "normal"
        )
    except Exception:
        pass

    return {
        "conversa_id": str(uuid.uuid4())[:8],
        "user_id": user_id,
        "mensagem": mensagem,
        "resposta": resposta,
        "modelo_usado": modelo_usado,
        "alerta_crise": is_crisis,
        "timestamp": datetime.utcnow().isoformat(),
        "recursos_emergencia": {"cvv": "188", "samu": "192"} if is_crisis else None
    }


@router.get("/historico/{user_id}")
async def historico(user_id: str, limite: int = 20):
    convs = _conversas.list(user_id=user_id, limite=limite)
    return {"total": len(convs), "conversas": convs}


plugin = ChatIaRealPlugin()
