"""
Plugin: P6 PostHog+Amplitude
Categoria: analytics
Extraido automaticamente do main.py
"""
VERSAO = "1.0"
NOME = "posthog"
DESCRICAO = "P6 PostHog+Amplitude"
CATEGORIA = "analytics"

# ═══════════════════════════════════════════════════════════════════════
# SISTEMA P6 — POSTHOG + AMPLITUDE + HOTJAR (Analytics)
# ═══════════════════════════════════════════════════════════════════════

POSTHOG_API_KEY = _os_s10.getenv("POSTHOG_API_KEY", "")
AMPLITUDE_API_KEY = _os_s10.getenv("AMPLITUDE_API_KEY", "")
HOTJAR_ID = _os_s10.getenv("HOTJAR_ID", "")

_eventos_analytics: list = []
_usuarios_analytics: dict = {}
_funil_conversao: dict = {}
_sessoes_analytics: dict = {}

# ── P6.1 PostHog
async def posthog_capturar_evento(
    usuario_id: int,
    evento: str,
    propriedades: dict = None
):
    _eventos_analytics.append({
        "usuario_id": usuario_id,
        "evento": evento,
        "props": propriedades or {},
        "ts": _datetime_s7.now().isoformat(),
        "fonte": "posthog"
    })
    if not POSTHOG_API_KEY:
        return
    try:
        import httpx
        async with httpx.AsyncClient(timeout=5) as client:
            await client.post(
                "https://app.posthog.com/capture/",
                json={
                    "api_key": POSTHOG_API_KEY,
                    "event": evento,
                    "distinct_id": str(usuario_id),
                    "properties": propriedades or {}
                }
            )
    except Exception:
        pass

async def posthog_identificar_usuario(usuario_id: int, propriedades: dict):
    if not POSTHOG_API_KEY:
        return
    try:
        import httpx
        async with httpx.AsyncClient(timeout=5) as client:
            await client.post(
                "https://app.posthog.com/capture/",
                json={
                    "api_key": POSTHOG_API_KEY,
                    "event": "$identify",
                    "distinct_id": str(usuario_id),
                    "properties": {"$set": propriedades}
                }
            )
    except Exception:
        pass

# ── P6.2 Amplitude
async def amplitude_track(usuario_id: int, evento: str, props: dict = None):
    _eventos_analytics.append({
        "usuario_id": usuario_id,
        "evento": evento,
        "props": props or {},
        "ts": _datetime_s7.now().isoformat(),
        "fonte": "amplitude"
    })
    if not AMPLITUDE_API_KEY:
        return
    try:
        import httpx
        async with httpx.AsyncClient(timeout=5) as client:
            await client.post(
                "https://api2.amplitude.com/2/httpapi",
                json={
                    "api_key": AMPLITUDE_API_KEY,
                    "events": [{
                        "user_id": str(usuario_id),
                        "event_type": evento,
                        "event_properties": props or {},
                        "time": int(_datetime_s7.now().timestamp() * 1000)
                    }]
                }
            )
    except Exception:
        pass

# ── P6.3 Analytics próprio (sem dependência externa)
def registrar_evento_analytics(
    usuario_id: int,
    evento: str,
    props: dict = None,
    sessao_id: str = None
):
    entrada = {
        "usuario_id": usuario_id,
        "evento": evento,
        "props": props or {},
        "sessao_id": sessao_id,
        "ts": _datetime_s7.now().isoformat()
    }
    _eventos_analytics.append(entrada)
    if len(_eventos_analytics) > 5000:
        _eventos_analytics.pop(0)
    if usuario_id not in _usuarios_analytics:
        _usuarios_analytics[usuario_id] = {
            "primeiro_evento": entrada["ts"],
            "total_eventos": 0,
            "eventos": []
        }
    _usuarios_analytics[usuario_id]["total_eventos"] += 1
    _usuarios_analytics[usuario_id]["ultimo_evento"] = entrada["ts"]

def registrar_etapa_funil(usuario_id: int, funil: str, etapa: str):
    chave = f"{funil}:{usuario_id}"
    if chave not in _funil_conversao:
        _funil_conversao[chave] = {
            "usuario_id": usuario_id,
            "funil": funil,
            "etapas": [],
            "iniciado_em": _datetime_s7.now().isoformat()
        }
    _funil_conversao[chave]["etapas"].append({
        "etapa": etapa,
        "ts": _datetime_s7.now().isoformat()
    })

def analisar_funil(funil: str) -> dict:
    entradas = {k: v for k, v in _funil_conversao.items() if funil in k}
    if not entradas:
        return {"funil": funil, "dados": {}}
    etapas_contagem = {}
    for dados in entradas.values():
        for etapa_data in dados["etapas"]:
            etapa = etapa_data["etapa"]
            etapas_contagem[etapa] = etapas_contagem.get(etapa, 0) + 1
    total_inicio = max(etapas_contagem.values()) if etapas_contagem else 1
    return {
        "funil": funil,
        "total_usuarios": len(entradas),
        "etapas": {
            etapa: {
                "usuarios": count,
                "taxa_pct": round(count/total_inicio*100, 1)
            }
            for etapa, count in sorted(etapas_contagem.items())
        }
    }

def stats_analytics_completo() -> dict:
    total_eventos = len(_eventos_analytics)
    usuarios_unicos = len(_usuarios_analytics)
    eventos_por_tipo = {}
    for ev in _eventos_analytics:
        tipo = ev.get("evento", "unknown")
        eventos_por_tipo[tipo] = eventos_por_tipo.get(tipo, 0) + 1
    top_eventos = sorted(eventos_por_tipo.items(), key=lambda x: x[1], reverse=True)[:10]
    return {
        "total_eventos": total_eventos,
        "usuarios_unicos": usuarios_unicos,
        "top_eventos": top_eventos,
        "posthog_ativo": bool(POSTHOG_API_KEY),
        "amplitude_ativo": bool(AMPLITUDE_API_KEY),
        "hotjar_id": HOTJAR_ID or "nao_configurado",
    }

@app.post("/api/analytics/evento")
async def analytics_evento_ep(request: Request, db=Depends(get_db)):
    try:
        usuario = await verificar_token(request, db)
        usuario_id = usuario.get("id", 0) if usuario else 0
        body = await request.json()
        evento = body.get("evento", "")
        props = body.get("props", {})
        if evento:
            registrar_evento_analytics(usuario_id, evento, props)
            await posthog_capturar_evento(usuario_id, evento, props)
        return JSONResponse({"ok": True})
    except Exception:
        return JSONResponse({"ok": False})

@app.get("/api/admin/analytics")
async def admin_analytics_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario or usuario.get("plano") != "admin":
        return JSONResponse({"erro": "Nao autorizado"}, status_code=403)
    return JSONResponse({
        "stats": stats_analytics_completo(),
        "funil_cadastro": analisar_funil("cadastro"),
        "funil_premium": analisar_funil("premium"),
        "sistema": "P6 Analytics"
    })


