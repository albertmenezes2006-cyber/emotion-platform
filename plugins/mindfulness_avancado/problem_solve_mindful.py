#!/usr/bin/env python3
"""Problem Solve Mindful"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/problem_solve_mindful", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_problem_solve_mindful","s":"ativo","d":"Problem Solve Mindful","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_problem_solve_mindful"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
