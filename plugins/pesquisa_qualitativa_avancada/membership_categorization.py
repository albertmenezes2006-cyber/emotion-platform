#!/usr/bin/env python3
"""Membership Categorization"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/membership_categorization", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_membership_categorization","s":"ativo","d":"Membership Categorization","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_membership_categorization"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
