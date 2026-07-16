"""
Logger estruturado — Emotion Platform v21.0
Uso: from modules.logger import log
"""
import sys
from loguru import logger
from pathlib import Path

LOG_DIR = Path(__file__).parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

# Remove logger padrão
logger.remove()

# Console — colorido e legível
logger.add(
    sys.stdout,
    format="<green>{time:DD/MM HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan> — <level>{message}</level>",
    level="INFO",
    colorize=True
)

# Arquivo rotativo — JSON estruturado
logger.add(
    LOG_DIR / "app_{time:YYYY-MM-DD}.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name} | {message} | {extra}",
    level="DEBUG",
    rotation="00:00",
    retention="7 days",
    compression="zip",
    serialize=False
)

# Arquivo de erros separado
logger.add(
    LOG_DIR / "errors.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{line} | {message}",
    level="ERROR",
    rotation="10 MB",
    retention="30 days"
)

log = logger

def log_request(method: str, path: str, status: int, duration_ms: float, usuario_id: int = None):
    log.bind(
        method=method,
        path=path,
        status=status,
        duration_ms=duration_ms,
        usuario_id=usuario_id
    ).info(f"{method} {path} → {status} ({duration_ms:.1f}ms)")

def log_emocao(usuario_id: int, emocao: str, intensidade: int, fonte: str):
    log.bind(
        usuario_id=usuario_id,
        emocao=emocao,
        intensidade=intensidade,
        fonte=fonte
    ).info(f"Emoção detectada: {emocao} (intensidade {intensidade}) via {fonte}")

def log_erro(contexto: str, erro: Exception, usuario_id: int = None):
    log.bind(
        contexto=contexto,
        usuario_id=usuario_id,
        tipo_erro=type(erro).__name__
    ).error(f"Erro em {contexto}: {erro}")

def log_ia(modelo: str, tokens: int, duracao_ms: float, sucesso: bool):
    log.bind(
        modelo=modelo,
        tokens=tokens,
        duracao_ms=duracao_ms,
        sucesso=sucesso
    ).info(f"IA {modelo}: {tokens} tokens em {duracao_ms:.0f}ms")

def log_pagamento(usuario_id: int, valor: float, plano: str, status: str):
    log.bind(
        usuario_id=usuario_id,
        valor=valor,
        plano=plano,
        status=status
    ).info(f"Pagamento {status}: R${valor} → {plano}")
