#!/usr/bin/env python3
"""Grupo regulação emocional"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/grupo-reg-emoc", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "grupo_regulacao_emocional", "status": "ativo",
                          "descricao": "Grupo regulação emocional",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "grupo_regulacao_emocional",
                          "descricao": "Grupo regulação emocional",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "grupo_regulacao_emocional"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
