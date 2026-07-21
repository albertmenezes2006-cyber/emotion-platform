#!/usr/bin/env python3
"""Dor crônica e saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/dor-cronica-mental", tags=["Populacoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "dor_cronica_mental", "status": "ativo",
                          "descricao": "Dor crônica e saúde mental",
                          "categoria": "populacoes",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "dor_cronica_mental",
                          "descricao": "Dor crônica e saúde mental",
                          "categoria": "populacoes",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "dor_cronica_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
