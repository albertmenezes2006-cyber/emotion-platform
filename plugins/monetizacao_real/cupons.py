from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import os, psycopg2

router = APIRouter(prefix="/api/v1/cupons", tags=["Cupons"])
DATABASE_URL = os.getenv("DATABASE_URL", "")

def get_conn():
    url = DATABASE_URL.replace("postgres://", "postgresql://")
    return psycopg2.connect(url, sslmode="require", connect_timeout=10)

def init_cupons():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cupons_default = [
            ("BEMVINDO", 50, True, 100, "2026-12-31"),
            ("PSICOLOGO", 30, True, 50, "2026-12-31"),
            ("LAUNCH", 100, True, 10, "2026-08-01"),
            ("ALBERT10", 10, True, 999, "2026-12-31"),
        ]
        for codigo, desconto, ativo, usos_max, expira in cupons_default:
            cur.execute("""
                INSERT INTO cupons (codigo, desconto_pct, ativo, usos_maximos, usos_atuais, expira_em)
                VALUES (%s, %s, %s, %s, 0, %s)
                ON CONFLICT (codigo) DO NOTHING
            """, (codigo, desconto, ativo, usos_max, expira))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        pass

init_cupons()

@router.post("/validar")
async def validar(request: Request):
    d = await request.json()
    codigo = (d.get("codigo") or "").upper().strip()
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            SELECT codigo, desconto_pct, ativo, usos_maximos, usos_atuais, expira_em 
            FROM cupons WHERE codigo=%s
        """, (codigo,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if not row:
            return JSONResponse({"valido":False,"erro":"Cupom nao encontrado"})
        codigo_db, desconto, ativo, usos_max, usos_atuais, expira = row
        if not ativo:
            return JSONResponse({"valido":False,"erro":"Cupom inativo"})
        if usos_atuais >= usos_max:
            return JSONResponse({"valido":False,"erro":"Cupom esgotado"})
        if expira and expira < datetime.now():
            return JSONResponse({"valido":False,"erro":"Cupom expirado"})
        return JSONResponse({
            "valido":True,
            "codigo":codigo_db,
            "desconto":desconto,
            "tipo":"percentual",
            "descricao":f"{desconto}% de desconto"
        })
    except Exception as e:
        return JSONResponse({"valido":False,"erro":str(e)})

@router.post("/usar")
async def usar(request: Request):
    d = await request.json()
    codigo = (d.get("codigo") or "").upper().strip()
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("UPDATE cupons SET usos_atuais=usos_atuais+1 WHERE codigo=%s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return JSONResponse({"ok":True})
    except Exception as e:
        return JSONResponse({"ok":False,"erro":str(e)})

@router.get("/listar")
async def listar():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT codigo,desconto_pct,ativo,usos_maximos,usos_atuais,expira_em FROM cupons")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return JSONResponse({"cupons":[{"codigo":r[0],"desconto":r[1],"ativo":r[2],"limite":r[3],"usado":r[4],"validade":str(r[5])} for r in rows]})
    except Exception as e:
        return JSONResponse({"cupons":[],"erro":str(e)})

class Plugin(PluginBase):
    name = "cupons_desconto"
    def setup(self, app): app.include_router(router)

plugin = Plugin()
