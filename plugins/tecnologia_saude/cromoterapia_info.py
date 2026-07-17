#!/usr/bin/env python3
"""Cromoterapia informações"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/cromoterapia", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "cromoterapia_info", "status": "ativo",
                          "descricao": "Cromoterapia informações",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "cromoterapia_info",
                          "descricao": "Cromoterapia informações",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "cromoterapia_info"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
