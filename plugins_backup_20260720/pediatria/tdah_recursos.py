#!/usr/bin/env python3
"""TDAH recursos para crianças"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/tdah-kids", tags=["Pediatria"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "tdah_recursos_kids", "status": "ativo",
                          "descricao": "TDAH recursos para crianças",
                          "versao": "1.0.0",
                          "categoria": "pediatria",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "tdah_recursos_kids"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
