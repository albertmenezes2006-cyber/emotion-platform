#!/usr/bin/env python3
"""Prática baseada em evidências"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/evidencias", tags=["Pesquisa Cientifica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "evidence_based", "status": "ativo",
                          "descricao": "Prática baseada em evidências",
                          "versao": "1.0.0",
                          "categoria": "pesquisa_cientifica",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "evidence_based"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
