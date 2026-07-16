"""
Plugin: GPT-4o Vision
Categoria: ia
"""
VERSAO = "1.0"
NOME = "gpt4_vision"
DESCRICAO = "OpenAI GPT-4o com visao — analisa imagens e expressoes faciais"
CATEGORIA = "ia"

import os, httpx, base64

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

async def gpt4_completar(mensagem: str, modelo: str = "gpt-4o-mini", max_tokens: int = 500) -> str:
    if not OPENAI_API_KEY:
        return ""
    try:
        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"},
                json={"model": modelo, "messages": [{"role": "user", "content": mensagem}], "max_tokens": max_tokens}
            )
            return r.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"GPT4 erro: {e}")
        return ""

async def gpt4_analisar_imagem(imagem_bytes: bytes, prompt: str = "Analise a expressao facial e emocao desta pessoa") -> dict:
    if not OPENAI_API_KEY:
        return {"erro": "OpenAI nao configurado"}
    try:
        img_b64 = base64.b64encode(imagem_bytes).decode()
        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"},
                json={
                    "model": "gpt-4o",
                    "messages": [{"role": "user", "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_b64}", "detail": "low"}}
                    ]}],
                    "max_tokens": 300
                }
            )
            resultado = r.json()["choices"][0]["message"]["content"]
            return {"analise": resultado, "modelo": "gpt-4o", "sucesso": True}
    except Exception as e:
        return {"erro": str(e), "sucesso": False}

async def gpt4_analisar_emocao_facial(imagem_bytes: bytes) -> dict:
    prompt = """Analise a expressao facial desta imagem.
Responda em JSON: {"emocao": "string", "intensidade": 1-5, "confianca": 0.0-1.0, "descricao": "string"}
Emocoes possiveis: alegria, tristeza, raiva, medo, surpresa, nojo, neutro, ansiedade"""
    resultado = await gpt4_analisar_imagem(imagem_bytes, prompt)
    if resultado.get("sucesso"):
        try:
            import json, re
            m = re.search(r'\{.*\}', resultado["analise"], re.DOTALL)
            if m:
                return json.loads(m.group())
        except Exception:
            pass
    return {"emocao": "neutro", "intensidade": 3, "confianca": 0.5}

def stats_gpt4() -> dict:
    return {"disponivel": bool(OPENAI_API_KEY), "modelos": ["gpt-4o", "gpt-4o-mini"], "vision": True, "plugin": "gpt4_vision v1.0"}
