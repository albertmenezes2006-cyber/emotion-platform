"""
Plugin: Groq Vision — LLaVA
Categoria: ia
"""
VERSAO = "1.0"
NOME = "groq_vision"
DESCRICAO = "Groq com LLaVA para analise de imagens e expressoes"
CATEGORIA = "ia"

import os, httpx, base64

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
LLAVA_MODEL = "llava-v1.5-7b-4096-preview"

async def groq_analisar_imagem(imagem_bytes: bytes, prompt: str) -> str:
    if not GROQ_API_KEY:
        return ""
    try:
        img_b64 = base64.b64encode(imagem_bytes).decode()
        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"},
                json={
                    "model": LLAVA_MODEL,
                    "messages": [{"role": "user", "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_b64}"}}
                    ]}],
                    "max_tokens": 300,
                    "temperature": 0.3
                }
            )
            return r.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Groq Vision erro: {e}")
        return ""

async def groq_emocao_facial(imagem_bytes: bytes) -> dict:
    prompt = "Analise a expressao facial. Responda em JSON: {emocao, intensidade 1-5, confianca 0-1}"
    resultado = await groq_analisar_imagem(imagem_bytes, prompt)
    try:
        import json, re
        m = re.search(r'\{.*\}', resultado, re.DOTALL)
        if m:
            return json.loads(m.group())
    except Exception:
        pass
    return {"emocao": "neutro", "intensidade": 3, "confianca": 0.5}

def stats_groq_vision() -> dict:
    return {"disponivel": bool(GROQ_API_KEY), "modelo": LLAVA_MODEL, "vision": True}
