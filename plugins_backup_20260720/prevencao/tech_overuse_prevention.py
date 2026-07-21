#!/usr/bin/env python3
"""Prevenção ao uso excessivo de tech"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/prev-tech", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "tech_overuse_prevention", "status": "ativo",
                          "descricao": "Prevenção ao uso excessivo de tech",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "tech_overuse_prevention",
                          "descricao": "Prevenção ao uso excessivo de tech",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "tech_overuse_prevention"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
