#!/usr/bin/env python3
"""Matrix Intensive Outpatient em intervencoes especificas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/intervencoes_es/matrix_intensive_outpatient", tags=["intervencoes_especificas"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"intervencoes_especif_matrix_intensive_outpatie","status":"ativo","desc":"Matrix Intensive Outpatient em intervencoes especificas","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "intervencoes_especif_matrix_intensive_outpatie"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
