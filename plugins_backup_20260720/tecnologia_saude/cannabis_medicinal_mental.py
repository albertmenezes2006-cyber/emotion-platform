#!/usr/bin/env python3
"""Cannabis medicinal e saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/cannabis-mental", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "cannabis_medicinal_mental", "status": "ativo",
                          "descricao": "Cannabis medicinal e saúde mental",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "cannabis_medicinal_mental",
                          "descricao": "Cannabis medicinal e saúde mental",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "cannabis_medicinal_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
