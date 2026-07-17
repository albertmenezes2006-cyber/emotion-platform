#!/usr/bin/env python3
"""WhatsApp Business"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/wa-business", tags=["wa_business"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "wa_business", "status": "ativo",
                          "descricao": "WhatsApp Business",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "wa_business"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
