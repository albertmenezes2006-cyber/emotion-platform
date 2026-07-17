#!/usr/bin/env python3
"""Evidence Based Practice2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/evidence_based_practice2", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_evidence_based_practice2","s":"ativo","d":"Evidence Based Practice2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_evidence_based_practice2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
