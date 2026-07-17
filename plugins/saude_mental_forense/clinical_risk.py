#!/usr/bin/env python3
"""Clinical Risk"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/clinical_risk", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_clinical_risk","s":"ativo","d":"Clinical Risk","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_clinical_risk"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
