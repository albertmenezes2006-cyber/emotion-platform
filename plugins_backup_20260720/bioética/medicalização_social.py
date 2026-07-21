#!/usr/bin/env python3
"""Medicalização da vida social"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/medicalizacao", tags=["Bioetica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "medicalização_social", "status": "ativo",
                          "descricao": "Medicalização da vida social",
                          "categoria": "bioetica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "medicalização_social",
                          "descricao": "Medicalização da vida social",
                          "categoria": "bioetica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "medicalização_social"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
