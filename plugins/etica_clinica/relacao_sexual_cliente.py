#!/usr/bin/env python3
"""Relacao Sexual Cliente em etica clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/etica_clinica/relacao_sexual_cliente", tags=["etica_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"etica_clinica_relacao_sexual_cliente","status":"ativo","desc":"Relacao Sexual Cliente em etica clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "etica_clinica_relacao_sexual_cliente"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
