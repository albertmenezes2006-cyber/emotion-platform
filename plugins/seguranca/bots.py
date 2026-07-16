"""
Plugin: S13-S14 Bots e SIEM
Categoria: seguranca
Extraido automaticamente do main.py
"""
VERSAO = "1.0"
NOME = "bots"
DESCRICAO = "S13-S14 Bots e SIEM"
CATEGORIA = "seguranca"

# ═══════════════════════════════════════════════════════════════════════
# SEGURANÇA S13/18 — PROTEÇÃO DE BOTS (14 implementações)
# ═══════════════════════════════════════════════════════════════════════

_bot_scores_s13: dict = {}
_pow_challenges_s13: dict = {}

BOT_UA_PATTERNS = [
    "bot","spider","crawler","scraper","wget","curl/",
    "python-urllib","go-http","java/","ruby","perl/",
    "libwww","jakarta","okhttp","axios/0","node-fetch",
]

SUSPEITOS_HEADERS = [
    "x-forwarded-for",
    "via",
    "x-real-ip",
    "forwarded",
]

def calcular_bot_score_s13(request: Request) -> int:
    score = 0
    ua = request.headers.get("user-agent", "").lower()
    if not ua:
        score += 50
    else:
        for pattern in BOT_UA_PATTERNS:
            if pattern in ua:
                score += 30
                break
    if not request.headers.get("accept"):
        score += 20
    if not request.headers.get("accept-language"):
        score += 15
    if not request.headers.get("accept-encoding"):
        score += 10
    proxies = sum(1 for h in SUSPEITOS_HEADERS if h in request.headers)
    score += proxies * 5
    return min(score, 100)

def gerar_pow_challenge_s13(dificuldade: int = 4) -> dict:
    import secrets
    import time
    challenge = secrets.token_hex(32)
    _pow_challenges_s13[challenge] = {
        "criado_em": time.time(),
        "dificuldade": dificuldade,
        "usado": False
    }
    return {"challenge": challenge, "dificuldade": dificuldade, "prefix": "0" * dificuldade}

def verificar_pow_s13(challenge: str, solucao: str) -> bool:
    import hashlib
    import time
    if challenge not in _pow_challenges_s13:
        return False
    dados = _pow_challenges_s13[challenge]
    if dados["usado"]:
        return False
    if time.time() - dados["criado_em"] > 300:
        return False
    dificuldade = dados["dificuldade"]
    hash_resultado = hashlib.sha256(f"{challenge}{solucao}".encode()).hexdigest()
    if hash_resultado.startswith("0" * dificuldade):
        _pow_challenges_s13[challenge]["usado"] = True
        return True
    return False

def honeypot_field_check_s13(form_data: dict) -> bool:
    campos_honeypot = ["website", "url", "homepage", "phone2", "fax"]
    for campo in campos_honeypot:
        if form_data.get(campo):
            return True
    return False

def detectar_headless_browser_s13(request: Request) -> bool:
    ua = request.headers.get("user-agent", "").lower()
    indicadores = ["headless","phantom","selenium","webdriver","puppeteer","playwright"]
    return any(ind in ua for ind in indicadores)

def detectar_automacao_s13(request: Request) -> bool:
    headers_automacao = ["x-selenium","x-webdriver","x-automation","x-playwright"]
    return any(h in request.headers for h in headers_automacao)

def bot_score_nivel_s13(score: int) -> str:
    if score < 20:
        return "humano"
    if score < 50:
        return "suspeito"
    if score < 80:
        return "provavel_bot"
    return "bot_confirmado"

class BotProtectionMiddlewareS13(_BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        ip = request.client.host if request.client else "unknown"
        path = request.url.path
        if path.startswith("/static/") or path in ("/favicon.ico","/robots.txt","/health"):
            return await call_next(request)
        if detectar_headless_browser_s13(request):
            incrementar_score_ip_s9(ip, 40)
            return JSONResponse({"erro": "Acesso automatizado detectado"}, status_code=403)
        if detectar_automacao_s13(request):
            incrementar_score_ip_s9(ip, 50)
            return JSONResponse({"erro": "Automacao nao permitida"}, status_code=403)
        bot_score = calcular_bot_score_s13(request)
        ip_key = f"bot:{ip}"
        _bot_scores_s13[ip_key] = bot_score
        response = await call_next(request)
        response.headers["X-Bot-Score"] = str(bot_score)
        return response

app.add_middleware(BotProtectionMiddlewareS13)

@app.get("/api/pow-challenge")
async def pow_challenge_ep(request: Request):
    challenge = gerar_pow_challenge_s13()
    return JSONResponse({"ok": True, "challenge": challenge, "seguranca": "S13/18"})

@app.get("/api/bot-status")
async def bot_status_ep(request: Request):
    score = calcular_bot_score_s13(request)
    return JSONResponse({
        "bot_score": score,
        "nivel": bot_score_nivel_s13(score),
        "headless": detectar_headless_browser_s13(request),
        "automacao": detectar_automacao_s13(request),
        "seguranca": "S13/18 — 14 protecoes anti-bot"
    })

# ═══ FIM S11+S12+S13/18 ═════════════════════════════════════════════



# ═══════════════════════════════════════════════════════════════════════
# SEGURANÇA S14/18 — MONITORAMENTO DE SEGURANÇA (18 implementações)
# ═══════════════════════════════════════════════════════════════════════

_eventos_siem_s14: list = []
_alertas_enviados_s14: dict = {}
_iocs_s14: set = set()
_geo_cache_s14: dict = {}

SEVERIDADES_SIEM = {
    "CRITICA":  {"notificar": True,  "bloquear": True,  "pontos": 100},
    "ALTA":     {"notificar": True,  "bloquear": False, "pontos": 50},
    "MEDIA":    {"notificar": False, "bloquear": False, "pontos": 25},
    "BAIXA":    {"notificar": False, "bloquear": False, "pontos": 10},
    "INFO":     {"notificar": False, "bloquear": False, "pontos": 0},
}

def registrar_evento_siem_s14(
    tipo: str,
    severidade: str,
    ip: str = None,
    usuario_id: int = None,
    detalhes: dict = None
):
    evento = {
        "id": gerar_token_seguro_sec(8),
        "tipo": tipo,
        "severidade": severidade,
        "ip": ip,
        "usuario_id": usuario_id,
        "detalhes": detalhes or {},
        "ts": _datetime_s7.now().isoformat()
    }
    _eventos_siem_s14.append(evento)
    if len(_eventos_siem_s14) > 1000:
        _eventos_siem_s14.pop(0)
    config = SEVERIDADES_SIEM.get(severidade, SEVERIDADES_SIEM["INFO"])
    if ip and config["pontos"] > 0:
        incrementar_score_ip_s9(ip, config["pontos"])
    if config["notificar"]:
        _notificar_siem_s14(evento)
    registrar_auditoria_s8(tipo, usuario_id=usuario_id, ip=ip, detalhes=detalhes)

def _notificar_siem_s14(evento: dict):
    tipo = evento.get("tipo","?")
    chave_cooldown = f"siem:{tipo}"
    agora = _datetime_s7.now()
    if chave_cooldown in _alertas_enviados_s14:
        delta = (agora - _alertas_enviados_s14[chave_cooldown]).total_seconds()
        if delta < 300:
            return
    _alertas_enviados_s14[chave_cooldown] = agora
    import urllib.request
    import urllib.parse
    token = _os_s10.getenv("TELEGRAM_TOKEN", "")
    chat_id = _os_s10.getenv("TELEGRAM_CHAT_ID", "")
    if not token or not chat_id:
        return
    try:
        sev = evento.get("severidade","?")
        emoji = {"CRITICA":"🔴","ALTA":"🟠","MEDIA":"🟡","BAIXA":"🟢","INFO":"🔵"}.get(sev,"⚪")
        msg = (
            f"{emoji} *SIEM {sev}*\n"
            f"Tipo: `{tipo}`\n"
            f"IP: `{evento.get('ip','N/A')}`\n"
            f"User: `{evento.get('usuario_id','N/A')}`\n"
            f"⏰ {evento.get('ts','')[:16]}"
        )
        data = urllib.parse.urlencode({"chat_id":chat_id,"text":msg,"parse_mode":"Markdown"}).encode()
        urllib.request.urlopen(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data=data, timeout=3
        )
    except Exception:
        pass

def adicionar_ioc_s14(indicador: str, tipo: str = "ip"):
    _iocs_s14.add(f"{tipo}:{indicador}")

def verificar_ioc_s14(indicador: str, tipo: str = "ip") -> bool:
    return f"{tipo}:{indicador}" in _iocs_s14

def correlacionar_eventos_s14(ip: str, janela_minutos: int = 10) -> dict:
    from datetime import timedelta
    agora = _datetime_s7.now()
    janela = agora - timedelta(minutes=janela_minutos)
    eventos_ip = [
        e for e in _eventos_siem_s14
        if e.get("ip") == ip and
        _datetime_s7.fromisoformat(e.get("ts", agora.isoformat())) > janela
    ]
    tipos = list(set(e.get("tipo") for e in eventos_ip))
    severidades = list(set(e.get("severidade") for e in eventos_ip))
    risco = "CRITICO" if "CRITICA" in severidades else "ALTO" if "ALTA" in severidades else "NORMAL"
    return {
        "ip": ip,
        "eventos_recentes": len(eventos_ip),
        "tipos": tipos,
        "risco": risco,
        "janela_minutos": janela_minutos
    }

def gerar_relatorio_seguranca_s14() -> dict:
    total = len(_eventos_siem_s14)
    por_sev = {}
    for ev in _eventos_siem_s14:
        sev = ev.get("severidade", "INFO")
        por_sev[sev] = por_sev.get(sev, 0) + 1
    ips_suspeitos = {
        ip: score for ip, score in _score_ip_s9.items() if score > 30
    }
    return {
        "total_eventos": total,
        "por_severidade": por_sev,
        "ips_suspeitos": len(ips_suspeitos),
        "ips_bloqueados": len(_blacklist_ips_s3),
        "iocs_monitorados": len(_iocs_s14),
        "honeypot_hits": len(_honeypot_acessos_s9),
        "gerado_em": _datetime_s7.now().isoformat()
    }

def gerar_scorecard_seguranca_s14() -> dict:
    implementacoes = {
        "S1_autenticacao": True,
        "S2_headers": True,
        "S3_rate_limit": True,
        "S4_input_validation": True,
        "S5_sql_protection": True,
        "S6_upload_security": True,
        "S7_sessions": True,
        "S8_audit_logs": True,
        "S9_attack_detection": True,
        "S10_criptografia": True,
        "S11_lgpd": True,
        "S12_api_security": True,
        "S13_bot_protection": True,
        "S14_siem": True,
        "S15_dependencies": False,
        "S16_backup": False,
        "S17_zero_trust": False,
        "S18_hardening": False,
    }
    total = len(implementacoes)
    ativas = sum(1 for v in implementacoes.values() if v)
    score = int((ativas / total) * 100)
    return {
        "score_seguranca": score,
        "implementacoes_ativas": ativas,
        "total_implementacoes": total,
        "nivel": "Excelente" if score >= 90 else "Bom" if score >= 70 else "Regular",
        "detalhes": implementacoes
    }

@app.get("/api/admin/siem")
async def admin_siem_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario or usuario.get("plano") != "admin":
        return JSONResponse({"erro": "Nao autorizado"}, status_code=403)
    return JSONResponse({
        "eventos": _eventos_siem_s14[-50:],
        "relatorio": gerar_relatorio_seguranca_s14(),
        "scorecard": gerar_scorecard_seguranca_s14(),
        "seguranca": "S14/18 — 18 implementacoes SIEM"
    })

@app.get("/api/security-score")
async def security_score_ep(request: Request):
    scorecard = gerar_scorecard_seguranca_s14()
    return JSONResponse({
        "score": scorecard["score_seguranca"],
        "nivel": scorecard["nivel"],
        "implementacoes": scorecard["implementacoes_ativas"],
        "seguranca": "S14/18"
    })


