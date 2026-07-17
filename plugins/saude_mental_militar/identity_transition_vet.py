#!/usr/bin/env python3
"""Identity Transition Vet"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/identity_transition_vet", tags=["saude_mental_militar"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_milit_identity_transition_vet","s":"ativo","d":"Identity Transition Vet","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_milit_identity_transition_vet"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
