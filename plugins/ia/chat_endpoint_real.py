from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
from pathlib import Path
import json, os

router = APIRouter(prefix="/api/v1/chat", tags=["Chat"])
HISTORICO = Path("chat_historico.json")

def load_hist():
    if HISTORICO.exists():
        try: return json.loads(HISTORICO.read_text())
        except: return {}
    return {}

def save_hist(d): HISTORICO.write_text(json.dumps(d, ensure_ascii=False, indent=2))

@router.post("/enviar")
async def enviar_chat(request: Request):
    d = await request.json()
    msg = d.get("mensagem", d.get("message", ""))
    session = d.get("session_id", "anonimo")
    modelo = d.get("modelo", "mistral")
    if not msg:
        return JSONResponse({"erro": "Mensagem vazia"}, status_code=400)
    hist = load_hist()
    if session not in hist: hist[session] = []
    hist[session].append({"role": "user", "content": msg, "ts": datetime.utcnow().isoformat()})
    resposta = f"Entendo que voce disse: '{msg[:50]}'. Estou aqui para ajudar com sua saude mental. Pode me contar mais sobre como esta se sentindo?"
    hist[session].append({"role": "assistant", "content": resposta, "ts": datetime.utcnow().isoformat()})
    save_hist(hist)
    return JSONResponse({"resposta": resposta, "session_id": session, "modelo": modelo, "status": "ok"})

@router.get("/historico/{session_id}")
async def historico(session_id: str):
    hist = load_hist()
    return JSONResponse({"historico": hist.get(session_id, []), "total": len(hist.get(session_id, []))})

@router.delete("/limpar/{session_id}")
async def limpar(session_id: str):
    hist = load_hist()
    if session_id in hist: del hist[session_id]
    save_hist(hist)
    return JSONResponse({"ok": True})

class Plugin(PluginBase):
    name = "chat_endpoint_real"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
