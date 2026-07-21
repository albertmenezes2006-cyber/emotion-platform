#!/usr/bin/env python3
"""Trabalho em equipe multidisciplinar"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/equipe-multi", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "equipe_multidisciplinar", "status": "ativo",
                          "descricao": "Trabalho em equipe multidisciplinar",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "equipe_multidisciplinar",
                          "descricao": "Trabalho em equipe multidisciplinar",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "equipe_multidisciplinar"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
