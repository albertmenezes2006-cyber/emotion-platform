#!/usr/bin/env python3
"""EAP digital para empresas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/eap", tags=["Corporativo"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "eap_digital", "status": "ativo",
                          "descricao": "EAP digital para empresas",
                          "versao": "1.0.0",
                          "categoria": "corporativo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "eap_digital"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
