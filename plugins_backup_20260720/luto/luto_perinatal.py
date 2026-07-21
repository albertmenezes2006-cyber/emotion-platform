#!/usr/bin/env python3
"""Suporte ao luto perinatal"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/luto-perinatal", tags=["Luto"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "luto_perinatal", "status": "ativo",
                          "descricao": "Suporte ao luto perinatal",
                          "versao": "1.0.0",
                          "categoria": "luto",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "luto_perinatal"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
