#!/usr/bin/env python3
"""Risk Assessment2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/risk_assessment2", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_risk_assessment2","s":"ativo","d":"Risk Assessment2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_risk_assessment2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
