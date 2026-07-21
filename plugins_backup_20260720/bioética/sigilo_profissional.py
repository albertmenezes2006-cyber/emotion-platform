#!/usr/bin/env python3
"""Sigilo profissional psicologia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/sigilo", tags=["Bioetica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "sigilo_profissional", "status": "ativo",
                          "descricao": "Sigilo profissional psicologia",
                          "categoria": "bioetica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "sigilo_profissional",
                          "descricao": "Sigilo profissional psicologia",
                          "categoria": "bioetica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "sigilo_profissional"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
