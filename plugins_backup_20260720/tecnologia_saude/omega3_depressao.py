#!/usr/bin/env python3
"""Ômega-3 e depressão evidências"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/omega3", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "omega3_depressao", "status": "ativo",
                          "descricao": "Ômega-3 e depressão evidências",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "omega3_depressao",
                          "descricao": "Ômega-3 e depressão evidências",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "omega3_depressao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
