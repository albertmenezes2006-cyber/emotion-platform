#!/usr/bin/env python3
"""Cognitive Remediation Therapy"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/crt", tags=["Neuropsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "cognitive_remediation", "status": "ativo",
                          "descricao": "Cognitive Remediation Therapy",
                          "categoria": "neuropsicologia",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "cognitive_remediation",
                          "descricao": "Cognitive Remediation Therapy",
                          "categoria": "neuropsicologia",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "cognitive_remediation"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
