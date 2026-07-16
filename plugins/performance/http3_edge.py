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
_preload_queue = []

# ── Configuracoes de performance
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

# ── Brotli compressao
def configurar_brotli() -> dict:
    try:
        import brotli
        return {"disponivel": True, "nivel_compressao": 4}
    except ImportError:
        return {"disponivel": False, "alternativa": "gzip", "nota": "pip install brotli"}

# ── Edge Cache
def edge_cache_set(chave: str, valor, ttl: int = 300):
    _cache_edge[chave] = {"valor": valor, "expira": time.time() + ttl, "criado_em": datetime.now().isoformat()}

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
    return {"entradas_ativas": ativas, "total": len(_cache_edge), "ttl_padrao": PERFORMANCE_CONFIG["edge_cache_ttl"]}

# ── Critical CSS
CRITICAL_CSS = """
:root{--primary:#6c63ff;--bg:#1a1a2e;--text:#e0e0e0}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,sans-serif;background:var(--bg);color:var(--text)}
.btn{display:inline-flex;align-items:center;padding:.75rem 1.5rem;border-radius:.5rem;border:none;cursor:pointer;font-weight:600}
.btn-primary{background:var(--primary);color:#fff}
.card{background:#16213e;border-radius:1rem;padding:1.5rem;margin-bottom:1rem}
.skeleton{background:linear-gradient(90deg,#1a1a2e 25%,#16213e 50%,#1a1a2e 75%);background-size:200%;animation:shimmer 1.5s infinite}
@keyframes shimmer{0%{background-position:200%}100%{background-position:-200%}}
"""

def gerar_link_preload(recursos: list) -> str:
    links = []
    for r in recursos:
        tipo = r.get("tipo","style")
        url = r.get("url","")
        links.append(f'<link rel="preload" href="{url}" as="{tipo}">')
    return "
".join(links)

# ── Image Optimization
def otimizar_url_imagem(url: str, largura: int = 800, formato: str = "webp", qualidade: int = 85) -> str:
    if not url:
        return url
    if "cloudinary.com" in url:
        partes = url.split("/upload/")
        if len(partes) == 2:
            return f"{partes[0]}/upload/w_{largura},f_{formato},q_{qualidade}/{partes[1]}"
    return url

def gerar_srcset(url_base: str, larguras: list = None) -> str:
    larguras = larguras or [320, 640, 768, 1024, 1280]
    partes = []
    for l in larguras:
        url_otimizada = otimizar_url_imagem(url_base, l)
        partes.append(f"{url_otimizada} {l}w")
    return ", ".join(partes)

# ── Performance Metrics
def registrar_metrica_performance(endpoint: str, duracao_ms: float, cache_hit: bool = False):
    _metricas_performance[endpoint].append({
        "duracao_ms": duracao_ms,
        "cache_hit": cache_hit,
        "ts": datetime.now().isoformat()
    })
    if len(_metricas_performance[endpoint]) > 100:
        _metricas_performance[endpoint].pop(0)

def analisar_performance() -> dict:
    resultado = {}
    for endpoint, metricas in _metricas_performance.items():
        if not metricas:
            continue
        duracoes = [m["duracao_ms"] for m in metricas]
        cache_hits = sum(1 for m in metricas if m["cache_hit"])
        resultado[endpoint] = {
            "media_ms": round(sum(duracoes)/len(duracoes), 1),
            "max_ms": max(duracoes),
            "min_ms": min(duracoes),
            "cache_hit_rate": round(cache_hits/len(metricas)*100, 1),
            "amostras": len(metricas)
        }
    return resultado

def score_performance_global() -> dict:
    todas_metricas = []
    for metricas in _metricas_performance.values():
        todas_metricas.extend([m["duracao_ms"] for m in metricas])
    if not todas_metricas:
        return {"score": 100, "status": "sem_dados"}
    media_global = sum(todas_metricas) / len(todas_metricas)
    score = 100 if media_global < 200 else 80 if media_global < 500 else 60 if media_global < 1000 else 40
    return {
        "score": score,
        "media_ms": round(media_global, 1),
        "status": "excelente" if score >= 90 else "bom" if score >= 70 else "regular" if score >= 50 else "lento",
        "recomendacao": "Cache mais agressivo" if score < 70 else "Performance OK"
    }

def stats_performance() -> dict:
    return {
        "config": PERFORMANCE_CONFIG,
        "brotli": configurar_brotli(),
        "edge_cache": edge_cache_stats(),
        "score": score_performance_global(),
        "plugin": "http3_edge v1.0"
    }
