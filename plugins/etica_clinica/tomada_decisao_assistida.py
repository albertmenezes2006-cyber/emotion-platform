#!/usr/bin/env python3
"""Tomada Decisao Assistida em etica clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/etica_clinica/tomada_decisao_assistida", tags=["etica_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"etica_clinica_tomada_decisao_assistida","status":"ativo","desc":"Tomada Decisao Assistida em etica clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "etica_clinica_tomada_decisao_assistida"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
