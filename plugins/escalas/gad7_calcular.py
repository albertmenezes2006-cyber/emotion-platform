#!/usr/bin/env python3
"""Escala GAD-7 — Ansiedade Generalizada"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import os, uuid, psycopg2, json

router = APIRouter(prefix="/api/v1/gad7", tags=["Escalas"])
DATABASE_URL = os.getenv("DATABASE_URL", "")

PERGUNTAS = [
    "Sentir-se nervoso, ansioso ou muito tenso",
    "Nao ser capaz de impedir ou controlar as preocupacoes",
    "Preocupar-se muito com diversas coisas",
    "Dificuldade para relaxar",
    "Ficar tao agitado que se torna dificil permanecer sentado",
    "Ficar facilmente aborrecido ou irritavel",
    "Sentir medo como se algo horrivel fosse acontecer",
]

def get_conn():
    url = DATABASE_URL.replace("postgres://", "postgresql://")
    return psycopg2.connect(url, sslmode="require", connect_timeout=10)

def init_table():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS gad7_resultados (
                id VARCHAR(8) PRIMARY KEY,
                paciente_id VARCHAR(200),
                score INTEGER,
                nivel VARCHAR(100),
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

@router.post("/calcular")
async def calcular_gad7(request: Request):
    try:
        body = await request.json()
        respostas = body if isinstance(body, list) else body.get("respostas", [])
        paciente = body.get("paciente_id", "anonimo") if isinstance(body, dict) else "anonimo"
    except:
        respostas = []
        paciente = "anonimo"
    total = sum(int(v) for v in respostas[:7] if str(v).isdigit())
    nivel = "Minima" if total <= 4 else "Leve" if total <= 9 else "Moderada" if total <= 14 else "Grave"
    resultado = {
        "score": total, "max": 21, "nivel": nivel,
        "percentual": round(total/21*100, 1),
        "alerta": total >= 15,
        "timestamp": datetime.utcnow().isoformat()
    }
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO gad7_resultados (id,paciente_id,score,nivel,percentual,alerta,respostas) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (str(uuid.uuid4())[:8], paciente, total, nivel, resultado["percentual"], total>=15, json.dumps(respostas))
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
            "SELECT score,nivel,percentual,alerta,criado_em FROM gad7_resultados WHERE paciente_id=%s ORDER BY criado_em DESC LIMIT 20",
            (paciente_id,)
        )
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return JSONResponse({"historico":[{"score":r[0],"nivel":r[1],"percentual":r[2],"alerta":r[3],"data":str(r[4])} for r in rows],"total":len(rows)})
    except: return JSONResponse({"historico":[],"total":0})

@router.get("/info")
async def info_gad7():
    return JSONResponse({"nome":"GAD-7","perguntas":7,"max":21,
                         "classificacao":{"0-4":"Minima","5-9":"Leve","10-14":"Moderada","15-21":"Grave"}})

class GAD7Plugin(PluginBase):
    name = "gad7_ansiedade"
    def setup(self, app): app.include_router(router)

plugin = GAD7Plugin()
