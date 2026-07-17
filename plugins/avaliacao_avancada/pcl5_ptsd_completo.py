#!/usr/bin/env python3
"""PCL-5 PTSD checklist"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/pcl5", tags=["Avaliacao Avancada"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "pcl5_ptsd_completo", "status": "ativo",
                          "descricao": "PCL-5 PTSD checklist",
                          "categoria": "avaliacao_avancada",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "pcl5_ptsd_completo",
                          "descricao": "PCL-5 PTSD checklist",
                          "categoria": "avaliacao_avancada",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "pcl5_ptsd_completo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
