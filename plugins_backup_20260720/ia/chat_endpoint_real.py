from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
from pathlib import Path
import json, os, urllib.request

router = APIRouter(prefix="/api/v1/chat", tags=["Chat"])
HISTORICO = Path("chat_historico.json")
MISTRAL_KEY = os.getenv("MISTRAL_API_KEY", "")

def load_hist():
    if HISTORICO.exists():
        try: return json.loads(HISTORICO.read_text())
        except: return {}
    return {}

def save_hist(d):
    HISTORICO.write_text(json.dumps(d, ensure_ascii=False, indent=2))

def chat_ia(mensagem):
    if not MISTRAL_KEY:
        return "IA nao configurada. Contate o administrador."
    try:
        data = json.dumps({
            "model": "mistral-small-latest",
            "messages": [
                {"role": "system", "content": "Voce e um assistente de saude mental em portugues brasileiro. Responda com empatia, carinho e baseado em evidencias. Nunca substitua um profissional. Em caso de crise, indique o CVV 188."},
                {"role": "user", "content": mensagem}
            ],
            "max_tokens": 500,
            "temperature": 0.7
        }).encode()
        req = urllib.request.Request(
            "https://api.mistral.ai/v1/chat/completions",
            data=data,
            headers={
                "Authorization": f"Bearer {MISTRAL_KEY}",
                "Content-Type": "application/json"
            }
        )
        resp = urllib.request.urlopen(req, timeout=30)
        d = json.loads(resp.read().decode())
        return d["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Desculpe, estou com dificuldades tecnicas no momento. Se precisar de ajuda urgente, ligue 188 (CVV). Erro: {str(e)[:50]}"

@router.post("/enviar")
async def enviar_chat(request: Request):
    d = await request.json()
    msg = d.get("mensagem", d.get("message", ""))
    session = d.get("session_id", "anonimo")
    if not msg:
        return JSONResponse({"erro": "Mensagem vazia"}, status_code=400)
    hist = load_hist()
    if session not in hist:
        hist[session] = []
    hist[session].append({"role": "user", "content": msg, "ts": datetime.utcnow().isoformat()})
    resposta = chat_ia(msg)
    hist[session].append({"role": "assistant", "content": resposta, "ts": datetime.utcnow().isoformat()})
    save_hist(hist)
    return JSONResponse({"resposta": resposta, "session_id": session, "modelo": "mistral", "status": "ok"})

@router.get("/historico/{session_id}")
async def historico(session_id: str):
    hist = load_hist()
    return JSONResponse({"historico": hist.get(session_id, []), "total": len(hist.get(session_id, []))})

@router.delete("/limpar/{session_id}")
async def limpar(session_id: str):
    hist = load_hist()
    if session_id in hist:
        del hist[session_id]
    save_hist(hist)
    return JSONResponse({"ok": True})

class Plugin(PluginBase):
    name = "chat_endpoint_real"
    def setup(self, app):
        app.include_router(router)

plugin = Plugin()
