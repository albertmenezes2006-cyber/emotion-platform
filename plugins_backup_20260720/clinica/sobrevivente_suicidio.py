#!/usr/bin/env python3
"""Sobreviventes de suicídio"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/sobrevivente-suic", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "sobrevivente_suicidio", "status": "ativo",
                          "descricao": "Sobreviventes de suicídio",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "sobrevivente_suicidio",
                          "descricao": "Sobreviventes de suicídio",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "sobrevivente_suicidio"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
