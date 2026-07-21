#!/usr/bin/env python3
"""Open Science em psicologia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/open-science", tags=["Pesquisa Cientifica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "open_science", "status": "ativo",
                          "descricao": "Open Science em psicologia",
                          "versao": "1.0.0",
                          "categoria": "pesquisa_cientifica",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "open_science"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
