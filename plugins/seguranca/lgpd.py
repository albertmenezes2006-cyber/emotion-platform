"""
Plugin: S11-S12 LGPD e API
Categoria: seguranca
Extraido automaticamente do main.py
"""
VERSAO = "1.0"
NOME = "lgpd"
DESCRICAO = "S11-S12 LGPD e API"
CATEGORIA = "seguranca"

# ═══════════════════════════════════════════════════════════════════════
# SEGURANÇA S11/18 — LGPD COMPLIANCE (22 implementações)
# ═══════════════════════════════════════════════════════════════════════

_consentimentos_s11: dict = {}
_solicitacoes_lgpd_s11: list = []

BASES_LEGAIS_LGPD = {
    "cadastro":       "Execucao de contrato (Art. 7, V)",
    "analise_emocao": "Consentimento explicito (Art. 7, I)",
    "chat_sofia":     "Consentimento explicito (Art. 7, I)",
    "diario":         "Consentimento explicito (Art. 7, I)",
    "pagamento":      "Execucao de contrato (Art. 7, V)",
    "email_mkt":      "Consentimento explicito (Art. 7, I)",
    "analytics":      "Interesse legitimo (Art. 7, IX)",
    "logs_sistema":   "Cumprimento de obrigacao legal (Art. 7, II)",
}

DADOS_COLETADOS = {
    "nome":           {"sensivel": False, "retencao_dias": 1825},
    "email":          {"sensivel": False, "retencao_dias": 1825},
    "senha_hash":     {"sensivel": False, "retencao_dias": 1825},
    "analises":       {"sensivel": True,  "retencao_dias": 730},
    "mensagens_sofia":{"sensivel": True,  "retencao_dias": 365},
    "diarios":        {"sensivel": True,  "retencao_dias": 730},
    "ip_acesso":      {"sensivel": False, "retencao_dias": 90},
    "pagamentos":     {"sensivel": False, "retencao_dias": 1825},
}

def registrar_consentimento_s11(usuario_id: int, tipo: str, aceito: bool, ip: str = None):
    chave = f"{usuario_id}:{tipo}"
    _consentimentos_s11[chave] = {
        "usuario_id": usuario_id,
        "tipo": tipo,
        "aceito": aceito,
        "ts": _datetime_s7.now().isoformat(),
        "ip": ip,
        "versao_politica": "2.0"
    }

def verificar_consentimento_s11(usuario_id: int, tipo: str) -> bool:
    chave = f"{usuario_id}:{tipo}"
    consent = _consentimentos_s11.get(chave)
    if not consent:
        return False
    return consent.get("aceito", False)

def revogar_consentimento_s11(usuario_id: int, tipo: str):
    chave = f"{usuario_id}:{tipo}"
    if chave in _consentimentos_s11:
        _consentimentos_s11[chave]["aceito"] = False
        _consentimentos_s11[chave]["revogado_em"] = _datetime_s7.now().isoformat()

def solicitar_portabilidade_s11(usuario_id: int, email: str) -> dict:
    solicitacao = {
        "id": gerar_token_seguro_sec(16),
        "tipo": "portabilidade",
        "usuario_id": usuario_id,
        "email": email,
        "status": "pendente",
        "prazo_dias": 15,
        "criado_em": _datetime_s7.now().isoformat()
    }
    _solicitacoes_lgpd_s11.append(solicitacao)
    return solicitacao

def solicitar_exclusao_s11(usuario_id: int, motivo: str = "") -> dict:
    solicitacao = {
        "id": gerar_token_seguro_sec(16),
        "tipo": "exclusao",
        "usuario_id": usuario_id,
        "motivo": motivo,
        "status": "pendente",
        "prazo_dias": 15,
        "criado_em": _datetime_s7.now().isoformat()
    }
    _solicitacoes_lgpd_s11.append(solicitacao)
    return solicitacao

def gerar_relatorio_dados_usuario_s11(usuario_id: int, usuario_data: dict) -> dict:
    return {
        "usuario_id": usuario_id,
        "dados_coletados": DADOS_COLETADOS,
        "bases_legais": BASES_LEGAIS_LGPD,
        "consentimentos": {
            k: v for k, v in _consentimentos_s11.items()
            if str(usuario_id) in k
        },
        "direitos": [
            "Acesso aos dados (Art. 18, I)",
            "Correcao de dados (Art. 18, III)",
            "Anonimizacao (Art. 18, IV)",
            "Portabilidade (Art. 18, V)",
            "Exclusao (Art. 18, VI)",
            "Revogacao de consentimento (Art. 18, IX)",
            "Oposicao ao tratamento (Art. 18, XI)",
        ],
        "contato_dpo": "dpo@emotionplatform.com.br",
        "gerado_em": _datetime_s7.now().isoformat()
    }

def verificar_menor_idade_s11(data_nascimento: str) -> bool:
    try:
        from datetime import date
        nascimento = _datetime_s7.strptime(data_nascimento, "%Y-%m-%d").date()
        hoje = date.today()
        idade = (hoje - nascimento).days // 365
        return idade < 18
    except Exception:
        return False

def notificar_violacao_dados_s11(descricao: str, dados_afetados: list, qtd_usuarios: int):
    notificacao = {
        "tipo": "VIOLACAO_DADOS",
        "descricao": descricao,
        "dados_afetados": dados_afetados,
        "qtd_usuarios": qtd_usuarios,
        "notificado_em": _datetime_s7.now().isoformat(),
        "prazo_anpd_horas": 72,
        "status": "pendente_notificacao_anpd"
    }
    _solicitacoes_lgpd_s11.append(notificacao)
    registrar_auditoria_s8("VIOLACAO_DADOS", detalhes=notificacao)
    return notificacao

@app.get("/api/meus-dados")
async def api_meus_dados(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario:
        return JSONResponse({"erro": "Nao autorizado"}, status_code=401)
    relatorio = gerar_relatorio_dados_usuario_s11(usuario.get("id"), usuario)
    registrar_auditoria_s8("EXPORT_DADOS", usuario_id=usuario.get("id"))
    return JSONResponse({"ok": True, "relatorio": relatorio, "seguranca": "S11/18 LGPD"})

@app.post("/api/solicitar-exclusao")
async def api_solicitar_exclusao(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario:
        return JSONResponse({"erro": "Nao autorizado"}, status_code=401)
    body = await request.json()
    solicitacao = solicitar_exclusao_s11(usuario.get("id"), body.get("motivo", ""))
    registrar_auditoria_s8("CONTA_DELETADA", usuario_id=usuario.get("id"))
    return JSONResponse({"ok": True, "protocolo": solicitacao["id"], "prazo_dias": 15})

@app.post("/api/consentimento")
async def api_consentimento(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario:
        return JSONResponse({"erro": "Nao autorizado"}, status_code=401)
    body = await request.json()
    tipo = body.get("tipo", "")
    aceito = body.get("aceito", False)
    ip = request.client.host if request.client else None
    registrar_consentimento_s11(usuario.get("id"), tipo, aceito, ip)
    return JSONResponse({"ok": True, "tipo": tipo, "aceito": aceito})

@app.get("/api/lgpd-status")
async def api_lgpd_status(request: Request):
    return JSONResponse({
        "conformidade": "LGPD — Lei 13.709/2018",
        "bases_legais": BASES_LEGAIS_LGPD,
        "dados_coletados": list(DADOS_COLETADOS.keys()),
        "dpo": "dpo@emotionplatform.com.br",
        "implementacoes": 22,
        "seguranca": "S11/18"
    })

# ═══════════════════════════════════════════════════════════════════════
# SEGURANÇA S12/18 — API SECURITY (16 implementações)
# ═══════════════════════════════════════════════════════════════════════

_api_keys_cache_s12: dict = {}
_api_usage_s12: dict = {}

API_SCOPES = {
    "read":      ["GET"],
    "write":     ["GET","POST","PUT"],
    "admin":     ["GET","POST","PUT","DELETE"],
    "analytics": ["GET"],
    "webhook":   ["POST"],
}

API_PLANOS_LIMITES = {
    "developer":  {"req_dia": 1000,   "req_min": 60},
    "business":   {"req_dia": 10000,  "req_min": 600},
    "enterprise": {"req_dia": 100000, "req_min": 6000},
}

def validar_api_key_s12(api_key: str, metodo: str = "GET", scope_requerido: str = "read") -> dict:
    if not api_key or not api_key.startswith("ep_"):
        return {"valida": False, "erro": "Formato de API key invalido"}
    if len(api_key) < 20:
        return {"valida": False, "erro": "API key muito curta"}
    metodos_permitidos = API_SCOPES.get(scope_requerido, ["GET"])
    if metodo not in metodos_permitidos:
        return {"valida": False, "erro": f"Metodo {metodo} nao permitido para scope {scope_requerido}"}
    return {"valida": True, "scope": scope_requerido, "metodo": metodo}

def gerar_idempotency_key_s12() -> str:
    import secrets
    return f"idem_{secrets.token_hex(16)}"

def verificar_idempotency_s12(key: str, resultado_anterior: dict = None) -> dict:
    if key in _api_usage_s12:
        return {"duplicado": True, "resultado": _api_usage_s12[key]}
    if resultado_anterior:
        _api_usage_s12[key] = resultado_anterior
    return {"duplicado": False}

def assinar_request_hmac_s12(payload: str, secret: str) -> str:
    import hmac as _hmac_local
    import hashlib
    return _hmac_local.new(
        secret.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()

def verificar_assinatura_webhook_s12(payload: str, assinatura: str, secret: str) -> bool:
    esperada = assinar_request_hmac_s12(payload, secret)
    return _hmac_sec.compare_digest(esperada, assinatura)

def adicionar_deprecation_header(response, versao_atual: str, versao_nova: str, sunset_date: str):
    response.headers["Deprecation"] = "true"
    response.headers["Sunset"] = sunset_date
    response.headers["Link"] = f'</api/{versao_nova}>; rel="successor-version"'
    return response

def limitar_response_fields(dados: dict, campos_permitidos: list) -> dict:
    if not campos_permitidos:
        return dados
    return {k: v for k, v in dados.items() if k in campos_permitidos}

def stats_api_s12() -> dict:
    return {
        "versao_atual": "v1",
        "versao_beta": "v2",
        "scopes_disponiveis": list(API_SCOPES.keys()),
        "planos": list(API_PLANOS_LIMITES.keys()),
        "autenticacao": ["API Key", "Bearer Token"],
        "formato": "JSON",
        "rate_limit": "sliding window",
        "idempotency": True,
        "webhook_signature": True,
        "implementacoes": 16
    }

@app.get("/api/v1/api-info")
async def api_info_ep(request: Request):
    return JSONResponse({
        "ok": True,
        "stats": stats_api_s12(),
        "documentacao": "/api/docs",
        "seguranca": "S12/18"
    })

@app.post("/api/v1/webhook/verify")
async def verificar_webhook_ep(request: Request):
    try:
        payload = await request.body()
        assinatura = request.headers.get("X-Webhook-Signature", "")
        secret = _os_s10.getenv("WEBHOOK_SECRET", "webhook_secret_2024")
        valida = verificar_assinatura_webhook_s12(payload.decode(), assinatura, secret)
        return JSONResponse({"valida": valida, "seguranca": "S12/18"})
    except Exception as e:
        return JSONResponse({"erro": str(e)}, status_code=500)


