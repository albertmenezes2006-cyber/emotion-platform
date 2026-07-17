#!/usr/bin/env python3
"""Feature flags para controle de funcionalidades"""
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from pathlib import Path
import json

router = APIRouter(prefix="/api/v1/features", tags=["Feature Flags"])
ARQUIVO = Path("feature_flags.json")

FLAGS_DEFAULT = {
    "pix_ativo": True, "blog_ativo": True, "nps_ativo": True,
    "exit_intent": True, "social_proof": True, "dark_mode": True,
    "widget_embed": True, "referral_ativo": True, "cupons_ativos": True,
    "chat_ia": True, "gamificacao": True, "push_notifications": False,
}

def carregar():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text())
    ARQUIVO.write_text(json.dumps(FLAGS_DEFAULT, indent=2))
    return FLAGS_DEFAULT

@router.get("")
async def listar_flags():
    return JSONResponse(carregar())

@router.get("/{flag}")
async def verificar_flag(flag: str):
    flags = carregar()
    return JSONResponse({"flag": flag, "ativo": flags.get(flag, False)})

@router.put("/{flag}")
async def atualizar_flag(flag: str, request: Request):
    d = await request.json()
    flags = carregar()
    flags[flag] = d.get("ativo", False)
    ARQUIVO.write_text(json.dumps(flags, indent=2))
    return JSONResponse({"ok": True, "flag": flag, "ativo": flags[flag]})

class FeatureFlagsPlugin(PluginBase):
    name = "feature_flags"
    def setup(self, app): app.include_router(router)
plugin = FeatureFlagsPlugin()
