#!/usr/bin/env python3
"""Evolução SOAP digital"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/soap-digital", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "evolucao_soap_digital", "status": "ativo",
                          "descricao": "Evolução SOAP digital",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "evolucao_soap_digital",
                          "descricao": "Evolução SOAP digital",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "evolucao_soap_digital"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
