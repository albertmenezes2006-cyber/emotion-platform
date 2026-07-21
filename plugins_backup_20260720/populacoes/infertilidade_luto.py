#!/usr/bin/env python3
"""Infertilidade e luto gestacional"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/infertilidade", tags=["Populacoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "infertilidade_luto", "status": "ativo",
                          "descricao": "Infertilidade e luto gestacional",
                          "categoria": "populacoes",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "infertilidade_luto",
                          "descricao": "Infertilidade e luto gestacional",
                          "categoria": "populacoes",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "infertilidade_luto"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
