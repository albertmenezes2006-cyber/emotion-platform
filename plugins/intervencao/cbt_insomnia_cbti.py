#!/usr/bin/env python3
"""CBT-I para insônia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/cbti", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "cbt_insomnia_cbti", "status": "ativo",
                          "descricao": "CBT-I para insônia",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "cbt_insomnia_cbti",
                          "descricao": "CBT-I para insônia",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "cbt_insomnia_cbti"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
