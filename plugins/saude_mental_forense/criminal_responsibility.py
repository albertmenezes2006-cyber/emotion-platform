#!/usr/bin/env python3
"""Criminal Responsibility"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/criminal_responsibility", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_criminal_responsibility","s":"ativo","d":"Criminal Responsibility","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_criminal_responsibility"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
