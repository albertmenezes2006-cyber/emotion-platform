#!/usr/bin/env python3
"""Lesão cerebral traumática"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/tbi", tags=["Populacoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "tbi_lesao_cerebral", "status": "ativo",
                          "descricao": "Lesão cerebral traumática",
                          "categoria": "populacoes",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "tbi_lesao_cerebral",
                          "descricao": "Lesão cerebral traumática",
                          "categoria": "populacoes",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "tbi_lesao_cerebral"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
