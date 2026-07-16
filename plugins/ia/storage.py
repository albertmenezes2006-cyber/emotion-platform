"""
Plugin: Q6 Cloudinary+Pinecone
Categoria: ia
Extraido automaticamente do main.py
"""
VERSAO = "1.0"
NOME = "storage"
DESCRICAO = "Q6 Cloudinary+Pinecone"
CATEGORIA = "ia"

# ═══════════════════════════════════════════════════════════════════════
# SISTEMA Q6 — BANCO E STORAGE AVANÇADO (6 implementações)
# ═══════════════════════════════════════════════════════════════════════

CLOUDINARY_URL = _os_s10.getenv("CLOUDINARY_URL", "")
CLOUDINARY_CLOUD_NAME = _os_s10.getenv("CLOUDINARY_CLOUD_NAME", "")
CLOUDINARY_API_KEY_CL = _os_s10.getenv("CLOUDINARY_API_KEY", "")
CLOUDINARY_API_SECRET = _os_s10.getenv("CLOUDINARY_API_SECRET", "")

# ── Q6.1 Cloudinary imagens
async def cloudinary_upload(imagem_bytes: bytes, pasta: str = "emotion_platform") -> dict:
    if not all([CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY_CL, CLOUDINARY_API_SECRET]):
        return {"erro": "Cloudinary nao configurado"}
    try:
        import httpx
        import hashlib
        import time as _t
        from base64 import b64encode
        timestamp = int(_t.time())
        params = f"folder={pasta}&timestamp={timestamp}"
        assinatura = hashlib.sha1(f"{params}{CLOUDINARY_API_SECRET}".encode()).hexdigest()
        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.post(
                f"https://api.cloudinary.com/v1_1/{CLOUDINARY_CLOUD_NAME}/image/upload",
                data={
                    "file": f"data:image/jpeg;base64,{b64encode(imagem_bytes).decode()}",
                    "folder": pasta,
                    "timestamp": timestamp,
                    "api_key": CLOUDINARY_API_KEY_CL,
                    "signature": assinatura
                }
            )
            return r.json()
    except Exception as e:
        return {"erro": str(e)}

async def cloudinary_otimizar_url(url: str, largura: int = 400, qualidade: int = 80) -> str:
    if not CLOUDINARY_CLOUD_NAME or not url:
        return url
    if "cloudinary.com" not in url:
        return url
    partes = url.split("/upload/")
    if len(partes) != 2:
        return url
    return f"{partes[0]}/upload/w_{largura},q_{qualidade},f_auto/{partes[1]}"

# ── Q6.2 Pinecone Vetorial
PINECONE_API_KEY = _os_s10.getenv("PINECONE_API_KEY", "")
PINECONE_ENV = _os_s10.getenv("PINECONE_ENVIRONMENT", "us-east-1-aws")
_pinecone_disponivel = False

try:
    import pinecone as _pinecone_lib
    _pinecone_disponivel = True
except ImportError:
    pass

async def pinecone_upsert(ids: list, embeddings: list, metadatas: list, namespace: str = "emocoes"):
    if not _pinecone_disponivel or not PINECONE_API_KEY:
        return False
    try:
        _pinecone_lib.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
        index = _pinecone_lib.Index("emotion-platform")
        vectors = [(ids[i], embeddings[i], metadatas[i]) for i in range(len(ids))]
        index.upsert(vectors=vectors, namespace=namespace)
        return True
    except Exception:
        return False

async def pinecone_query(embedding: list, top_k: int = 5, namespace: str = "emocoes") -> list:
    if not _pinecone_disponivel or not PINECONE_API_KEY:
        return []
    try:
        _pinecone_lib.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
        index = _pinecone_lib.Index("emotion-platform")
        result = index.query(vector=embedding, top_k=top_k, namespace=namespace, include_metadata=True)
        return result.get("matches", [])
    except Exception:
        return []

# ── Q6.3 Elasticsearch
ELASTICSEARCH_URL = _os_s10.getenv("ELASTICSEARCH_URL", "")

async def elasticsearch_indexar(indice: str, documento_id: str, documento: dict) -> bool:
    if not ELASTICSEARCH_URL:
        return False
    try:
        import httpx
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.put(
                f"{ELASTICSEARCH_URL}/{indice}/_doc/{documento_id}",
                json=documento
            )
            return r.status_code in (200, 201)
    except Exception:
        return False

async def elasticsearch_buscar(indice: str, query: str, campo: str = "texto") -> list:
    if not ELASTICSEARCH_URL:
        return []
    try:
        import httpx
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.post(
                f"{ELASTICSEARCH_URL}/{indice}/_search",
                json={"query": {"match": {campo: query}}, "size": 10}
            )
            hits = r.json().get("hits", {}).get("hits", [])
            return [h.get("_source", {}) for h in hits]
    except Exception:
        return []

# ── Q6.4 Weaviate
WEAVIATE_URL = _os_s10.getenv("WEAVIATE_URL", "")

async def weaviate_criar_objeto(classe: str, propriedades: dict, embedding: list = None) -> dict:
    if not WEAVIATE_URL:
        return {}
    try:
        import httpx
        payload = {"class": classe, "properties": propriedades}
        if embedding:
            payload["vector"] = embedding
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.post(f"{WEAVIATE_URL}/v1/objects", json=payload)
            return r.json()
    except Exception as e:
        return {"erro": str(e)}

# ── Q6.5 MongoDB
MONGODB_URI = _os_s10.getenv("MONGODB_URI", "")
_mongo_client = None
_mongo_disponivel = False

try:
    import pymongo as _pymongo
    if MONGODB_URI:
        _mongo_client = _pymongo.MongoClient(MONGODB_URI, serverSelectionTimeoutMS=2000)
        _mongo_client.admin.command("ping")
        _mongo_disponivel = True
        print("✅ MongoDB conectado")
except Exception:
    pass

def mongo_inserir(colecao: str, documento: dict) -> bool:
    if not _mongo_disponivel or not _mongo_client:
        return False
    try:
        db = _mongo_client["emotion_platform"]
        db[colecao].insert_one(documento)
        return True
    except Exception:
        return False

def mongo_buscar(colecao: str, filtro: dict, limite: int = 10) -> list:
    if not _mongo_disponivel or not _mongo_client:
        return []
    try:
        db = _mongo_client["emotion_platform"]
        return list(db[colecao].find(filtro, {"_id": 0}).limit(limite))
    except Exception:
        return []

# ── Q6.6 Storage Stats
def stats_storage() -> dict:
    return {
        "postgresql": {"status": "conectado", "tipo": "principal"},
        "redis": {"status": "conectado" if _redis_disponivel else "indisponivel", "tipo": "cache"},
        "chromadb": {"status": "ativo" if _chroma_disponivel else "indisponivel", "tipo": "vetorial_local"},
        "pinecone": {"status": "configurado" if PINECONE_API_KEY else "nao_configurado", "tipo": "vetorial_cloud"},
        "elasticsearch": {"status": "configurado" if ELASTICSEARCH_URL else "nao_configurado", "tipo": "busca"},
        "weaviate": {"status": "configurado" if WEAVIATE_URL else "nao_configurado", "tipo": "vetorial_grafo"},
        "mongodb": {"status": "conectado" if _mongo_disponivel else "nao_configurado", "tipo": "documentos"},
        "cloudinary": {"status": "configurado" if CLOUDINARY_CLOUD_NAME else "nao_configurado", "tipo": "imagens"},
    }

@app.get("/api/storage/status")
async def storage_status_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario or usuario.get("plano") != "admin":
        return JSONResponse({"erro": "Nao autorizado"}, status_code=403)
    return JSONResponse({"storage": stats_storage(), "sistema": "Q6 Storage"})

@app.post("/api/cloudinary/upload")
async def cloudinary_upload_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario:
        return JSONResponse({"erro": "Nao autorizado"}, status_code=401)
    try:
        form = await request.form()
        arquivo = form.get("file")
        if not arquivo:
            return JSONResponse({"erro": "Arquivo obrigatorio"}, status_code=400)
        conteudo = await arquivo.read()
        resultado = await cloudinary_upload(conteudo)
        return JSONResponse({"ok": True, "resultado": resultado, "sistema": "Q6 Cloudinary"})
    except Exception as e:
        return JSONResponse({"erro": str(e)}, status_code=500)

@app.get("/api/busca-semantica")
async def busca_semantica_ep(q: str, request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario:
        return JSONResponse({"erro": "Nao autorizado"}, status_code=401)
    resultados_es = await elasticsearch_buscar("analises", q)
    similares = await encontrar_emocoes_similares(q)
    return JSONResponse({
        "query": q,
        "resultados_elasticsearch": resultados_es,
        "emocoes_similares": similares,
        "sistema": "Q6 Busca Semantica"
    })

# ═══ FIM Q4+Q5+Q6 ════════════════════════════════════════════════════




