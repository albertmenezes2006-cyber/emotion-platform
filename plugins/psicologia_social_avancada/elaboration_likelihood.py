#!/usr/bin/env python3
"""Elaboration Likelihood"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/elaboration_likelihood", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__elaboration_likelihood","s":"ativo","d":"Elaboration Likelihood","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__elaboration_likelihood"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
