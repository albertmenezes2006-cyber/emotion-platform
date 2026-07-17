#!/usr/bin/env python3
"""Antivacinas e saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/antivacina-mental", tags=["Bioetica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "movimento_antivacinas", "status": "ativo",
                          "descricao": "Antivacinas e saúde mental",
                          "categoria": "bioetica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "movimento_antivacinas",
                          "descricao": "Antivacinas e saúde mental",
                          "categoria": "bioetica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "movimento_antivacinas"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
