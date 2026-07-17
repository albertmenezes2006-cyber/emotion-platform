#!/usr/bin/env python3
"""Sono saudável na infância"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/sono-infantil", tags=["Pediatria"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "sono_infantil", "status": "ativo",
                          "descricao": "Sono saudável na infância",
                          "versao": "1.0.0",
                          "categoria": "pediatria",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "sono_infantil"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
