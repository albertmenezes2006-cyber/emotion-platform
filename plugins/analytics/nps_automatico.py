from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import os, uuid, psycopg2

router = APIRouter(prefix="/api/v1/nps", tags=["NPS"])
DATABASE_URL = os.getenv("DATABASE_URL", "")

def get_conn():
    url = DATABASE_URL.replace("postgres://", "postgresql://")
    return psycopg2.connect(url, sslmode="require", connect_timeout=10)

def init_table():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS nps_respostas (
                id VARCHAR(8) PRIMARY KEY,
                nota INTEGER,
                comentario TEXT,
                email VARCHAR(200),
                categoria VARCHAR(20),
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        cur.close()
        conn.close()
    except: pass

init_table()

@router.post("/responder")
async def responder_nps(request: Request):
    dados = await request.json()
    nota = int(dados.get("nota", 0))
    categoria = "promotor" if nota >= 9 else "neutro" if nota >= 7 else "detrator"
    uid = str(uuid.uuid4())[:8]
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO nps_respostas (id,nota,comentario,email,categoria)
            VALUES (%s,%s,%s,%s,%s)
        """, (uid, nota, dados.get("comentario",""), dados.get("email",""), categoria))
        conn.commit()
        cur.close()
        conn.close()
        return JSONResponse({"ok":True,"categoria":categoria})
    except Exception as e:
        return JSONResponse({"ok":False,"erro":str(e)})

@router.get("/resultado")
async def resultado():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT nota, categoria FROM nps_respostas")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        if not rows:
            return JSONResponse({"nps":0,"total":0,"promotores":0,"neutros":0,"detratores":0})
        total = len(rows)
        promotores = sum(1 for r in rows if r[1] == "promotor")
        detratores = sum(1 for r in rows if r[1] == "detrator")
        nps = round(((promotores - detratores) / total) * 100, 1)
        return JSONResponse({
            "nps": nps,
            "total": total,
            "promotores": promotores,
            "neutros": sum(1 for r in rows if r[1] == "neutro"),
            "detratores": detratores
        })
    except Exception as e:
        return JSONResponse({"nps":0,"total":0,"erro":str(e)})

class Plugin(PluginBase):
    name = "nps_automatico"
    def setup(self, app): app.include_router(router)

plugin = Plugin()
