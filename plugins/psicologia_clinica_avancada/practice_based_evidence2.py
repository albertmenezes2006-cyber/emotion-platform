#!/usr/bin/env python3
"""Practice Based Evidence2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/practice_based_evidence2", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_practice_based_evidence2","s":"ativo","d":"Practice Based Evidence2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_practice_based_evidence2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
