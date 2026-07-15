"""
Sistema de Saúde — Emotion Platform v21.0
Monitora e alerta sobre problemas automaticamente
"""
import os
import psutil
import urllib.request
import urllib.parse
import json
from datetime import datetime
from typing import List, Dict

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "8909749074:AAGNoB-JPZVC0Vl1dYeiN__1ktxza6GZ0s4")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "7757404855")

LIMITES = {
    "cpu_pct_max": 85.0,
    "memoria_mb_max": 450.0,
    "taxa_erro_max": 5.0,
    "tempo_resposta_ms_max": 3000.0,
    "uptime_min_horas": 0.0
}

def verificar_saude_sistema() -> Dict:
    alertas = []
    status = "saudavel"

    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory()
    disco = psutil.disk_usage("/")

    if cpu > LIMITES["cpu_pct_max"]:
        alertas.append(f"⚠️ CPU alta: {cpu}%")
        status = "degradado"

    mem_uso_pct = mem.percent
    if mem_uso_pct > 90:
        alertas.append(f"⚠️ Memória crítica: {mem_uso_pct}%")
        status = "critico"
    elif mem_uso_pct > 75:
        alertas.append(f"⚠️ Memória alta: {mem_uso_pct}%")
        status = "degradado"

    disco_pct = disco.percent
    if disco_pct > 90:
        alertas.append(f"⚠️ Disco crítico: {disco_pct}%")
        status = "critico"

    return {
        "status": status,
        "alertas": alertas,
        "sistema": {
            "cpu_pct": cpu,
            "memoria_pct": mem_uso_pct,
            "memoria_disponivel_mb": round(mem.available / 1024 / 1024, 1),
            "disco_pct": disco_pct,
            "disco_livre_gb": round(disco.free / 1024**3, 2)
        },
        "verificado_em": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

def notificar_telegram(msg: str):
    try:
        data = urllib.parse.urlencode({
            "chat_id": TELEGRAM_CHAT_ID,
            "text": msg,
            "parse_mode": "Markdown"
        }).encode()
        urllib.request.urlopen(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            data=data, timeout=5
        )
    except Exception:
        pass

def verificar_e_alertar():
    saude = verificar_saude_sistema()
    if saude["alertas"] and saude["status"] in ("degradado", "critico"):
        emoji = "🔴" if saude["status"] == "critico" else "🟡"
        msg = (
            f"{emoji} *Sistema {saude['status'].upper()}*\n"
            + "\n".join(saude["alertas"])
            + f"\n⏰ {saude['verificado_em']}"
        )
        notificar_telegram(msg)
    return saude
