#!/usr/bin/env python3
"""Dupla relação na psicologia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/dupla-relacao", tags=["Bioetica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "dupla_relacao", "status": "ativo",
                          "descricao": "Dupla relação na psicologia",
                          "categoria": "bioetica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "dupla_relacao",
                          "descricao": "Dupla relação na psicologia",
                          "categoria": "bioetica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "dupla_relacao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
