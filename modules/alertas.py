"""
Alertas Inteligentes — Emotion Platform v21.0
Detecta anomalias e notifica automaticamente
"""
import os
import urllib.request
import urllib.parse
from datetime import datetime
from collections import deque
from typing import List, Dict

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "8909749074:AAGNoB-JPZVC0Vl1dYeiN__1ktxza6GZ0s4")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "7757404855")

historico_erros: deque = deque(maxlen=100)
historico_requests: deque = deque(maxlen=1000)
alertas_enviados: Dict[str, datetime] = {}

COOLDOWN_MINUTOS = 30

def pode_alertar(tipo: str) -> bool:
    if tipo not in alertas_enviados:
        return True
    delta = (datetime.now() - alertas_enviados[tipo]).total_seconds() / 60
    return delta >= COOLDOWN_MINUTOS

def registrar_erro(rota: str, erro: str, status_code: int):
    historico_erros.append({
        "rota": rota,
        "erro": erro[:200],
        "status": status_code,
        "ts": datetime.now()
    })
    erros_recentes = [
        e for e in historico_erros
        if (datetime.now() - e["ts"]).total_seconds() < 300
    ]
    if len(erros_recentes) >= 5 and pode_alertar("erros_frequentes"):
        alertas_enviados["erros_frequentes"] = datetime.now()
        _notify(
            f"🚨 *Muitos erros detectados*\n"
            f"{len(erros_recentes)} erros nos últimos 5 minutos\n"
            f"Último: `{rota}` → {status_code}\n"
            f"⏰ {datetime.now().strftime('%d/%m %H:%M')}"
        )

def alerta_novo_usuario(nome: str, email: str, total: int):
    _notify(
        f"🎉 *Novo usuário cadastrado!*\n"
        f"Nome: {nome}\n"
        f"Total: {total} usuários\n"
        f"⏰ {datetime.now().strftime('%d/%m %H:%M')}"
    )

def alerta_pagamento(valor: float, plano: str, usuario: str):
    _notify(
        f"💰 *Pagamento aprovado!*\n"
        f"Usuário: {usuario}\n"
        f"Plano: {plano}\n"
        f"Valor: R${valor:.2f}\n"
        f"⏰ {datetime.now().strftime('%d/%m %H:%M')}"
    )

def alerta_crise(usuario_id: int, texto: str):
    _notify(
        f"🆘 *CRISE DETECTADA*\n"
        f"Usuário ID: {usuario_id}\n"
        f"Texto: _{texto[:100]}_\n"
        f"⏰ {datetime.now().strftime('%d/%m %H:%M')}"
    )

def _notify(msg: str):
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
