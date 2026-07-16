"""
Plugin: P2 Sentry+Prometheus
Categoria: sistemas
Extraido automaticamente do main.py
"""
VERSAO = "1.0"
NOME = "monitoring"
DESCRICAO = "P2 Sentry+Prometheus"
CATEGORIA = "sistemas"

# ═══════════════════════════════════════════════════════════════════════
# SISTEMA P2 — SENTRY + PROMETHEUS + LOGURU
# ═══════════════════════════════════════════════════════════════════════

# ── P2.1 Sentry Error Tracking
SENTRY_DSN = _os_s10.getenv("SENTRY_DSN", "")
_sentry_inicializado = False

def inicializar_sentry():
    global _sentry_inicializado
    if not SENTRY_DSN or _sentry_inicializado:
        return
    try:
        import sentry_sdk
        from sentry_sdk.integrations.fastapi import FastApiIntegration
        from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
        sentry_sdk.init(
            dsn=SENTRY_DSN,
            integrations=[FastApiIntegration(), SqlalchemyIntegration()],
            traces_sample_rate=0.1,
            profiles_sample_rate=0.1,
            environment=_os_s10.getenv("ENVIRONMENT", "production"),
            release="21.0",
            send_default_pii=False,
        )
        _sentry_inicializado = True
        print("✅ Sentry inicializado")
    except ImportError:
        print("⚠️  sentry-sdk nao instalado")
    except Exception as e:
        print(f"⚠️  Sentry erro: {e}")

def capturar_erro_sentry(erro: Exception, contexto: dict = None):
    if not _sentry_inicializado:
        return
    try:
        import sentry_sdk
        with sentry_sdk.push_scope() as scope:
            if contexto:
                for k, v in contexto.items():
                    scope.set_extra(k, v)
            sentry_sdk.capture_exception(erro)
    except Exception:
        pass

def capturar_mensagem_sentry(mensagem: str, nivel: str = "info", dados: dict = None):
    if not _sentry_inicializado:
        return
    try:
        import sentry_sdk
        sentry_sdk.capture_message(mensagem, level=nivel, extras=dados or {})
    except Exception:
        pass

# Inicializar no startup
inicializar_sentry()

# ── P2.2 Prometheus Metrics
_prometheus_disponivel = False
try:
    from prometheus_client import Counter as _PCounter
    from prometheus_client import Histogram as _PHistogram
    from prometheus_client import Gauge as _PGauge
    from prometheus_client import generate_latest as _prom_generate
    from prometheus_client import CONTENT_TYPE_LATEST as _PROM_CONTENT_TYPE

    _prom_requests = _PCounter(
        "emotion_requests_total",
        "Total de requisicoes",
        ["method", "endpoint", "status"]
    )
    _prom_duration = _PHistogram(
        "emotion_request_duration_seconds",
        "Duracao das requisicoes",
        ["endpoint"]
    )
    _prom_usuarios_ativos = _PGauge(
        "emotion_usuarios_ativos",
        "Usuarios ativos"
    )
    _prom_analises = _PCounter(
        "emotion_analises_total",
        "Total de analises emocionais",
        ["emocao"]
    )
    _prom_erros_ia = _PCounter(
        "emotion_ia_erros_total",
        "Erros de IA",
        ["modelo"]
    )
    _prometheus_disponivel = True
except ImportError:
    pass

def registrar_metrica_request(method: str, endpoint: str, status: int, duration: float):
    if not _prometheus_disponivel:
        return
    try:
        _prom_requests.labels(method=method, endpoint=endpoint, status=str(status)).inc()
        _prom_duration.labels(endpoint=endpoint).observe(duration)
    except Exception:
        pass

def registrar_metrica_analise(emocao: str):
    if not _prometheus_disponivel:
        return
    try:
        _prom_analises.labels(emocao=emocao).inc()
    except Exception:
        pass

def registrar_metrica_erro_ia(modelo: str):
    if not _prometheus_disponivel:
        return
    try:
        _prom_erros_ia.labels(modelo=modelo).inc()
    except Exception:
        pass

@app.get("/metrics")
async def prometheus_metrics(request: Request):
    ip = request.client.host if request.client else "unknown"
    if ip not in _whitelist_ips_s3 and not ip.startswith("127."):
        return JSONResponse({"erro": "Nao autorizado"}, status_code=403)
    if not _prometheus_disponivel:
        return JSONResponse({"erro": "Prometheus nao disponivel"}, status_code=503)
    from fastapi.responses import Response
    return Response(
        content=_prom_generate(),
        media_type=_PROM_CONTENT_TYPE
    )

# ── P2.3 Loguru estruturado
_loguru_disponivel = False
try:
    from loguru import logger as _loguru
    _loguru.add(
        "logs/app_{time:YYYY-MM-DD}.log",
        rotation="00:00",
        retention="7 days",
        level="INFO",
        format="{time:DD/MM HH:mm:ss} | {level} | {message}"
    )
    _loguru_disponivel = True
except ImportError:
    pass

def log_estruturado(nivel: str, msg: str, **kwargs):
    if _loguru_disponivel:
        getattr(_loguru, nivel.lower(), _loguru.info)(msg, **kwargs)
    else:
        print(f"[{nivel}] {msg} {kwargs}")

@app.get("/api/admin/health-detalhado")
async def health_detalhado_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario or usuario.get("plano") != "admin":
        return JSONResponse({"erro": "Nao autorizado"}, status_code=403)
    return JSONResponse({
        "sentry": {"ativo": _sentry_inicializado, "dsn_configurado": bool(SENTRY_DSN)},
        "prometheus": {"ativo": _prometheus_disponivel},
        "loguru": {"ativo": _loguru_disponivel},
        "sistema": "P2 — Monitoramento completo"
    })


