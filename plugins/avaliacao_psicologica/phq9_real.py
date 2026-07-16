"""
Plugin: PHQ-9 Real — Escala de Depressão com persistência e scoring real
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
from plugins.db_manager import SimpleDB
import uuid, json, logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/phq9", tags=["avaliacao_psicologica"])

PERGUNTAS = [
    "Pouco interesse ou prazer em fazer as coisas",
    "Sentir-se triste, deprimido ou sem esperança",
    "Dificuldade para adormecer, continuar dormindo ou dormindo demais",
    "Sentir-se cansado ou com pouca energia",
    "Falta de apetite ou comer demais",
    "Sentir-se mal consigo mesmo — ou achar que é um fracasso",
    "Dificuldade de concentrar-se nas coisas",
    "Mover ou falar tão lentamente que outras pessoas notaram — ou estar tão agitado",
    "Pensamentos de que seria melhor estar morto ou de se machucar"
]

OPCOES = {0: "Nenhuma vez", 1: "Menos de uma semana", 2: "Uma semana ou mais", 3: "Quase todos os dias"}

CLASSIFICACAO = [
    (0, 4, "Mínimo", "Sem depressão significativa", "verde"),
    (5, 9, "Leve", "Sintomas leves — Monitorar e reavaliar", "amarelo"),
    (10, 14, "Moderado", "Iniciar plano de tratamento", "laranja"),
    (15, 19, "Moderado-Grave", "Tratamento ativo e farmacoterapia", "vermelho"),
    (20, 27, "Grave", "Tratamento imediato — urgente", "vermelho_escuro"),
]

_db = SimpleDB("phq9_avaliacoes")

class Phq9RealPlugin(PluginBase):
    name = "phq9_real"; version = "2.0.0"
    description = "PHQ-9 real com scoring clínico e persistência"; category = "avaliacao_psicologica"
    def setup(self, app): app.include_router(router); logger.info("[phq9_real] OK")
    def health_check(self): return {"status": "healthy", "total_avaliacoes": _db.count()}

@router.get("/perguntas")
async def obter_perguntas():
    return {
        "escala": "PHQ-9",
        "descricao": "Patient Health Questionnaire-9 para rastreio de depressão",
        "instrucao": "Nas últimas 2 semanas, com que frequência você foi incomodado por:",
        "perguntas": [{"id": i+1, "texto": q} for i, q in enumerate(PERGUNTAS)],
        "opcoes": OPCOES,
        "tempo_estimado_min": 3
    }

@router.post("/aplicar")
async def aplicar_phq9(user_id: str, respostas: list, observacoes: str = ""):
    if len(respostas) != 9:
        raise HTTPException(400, f"Envie exatamente 9 respostas (0-3). Recebido: {len(respostas)}")

    for i, r in enumerate(respostas):
        if r not in [0, 1, 2, 3]:
            raise HTTPException(400, f"Resposta {i+1} inválida: {r}. Use 0-3")

    score_total = sum(respostas)

    classificacao = None
    for minimo, maximo, nivel, recomendacao, cor in CLASSIFICACAO:
        if minimo <= score_total <= maximo:
            classificacao = {"nivel": nivel, "recomendacao": recomendacao, "cor": cor}
            break

    alerta_suicidio = respostas[8] >= 1
    detalhes = [
        {"pergunta": PERGUNTAS[i], "resposta": r, "descricao": OPCOES[r]}
        for i, r in enumerate(respostas)
    ]

    resultado = {
        "id": str(uuid.uuid4())[:8],
        "user_id": user_id,
        "escala": "PHQ-9",
        "score": score_total,
        "score_maximo": 27,
        "percentual": round(score_total/27*100, 1),
        "classificacao": classificacao,
        "alerta_suicidio": alerta_suicidio,
        "respostas_detalhadas": detalhes,
        "observacoes": observacoes,
        "data": datetime.utcnow().isoformat(),
        "proxima_avaliacao": "2 semanas"
    }

    _db.create(
        nome=f"PHQ9_{user_id}",
        user_id=user_id,
        valor=str(score_total),
        dados=json.dumps(resultado),
        categoria=classificacao["nivel"] if classificacao else "indefinido"
    )

    if alerta_suicidio:
        logger.warning(f"[ALERTA SUICÍDIO] PHQ-9 Q9>0 — user {user_id} — score {score_total}")

    return resultado

@router.get("/historico/{user_id}")
async def historico_phq9(user_id: str):
    avaliacoes = _db.list(user_id=user_id, limite=20)
    resultados = []
    for av in avaliacoes:
        try:
            dados = json.loads(av.get("dados", "{}"))
            resultados.append({
                "data": av.get("criado_em"),
                "score": dados.get("score"),
                "nivel": dados.get("classificacao", {}).get("nivel"),
                "alerta_suicidio": dados.get("alerta_suicidio", False)
            })
        except Exception:
            pass
    tendencia = "sem dados"
    if len(resultados) >= 2:
        if resultados[0]["score"] < resultados[-1]["score"]:
            tendencia = "melhora"
        elif resultados[0]["score"] > resultados[-1]["score"]:
            tendencia = "piora"
        else:
            tendencia = "estavel"
    return {
        "user_id": user_id,
        "total_avaliacoes": len(resultados),
        "tendencia": tendencia,
        "historico": resultados
    }

@router.get("/stats/populacao")
async def stats_populacao():
    total = _db.count()
    return {
        "total_avaliacoes": total,
        "escala": "PHQ-9",
        "referencia": "Kroenke K, Spitzer RL, Williams JB. J Gen Intern Med. 2001"
    }

plugin = Phq9RealPlugin()
