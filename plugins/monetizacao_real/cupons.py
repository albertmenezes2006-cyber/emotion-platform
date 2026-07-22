from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import os, psycopg2, json

router = APIRouter(prefix="/api/v1/cupons", tags=["Cupons"])
DATABASE_URL = os.getenv("DATABASE_URL", "")

CUPONS_DEFAULT = {
    "BEMVINDO": {"desconto":50,"tipo":"percentual","limite":100,"usado":0,"validade":"2026-12-31","descricao":"50% off primeiro mes"},
    "PSICOLOGO": {"desconto":30,"tipo":"percentual","limite":50,"usado":0,"validade":"2026-12-31","descricao":"30% para psicologos"},
    "LAUNCH": {"desconto":100,"tipo":"percentual","limite":10,"usado":0,"validade":"2026-08-01","descricao":"Gratis no lancamento"},
    "ALBERT10": {"desconto":10,"tipo":"reais","limite":999,"usado":0,"validade":"2026-12-31","descricao":"R$10 off"}
}

def get_conn():
    url = DATABASE_URL.replace("postgres://", "postgresql://")
    return psycopg2.connect(url, sslmode="require", connect_timeout=10)

def init_table():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS cupons (
                codigo VARCHAR(50) PRIMARY KEY,
                desconto INTEGER,
                tipo VARCHAR(20),
                limite INTEGER,
                usado INTEGER DEFAULT 0,
                validade VARCHAR(20),
                descricao VARCHAR(200)
            )
        """)
        for codigo, c in CUPONS_DEFAULT.items():
            cur.execute("""
                INSERT INTO cupons (codigo,desconto,tipo,limite,usado,validade,descricao)
                VALUES (%s,%s,%s,%s,%s,%s,%s)
                ON CONFLICT (codigo) DO NOTHING
            """, (codigo, c["desconto"], c["tipo"], c["limite"], c["usado"], c["validade"], c["descricao"]))
        conn.commit()
        cur.close()
        conn.close()
    except: pass

init_table()

@router.post("/validar")
async def validar(request: Request):
    d = await request.json()
    codigo = (d.get("codigo") or "").upper().strip()
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT codigo,desconto,tipo,limite,usado,validade FROM cupons WHERE codigo=%s", (codigo,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if not row:
            return JSONResponse({"valido":False,"erro":"Cupom nao encontrado"})
        codigo_db,desconto,tipo,limite,usado,validade = row
        if usado >= limite:
            return JSONResponse({"valido":False,"erro":"Cupom esgotado"})
        if validade < datetime.now().strftime("%Y-%m-%d"):
            return JSONResponse({"valido":False,"erro":"Cupom expirado"})
        return JSONResponse({"valido":True,"codigo":codigo_db,"desconto":desconto,"tipo":tipo,"descricao":f"{desconto}{'%' if tipo=='percentual' else ' reais'} de desconto"})
    except Exception as e:
        return JSONResponse({"valido":False,"erro":str(e)})

@router.post("/usar")
async def usar(request: Request):
    d = await request.json()
    codigo = (d.get("codigo") or "").upper().strip()
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("UPDATE cupons SET usado=usado+1 WHERE codigo=%s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return JSONResponse({"ok":True})
    except: return JSONResponse({"ok":False})

@router.get("/listar")
async def listar():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT codigo,desconto,tipo,limite,usado,validade,descricao FROM cupons")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return JSONResponse({"cupons":[{"codigo":r[0],"desconto":r[1],"tipo":r[2],"limite":r[3],"usado":r[4],"validade":r[5],"descricao":r[6]} for r in rows]})
    except: return JSONResponse({"cupons":[]})

class Plugin(PluginBase):
    name = "cupons_desconto"
    def setup(self, app): app.include_router(router)

plugin = Plugin()
