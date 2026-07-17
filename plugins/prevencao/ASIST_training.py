#!/usr/bin/env python3
"""ASIST intervenção aplicada"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/asist", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "ASIST_training", "status": "ativo",
                          "descricao": "ASIST intervenção aplicada",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "ASIST_training",
                          "descricao": "ASIST intervenção aplicada",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "ASIST_training"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
