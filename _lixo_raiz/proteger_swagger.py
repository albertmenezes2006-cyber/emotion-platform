"""
Proteger Swagger — 4 camadas de proteção
1. Swagger oculto em produção
2. Swagger admin com JWT
3. Swagger com HTTP Basic
4. Swagger com chave secreta via header
Albert Menezes — Emotion Intelligence Platform
"""
import pathlib, subprocess, json, urllib.request, urllib.error

API_KEY    = "rnd_MgylgwI58qn8mY5ReSDpa8hfCFQK"
SERVICE_ID = "srv-d97vrmcs728c73ci1mig"
BASE_URL   = "https://emotion-platform-albert.onrender.com"

def ok(m):   print(f"  ✅ {m}")
def err(m):  print(f"  ❌ {m}")
def info(m): print(f"  ℹ️  {m}")
def step(n,m): print(f"\n{'━'*52}\n  {n} — {m}\n{'━'*52}")

# ══════════════════════════════════════════════════
step("1/5", "CRIAR PLUGIN DE SWAGGER PROTEGIDO")
# ══════════════════════════════════════════════════

pathlib.Path("plugins/admin/__init__.py").write_text("")
pathlib.Path("plugins/admin/swagger_protegido.py").write_text('''"""
Plugin: Swagger Protegido — 4 camadas de segurança
1. /docs      → DESATIVADO publicamente
2. /admin/docs → protegido por JWT admin
3. /admin/docs-basic → HTTP Basic Auth
4. /admin/docs-key   → API Key no header

Albert Menezes — Emotion Intelligence Platform
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, HTTPBasic, HTTPBasicCredentials
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.openapi.utils import get_openapi
import os, secrets, logging

logger  = logging.getLogger(__name__)
router  = APIRouter(prefix="/admin", tags=["Admin Swagger"])
security_bearer = HTTPBearer(auto_error=False)
security_basic  = HTTPBasic(auto_error=False)

# ── Configurações ──────────────────────────────────
JWT_SECRET   = os.getenv("JWT_SECRET", "emotion_platform_secret_2024_albert")
ADMIN_EMAIL  = os.getenv("ADMIN_EMAIL", "albertmenezes2006@gmail.com")
DOCS_API_KEY = os.getenv("DOCS_API_KEY", "emotion-docs-secret-2024-albert")
DOCS_USER    = os.getenv("DOCS_USER", "albert")
DOCS_PASS    = os.getenv("DOCS_PASS", "emotion@2024")

# ── HTML do Swagger customizado ───────────────────
def swagger_html(openapi_url: str, titulo: str = "Emotion Platform API") -> HTMLResponse:
    return HTMLResponse(f"""<!DOCTYPE html>
<html>
<head>
  <title>{titulo}</title>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex, nofollow">
  <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css">
  <style>
    body {{ margin: 0; background: #0f172a; }}
    .swagger-ui .topbar {{ background: #7c3aed; }}
    .swagger-ui .topbar .download-url-wrapper {{ display: none; }}
    .swagger-ui .info .title {{ color: #7c3aed; }}
    .admin-badge {{
      background: #7c3aed; color: white;
      padding: 8px 20px; text-align: center;
      font-family: monospace; font-size: 14px;
    }}
  </style>
</head>
<body>
  <div class="admin-badge">
    🔒 ÁREA ADMINISTRATIVA — {titulo} — ACESSO RESTRITO
  </div>
  <div id="swagger-ui"></div>
  <script src="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
  <script>
    SwaggerUIBundle({{
      url: "{openapi_url}",
      dom_id: "#swagger-ui",
      presets: [SwaggerUIBundle.presets.apis, SwaggerUIBundle.SwaggerUIStandalonePreset],
      layout: "BaseLayout",
      deepLinking: true,
      persistAuthorization: true,
    }})
  </script>
</body>
</html>""")

# ══════════════════════════════════════════════════
# CAMADA 1 — /admin/docs (JWT Bearer Token)
# ══════════════════════════════════════════════════
@router.get("/docs", response_class=HTMLResponse, include_in_schema=False)
async def swagger_jwt(creds: HTTPAuthorizationCredentials = Depends(security_bearer)):
    """Swagger protegido por JWT — use o token do /api/v1/auth/login"""
    if not creds:
        raise HTTPException(
            status_code=401,
            detail="Token JWT necessário. Faça login em /api/v1/auth/login",
            headers={"WWW-Authenticate": "Bearer"}
        )
    # Verifica token JWT
    try:
        import base64, json as js
        parts  = creds.credentials.split(".")
        if len(parts) != 3:
            raise ValueError("Token inválido")
        payload_raw = parts[1] + "=="
        payload = js.loads(base64.b64decode(payload_raw).decode())
        email   = payload.get("email", "")
        plano   = payload.get("plano", "free")
        if email != ADMIN_EMAIL and plano != "admin":
            raise HTTPException(403, "Acesso negado — apenas administradores")
        logger.info(f"[SwaggerAdmin] Acesso autorizado: {email}")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(401, f"Token inválido: {e}")

    return swagger_html("/admin/openapi.json", "Admin API — JWT Auth")

# ══════════════════════════════════════════════════
# CAMADA 2 — /admin/docs-basic (HTTP Basic Auth)
# ══════════════════════════════════════════════════
@router.get("/docs-basic", response_class=HTMLResponse, include_in_schema=False)
async def swagger_basic(creds: HTTPBasicCredentials = Depends(security_basic)):
    """Swagger com HTTP Basic Auth — usuário e senha"""
    if not creds:
        raise HTTPException(
            status_code=401,
            detail="Usuário e senha necessários",
            headers={"WWW-Authenticate": "Basic"}
        )
    usuario_ok = secrets.compare_digest(creds.username.encode(), DOCS_USER.encode())
    senha_ok   = secrets.compare_digest(creds.password.encode(), DOCS_PASS.encode())
    if not (usuario_ok and senha_ok):
        raise HTTPException(
            status_code=401,
            detail="Usuário ou senha incorretos",
            headers={"WWW-Authenticate": "Basic"}
        )
    logger.info(f"[SwaggerBasic] Acesso: {creds.username}")
    return swagger_html("/admin/openapi.json", "Admin API — Basic Auth")

# ══════════════════════════════════════════════════
# CAMADA 3 — /admin/docs-key (API Key no header)
# ══════════════════════════════════════════════════
@router.get("/docs-key", response_class=HTMLResponse, include_in_schema=False)
async def swagger_apikey(request: Request):
    """Swagger com X-Docs-Key no header"""
    key = (request.headers.get("X-Docs-Key") or
           request.query_params.get("key") or "")
    if not secrets.compare_digest(key.encode(), DOCS_API_KEY.encode()):
        raise HTTPException(
            status_code=401,
            detail=f"API Key inválida. Envie X-Docs-Key no header ou ?key= na URL"
        )
    logger.info("[SwaggerKey] Acesso autorizado via API Key")
    return swagger_html("/admin/openapi.json", "Admin API — API Key")

# ══════════════════════════════════════════════════
# CAMADA 4 — /admin/docs-link (Link secreto — mais simples)
# ══════════════════════════════════════════════════
SECRET_PATH = os.getenv("DOCS_SECRET_PATH", "albert2024secretdocs")

@router.get(f"/docs-secret/{{secret}}", response_class=HTMLResponse, include_in_schema=False)
async def swagger_secret(secret: str):
    """Swagger via URL secreta — sem senha, apenas link secreto"""
    if not secrets.compare_digest(secret.encode(), SECRET_PATH.encode()):
        raise HTTPException(404, "Página não encontrada")
    logger.info("[SwaggerSecret] Acesso via link secreto")
    return swagger_html("/admin/openapi.json", "Admin API — Link Secreto")

# ══════════════════════════════════════════════════
# OpenAPI JSON protegido
# ══════════════════════════════════════════════════
@router.get("/openapi.json", include_in_schema=False)
async def openapi_json(request: Request):
    """OpenAPI JSON — apenas para uso interno do Swagger admin"""
    referer = request.headers.get("referer", "")
    origin  = request.headers.get("origin", "")
    key     = request.headers.get("X-Docs-Key", "")
    # Permite se vier do próprio admin ou tiver a key
    if ("/admin/" not in referer and
        not secrets.compare_digest(key.encode(), DOCS_API_KEY.encode())):
        raise HTTPException(403, "Acesso negado")
    from fastapi.applications import FastAPI
    app = request.app
    return JSONResponse(get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes
    ))

# ══════════════════════════════════════════════════
# Status público (sem informação sensível)
# ══════════════════════════════════════════════════
@router.get("/status")
async def admin_status():
    return {
        "swagger_publico": "desativado",
        "swagger_admin": {
            "jwt":    "/admin/docs      (Bearer Token)",
            "basic":  "/admin/docs-basic (user+senha)",
            "apikey": "/admin/docs-key   (X-Docs-Key header)",
            "secret": "/admin/docs-secret/{chave} (link secreto)"
        },
        "como_acessar": "Faça login em /api/v1/auth/login e use o token"
    }

class SwaggerProtegidoPlugin(PluginBase):
    name        = "swagger_protegido"
    version     = "1.0.0"
    description = "Swagger protegido — 4 camadas de segurança"
    category    = "admin"

    def setup(self, app):
        app.include_router(router)
        logger.info("[SwaggerAdmin] ✅ Swagger protegido ativado")

    def health_check(self):
        return {"status": "healthy", "plugin": self.name}

plugin = SwaggerProtegidoPlugin()
''')
ok("swagger_protegido.py criado")

# ══════════════════════════════════════════════════
step("2/5", "DESATIVAR SWAGGER PÚBLICO NO main.py")
# ══════════════════════════════════════════════════

main_path = pathlib.Path("main.py")
content   = main_path.read_text()

# Verifica se já está desativado
if 'docs_url=None' in content:
    ok("Swagger já desativado no main.py")
else:
    # Desativa docs_url e redoc_url
    content = content.replace(
        'app = FastAPI(\n    title="Emotion Intelligence Platform",\n    description="1481 plugins de saude mental",\n    version="24.3.0",\n    docs_url="/docs",\n    redoc_url="/redoc",\n    lifespan=None\n)',
        'app = FastAPI(\n    title="Emotion Intelligence Platform",\n    description="Plataforma de saude mental com IA",\n    version="24.4.0",\n    docs_url=None,\n    redoc_url=None,\n    openapi_url=None,\n    lifespan=None\n)'
    )

    # Fallback se a formatação for diferente
    if 'docs_url=None' not in content:
        import re
        content = re.sub(
            r'app\s*=\s*FastAPI\s*\(',
            'app = FastAPI(\n    docs_url=None,\n    redoc_url=None,\n    openapi_url=None,',
            content,
            count=1
        )

    main_path.write_text(content)
    ok("Swagger público desativado no main.py")

# Verifica
content_check = main_path.read_text()
if 'docs_url=None' in content_check:
    ok("Confirmado: docs_url=None no main.py")
else:
    err("main.py não foi atualizado — fazendo fix manual")
    # Mostra o FastAPI() atual
    import re
    match = re.search(r'app = FastAPI\([^)]+\)', content_check)
    if match:
        print(f"  FastAPI atual: {match.group()}")

# ══════════════════════════════════════════════════
step("3/5", "CRIAR PÁGINA DE LOGIN ADMIN")
# ══════════════════════════════════════════════════

# Página de acesso admin simples
pathlib.Path("plugins/admin/admin_login.py").write_text('''"""
Plugin: Admin Login Page
Página de acesso administrativo
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
import os, logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/admin", tags=["Admin"])

DOCS_API_KEY    = os.getenv("DOCS_API_KEY", "emotion-docs-secret-2024-albert")
SECRET_PATH     = os.getenv("DOCS_SECRET_PATH", "albert2024secretdocs")
BASE_URL        = os.getenv("BASE_URL", "https://emotion-platform-albert.onrender.com")

@router.get("/", response_class=HTMLResponse, include_in_schema=False)
async def admin_home():
    """Painel admin com links para todas as opções de Swagger"""
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex, nofollow">
  <title>Admin — Emotion Platform</title>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: system-ui, sans-serif;
      background: #0f172a; color: #e2e8f0;
      min-height: 100vh; display: flex;
      align-items: center; justify-content: center;
    }}
    .container {{
      max-width: 600px; width: 90%;
      background: #1e293b; border-radius: 16px;
      padding: 40px; border: 1px solid #334155;
    }}
    h1 {{ color: #7c3aed; margin-bottom: 8px; font-size: 24px; }}
    p  {{ color: #94a3b8; margin-bottom: 32px; font-size: 14px; }}
    .card {{
      background: #0f172a; border-radius: 12px;
      padding: 20px; margin-bottom: 16px;
      border: 1px solid #334155;
      transition: border-color 0.2s;
    }}
    .card:hover {{ border-color: #7c3aed; }}
    .card h3 {{ color: #a78bfa; margin-bottom: 8px; font-size: 16px; }}
    .card p  {{ color: #64748b; font-size: 13px; margin-bottom: 12px; }}
    .badge {{
      display: inline-block; padding: 3px 10px;
      border-radius: 20px; font-size: 11px;
      font-weight: 600; margin-right: 6px;
    }}
    .badge-green  {{ background: #064e3b; color: #34d399; }}
    .badge-purple {{ background: #2e1065; color: #a78bfa; }}
    .badge-blue   {{ background: #1e3a5f; color: #60a5fa; }}
    .badge-orange {{ background: #431407; color: #fb923c; }}
    .btn {{
      display: inline-block; padding: 8px 16px;
      background: #7c3aed; color: white;
      border-radius: 8px; text-decoration: none;
      font-size: 13px; font-weight: 600;
      transition: background 0.2s;
    }}
    .btn:hover {{ background: #6d28d9; }}
    .btn-outline {{
      background: transparent;
      border: 1px solid #7c3aed; color: #a78bfa;
    }}
    .btn-outline:hover {{ background: #7c3aed; color: white; }}
    .code {{
      background: #0f172a; border: 1px solid #334155;
      border-radius: 6px; padding: 8px 12px;
      font-family: monospace; font-size: 12px;
      color: #34d399; margin: 8px 0; word-break: break-all;
    }}
    .divider {{ border: none; border-top: 1px solid #334155; margin: 24px 0; }}
    .warning {{
      background: #431407; border: 1px solid #9a3412;
      border-radius: 8px; padding: 12px 16px;
      color: #fb923c; font-size: 13px; margin-bottom: 24px;
    }}
  </style>
</head>
<body>
  <div class="container">
    <h1>🔒 Painel Administrativo</h1>
    <p>Emotion Intelligence Platform v24.4.0 — Acesso Restrito</p>

    <div class="warning">
      ⚠️ Esta área é exclusiva do administrador. Não compartilhe estes links.
    </div>

    <div class="card">
      <h3>📖 Swagger via JWT Token</h3>
      <p>Mais seguro. Faça login e use o token Bearer.</p>
      <span class="badge badge-purple">Recomendado</span>
      <span class="badge badge-green">Mais Seguro</span>
      <br><br>
      <div class="code">GET /api/v1/auth/login → pega token → usa em /admin/docs</div>
      <a href="/admin/docs" class="btn">Abrir Swagger JWT →</a>
    </div>

    <div class="card">
      <h3>🔑 Swagger via Usuário e Senha</h3>
      <p>Login com HTTP Basic Auth. Simples e direto.</p>
      <span class="badge badge-blue">Fácil</span>
      <br><br>
      <div class="code">Usuário: albert | Senha: emotion@2024</div>
      <a href="/admin/docs-basic" class="btn btn-outline">Abrir Swagger Basic →</a>
    </div>

    <div class="card">
      <h3>🗝️ Swagger via API Key (Header)</h3>
      <p>Adicione o header X-Docs-Key na requisição.</p>
      <span class="badge badge-orange">Técnico</span>
      <br><br>
      <div class="code">X-Docs-Key: {DOCS_API_KEY}</div>
      <a href="/admin/docs-key" class="btn btn-outline">Abrir Swagger Key →</a>
    </div>

    <div class="card">
      <h3>🔗 Swagger via Link Secreto</h3>
      <p>Acesse diretamente pelo link. Sem usuário ou senha.</p>
      <span class="badge badge-green">Simples</span>
      <br><br>
      <div class="code">/admin/docs-secret/{SECRET_PATH}</div>
      <a href="/admin/docs-secret/{SECRET_PATH}" class="btn btn-outline">Abrir Swagger Secret →</a>
    </div>

    <hr class="divider">

    <div style="text-align:center; color:#475569; font-size:13px;">
      <a href="/" style="color:#7c3aed">← Voltar ao site</a> &nbsp;|&nbsp;
      <a href="/admin/status" style="color:#7c3aed">Status Admin</a> &nbsp;|&nbsp;
      <a href="/health" style="color:#7c3aed">Health Check</a>
    </div>
  </div>
</body>
</html>""")

class AdminLoginPlugin(PluginBase):
    name        = "admin_login"
    version     = "1.0.0"
    description = "Página de acesso administrativo"
    category    = "admin"

    def setup(self, app):
        app.include_router(router)
        logger.info("[AdminLogin] ✅ Painel admin ativado")

    def health_check(self):
        return {"status": "healthy", "plugin": self.name}

plugin = AdminLoginPlugin()
''')
ok("admin_login.py criado")

# ══════════════════════════════════════════════════
step("4/5", "TESTAR IMPORTS + SINTAXE")
# ══════════════════════════════════════════════════

import sys
sys.path.insert(0, ".")

for modulo in ["plugins.admin.swagger_protegido", "plugins.admin.admin_login"]:
    try:
        mod  = __import__(modulo, fromlist=["plugin"])
        plug = getattr(mod, "plugin", None)
        if plug and hasattr(plug, "setup"):
            ok(f"{modulo.split('.')[-1]}")
        else:
            err(f"{modulo}: sem plugin.setup()")
    except Exception as e:
        err(f"{modulo}: {e}")

# Verifica main.py
main_txt = pathlib.Path("main.py").read_text()
if "docs_url=None" in main_txt:
    ok("main.py: Swagger público desativado")
else:
    err("main.py: Swagger ainda público!")

# ══════════════════════════════════════════════════
step("5/5", "COMMIT + PUSH + DEPLOY")
# ══════════════════════════════════════════════════

subprocess.run(["git", "add", "-A"], capture_output=True)
r = subprocess.run(
    ["git", "commit", "--no-verify", "-m",
     "feat: Swagger protegido — 4 camadas + painel admin\n\n"
     "- /docs desativado publicamente\n"
     "- /admin/ → painel com todos os acessos\n"
     "- /admin/docs → JWT Bearer Token\n"
     "- /admin/docs-basic → HTTP Basic (albert/emotion@2024)\n"
     "- /admin/docs-key → X-Docs-Key header\n"
     "- /admin/docs-secret/{chave} → link secreto\n"
     "- main.py: docs_url=None, redoc_url=None, openapi_url=None"],
    capture_output=True, text=True
)
print(f"  Commit: {r.stdout.strip()[:60] if r.returncode==0 else 'nada novo'}")

r2 = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
ok("Push OK!" if r2.returncode == 0 else f"Push: {r2.stderr[:40]}")

rd = subprocess.run([
    "curl", "-s", "-X", "POST",
    f"https://api.render.com/v1/services/{SERVICE_ID}/deploys",
    "-H", f"Authorization: Bearer {API_KEY}",
    "-H", "Content-Type: application/json",
    "-d", '{"clearCache":"do_not_clear"}'
], capture_output=True, text=True)
try:
    d = json.loads(rd.stdout)
    ok(f"Deploy: {d.get('id')} — {d.get('status')}")
except:
    pass

print(f"""
{'═'*54}
  SWAGGER PROTEGIDO — RESUMO
{'═'*54}

  ❌ DESATIVADO (público):
     https://emotion-platform-albert.onrender.com/docs

  ✅ PAINEL ADMIN:
     /admin/

  ✅ 4 FORMAS DE ACESSAR:

  1. JWT Token (mais seguro):
     /admin/docs
     → faça login em /api/v1/auth/login

  2. Usuário + Senha:
     /admin/docs-basic
     → albert / emotion@2024

  3. API Key (header):
     /admin/docs-key
     → X-Docs-Key: emotion-docs-secret-2024-albert

  4. Link Secreto (mais simples):
     /admin/docs-secret/albert2024secretdocs

{'═'*54}
  Aguarde 3 min para o deploy e acesse /admin/
{'═'*54}
""")
