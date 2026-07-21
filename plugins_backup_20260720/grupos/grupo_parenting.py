#!/usr/bin/env python3
"""Grupo parentalidade"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/grupo-parenting", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "grupo_parenting", "status": "ativo",
                          "descricao": "Grupo parentalidade",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "grupo_parenting",
                          "descricao": "Grupo parentalidade",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "grupo_parenting"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
