#!/usr/bin/env python3
"""Rupturas e reparação da aliança"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/rupturas", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "rupturas_alianca", "status": "ativo",
                          "descricao": "Rupturas e reparação da aliança",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "rupturas_alianca",
                          "descricao": "Rupturas e reparação da aliança",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "rupturas_alianca"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
