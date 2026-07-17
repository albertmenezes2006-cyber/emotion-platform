#!/usr/bin/env python3
"""Compressao GZip para respostas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from starlette.middleware.gzip import GZipMiddleware

router = APIRouter(prefix="/api/v1/performance", tags=["Performance"])

@router.get("/info")
async def performance_info():
    return {
        "gzip": "ativo",
        "min_size": "500 bytes",
        "beneficio": "30-70% menor tamanho de resposta",
        "status": "otimizado"
    }

class GZipPlugin(PluginBase):
    name = "gzip_compression"
    def setup(self, app):
        app.add_middleware(GZipMiddleware, minimum_size=500)
        app.include_router(router)

plugin = GZipPlugin()
