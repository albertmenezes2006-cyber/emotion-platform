#!/usr/bin/env python3
"""Classical Gt"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/classical_gt", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_classical_gt","s":"ativo","d":"Classical Gt","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_classical_gt"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
