#!/usr/bin/env python3
"""Medicação e psicoterapia combinadas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/med-psicot", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "medicacao_psicoterapia", "status": "ativo",
                          "descricao": "Medicação e psicoterapia combinadas",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "medicacao_psicoterapia",
                          "descricao": "Medicação e psicoterapia combinadas",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "medicacao_psicoterapia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
