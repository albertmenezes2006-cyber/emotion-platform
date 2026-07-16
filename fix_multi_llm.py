#!/usr/bin/env python3
"""Corrige f-string do multi_llm.py"""

content = '''"""
Plugin: Multi-LLM — Claude + GPT-4 + Mistral + Groq + Gemini
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

SYSTEM_TERAPEUTICO = (
    "Você é um assistente de saúde mental empático da Emotion Intelligence Platform. "
    "Ofereça suporte emocional baseado em TCC, mindfulness e DBT. "
    "Em crises: indique CVV 188 e SAMU 192. "
    "Responda em português brasileiro. Máximo 300 palavras. "
    "NAO substitua profissionais de saúde mental."
)

class MultiLlmPlugin(PluginBase):
    name = "multi_llm"; version = "2.0.0"
    description = "Router inteligente entre Claude, GPT-4, Mistral, Groq, Gemini"
    category = "ia_avancada"

    def setup(self, app):
        app.include_router(router)
        logger.info("[multi_llm] OK")

    def health_check(self):
        modelos_ok = []
        if os.getenv("GROQ_API_KEY"): modelos_ok.append("groq")
        if os.getenv("GEMINI_API_KEY"): modelos_ok.append("gemini")
        if os.getenv("ANTHROPIC_API_KEY"): modelos_ok.append("claude")
        if os.getenv("OPENAI_API_KEY"): modelos_ok.append("gpt4")
        if os.getenv("MISTRAL_API_KEY"): modelos_ok.append("mistral")
        if os.getenv("OPENROUTER_API_KEY"): modelos_ok.append("openrouter")
        return {"status": "healthy", "modelos": modelos_ok, "total": len(modelos_ok)}


@router.get("/modelos")
async def listar_modelos():
    return {"modelos": [
        {"id": "groq", "nome": "Groq LLaMA3 70B", "velocidade": "muito_rapida",
         "custo": "gratis", "disponivel": bool(os.getenv("GROQ_API_KEY"))},
        {"id": "gemini", "nome": "Google Gemini Pro", "velocidade": "rapida",
         "custo": "gratis", "disponivel": bool(os.getenv("GEMINI_API_KEY"))},
        {"id": "claude", "nome": "Claude 3.5 Sonnet", "velocidade": "media",
         "custo": "pago", "disponivel": bool(os.getenv("ANTHROPIC_API_KEY"))},
        {"id": "gpt4", "nome": "GPT-4o Mini", "velocidade": "media",
         "custo": "pago", "disponivel": bool(os.getenv("OPENAI_API_KEY"))},
        {"id": "mistral", "nome": "Mistral Large", "velocidade": "rapida",
         "custo": "pago", "disponivel": bool(os.getenv("MISTRAL_API_KEY"))},
        {"id": "openrouter", "nome": "OpenRouter (250+ modelos)", "velocidade": "variavel",
         "custo": "misto", "disponivel": bool(os.getenv("OPENROUTER_API_KEY"))},
    ]}


@router.post("/chat")
async def chat_multi_llm(
    mensagem: str,
    user_id: str = "anonimo",
    modelo_preferido: str = "auto",
    contexto: str = "terapeutico"
):
    """Chat com roteamento automático entre modelos"""
    if not mensagem.strip():
        raise HTTPException(400, "Mensagem vazia")

    system = SYSTEM_TERAPEUTICO if contexto == "terapeutico" else "Voce e um assistente util."
    resposta = None
    modelo_usado = None

    ordem = ["groq", "gemini", "claude", "gpt4", "mistral", "openrouter"]
    if modelo_preferido != "auto" and modelo_preferido in ordem:
        ordem = [modelo_preferido] + [m for m in ordem if m != modelo_preferido]

    import httpx

    for modelo in ordem:
        if resposta:
            break
        try:
            if modelo == "groq" and os.getenv("GROQ_API_KEY"):
                msgs = [
                    {"role": "system", "content": system},
                    {"role": "user", "content": mensagem}
                ]
                async with httpx.AsyncClient(timeout=25) as c:
                    r = await c.post(
                        "https://api.groq.com/openai/v1/chat/completions",
                        headers={"Authorization": "Bearer " + os.getenv("GROQ_API_KEY")},
                        json={"model": "llama-3.1-70b-versatile", "messages": msgs,
                              "max_tokens": 400, "temperature": 0.7}
                    )
                    if r.status_code == 200:
                        resposta = r.json()["choices"][0]["message"]["content"]
                        modelo_usado = "groq/llama-3.1-70b"

            elif modelo == "gemini" and os.getenv("GEMINI_API_KEY"):
                prompt_gemini = system + "\\n\\nUsuario: " + mensagem
                payload_gemini = {
                    "contents": [{"parts": [{"text": prompt_gemini}]}],
                    "generationConfig": {"maxOutputTokens": 400, "temperature": 0.7}
                }
                url_gemini = (
                    "https://generativelanguage.googleapis.com/v1beta/models/"
                    "gemini-1.5-flash:generateContent?key=" + os.getenv("GEMINI_API_KEY")
                )
                async with httpx.AsyncClient(timeout=25) as c:
                    r = await c.post(url_gemini, json=payload_gemini)
                    if r.status_code == 200:
                        resposta = r.json()["candidates"][0]["content"]["parts"][0]["text"]
                        modelo_usado = "gemini-1.5-flash"

            elif modelo == "claude" and os.getenv("ANTHROPIC_API_KEY"):
                async with httpx.AsyncClient(timeout=30) as c:
                    r = await c.post(
                        "https://api.anthropic.com/v1/messages",
                        headers={
                            "x-api-key": os.getenv("ANTHROPIC_API_KEY"),
                            "anthropic-version": "2023-06-01"
                        },
                        json={
                            "model": "claude-3-haiku-20240307",
                            "max_tokens": 400,
                            "system": system,
                            "messages": [{"role": "user", "content": mensagem}]
                        }
                    )
                    if r.status_code == 200:
                        resposta = r.json()["content"][0]["text"]
                        modelo_usado = "claude-3-haiku"

            elif modelo == "gpt4" and os.getenv("OPENAI_API_KEY"):
                msgs_gpt = [
                    {"role": "system", "content": system},
                    {"role": "user", "content": mensagem}
                ]
                async with httpx.AsyncClient(timeout=30) as c:
                    r = await c.post(
                        "https://api.openai.com/v1/chat/completions",
                        headers={"Authorization": "Bearer " + os.getenv("OPENAI_API_KEY")},
                        json={"model": "gpt-4o-mini", "messages": msgs_gpt, "max_tokens": 400}
                    )
                    if r.status_code == 200:
                        resposta = r.json()["choices"][0]["message"]["content"]
                        modelo_usado = "gpt-4o-mini"

            elif modelo == "mistral" and os.getenv("MISTRAL_API_KEY"):
                msgs_mistral = [
                    {"role": "system", "content": system},
                    {"role": "user", "content": mensagem}
                ]
                async with httpx.AsyncClient(timeout=25) as c:
                    r = await c.post(
                        "https://api.mistral.ai/v1/chat/completions",
                        headers={"Authorization": "Bearer " + os.getenv("MISTRAL_API_KEY")},
                        json={"model": "mistral-small-latest", "messages": msgs_mistral,
                              "max_tokens": 400}
                    )
                    if r.status_code == 200:
                        resposta = r.json()["choices"][0]["message"]["content"]
                        modelo_usado = "mistral-small"

            elif modelo == "openrouter" and os.getenv("OPENROUTER_API_KEY"):
                base_url = "https://emotion-platform-albert.onrender.com"
                msgs_or = [
                    {"role": "system", "content": system},
                    {"role": "user", "content": mensagem}
                ]
                async with httpx.AsyncClient(timeout=30) as c:
                    r = await c.post(
                        "https://openrouter.ai/api/v1/chat/completions",
                        headers={
                            "Authorization": "Bearer " + os.getenv("OPENROUTER_API_KEY"),
                            "HTTP-Referer": base_url
                        },
                        json={
                            "model": "meta-llama/llama-3.1-8b-instruct:free",
                            "messages": msgs_or,
                            "max_tokens": 400
                        }
                    )
                    if r.status_code == 200:
                        resposta = r.json()["choices"][0]["message"]["content"]
                        modelo_usado = "openrouter/llama-3.1-8b"

        except Exception as e:
            logger.debug("Modelo %s falhou: %s", modelo, e)
            continue

    # Fallback final
    if not resposta:
        palavras_neg = any(w in mensagem.lower()
                           for w in ["triste", "ansioso", "medo", "sozinho"])
        if palavras_neg:
            resposta = "Estou aqui para te ouvir. Me conta mais sobre como voce esta se sentindo? 💙"
        else:
            resposta = "Obrigado por compartilhar. Continue se cuidando! 🌟"
        modelo_usado = "fallback"

    # Detectar crise
    crisis_words = ["suicidio", "me matar", "nao quero viver", "acabar com tudo"]
    is_crisis = any(w in mensagem.lower() for w in crisis_words)
    if is_crisis:
        aviso = "ALERTA: Ligue agora para CVV 188 (24h gratuito) ou SAMU 192. Voce nao esta sozinho. 💙"
        resposta = aviso + "\\n\\n" + resposta

    log_id = str(uuid.uuid4())[:8]
    _logs.create(
        nome="Chat " + user_id,
        user_id=user_id,
        valor=modelo_usado or "?",
        dados=json.dumps({
            "msg": mensagem[:100],
            "modelo": modelo_usado,
            "crise": is_crisis
        })
    )

    return {
        "id": log_id,
        "resposta": resposta,
        "modelo_usado": modelo_usado,
        "is_crisis": is_crisis,
        "ts": datetime.utcnow().isoformat(),
        "recursos": {"cvv": "188", "samu": "192"} if is_crisis else None
    }


@router.post("/analisar-emocao")
async def analisar_emocao_llm(texto: str, user_id: str = "anonimo"):
    """Analise emocional profunda com LLM"""
    prompt = (
        "Analise o texto e responda SOMENTE em JSON valido: "
        \'{"emocao":"palavra","intensidade":0,"valencia":"positiva/negativa/neutra","insight":"frase","recomendacao":"frase"}\'. "
        "Texto: \'" + texto[:300] + "\'"
    )
    result = await chat_multi_llm(prompt, user_id, "auto", "analise")
    try:
        json_match = re.search(r"\\{[^}]+\\}", result["resposta"])
        if json_match:
            analise = json.loads(json_match.group())
            return {"texto": texto[:100], "analise": analise, "modelo": result["modelo_usado"]}
    except Exception:
        pass
    return {
        "texto": texto[:100],
        "analise": {
            "emocao": "neutro", "intensidade": 5,
            "valencia": "neutra", "insight": "Analise realizada",
            "recomendacao": "Continue se cuidando"
        },
        "modelo": result.get("modelo_usado", "desconhecido")
    }


@router.get("/benchmark")
async def benchmark_modelos():
    """Testa qual modelo esta mais rapido"""
    import time
    resultados = []
    chaves = {"groq": "GROQ_API_KEY", "gemini": "GEMINI_API_KEY", "mistral": "MISTRAL_API_KEY"}

    for modelo, chave in chaves.items():
        if not os.getenv(chave):
            resultados.append({"modelo": modelo, "disponivel": False, "latencia_ms": None})
            continue
        inicio = time.time()
        try:
            r = await chat_multi_llm("Ola", "benchmark", modelo, "geral")
            ms = round((time.time() - inicio) * 1000)
            resultados.append({"modelo": modelo, "disponivel": True,
                                "latencia_ms": ms, "status": "ok"})
        except Exception as e:
            resultados.append({"modelo": modelo, "disponivel": True,
                                "latencia_ms": None, "status": str(e)[:50]})

    resultados.sort(key=lambda x: x.get("latencia_ms") or 99999)
    return {
        "benchmark": resultados,
        "mais_rapido": resultados[0]["modelo"] if resultados else None
    }


plugin = MultiLlmPlugin()
'''

# Fix the f-string issue with the analyze prompt
content = content.replace(
    "\'",
    "'"
)

with open("plugins/ia_avancada/multi_llm.py", "w") as f:
    f.write(content)

print("✅ multi_llm.py reescrito")

import subprocess, sys
r = subprocess.run([sys.executable, "-m", "py_compile", "plugins/ia_avancada/multi_llm.py"],
                   capture_output=True, text=True)
if r.returncode == 0:
    print("✅ Compila OK")
else:
    print("❌ Erro:")
    print(r.stderr[:300])
