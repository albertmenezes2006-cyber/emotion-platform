#!/usr/bin/env python3
"""Parenting Assessment"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/parenting_assessment", tags=["saude_mental_juridico_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_jurid_parenting_assessment","s":"ativo","d":"Parenting Assessment","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_jurid_parenting_assessment"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
