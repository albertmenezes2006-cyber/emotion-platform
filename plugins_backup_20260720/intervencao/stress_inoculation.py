#!/usr/bin/env python3
"""Inoculação de estresse Meichenbaum"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/inoculacao", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "stress_inoculation", "status": "ativo",
                          "descricao": "Inoculação de estresse Meichenbaum",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "stress_inoculation",
                          "descricao": "Inoculação de estresse Meichenbaum",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "stress_inoculation"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
