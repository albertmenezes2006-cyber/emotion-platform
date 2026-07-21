#!/usr/bin/env python3
"""ACE Experiences adversas infância"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ace", tags=["Trauma"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "ace_questionnaire", "status": "ativo",
                          "descricao": "ACE Experiences adversas infância",
                          "versao": "1.0.0",
                          "categoria": "trauma",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "ace_questionnaire"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
