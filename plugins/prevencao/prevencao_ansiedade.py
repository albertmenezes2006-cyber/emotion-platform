#!/usr/bin/env python3
"""Prevenção à ansiedade"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/prev-ansiedade", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "prevencao_ansiedade", "status": "ativo",
                          "descricao": "Prevenção à ansiedade",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "prevencao_ansiedade",
                          "descricao": "Prevenção à ansiedade",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "prevencao_ansiedade"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
