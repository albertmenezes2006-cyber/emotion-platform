#!/usr/bin/env python3
"""Semi Imputabilidade"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/semi_imputabilidade", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_semi_imputabilidade","s":"ativo","d":"Semi Imputabilidade","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_semi_imputabilidade"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
