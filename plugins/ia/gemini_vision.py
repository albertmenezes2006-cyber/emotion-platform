"""
Plugin: Gemini Pro Vision
Categoria: ia
"""
VERSAO = "1.0"
NOME = "gemini_vision"
DESCRICAO = "Google Gemini Pro Vision — analise multimodal"
CATEGORIA = "ia"

import os, httpx, base64

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_VISION_MODEL = "gemini-1.5-flash"

async def gemini_analisar_imagem(imagem_bytes: bytes, prompt: str) -> str:
    if not GEMINI_API_KEY:
        return ""
    try:
        img_b64 = base64.b64encode(imagem_bytes).decode()
        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.post(
                f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_VISION_MODEL}:generateContent?key={GEMINI_API_KEY}",
                json={"contents": [{"parts": [
                    {"text": prompt},
                    {"inline_data": {"mime_type": "image/jpeg", "data": img_b64}}
                ]}]}
            )
            data = r.json()
            return data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
    except Exception as e:
        print(f"Gemini Vision erro: {e}")
        return ""

async def gemini_emocao_facial(imagem_bytes: bytes) -> dict:
    prompt = """Analise a emocao facial. JSON: {"emocao": "string", "intensidade": 1-5, "confianca": 0.0-1.0}"""
    resultado = await gemini_analisar_imagem(imagem_bytes, prompt)
    try:
        import json, re
        m = re.search(r'\{.*\}', resultado, re.DOTALL)
        if m:
            return json.loads(m.group())
    except Exception:
        pass
    return {"emocao": "neutro", "intensidade": 3, "confianca": 0.5}

async def gemini_analisar_audio_emocao(audio_bytes: bytes) -> str:
    audio_b64 = base64.b64encode(audio_bytes).decode()
    if not GEMINI_API_KEY:
        return ""
    try:
        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.post(
                f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key={GEMINI_API_KEY}",
                json={"contents": [{"parts": [
                    {"text": "Transcreva e analise a emocao neste audio em portugues"},
                    {"inline_data": {"mime_type": "audio/wav", "data": audio_b64}}
                ]}]}
            )
            return r.json().get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
    except Exception:
        return ""

def stats_gemini_vision() -> dict:
    return {"disponivel": bool(GEMINI_API_KEY), "modelo": GEMINI_VISION_MODEL, "vision": True, "audio": True}
