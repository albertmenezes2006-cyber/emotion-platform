#!/usr/bin/env python3
"""Bond Agreement"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/bond_agreement", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_bond_agreement","s":"ativo","d":"Bond Agreement","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_bond_agreement"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
