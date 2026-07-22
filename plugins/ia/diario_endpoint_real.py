from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import os, uuid, psycopg2

router = APIRouter(prefix="/api/v1/diario", tags=["Diario"])
DATABASE_URL = os.getenv("DATABASE_URL", "")

def get_conn():
    url = DATABASE_URL.replace("postgres://", "postgresql://")
    return psycopg2.connect(url, sslmode="require", connect_timeout=10)

def init_table():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS diario_entradas (
                id VARCHAR(8) PRIMARY KEY,
                user_id VARCHAR(200),
                conteudo TEXT,
                humor INTEGER DEFAULT 5,
                tags TEXT DEFAULT '',
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        cur.close()
        conn.close()
    except: pass

init_table()

@router.post("/salvar")
async def salvar(request: Request):
    d = await request.json()
    uid = str(uuid.uuid4())[:8]
    user_id = d.get("user_id", "anonimo")
    conteudo = d.get("conteudo", "")
    humor = int(d.get("humor", 5))
    tags = str(d.get("tags", []))
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO diario_entradas (id,user_id,conteudo,humor,tags) VALUES (%s,%s,%s,%s,%s)",
            (uid, user_id, conteudo, humor, tags)
        )
        conn.commit()
        cur.close()
        conn.close()
        return JSONResponse({"ok":True,"id":uid,"xp_ganho":20})
    except Exception as e:
        return JSONResponse({"ok":False,"erro":str(e)}, status_code=500)

@router.get("/listar/{user_id}")
async def listar(user_id: str):
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "SELECT id,user_id,conteudo,humor,tags,criado_em FROM diario_entradas WHERE user_id=%s ORDER BY criado_em DESC LIMIT 50",
            (user_id,)
        )
        rows = cur.fetchall()
        cur.close()
        conn.close()
        entradas = [{"id":r[0],"user_id":r[1],"conteudo":r[2],"humor":r[3],"tags":r[4],"data":str(r[5])} for r in rows]
        return JSONResponse({"entradas":entradas,"total":len(entradas)})
    except Exception as e:
        return JSONResponse({"entradas":[],"total":0,"erro":str(e)})

@router.get("/stats/{user_id}")
async def stats(user_id: str):
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "SELECT humor FROM diario_entradas WHERE user_id=%s",
            (user_id,)
        )
        rows = cur.fetchall()
        cur.close()
        conn.close()
        humores = [r[0] for r in rows]
        media = sum(humores)/max(1,len(humores))
        return JSONResponse({"total_entradas":len(humores),"humor_medio":round(media,1),"streak":len(humores)})
    except Exception as e:
        return JSONResponse({"total_entradas":0,"humor_medio":5,"streak":0})

class Plugin(PluginBase):
    name = "diario_endpoint_real"
    def setup(self, app): app.include_router(router)

plugin = Plugin()
