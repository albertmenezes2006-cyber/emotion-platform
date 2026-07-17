#!/usr/bin/env python3
"""Memória episódica teste"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/memoria-epis", tags=["Neuropsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "episodic_memory_test", "status": "ativo",
                          "descricao": "Memória episódica teste",
                          "categoria": "neuropsicologia",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "episodic_memory_test",
                          "descricao": "Memória episódica teste",
                          "categoria": "neuropsicologia",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "episodic_memory_test"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
