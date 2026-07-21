#!/usr/bin/env python3
"""EFT tapping guiado"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/eft", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "eft_tapping_guide", "status": "ativo",
                          "descricao": "EFT tapping guiado",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "eft_tapping_guide",
                          "descricao": "EFT tapping guiado",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "eft_tapping_guide"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
