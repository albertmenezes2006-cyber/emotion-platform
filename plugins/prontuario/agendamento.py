from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import os, uuid, psycopg2

router = APIRouter(prefix="/api/v1/agenda", tags=["Agenda"])
DATABASE_URL = os.getenv("DATABASE_URL", "")

def get_conn():
    url = DATABASE_URL.replace("postgres://", "postgresql://")
    return psycopg2.connect(url, sslmode="require", connect_timeout=10)

def init_table():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS agenda_sessoes_v2 (
                id VARCHAR(8) PRIMARY KEY,
                paciente VARCHAR(200),
                psicologo VARCHAR(200),
                data VARCHAR(20),
                hora VARCHAR(10),
                tipo VARCHAR(50) DEFAULT 'presencial',
                status VARCHAR(50) DEFAULT 'agendado',
                link_video VARCHAR(500) DEFAULT '',
                notas TEXT DEFAULT '',
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        cur.close()
        conn.close()
    except: pass

init_table()

@router.post("/criar")
async def criar_sessao(request: Request):
    d = await request.json()
    uid = str(uuid.uuid4())[:8]
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO agenda_sessoes_v2 (id,paciente,psicologo,data,hora,tipo,status,link_video,notas)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, (uid, d.get("paciente",""), d.get("psicologo",""), d.get("data",""),
              d.get("hora",""), d.get("tipo","presencial"), "agendado",
              d.get("link_video",""), d.get("notas","")))
        conn.commit()
        cur.close()
        conn.close()
        return JSONResponse({"ok":True,"sessao_id":uid})
    except Exception as e:
        return JSONResponse({"ok":False,"erro":str(e)}, status_code=500)

@router.get("/listar")
async def listar_sessoes(psicologo: str = ""):
    try:
        conn = get_conn()
        cur = conn.cursor()
        if psicologo:
            cur.execute("SELECT * FROM agenda_sessoes_v2 WHERE psicologo=%s ORDER BY data,hora", (psicologo,))
        else:
            cur.execute("SELECT * FROM agenda_sessoes_v2 ORDER BY data,hora")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        sessoes = [{"id":r[0],"paciente":r[1],"psicologo":r[2],"data":r[3],"hora":r[4],"tipo":r[5],"status":r[6],"link_video":r[7],"notas":r[8]} for r in rows]
        return JSONResponse({"sessoes":sessoes,"total":len(sessoes)})
    except Exception as e:
        return JSONResponse({"sessoes":[],"total":0,"erro":str(e)})

@router.put("/status/{sessao_id}")
async def atualizar_status(sessao_id: str, request: Request):
    d = await request.json()
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("UPDATE agenda_sessoes_v2 SET status=%s WHERE id=%s", (d.get("status","agendado"), sessao_id))
        conn.commit()
        cur.close()
        conn.close()
        return JSONResponse({"ok":True})
    except Exception as e:
        return JSONResponse({"ok":False,"erro":str(e)})

@router.delete("/cancelar/{sessao_id}")
async def cancelar(sessao_id: str):
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("UPDATE agenda_sessoes_v2 SET status='cancelado' WHERE id=%s", (sessao_id,))
        conn.commit()
        cur.close()
        conn.close()
        return JSONResponse({"ok":True})
    except Exception as e:
        return JSONResponse({"ok":False,"erro":str(e)})

class Plugin(PluginBase):
    name = "agendamento_sessoes"
    def setup(self, app): app.include_router(router)

plugin = Plugin()
