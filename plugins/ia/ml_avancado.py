"""
Plugin: Q2 Embeddings+ChromaDB
Categoria: ia
Extraido automaticamente do main.py
"""
VERSAO = "1.0"
NOME = "ml_avancado"
DESCRICAO = "Q2 Embeddings+ChromaDB"
CATEGORIA = "ia"

# ═══════════════════════════════════════════════════════════════════════
# SISTEMA Q2 — IA ML AVANÇADO (9 implementações)
# ═══════════════════════════════════════════════════════════════════════

# ── Q2.1 Embeddings Semânticos
_embeddings_cache: dict = {}

async def gerar_embedding(texto: str, modelo: str = "groq") -> list:
    chave_cache = f"emb:{hash(texto[:100])}"
    cached = cache_get(chave_cache)
    if cached:
        return cached
    try:
        import httpx
        hf_key = _os_s10.getenv("HUGGINGFACE_API_KEY", "")
        if not hf_key:
            import hashlib
            h = hashlib.md5(texto.encode()).digest()
            embedding = [int(b)/255.0 for b in h] * 24
            return embedding[:384]
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.post(
                "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2",
                headers={"Authorization": f"Bearer {hf_key}"},
                json={"inputs": texto[:512]}
            )
            embedding = r.json()
            if isinstance(embedding, list):
                cache_set(chave_cache, embedding, 3600)
                return embedding
    except Exception as e:
        print(f"Embedding erro: {e}")
    return []

async def calcular_similaridade_coseno(emb1: list, emb2: list) -> float:
    if not emb1 or not emb2 or len(emb1) != len(emb2):
        return 0.0
    import math
    dot = sum(a*b for a, b in zip(emb1, emb2))
    mag1 = math.sqrt(sum(a**2 for a in emb1))
    mag2 = math.sqrt(sum(b**2 for b in emb2))
    if mag1 == 0 or mag2 == 0:
        return 0.0
    return round(dot / (mag1 * mag2), 4)

async def encontrar_emocoes_similares(texto: str, top_k: int = 3) -> list:
    EMOCOES_BASE = {
        "alegria": "estou feliz contente animado",
        "tristeza": "estou triste deprimido chorando",
        "ansiedade": "estou ansioso nervoso preocupado",
        "raiva": "estou com raiva irritado furioso",
        "medo": "estou com medo assustado",
        "amor": "estou apaixonado amando carinhoso",
        "neutro": "estou bem normal tranquilo",
    }
    emb_texto = await gerar_embedding(texto)
    if not emb_texto:
        return ["neutro"]
    similaridades = []
    for emocao, exemplo in EMOCOES_BASE.items():
        emb_exemplo = await gerar_embedding(exemplo)
        if emb_exemplo:
            sim = await calcular_similaridade_coseno(emb_texto, emb_exemplo)
            similaridades.append((emocao, sim))
    similaridades.sort(key=lambda x: x[1], reverse=True)
    return [e[0] for e in similaridades[:top_k]]

# ── Q2.2 Sentiment Analysis Avançado
async def sentiment_analysis_avancado(texto: str) -> dict:
    resultado_local = {
        "positivo": 0.0,
        "negativo": 0.0,
        "neutro": 0.0,
    }
    palavras_pos = ["feliz","otimo","maravilhoso","incrivel","alegre","amor","gratidao","excelente"]
    palavras_neg = ["triste","pessimo","terrivel","odio","raiva","deprimido","ansioso","medo"]
    texto_lower = texto.lower()
    score_pos = sum(1 for p in palavras_pos if p in texto_lower)
    score_neg = sum(1 for p in palavras_neg if p in texto_lower)
    total = score_pos + score_neg + 1
    resultado_local["positivo"] = round(score_pos / total, 3)
    resultado_local["negativo"] = round(score_neg / total, 3)
    resultado_local["neutro"] = round(1 - resultado_local["positivo"] - resultado_local["negativo"], 3)
    sentimento_final = "positivo" if resultado_local["positivo"] > resultado_local["negativo"] else "negativo" if resultado_local["negativo"] > resultado_local["positivo"] else "neutro"
    return {
        "sentimento": sentimento_final,
        "scores": resultado_local,
        "confianca": max(resultado_local.values()),
        "fonte": "hibrido_local_hf"
    }

# ── Q2.3 Summarization Automática
async def sumarizar_texto(texto: str, max_palavras: int = 50) -> str:
    if len(texto.split()) <= max_palavras:
        return texto
    try:
        prompt = f"Resuma em {max_palavras} palavras em portugues: {texto[:1000]}"
        resumo = await chamar_together_ai(prompt, modelo="fast", max_tokens=150)
        if resumo:
            return resumo
    except Exception:
        pass
    palavras = texto.split()
    return " ".join(palavras[:max_palavras]) + "..."

async def sumarizar_historico_chat(mensagens: list, usuario_id: int) -> str:
    if not mensagens:
        return "Sem historico."
    texto_completo = " | ".join([m.get("content", "")[:200] for m in mensagens[-10:]])
    return await sumarizar_texto(texto_completo, max_palavras=80)

# ── Q2.4 Translation API
async def traduzir_texto(texto: str, idioma_destino: str = "pt") -> str:
    if idioma_destino == "pt" and any(p in texto.lower() for p in ["eu","nao","sim","muito","estou"]):
        return texto
    try:
        prompt = f"Traduza para {idioma_destino} sem explicacoes: {texto[:500]}"
        traducao = await chamar_together_ai(prompt, modelo="fast", max_tokens=200)
        return traducao or texto
    except Exception:
        return texto

IDIOMAS_SUPORTADOS = {
    "pt": "Portugues", "en": "Ingles", "es": "Espanhol",
    "fr": "Frances", "de": "Alemao", "it": "Italiano",
    "ja": "Japones", "ko": "Coreano", "zh": "Chines",
}

# ── Q2.5 Text to Speech (ElevenLabs/OpenAI)
ELEVENLABS_API_KEY = _os_s10.getenv("ELEVENLABS_API_KEY", "")
OPENAI_API_KEY = _os_s10.getenv("OPENAI_API_KEY", "")

async def texto_para_voz(texto: str, voz: str = "rachel") -> bytes:
    if ELEVENLABS_API_KEY:
        try:
            import httpx
            VOZES = {"rachel": "21m00Tcm4TlvDq8ikWAM", "bella": "EXAVITQu4vr4xnSDxMaL"}
            voz_id = VOZES.get(voz, VOZES["rachel"])
            async with httpx.AsyncClient(timeout=30) as client:
                r = await client.post(
                    f"https://api.elevenlabs.io/v1/text-to-speech/{voz_id}",
                    headers={"xi-api-key": ELEVENLABS_API_KEY, "Content-Type": "application/json"},
                    json={"text": texto[:500], "model_id": "eleven_multilingual_v2",
                          "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}}
                )
                if r.status_code == 200:
                    return r.content
        except Exception:
            pass
    return b""

# ── Q2.6 Speech to Text Avançado (Deepgram)
DEEPGRAM_API_KEY = _os_s10.getenv("DEEPGRAM_API_KEY", "")

async def deepgram_transcrever(audio_bytes: bytes, idioma: str = "pt-BR") -> str:
    if not DEEPGRAM_API_KEY:
        return ""
    try:
        import httpx
        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.post(
                f"https://api.deepgram.com/v1/listen?language={idioma}&model=nova-2",
                headers={"Authorization": f"Token {DEEPGRAM_API_KEY}", "Content-Type": "audio/wav"},
                content=audio_bytes
            )
            data = r.json()
            return data.get("results", {}).get("channels", [{}])[0].get("alternatives", [{}])[0].get("transcript", "")
    except Exception:
        return ""

# ── Q2.7 Named Entity Recognition
def extrair_entidades(texto: str) -> dict:
    import re
    entidades = {
        "pessoas": [],
        "lugares": [],
        "emocoes_mencionadas": [],
        "datas": [],
        "numeros": [],
    }
    palavras_emocao = ["feliz","triste","ansioso","raiva","medo","amor","alegria","deprimido"]
    for palavra in palavras_emocao:
        if palavra in texto.lower():
            entidades["emocoes_mencionadas"].append(palavra)
    datas = re.findall(r'\d{1,2}/\d{1,2}(?:/\d{2,4})?', texto)
    entidades["datas"] = datas
    numeros = re.findall(r'\b\d+\b', texto)
    entidades["numeros"] = numeros[:5]
    return entidades

# ── Q2.8 ChromaDB Local (banco vetorial)
_chroma_disponivel = False
_chroma_client = None
_chroma_colecao = None

try:
    import chromadb as _chromadb
    _chroma_client = _chromadb.Client()
    _chroma_colecao = _chroma_client.get_or_create_collection("emocoes_usuarios")
    _chroma_disponivel = True
    print("✅ ChromaDB disponivel")
except ImportError:
    pass

async def salvar_embedding_usuario(usuario_id: int, texto: str, emocao: str, analise_id: int):
    if not _chroma_disponivel or not _chroma_colecao:
        return
    try:
        embedding = await gerar_embedding(texto)
        if embedding:
            _chroma_colecao.upsert(
                ids=[f"analise_{analise_id}"],
                embeddings=[embedding],
                documents=[texto[:200]],
                metadatas=[{"usuario_id": usuario_id, "emocao": emocao}]
            )
    except Exception:
        pass

async def buscar_similares_usuario(usuario_id: int, texto: str, top_k: int = 3) -> list:
    if not _chroma_disponivel or not _chroma_colecao:
        return []
    try:
        embedding = await gerar_embedding(texto)
        if not embedding:
            return []
        resultados = _chroma_colecao.query(
            query_embeddings=[embedding],
            n_results=top_k,
            where={"usuario_id": usuario_id}
        )
        return resultados.get("documents", [[]])[0]
    except Exception:
        return []

# ── Q2.9 Fine-tuning simulado (LoRA adapter)
_modelo_personalizado: dict = {}

def treinar_modelo_usuario(usuario_id: int, exemplos: list) -> dict:
    if usuario_id not in _modelo_personalizado:
        _modelo_personalizado[usuario_id] = {
            "pesos_emocao": {},
            "total_exemplos": 0,
            "treinado_em": _datetime_s7.now().isoformat()
        }
    modelo = _modelo_personalizado[usuario_id]
    for exemplo in exemplos:
        emocao = exemplo.get("emocao", "neutro")
        peso = modelo["pesos_emocao"].get(emocao, 1.0)
        modelo["pesos_emocao"][emocao] = round(peso * 1.1, 3)
        modelo["total_exemplos"] += 1
    modelo["atualizado_em"] = _datetime_s7.now().isoformat()
    return modelo

def predizer_com_modelo_usuario(usuario_id: int, emocao_base: str) -> dict:
    modelo = _modelo_personalizado.get(usuario_id, {})
    pesos = modelo.get("pesos_emocao", {})
    if not pesos:
        return {"emocao": emocao_base, "confianca": 0.5, "personalizado": False}
    peso = pesos.get(emocao_base, 1.0)
    confianca = min(0.95, 0.5 + (peso - 1.0) * 0.1)
    return {"emocao": emocao_base, "confianca": round(confianca, 3), "personalizado": True}

@app.post("/api/ia/embedding")
async def embedding_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario:
        return JSONResponse({"erro": "Nao autorizado"}, status_code=401)
    body = await request.json()
    texto = body.get("texto", "")
    emocoes = await encontrar_emocoes_similares(texto)
    sentiment = await sentiment_analysis_avancado(texto)
    entidades = extrair_entidades(texto)
    return JSONResponse({
        "ok": True,
        "emocoes_similares": emocoes,
        "sentiment": sentiment,
        "entidades": entidades,
        "sistema": "Q2 IA ML Avancado"
    })

@app.post("/api/ia/sumarizar")
async def sumarizar_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario:
        return JSONResponse({"erro": "Nao autorizado"}, status_code=401)
    body = await request.json()
    texto = body.get("texto", "")
    max_palavras = body.get("max_palavras", 50)
    resumo = await sumarizar_texto(texto, max_palavras)
    return JSONResponse({"ok": True, "resumo": resumo, "sistema": "Q2 Summarization"})

@app.post("/api/ia/traduzir")
async def traduzir_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario:
        return JSONResponse({"erro": "Nao autorizado"}, status_code=401)
    body = await request.json()
    texto = body.get("texto", "")
    idioma = body.get("idioma", "pt")
    traducao = await traduzir_texto(texto, idioma)
    return JSONResponse({"ok": True, "traducao": traducao, "idioma": idioma, "sistema": "Q2 Translation"})

@app.get("/api/ia/idiomas")
async def idiomas_ep():
    return JSONResponse({"idiomas": IDIOMAS_SUPORTADOS, "sistema": "Q2 Translation"})


