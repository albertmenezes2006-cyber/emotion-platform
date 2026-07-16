"""Plugin: GAD-7 Clinico Real"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException, Body
from datetime import datetime
from plugins.db_manager import SimpleDB
import uuid, json, logging
from typing import List

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/gad7-clinico", tags=["avaliacao_clinica"])

PERGUNTAS = [
    "Sentir-se nervoso, ansioso ou no limite",
    "Nao ser capaz de parar as preocupacoes",
    "Preocupar-se muito com diferentes coisas",
    "Dificuldade para relaxar",
    "Estar tao agitado que e dificil ficar parado",
    "Ficar facilmente contrariado ou irritavel",
    "Sentir medo como se algo terrivel fosse acontecer"
]

CLASSIF = [
    (0, 4, "Minimo", "Sem ansiedade significativa"),
    (5, 9, "Leve", "Monitorar e reavaliar"),
    (10, 14, "Moderado", "Considerar psicoterapia"),
    (15, 21, "Grave", "Intervencao imediata recomendada"),
]

_db = SimpleDB("gad7_clinico")

class Gad7ClinicoPlugin(PluginBase):
    name = "gad7_real"
    version = "3.0.0"
    description = "GAD-7 clinico com scoring real"
    category = "avaliacao_psicologica"

    def setup(self, app):
        app.include_router(router)
        logger.info("[gad7_real] OK -> /api/v1/gad7-clinico")

    def health_check(self):
        return {"status": "healthy", "total": _db.count()}

@router.get("/perguntas")
async def perguntas():
    return {
        "escala": "GAD-7",
        "instrucao": "Nas ultimas 2 semanas, com que frequencia:",
        "perguntas": [{"id": i+1, "texto": q} for i, q in enumerate(PERGUNTAS)],
        "opcoes": {0:"Nenhuma vez", 1:"Menos de 1 semana",
                   2:"Uma semana ou mais", 3:"Quase todos os dias"},
        "tempo_min": 2
    }

@router.post("/aplicar")
async def aplicar(
    user_id: str,
    respostas: List[int] = Body(..., example=[0,1,2,1,0,1,2])
):
    if len(respostas) != 7:
        raise HTTPException(400, f"Envie 7 respostas (0-3). Recebido: {len(respostas)}")
    for i, r in enumerate(respostas):
        if r not in [0,1,2,3]:
            raise HTTPException(400, f"Resposta {i+1} invalida: {r}")

    score = sum(respostas)
    nivel, rec = next(
        ((n, r) for mi, ma, n, r in CLASSIF if mi <= score <= ma),
        ("?", "Consulte profissional")
    )

    resultado = {
        "id": str(uuid.uuid4())[:8],
        "user_id": user_id,
        "escala": "GAD-7",
        "score": score,
        "score_maximo": 21,
        "nivel": nivel,
        "recomendacao": rec,
        "data": datetime.utcnow().isoformat()
    }
    _db.create(nome=f"GAD7_{user_id}", user_id=user_id,
               valor=str(score), dados=json.dumps(resultado), categoria=nivel)
    return resultado

@router.get("/historico/{user_id}")
async def historico(user_id: str):
    avs = _db.list(user_id=user_id, limite=20)
    return {"total": len(avs), "historico": avs}

plugin = Gad7ClinicoPlugin()
