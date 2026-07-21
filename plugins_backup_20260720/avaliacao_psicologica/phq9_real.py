"""Plugin: PHQ-9 Clinico Real"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException, Body
from datetime import datetime
from plugins.db_manager import SimpleDB
import uuid
import json
import logging
from typing import List

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/phq9-clinico", tags=["avaliacao_clinica"])

PERGUNTAS = [
    "Pouco interesse ou prazer em fazer as coisas",
    "Sentir-se triste, deprimido ou sem esperanca",
    "Dificuldade para adormecer ou dormindo demais",
    "Sentir-se cansado ou com pouca energia",
    "Falta de apetite ou comer demais",
    "Sentir-se mal consigo mesmo ou fracasso",
    "Dificuldade de concentrar-se",
    "Mover ou falar lentamente que outros notaram",
    "Pensamentos de se machucar"
]

CLASSIF = [
    (0, 4, "Minimo", "Sem depressao significativa"),
    (5, 9, "Leve", "Monitorar e reavaliar"),
    (10, 14, "Moderado", "Iniciar plano de tratamento"),
    (15, 19, "Moderado-Grave", "Tratamento ativo recomendado"),
    (20, 27, "Grave", "Tratamento imediato necessario"),
]

_db = SimpleDB("phq9_clinico")

class Phq9ClinicoPlugin(PluginBase):
    name = "phq9_real"
    version = "3.0.0"
    description = "PHQ-9 clinico com scoring real"
    category = "avaliacao_psicologica"

    def setup(self, app):
        app.include_router(router)
        logger.info("[phq9_real] OK -> /api/v1/phq9-clinico")

    def health_check(self):
        return {"status": "healthy", "total": _db.count()}

@router.get("/perguntas")
async def perguntas():
    return {
        "escala": "PHQ-9",
        "instrucao": "Nas ultimas 2 semanas, com que frequencia:",
        "perguntas": [{"id": i+1, "texto": q} for i, q in enumerate(PERGUNTAS)],
        "opcoes": {0:"Nenhuma vez", 1:"Menos de 1 semana",
                   2:"Uma semana ou mais", 3:"Quase todos os dias"},
        "tempo_min": 3
    }

@router.post("/aplicar")
async def aplicar(
    user_id: str,
    respostas: List[int] = Body(..., example=[0,1,2,1,0,1,2,0,0])
):
    if len(respostas) != 9:
        raise HTTPException(400, f"Envie 9 respostas (0-3). Recebido: {len(respostas)}")
    for i, r in enumerate(respostas):
        if r not in [0,1,2,3]:
            raise HTTPException(400, f"Resposta {i+1} invalida: {r}")

    score = sum(respostas)
    nivel, rec = next(
        ((n, r) for mi, ma, n, r in CLASSIF if mi <= score <= ma),
        ("?", "Consulte profissional")
    )
    alerta = respostas[8] >= 1

    resultado = {
        "id": str(uuid.uuid4())[:8],
        "user_id": user_id,
        "escala": "PHQ-9",
        "score": score,
        "score_maximo": 27,
        "classificacao": {"nivel": nivel, "recomendacao": rec},
        "alerta_suicidio": alerta,
        "data": datetime.utcnow().isoformat()
    }
    _db.create(nome=f"PHQ9_{user_id}", user_id=user_id,
               valor=str(score), dados=json.dumps(resultado), categoria=nivel)

    if alerta:
        logger.warning("ALERTA Q9>0 user=%s score=%d", user_id, score)
    return resultado

@router.get("/historico/{user_id}")
async def historico(user_id: str):
    avs = _db.list(user_id=user_id, limite=20)
    return {"total": len(avs), "historico": avs}

plugin = Phq9ClinicoPlugin()
