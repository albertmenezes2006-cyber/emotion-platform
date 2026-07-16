"""Plugin: Chat IA Real — integração com Groq, Gemini e fallback"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
from plugins.db_manager import SimpleDB
import os, uuid, json, logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/chat-ia", tags=["ia"])

_conversas = SimpleDB("chat_ia_conversas")

SYSTEM_PROMPT = """Você é um assistente de saúde mental empático e acolhedor da plataforma 
Emotion Intelligence Platform. Você oferece suporte emocional, psicoeducação e técnicas 
terapêuticas baseadas em evidências (TCC, mindfulness, DBT).

REGRAS IMPORTANTES:
- Nunca substitua um profissional de saúde mental
- Em emergências, sempre indique: CVV 188, SAMU 192
- Seja empático, caloroso e não-julgamental
- Use linguagem acessível e clara
- Respostas em português brasileiro
- Máximo 300 palavras por resposta

Você NÃO é terapeuta. Você é um assistente de apoio emocional."""

class ChatIaRealPlugin(PluginBase):
    name = "chat_ia_real"; version = "2.0.0"
    description = "Chat com IA real (Groq/Gemini) para suporte emocional"; category = "ia"
    def setup(self, app): app.include_router(router); logger.info("[chat_ia_real] OK")
    def health_check(self):
        groq_ok = bool(os.getenv("GROQ_API_KEY"))
        gemini_ok = bool(os.getenv("GEMINI_API_KEY"))
        return {"status": "healthy", "groq": groq_ok, "gemini": gemini_ok, "conversas": _conversas.count()}

@router.post("/mensagem")
async def enviar_mensagem(
    user_id: str,
    mensagem: str,
    historico_conversa: list = None,
    modelo: str = "auto"
):
    if not mensagem or len(mensagem.strip()) < 2:
        raise HTTPException(400, "Mensagem muito curta")

    historico_conversa = historico_conversa or []
    resposta_ia = None
    modelo_usado = None

    # Tentar Groq primeiro
    groq_key = os.getenv("GROQ_API_KEY")
    if groq_key and modelo in ["auto", "groq"]:
        try:
            import httpx
            messages = [{"role": "system", "content": SYSTEM_PROMPT}]
            for h in historico_conversa[-6:]:
                messages.append({"role": h.get("role", "user"), "content": h.get("content", "")})
            messages.append({"role": "user", "content": mensagem})

            async with httpx.AsyncClient(timeout=30) as client:
                resp = await client.post(
                    "https://api.groq.com/openai/v1/chat/completions",
                    headers={"Authorization": f"Bearer {groq_key}"},
                    json={"model": "llama3-8b-8192", "messages": messages, "max_tokens": 400, "temperature": 0.7}
                )
                if resp.status_code == 200:
                    data = resp.json()
                    resposta_ia = data["choices"][0]["message"]["content"]
                    modelo_usado = "groq/llama3-8b-8192"
        except Exception as e:
            logger.warning(f"Groq error: {e}")

    # Tentar Gemini
    if not resposta_ia:
        gemini_key = os.getenv("GEMINI_API_KEY")
        if gemini_key and modelo in ["auto", "gemini"]:
            try:
                import httpx
                prompt = f"{SYSTEM_PROMPT}\n\nUsuário: {mensagem}\nAssistente:"
                async with httpx.AsyncClient(timeout=30) as client:
                    resp = await client.post(
                        f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={gemini_key}",
                        json={"contents": [{"parts": [{"text": prompt}]}]}
                    )
                    if resp.status_code == 200:
                        data = resp.json()
                        resposta_ia = data["candidates"][0]["content"]["parts"][0]["text"]
                        modelo_usado = "gemini-pro"
            except Exception as e:
                logger.warning(f"Gemini error: {e}")

    # Fallback inteligente
    if not resposta_ia:
        respostas_fallback = {
            "triste": "Entendo que você está passando por um momento difícil. É corajoso compartilhar isso. O que está te fazendo sentir assim? 💙",
            "ansioso": "A ansiedade pode ser muito desconfortável. Vamos tentar uma respiração juntos: inspire por 4 segundos, segure por 4, expire por 4. Como está se sentindo agora? 🌬️",
            "ajuda": "Estou aqui para te apoiar. Pode me contar mais sobre o que está acontecendo? Lembre-se: o CVV (188) está disponível 24h se precisar de apoio imediato.",
            "default": "Obrigado por compartilhar comigo. Estou aqui para te ouvir. Me conta mais sobre o que você está sentindo? 🤗"
        }
        msg_lower = mensagem.lower()
        if any(w in msg_lower for w in ["triste", "chorando", "deprimido"]):
            resposta_ia = respostas_fallback["triste"]
        elif any(w in msg_lower for w in ["ansioso", "ansiedade", "nervoso", "preocupado"]):
            resposta_ia = respostas_fallback["ansioso"]
        elif any(w in msg_lower for w in ["ajuda", "socorro", "não aguento"]):
            resposta_ia = respostas_fallback["ajuda"]
        else:
            resposta_ia = respostas_fallback["default"]
        modelo_usado = "fallback"

    # Verificar palavras de crise
    palavras_crise = ["suicídio", "me matar", "não quero viver", "acabar com tudo"]
    alerta_crise = any(p in mensagem.lower() for p in palavras_crise)
    if alerta_crise:
        resposta_ia = f"Estou muito preocupado com você agora. Por favor, ligue imediatamente para o CVV: **188** (24h, gratuito) ou SAMU: **192**. Você não está sozinho. 💙

{resposta_ia}"
        logger.warning(f"[ALERTA CRISE] user {user_id}: {mensagem[:100]}")

    conversa_id = str(uuid.uuid4())[:8]
    _conversas.create(
        nome=f"Chat {user_id}",
        user_id=user_id,
        valor=mensagem[:100],
        dados=json.dumps({"mensagem": mensagem, "resposta": resposta_ia, "modelo": modelo_usado}),
        categoria="crise" if alerta_crise else "normal"
    )

    return {
        "conversa_id": conversa_id,
        "user_id": user_id,
        "mensagem": mensagem,
        "resposta": resposta_ia,
        "modelo_usado": modelo_usado,
        "alerta_crise": alerta_crise,
        "timestamp": datetime.utcnow().isoformat(),
        "recursos_emergencia": {"cvv": "188", "samu": "192"} if alerta_crise else None
    }

@router.get("/historico/{user_id}")
async def historico(user_id: str, limite: int = 20):
    convs = _conversas.list(user_id=user_id, limite=limite)
    return {"total": len(convs), "conversas": convs}

@router.get("/modelos/disponiveis")
async def modelos_disponiveis():
    return {
        "modelos": [
            {"id": "groq", "nome": "Groq LLaMA3", "disponivel": bool(os.getenv("GROQ_API_KEY")), "velocidade": "muito_rapida"},
            {"id": "gemini", "nome": "Google Gemini", "disponivel": bool(os.getenv("GEMINI_API_KEY")), "velocidade": "rapida"},
            {"id": "fallback", "nome": "Respostas base", "disponivel": True, "velocidade": "instantanea"},
        ]
    }

plugin = ChatIaRealPlugin()
