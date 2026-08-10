"""Monitor de segurança em tempo real com alerta Telegram e bloqueio automático"""
import os
import logging
from datetime import datetime
from fastapi import APIRouter, Request, HTTPException
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
        cur.execute("""
            CREATE TABLE IF NOT EXISTS security_blocks (
                ip VARCHAR(50) PRIMARY KEY,
                motivo TEXT,
                bloqueado_em TIMESTAMP DEFAULT NOW(),
                expira_em TIMESTAMP,
                ativo BOOLEAN DEFAULT TRUE
            )
        """)
        cur.execute("CREATE INDEX IF NOT EXISTS idx_sec_ip ON security_log(ip)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_sec_data ON security_log(criado_em)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_block_expira ON security_blocks(expira_em)")
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        logger.warning(f"Erro init security: {e}")

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
            f"SELECT COUNT(*) FROM security_log WHERE ip=%s AND sucesso=FALSE AND criado_em > NOW() - INTERVAL '{int(minutos)} minutes'",
            (ip,)
        )
        n = cur.fetchone()[0]
        cur.close()
        conn.close()
        return n
    except:
        return 0

def ip_bloqueado(ip: str) -> dict:
    """Retorna info do bloqueio se IP está bloqueado, senão None"""
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "SELECT motivo, expira_em FROM security_blocks WHERE ip=%s AND ativo=TRUE AND expira_em > NOW()",
            (ip,)
        )
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            return {"bloqueado": True, "motivo": row[0], "expira_em": row[1].isoformat()}
        return None
    except:
        return None

def bloquear_ip(ip: str, motivo: str, horas: int = 1):
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            f"""INSERT INTO security_blocks (ip, motivo, expira_em, ativo)
                VALUES (%s, %s, NOW() + INTERVAL '{int(horas)} hours', TRUE)
                ON CONFLICT (ip) DO UPDATE SET
                    motivo = EXCLUDED.motivo,
                    bloqueado_em = NOW(),
                    expira_em = NOW() + INTERVAL '{int(horas)} hours',
                    ativo = TRUE""",
            (ip, motivo)
        )
        conn.commit()
        cur.close()
        conn.close()
        return True
    except Exception as e:
        logger.warning(f"Erro bloquear IP: {e}")
        return False

def desbloquear_ip(ip: str):
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("UPDATE security_blocks SET ativo=FALSE WHERE ip=%s", (ip,))
        conn.commit()
        cur.close()
        conn.close()
        return True
    except:
        return False

async def verificar_e_bloquear(ip: str, email: str = ""):
    """Verifica se deve bloquear e alerta no Telegram"""
    falhas_10min = contar_falhas_recentes(ip, minutos=10)
    falhas_1h = contar_falhas_recentes(ip, minutos=60)
    
    # 30 falhas em 1h = bloqueio de 24h
    if falhas_1h >= 30:
        if bloquear_ip(ip, f"30+ falhas em 1h (email: {email})", horas=24):
            await alertar_telegram(
                f"🛑 IP BLOQUEADO POR 24 HORAS\n\n"
                f"IP: {ip}\n"
                f"Email tentado: {email}\n"
                f"Falhas em 1h: {falhas_1h}\n\n"
                f"Ataque persistente detectado!"
            )
        return True
    
    # 10 falhas em 10min = bloqueio de 1h
    if falhas_10min >= 10:
        if bloquear_ip(ip, f"10+ falhas em 10min (email: {email})", horas=1):
            await alertar_telegram(
                f"🛑 IP BLOQUEADO POR 1 HORA\n\n"
                f"IP: {ip}\n"
                f"Email tentado: {email}\n"
                f"Falhas em 10min: {falhas_10min}\n\n"
                f"Força bruta detectada!"
            )
        return True
    
    # 5 falhas = só alerta
    if falhas_10min >= 5:
        await alertar_telegram(
            f"⚠️ ALERTA DE SEGURANÇA\n\n"
            f"IP: {ip}\n"
            f"Email tentado: {email}\n"
            f"Falhas em 10min: {falhas_10min}\n\n"
            f"Próximas 5 falhas = bloqueio automático!"
        )
    
    return False

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
        cur.execute("SELECT ip, motivo, bloqueado_em, expira_em FROM security_blocks WHERE ativo=TRUE AND expira_em > NOW() ORDER BY bloqueado_em DESC")
        ips_bloqueados = [
            {"ip": r[0], "motivo": r[1], "bloqueado_em": r[2].isoformat(), "expira_em": r[3].isoformat()}
            for r in cur.fetchall()
        ]
        cur.close()
        conn.close()
        return {
            "falhas_24h": falhas_24h,
            "ips_suspeitos": ips_suspeitos,
            "ips_bloqueados": ips_bloqueados,
            "eventos_recentes": eventos
        }
    except Exception as e:
        return {"erro": str(e)}

@router.post("/desbloquear/{ip}")
async def desbloquear(ip: str):
    if desbloquear_ip(ip):
        return {"status": "ok", "ip_desbloqueado": ip}
    return {"status": "erro"}

class SecurityMonitorPlugin(PluginBase):
    name = "security_monitor"
    def setup(self, app):
        app.include_router(router)

plugin = SecurityMonitorPlugin()
