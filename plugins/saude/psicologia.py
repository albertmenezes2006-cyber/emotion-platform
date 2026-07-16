"""
Plugin: Q1 PHQ9+GAD7+Mindfulness
Categoria: saude
Extraido automaticamente do main.py
"""
VERSAO = "1.0"
NOME = "psicologia"
DESCRICAO = "Q1 PHQ9+GAD7+Mindfulness"
CATEGORIA = "saude"

# ═══════════════════════════════════════════════════════════════════════
# SISTEMA Q1 — PSICOLOGIA E SAÚDE DIGITAL (10 implementações)
# ═══════════════════════════════════════════════════════════════════════

# ── Q1.1 PHQ-9 — Depressão
PHQ9_PERGUNTAS = [
    "Pouco interesse ou prazer em fazer as coisas",
    "Se sentindo mal, deprimido ou sem perspectiva",
    "Dificuldade para adormecer ou dormindo demais",
    "Se sentindo cansado ou com pouca energia",
    "Falta de apetite ou comendo demais",
    "Se sentindo mal consigo mesmo",
    "Dificuldade de concentracao",
    "Lentidao ou agitacao excessiva",
    "Pensamentos de se machucar",
]

PHQ9_OPCOES = [
    {"valor": 0, "label": "Nenhuma vez"},
    {"valor": 1, "label": "Varios dias"},
    {"valor": 2, "label": "Mais da metade dos dias"},
    {"valor": 3, "label": "Quase todos os dias"},
]

def calcular_phq9(respostas: list) -> dict:
    if len(respostas) != 9:
        return {"erro": "Precisam de 9 respostas"}
    total = sum(int(r) for r in respostas)
    if total <= 4:
        nivel = "Minimo"
        cor = "verde"
        recomendacao = "Sem indicacao de depressao. Continue cuidando do seu bem-estar!"
    elif total <= 9:
        nivel = "Leve"
        cor = "amarelo"
        recomendacao = "Indicacao leve. Considere conversar com alguem de confianca."
    elif total <= 14:
        nivel = "Moderado"
        cor = "laranja"
        recomendacao = "Recomendamos consultar um profissional de saude mental."
    elif total <= 19:
        nivel = "Moderadamente severo"
        cor = "vermelho"
        recomendacao = "Importante buscar apoio profissional em breve."
    else:
        nivel = "Severo"
        cor = "vermelho_escuro"
        recomendacao = "Busque apoio profissional urgente. CVV: 188 (24h gratuito)."
    questao9 = int(respostas[8]) if respostas[8] else 0
    alerta_crise = questao9 >= 1
    return {
        "total": total,
        "nivel": nivel,
        "cor": cor,
        "recomendacao": recomendacao,
        "alerta_crise": alerta_crise,
        "percentual": round((total / 27) * 100, 1),
        "escala": "PHQ-9",
        "max_score": 27,
    }

# ── Q1.2 GAD-7 — Ansiedade
GAD7_PERGUNTAS = [
    "Se sentindo nervoso, ansioso ou no limite",
    "Nao conseguindo parar ou controlar preocupacoes",
    "Preocupando-se muito com coisas diferentes",
    "Dificuldade para relaxar",
    "Tao agitado que fica dificil ficar parado",
    "Ficando facilmente irritado",
    "Sentindo medo de que algo ruim possa acontecer",
]

def calcular_gad7(respostas: list) -> dict:
    if len(respostas) != 7:
        return {"erro": "Precisam de 7 respostas"}
    total = sum(int(r) for r in respostas)
    if total <= 4:
        nivel = "Minimo"
        cor = "verde"
        recomendacao = "Nivel de ansiedade dentro do esperado."
    elif total <= 9:
        nivel = "Leve"
        cor = "amarelo"
        recomendacao = "Ansiedade leve. Tecnicas de respiracao podem ajudar."
    elif total <= 14:
        nivel = "Moderado"
        cor = "laranja"
        recomendacao = "Recomendamos apoio profissional."
    else:
        nivel = "Severo"
        cor = "vermelho"
        recomendacao = "Busque apoio profissional. A ansiedade tem tratamento eficaz."
    return {
        "total": total,
        "nivel": nivel,
        "cor": cor,
        "recomendacao": recomendacao,
        "percentual": round((total / 21) * 100, 1),
        "escala": "GAD-7",
        "max_score": 21,
    }

# ── Q1.3 DASS-21 — Depressao, Ansiedade e Estresse
DASS21_PERGUNTAS = {
    "depressao": [2, 4, 9, 12, 15, 16, 17],
    "ansiedade": [1, 3, 6, 7, 8, 14, 19],
    "estresse":  [0, 5, 10, 11, 13, 18, 20],
}

def calcular_dass21(respostas: list) -> dict:
    if len(respostas) != 21:
        return {"erro": "Precisam de 21 respostas"}
    scores = {}
    for escala, indices in DASS21_PERGUNTAS.items():
        scores[escala] = sum(int(respostas[i]) for i in indices) * 2
    def nivel_dep(s):
        if s <= 9: return "Normal"  # noqa: E701
        if s <= 13: return "Leve"  # noqa: E701
        if s <= 20: return "Moderado"  # noqa: E701
        if s <= 27: return "Severo"  # noqa: E701
        return "Extremamente severo"
    def nivel_ans(s):
        if s <= 7: return "Normal"  # noqa: E701
        if s <= 9: return "Leve"  # noqa: E701
        if s <= 14: return "Moderado"  # noqa: E701
        if s <= 19: return "Severo"  # noqa: E701
        return "Extremamente severo"
    def nivel_est(s):
        if s <= 14: return "Normal"  # noqa: E701
        if s <= 18: return "Leve"  # noqa: E701
        if s <= 25: return "Moderado"  # noqa: E701
        if s <= 33: return "Severo"  # noqa: E701
        return "Extremamente severo"
    return {
        "depressao": {"score": scores["depressao"], "nivel": nivel_dep(scores["depressao"])},
        "ansiedade": {"score": scores["ansiedade"], "nivel": nivel_ans(scores["ansiedade"])},
        "estresse":  {"score": scores["estresse"],  "nivel": nivel_est(scores["estresse"])},
        "escala": "DASS-21",
    }

# ── Q1.4 Mindfulness Timer
_sessoes_mindfulness: list = []

EXERCICIOS_MINDFULNESS = {
    "respiracao_4_7_8": {
        "nome": "Respiracao 4-7-8",
        "descricao": "Inspire 4s, segure 7s, expire 8s. Ativa o sistema nervoso parassimpatico.",
        "duracao_minutos": 5,
        "instrucoes": ["Inspire pelo nariz por 4 segundos","Segure o ar por 7 segundos","Expire pela boca por 8 segundos","Repita 4 vezes"],
        "beneficios": ["Reduz ansiedade","Melhora sono","Reduz estresse"],
    },
    "body_scan": {
        "nome": "Body Scan",
        "descricao": "Varredura corporal para relaxamento profundo.",
        "duracao_minutos": 10,
        "instrucoes": ["Deite-se confortavelmente","Feche os olhos","Foque nos pes","Suba lentamente pelo corpo"],
        "beneficios": ["Relaxamento profundo","Consciencia corporal","Reducao de tensao"],
    },
    "meditacao_5min": {
        "nome": "Meditacao 5 minutos",
        "descricao": "Meditacao rapida para clareza mental.",
        "duracao_minutos": 5,
        "instrucoes": ["Sente-se confortavelmente","Feche os olhos","Foque na respiracao","Observe pensamentos sem julgamento"],
        "beneficios": ["Clareza mental","Reducao de estresse","Foco"],
    },
    "gratidao": {
        "nome": "Pratica de Gratidao",
        "descricao": "Liste 3 coisas pelas quais voce e grato hoje.",
        "duracao_minutos": 3,
        "instrucoes": ["Respire fundo","Pense em 3 coisas boas do dia","Sinta a gratidao no corpo","Anote se quiser"],
        "beneficios": ["Bem-estar","Positividade","Perspectiva"],
    },
    "54321_grounding": {
        "nome": "5-4-3-2-1 Grounding",
        "descricao": "Tecnica de ancoragem para ansiedade e panico.",
        "duracao_minutos": 3,
        "instrucoes": ["5 coisas que voce VE","4 que pode TOCAR","3 que OUVE","2 que CHEIRA","1 que SENTE"],
        "beneficios": ["Ancoragem imediata","Reducao de panico","Presenca"],
    },
}

def registrar_sessao_mindfulness(usuario_id: int, exercicio: str, duracao_real_min: float, nota: int = None):
    _sessoes_mindfulness.append({
        "usuario_id": usuario_id,
        "exercicio": exercicio,
        "duracao_min": duracao_real_min,
        "nota": nota,
        "ts": _datetime_s7.now().isoformat()
    })

def stats_mindfulness_usuario(usuario_id: int) -> dict:
    sessoes = [s for s in _sessoes_mindfulness if s["usuario_id"] == usuario_id]
    if not sessoes:
        return {"total_sessoes": 0, "total_minutos": 0}
    total_min = sum(s.get("duracao_min", 0) for s in sessoes)
    exercicios_feitos = list(set(s["exercicio"] for s in sessoes))
    return {
        "total_sessoes": len(sessoes),
        "total_minutos": round(total_min, 1),
        "exercicios_diferentes": len(exercicios_feitos),
        "favorito": max(set(s["exercicio"] for s in sessoes), key=lambda x: sum(1 for s in sessoes if s["exercicio"]==x)),
        "media_duracao": round(total_min/len(sessoes), 1),
    }

# ── Q1.5 Breathing Exercises (animacao JS)
BREATHING_PATTERNS = {
    "box_breathing":     {"inspire": 4, "segure": 4, "expire": 4, "pause": 4, "nome": "Box Breathing"},
    "relaxamento":       {"inspire": 4, "segure": 0, "expire": 8, "pause": 0, "nome": "Relaxamento 4-8"},
    "energia":           {"inspire": 6, "segure": 2, "expire": 4, "pause": 0, "nome": "Energia"},
    "sono":              {"inspire": 4, "segure": 7, "expire": 8, "pause": 0, "nome": "Sono (4-7-8)"},
    "equilibrio":        {"inspire": 5, "segure": 5, "expire": 5, "pause": 5, "nome": "Equilibrio"},
}

def gerar_breathing_config(padrao: str = "box_breathing") -> dict:
    config = BREATHING_PATTERNS.get(padrao, BREATHING_PATTERNS["box_breathing"])
    total_ciclo = sum(v for k, v in config.items() if k != "nome")
    return {
        "padrao": padrao,
        "config": config,
        "ciclo_segundos": total_ciclo,
        "ciclos_5min": round(300 / total_ciclo),
    }

# ── Q1.6 Sleep Tracking
_registros_sono: dict = {}

def registrar_sono(usuario_id: int, horas: float, qualidade: int, notas: str = ""):
    if usuario_id not in _registros_sono:
        _registros_sono[usuario_id] = []
    _registros_sono[usuario_id].append({
        "horas": horas,
        "qualidade": qualidade,
        "notas": notas,
        "data": _datetime_s7.now().strftime("%Y-%m-%d"),
        "ts": _datetime_s7.now().isoformat()
    })

def analisar_sono_usuario(usuario_id: int) -> dict:
    registros = _registros_sono.get(usuario_id, [])
    if not registros:
        return {"sem_dados": True}
    horas = [r["horas"] for r in registros]
    qualidades = [r["qualidade"] for r in registros]
    media_horas = round(sum(horas)/len(horas), 1)
    media_qual = round(sum(qualidades)/len(qualidades), 1)
    status = "otimo" if media_horas >= 7 and media_qual >= 7 else "regular" if media_horas >= 6 else "ruim"
    return {
        "media_horas": media_horas,
        "media_qualidade": media_qual,
        "status": status,
        "total_registros": len(registros),
        "recomendacao": "8h de sono por noite e ideal para adultos",
    }

# ── Q1.7 Spotify Mood
SPOTIFY_CLIENT_ID = _os_s10.getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = _os_s10.getenv("SPOTIFY_CLIENT_SECRET", "")

PLAYLISTS_POR_EMOCAO = {
    "alegria":    {"query": "happy upbeat music", "energy": 0.8, "valence": 0.9},
    "tristeza":   {"query": "sad emotional music", "energy": 0.3, "valence": 0.2},
    "ansiedade":  {"query": "calm relaxing anxiety relief", "energy": 0.2, "valence": 0.5},
    "raiva":      {"query": "calm meditation peace", "energy": 0.3, "valence": 0.4},
    "motivacao":  {"query": "motivational workout energy", "energy": 0.9, "valence": 0.8},
    "amor":       {"query": "romantic love songs", "energy": 0.5, "valence": 0.8},
    "neutro":     {"query": "focus concentration music", "energy": 0.5, "valence": 0.5},
    "estresse":   {"query": "stress relief nature sounds", "energy": 0.2, "valence": 0.5},
}

async def spotify_obter_token_s() -> str:
    if not all([SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET]):
        return ""
    try:
        import httpx
        from base64 import b64encode
        auth = b64encode(f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}".encode()).decode()
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.post(
                "https://accounts.spotify.com/api/token",
                headers={"Authorization": f"Basic {auth}"},
                data={"grant_type": "client_credentials"}
            )
            return r.json().get("access_token", "")
    except Exception:
        return ""

async def spotify_recomendar_por_emocao(emocao: str) -> dict:
    config = PLAYLISTS_POR_EMOCAO.get(emocao, PLAYLISTS_POR_EMOCAO["neutro"])
    token = await spotify_obter_token_s()
    if not token:
        return {"emocao": emocao, "query": config["query"], "spotify_disponivel": False}
    try:
        import httpx
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.get(
                "https://api.spotify.com/v1/search",
                headers={"Authorization": f"Bearer {token}"},
                params={"q": config["query"], "type": "playlist", "limit": 5, "market": "BR"}
            )
            data = r.json()
            playlists = data.get("playlists", {}).get("items", [])
            return {
                "emocao": emocao,
                "playlists": [
                    {"nome": p["name"], "url": p["external_urls"]["spotify"], "imagem": p["images"][0]["url"] if p.get("images") else ""}
                    for p in playlists if p
                ],
                "spotify_disponivel": True
            }
    except Exception as e:
        return {"emocao": emocao, "erro": str(e), "spotify_disponivel": False}

# ── Q1.8 Wearables (estrutura)
def processar_dados_wearable(dados: dict, tipo: str = "generico") -> dict:
    processado = {
        "tipo": tipo,
        "processado_em": _datetime_s7.now().isoformat(),
        "metricas": {}
    }
    if "heart_rate" in dados:
        hr = dados["heart_rate"]
        processado["metricas"]["frequencia_cardiaca"] = {
            "valor": hr,
            "status": "normal" if 60 <= hr <= 100 else "atencao",
            "unidade": "bpm"
        }
    if "steps" in dados:
        steps = dados["steps"]
        processado["metricas"]["passos"] = {
            "valor": steps,
            "meta": 10000,
            "percentual": round(min(steps/10000*100, 100), 1)
        }
    if "sleep_hours" in dados:
        processado["metricas"]["sono"] = {
            "valor": dados["sleep_hours"],
            "meta": 8,
            "status": "bom" if dados["sleep_hours"] >= 7 else "ruim"
        }
    return processado

# ── Q1.9 Endpoints
@app.get("/api/testes-psicologicos/lista")
async def lista_testes_ep():
    return JSONResponse({
        "testes": [
            {"id": "phq9",   "nome": "PHQ-9",   "descricao": "Escala de depressao", "perguntas": 9,  "tempo_min": 3},
            {"id": "gad7",   "nome": "GAD-7",   "descricao": "Escala de ansiedade", "perguntas": 7,  "tempo_min": 2},
            {"id": "dass21", "nome": "DASS-21",  "descricao": "Depressao, ansiedade e estresse", "perguntas": 21, "tempo_min": 5},
        ],
        "aviso": "Estes testes sao de rastreamento, nao substituem avaliacao profissional.",
        "sistema": "Q1 Psicologia"
    })

@app.post("/api/testes-psicologicos/phq9")
async def aplicar_phq9_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario:
        return JSONResponse({"erro": "Nao autorizado"}, status_code=401)
    body = await request.json()
    respostas = body.get("respostas", [])
    resultado = calcular_phq9(respostas)
    if resultado.get("alerta_crise"):
        registrar_evento_siem_s14("PHQ9_CRISE", "ALTA", usuario_id=usuario.get("id"), detalhes={"motivo": "PHQ9 questao 9 positiva"})
    registrar_evento_analytics(usuario.get("id"), "teste_phq9", {"nivel": resultado.get("nivel")})
    return JSONResponse({"ok": True, "resultado": resultado, "sistema": "Q1 PHQ-9"})

@app.post("/api/testes-psicologicos/gad7")
async def aplicar_gad7_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario:
        return JSONResponse({"erro": "Nao autorizado"}, status_code=401)
    body = await request.json()
    respostas = body.get("respostas", [])
    resultado = calcular_gad7(respostas)
    registrar_evento_analytics(usuario.get("id"), "teste_gad7", {"nivel": resultado.get("nivel")})
    return JSONResponse({"ok": True, "resultado": resultado, "sistema": "Q1 GAD-7"})

@app.post("/api/testes-psicologicos/dass21")
async def aplicar_dass21_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario:
        return JSONResponse({"erro": "Nao autorizado"}, status_code=401)
    body = await request.json()
    respostas = body.get("respostas", [])
    resultado = calcular_dass21(respostas)
    registrar_evento_analytics(usuario.get("id"), "teste_dass21", {})
    return JSONResponse({"ok": True, "resultado": resultado, "sistema": "Q1 DASS-21"})

@app.get("/api/mindfulness/exercicios")
async def mindfulness_exercicios_ep():
    return JSONResponse({
        "exercicios": EXERCICIOS_MINDFULNESS,
        "breathing_patterns": BREATHING_PATTERNS,
        "sistema": "Q1 Mindfulness"
    })

@app.post("/api/mindfulness/registrar-sessao")
async def registrar_sessao_mindfulness_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario:
        return JSONResponse({"erro": "Nao autorizado"}, status_code=401)
    body = await request.json()
    registrar_sessao_mindfulness(
        usuario.get("id"),
        body.get("exercicio", ""),
        body.get("duracao_min", 5),
        body.get("nota")
    )
    return JSONResponse({"ok": True, "stats": stats_mindfulness_usuario(usuario.get("id"))})

@app.get("/api/mindfulness/stats")
async def mindfulness_stats_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario:
        return JSONResponse({"erro": "Nao autorizado"}, status_code=401)
    return JSONResponse({
        "stats": stats_mindfulness_usuario(usuario.get("id")),
        "sistema": "Q1 Mindfulness"
    })

@app.get("/api/breathing/{padrao}")
async def breathing_config_ep(padrao: str):
    config = gerar_breathing_config(padrao)
    return JSONResponse({"ok": True, "config": config, "sistema": "Q1 Breathing"})

@app.post("/api/sono/registrar")
async def registrar_sono_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario:
        return JSONResponse({"erro": "Nao autorizado"}, status_code=401)
    body = await request.json()
    registrar_sono(usuario.get("id"), body.get("horas", 7), body.get("qualidade", 7), body.get("notas", ""))
    return JSONResponse({"ok": True, "analise": analisar_sono_usuario(usuario.get("id"))})

@app.get("/api/spotify/recomendar/{emocao}")
async def spotify_recomendar_ep(emocao: str, request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario:
        return JSONResponse({"erro": "Nao autorizado"}, status_code=401)
    resultado = await spotify_recomendar_por_emocao(emocao)
    return JSONResponse({"ok": True, "recomendacao": resultado, "sistema": "Q1 Spotify"})

@app.post("/api/wearable/processar")
async def wearable_processar_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario:
        return JSONResponse({"erro": "Nao autorizado"}, status_code=401)
    body = await request.json()
    resultado = processar_dados_wearable(body.get("dados", {}), body.get("tipo", "generico"))
    return JSONResponse({"ok": True, "resultado": resultado, "sistema": "Q1 Wearables"})

# ═══ FIM Q1 — PSICOLOGIA E SAÚDE DIGITAL ════════════════════════════




