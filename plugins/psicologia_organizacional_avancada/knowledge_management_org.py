#!/usr/bin/env python3
"""Knowledge Management Org"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/knowledge_management_org", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_knowledge_management_org","s":"ativo","d":"Knowledge Management Org","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_knowledge_management_org"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
