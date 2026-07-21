"""
Plugin: Claude API Direto
Categoria: ia
"""
VERSAO = "1.0"
NOME = "claude"
DESCRICAO = "Anthropic Claude — claude-3-5-sonnet, haiku, opus"
CATEGORIA = "ia"

import os
import httpx

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
CLAUDE_MODELS = {
    "sonnet": "claude-3-5-sonnet-20241022",
    "haiku":  "claude-3-haiku-20240307",
    "opus":   "claude-3-opus-20240229",
}

async def claude_completar(mensagem: str, modelo: str = "haiku", max_tokens: int = 1000, sistema: str = "") -> str:
    if not ANTHROPIC_API_KEY:
        return ""
    try:
        async with httpx.AsyncClient(timeout=30) as client:
            payload = {
                "model": CLAUDE_MODELS.get(modelo, CLAUDE_MODELS["haiku"]),
                "max_tokens": max_tokens,
                "messages": [{"role": "user", "content": mensagem}]
            }
            if sistema:
                payload["system"] = sistema
            r = await client.post(
                "https://api.anthropic.com/v1/messages",
                headers={"x-api-key": ANTHROPIC_API_KEY, "anthropic-version": "2023-06-01", "content-type": "application/json"},
                json=payload
            )
            data = r.json()
            return data.get("content", [{}])[0].get("text", "")
    except Exception as e:
        print(f"Claude erro: {e}")
        return ""

async def claude_analisar_emocao(texto: str) -> dict:
    prompt = f"""Analise a emocao do texto em portugues.
Responda APENAS em JSON valido: {{"emocao": "string", "intensidade": 1-5, "confianca": 0.0-1.0, "subtom": "string"}}
Texto: {texto[:500]}"""
    resultado = await claude_completar(prompt, modelo="haiku", max_tokens=150)
    try:
        import json
        import re
        m = re.search(r'\{.*\}', resultado, re.DOTALL)
        if m:
            return json.loads(m.group())
    except Exception:
        pass
    return {"emocao": "neutro", "intensidade": 3, "confianca": 0.5, "subtom": ""}

async def claude_terapia(mensagem: str, historico: list = None, perfil: str = "") -> str:
    sistema = f"""Voce e Sofia, psicologa virtual empatica e especializada em inteligencia emocional.
Responda em portugues brasileiro de forma calorosa, profissional e acolhedora.
{f"Perfil do usuario: {perfil}" if perfil else ""}
Nao repita frases. Seja genuina e presente."""
    historico = historico or []
    messages = historico[-10:] + [{"role": "user", "content": mensagem}]
    if not ANTHROPIC_API_KEY:
        return ""
    try:
        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.post(
                "https://api.anthropic.com/v1/messages",
                headers={"x-api-key": ANTHROPIC_API_KEY, "anthropic-version": "2023-06-01", "content-type": "application/json"},
                json={"model": CLAUDE_MODELS["haiku"], "max_tokens": 500, "system": sistema, "messages": messages}
            )
            data = r.json()
            return data.get("content", [{}])[0].get("text", "")
    except Exception:
        return ""

def stats_claude() -> dict:
    return {"disponivel": bool(ANTHROPIC_API_KEY), "modelos": list(CLAUDE_MODELS.keys()), "plugin": "claude v1.0"}
