#!/usr/bin/env python3
"""Inpi Ia em bem estar digital"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/bem_estar_digit/inpi_ia", tags=["bem_estar_digital"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "bem_estar_digital_inpi_ia", "status": "ativo",
                          "descricao": "Inpi Ia em bem estar digital", "categoria": "bem_estar_digital",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "bem_estar_digital_inpi_ia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
