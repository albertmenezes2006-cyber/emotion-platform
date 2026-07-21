#!/usr/bin/env python3
"""Escola promotora de saúde"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/escola-saudavel", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "health_promotion_school", "status": "ativo",
                          "descricao": "Escola promotora de saúde",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "health_promotion_school",
                          "descricao": "Escola promotora de saúde",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "health_promotion_school"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
