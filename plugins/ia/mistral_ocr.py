"""
Plugin: Mistral OCR e Analise de Documentos
Categoria: ia
"""
VERSAO = "1.0"
NOME = "mistral_ocr"
DESCRICAO = "Mistral para OCR, analise de documentos e textos longos"
CATEGORIA = "ia"

import os, httpx, base64

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "")

async def mistral_completar(mensagem: str, modelo: str = "mistral-small-latest", max_tokens: int = 1000) -> str:
    if not MISTRAL_API_KEY:
        return ""
    try:
        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.post(
                "https://api.mistral.ai/v1/chat/completions",
                headers={"Authorization": f"Bearer {MISTRAL_API_KEY}", "Content-Type": "application/json"},
                json={"model": modelo, "messages": [{"role": "user", "content": mensagem}], "max_tokens": max_tokens}
            )
            return r.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Mistral erro: {e}")
        return ""

async def mistral_analisar_documento(texto_documento: str) -> dict:
    prompt = f"""Analise este documento e extraia informacoes relevantes sobre saude mental e bem-estar.
Responda em JSON: {{"topicos": [], "emocoes_detectadas": [], "urgencia": "baixa/media/alta", "resumo": "string"}}
Documento: {texto_documento[:2000]}"""
    resultado = await mistral_completar(prompt, "mistral-large-latest")
    try:
        import json, re
        m = re.search(r'\{.*\}', resultado, re.DOTALL)
        if m:
            return json.loads(m.group())
    except Exception:
        pass
    return {"topicos": [], "emocoes_detectadas": [], "urgencia": "baixa", "resumo": resultado[:200]}

async def mistral_resumir_sessao(historico_chat: list) -> str:
    textos = [m.get("content", "")[:200] for m in historico_chat[-20:]]
    texto = " | ".join(textos)
    prompt = f"Resuma esta sessao terapeutica em 3 frases focando nos temas principais: {texto}"
    return await mistral_completar(prompt, "mistral-small-latest", 200)

async def mistral_codestral(codigo: str, instrucao: str) -> str:
    prompt = f"Instrucao: {instrucao}\n\nCodigo:\n{codigo[:2000]}"
    return await mistral_completar(prompt, "codestral-latest", 1000)

def stats_mistral_ocr() -> dict:
    return {"disponivel": bool(MISTRAL_API_KEY), "modelos": ["mistral-small", "mistral-large", "codestral"], "plugin": "mistral_ocr v1.0"}
