#!/usr/bin/env python3
"""Magnésio e ansiedade"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/magnesio", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "magnesio_ansiedade", "status": "ativo",
                          "descricao": "Magnésio e ansiedade",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "magnesio_ansiedade",
                          "descricao": "Magnésio e ansiedade",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "magnesio_ansiedade"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
