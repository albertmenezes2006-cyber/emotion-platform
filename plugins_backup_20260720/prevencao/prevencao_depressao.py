#!/usr/bin/env python3
"""Prevenção à depressão"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/prev-depressao", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "prevencao_depressao", "status": "ativo",
                          "descricao": "Prevenção à depressão",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "prevencao_depressao",
                          "descricao": "Prevenção à depressão",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "prevencao_depressao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
