#!/usr/bin/env python3
"""ANS coberturas em saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ans-mental", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "ans_coberturas_mental", "status": "ativo",
                          "descricao": "ANS coberturas em saúde mental",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "ans_coberturas_mental",
                          "descricao": "ANS coberturas em saúde mental",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "ans_coberturas_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
