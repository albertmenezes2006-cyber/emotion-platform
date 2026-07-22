from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import os, uuid, psycopg2, json

router = APIRouter(prefix="/api/v1/phq9", tags=["PHQ9"])
DATABASE_URL = os.getenv("DATABASE_URL", "")

def get_conn():
    url = DATABASE_URL.replace("postgres://", "postgresql://")
    return psycopg2.connect(url, sslmode="require", connect_timeout=10)

def init_table():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phq9_resultados (
                id VARCHAR(8) PRIMARY KEY,
                paciente_id VARCHAR(200),
                score INTEGER,
                nivel VARCHAR(100),
                cor VARCHAR(50),
                percentual FLOAT,
                alerta BOOLEAN,
                respostas TEXT,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        cur.close()
        conn.close()
    except: pass

init_table()

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
        return JSONResponse({"erro":"PHQ-9 requer 9 respostas (0-3)"}, status_code=400)
    score = sum(int(r) for r in respostas)
    nivel, cor = interpretar(score)
    resultado = {
        "score": score, "max": 27, "nivel": nivel, "cor": cor,
        "percentual": round(score/27*100, 1),
        "recomendacao": "Busque suporte profissional" if score >= 10 else "Continue monitorando",
        "alerta": score >= 15,
        "timestamp": datetime.utcnow().isoformat()
    }
    paciente = d.get("paciente_id", "anonimo")
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO phq9_resultados (id,paciente_id,score,nivel,cor,percentual,alerta,respostas) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
            (str(uuid.uuid4())[:8], paciente, score, nivel, cor, resultado["percentual"], score>=15, json.dumps(respostas))
        )
        conn.commit()
        cur.close()
        conn.close()
    except: pass
    return JSONResponse(resultado)

@router.get("/historico/{paciente_id}")
async def historico(paciente_id: str):
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "SELECT score,nivel,cor,percentual,alerta,criado_em FROM phq9_resultados WHERE paciente_id=%s ORDER BY criado_em DESC LIMIT 20",
            (paciente_id,)
        )
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return JSONResponse({"historico":[{"score":r[0],"nivel":r[1],"cor":r[2],"percentual":r[3],"alerta":r[4],"data":str(r[5])} for r in rows],"total":len(rows)})
    except: return JSONResponse({"historico":[],"total":0})

@router.post("/avaliacao")
async def avaliacao_completa(request: Request):
    return await calcular(request)

class Plugin(PluginBase):
    name = "phq9_calcular"
    def setup(self, app): app.include_router(router)

plugin = Plugin()
