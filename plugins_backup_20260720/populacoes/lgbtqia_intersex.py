#!/usr/bin/env python3
"""Intersex e saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/intersex", tags=["Populacoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "lgbtqia_intersex", "status": "ativo",
                          "descricao": "Intersex e saúde mental",
                          "categoria": "populacoes",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "lgbtqia_intersex",
                          "descricao": "Intersex e saúde mental",
                          "categoria": "populacoes",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "lgbtqia_intersex"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
