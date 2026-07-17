#!/usr/bin/env python3
"""Supervisão ética"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/supervisao-etica", tags=["Bioetica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "supervisao_etica", "status": "ativo",
                          "descricao": "Supervisão ética",
                          "categoria": "bioetica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "supervisao_etica",
                          "descricao": "Supervisão ética",
                          "categoria": "bioetica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "supervisao_etica"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
