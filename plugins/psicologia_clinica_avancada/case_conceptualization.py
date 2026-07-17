#!/usr/bin/env python3
"""Case Conceptualization"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/case_conceptualization", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_case_conceptualization","s":"ativo","d":"Case Conceptualization","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_case_conceptualization"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
