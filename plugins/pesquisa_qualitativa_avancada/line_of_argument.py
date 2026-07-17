#!/usr/bin/env python3
"""Line Of Argument"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/line_of_argument", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_line_of_argument","s":"ativo","d":"Line Of Argument","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_line_of_argument"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
