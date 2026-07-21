#!/usr/bin/env python3
"""Encaminhamento para psiquiatra"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/encam-psiq", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "encaminhamento_psiquiatra", "status": "ativo",
                          "descricao": "Encaminhamento para psiquiatra",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "encaminhamento_psiquiatra",
                          "descricao": "Encaminhamento para psiquiatra",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "encaminhamento_psiquiatra"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
