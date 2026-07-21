#!/usr/bin/env python3
"""Exit intent popup"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/api/v1/exit-intent", tags=["Marketing"])

@router.get("/widget", response_class=HTMLResponse)
async def exit_widget():
    return HTMLResponse("""
<div id="exit-overlay" style="display:none;position:fixed;top:0;left:0;width:100%;height:100%;
     background:rgba(0,0,0,0.6);z-index:99999;align-items:center;justify-content:center">
  <div style="background:white;border-radius:24px;padding:48px;max-width:480px;
              width:90%;text-align:center;position:relative">
    <button onclick="fechar()" style="position:absolute;top:16px;right:16px;
      background:none;border:none;font-size:24px;cursor:pointer;color:#bbb">✕</button>
    <div style="font-size:48px;margin-bottom:16px">🎁</div>
    <h2 style="color:#333;margin:0 0 12px">Espera! Temos um presente para você</h2>
    <p style="color:#666;margin-bottom:24px;line-height:1.6">
      Use o cupom <strong style="color:#667eea">BEMVINDO</strong> e ganhe
      <strong>50% de desconto</strong> no primeiro mês do plano Pro!
    </p>
    <div style="background:#f0f4ff;border-radius:12px;padding:16px;
                font-size:24px;font-weight:800;color:#667eea;margin-bottom:24px;
                letter-spacing:4px">BEMVINDO</div>
    <a href="/precos" onclick="fechar()" style="display:block;
      background:linear-gradient(135deg,#667eea,#764ba2);color:white;
      padding:16px;border-radius:12px;text-decoration:none;
      font-weight:700;font-size:16px;margin-bottom:12px">
      Aproveitar desconto →
    </a>
    <button onclick="fechar()" style="background:none;border:none;
      color:#aaa;cursor:pointer;font-size:14px">Não, obrigado</button>
  </div>
</div>
<script>
var mostrado=false;
document.addEventListener("mouseleave",function(e){
  if(e.clientY<=0&&!mostrado&&!localStorage.getItem("exit_shown")){
    document.getElementById("exit-overlay").style.display="flex";
    mostrado=true;
    localStorage.setItem("exit_shown","1");
  }
});
function fechar(){document.getElementById("exit-overlay").style.display="none";}
</script>""")

class ExitPlugin(PluginBase):
    name = "exit_intent"
    def setup(self, app): app.include_router(router)
plugin = ExitPlugin()
