#!/usr/bin/env python3
"""PHQ-A versão adolescente"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/phq-a", tags=["Pediatria"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "phq_a_teen", "status": "ativo",
                          "descricao": "PHQ-A versão adolescente",
                          "versao": "1.0.0",
                          "categoria": "pediatria",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "phq_a_teen"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
