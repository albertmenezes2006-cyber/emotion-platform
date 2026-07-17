#!/usr/bin/env python3
"""Mentalizacao Parental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/mentalizacao_parental", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_mentalizacao_parental","s":"ativo","d":"Mentalizacao Parental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_mentalizacao_parental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
