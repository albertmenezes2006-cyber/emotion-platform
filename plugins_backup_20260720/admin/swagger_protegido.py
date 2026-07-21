"""
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
