#!/usr/bin/env python3
"""Executive Function Adhd"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/executive_function_adhd", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_executive_function_adhd","s":"ativo","d":"Executive Function Adhd","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_executive_function_adhd"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
