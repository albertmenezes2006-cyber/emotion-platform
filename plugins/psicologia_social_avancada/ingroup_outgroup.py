#!/usr/bin/env python3
"""Ingroup Outgroup"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/ingroup_outgroup", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__ingroup_outgroup","s":"ativo","d":"Ingroup Outgroup","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__ingroup_outgroup"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
