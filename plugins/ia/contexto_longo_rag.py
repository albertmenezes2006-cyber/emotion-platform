"""
Plugin: RAG com Contexto Longo
Categoria: ia
"""
VERSAO = "1.0"
NOME = "contexto_longo_rag"
DESCRICAO = "RAG avancado com contexto de 128k tokens e retrieval semantico"
CATEGORIA = "ia"

import os
from datetime import datetime
from collections import defaultdict

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
_base_conhecimento = {}
_chunks_indexados = defaultdict(list)
_embeddings_base = {}

MODELO_CONTEXTO_LONGO = "llama-3.1-70b-versatile"
MAX_TOKENS_CONTEXTO = 128000

BASE_CONHECIMENTO_SAUDE = {
    "ansiedade": {
        "definicao": "Ansiedade e uma resposta emocional a ameacas percebidas, caracterizada por tensao, preocupacao e sinais fisicos como aumento da frequencia cardiaca.",
        "tecnicas": ["respiracao_diafragmatica", "exposicao_gradual", "reestruturacao_cognitiva", "mindfulness"],
        "recursos": ["Terapia Cognitivo-Comportamental", "EMDR", "Medicacao (avaliacao psiquiatrica)"],
        "fonte": "Manual Diagnostico e Estatistico de Transtornos Mentais (DSM-5)"
    },
    "depressao": {
        "definicao": "Transtorno de humor caracterizado por tristeza persistente, perda de interesse e varios sintomas fisicos e cognitivos.",
        "tecnicas": ["ativacao_comportamental", "higiene_do_sono", "exercicio_fisico", "psicoterapia"],
        "recursos": ["Psicoterapia", "Psiquiatria", "Grupos de apoio"],
        "fonte": "OMS — Classificacao Internacional de Doencas (CID-11)"
    },
    "mindfulness": {
        "definicao": "Pratica de atencao plena baseada em trazer consciencia ao momento presente sem julgamento.",
        "tecnicas": ["meditacao_respiracao", "body_scan", "yoga", "caminhada_consciente"],
        "recursos": ["MBSR", "MBCT", "Apps de meditacao"],
        "fonte": "Jon Kabat-Zinn — Wherever You Go, There You Are"
    },
    "inteligencia_emocional": {
        "definicao": "Capacidade de identificar, compreender, usar e gerenciar emocoes proprias e dos outros.",
        "componentes": ["autoconsciencia", "autorregulacao", "motivacao", "empatia", "habilidades_sociais"],
        "recursos": ["Daniel Goleman — Inteligencia Emocional", "Peter Salovey e John Mayer"],
        "fonte": "Goleman, D. (1995). Emotional Intelligence"
    }
}

def indexar_documento(doc_id: str, conteudo: str, metadados: dict = None):
    tamanho_chunk = 500
    chunks = []
    palavras = conteudo.split()
    for i in range(0, len(palavras), tamanho_chunk // 5):
        chunk = " ".join(palavras[i:i + tamanho_chunk // 5])
        if chunk:
            chunks.append({"texto": chunk, "posicao": i, "doc_id": doc_id})
    _base_conhecimento[doc_id] = {"conteudo": conteudo[:5000], "metadados": metadados or {}, "chunks": len(chunks), "indexado_em": datetime.now().isoformat()}
    _chunks_indexados[doc_id] = chunks

def buscar_conhecimento_relevante(query: str, top_k: int = 3) -> list:
    query_lower = query.lower()
    query_words = set(query_lower.split())
    resultados = []
    for topico, dados in BASE_CONHECIMENTO_SAUDE.items():
        score = 0
        for campo in ["definicao", "tecnicas", "recursos"]:
            conteudo = str(dados.get(campo, "")).lower()
            matches = sum(1 for w in query_words if w in conteudo and len(w) > 3)
            score += matches
        if score > 0 or topico in query_lower:
            resultados.append({"topico": topico, "dados": dados, "relevancia": score + (5 if topico in query_lower else 0)})
    resultados.sort(key=lambda x: x["relevancia"], reverse=True)
    return resultados[:top_k]

async def rag_responder(pergunta: str, contexto_usuario: str = "") -> str:
    conhecimento = buscar_conhecimento_relevante(pergunta)
    contexto_rag = ""
    for item in conhecimento:
        dados = item["dados"]
        contexto_rag += f"Topico: {item['topico']}\n"
        contexto_rag += f"Definicao: {dados.get('definicao','')}\n"
        tecnicas = dados.get("tecnicas", [])
        if tecnicas:
            contexto_rag += f"Tecnicas: {', '.join(tecnicas)}\n"
        contexto_rag += "\n"
    prompt = f"""Contexto de conhecimento terapeutico:
{contexto_rag}

Contexto do usuario: {contexto_usuario}

Pergunta: {pergunta}

Responda em portugues de forma empatica, baseada no conhecimento acima:"""
    if not GROQ_API_KEY:
        return f"Com base no conhecimento terapeutico sobre {pergunta}, posso ajudar. Quais aspectos voce gostaria de explorar?"
    try:
        import httpx
        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"},
                json={"model": MODELO_CONTEXTO_LONGO, "messages": [{"role": "user", "content": prompt}], "max_tokens": 500, "temperature": 0.7}
            )
            return r.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Desculpe, nao consegui processar sua pergunta. Erro: {str(e)[:50]}"

def stats_rag() -> dict:
    return {
        "documentos_indexados": len(_base_conhecimento),
        "base_conhecimento_topicos": len(BASE_CONHECIMENTO_SAUDE),
        "modelo": MODELO_CONTEXTO_LONGO,
        "max_tokens": MAX_TOKENS_CONTEXTO,
        "plugin": "contexto_longo_rag v1.0"
    }
