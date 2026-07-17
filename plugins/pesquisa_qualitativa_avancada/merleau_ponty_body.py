#!/usr/bin/env python3
"""Merleau Ponty Body"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/merleau_ponty_body", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_merleau_ponty_body","s":"ativo","d":"Merleau Ponty Body","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_merleau_ponty_body"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
