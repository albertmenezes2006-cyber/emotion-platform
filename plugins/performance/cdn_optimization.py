"""
Plugin: CDN e Otimizacao de Assets
Categoria: performance
"""
VERSAO = "1.0"
NOME = "cdn_optimization"
DESCRICAO = "CDN multi-regiao, otimizacao de assets e cache de navegador"
CATEGORIA = "performance"

import os
from datetime import datetime

CDN_URL = os.getenv("CDN_URL", "")
CLOUDFLARE_ZONE_ID = os.getenv("CLOUDFLARE_ZONE_ID", "")
CLOUDFLARE_API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN", "")

CACHE_HEADERS = {
    "static_assets": "public, max-age=31536000, immutable",
    "api_responses": "no-store, no-cache, must-revalidate",
    "html_pages": "no-cache, must-revalidate",
    "images": "public, max-age=86400, stale-while-revalidate=3600",
    "fonts": "public, max-age=31536000, immutable",
    "manifest": "public, max-age=3600",
}

def obter_url_asset(caminho: str, versao: str = "") -> str:
    if CDN_URL:
        base = CDN_URL.rstrip("/")
        path = caminho.lstrip("/")
        if versao:
            return f"{base}/{path}?v={versao}"
        return f"{base}/{path}"
    return caminho

def gerar_cache_control(tipo: str) -> str:
    return CACHE_HEADERS.get(tipo, CACHE_HEADERS["api_responses"])

async def cloudflare_purge_cache(urls: list) -> dict:
    if not all([CLOUDFLARE_ZONE_ID, CLOUDFLARE_API_TOKEN]):
        return {"erro": "Cloudflare nao configurado"}
    try:
        import httpx
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.post(
                f"https://api.cloudflare.com/client/v4/zones/{CLOUDFLARE_ZONE_ID}/purge_cache",
                headers={"Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}", "Content-Type": "application/json"},
                json={"files": urls[:30]}
            )
            return r.json()
    except Exception as e:
        return {"erro": str(e)}

async def cloudflare_obter_analytics() -> dict:
    if not all([CLOUDFLARE_ZONE_ID, CLOUDFLARE_API_TOKEN]):
        return {}
    try:
        import httpx
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.get(
                f"https://api.cloudflare.com/client/v4/zones/{CLOUDFLARE_ZONE_ID}/analytics/dashboard",
                headers={"Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}"},
                params={"since": "-1440", "until": "0"}
            )
            return r.json().get("result", {})
    except Exception as e:
        return {"erro": str(e)}

def gerar_config_nginx_cdn() -> str:
    return """
# Configuracao Nginx para CDN local
location /static/ {
    alias /app/static/;
    expires 1y;
    add_header Cache-Control "public, max-age=31536000, immutable";
    add_header Vary "Accept-Encoding";
    gzip_static on;
    brotli_static on;
}
location ~* \.(jpg|jpeg|png|gif|webp|svg|ico)$ {
    expires 30d;
    add_header Cache-Control "public, max-age=2592000";
}
location ~* \.(css|js)$ {
    expires 1y;
    add_header Cache-Control "public, max-age=31536000, immutable";
}
"""

def calcular_savings_cdn(requests_por_dia: int, bytes_por_request: int) -> dict:
    cache_hit_rate = 0.85
    requests_servidas_cdn = int(requests_por_dia * cache_hit_rate)
    bytes_economizados = requests_servidas_cdn * bytes_por_request
    return {
        "requests_cdn": requests_servidas_cdn,
        "requests_origem": requests_por_dia - requests_servidas_cdn,
        "bytes_economizados_mb": round(bytes_economizados / 1024 / 1024, 2),
        "reducao_latencia_ms": 150,
        "cache_hit_rate_pct": cache_hit_rate * 100
    }

def stats_cdn() -> dict:
    return {
        "cdn_url": CDN_URL or "nao_configurado",
        "cloudflare": bool(CLOUDFLARE_ZONE_ID),
        "cache_policies": len(CACHE_HEADERS),
        "plugin": "cdn_optimization v1.0"
    }
