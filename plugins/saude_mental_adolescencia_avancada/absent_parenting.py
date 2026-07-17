#!/usr/bin/env python3
"""Absent Parenting"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/absent_parenting", tags=["saude_mental_adolescencia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_adole_absent_parenting","s":"ativo","d":"Absent Parenting","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_adole_absent_parenting"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
