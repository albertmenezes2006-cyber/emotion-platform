"""
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
