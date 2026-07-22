"""Plugin: Rate Limit — bloqueio após 5 tentativas falhas — Supabase"""
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import time, os, psycopg2

router = APIRouter(prefix="/api/v1/rate-limit", tags=["seguranca"])
DATABASE_URL = os.getenv("DATABASE_URL", "")
MAX_TENTATIVAS = 5
BLOQUEAR_MINUTOS = 15

def get_conn():
    url = DATABASE_URL.replace("postgres://", "postgresql://")
    return psycopg2.connect(url, sslmode="require", connect_timeout=10)

def init_table():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS rate_limit (
                ip VARCHAR(50) PRIMARY KEY,
                tentativas INTEGER DEFAULT 0,
                bloqueado_ate TIMESTAMP,
                atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        cur.close()
        conn.close()
    except: pass

init_table()

def verificar_rate_limit(ip: str) -> bool:
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT tentativas, bloqueado_ate FROM rate_limit WHERE ip=%s", (ip,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            tentativas, bloqueado_ate = row
            if bloqueado_ate and bloqueado_ate > datetime.utcnow():
                return True
            if tentativas >= MAX_TENTATIVAS:
                return True
        return False
    except: return False

def registrar_falha(ip: str):
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO rate_limit (ip, tentativas, bloqueado_ate)
            VALUES (%s, 1, NULL)
            ON CONFLICT (ip) DO UPDATE
            SET tentativas = rate_limit.tentativas + 1,
                bloqueado_ate = CASE
                    WHEN rate_limit.tentativas + 1 >= %s
                    THEN NOW() + INTERVAL '%s minutes'
                    ELSE NULL
                END,
                atualizado_em = NOW()
        """, (ip, MAX_TENTATIVAS, BLOQUEAR_MINUTOS))
        conn.commit()
        cur.close()
        conn.close()
    except: pass

def limpar_ip(ip: str):
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("DELETE FROM rate_limit WHERE ip=%s", (ip,))
        conn.commit()
        cur.close()
        conn.close()
    except: pass

@router.get("/status")
async def status():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM rate_limit")
        total = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM rate_limit WHERE bloqueado_ate > NOW()")
        bloqueados = cur.fetchone()[0]
        cur.close()
        conn.close()
        return {"plugin":"rate_limit","max_tentativas":MAX_TENTATIVAS,"bloquear_minutos":BLOQUEAR_MINUTOS,"ips_monitorados":total,"ips_bloqueados":bloqueados}
    except Exception as e:
        return {"plugin":"rate_limit","erro":str(e)}

@router.get("/listar")
async def listar():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT ip,tentativas,bloqueado_ate FROM rate_limit ORDER BY atualizado_em DESC LIMIT 50")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return {"items":[{"ip":r[0],"tentativas":r[1],"bloqueado":r[2] and r[2] > datetime.utcnow()} for r in rows]}
    except Exception as e:
        return {"items":[],"erro":str(e)}

@router.post("/criar")
async def criar(request: Request):
    return JSONResponse({"ok":True})

class RateLimitPlugin(PluginBase):
    name = "rate_limit"
    version = "3.0.0"
    description = "Rate limiting com Supabase — persiste restarts"
    category = "seguranca"

    def setup(self, app):
        app.include_router(router)
        from starlette.middleware.base import BaseHTTPMiddleware
        from fastapi import Request as FastRequest
        from fastapi.responses import JSONResponse as FastJSON

        class RateLimitMiddleware(BaseHTTPMiddleware):
            async def dispatch(self, request: FastRequest, call_next):
                if "/auth/login" in request.url.path or "/auth/cadastrar" in request.url.path:
                    ip = request.client.host if request.client else "unknown"
                    if verificar_rate_limit(ip):
                        return FastJSON(
                            {"detail":f"Muitas tentativas. Tente em {BLOQUEAR_MINUTOS} minutos."},
                            status_code=429
                        )
                response = await call_next(request)
                if response.status_code == 401 and "/auth/login" in request.url.path:
                    ip = request.client.host if request.client else "unknown"
                    registrar_falha(ip)
                elif response.status_code == 200 and "/auth/login" in request.url.path:
                    ip = request.client.host if request.client else "unknown"
                    limpar_ip(ip)
                return response

        app.add_middleware(RateLimitMiddleware)

    def health_check(self):
        return {"status":"healthy","plugin":"rate_limit","storage":"supabase"}

plugin = RateLimitPlugin()
