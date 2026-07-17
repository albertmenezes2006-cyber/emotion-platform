#!/usr/bin/env python3
"""TEA suporte e recursos"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/tea", tags=["Pediatria"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "tea_suporte", "status": "ativo",
                          "descricao": "TEA suporte e recursos",
                          "versao": "1.0.0",
                          "categoria": "pediatria",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "tea_suporte"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
