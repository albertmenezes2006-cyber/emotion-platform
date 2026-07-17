#!/usr/bin/env python3
"""Sistema de logs estruturados"""
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
from pathlib import Path
import json

router = APIRouter(prefix="/api/v1/logs", tags=["Logs"])
ARQUIVO = Path("logs_sistema.json")

def log(nivel: str, msg: str, extra: dict = None):
    logs = []
    if ARQUIVO.exists():
        try: logs = json.loads(ARQUIVO.read_text())
        except: logs = []
    logs.append({"nivel": nivel, "msg": msg, "extra": extra or {},
                 "ts": datetime.utcnow().isoformat()})
    if len(logs) > 1000: logs = logs[-1000:]
    ARQUIVO.write_text(json.dumps(logs, ensure_ascii=False))

@router.get("/recentes")
async def logs_recentes(limite: int = 20):
    if not ARQUIVO.exists():
        return JSONResponse({"logs": [], "total": 0})
    try:
        logs = json.loads(ARQUIVO.read_text())
        return JSONResponse({"logs": logs[-limite:], "total": len(logs)})
    except:
        return JSONResponse({"logs": [], "total": 0})

@router.post("/registrar")
async def registrar_log(request: Request):
    d = await request.json()
    log(d.get("nivel","info"), d.get("msg",""), d.get("extra"))
    return JSONResponse({"ok": True})

class LogsPlugin(PluginBase):
    name = "logs_sistema"
    def setup(self, app): app.include_router(router)
plugin = LogsPlugin()
