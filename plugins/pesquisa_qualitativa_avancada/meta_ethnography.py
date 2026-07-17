#!/usr/bin/env python3
"""Meta Ethnography"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/meta_ethnography", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_meta_ethnography","s":"ativo","d":"Meta Ethnography","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_meta_ethnography"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
