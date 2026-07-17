#!/usr/bin/env python3
"""Clinical Decision Making"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/clinical_decision_making", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_clinical_decision_making","s":"ativo","d":"Clinical Decision Making","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_clinical_decision_making"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
