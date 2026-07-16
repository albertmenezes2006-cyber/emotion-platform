"""Plugin: Chat IA Real v4 — usa Multi-LLM como backend"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
from plugins.db_manager import SimpleDB
import os, uuid, json, logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/chat-ia", tags=["ia"])
_conversas = SimpleDB("chat_ia_v3")

SYSTEM = (
    "Voce e um assistente de saude mental empatico da plataforma EmotionAI. "
    "Responda SEMPRE em portugues brasileiro. "
    "Use tecnicas de TCC, DBT e Mindfulness nas respostas. "
    "Seja empático, acolhedor e nao julgamental. "
    "Em situacoes de crise: indique CVV 188 e SAMU 192. "
    "Maximo 250 palavras. NAO substitua profissionais de saude mental."
)

CRISIS_WORDS = ["suicidio","suicídio","me matar","nao quero viver",
                "nao quero mais viver","acabar com tudo","me machucar"]

FALLBACK_INTELIGENTE = {
    "ansio": "A ansiedade pode ser muito desconfortavel. Vamos tentar a respiracao 4-7-8 agora:\n\n1. Expire completamente\n2. Inspire pelo nariz: 4 segundos\n3. Segure o ar: 7 segundos\n4. Expire pela boca: 8 segundos\n\nRepita 4 vezes. Isso ativa o sistema nervoso parassimpatico. Como esta se sentindo?",
    "nervos": "Entendo que voce esta nervoso. Isso e muito comum. Tente se concentrar no momento presente: o que voce ve, ouve e sente agora? Isso e uma tecnica de grounding que ajuda a reduzir a tensao.",
    "trist": "Sinto muito que voce esta passando por isso. 💙 A tristeza e uma emocao valida. Voce nao precisa enfrentar isso sozinho. Me conta mais: o que esta acontecendo em sua vida ultimamente?",
    "deprim": "Reconheco que voce esta passando por um momento muito dificil. Sentimentos de depressao merecem atencao e cuidado. Voce esta buscando ajuda profissional? Um psicologo ou psiquiatra pode fazer uma diferenca enorme.",
    "dormir": "Problemas de sono afetam muito o bem-estar. Algumas dicas baseadas em evidencias:\n• Mantenha horario fixo para dormir/acordar\n• Evite telas 1h antes de dormir\n• Quarto escuro, fresco (18-20 graus) e silencioso\n• Tecnica 4-7-8 ajuda muito antes de dormir\n\nO que passa pela sua cabeca quando tenta dormir?",
    "respiracao": "Tecnica de Respiracao 4-7-8:\n\n1. Expire todo o ar\n2. Inspire pelo nariz: 4 segundos\n3. Segure: 7 segundos\n4. Expire pela boca fazendo som: 8 segundos\n\nRepita 4 vezes. Quer tentar agora comigo?",
    "mindf": "Mindfulness em 5 minutos:\n1. Sente-se confortavelmente\n2. Feche os olhos e respire normalmente\n3. Foque apenas na sensacao do ar entrando e saindo\n4. Quando pensamentos vierem, so observe - sem julgar - e volte a respiracao\n\nComecar com 5 min/dia ja traz beneficios comprovados!",
    "raiva": "A raiva e uma emocao valida que precisa de expressao saudavel. Antes de agir: respire fundo 10 vezes, beba agua, afaste-se da situacao por alguns minutos. O que esta te deixando com raiva?",
    "motivacao": "Entendo que voce esta precisando de motivacao. Uma tecnica util e comecar pelo menor passo possivel. Qual seria a menor acao que voce poderia fazer agora em direcao ao que precisa?",
    "sozinho": "Sentir-se sozinho e muito doloroso. Voce nao esta sozinho neste momento - estou aqui. Mas conexoes humanas sao fundamentais. Ha alguem de confianca com quem voce poderia entrar em contato hoje?",
    "default": "Estou aqui para te ouvir e apoiar. 💙 Me conta mais sobre o que esta sentindo ou passando. Quanto mais voce compartilhar, mais posso te ajudar de forma personalizada."
}


class ChatIaRealPlugin(PluginBase):
    name = "chat_ia_real"
    version = "4.0.0"
    description = "Chat IA com Multi-LLM backend (Mistral + Groq + Gemini)"
    category = "ia"

    def setup(self, app):
        app.include_router(router)
        logger.info("[chat_ia_real v4] OK — usa Multi-LLM backend")

    def health_check(self):
        return {
            "status": "healthy",
            "versao": "4.0.0",
            "backend": "multi-llm",
            "conversas": _conversas.count()
        }


async def _chamar_multi_llm(mensagem: str, modelo: str = "auto") -> tuple:
    """Usa o plugin multi-llm que ja funciona"""
    import httpx
    import os
    
    # Tentar diretamente os modelos que sabemos que funcionam
    modelos_ordem = ["mistral", "groq", "gemini", "openrouter"]
    if modelo != "auto" and modelo in modelos_ordem:
        modelos_ordem = [modelo] + [m for m in modelos_ordem if m != modelo]
    
    msgs = [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": mensagem}
    ]
    
    # Mistral (sabemos que funciona)
    if "mistral" in modelos_ordem:
        key = os.getenv("MISTRAL_API_KEY","")
        if key:
            try:
                async with httpx.AsyncClient(timeout=20) as c:
                    r = await c.post(
                        "https://api.mistral.ai/v1/chat/completions",
                        headers={"Authorization": "Bearer " + key},
                        json={"model":"mistral-small-latest","messages":msgs,"max_tokens":350,"temperature":0.7}
                    )
                    if r.status_code == 200:
                        texto = r.json()["choices"][0]["message"]["content"]
                        if texto and len(texto.strip()) > 5:
                            return texto.strip(), "mistral-small"
                    else:
                        logger.warning(f"Mistral {r.status_code}: {r.text[:80]}")
            except Exception as e:
                logger.warning(f"Mistral error: {e}")
    
    # OpenRouter (fallback gratuito)
    if "openrouter" in modelos_ordem:
        key = os.getenv("OPENROUTER_API_KEY","")
        if key:
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
                        texto = r.json()["choices"][0]["message"]["content"]
                        if texto and len(texto.strip()) > 5:
                            return texto.strip(), "openrouter/llama3"
            except Exception as e:
                logger.warning(f"OpenRouter error: {e}")
    
    # Groq
    if "groq" in modelos_ordem:
        key = os.getenv("GROQ_API_KEY","")
        if key:
            try:
                async with httpx.AsyncClient(timeout=20) as c:
                    r = await c.post(
                        "https://api.groq.com/openai/v1/chat/completions",
                        headers={"Authorization": "Bearer " + key},
                        json={"model":"llama3-8b-8192","messages":msgs,"max_tokens":350,"temperature":0.7}
                    )
                    if r.status_code == 200:
                        texto = r.json()["choices"][0]["message"]["content"]
                        if texto and len(texto.strip()) > 5:
                            return texto.strip(), "groq/llama3-8b"
                    else:
                        logger.warning(f"Groq {r.status_code}: {r.text[:80]}")
            except Exception as e:
                logger.warning(f"Groq error: {e}")
    
    # Gemini
    if "gemini" in modelos_ordem:
        key = os.getenv("GEMINI_API_KEY","")
        if key:
            try:
                prompt = SYSTEM + "\n\nUsuario: " + mensagem
                url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=" + key
                async with httpx.AsyncClient(timeout=20) as c:
                    r = await c.post(url, json={
                        "contents":[{"parts":[{"text":prompt}]}],
                        "generationConfig":{"maxOutputTokens":350,"temperature":0.7}
                    })
                    if r.status_code == 200:
                        texto = r.json()["candidates"][0]["content"]["parts"][0]["text"]
                        if texto and len(texto.strip()) > 5:
                            return texto.strip(), "gemini-1.5-flash"
            except Exception as e:
                logger.warning(f"Gemini error: {e}")
    
    return None, None


def _fallback(mensagem: str) -> str:
    baixo = mensagem.lower()
    for chave, resp in FALLBACK_INTELIGENTE.items():
        if chave != "default" and chave in baixo:
            return resp
    return FALLBACK_INTELIGENTE["default"]


@router.get("/modelos/disponiveis")
async def modelos_disponiveis():
    return {"modelos": [
        {"id":"auto","nome":"Auto (melhor disponível)","disponivel":True,"velocidade":"variavel"},
        {"id":"mistral","nome":"Mistral Small","disponivel":bool(os.getenv("MISTRAL_API_KEY")),"velocidade":"rapida"},
        {"id":"groq","nome":"Groq LLaMA3","disponivel":bool(os.getenv("GROQ_API_KEY")),"velocidade":"muito_rapida"},
        {"id":"gemini","nome":"Google Gemini","disponivel":bool(os.getenv("GEMINI_API_KEY")),"velocidade":"rapida"},
        {"id":"openrouter","nome":"OpenRouter","disponivel":bool(os.getenv("OPENROUTER_API_KEY")),"velocidade":"variavel"},
        {"id":"fallback","nome":"Respostas base","disponivel":True,"velocidade":"instantanea"},
    ]}


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

    # Tentar IA real
    resposta, modelo_usado = await _chamar_multi_llm(mensagem, modelo)

    # Fallback inteligente
    if not resposta:
        resposta = _fallback(mensagem)
        modelo_usado = "fallback"

    # Detectar crise
    is_crisis = any(w in mensagem.lower() for w in CRISIS_WORDS)
    if is_crisis:
        aviso = "🚨 EMERGENCIA: CVV 188 (24h gratuito) | SAMU 192. Voce nao esta sozinho.\n\n"
        resposta = aviso + resposta
        logger.warning(f"CRISE: user={user_id}")

    # Salvar
    try:
        _conversas.create(
            nome="Chat " + user_id, user_id=user_id,
            valor=modelo_usado or "?",
            dados=json.dumps({"msg":mensagem[:100],"resp":resposta[:100],"modelo":modelo_usado}),
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
        "recursos_emergencia": {"cvv":"188","samu":"192"} if is_crisis else None
    }


@router.get("/historico/{user_id}")
async def historico(user_id: str, limite: int = 20):
    convs = _conversas.list(user_id=user_id, limite=limite)
    return {"total": len(convs), "conversas": convs}


plugin = ChatIaRealPlugin()
