#!/usr/bin/env python3
"""Saúde mental LGBTQIA+"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/lgbtqia-saude", tags=["Diversidade"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "lgbtqia_saude_mental", "status": "ativo",
                          "descricao": "Saúde mental LGBTQIA+",
                          "versao": "1.0.0",
                          "categoria": "diversidade",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "lgbtqia_saude_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
