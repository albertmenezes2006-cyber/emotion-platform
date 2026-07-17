#!/usr/bin/env python3
"""Constructivist Gt"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/constructivist_gt", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_constructivist_gt","s":"ativo","d":"Constructivist Gt","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_constructivist_gt"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
