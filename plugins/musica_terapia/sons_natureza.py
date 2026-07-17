#!/usr/bin/env python3
"""Sons da natureza terapêuticos"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/sons", tags=["Musica Terapia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "sons_natureza", "status": "ativo",
                          "descricao": "Sons da natureza terapêuticos",
                          "versao": "1.0.0",
                          "categoria": "musica_terapia",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "sons_natureza"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
