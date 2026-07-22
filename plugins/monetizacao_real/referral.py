from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import os, uuid, psycopg2, hashlib

router = APIRouter(prefix="/api/v1/referral", tags=["Referral"])
DATABASE_URL = os.getenv("DATABASE_URL", "")

def get_conn():
    url = DATABASE_URL.replace("postgres://", "postgresql://")
    return psycopg2.connect(url, sslmode="require", connect_timeout=10)

def init_table():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS referrals (
                codigo VARCHAR(20) PRIMARY KEY,
                email VARCHAR(200),
                indicacoes INTEGER DEFAULT 0,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        cur.close()
        conn.close()
    except: pass

init_table()

def gerar_codigo(email):
    return hashlib.md5(email.encode()).hexdigest()[:8].upper()

@router.get("/gerar/{email}")
async def gerar_referral(email: str):
    codigo = gerar_codigo(email)
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("INSERT INTO referrals (codigo,email) VALUES (%s,%s) ON CONFLICT (codigo) DO NOTHING", (codigo, email))
        conn.commit()
        cur.execute("SELECT indicacoes FROM referrals WHERE codigo=%s", (codigo,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        indicacoes = row[0] if row else 0
        url = f"https://emotion-platform-albert.onrender.com/?ref={codigo}"
        return JSONResponse({"codigo":codigo,"url":url,"indicacoes":indicacoes,"beneficio":"30 dias gratis por indicacao","whatsapp":f"https://wa.me/?text=Use meu codigo {codigo} no Emotion Platform e ganhe 30 dias gratis: {url}"})
    except Exception as e:
        return JSONResponse({"erro":str(e)}, status_code=500)

@router.get("/usar/{codigo}")
async def usar_referral(codigo: str):
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("UPDATE referrals SET indicacoes=indicacoes+1 WHERE codigo=%s", (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return JSONResponse({"ok":True,"desconto":"30 dias gratis aplicado"})
    except: return JSONResponse({"erro":"Codigo invalido"}, status_code=404)

@router.get("/stats")
async def stats_referral():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*),SUM(indicacoes) FROM referrals")
        row = cur.fetchone()
        cur.close()
        conn.close()
        return JSONResponse({"total_codigos":row[0] or 0,"total_indicacoes":row[1] or 0})
    except: return JSONResponse({"total_codigos":0,"total_indicacoes":0})

class Plugin(PluginBase):
    name = "referral_system"
    def setup(self, app): app.include_router(router)

plugin = Plugin()
