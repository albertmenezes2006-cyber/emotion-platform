#!/usr/bin/env python3
"""Eco-ansiedade e crise climática"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/clima-mental", tags=["Populacoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "crise_climatica_mental", "status": "ativo",
                          "descricao": "Eco-ansiedade e crise climática",
                          "categoria": "populacoes",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "crise_climatica_mental",
                          "descricao": "Eco-ansiedade e crise climática",
                          "categoria": "populacoes",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "crise_climatica_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
