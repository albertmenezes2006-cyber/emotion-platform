"""
Plugin: Perplexity API
Categoria: ia
"""
VERSAO = "1.0"
NOME = "perplexity"
DESCRICAO = "Perplexity — busca e respostas com fontes em tempo real"
CATEGORIA = "ia"

import os, httpx

PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY", "")
PERPLEXITY_MODELS = {
    "fast":   "llama-3.1-sonar-small-128k-online",
    "large":  "llama-3.1-sonar-large-128k-online",
    "chat":   "llama-3.1-sonar-small-128k-chat",
}

async def perplexity_buscar(query: str, modelo: str = "fast") -> dict:
    if not PERPLEXITY_API_KEY:
        return {"erro": "Perplexity nao configurado"}
    try:
        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.post(
                "https://api.perplexity.ai/chat/completions",
                headers={"Authorization": f"Bearer {PERPLEXITY_API_KEY}", "Content-Type": "application/json"},
                json={
                    "model": PERPLEXITY_MODELS.get(modelo, PERPLEXITY_MODELS["fast"]),
                    "messages": [{"role": "user", "content": query}],
                    "max_tokens": 500,
                    "return_citations": True,
                }
            )
            data = r.json()
            resposta = data["choices"][0]["message"]["content"]
            citacoes = data.get("citations", [])
            return {"resposta": resposta, "citacoes": citacoes, "modelo": modelo}
    except Exception as e:
        return {"erro": str(e)}

async def perplexity_pesquisar_emocao(emocao: str) -> dict:
    query = f"O que e {emocao} em psicologia? Como lidar? Pesquisa recente em portugues"
    return await perplexity_buscar(query)

async def perplexity_noticias_saude_mental() -> dict:
    query = "Noticias recentes sobre saude mental e bem-estar em 2025"
    return await perplexity_buscar(query, "large")

def stats_perplexity() -> dict:
    return {"disponivel": bool(PERPLEXITY_API_KEY), "modelos": list(PERPLEXITY_MODELS.keys()), "online": True}
