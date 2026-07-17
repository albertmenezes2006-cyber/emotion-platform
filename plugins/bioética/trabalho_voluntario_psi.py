#!/usr/bin/env python3
"""Trabalho voluntário em psicologia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/voluntario", tags=["Bioetica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "trabalho_voluntario_psi", "status": "ativo",
                          "descricao": "Trabalho voluntário em psicologia",
                          "categoria": "bioetica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "trabalho_voluntario_psi",
                          "descricao": "Trabalho voluntário em psicologia",
                          "categoria": "bioetica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "trabalho_voluntario_psi"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
