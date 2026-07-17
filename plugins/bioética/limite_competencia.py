#!/usr/bin/env python3
"""Limites de competência"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/competencia", tags=["Bioetica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "limite_competencia", "status": "ativo",
                          "descricao": "Limites de competência",
                          "categoria": "bioetica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "limite_competencia",
                          "descricao": "Limites de competência",
                          "categoria": "bioetica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "limite_competencia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
