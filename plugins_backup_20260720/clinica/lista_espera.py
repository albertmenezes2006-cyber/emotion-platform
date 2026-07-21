#!/usr/bin/env python3
"""Lista de espera da clínica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/lista-espera", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "lista_espera_clinica", "status": "ativo",
                          "descricao": "Lista de espera da clínica",
                          "versao": "1.0.0",
                          "categoria": "clinica",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "lista_espera_clinica"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
