#!/usr/bin/env python3
"""Pós tentativa suicídio"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/pos-tentativa", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "tentativa_suicidio_pos", "status": "ativo",
                          "descricao": "Pós tentativa suicídio",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "tentativa_suicidio_pos",
                          "descricao": "Pós tentativa suicídio",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "tentativa_suicidio_pos"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
