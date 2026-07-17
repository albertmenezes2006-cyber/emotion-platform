#!/usr/bin/env python3
"""Ricoeur Narrative"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/ricoeur_narrative", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_ricoeur_narrative","s":"ativo","d":"Ricoeur Narrative","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_ricoeur_narrative"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
