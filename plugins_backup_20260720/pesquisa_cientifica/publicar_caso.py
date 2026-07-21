#!/usr/bin/env python3
"""Publicar relato de caso"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/publicar", tags=["Pesquisa Cientifica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "publicar_caso", "status": "ativo",
                          "descricao": "Publicar relato de caso",
                          "versao": "1.0.0",
                          "categoria": "pesquisa_cientifica",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "publicar_caso"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
