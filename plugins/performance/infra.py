"""
Plugin: Q9 Docker+Nginx+WAF
Categoria: performance
Extraido automaticamente do main.py
"""
VERSAO = "1.0"
NOME = "infra"
DESCRICAO = "Q9 Docker+Nginx+WAF"
CATEGORIA = "performance"

# ═══════════════════════════════════════════════════════════════════════
# SISTEMA Q9 — INFRAESTRUTURA AVANÇADA (10 implementações)
# ═══════════════════════════════════════════════════════════════════════


# ── Q9.1 Docker info
def obter_info_docker() -> dict:
    try:
        result = _subprocess_q9.run(["docker", "version", "--format", "{{.Server.Version}}"], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            return {"disponivel": True, "versao": result.stdout.strip()}
    except Exception:
        pass
    return {"disponivel": False, "nota": "Docker nao instalado ou nao acessivel"}

# ── Q9.2 Nginx config
NGINX_CONFIG_TEMPLATE = """
server {
    listen 80;
    server_name emotion-platform-albert.onrender.com;
    
    location / {
        proxy_pass http://127.0.0.1:10000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    location /static/ {
        alias /app/static/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
    
    location /ws/ {
        proxy_pass http://127.0.0.1:10000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
    
    gzip on;
    gzip_types text/plain application/json application/javascript text/css;
    gzip_min_length 1024;
}
"""

def gerar_nginx_config() -> str:
    return NGINX_CONFIG_TEMPLATE

# ── Q9.3 Cloudflare WAF Rules
CLOUDFLARE_WAF_RULES = [
    {"nome": "Block SQL Injection", "expressao": '(http.request.uri.query contains "union select") or (http.request.uri.query contains "drop table")'},
    {"nome": "Block XSS", "expressao": '(http.request.uri.query contains "<script") or (http.request.body contains "<script")'},
    {"nome": "Block Bot Scanners", "expressao": '(http.user_agent contains "sqlmap") or (http.user_agent contains "nikto")'},
    {"nome": "Rate Limit Login", "expressao": '(http.request.uri.path eq "/login") and (http.request.method eq "POST")'},
    {"nome": "Block Path Traversal", "expressao": '(http.request.uri.path contains "../") or (http.request.uri.path contains "etc/passwd")'},
]

def gerar_cloudflare_rules() -> list:
    return CLOUDFLARE_WAF_RULES

# ── Q9.4 Multi-região config
REGIOES_DISPONIVEIS = {
    "sa-east-1": {"nome": "Sao Paulo", "latencia_ms": 10, "principal": True},
    "us-east-1": {"nome": "Virginia", "latencia_ms": 180, "principal": False},
    "eu-west-1": {"nome": "Irlanda", "latencia_ms": 220, "principal": False},
}

def selecionar_melhor_regiao(ip_origem: str = None) -> dict:
    return REGIOES_DISPONIVEIS["sa-east-1"]

# ── Q9.5 Load Balancer simulado
_servidores_lb: list = [
    {"id": "render-primary", "url": "https://emotion-platform-albert.onrender.com", "peso": 100, "saudavel": True}
]
_lb_round_robin_idx = 0

def selecionar_servidor_lb() -> dict:
    global _lb_round_robin_idx
    saudaveis = [s for s in _servidores_lb if s["saudavel"]]
    if not saudaveis:
        return _servidores_lb[0]
    servidor = saudaveis[_lb_round_robin_idx % len(saudaveis)]
    _lb_round_robin_idx += 1
    return servidor

# ── Q9.6 Auto-scaling config
AUTO_SCALING_CONFIG = {
    "min_instancias": 1,
    "max_instancias": 10,
    "cpu_scale_up": 70,
    "cpu_scale_down": 30,
    "memoria_scale_up": 80,
    "cooldown_segundos": 300,
    "atual_instancias": 1,
}

def verificar_necessidade_escala() -> dict:
    import psutil as _psutil_q9
    cpu = _psutil_q9.cpu_percent(interval=0.1)
    memoria = _psutil_q9.virtual_memory().percent
    acao = "manter"
    if cpu > AUTO_SCALING_CONFIG["cpu_scale_up"] or memoria > AUTO_SCALING_CONFIG["memoria_scale_up"]:
        if AUTO_SCALING_CONFIG["atual_instancias"] < AUTO_SCALING_CONFIG["max_instancias"]:
            acao = "escalar_up"
    elif cpu < AUTO_SCALING_CONFIG["cpu_scale_down"] and memoria < 50:
        if AUTO_SCALING_CONFIG["atual_instancias"] > AUTO_SCALING_CONFIG["min_instancias"]:
            acao = "escalar_down"
    return {"acao": acao, "cpu": cpu, "memoria": memoria, "instancias": AUTO_SCALING_CONFIG["atual_instancias"]}

# ── Q9.7 Supabase
SUPABASE_URL = _os_s10.getenv("SUPABASE_URL", "")
SUPABASE_KEY = _os_s10.getenv("SUPABASE_KEY", "")

async def supabase_query(tabela: str, filtros: dict = None, limite: int = 10) -> list:
    if not all([SUPABASE_URL, SUPABASE_KEY]):
        return []
    try:
        import httpx
        params = f"limit={limite}"
        if filtros:
            for k, v in filtros.items():
                params += f"&{k}=eq.{v}"
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.get(
                f"{SUPABASE_URL}/rest/v1/{tabela}?{params}",
                headers={"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}"}
            )
            return r.json() if isinstance(r.json(), list) else []
    except Exception:
        return []

# ── Q9.8 Railway config
RAILWAY_CONFIG = {
    "servico": "emotion-platform",
    "regiao": "us-east4",
    "restart_policy": "always",
    "health_check": "/health",
    "env_vars_necessarias": ["GROQ_API_KEY","DATABASE_URL","TELEGRAM_TOKEN","MP_ACCESS_TOKEN"]
}

# ── Q9.9 Fly.io config
FLYIO_CONFIG = {
    "app": "emotion-platform",
    "regioes": ["gru"],
    "vm_size": "shared-cpu-1x",
    "memoria_mb": 256,
    "auto_stop": True,
    "auto_start": True,
}

# ── Q9.10 Infraestrutura status
def relatorio_infraestrutura() -> dict:
    import platform
    return {
        "docker": obter_info_docker(),
        "load_balancer": {"servidores": len(_servidores_lb), "saudaveis": sum(1 for s in _servidores_lb if s["saudavel"])},
        "auto_scaling": verificar_necessidade_escala(),
        "regioes": REGIOES_DISPONIVEIS,
        "sistema_operacional": {"os": platform.system(), "versao": platform.release(), "python": platform.python_version()},
        "supabase": {"configurado": bool(SUPABASE_URL)},
        "railway": RAILWAY_CONFIG,
        "fly_io": FLYIO_CONFIG,
        "nginx_config": "disponivel",
        "cloudflare_waf": {"regras": len(CLOUDFLARE_WAF_RULES)},
    }

@app.get("/api/admin/infraestrutura")
async def infraestrutura_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario or usuario.get("plano") != "admin":
        return JSONResponse({"erro": "Nao autorizado"}, status_code=403)
    return JSONResponse({"infraestrutura": relatorio_infraestrutura(), "sistema": "Q9 Infra"})

@app.get("/api/nginx-config")
async def nginx_config_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario or usuario.get("plano") != "admin":
        return JSONResponse({"erro": "Nao autorizado"}, status_code=403)
    from fastapi.responses import PlainTextResponse
    return PlainTextResponse(gerar_nginx_config(), media_type="text/plain")


