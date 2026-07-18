from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
from pathlib import Path
import json

router = APIRouter(prefix="/api/v1/phq9", tags=["PHQ9"])
ARQ = Path("phq9_resultados.json")

def load():
    if ARQ.exists():
        try: return json.loads(ARQ.read_text())
        except: return []
    return []

def interpretar(score):
    if score <= 4: return "Sem depressao significativa", "verde"
    elif score <= 9: return "Depressao leve", "amarelo"
    elif score <= 14: return "Depressao moderada", "laranja"
    elif score <= 19: return "Depressao moderadamente grave", "vermelho"
    else: return "Depressao grave", "vermelho_escuro"

@router.post("/calcular")
async def calcular(request: Request):
    d = await request.json()
    respostas = d.get("respostas", [])
    if len(respostas) != 9:
        return JSONResponse({"erro": "PHQ-9 requer 9 respostas (0-3)"}, status_code=400)
    score = sum(int(r) for r in respostas)
    nivel, cor = interpretar(score)
    resultado = {
        "score": score,
        "max": 27,
        "nivel": nivel,
        "cor": cor,
        "percentual": round(score/27*100, 1),
        "recomendacao": "Busque suporte profissional" if score >= 10 else "Continue monitorando",
        "alerta": score >= 15,
        "timestamp": datetime.utcnow().isoformat()
    }
    # Salvar
    paciente = d.get("paciente_id", "anonimo")
    todos = load()
    todos.append({**resultado, "paciente_id": paciente, "respostas": respostas})
    ARQ.write_text(json.dumps(todos, ensure_ascii=False, indent=2))
    return JSONResponse(resultado)

@router.get("/historico/{paciente_id}")
async def historico(paciente_id: str):
    todos = load()
    pac = [r for r in todos if r.get("paciente_id") == paciente_id]
    return JSONResponse({"historico": pac, "total": len(pac)})

@router.post("/avaliacao")
async def avaliacao_completa(request: Request):
    d = await request.json()
    return await calcular(request)

class Plugin(PluginBase):
    name = "phq9_calcular"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
