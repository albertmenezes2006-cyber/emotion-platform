#!/usr/bin/env python3
"""Templates de email"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/email-templates", tags=["email_templates"])

@router.get("")
async def info():
    return JSONResponse({"nome": "email_templates", "status": "ativo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "email_templates"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
