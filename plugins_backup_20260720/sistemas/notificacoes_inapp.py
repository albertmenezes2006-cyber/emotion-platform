#!/usr/bin/env python3
"""Sistema de notificacoes in-app"""
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, HTMLResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import json
from pathlib import Path

router = APIRouter(prefix="/api/v1/notificacoes", tags=["Notificações"])
ARQUIVO = Path("notificacoes.json")

def carregar():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text())
    return []

@router.post("/criar")
async def criar_notificacao(request: Request):
    d = await request.json()
    notifs = carregar()
    notifs.append({"id": len(notifs)+1, "titulo": d.get("titulo",""),
                   "mensagem": d.get("mensagem",""), "tipo": d.get("tipo","info"),
                   "lida": False, "timestamp": datetime.utcnow().isoformat()})
    ARQUIVO.write_text(json.dumps(notifs, ensure_ascii=False, indent=2))
    return JSONResponse({"ok": True, "id": len(notifs)})

@router.get("/listar")
async def listar_notificacoes(user_id: str = "anonimo"):
    notifs = carregar()
    nao_lidas = [n for n in notifs if not n["lida"]]
    return JSONResponse({"total": len(notifs), "nao_lidas": len(nao_lidas),
                         "notificacoes": notifs[-10:]})

@router.post("/marcar-lida/{notif_id}")
async def marcar_lida(notif_id: int):
    notifs = carregar()
    for n in notifs:
        if n["id"] == notif_id:
            n["lida"] = True
    ARQUIVO.write_text(json.dumps(notifs, ensure_ascii=False, indent=2))
    return JSONResponse({"ok": True})

@router.get("/badge", response_class=HTMLResponse)
async def badge_notificacoes():
    notifs = carregar()
    nao_lidas = len([n for n in notifs if not n["lida"]])
    return HTMLResponse(f"""
<div id="notif-badge" style="position:relative;display:inline-block">
  <button onclick="toggleNotifs()" style="background:none;border:none;cursor:pointer;
    font-size:24px;position:relative">🔔
    <span id="count" style="{'display:none' if nao_lidas==0 else ''};position:absolute;
      top:-4px;right:-4px;background:#e53e3e;color:white;border-radius:50%;
      width:18px;height:18px;font-size:11px;display:flex;align-items:center;
      justify-content:center;font-weight:700">{nao_lidas}</span>
  </button>
</div>""")

class NotifPlugin(PluginBase):
    name = "notificacoes_inapp"
    def setup(self, app): app.include_router(router)
plugin = NotifPlugin()
