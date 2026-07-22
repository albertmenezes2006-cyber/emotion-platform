from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import os, uuid, psycopg2

router_l = APIRouter(prefix="/api/v1/lembretes", tags=["Lembretes"])
router_x = APIRouter(prefix="/api/v1/xp-lembretes", tags=["XP"])
DATABASE_URL = os.getenv("DATABASE_URL", "")

def get_conn():
    url = DATABASE_URL.replace("postgres://", "postgresql://")
    return psycopg2.connect(url, sslmode="require", connect_timeout=10)

def init_table():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS lembretes (
                id VARCHAR(8) PRIMARY KEY,
                user_id VARCHAR(200),
                titulo VARCHAR(500),
                horario VARCHAR(20),
                dias TEXT,
                ativo BOOLEAN DEFAULT TRUE,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        cur.close()
        conn.close()
    except: pass

init_table()

@router_l.post("/criar")
async def criar_l(request: Request):
    d = await request.json()
    uid = str(uuid.uuid4())[:8]
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO lembretes (id,user_id,titulo,horario,dias,ativo)
            VALUES (%s,%s,%s,%s,%s,%s)
        """, (uid, d.get("user_id","anonimo"), d.get("titulo",""), d.get("horario",""), str(d.get("dias",[])), True))
        conn.commit()
        cur.close()
        conn.close()
        return JSONResponse({"ok":True,"id":uid})
    except Exception as e:
        return JSONResponse({"ok":False,"erro":str(e)})

@router_l.get("/listar")
async def listar_l(user_id: str = ""):
    try:
        conn = get_conn()
        cur = conn.cursor()
        if user_id:
            cur.execute("SELECT id,titulo,horario,dias,ativo FROM lembretes WHERE user_id=%s ORDER BY criado_em DESC", (user_id,))
        else:
            cur.execute("SELECT id,titulo,horario,dias,ativo FROM lembretes ORDER BY criado_em DESC LIMIT 50")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return JSONResponse({"lembretes":[{"id":r[0],"titulo":r[1],"horario":r[2],"dias":r[3],"ativo":r[4]} for r in rows]})
    except Exception as e:
        return JSONResponse({"lembretes":[],"erro":str(e)})

@router_x.get("/perfil/{uid}")
async def perfil_xp(uid: str):
    return JSONResponse({"user_id":uid,"xp":0,"nivel":"Iniciante"})

class Plugin(PluginBase):
    name = "lembretes_xp_fix"
    def setup(self, app):
        app.include_router(router_l)
        app.include_router(router_x)

plugin = Plugin()
