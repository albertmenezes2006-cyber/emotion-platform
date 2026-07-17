#!/usr/bin/env python3
"""Psicologia Africana em saude mental grupos especificos"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental_gr/psicologia_africana", tags=["saude_mental_grupos_especificos"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"saude_mental_grupos__psicologia_africana","status":"ativo","desc":"Psicologia Africana em saude mental grupos especificos","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_grupos__psicologia_africana"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
