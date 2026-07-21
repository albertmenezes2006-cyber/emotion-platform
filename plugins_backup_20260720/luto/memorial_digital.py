#!/usr/bin/env python3
"""Memorial digital para homenagens"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/memorial", tags=["Luto"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "memorial_digital", "status": "ativo",
                          "descricao": "Memorial digital para homenagens",
                          "versao": "1.0.0",
                          "categoria": "luto",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "memorial_digital"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
