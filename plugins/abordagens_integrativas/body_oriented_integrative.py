#!/usr/bin/env python3
"""Body Oriented Integrative"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/body_oriented_integrative", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_body_oriented_integrative","s":"ativo","d":"Body Oriented Integrative","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_body_oriented_integrative"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
