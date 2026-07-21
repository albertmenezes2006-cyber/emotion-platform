"""
Plugin: Midjourney + DALL-E 3 — Geração de Imagens
Categoria: ia
"""
VERSAO = "1.0"
NOME = "midjourney"
DESCRICAO = "Geracao de imagens terapeuticas com DALL-E 3 e Midjourney"
CATEGORIA = "ia"

import os
import httpx

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
REPLICATE_API_KEY = os.getenv("REPLICATE_API_KEY", "")

PROMPTS_TERAPEUTICOS = {
    "alegria":   "peaceful sunny meadow with colorful flowers, warm light, healing atmosphere, watercolor style",
    "tristeza":  "gentle rain on window, cozy interior, soft blue tones, healing and contemplative, watercolor",
    "ansiedade": "calm ocean waves at sunset, breathing space, peaceful horizon, soft colors, watercolor",
    "raiva":     "volcanic landscape transforming into peaceful garden, healing transition, artistic",
    "medo":      "lighthouse in stormy sea providing guidance and safety, warm golden light, watercolor",
    "amor":      "warm sunset with hearts and gentle nature, romantic and healing, watercolor style",
    "neutro":    "zen garden with stones and moss, balance and peace, Japanese art style",
    "estresse":  "deep forest path leading to light, tranquil and healing, watercolor style",
}

async def dalle3_gerar(prompt: str, tamanho: str = "1024x1024") -> dict:
    if not OPENAI_API_KEY:
        return {"erro": "OpenAI nao configurado"}
    try:
        async with httpx.AsyncClient(timeout=60) as client:
            r = await client.post(
                "https://api.openai.com/v1/images/generations",
                headers={"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"},
                json={"model": "dall-e-3", "prompt": prompt, "n": 1, "size": tamanho, "quality": "standard"}
            )
            data = r.json()
            if "data" in data:
                return {"url": data["data"][0]["url"], "sucesso": True, "modelo": "dall-e-3"}
            return {"erro": data.get("error", {}).get("message", "Erro"), "sucesso": False}
    except Exception as e:
        return {"erro": str(e), "sucesso": False}

async def gerar_imagem_terapeutica(emocao: str) -> dict:
    prompt_base = PROMPTS_TERAPEUTICOS.get(emocao, PROMPTS_TERAPEUTICOS["neutro"])
    prompt = f"{prompt_base}, therapeutic art, soothing, professional quality"
    return await dalle3_gerar(prompt)

async def gerar_mandala_emocional(emocao: str, nome: str = "") -> dict:
    prompt = f"Sacred mandala representing {emocao} emotion, intricate geometric patterns, therapeutic colors, spiritual art, high detail"
    if nome:
        prompt += f", personalized for {nome}"
    return await dalle3_gerar(prompt)

def stats_imagens() -> dict:
    return {
        "dalle3": bool(OPENAI_API_KEY),
        "replicate": bool(REPLICATE_API_KEY),
        "emocoes_suportadas": list(PROMPTS_TERAPEUTICOS.keys()),
        "plugin": "midjourney v1.0"
    }
