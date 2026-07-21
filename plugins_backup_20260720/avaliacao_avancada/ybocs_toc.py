#!/usr/bin/env python3
"""Y-BOCS Obsessões Compulsões"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ybocs", tags=["Avaliacao Avancada"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "ybocs_toc", "status": "ativo",
                          "descricao": "Y-BOCS Obsessões Compulsões",
                          "categoria": "avaliacao_avancada",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "ybocs_toc",
                          "descricao": "Y-BOCS Obsessões Compulsões",
                          "categoria": "avaliacao_avancada",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "ybocs_toc"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
