#!/usr/bin/env python3
"""Neurobiologia Depressao"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/neurobiologia_depressao", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_neurobiologia_depressao","s":"ativo","d":"Neurobiologia Depressao","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_neurobiologia_depressao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
