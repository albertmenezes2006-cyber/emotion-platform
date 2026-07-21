#!/usr/bin/env python3
"""Cache simples em memoria"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
from functools import lru_cache

router = APIRouter(prefix="/api/v1/cache", tags=["Cache"])
_cache = {}
_stats = {"hits": 0, "misses": 0}

def get_cache(key):
    if key in _cache:
        item = _cache[key]
        if (datetime.utcnow()-item["ts"]).seconds < item["ttl"]:
            _stats["hits"] += 1
            return item["valor"]
    _stats["misses"] += 1
    return None

def set_cache(key, valor, ttl=300):
    _cache[key] = {"valor": valor, "ts": datetime.utcnow(), "ttl": ttl}

@router.get("/stats")
async def cache_stats():
    total = _stats["hits"] + _stats["misses"]
    taxa = (_stats["hits"]/total*100) if total > 0 else 0
    return JSONResponse({"hits": _stats["hits"], "misses": _stats["misses"],
                         "taxa_acerto": f"{taxa:.1f}%", "itens_cache": len(_cache)})

@router.delete("/limpar")
async def limpar_cache():
    _cache.clear()
    return JSONResponse({"ok": True, "msg": "Cache limpo"})

class CachePlugin(PluginBase):
    name = "cache_simples"
    def setup(self, app): app.include_router(router)
plugin = CachePlugin()
