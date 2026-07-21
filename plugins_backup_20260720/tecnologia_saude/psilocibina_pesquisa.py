#!/usr/bin/env python3
"""Psilocibina pesquisa clínica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/psilocibina", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "psilocibina_pesquisa", "status": "ativo",
                          "descricao": "Psilocibina pesquisa clínica",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "psilocibina_pesquisa",
                          "descricao": "Psilocibina pesquisa clínica",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "psilocibina_pesquisa"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
