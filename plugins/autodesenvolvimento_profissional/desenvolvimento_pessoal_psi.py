#!/usr/bin/env python3
"""Desenvolvimento Pessoal Psi em autodesenvolvimento profissional"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/autodesenvolvim/desenvolvimento_pessoal_psi", tags=["autodesenvolvimento_profissional"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"autodesenvolvimento__desenvolvimento_pessoal_p","status":"ativo","desc":"Desenvolvimento Pessoal Psi em autodesenvolvimento profissional","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "autodesenvolvimento__desenvolvimento_pessoal_p"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
