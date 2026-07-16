"""
Plugin: Q5 MRR+NPS+Churn
Categoria: analytics
Extraido automaticamente do main.py
"""
VERSAO = "1.0"
NOME = "bi"
DESCRICAO = "Q5 MRR+NPS+Churn"
CATEGORIA = "analytics"

# ═══════════════════════════════════════════════════════════════════════
# SISTEMA Q5 — BUSINESS INTELLIGENCE (8 implementações)
# ═══════════════════════════════════════════════════════════════════════

_metricas_negocio: dict = {
    "mrr": 0.0,
    "arr": 0.0,
    "churn_rate": 0.0,
    "ltv": 0.0,
    "cac": 0.0,
    "nps": 0.0,
    "dau": 0,
    "mau": 0,
}

# ── Q5.1 MRR e ARR
def calcular_mrr(usuarios_premium: int, preco_mensal: float = 49.0) -> float:
    return round(usuarios_premium * preco_mensal, 2)

def calcular_arr(mrr: float) -> float:
    return round(mrr * 12, 2)

# ── Q5.2 Churn Rate
def calcular_churn_rate(cancelamentos_mes: int, total_inicio_mes: int) -> float:
    if total_inicio_mes == 0:
        return 0.0
    return round((cancelamentos_mes / total_inicio_mes) * 100, 2)

# ── Q5.3 LTV
def calcular_ltv(mrr_por_usuario: float, churn_rate_mensal: float) -> float:
    if churn_rate_mensal == 0:
        return mrr_por_usuario * 24
    return round(mrr_por_usuario / (churn_rate_mensal / 100), 2)

# ── Q5.4 CAC
def calcular_cac(custo_marketing_mes: float, novos_clientes_mes: int) -> float:
    if novos_clientes_mes == 0:
        return 0.0
    return round(custo_marketing_mes / novos_clientes_mes, 2)

# ── Q5.5 NPS Score
_nps_respostas: list = []

def registrar_nps(usuario_id: int, nota: int, comentario: str = ""):
    _nps_respostas.append({
        "usuario_id": usuario_id,
        "nota": max(0, min(10, nota)),
        "comentario": comentario[:200],
        "ts": _datetime_s7.now().isoformat()
    })

def calcular_nps() -> dict:
    if not _nps_respostas:
        return {"nps": 0, "total": 0}
    promotores = sum(1 for r in _nps_respostas if r["nota"] >= 9)
    detratores = sum(1 for r in _nps_respostas if r["nota"] <= 6)
    total = len(_nps_respostas)
    nps = round(((promotores - detratores) / total) * 100)
    return {
        "nps": nps,
        "promotores": promotores,
        "neutros": total - promotores - detratores,
        "detratores": detratores,
        "total": total,
        "classificacao": "Excelente" if nps >= 70 else "Bom" if nps >= 50 else "Regular" if nps >= 0 else "Ruim"
    }

# ── Q5.6 DAU/MAU
_usuarios_ativos_dia: dict = {}
_usuarios_ativos_mes: dict = {}

def registrar_usuario_ativo(usuario_id: int):
    hoje = _datetime_s7.now().strftime("%Y-%m-%d")
    mes = _datetime_s7.now().strftime("%Y-%m")
    if hoje not in _usuarios_ativos_dia:
        _usuarios_ativos_dia[hoje] = set()
    _usuarios_ativos_dia[hoje].add(usuario_id)
    if mes not in _usuarios_ativos_mes:
        _usuarios_ativos_mes[mes] = set()
    _usuarios_ativos_mes[mes].add(usuario_id)

def obter_dau() -> int:
    hoje = _datetime_s7.now().strftime("%Y-%m-%d")
    return len(_usuarios_ativos_dia.get(hoje, set()))

def obter_mau() -> int:
    mes = _datetime_s7.now().strftime("%Y-%m")
    return len(_usuarios_ativos_mes.get(mes, set()))

def calcular_stickiness() -> float:
    dau = obter_dau()
    mau = obter_mau()
    if mau == 0:
        return 0.0
    return round((dau / mau) * 100, 1)

# ── Q5.7 Revenue Analytics
def gerar_relatorio_receita(pagamentos: list) -> dict:
    if not pagamentos:
        return {"total": 0, "por_plano": {}, "crescimento": 0}
    total = sum(p.get("valor", 0) for p in pagamentos)
    por_plano = {}
    for p in pagamentos:
        plano = p.get("plano", "unknown")
        por_plano[plano] = por_plano.get(plano, 0) + p.get("valor", 0)
    return {
        "total": round(total, 2),
        "por_plano": {k: round(v, 2) for k, v in por_plano.items()},
        "ticket_medio": round(total/len(pagamentos), 2),
        "total_transacoes": len(pagamentos)
    }

# ── Q5.8 Churn Prediction
def predizer_churn(usuario: dict) -> dict:
    score_churn = 0
    fatores = []
    dias_sem_login = usuario.get("dias_sem_login", 0)
    if dias_sem_login > 7:
        score_churn += 20
        fatores.append(f"Sem login ha {dias_sem_login} dias")
    total_analises = usuario.get("total_analises", 0)
    if total_analises < 3:
        score_churn += 15
        fatores.append("Poucas analises realizadas")
    if usuario.get("plano") == "free":
        score_churn += 10
        fatores.append("Plano gratuito")
    if not usuario.get("email_verificado"):
        score_churn += 25
        fatores.append("Email nao verificado")
    risco = "alto" if score_churn >= 40 else "medio" if score_churn >= 20 else "baixo"
    return {
        "score_churn": score_churn,
        "risco": risco,
        "fatores": fatores,
        "acao_recomendada": "Enviar email de reativacao" if risco == "alto" else "Monitorar"
    }

@app.get("/api/admin/bi-dashboard")
async def bi_dashboard_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario or usuario.get("plano") != "admin":
        return JSONResponse({"erro": "Nao autorizado"}, status_code=403)
    try:
        total_usuarios = db.query(Usuario).count()
        usuarios_premium = db.query(Usuario).filter(Usuario.plano.in_(["premium","enterprise"])).count()
    except Exception:
        total_usuarios = 0
        usuarios_premium = 0
    mrr = calcular_mrr(usuarios_premium)
    return JSONResponse({
        "metricas": {
            "mrr": mrr,
            "arr": calcular_arr(mrr),
            "total_usuarios": total_usuarios,
            "usuarios_premium": usuarios_premium,
            "dau": obter_dau(),
            "mau": obter_mau(),
            "stickiness_pct": calcular_stickiness(),
            "nps": calcular_nps(),
        },
        "sistema": "Q5 Business Intelligence"
    })

@app.post("/api/nps")
async def nps_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario:
        return JSONResponse({"erro": "Nao autorizado"}, status_code=401)
    body = await request.json()
    nota = body.get("nota", 0)
    comentario = body.get("comentario", "")
    registrar_nps(usuario.get("id"), nota, comentario)
    return JSONResponse({"ok": True, "nps_atual": calcular_nps(), "sistema": "Q5 NPS"})


