"""
Plugin: Multi-LLM — Claude + GPT-4 + Mistral + Groq + Gemini + OpenRouter
Router inteligente que escolhe o melhor modelo disponível
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
from plugins.db_manager import SimpleDB
import os, uuid, json, logging, re

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/multi-llm", tags=["ia_avancada"])
_logs = SimpleDB("multi_llm_logs")

SYSTEM = (
    "Voce e um assistente de saude mental empatico da Emotion Intelligence Platform. "
    "Ofereca suporte emocional baseado em TCC, mindfulness e DBT. "
    "Em crises: indique CVV 188 e SAMU 192. "
    "Responda em portugues brasileiro. Maximo 300 palavras. "
    "NAO substitua profissionais de saude mental."
)


class MultiLlmPlugin(PluginBase):
    name = "multi_llm"
    version = "2.0.0"
    description = "Router inteligente entre Claude, GPT-4, Mistral, Groq, Gemini"
    category = "ia_avancada"

    def setup(self, app):
        app.include_router(router)
        logger.info("[multi_llm] OK")

    def health_check(self):
        ok = []
        for nome, key in [("groq","GROQ_API_KEY"),("gemini","GEMINI_API_KEY"),
                           ("claude","ANTHROPIC_API_KEY"),("gpt4","OPENAI_API_KEY"),
                           ("mistral","MISTRAL_API_KEY"),("openrouter","OPENROUTER_API_KEY")]:
            if os.getenv(key):
                ok.append(nome)
        return {"status": "healthy", "modelos_disponiveis": ok, "total": len(ok)}


@router.get("/modelos")
async def listar_modelos():
    return {"modelos": [
        {"id": "groq", "nome": "Groq LLaMA3 70B", "velocidade": "muito_rapida",
         "custo": "gratis", "disponivel": bool(os.getenv("GROQ_API_KEY"))},
        {"id": "gemini", "nome": "Google Gemini 1.5 Flash", "velocidade": "rapida",
         "custo": "gratis", "disponivel": bool(os.getenv("GEMINI_API_KEY"))},
        {"id": "claude", "nome": "Claude 3 Haiku", "velocidade": "media",
         "custo": "pago", "disponivel": bool(os.getenv("ANTHROPIC_API_KEY"))},
        {"id": "gpt4", "nome": "GPT-4o Mini", "velocidade": "media",
         "custo": "pago", "disponivel": bool(os.getenv("OPENAI_API_KEY"))},
        {"id": "mistral", "nome": "Mistral Small", "velocidade": "rapida",
         "custo": "pago", "disponivel": bool(os.getenv("MISTRAL_API_KEY"))},
        {"id": "openrouter", "nome": "OpenRouter (250+ modelos)", "velocidade": "variavel",
         "custo": "misto", "disponivel": bool(os.getenv("OPENROUTER_API_KEY"))},
    ]}


async def _chamar_groq(mensagem: str, system: str) -> str:
    import httpx
    key = os.getenv("GROQ_API_KEY", "")
    msgs = [{"role": "system", "content": system}, {"role": "user", "content": mensagem}]
    payload = {"model": "llama-3.1-70b-versatile", "messages": msgs,
               "max_tokens": 400, "temperature": 0.7}
    async with httpx.AsyncClient(timeout=25) as c:
        r = await c.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": "Bearer " + key},
            json=payload
        )
        if r.status_code == 200:
            return r.json()["choices"][0]["message"]["content"]
    return ""


async def _chamar_gemini(mensagem: str, system: str) -> str:
    import httpx
    key = os.getenv("GEMINI_API_KEY", "")
    prompt = system + "\n\nUsuario: " + mensagem
    url = ("https://generativelanguage.googleapis.com/v1beta/models/"
           "gemini-1.5-flash:generateContent?key=" + key)
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"maxOutputTokens": 400, "temperature": 0.7}
    }
    async with httpx.AsyncClient(timeout=25) as c:
        r = await c.post(url, json=payload)
        if r.status_code == 200:
            return r.json()["candidates"][0]["content"]["parts"][0]["text"]
    return ""


async def _chamar_claude(mensagem: str, system: str) -> str:
    import httpx
    key = os.getenv("ANTHROPIC_API_KEY", "")
    payload = {
        "model": "claude-3-haiku-20240307",
        "max_tokens": 400,
        "system": system,
        "messages": [{"role": "user", "content": mensagem}]
    }
    async with httpx.AsyncClient(timeout=30) as c:
        r = await c.post(
            "https://api.anthropic.com/v1/messages",
            headers={"x-api-key": key, "anthropic-version": "2023-06-01"},
            json=payload
        )
        if r.status_code == 200:
            return r.json()["content"][0]["text"]
    return ""


async def _chamar_gpt4(mensagem: str, system: str) -> str:
    import httpx
    key = os.getenv("OPENAI_API_KEY", "")
    msgs = [{"role": "system", "content": system}, {"role": "user", "content": mensagem}]
    async with httpx.AsyncClient(timeout=30) as c:
        r = await c.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": "Bearer " + key},
            json={"model": "gpt-4o-mini", "messages": msgs, "max_tokens": 400}
        )
        if r.status_code == 200:
            return r.json()["choices"][0]["message"]["content"]
    return ""


async def _chamar_mistral(mensagem: str, system: str) -> str:
    import httpx
    key = os.getenv("MISTRAL_API_KEY", "")
    msgs = [{"role": "system", "content": system}, {"role": "user", "content": mensagem}]
    async with httpx.AsyncClient(timeout=25) as c:
        r = await c.post(
            "https://api.mistral.ai/v1/chat/completions",
            headers={"Authorization": "Bearer " + key},
            json={"model": "mistral-small-latest", "messages": msgs, "max_tokens": 400}
        )
        if r.status_code == 200:
            return r.json()["choices"][0]["message"]["content"]
    return ""


async def _chamar_openrouter(mensagem: str, system: str) -> str:
    import httpx
    key = os.getenv("OPENROUTER_API_KEY", "")
    base = os.getenv("BASE_URL", "https://emotion-platform-albert.onrender.com")
    msgs = [{"role": "system", "content": system}, {"role": "user", "content": mensagem}]
    async with httpx.AsyncClient(timeout=30) as c:
        r = await c.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": "Bearer " + key, "HTTP-Referer": base},
            json={"model": "meta-llama/llama-3.1-8b-instruct:free",
                  "messages": msgs, "max_tokens": 400}
        )
        if r.status_code == 200:
            return r.json()["choices"][0]["message"]["content"]
    return ""


CHAMADAS = {
    "groq": (_chamar_groq, "GROQ_API_KEY", "groq/llama-3.1-70b"),
    "gemini": (_chamar_gemini, "GEMINI_API_KEY", "gemini-1.5-flash"),
    "claude": (_chamar_claude, "ANTHROPIC_API_KEY", "claude-3-haiku"),
    "gpt4": (_chamar_gpt4, "OPENAI_API_KEY", "gpt-4o-mini"),
    "mistral": (_chamar_mistral, "MISTRAL_API_KEY", "mistral-small"),
    "openrouter": (_chamar_openrouter, "OPENROUTER_API_KEY", "openrouter/llama-3.1-8b"),
}


@router.post("/chat")
async def chat_multi_llm(
    mensagem: str,
    user_id: str = "anonimo",
    modelo_preferido: str = "auto",
    contexto: str = "terapeutico"
):
    if not mensagem.strip():
        raise HTTPException(400, "Mensagem vazia")

    system = SYSTEM if contexto == "terapeutico" else "Voce e um assistente util."
    resposta = None
    modelo_usado = None

    ordem = list(CHAMADAS.keys())
    if modelo_preferido != "auto" and modelo_preferido in CHAMADAS:
        ordem = [modelo_preferido] + [m for m in ordem if m != modelo_preferido]

    for modelo in ordem:
        if resposta:
            break
        fn, key_env, nome_modelo = CHAMADAS[modelo]
        if not os.getenv(key_env):
            continue
        try:
            texto = await fn(mensagem, system)
            if texto:
                resposta = texto
                modelo_usado = nome_modelo
        except Exception as e:
            logger.debug("Modelo %s falhou: %s", modelo, e)

    # Fallback
    if not resposta:
        palavras_neg = any(w in mensagem.lower()
                           for w in ["triste", "ansioso", "medo", "sozinho", "deprimido"])
        if palavras_neg:
            resposta = "Estou aqui para te ouvir. Me conta mais sobre como voce esta se sentindo? Voce nao esta sozinho. 💙"
        else:
            resposta = "Obrigado por compartilhar comigo. Continue se cuidando! 🌟"
        modelo_usado = "fallback"

    # Detectar crise
    crisis_words = ["suicidio", "me matar", "nao quero viver", "acabar com tudo", "me machucar"]
    is_crisis = any(w in mensagem.lower() for w in crisis_words)
    if is_crisis:
        aviso = "EMERGENCIA: Ligue AGORA para o CVV 188 (24h, gratuito) ou SAMU 192. Voce nao esta sozinho. 💙\n\n"
        resposta = aviso + resposta
        logger.warning("CRISE DETECTADA — usuario %s", user_id)

    _logs.create(
        nome="Chat " + user_id,
        user_id=user_id,
        valor=modelo_usado or "?",
        dados=json.dumps({"msg": mensagem[:100], "modelo": modelo_usado, "crise": is_crisis})
    )

    return {
        "id": str(uuid.uuid4())[:8],
        "resposta": resposta,
        "modelo_usado": modelo_usado,
        "is_crisis": is_crisis,
        "ts": datetime.utcnow().isoformat(),
        "recursos": {"cvv": "188", "samu": "192"} if is_crisis else None
    }


@router.post("/analisar-emocao")
async def analisar_emocao_llm(texto: str, user_id: str = "anonimo"):
    schema = '{"emocao":"str","intensidade":0,"valencia":"str","insight":"str","recomendacao":"str"}'
    prompt = "Analise o texto. Responda SOMENTE em JSON valido com este schema: " + schema + ". Texto: " + texto[:300]
    result = await chat_multi_llm(prompt, user_id, "auto", "analise")
    try:
        m = re.search(r"\{[^}]+\}", result["resposta"])
        if m:
            return {"texto": texto[:100], "analise": json.loads(m.group()),
                    "modelo": result["modelo_usado"]}
    except Exception:
        pass
    return {
        "texto": texto[:100],
        "analise": {"emocao": "neutro", "intensidade": 5, "valencia": "neutra",
                    "insight": "Analise realizada", "recomendacao": "Continue se cuidando"},
        "modelo": result.get("modelo_usado", "desconhecido")
    }


@router.get("/benchmark")
async def benchmark_modelos():
    import time
    resultados = []
    for modelo, (fn, key_env, nome) in CHAMADAS.items():
        if not os.getenv(key_env):
            resultados.append({"modelo": modelo, "disponivel": False})
            continue
        inicio = time.time()
        try:
            texto = await fn("Ola", "Seja breve.")
            ms = round((time.time() - inicio) * 1000)
            resultados.append({"modelo": modelo, "nome": nome,
                                "disponivel": True, "latencia_ms": ms,
                                "status": "ok" if texto else "sem resposta"})
        except Exception as e:
            resultados.append({"modelo": modelo, "disponivel": True,
                                "latencia_ms": None, "status": str(e)[:50]})

    resultados.sort(key=lambda x: x.get("latencia_ms") or 99999)
    return {"benchmark": resultados,
            "mais_rapido": next((r["modelo"] for r in resultados if r.get("latencia_ms")), None)}


@router.get("/logs/{user_id}")
async def logs_usuario(user_id: str, limite: int = 20):
    logs = _logs.list(user_id=user_id, limite=limite)
    return {"total": len(logs), "logs": logs}


plugin = MultiLlmPlugin()
