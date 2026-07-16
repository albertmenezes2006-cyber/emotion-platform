"""
Plugin: P7 Redis+CQRS+Cache
Categoria: performance
Extraido automaticamente do main.py
"""
VERSAO = "1.0"
NOME = "cache"
DESCRICAO = "P7 Redis+CQRS+Cache"
CATEGORIA = "performance"

# ═══════════════════════════════════════════════════════════════════════
# SISTEMA P7 — CELERY + REDIS AVANÇADO + CQRS
# ═══════════════════════════════════════════════════════════════════════

REDIS_URL = _os_s10.getenv("REDIS_URL", "redis://localhost:6379/0")
_celery_disponivel = False
_redis_disponivel = False

try:
    import redis as _redis_lib
    _redis_client = _redis_lib.from_url(REDIS_URL, decode_responses=True, socket_timeout=2)
    _redis_client.ping()
    _redis_disponivel = True
    print("✅ Redis conectado")
except Exception:
    _redis_client = None

try:
    from celery import Celery as _Celery
    _celery_app = _Celery("emotion_platform", broker=REDIS_URL, backend=REDIS_URL)
    _celery_app.conf.update(
        task_serializer="json",
        accept_content=["json"],
        result_serializer="json",
        timezone="America/Sao_Paulo",
        enable_utc=True,
        task_track_started=True,
        task_acks_late=True,
        worker_prefetch_multiplier=1,
    )
    _celery_disponivel = True
except ImportError:
    _celery_app = None

# ── P7.1 Cache com Redis (com fallback em memória)
_cache_memoria: dict = {}

def cache_set(chave: str, valor, ttl_segundos: int = 300):
    import json
    if _redis_disponivel and _redis_client:
        try:
            _redis_client.setex(chave, ttl_segundos, json.dumps(valor, default=str))
            return
        except Exception:
            pass
    _cache_memoria[chave] = {
        "valor": valor,
        "expira": _time_sec.time() + ttl_segundos
    }

def cache_get(chave: str):
    import json
    if _redis_disponivel and _redis_client:
        try:
            val = _redis_client.get(chave)
            return json.loads(val) if val else None
        except Exception:
            pass
    entrada = _cache_memoria.get(chave)
    if not entrada:
        return None
    if _time_sec.time() > entrada["expira"]:
        del _cache_memoria[chave]
        return None
    return entrada["valor"]

def cache_delete(chave: str):
    if _redis_disponivel and _redis_client:
        try:
            _redis_client.delete(chave)
        except Exception:
            pass
    _cache_memoria.pop(chave, None)

def cache_invalidar_usuario(usuario_id: int):
    prefixos = [f"usuario:{usuario_id}", f"dashboard:{usuario_id}", f"score:{usuario_id}"]
    for prefixo in prefixos:
        cache_delete(prefixo)

# ── P7.2 Filas de tarefas (sem Celery — usando asyncio)
_fila_tarefas: list = []
_tarefas_em_execucao: dict = {}
_historico_tarefas: list = []

async def adicionar_tarefa_fila(tipo: str, dados: dict, prioridade: int = 5) -> str:
    import secrets
    task_id = secrets.token_hex(8)
    _fila_tarefas.append({
        "id": task_id,
        "tipo": tipo,
        "dados": dados,
        "prioridade": prioridade,
        "criado_em": _datetime_s7.now().isoformat(),
        "status": "pendente"
    })
    _fila_tarefas.sort(key=lambda x: x["prioridade"])
    return task_id

async def processar_proxima_tarefa():
    if not _fila_tarefas:
        return None
    tarefa = _fila_tarefas.pop(0)
    task_id = tarefa["id"]
    _tarefas_em_execucao[task_id] = tarefa
    tarefa["status"] = "executando"
    tarefa["iniciado_em"] = _datetime_s7.now().isoformat()
    try:
        tipo = tarefa["tipo"]
        if tipo == "enviar_email":
            pass
        elif tipo == "gerar_relatorio":
            pass
        elif tipo == "analisar_lote":
            pass
        tarefa["status"] = "concluido"
        tarefa["concluido_em"] = _datetime_s7.now().isoformat()
    except Exception as e:
        tarefa["status"] = "erro"
        tarefa["erro"] = str(e)
    finally:
        _historico_tarefas.append(tarefa)
        _tarefas_em_execucao.pop(task_id, None)
    return tarefa

# ── P7.3 CQRS básico
_comandos_log: list = []
_queries_log: list = []

def registrar_comando_cqrs(tipo: str, dados: dict, usuario_id: int = None):
    _comandos_log.append({
        "tipo": tipo,
        "dados": zerar_dados_sensiveis_s10(dados),
        "usuario_id": usuario_id,
        "ts": _datetime_s7.now().isoformat()
    })
    if len(_comandos_log) > 1000:
        _comandos_log.pop(0)

def registrar_query_cqrs(tipo: str, resultado_count: int, duracao_ms: float):
    _queries_log.append({
        "tipo": tipo,
        "resultado_count": resultado_count,
        "duracao_ms": duracao_ms,
        "ts": _datetime_s7.now().isoformat()
    })
    if len(_queries_log) > 1000:
        _queries_log.pop(0)

def stats_cqrs() -> dict:
    return {
        "total_comandos": len(_comandos_log),
        "total_queries": len(_queries_log),
        "tarefas_fila": len(_fila_tarefas),
        "tarefas_executando": len(_tarefas_em_execucao),
        "tarefas_historico": len(_historico_tarefas),
        "cache_redis": _redis_disponivel,
        "celery_disponivel": _celery_disponivel
    }

@app.get("/api/admin/performance")
async def admin_performance_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario or usuario.get("plano") != "admin":
        return JSONResponse({"erro": "Nao autorizado"}, status_code=403)
    return JSONResponse({
        "cache": {"redis": _redis_disponivel, "memoria": len(_cache_memoria)},
        "filas": stats_cqrs(),
        "sistema": "P7 Performance"
    })

@app.post("/api/cache/invalidar")
async def invalidar_cache_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario:
        return JSONResponse({"erro": "Nao autorizado"}, status_code=401)
    cache_invalidar_usuario(usuario.get("id"))
    return JSONResponse({"ok": True, "msg": "Cache invalidado"})


