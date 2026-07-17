#!/usr/bin/env python3
"""CPT Cognitive Processing Therapy"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/cpt", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "cpt_cognitive_proc", "status": "ativo",
                          "descricao": "CPT Cognitive Processing Therapy",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "cpt_cognitive_proc",
                          "descricao": "CPT Cognitive Processing Therapy",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "cpt_cognitive_proc"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
