#!/usr/bin/env python3
"""Psicoterapia positiva Seligman"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/pp-protocol", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "positive_psychotherapy", "status": "ativo",
                          "descricao": "Psicoterapia positiva Seligman",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "positive_psychotherapy",
                          "descricao": "Psicoterapia positiva Seligman",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "positive_psychotherapy"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
