#!/usr/bin/env python3
"""Banner de consentimento de cookies LGPD"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/api/v1/cookies", tags=["Cookies"])

@router.get("/banner", response_class=HTMLResponse)
async def cookie_banner():
    return HTMLResponse("""
<div id="cookie-banner" style="display:none;position:fixed;bottom:0;left:0;right:0;
     background:#1a1a2e;color:white;padding:20px 24px;z-index:99998;
     box-shadow:0 -4px 20px rgba(0,0,0,0.3);font-family:sans-serif">
  <div style="max-width:1000px;margin:0 auto;display:flex;
              align-items:center;gap:20px;flex-wrap:wrap">
    <div style="flex:1;min-width:280px">
      <strong>🍪 Cookies e Privacidade</strong>
      <p style="margin:4px 0 0;font-size:14px;opacity:0.9">
        Usamos cookies essenciais e analytics para melhorar sua experiência.
        Seus dados de saúde são protegidos conforme a LGPD.
        <a href="/privacidade" style="color:#667eea">Saiba mais</a>
      </p>
    </div>
    <div style="display:flex;gap:8px;flex-wrap:wrap">
      <button onclick="aceitar('essenciais')"
        style="background:transparent;color:white;border:2px solid rgba(255,255,255,0.3);
               padding:10px 16px;border-radius:8px;cursor:pointer;font-size:14px">
        Somente essenciais
      </button>
      <button onclick="aceitar('todos')"
        style="background:#667eea;color:white;border:none;
               padding:10px 20px;border-radius:8px;cursor:pointer;
               font-size:14px;font-weight:700">
        Aceitar todos ✓
      </button>
    </div>
  </div>
</div>
<script>
if(!localStorage.getItem("cookie_consent")){
  document.getElementById("cookie-banner").style.display="block";
}
function aceitar(tipo){
  localStorage.setItem("cookie_consent",tipo);
  localStorage.setItem("cookie_date",new Date().toISOString());
  document.getElementById("cookie-banner").style.display="none";
  if(tipo==="todos"){
    console.log("Analytics ativado");
  }
}
</script>""")

@router.get("/status")
async def cookie_status():
    return {"banner": "ativo", "lgpd": True,
            "tipos": ["essenciais", "analytics"],
            "validade_dias": 365}

class CookiePlugin(PluginBase):
    name = "cookie_consent_lgpd"
    def setup(self, app): app.include_router(router)
plugin = CookiePlugin()
