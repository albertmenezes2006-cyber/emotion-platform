"""
Plugin: S3-S4 Rate Limit e Input
Categoria: seguranca
Extraido automaticamente do main.py
"""
VERSAO = "1.0"
NOME = "rate_limit"
DESCRICAO = "S3-S4 Rate Limit e Input"
CATEGORIA = "seguranca"

# ═══════════════════════════════════════════════════════════════════════
# SEGURANÇA S2/18 — HEADERS DE SEGURANÇA
# ═══════════════════════════════════════════════════════════════════════

SECURITY_HEADERS_S2 = {
    "X-Frame-Options": "DENY",
    "X-Content-Type-Options": "nosniff",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains; preload",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "Server": "Emotion-Platform",
    "X-XSS-Protection": "1; mode=block",
    "Permissions-Policy": "camera=(), microphone=(self), geolocation=(), payment=()",
    "Cross-Origin-Opener-Policy": "same-origin",
    "Cross-Origin-Resource-Policy": "same-origin",
    "Cache-Control": "no-store, no-cache, must-revalidate, private",
    "Pragma": "no-cache",
}

CSP_POLICY_S2 = (
    "default-src 'self'; "
    "script-src 'self' 'unsafe-inline' 'unsafe-eval' "
    "https://cdn.jsdelivr.net https://cdnjs.cloudflare.com "
    "https://www.googletagmanager.com https://www.google-analytics.com; "
    "style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net "
    "https://fonts.googleapis.com; "
    "font-src 'self' https://fonts.gstatic.com https://cdnjs.cloudflare.com; "
    "img-src 'self' data: https: blob:; "
    "connect-src 'self' https://api.groq.com https://www.google-analytics.com; "
    "frame-src 'none'; object-src 'none'; base-uri 'self'; form-action 'self';"
)


class SecurityHeadersMiddleware(_BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        path = request.url.path
        for h, v in SECURITY_HEADERS_S2.items():
            response.headers[h] = v
        if not path.startswith("/api/"):
            response.headers["Content-Security-Policy"] = CSP_POLICY_S2
        response.headers.pop("X-Powered-By", None)
        origin = request.headers.get("origin", "")
        allowed = ["https://emotion-platform-albert.onrender.com","http://localhost:10000"]
        if origin in allowed:
            response.headers["Access-Control-Allow-Origin"] = origin
            response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
            response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization, X-API-Key"
            response.headers["Access-Control-Allow-Credentials"] = "true"
            response.headers["Vary"] = "Origin"
        return response

app.add_middleware(SecurityHeadersMiddleware)

@app.post("/api/csp-report")
async def receber_csp_report(request: Request):
    return JSONResponse({"ok": True})

@app.get("/api/security-headers")
async def verificar_security_headers_ep(request: Request):
    return JSONResponse({"headers_ativos": list(SECURITY_HEADERS_S2.keys()), "csp_ativo": True, "seguranca": "S2/18"})

# ═══════════════════════════════════════════════════════════════════════
# SEGURANÇA S3/18 — RATE LIMITING AVANCADO
# ═══════════════════════════════════════════════════════════════════════

RATE_LIMITS_S3 = {
    "global":          {"requisicoes": 1000, "janela_seg": 3600},
    "login":           {"requisicoes": 5,    "janela_seg": 300},
    "cadastro":        {"requisicoes": 3,    "janela_seg": 3600},
    "recuperar_senha": {"requisicoes": 3,    "janela_seg": 1800},
    "api_publica":     {"requisicoes": 100,  "janela_seg": 3600},
    "api_premium":     {"requisicoes": 1000, "janela_seg": 3600},
    "analisar":        {"requisicoes": 50,   "janela_seg": 3600},
    "chat":            {"requisicoes": 100,  "janela_seg": 3600},
    "upload":          {"requisicoes": 10,   "janela_seg": 3600},
    "admin":           {"requisicoes": 200,  "janela_seg": 3600},
    "free":            {"requisicoes": 200,  "janela_seg": 3600},
}

_rate_store_s3 = {}
_rate_lock_s3 = _threading_sec.Lock()
_blacklist_ips_s3: set = set()
_whitelist_ips_s3: set = {"127.0.0.1", "::1"}

def sliding_window_s3(chave: str, limite: int, janela_seg: int) -> dict:
    agora = _time_sec.time()
    with _rate_lock_s3:
        if chave not in _rate_store_s3:
            _rate_store_s3[chave] = _deque_sec()
        janela = _rate_store_s3[chave]
        limite_tempo = agora - janela_seg
        while janela and janela[0] < limite_tempo:
            janela.popleft()
        count = len(janela)
        restantes = max(0, limite - count)
        reset_em = int(janela[0] + janela_seg - agora) if janela else janela_seg
        if count >= limite:
            return {"permitido": False, "count": count, "limite": limite, "restantes": 0, "reset_em": reset_em}
        janela.append(agora)
        return {"permitido": True, "count": count+1, "limite": limite, "restantes": restantes-1, "reset_em": janela_seg}

def verificar_rate_limit_s3(ip: str, tipo: str, plano: str = "free") -> dict:
    if ip in _whitelist_ips_s3:
        return {"permitido": True, "restantes": 999, "reset_em": 0}
    if ip in _blacklist_ips_s3:
        return {"permitido": False, "restantes": 0, "reset_em": 3600}
    config = RATE_LIMITS_S3.get(tipo, RATE_LIMITS_S3["global"])
    limite = config["requisicoes"]
    if plano == "premium":
        limite = int(limite * 3)
    elif plano == "enterprise":
        limite = int(limite * 10)
    return sliding_window_s3(f"rl:{tipo}:{ip}", limite, config["janela_seg"])

def ip_bloqueado_s3(ip: str) -> bool:
    return ip in _blacklist_ips_s3

class RateLimitMiddlewareS3(_BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        ip = request.client.host if request.client else "unknown"
        path = request.url.path
        if path.startswith("/static/") or path in ("/favicon.ico", "/robots.txt"):
            return await call_next(request)
        if ip_bloqueado_s3(ip):
            return JSONResponse({"erro": "IP bloqueado"}, status_code=403)
        tipo = "global"
        if "/login" in path:
            tipo = "login"
        elif "/cadastro" in path:
            tipo = "cadastro"
        elif "/recuperar" in path:
            tipo = "recuperar_senha"
        elif "/api/v1/" in path:
            tipo = "api_publica"
        elif "/admin" in path:
            tipo = "admin"
        elif "/upload" in path:
            tipo = "upload"
        resultado = verificar_rate_limit_s3(ip, tipo)
        if not resultado["permitido"]:
            return JSONResponse(
                {"erro": "Rate limit excedido", "retry_after": resultado.get("reset_em", 60)},
                status_code=429,
                headers={"Retry-After": str(resultado.get("reset_em", 60))}
            )
        response = await call_next(request)
        response.headers["X-RateLimit-Remaining"] = str(resultado.get("restantes", 0))
        return response

app.add_middleware(RateLimitMiddlewareS3)

@app.get("/api/rate-limit-status")
async def rate_limit_status_ep(request: Request):
    ip = request.client.host if request.client else "unknown"
    return JSONResponse({"ip": ip, "bloqueado": ip_bloqueado_s3(ip), "limites": RATE_LIMITS_S3, "seguranca": "S3/18"})


