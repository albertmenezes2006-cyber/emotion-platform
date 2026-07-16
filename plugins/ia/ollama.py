"""
Plugin: Ollama — Modelos Locais
Categoria: ia
"""
VERSAO = "1.0"
NOME = "ollama"
DESCRICAO = "Llama, Mistral, Gemma rodando localmente via Ollama"
CATEGORIA = "ia"

import os, httpx

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODELS = {
    "chat":   "llama3.2:3b",
    "code":   "qwen2.5-coder:7b",
    "embed":  "nomic-embed-text",
    "vision": "llava:7b",
}

async def ollama_disponivel() -> bool:
    try:
        async with httpx.AsyncClient(timeout=3) as client:
            r = await client.get(f"{OLLAMA_URL}/api/tags")
            return r.status_code == 200
    except Exception:
        return False

async def ollama_completar(prompt: str, modelo: str = "chat", stream: bool = False) -> str:
    model_id = OLLAMA_MODELS.get(modelo, modelo)
    try:
        async with httpx.AsyncClient(timeout=60) as client:
            r = await client.post(
                f"{OLLAMA_URL}/api/generate",
                json={"model": model_id, "prompt": prompt, "stream": False}
            )
            return r.json().get("response", "")
    except Exception as e:
        print(f"Ollama erro: {e}")
        return ""

async def ollama_embedding(texto: str) -> list:
    try:
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.post(
                f"{OLLAMA_URL}/api/embeddings",
                json={"model": OLLAMA_MODELS["embed"], "prompt": texto[:512]}
            )
            return r.json().get("embedding", [])
    except Exception:
        return []

async def ollama_listar_modelos() -> list:
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            r = await client.get(f"{OLLAMA_URL}/api/tags")
            return [m["name"] for m in r.json().get("models", [])]
    except Exception:
        return []

async def ollama_analisar_emocao(texto: str) -> dict:
    prompt = f"""Analise em JSON sem explicacoes: {{"emocao": "string", "intensidade": 1-5}}
Texto: {texto[:300]}"""
    resultado = await ollama_completar(prompt, "chat")
    try:
        import json, re
        m = re.search(r'\{.*\}', resultado, re.DOTALL)
        if m:
            return json.loads(m.group())
    except Exception:
        pass
    return {"emocao": "neutro", "intensidade": 3}

def stats_ollama() -> dict:
    return {"url": OLLAMA_URL, "modelos": OLLAMA_MODELS, "plugin": "ollama v1.0"}
