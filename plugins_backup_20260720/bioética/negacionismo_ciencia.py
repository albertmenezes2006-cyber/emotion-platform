#!/usr/bin/env python3
"""Negacionismo científico"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/negacionismo", tags=["Bioetica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "negacionismo_ciencia", "status": "ativo",
                          "descricao": "Negacionismo científico",
                          "categoria": "bioetica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "negacionismo_ciencia",
                          "descricao": "Negacionismo científico",
                          "categoria": "bioetica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "negacionismo_ciencia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
