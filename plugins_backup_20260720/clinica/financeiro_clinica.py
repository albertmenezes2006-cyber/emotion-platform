#!/usr/bin/env python3
"""Gestão financeira da clínica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/fin-clinica", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "financeiro_clinica", "status": "ativo",
                          "descricao": "Gestão financeira da clínica",
                          "versao": "1.0.0",
                          "categoria": "clinica",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "financeiro_clinica"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
