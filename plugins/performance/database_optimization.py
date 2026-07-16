"""
Plugin: Otimizacao de Banco de Dados
Categoria: performance
"""
VERSAO = "1.0"
NOME = "database_optimization"
DESCRICAO = "Indices, query optimization, connection pooling e cache de queries"
CATEGORIA = "performance"

import time
from collections import defaultdict
from datetime import datetime

_query_stats = defaultdict(list)
_slow_queries = []
_index_sugestoes = []
SLOW_QUERY_THRESHOLD_MS = 500

def registrar_query(query_hash: str, duracao_ms: float, tabela: str = "", linhas: int = 0):
    _query_stats[query_hash].append({"duracao_ms": duracao_ms, "tabela": tabela, "linhas": linhas, "ts": datetime.now().isoformat()})
    if duracao_ms > SLOW_QUERY_THRESHOLD_MS:
        _slow_queries.append({"query_hash": query_hash, "duracao_ms": duracao_ms, "tabela": tabela, "ts": datetime.now().isoformat()})
        if len(_slow_queries) > 100:
            _slow_queries.pop(0)

def analisar_slow_queries() -> list:
    agrupado = defaultdict(list)
    for q in _slow_queries:
        agrupado[q["query_hash"]].append(q["duracao_ms"])
    resultado = []
    for query_hash, duracoes in agrupado.items():
        resultado.append({"query_hash": query_hash, "ocorrencias": len(duracoes), "media_ms": round(sum(duracoes)/len(duracoes),1), "max_ms": max(duracoes)})
    return sorted(resultado, key=lambda x: x["media_ms"], reverse=True)[:10]

def sugerir_indices(tabela: str, colunas_filtro: list) -> list:
    sugestoes = []
    for col in colunas_filtro:
        sugestoes.append({"tabela": tabela, "coluna": col, "sql": f"CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_{tabela}_{col} ON {tabela} ({col});", "impacto_estimado": "alto"})
    _index_sugestoes.extend(sugestoes)
    return sugestoes

INDICES_RECOMENDADOS = [
    "CREATE INDEX IF NOT EXISTS idx_analises_usuario_data ON analises (usuario_id, created_at DESC);",
    "CREATE INDEX IF NOT EXISTS idx_mensagens_usuario ON mensagens (usuario_id, criado_em DESC);",
    "CREATE INDEX IF NOT EXISTS idx_diarios_usuario ON diarios (usuario_id, created_at DESC);",
    "CREATE INDEX IF NOT EXISTS idx_usuarios_email ON usuarios (email);",
    "CREATE INDEX IF NOT EXISTS idx_usuarios_plano ON usuarios (plano);",
    "CREATE INDEX IF NOT EXISTS idx_pagamentos_usuario ON pagamentos (usuario_id, created_at DESC);",
    "CREATE INDEX IF NOT EXISTS idx_conquistas_usuario ON conquistas (usuario_id);",
    "CREATE INDEX IF NOT EXISTS idx_notificacoes_usuario ON notificacoes (usuario_id, lida);",
]

def gerar_script_otimizacao() -> str:
    return "\n".join(INDICES_RECOMENDADOS)

def configurar_pgbouncer() -> dict:
    return {
        "pool_mode": "transaction",
        "max_client_conn": 100,
        "default_pool_size": 20,
        "reserve_pool_size": 5,
        "pool_size": 10,
        "config_exemplo": "[databases]\nemotion_db = host=localhost dbname=emotion_platform\n[pgbouncer]\npool_mode = transaction\nmax_client_conn = 100\ndefault_pool_size = 20"
    }

def stats_database_opt() -> dict:
    return {
        "queries_monitoradas": len(_query_stats),
        "slow_queries": len(_slow_queries),
        "indices_recomendados": len(INDICES_RECOMENDADOS),
        "threshold_slow_ms": SLOW_QUERY_THRESHOLD_MS,
        "plugin": "database_optimization v1.0"
    }
