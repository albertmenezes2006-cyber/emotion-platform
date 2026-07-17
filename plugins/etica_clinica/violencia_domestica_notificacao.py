#!/usr/bin/env python3
"""Violencia Domestica Notificacao em etica clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/etica_clinica/violencia_domestica_notificaca", tags=["etica_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"etica_clinica_violencia_domestica_notif","status":"ativo","desc":"Violencia Domestica Notificacao em etica clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "etica_clinica_violencia_domestica_notif"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
