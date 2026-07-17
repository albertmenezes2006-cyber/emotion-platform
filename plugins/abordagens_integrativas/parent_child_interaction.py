#!/usr/bin/env python3
"""Parent Child Interaction"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/parent_child_interaction", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_parent_child_interaction","s":"ativo","d":"Parent Child Interaction","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_parent_child_interaction"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
