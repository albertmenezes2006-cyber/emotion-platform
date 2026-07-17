#!/usr/bin/env python3
"""Maudsley Anorexia em intervencoes especificas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/intervencoes_es/maudsley_anorexia", tags=["intervencoes_especificas"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"intervencoes_especif_maudsley_anorexia","status":"ativo","desc":"Maudsley Anorexia em intervencoes especificas","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "intervencoes_especif_maudsley_anorexia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
