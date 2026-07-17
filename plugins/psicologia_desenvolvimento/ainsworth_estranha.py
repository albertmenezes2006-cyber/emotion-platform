#!/usr/bin/env python3
"""Ainsworth Estranha"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/ainsworth_estranha", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_ainsworth_estranha","s":"ativo","d":"Ainsworth Estranha","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_ainsworth_estranha"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
