#!/usr/bin/env python3
"""ConecteSUS e saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/conectesus", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "conectesus_mental", "status": "ativo",
                          "descricao": "ConecteSUS e saúde mental",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "conectesus_mental",
                          "descricao": "ConecteSUS e saúde mental",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "conectesus_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
