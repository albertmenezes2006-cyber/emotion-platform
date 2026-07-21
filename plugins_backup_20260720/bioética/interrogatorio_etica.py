#!/usr/bin/env python3
"""Ética em interrogatório"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/interrogatorio", tags=["Bioetica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "interrogatorio_etica", "status": "ativo",
                          "descricao": "Ética em interrogatório",
                          "categoria": "bioetica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "interrogatorio_etica",
                          "descricao": "Ética em interrogatório",
                          "categoria": "bioetica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "interrogatorio_etica"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
