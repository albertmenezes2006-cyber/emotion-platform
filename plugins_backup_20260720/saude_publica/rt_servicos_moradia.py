#!/usr/bin/env python3
"""RT e moradia assistida"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/rt-moradia", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "rt_servicos_moradia", "status": "ativo",
                          "descricao": "RT e moradia assistida",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "rt_servicos_moradia",
                          "descricao": "RT e moradia assistida",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "rt_servicos_moradia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
