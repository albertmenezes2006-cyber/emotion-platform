#!/usr/bin/env python3
"""Registro clínico padronizado"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/registro-padrao", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "registro_clinico_padrao", "status": "ativo",
                          "descricao": "Registro clínico padronizado",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "registro_clinico_padrao",
                          "descricao": "Registro clínico padronizado",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "registro_clinico_padrao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
