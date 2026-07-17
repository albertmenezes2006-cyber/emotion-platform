#!/usr/bin/env python3
"""Key Informant"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/key_informant", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_key_informant","s":"ativo","d":"Key Informant","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_key_informant"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
