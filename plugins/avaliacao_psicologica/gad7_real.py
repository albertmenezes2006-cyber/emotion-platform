"""Plugin: GAD-7 Real — Escala de Ansiedade"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
from plugins.db_manager import SimpleDB
import uuid, json, logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/gad7", tags=["avaliacao_psicologica"])

PERGUNTAS = [
    "Sentir-se nervoso, ansioso ou no limite",
    "Não ser capaz de parar ou controlar as preocupações",
    "Preocupar-se muito com diferentes coisas",
    "Dificuldade para relaxar",
    "Estar tão agitado que é difícil ficar parado",
    "Ficar facilmente contrariado ou irritável",
    "Sentir medo como se algo terrível fosse acontecer"
]

OPCOES = {0: "Nenhuma vez", 1: "Menos de uma semana", 2: "Uma semana ou mais", 3: "Quase todos os dias"}

CLASSIFICACAO = [
    (0, 4, "Mínimo", "Sem ansiedade significativa"),
    (5, 9, "Leve", "Monitorar e reavaliar em 2 semanas"),
    (10, 14, "Moderado", "Considerar psicoterapia e/ou farmacoterapia"),
    (15, 21, "Grave", "Intervenção imediata — encaminhar especialista"),
]

_db = SimpleDB("gad7_avaliacoes")

class Gad7RealPlugin(PluginBase):
    name = "gad7_real"; version = "2.0.0"
    description = "GAD-7 real com scoring clínico"; category = "avaliacao_psicologica"
    def setup(self, app): app.include_router(router); logger.info("[gad7_real] OK")
    def health_check(self): return {"status": "healthy", "total": _db.count()}

@router.get("/perguntas")
async def perguntas():
    return {
        "escala": "GAD-7",
        "descricao": "Generalized Anxiety Disorder 7-item scale",
        "instrucao": "Nas últimas 2 semanas, com que frequência você foi incomodado por:",
        "perguntas": [{"id": i+1, "texto": q} for i, q in enumerate(PERGUNTAS)],
        "opcoes": OPCOES
    }

@router.post("/aplicar")
async def aplicar(user_id: str, respostas: list, observacoes: str = ""):
    if len(respostas) != 7:
        raise HTTPException(400, f"Envie 7 respostas (0-3). Recebido: {len(respostas)}")
    for i, r in enumerate(respostas):
        if r not in [0, 1, 2, 3]:
            raise HTTPException(400, f"Resposta {i+1} inválida: {r}")

    score = sum(respostas)
    classif = next(((n, r) for mi, ma, n, r in CLASSIFICACAO if mi <= score <= ma), ("Indefinido", ""))

    resultado = {
        "id": str(uuid.uuid4())[:8],
        "user_id": user_id,
        "escala": "GAD-7",
        "score": score,
        "score_maximo": 21,
        "nivel": classif[0],
        "recomendacao": classif[1],
        "respostas": [{"pergunta": PERGUNTAS[i], "resposta": r, "descricao": OPCOES[r]} for i, r in enumerate(respostas)],
        "observacoes": observacoes,
        "data": datetime.utcnow().isoformat()
    }
    _db.create(nome=f"GAD7_{user_id}", user_id=user_id, valor=str(score), dados=json.dumps(resultado), categoria=classif[0])
    return resultado

@router.get("/historico/{user_id}")
async def historico(user_id: str):
    avs = _db.list(user_id=user_id, limite=20)
    return {"total": len(avs), "historico": avs}

plugin = Gad7RealPlugin()
