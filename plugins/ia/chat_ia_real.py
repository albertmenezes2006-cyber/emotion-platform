"""Plugin: Chat IA Real — Groq + Gemini + fallback"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
from plugins.db_manager import SimpleDB
import os, uuid, json, logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/chat-ia", tags=["ia"])
_conversas = SimpleDB("chat_ia_conversas")

SYSTEM = (
    "Voce e um assistente de saude mental empatico da Emotion Intelligence Platform. "
    "Ofereca suporte emocional baseado em TCC, mindfulness e DBT. "
    "Em crises indique CVV 188 e SAMU 192. "
    "Responda em portugues brasileiro. Maximo 300 palavras. "
    "NAO substitua profissionais de saude mental."
)

class ChatIaRealPlugin(PluginBase):
    name = "chat_ia_real"; version = "2.0.0"
    description = "Chat IA com Groq e Gemini"; category = "ia"
    def setup(self, app):
        app.include_router(router)
        logger.info("[chat_ia_real] OK")
    def health_check(self):
        return {
            "status": "healthy",
            "groq": bool(os.getenv("GROQ_API_KEY")),
            "gemini": bool(os.getenv("GEMINI_API_KEY")),
            "conversas": _conversas.count()
        }

@router.get("/modelos/disponiveis")
async def modelos_disponiveis():
    return {"modelos": [
        {"id": "groq", "nome": "Groq LLaMA3", "disponivel": bool(os.getenv("GROQ_API_KEY")), "velocidade": "muito_rapida"},
        {"id": "gemini", "nome": "Google Gemini", "disponivel": bool(os.getenv("GEMINI_API_KEY")), "velocidade": "rapida"},
        {"id": "fallback", "nome": "Respostas base", "disponivel": True, "velocidade": "instantanea"},
    ]}

@router.post("/mensagem")
async def enviar_mensagem(user_id: str, mensagem: str,
                          historico_conversa: list = None, modelo: str = "auto"):
    if not mensagem or len(mensagem.strip()) < 2:
        raise HTTPException(400, "Mensagem muito curta")

    historico_conversa = historico_conversa or []
    resposta = None
    modelo_usado = None

    # Tentar Groq
    groq_key = os.getenv("GROQ_API_KEY", "")
    if groq_key and modelo in ["auto", "groq"]:
        try:
            import httpx
            msgs = [{"role": "system", "content": SYSTEM}]
            for h in historico_conversa[-6:]:
                msgs.append({"role": h.get("role", "user"), "content": h.get("content", "")})
            msgs.append({"role": "user", "content": mensagem})
            async with httpx.AsyncClient(timeout=30) as client:
                resp = await client.post(
                    "https://api.groq.com/openai/v1/chat/completions",
                    headers={"Authorization": "Bearer " + groq_key},
                    json={"model": "llama3-8b-8192", "messages": msgs,
                          "max_tokens": 400, "temperature": 0.7}
                )
                if resp.status_code == 200:
                    resposta = resp.json()["choices"][0]["message"]["content"]
                    modelo_usado = "groq/llama3-8b-8192"
        except Exception as e:
            logger.warning("Groq error: %s", e)

    # Tentar Gemini
    if not resposta:
        gemini_key = os.getenv("GEMINI_API_KEY", "")
        if gemini_key and modelo in ["auto", "gemini"]:
            try:
                import httpx
                prompt = SYSTEM + "\n\nUsuario: " + mensagem + "\nAssistente:"
                url = ("https://generativelanguage.googleapis.com/v1beta/models/"
                       "gemini-pro:generateContent?key=" + gemini_key)
                async with httpx.AsyncClient(timeout=30) as client:
                    resp = await client.post(
                        url,
                        json={"contents": [{"parts": [{"text": prompt}]}]}
                    )
                    if resp.status_code == 200:
                        resposta = resp.json()["candidates"][0]["content"]["parts"][0]["text"]
                        modelo_usado = "gemini-pro"
            except Exception as e:
                logger.warning("Gemini error: %s", e)

    # Fallback
    if not resposta:
        msg_lower = mensagem.lower()
        if any(w in msg_lower for w in ["triste", "chorando", "deprimido", "nao quero"]):
            resposta = "Entendo que voce esta passando por um momento dificil. Estou aqui para te ouvir. O que esta acontecendo? 💙"
        elif any(w in msg_lower for w in ["ansioso", "ansiedade", "nervoso", "preocupado"]):
            resposta = "A ansiedade pode ser muito desconfortavel. Tente: inspire por 4s, segure 4s, expire 4s. Repita 4 vezes. Como esta se sentindo agora? 🌬️"
        elif any(w in msg_lower for w in ["ajuda", "socorro", "nao aguento"]):
            resposta = "Estou aqui. Em emergencias: CVV 188 (24h gratuito) ou SAMU 192. Me conta mais sobre o que esta acontecendo. 💙"
        else:
            resposta = "Obrigado por compartilhar comigo. Estou aqui para te ouvir. Me conta mais sobre o que voce esta sentindo? 🤗"
        modelo_usado = "fallback"

    # Detectar crise
    crisis = ["suicidio", "me matar", "nao quero viver", "acabar com tudo"]
    alerta_crise = any(c in mensagem.lower() for c in crisis)
    if alerta_crise:
        aviso = "EMERGENCIA: CVV 188 (24h gratuito) | SAMU 192. Voce nao esta sozinho. 💙\n\n"
        resposta = aviso + resposta
        logger.warning("CRISE: user %s", user_id)

    conv_id = str(uuid.uuid4())[:8]
    _conversas.create(
        nome="Chat " + user_id, user_id=user_id, valor=mensagem[:100],
        dados=json.dumps({"mensagem": mensagem, "resposta": resposta, "modelo": modelo_usado}),
        categoria="crise" if alerta_crise else "normal"
    )

    return {
        "conversa_id": conv_id,
        "user_id": user_id,
        "mensagem": mensagem,
        "resposta": resposta,
        "modelo_usado": modelo_usado,
        "alerta_crise": alerta_crise,
        "timestamp": datetime.utcnow().isoformat(),
        "recursos_emergencia": {"cvv": "188", "samu": "192"} if alerta_crise else None
    }

@router.get("/historico/{user_id}")
async def historico(user_id: str, limite: int = 20):
    convs = _conversas.list(user_id=user_id, limite=limite)
    return {"total": len(convs), "conversas": convs}

plugin = ChatIaRealPlugin()
