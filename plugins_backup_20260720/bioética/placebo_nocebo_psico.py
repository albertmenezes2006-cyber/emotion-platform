#!/usr/bin/env python3
"""Placebo e nocebo em psicologia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/placebo", tags=["Bioetica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "placebo_nocebo_psico", "status": "ativo",
                          "descricao": "Placebo e nocebo em psicologia",
                          "categoria": "bioetica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "placebo_nocebo_psico",
                          "descricao": "Placebo e nocebo em psicologia",
                          "categoria": "bioetica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "placebo_nocebo_psico"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
