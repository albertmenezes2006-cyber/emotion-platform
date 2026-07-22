from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import os, uuid, psycopg2

router = APIRouter(prefix="/cbt/pensamentos", tags=["CBT"])
DATABASE_URL = os.getenv("DATABASE_URL", "")

def get_conn():
    url = DATABASE_URL.replace("postgres://", "postgresql://")
    return psycopg2.connect(url, sslmode="require", connect_timeout=10)

def init_table():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS cbt_pensamentos (
                id VARCHAR(8) PRIMARY KEY,
                user_id VARCHAR(200),
                situacao TEXT,
                pensamento TEXT,
                emocao TEXT,
                comportamento TEXT,
                alternativa TEXT,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        cur.close()
        conn.close()
    except: pass

init_table()

@router.post("/registrar")
async def registrar(request: Request):
    d = await request.json()
    uid = str(uuid.uuid4())[:8]
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO cbt_pensamentos (id,user_id,situacao,pensamento,emocao,comportamento,alternativa)
            VALUES (%s,%s,%s,%s,%s,%s,%s)
        """, (uid, d.get("user_id","anonimo"), d.get("situacao",""), d.get("pensamento",""),
              d.get("emocao",""), d.get("comportamento",""), d.get("alternativa","")))
        conn.commit()
        cur.close()
        conn.close()
        return JSONResponse({"ok":True,"id":uid})
    except Exception as e:
        return JSONResponse({"ok":False,"erro":str(e)}, status_code=500)

@router.get("/listar")
async def listar(user_id: str = ""):
    try:
        conn = get_conn()
        cur = conn.cursor()
        if user_id:
            cur.execute("SELECT id,situacao,pensamento,emocao,criado_em FROM cbt_pensamentos WHERE user_id=%s ORDER BY criado_em DESC LIMIT 10", (user_id,))
        else:
            cur.execute("SELECT id,situacao,pensamento,emocao,criado_em FROM cbt_pensamentos ORDER BY criado_em DESC LIMIT 10")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return JSONResponse({"registros":[{"id":r[0],"situacao":r[1],"pensamento":r[2],"emocao":r[3],"data":str(r[4])} for r in rows],"total":len(rows)})
    except Exception as e:
        return JSONResponse({"registros":[],"total":0,"erro":str(e)})

class Plugin(PluginBase):
    name = "cbt_thought_record_v2"
    def setup(self, app): app.include_router(router)

plugin = Plugin()
