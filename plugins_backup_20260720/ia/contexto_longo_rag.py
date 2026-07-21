"""
Plugin: Contexto Longo RAG
Categoria: ia
Descrição: Retrieval-Augmented Generation para contexto longo em conversas terapêuticas
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid
import hashlib
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/rag", tags=["ia"])

documentos_db = {}
chunks_db = {}
indices_db = {}
consultas_log = []


class ContextoLongoRAGPlugin(PluginBase):
    name = "contexto_longo_rag"
    version = "1.0.0"
    description = "RAG para contexto longo em conversas terapêuticas"
    category = "ia"

    def setup(self, app):
        app.include_router(router)
        logger.info(f"[{self.name}] Plugin carregado com sucesso")

    def health_check(self):
        return {
            "status": "healthy",
            "documentos": len(documentos_db),
            "chunks": len(chunks_db),
            "consultas_realizadas": len(consultas_log)
        }


@router.post("/documento/indexar")
async def indexar_documento(
    titulo: str,
    conteudo: str,
    categoria: str = "geral",
    user_id: str = "system",
    metadata: dict = None
):
    """Indexa um documento para RAG"""
    doc_id = str(uuid.uuid4())[:8]

    # Criar chunks
    chunks = _criar_chunks(conteudo, tamanho=500, overlap=50)
    chunk_ids = []

    for i, chunk_texto in enumerate(chunks):
        chunk_id = f"{doc_id}_c{i}"
        chunks_db[chunk_id] = {
            "id": chunk_id,
            "doc_id": doc_id,
            "texto": chunk_texto,
            "posicao": i,
            "hash": hashlib.md5(chunk_texto.encode()).hexdigest()[:8],
            "palavras_chave": _extrair_palavras_chave(chunk_texto),
            "tamanho": len(chunk_texto)
        }
        chunk_ids.append(chunk_id)

    documentos_db[doc_id] = {
        "id": doc_id,
        "titulo": titulo,
        "categoria": categoria,
        "user_id": user_id,
        "total_chunks": len(chunks),
        "chunk_ids": chunk_ids,
        "tamanho_original": len(conteudo),
        "metadata": metadata or {},
        "indexado_em": datetime.utcnow().isoformat()
    }

    # Atualizar índice invertido
    for chunk_id in chunk_ids:
        chunk = chunks_db[chunk_id]
        for palavra in chunk["palavras_chave"]:
            if palavra not in indices_db:
                indices_db[palavra] = []
            indices_db[palavra].append(chunk_id)

    return {
        "doc_id": doc_id,
        "chunks_criados": len(chunks),
        "status": "documento indexado com sucesso"
    }


@router.post("/consultar")
async def consultar_rag(
    query: str,
    top_k: int = 5,
    categoria: str = None,
    user_id: str = None
):
    """Consulta RAG — busca chunks relevantes para a query"""
    # Extrair palavras-chave da query
    palavras_query = _extrair_palavras_chave(query)

    # Buscar chunks relevantes usando índice invertido
    scores_chunks = {}
    for palavra in palavras_query:
        chunk_ids = indices_db.get(palavra, [])
        for cid in chunk_ids:
            scores_chunks[cid] = scores_chunks.get(cid, 0) + 1

    # Filtrar por categoria se especificado
    if categoria:
        docs_categoria = {d["id"] for d in documentos_db.values() if d["categoria"] == categoria}
        scores_chunks = {
            cid: score for cid, score in scores_chunks.items()
            if chunks_db.get(cid, {}).get("doc_id") in docs_categoria
        }

    # Ordenar por relevância
    ranking = sorted(scores_chunks.items(), key=lambda x: x[1], reverse=True)[:top_k]

    resultados = []
    for chunk_id, score in ranking:
        chunk = chunks_db.get(chunk_id)
        if chunk:
            doc = documentos_db.get(chunk["doc_id"], {})
            resultados.append({
                "chunk_id": chunk_id,
                "texto": chunk["texto"],
                "score_relevancia": score / len(palavras_query) if palavras_query else 0,
                "documento": doc.get("titulo", ""),
                "categoria": doc.get("categoria", "")
            })

    # Log da consulta
    consultas_log.append({
        "query": query,
        "resultados": len(resultados),
        "timestamp": datetime.utcnow().isoformat()
    })

    # Gerar contexto combinado
    contexto_combinado = "\n\n".join([r["texto"] for r in resultados])

    return {
        "query": query,
        "total_resultados": len(resultados),
        "resultados": resultados,
        "contexto_combinado": contexto_combinado[:3000],
        "palavras_chave_usadas": palavras_query
    }


@router.post("/gerar-resposta")
async def gerar_resposta_com_contexto(
    pergunta: str,
    top_k: int = 3
):
    """Gera resposta usando contexto RAG (simulação)"""
    # Buscar contexto
    busca = await consultar_rag(query=pergunta, top_k=top_k)

    contexto = busca.get("contexto_combinado", "")

    # Resposta simulada (em produção, enviaria para LLM)
    resposta = {
        "pergunta": pergunta,
        "contexto_usado": len(contexto) > 0,
        "chunks_relevantes": busca["total_resultados"],
        "resposta": f"[Resposta baseada em {busca['total_resultados']} chunks relevantes]" if contexto
                    else "Não encontrei informações relevantes na base de conhecimento.",
        "fontes": [r["documento"] for r in busca["resultados"]],
        "confianca": min(0.95, busca["total_resultados"] * 0.2) if busca["total_resultados"] > 0 else 0.1
    }

    return resposta


@router.get("/documentos")
async def listar_documentos(categoria: str = None):
    """Lista documentos indexados"""
    docs = list(documentos_db.values())
    if categoria:
        docs = [d for d in docs if d["categoria"] == categoria]

    return {
        "total": len(docs),
        "documentos": [{
            "id": d["id"],
            "titulo": d["titulo"],
            "categoria": d["categoria"],
            "chunks": d["total_chunks"],
            "tamanho": d["tamanho_original"],
            "indexado_em": d["indexado_em"]
        } for d in docs]
    }


@router.delete("/documento/{doc_id}")
async def remover_documento(doc_id: str):
    """Remove um documento e seus chunks"""
    if doc_id not in documentos_db:
        raise HTTPException(status_code=404, detail="Documento não encontrado")

    doc = documentos_db[doc_id]
    # Remover chunks
    for cid in doc["chunk_ids"]:
        if cid in chunks_db:
            del chunks_db[cid]

    del documentos_db[doc_id]
    return {"status": "documento removido", "chunks_removidos": len(doc["chunk_ids"])}


@router.get("/stats")
async def stats_rag():
    """Estatísticas do sistema RAG"""
    return {
        "documentos": len(documentos_db),
        "chunks_total": len(chunks_db),
        "termos_indexados": len(indices_db),
        "consultas_realizadas": len(consultas_log),
        "categorias": list(set(d["categoria"] for d in documentos_db.values()))
    }


def _criar_chunks(texto: str, tamanho: int = 500, overlap: int = 50) -> list:
    """Divide texto em chunks com overlap"""
    if len(texto) <= tamanho:
        return [texto]

    chunks = []
    inicio = 0
    while inicio < len(texto):
        fim = min(inicio + tamanho, len(texto))
        chunk = texto[inicio:fim]
        chunks.append(chunk.strip())
        inicio += tamanho - overlap

    return chunks


def _extrair_palavras_chave(texto: str) -> list:
    """Extrai palavras-chave relevantes"""
    stopwords = {
        "de", "da", "do", "em", "no", "na", "um", "uma", "o", "a", "os", "as",
        "e", "ou", "que", "para", "por", "com", "se", "não", "mais", "mas",
        "como", "foi", "ser", "ter", "são", "está", "isso", "este", "esta",
        "the", "is", "are", "was", "were", "and", "or", "but", "in", "on",
        "at", "to", "for", "of", "with", "by", "from", "it", "this", "that"
    }
    palavras = texto.lower().split()
    palavras = [p.strip(".,!?;:()[]{}\"'") for p in palavras]
    palavras = [p for p in palavras if len(p) > 2 and p not in stopwords]
    return list(set(palavras))[:30]


plugin = ContextoLongoRAGPlugin()
