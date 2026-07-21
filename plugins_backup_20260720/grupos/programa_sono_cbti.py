#!/usr/bin/env python3
"""Programa CBT-I para insônia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/cbti-program", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "programa_sono_cbti", "status": "ativo",
                          "descricao": "Programa CBT-I para insônia",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "programa_sono_cbti",
                          "descricao": "Programa CBT-I para insônia",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "programa_sono_cbti"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
