#!/usr/bin/env python3
"""Empoderamento Digital em bem estar digital"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/bem_estar_digit/empoderamento_digital", tags=["bem_estar_digital"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "bem_estar_digital_empoderamento_digital", "status": "ativo",
                          "descricao": "Empoderamento Digital em bem estar digital", "categoria": "bem_estar_digital",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "bem_estar_digital_empoderamento_digital"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
