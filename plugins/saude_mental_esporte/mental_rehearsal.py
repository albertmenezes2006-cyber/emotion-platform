#!/usr/bin/env python3
"""Mental Rehearsal"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/mental_rehearsal", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_mental_rehearsal","s":"ativo","d":"Mental Rehearsal","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_mental_rehearsal"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
