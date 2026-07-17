#!/usr/bin/env python3
"""Copy Number Variant"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/copy_number_variant", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_copy_number_variant","s":"ativo","d":"Copy Number Variant","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_copy_number_variant"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
