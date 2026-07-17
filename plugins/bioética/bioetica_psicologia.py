#!/usr/bin/env python3
"""Bioética em psicologia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/bioetica", tags=["Bioetica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "bioetica_psicologia", "status": "ativo",
                          "descricao": "Bioética em psicologia",
                          "categoria": "bioetica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "bioetica_psicologia",
                          "descricao": "Bioética em psicologia",
                          "categoria": "bioetica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "bioetica_psicologia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
