from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
from pathlib import Path
import json

router = APIRouter(prefix="/api/v1/diario", tags=["Diario"])
ARQ = Path("diario_real.json")

def load(): 
    if ARQ.exists():
        try: return json.loads(ARQ.read_text())
        except: return []
    return []

def save(d): ARQ.write_text(json.dumps(d, ensure_ascii=False, indent=2))

@router.post("/salvar")
async def salvar(request: Request):
    d = await request.json()
    entradas = load()
    entrada = {
        "id": len(entradas)+1,
        "user_id": d.get("user_id", "anonimo"),
        "conteudo": d.get("conteudo", ""),
        "humor": d.get("humor", 5),
        "tags": d.get("tags", []),
        "data": datetime.utcnow().strftime("%d/%m/%Y"),
        "timestamp": datetime.utcnow().isoformat()
    }
    entradas.append(entrada)
    save(entradas)
    return JSONResponse({"ok": True, "id": entrada["id"], "xp_ganho": 20})

@router.get("/listar/{user_id}")
async def listar(user_id: str):
    entradas = load()
    user_entries = [e for e in entradas if e.get("user_id") == user_id]
    return JSONResponse({"entradas": user_entries, "total": len(user_entries)})

@router.get("/stats/{user_id}")
async def stats(user_id: str):
    entradas = load()
    ue = [e for e in entradas if e.get("user_id") == user_id]
    media = sum(e.get("humor",5) for e in ue)/max(1,len(ue))
    return JSONResponse({"total_entradas": len(ue), "humor_medio": round(media,1), "streak": len(ue)})

class Plugin(PluginBase):
    name = "diario_endpoint_real"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
