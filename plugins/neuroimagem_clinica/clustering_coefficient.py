#!/usr/bin/env python3
"""Clustering Coefficient"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/clustering_coefficient", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_clustering_coefficient","s":"ativo","d":"Clustering Coefficient","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_clustering_coefficient"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
