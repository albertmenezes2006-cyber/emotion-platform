"""Monitor de segurança em tempo real com alerta Telegram"""
import os
import logging
from datetime import datetime
from fastapi import APIRouter, Request
from plugins.plugin_base import PluginBase
import psycopg2
import httpx

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/security", tags=["Security"])

def get_db():
    return psycopg2.connect(os.getenv("DATABASE_URL"))

def init_tabela():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS security_log (
                id SERIAL PRIMARY KEY,
                tipo VARCHAR(50),
                ip VARCHAR(50),
                email VARCHAR(200),
                sucesso BOOLEAN,
                detalhes TEXT,
                user_agent TEXT,
                criado_em TIMESTAMP DEFAULT NOW()
            )
        """)
        cur.execute("CREATE INDEX IF NOT EXISTS idx_sec_ip ON security_log(ip)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_sec_data ON security_log(criado_em)")
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        logger.warning(f"Erro init security_log: {e}")

init_tabela()

async def alertar_telegram(msg: str):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        return
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            await client.post(
                f"https://api.telegram.org/bot{token}/sendMessage",
                json={"chat_id": chat_id, "text": msg}
            )
    except Exception as e:
        logger.warning(f"Erro Telegram: {e}")

def registrar_evento(tipo: str, ip: str, email: str = "", sucesso: bool = True, detalhes: str = "", user_agent: str = ""):
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO security_log (tipo, ip, email, sucesso, detalhes, user_agent) VALUES (%s,%s,%s,%s,%s,%s)",
            (tipo, ip, email, sucesso, detalhes, user_agent)
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        logger.warning(f"Erro registrar: {e}")

def contar_falhas_recentes(ip: str, minutos: int = 10) -> int:
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "SELECT COUNT(*) FROM security_log WHERE ip=%s AND sucesso=FALSE AND criado_em > NOW() - INTERVAL '%s minutes'",
            (ip, minutos)
        )
        n = cur.fetchone()[0]
        cur.close()
        conn.close()
        return n
    except:
        return 0

@router.get("/dashboard")
async def dashboard(limite: int = 50):
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "SELECT tipo, ip, email, sucesso, detalhes, criado_em FROM security_log ORDER BY criado_em DESC LIMIT %s",
            (limite,)
        )
        rows = cur.fetchall()
        eventos = [
            {
                "tipo": r[0], "ip": r[1], "email": r[2],
                "sucesso": r[3], "detalhes": r[4],
                "quando": r[5].isoformat() if r[5] else None
            } for r in rows
        ]
        cur.execute("SELECT COUNT(*) FROM security_log WHERE sucesso=FALSE AND criado_em > NOW() - INTERVAL '24 hours'")
        falhas_24h = cur.fetchone()[0]
        cur.execute("SELECT ip, COUNT(*) as n FROM security_log WHERE sucesso=FALSE AND criado_em > NOW() - INTERVAL '24 hours' GROUP BY ip ORDER BY n DESC LIMIT 10")
        ips_suspeitos = [{"ip": r[0], "falhas": r[1]} for r in cur.fetchall()]
        cur.close()
        conn.close()
        return {
            "falhas_24h": falhas_24h,
            "ips_suspeitos": ips_suspeitos,
            "eventos_recentes": eventos
        }
    except Exception as e:
        return {"erro": str(e)}

@router.post("/registrar")
async def registrar(request: Request):
    """Endpoint interno para outros plugins registrarem eventos"""
    data = await request.json()
    tipo = data.get("tipo", "unknown")
    ip = request.client.host if request.client else "unknown"
    email = data.get("email", "")
    sucesso = data.get("sucesso", True)
    detalhes = data.get("detalhes", "")
    ua = request.headers.get("user-agent", "")
    
    registrar_evento(tipo, ip, email, sucesso, detalhes, ua)
    
    # Se falha, checa se tem muitas
    if not sucesso:
        n = contar_falhas_recentes(ip, minutos=10)
        if n >= 5:
            await alertar_telegram(
                f"🚨 ALERTA DE SEGURANÇA\n\n"
                f"IP: {ip}\n"
                f"Tipo: {tipo}\n"
                f"Email tentado: {email}\n"
                f"Falhas em 10min: {n}\n\n"
                f"Possível ataque de força bruta!"
            )
    
    return {"status": "registrado"}

class SecurityMonitorPlugin(PluginBase):
    name = "security_monitor"
    def setup(self, app):
        app.include_router(router)

plugin = SecurityMonitorPlugin()
