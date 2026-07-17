#!/usr/bin/env python3
"""Hermeneutic Phenomenology"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/hermeneutic_phenomenology", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_hermeneutic_phenomenology","s":"ativo","d":"Hermeneutic Phenomenology","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_hermeneutic_phenomenology"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
