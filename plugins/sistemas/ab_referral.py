"""
Plugin: P3 AB+Email+Referral
Categoria: sistemas
Extraido automaticamente do main.py
"""
VERSAO = "1.0"
NOME = "ab_referral"
DESCRICAO = "P3 AB+Email+Referral"
CATEGORIA = "sistemas"

# ═══════════════════════════════════════════════════════════════════════
# SISTEMA P3 — A/B TESTING + EMAIL MARKETING + REFERRAL
# ═══════════════════════════════════════════════════════════════════════


# ── P3.1 A/B Testing
_experimentos_ab: dict = {}
_participantes_ab: dict = {}
_resultados_ab: dict = {}

def criar_experimento_ab(
    nome: str,
    variantes: list,
    objetivo: str = "conversao",
    trafego_pct: float = 1.0
) -> dict:
    _experimentos_ab[nome] = {
        "nome": nome,
        "variantes": variantes,
        "objetivo": objetivo,
        "trafego_pct": trafego_pct,
        "criado_em": _datetime_s7.now().isoformat(),
        "ativo": True,
        "participantes": {v: 0 for v in variantes},
        "conversoes": {v: 0 for v in variantes},
    }
    return _experimentos_ab[nome]

def obter_variante_ab(experimento: str, usuario_id: int) -> str:
    if experimento not in _experimentos_ab:
        return "controle"
    exp = _experimentos_ab[experimento]
    if not exp["ativo"]:
        return exp["variantes"][0]
    chave = f"{experimento}:{usuario_id}"
    if chave in _participantes_ab:
        return _participantes_ab[chave]
    if _random_p3.random() > exp["trafego_pct"]:
        return exp["variantes"][0]
    variante = _random_p3.choice(exp["variantes"])
    _participantes_ab[chave] = variante
    exp["participantes"][variante] = exp["participantes"].get(variante, 0) + 1
    return variante

def registrar_conversao_ab(experimento: str, usuario_id: int):
    chave = f"{experimento}:{usuario_id}"
    variante = _participantes_ab.get(chave)
    if not variante or experimento not in _experimentos_ab:
        return
    _experimentos_ab[experimento]["conversoes"][variante] = (
        _experimentos_ab[experimento]["conversoes"].get(variante, 0) + 1
    )

def calcular_resultados_ab(experimento: str) -> dict:
    if experimento not in _experimentos_ab:
        return {}
    exp = _experimentos_ab[experimento]
    resultados = {}
    for variante in exp["variantes"]:
        participantes = exp["participantes"].get(variante, 0)
        conversoes = exp["conversoes"].get(variante, 0)
        taxa = round((conversoes / participantes * 100) if participantes > 0 else 0, 2)
        resultados[variante] = {
            "participantes": participantes,
            "conversoes": conversoes,
            "taxa_conversao_pct": taxa
        }
    vencedor = max(resultados, key=lambda v: resultados[v]["taxa_conversao_pct"]) if resultados else None
    return {"experimento": experimento, "resultados": resultados, "vencedor": vencedor}

# Criar experimentos padrão
criar_experimento_ab(
    "preco_premium",
    ["R$49", "R$39", "R$59"],
    objetivo="assinatura"
)
criar_experimento_ab(
    "cta_dashboard",
    ["Analisar Agora", "Descobrir Minhas Emocoes", "Iniciar Analise"],
    objetivo="clique"
)
criar_experimento_ab(
    "onboarding",
    ["tour_guiado", "video_intro", "direto_dashboard"],
    objetivo="retencao_7dias"
)

# ── P3.2 Email Marketing com sequências
_sequencias_email: dict = {}
_usuarios_sequencia: dict = {}

SEQUENCIAS_PADRAO = {
    "boas_vindas": {
        "nome": "Boas-vindas",
        "emails": [
            {"dia": 0,  "assunto": "Bem-vindo ao Emotion Intelligence! 🧠", "tipo": "boas_vindas"},
            {"dia": 1,  "assunto": "Como fazer sua primeira analise emocional", "tipo": "tutorial"},
            {"dia": 3,  "assunto": "Seu progresso emocional esta crescendo 📈", "tipo": "engajamento"},
            {"dia": 7,  "assunto": "Uma semana de autoconhecimento — parabens!", "tipo": "marco"},
            {"dia": 14, "assunto": "Recursos Premium que voce ainda nao explorou", "tipo": "upsell"},
            {"dia": 30, "assunto": "30 dias de jornada emocional 🎉", "tipo": "retencao"},
        ]
    },
    "recuperacao": {
        "nome": "Recuperacao de Inativo",
        "emails": [
            {"dia": 0, "assunto": "Sentimos sua falta! 💙", "tipo": "reativacao"},
            {"dia": 3, "assunto": "Algo novo te espera no Emotion Intelligence", "tipo": "novidade"},
            {"dia": 7, "assunto": "Ultimo aviso — sua jornada emocional aguarda", "tipo": "urgencia"},
        ]
    },
    "upsell_premium": {
        "nome": "Upsell Premium",
        "emails": [
            {"dia": 0, "assunto": "Voce esta quase no limite — que tal o Premium?", "tipo": "upsell"},
            {"dia": 2, "assunto": "50% mais insights com o plano Premium", "tipo": "beneficios"},
            {"dia": 5, "assunto": "Oferta especial: Premium por R$39/mes", "tipo": "oferta"},
        ]
    }
}

def iniciar_sequencia_email(usuario_id: int, sequencia: str, email: str):
    chave = f"{usuario_id}:{sequencia}"
    _usuarios_sequencia[chave] = {
        "usuario_id": usuario_id,
        "email": email,
        "sequencia": sequencia,
        "email_index": 0,
        "iniciado_em": _datetime_s7.now().isoformat(),
        "ultimo_envio": None,
        "ativo": True
    }

def obter_proximo_email_sequencia(usuario_id: int, sequencia: str) -> dict:
    chave = f"{usuario_id}:{sequencia}"
    if chave not in _usuarios_sequencia:
        return {}
    estado = _usuarios_sequencia[chave]
    if not estado["ativo"]:
        return {}
    seq_config = SEQUENCIAS_PADRAO.get(sequencia, {})
    emails = seq_config.get("emails", [])
    idx = estado["email_index"]
    if idx >= len(emails):
        estado["ativo"] = False
        return {}
    return emails[idx]

def avancar_sequencia_email(usuario_id: int, sequencia: str):
    chave = f"{usuario_id}:{sequencia}"
    if chave in _usuarios_sequencia:
        _usuarios_sequencia[chave]["email_index"] += 1
        _usuarios_sequencia[chave]["ultimo_envio"] = _datetime_s7.now().isoformat()

def stats_email_marketing() -> dict:
    total_sequencias = len(_usuarios_sequencia)
    ativas = sum(1 for v in _usuarios_sequencia.values() if v.get("ativo"))
    return {
        "sequencias_ativas": ativas,
        "total_usuarios": total_sequencias,
        "sequencias_disponiveis": list(SEQUENCIAS_PADRAO.keys()),
        "total_emails_configurados": sum(
            len(s["emails"]) for s in SEQUENCIAS_PADRAO.values()
        )
    }

# ── P3.3 Sistema de Referral
_codigos_referral: dict = {}
_conversoes_referral: dict = {}

def gerar_codigo_referral(usuario_id: int, nome: str) -> str:
    import secrets
    codigo = f"{nome[:4].upper()}{secrets.token_hex(3).upper()}"
    _codigos_referral[codigo] = {
        "usuario_id": usuario_id,
        "codigo": codigo,
        "criado_em": _datetime_s7.now().isoformat(),
        "cliques": 0,
        "conversoes": 0,
        "creditos_ganhos": 0.0
    }
    return codigo

def registrar_clique_referral(codigo: str):
    if codigo in _codigos_referral:
        _codigos_referral[codigo]["cliques"] += 1

def registrar_conversao_referral(codigo: str, novo_usuario_id: int, valor: float = 0):
    if codigo not in _codigos_referral:
        return None
    ref = _codigos_referral[codigo]
    ref["conversoes"] += 1
    credito = valor * 0.1
    ref["creditos_ganhos"] = round(ref.get("creditos_ganhos", 0) + credito, 2)
    _conversoes_referral[novo_usuario_id] = {
        "via_codigo": codigo,
        "usuario_referente": ref["usuario_id"],
        "credito_gerado": credito,
        "ts": _datetime_s7.now().isoformat()
    }
    return {"credito": credito, "referente_id": ref["usuario_id"]}

def stats_referral_usuario(usuario_id: int) -> dict:
    codigos_user = {k: v for k, v in _codigos_referral.items() if v["usuario_id"] == usuario_id}
    total_cliques = sum(v["cliques"] for v in codigos_user.values())
    total_conversoes = sum(v["conversoes"] for v in codigos_user.values())
    total_creditos = sum(v["creditos_ganhos"] for v in codigos_user.values())
    return {
        "codigos": list(codigos_user.keys()),
        "total_cliques": total_cliques,
        "total_conversoes": total_conversoes,
        "creditos_ganhos": round(total_creditos, 2),
        "taxa_conversao": round((total_conversoes/total_cliques*100) if total_cliques > 0 else 0, 1)
    }

# ── P3.4 Endpoints
@app.get("/api/ab-teste/{experimento}")
async def ab_teste_ep(experimento: str, request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    usuario_id = usuario.get("id", 0) if usuario else 0
    variante = obter_variante_ab(experimento, usuario_id)
    return JSONResponse({"experimento": experimento, "variante": variante})

@app.get("/api/admin/ab-resultados")
async def ab_resultados_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario or usuario.get("plano") != "admin":
        return JSONResponse({"erro": "Nao autorizado"}, status_code=403)
    resultados = {exp: calcular_resultados_ab(exp) for exp in _experimentos_ab}
    return JSONResponse({"resultados": resultados, "sistema": "P3 A/B Testing"})

@app.get("/api/referral/meu-codigo")
async def meu_codigo_referral_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario:
        return JSONResponse({"erro": "Nao autorizado"}, status_code=401)
    usuario_id = usuario.get("id")
    nome = usuario.get("nome", "USER")
    codigos_existentes = [k for k, v in _codigos_referral.items() if v["usuario_id"] == usuario_id]
    if codigos_existentes:
        codigo = codigos_existentes[0]
    else:
        codigo = gerar_codigo_referral(usuario_id, nome)
    stats = stats_referral_usuario(usuario_id)
    return JSONResponse({
        "codigo": codigo,
        "link": f"https://emotion-platform-albert.onrender.com/cadastro?ref={codigo}",
        "stats": stats,
        "comissao": "10% de creditos por conversao",
        "sistema": "P3 Referral"
    })

@app.post("/api/referral/registrar-clique")
async def registrar_clique_ep(request: Request):
    body = await request.json()
    codigo = body.get("codigo", "")
    if codigo:
        registrar_clique_referral(codigo)
    return JSONResponse({"ok": True})

@app.get("/api/email-marketing/stats")
async def email_marketing_stats_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario or usuario.get("plano") != "admin":
        return JSONResponse({"erro": "Nao autorizado"}, status_code=403)
    return JSONResponse({
        "stats": stats_email_marketing(),
        "sistema": "P3 Email Marketing"
    })

# ═══ FIM P2+P3 ═══════════════════════════════════════════════════════




