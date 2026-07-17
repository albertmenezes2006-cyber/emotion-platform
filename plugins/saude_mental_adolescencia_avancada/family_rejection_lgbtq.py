#!/usr/bin/env python3
"""Family Rejection Lgbtq"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/family_rejection_lgbtq", tags=["saude_mental_adolescencia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_adole_family_rejection_lgbtq","s":"ativo","d":"Family Rejection Lgbtq","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_adole_family_rejection_lgbtq"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
