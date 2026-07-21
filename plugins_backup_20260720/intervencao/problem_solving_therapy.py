#!/usr/bin/env python3
"""Problem Solving Therapy PST"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/pstp", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "problem_solving_therapy", "status": "ativo",
                          "descricao": "Problem Solving Therapy PST",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "problem_solving_therapy",
                          "descricao": "Problem Solving Therapy PST",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "problem_solving_therapy"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
