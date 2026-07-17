#!/usr/bin/env python3
"""Autoajuda responsável"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/autoajuda-resp", tags=["Bioetica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "autoajuda_responsavel", "status": "ativo",
                          "descricao": "Autoajuda responsável",
                          "categoria": "bioetica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "autoajuda_responsavel",
                          "descricao": "Autoajuda responsável",
                          "categoria": "bioetica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "autoajuda_responsavel"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
