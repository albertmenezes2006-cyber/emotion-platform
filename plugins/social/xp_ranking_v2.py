from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import os, psycopg2

router = APIRouter(prefix="/api/v1/xp-ranking", tags=["XP"])
DATABASE_URL = os.getenv("DATABASE_URL", "")

NIVEIS = [
    {"nivel":1,"nome":"Iniciante","xp_min":0,"icone":"🌱"},
    {"nivel":2,"nome":"Explorador","xp_min":100,"icone":"🔍"},
    {"nivel":3,"nome":"Expert","xp_min":300,"icone":"⭐"},
    {"nivel":4,"nome":"Mestre","xp_min":600,"icone":"🏆"}
]
ACOES = {"avaliacao_phq9":50,"avaliacao_gad7":50,"entrada_diario":20,"chat_ia":10,"login_diario":5,"indicar_amigo":200}

def get_conn():
    url = DATABASE_URL.replace("postgres://", "postgresql://")
    return psycopg2.connect(url, sslmode="require", connect_timeout=10)

def init_table():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS xp_usuarios (
                user_id VARCHAR(200) PRIMARY KEY,
                xp INTEGER DEFAULT 0,
                atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        cur.close()
        conn.close()
    except: pass

init_table()

def get_nivel(xp):
    n = NIVEIS[0]
    for nv in NIVEIS:
        if xp >= nv["xp_min"]: n = nv
    return n

@router.post("/ganhar/{uid}/{acao}")
async def ganhar(uid: str, acao: str):
    pts = ACOES.get(acao, 10)
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO xp_usuarios (user_id, xp) VALUES (%s, %s)
            ON CONFLICT (user_id) DO UPDATE SET xp = xp_usuarios.xp + %s, atualizado_em = NOW()
        """, (uid, pts, pts))
        conn.commit()
        cur.execute("SELECT xp FROM xp_usuarios WHERE user_id=%s", (uid,))
        total = cur.fetchone()[0]
        cur.close()
        conn.close()
        return JSONResponse({"ok":True,"xp_ganho":pts,"xp_total":total,"nivel":get_nivel(total)})
    except Exception as e:
        return JSONResponse({"ok":False,"erro":str(e)})

@router.get("/perfil/{uid}")
async def perfil(uid: str):
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT xp FROM xp_usuarios WHERE user_id=%s", (uid,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        xp_total = row[0] if row else 0
        return JSONResponse({"user_id":uid,"xp":xp_total,"nivel":get_nivel(xp_total)})
    except: return JSONResponse({"user_id":uid,"xp":0,"nivel":NIVEIS[0]})

@router.get("/ranking")
async def ranking():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT user_id,xp FROM xp_usuarios ORDER BY xp DESC LIMIT 10")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return JSONResponse({"ranking":[{"posicao":i+1,"user_id":r[0],"xp":r[1],"nivel":get_nivel(r[1])} for i,r in enumerate(rows)]})
    except: return JSONResponse({"ranking":[]})

class Plugin(PluginBase):
    name = "xp_ranking_v2"
    def setup(self, app): app.include_router(router)

plugin = Plugin()
