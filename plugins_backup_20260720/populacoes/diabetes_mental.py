#!/usr/bin/env python3
"""Diabetes e saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/diabetes-mental", tags=["Populacoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "diabetes_mental", "status": "ativo",
                          "descricao": "Diabetes e saúde mental",
                          "categoria": "populacoes",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "diabetes_mental",
                          "descricao": "Diabetes e saúde mental",
                          "categoria": "populacoes",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "diabetes_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
