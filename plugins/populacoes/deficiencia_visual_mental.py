#!/usr/bin/env python3
"""Deficiência visual e saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/def-visual", tags=["Populacoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "deficiencia_visual_mental", "status": "ativo",
                          "descricao": "Deficiência visual e saúde mental",
                          "categoria": "populacoes",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "deficiencia_visual_mental",
                          "descricao": "Deficiência visual e saúde mental",
                          "categoria": "populacoes",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "deficiencia_visual_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
