#!/usr/bin/env python3
"""Existential Phenomenology"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/existential_phenomenology", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_existential_phenomenology","s":"ativo","d":"Existential Phenomenology","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_existential_phenomenology"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
