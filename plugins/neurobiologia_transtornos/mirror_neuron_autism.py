#!/usr/bin/env python3
"""Mirror Neuron Autism"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/mirror_neuron_autism", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_mirror_neuron_autism","s":"ativo","d":"Mirror Neuron Autism","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_mirror_neuron_autism"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
