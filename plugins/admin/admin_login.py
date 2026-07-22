"""
Plugin: Admin Login Page — SEGURO
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
import os, logging, hashlib

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/admin", tags=["Admin"])

ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "albertmenezes2006@gmail.com")
JWT_SECRET = os.getenv("JWT_SECRET", "")
BASE_URL = os.getenv("BASE_URL", "https://emotion-platform-albert.onrender.com")

def verificar_admin(request: Request) -> bool:
    token = request.cookies.get("admin_token") or request.headers.get("X-Admin-Token", "")
    expected = hashlib.sha256((JWT_SECRET + "admin_access").encode()).hexdigest()[:32]
    return token == expected

def get_admin_token() -> str:
    return hashlib.sha256((JWT_SECRET + "admin_access").encode()).hexdigest()[:32]

@router.get("/", response_class=HTMLResponse, include_in_schema=False)
async def admin_home(request: Request):
    if not verificar_admin(request):
        return RedirectResponse("/admin/login")
    token = get_admin_token()
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex, nofollow">
  <title>Admin — Emotion Platform</title>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: system-ui, sans-serif; background: #0f172a; color: #e2e8f0; min-height: 100vh; display: flex; align-items: center; justify-content: center; }}
    .container {{ max-width: 600px; width: 90%; background: #1e293b; border-radius: 16px; padding: 40px; border: 1px solid #334155; }}
    h1 {{ color: #7c3aed; margin-bottom: 8px; font-size: 24px; }}
    p {{ color: #94a3b8; margin-bottom: 32px; font-size: 14px; }}
    .card {{ background: #0f172a; border-radius: 12px; padding: 20px; margin-bottom: 16px; border: 1px solid #334155; }}
    .card h3 {{ color: #a78bfa; margin-bottom: 8px; }}
    .btn {{ display: inline-block; padding: 8px 16px; background: #7c3aed; color: white; border-radius: 8px; text-decoration: none; font-size: 13px; font-weight: 600; }}
    .divider {{ border: none; border-top: 1px solid #334155; margin: 24px 0; }}
  </style>
</head>
<body>
  <div class="container">
    <h1>🔒 Painel Administrativo</h1>
    <p>Emotion Intelligence Platform v24.4.0 — Acesso Restrito</p>
    <div class="card">
      <h3>📊 Links de Gestão</h3>
      <br>
      <a href="/health" class="btn">Health Check</a>&nbsp;
      <a href="/" class="btn" style="background:#334155">← Site</a>&nbsp;
      <a href="/admin/sair" class="btn" style="background:#dc2626">Sair</a>
    </div>
    <div class="card">
      <h3>📈 Status</h3>
      <p style="margin-top:8px;color:#64748b">Admin: {ADMIN_EMAIL}</p>
    </div>
  </div>
</body>
</html>""")

@router.get("/login", response_class=HTMLResponse, include_in_schema=False)
async def admin_login_page():
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="robots" content="noindex, nofollow">
  <title>Admin Login</title>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: system-ui, sans-serif; background: #0f172a; color: #e2e8f0; min-height: 100vh; display: flex; align-items: center; justify-content: center; }}
    .box {{ background: #1e293b; border-radius: 16px; padding: 40px; width: 90%; max-width: 400px; border: 1px solid #334155; }}
    h1 {{ color: #7c3aed; margin-bottom: 24px; font-size: 22px; }}
    input {{ width: 100%; padding: 12px; background: #0f172a; border: 1px solid #334155; border-radius: 8px; color: white; margin-bottom: 16px; font-size: 14px; }}
    button {{ width: 100%; padding: 12px; background: #7c3aed; color: white; border: none; border-radius: 8px; font-size: 15px; font-weight: 700; cursor: pointer; }}
    .erro {{ color: #f87171; font-size: 13px; margin-bottom: 12px; display: none; }}
  </style>
</head>
<body>
  <div class="box">
    <h1>🔒 Admin Login</h1>
    <div class="erro" id="erro">Senha incorreta</div>
    <input type="password" id="senha" placeholder="Senha admin" />
    <button onclick="entrar()">Entrar</button>
  </div>
  <script>
  async function entrar() {
    const senha = document.getElementById('senha').value;
    const r = await fetch('/admin/auth', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({senha})});
    if (r.ok) { window.location.href = '/admin/'; }
    else { document.getElementById('erro').style.display = 'block'; }
  }
  document.getElementById('senha').addEventListener('keydown', e => { if (e.key === 'Enter') entrar(); });
  </script>
</body>
</html>""")

@router.post("/auth", include_in_schema=False)
async def admin_auth(request: Request):
    from fastapi.responses import JSONResponse, Response
    body = await request.json()
    senha = body.get("senha", "")
    senha_correta = hashlib.sha256((JWT_SECRET + "admin2026albert").encode()).hexdigest()[:16]
    if senha == senha_correta:
        token = get_admin_token()
        resp = JSONResponse({"ok": True})
        resp.set_cookie("admin_token", token, httponly=True, max_age=86400, samesite="strict")
        return resp
    raise HTTPException(401, "Senha incorreta")

@router.get("/sair", include_in_schema=False)
async def admin_sair():
    resp = RedirectResponse("/admin/login")
    resp.delete_cookie("admin_token")
    return resp

class AdminLoginPlugin(PluginBase):
    name = "admin_login"
    def setup(self, app):
        app.include_router(router)
        logger.info("[AdminLogin] ✅ Admin seguro ativado")

plugin = AdminLoginPlugin()
