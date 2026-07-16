"""
Plugin: HTTP/3, Edge Computing e Performance Extrema
Categoria: performance
"""
VERSAO = "1.0"
NOME = "http3_edge"
DESCRICAO = "HTTP/3 QUIC, edge computing, brotli e otimizacoes extremas"
CATEGORIA = "performance"

import os, time
from collections import defaultdict
from datetime import datetime

_metricas_performance = defaultdict(list)
_cache_edge = {}

PERFORMANCE_CONFIG = {
    "http3_habilitado": False,
    "brotli_habilitado": True,
    "preload_habilitado": True,
    "edge_cache_ttl": 300,
    "image_webp": True,
    "critical_css_inline": True,
    "lazy_loading": True,
    "service_worker": True,
}

def configurar_brotli() -> dict:
    try:
        import brotli
        return {"disponivel": True, "nivel_compressao": 4}
    except ImportError:
        return {"disponivel": False, "alternativa": "gzip"}

def edge_cache_set(chave: str, valor, ttl: int = 300):
    _cache_edge[chave] = {"valor": valor, "expira": time.time() + ttl}

def edge_cache_get(chave: str):
    entrada = _cache_edge.get(chave)
    if not entrada:
        return None
    if time.time() > entrada["expira"]:
        del _cache_edge[chave]
        return None
    return entrada["valor"]

def edge_cache_stats() -> dict:
    ativas = sum(1 for v in _cache_edge.values() if time.time() < v["expira"])
    return {"entradas_ativas": ativas, "total": len(_cache_edge)}

CRITICAL_CSS = (
    ":root{--primary:#6c63ff;--bg:#1a1a2e;--text:#e0e0e0}"
    "*{box-sizing:border-box;margin:0;padding:0}"
    "body{font-family:-apple-system,sans-serif;background:var(--bg);color:var(--text)}"
    ".btn{display:inline-flex;align-items:center;padding:.75rem 1.5rem;border-radius:.5rem;border:none;cursor:pointer}"
    ".btn-primary{background:var(--primary);color:#fff}"
    ".card{background:#16213e;border-radius:1rem;padding:1.5rem;margin-bottom:1rem}"
    ".skeleton{background:linear-gradient(90deg,#1a1a2e 25%,#16213e 50%,#1a1a2e 75%);animation:shimmer 1.5s infinite}"
    "@keyframes shimmer{0%{background-position:200%}100%{background-position:-200%}}"
)

def gerar_link_preload(recursos: list) -> str:
    links = []
    for r in recursos:
        tipo = r.get("tipo", "style")
        url = r.get("url", "")
        links.append(f'<link rel="preload" href="{url}" as="{tipo}">')
    return "\n".join(links)

def otimizar_url_imagem(url: str, largura: int = 800, formato: str = "webp", qualidade: int = 85) -> str:
    if not url:
        return url
    if "cloudinary.com" in url:
        partes = url.split("/upload/")
        if len(partes) == 2:
            return f"{partes[0]}/upload/w_{largura},f_{formato},q_{qualidade}/{partes[1]}"
    return url

def registrar_metrica_performance(endpoint: str, duracao_ms: float, cache_hit: bool = False):
    _metricas_performance[endpoint].append({"duracao_ms": duracao_ms, "cache_hit": cache_hit, "ts": datetime.now().isoformat()})
    if len(_metricas_performance[endpoint]) > 100:
        _metricas_performance[endpoint].pop(0)

def score_performance_global() -> dict:
    todas = []
    for metricas in _metricas_performance.values():
        todas.extend([m["duracao_ms"] for m in metricas])
    if not todas:
        return {"score": 100, "status": "sem_dados"}
    media = sum(todas) / len(todas)
    score = 100 if media < 200 else 80 if media < 500 else 60 if media < 1000 else 40
    return {"score": score, "media_ms": round(media, 1), "status": "excelente" if score >= 90 else "bom" if score >= 70 else "lento"}

def stats_performance() -> dict:
    return {
        "config": PERFORMANCE_CONFIG,
        "brotli": configurar_brotli(),
        "edge_cache": edge_cache_stats(),
        "score": score_performance_global(),
        "plugin": "http3_edge v1.0"
    }
