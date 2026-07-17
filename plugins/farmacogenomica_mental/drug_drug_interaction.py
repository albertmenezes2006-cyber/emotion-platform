#!/usr/bin/env python3
"""Drug Drug Interaction"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/drug_drug_interaction", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_drug_drug_interaction","s":"ativo","d":"Drug Drug Interaction","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_drug_drug_interaction"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
