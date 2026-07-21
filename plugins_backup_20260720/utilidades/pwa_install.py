#!/usr/bin/env python3
"""Botao de instalacao PWA"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/api/v1/pwa", tags=["PWA"])

@router.get("/install-btn", response_class=HTMLResponse)
async def install_button():
    return HTMLResponse("""
<div id="pwa-install" style="display:none;position:fixed;bottom:80px;left:20px;
     background:linear-gradient(135deg,#667eea,#764ba2);color:white;
     border-radius:16px;padding:16px 20px;font-family:sans-serif;
     box-shadow:0 4px 20px rgba(102,126,234,0.5);z-index:9996;max-width:280px">
    <div style="font-weight:700;margin-bottom:4px">📱 Instalar app</div>
    <div style="font-size:13px;opacity:0.9;margin-bottom:12px">
        Instale o Emotion Platform no seu celular
    </div>
    <div style="display:flex;gap:8px">
        <button onclick="instalar()" style="background:white;color:#667eea;border:none;
            border-radius:8px;padding:8px 16px;font-weight:700;cursor:pointer;flex:1">
            Instalar
        </button>
        <button onclick="fechar()" style="background:rgba(255,255,255,0.2);color:white;
            border:none;border-radius:8px;padding:8px 12px;cursor:pointer">
            ✕
        </button>
    </div>
</div>
<script>
var deferredPrompt;
window.addEventListener('beforeinstallprompt', function(e) {
    e.preventDefault();
    deferredPrompt = e;
    document.getElementById('pwa-install').style.display = 'block';
});
function instalar() {
    document.getElementById('pwa-install').style.display = 'none';
    if (deferredPrompt) { deferredPrompt.prompt(); deferredPrompt = null; }
}
function fechar() { document.getElementById('pwa-install').style.display = 'none'; }
</script>""")

class PWAInstallPlugin(PluginBase):
    name = "pwa_install_btn"
    def setup(self, app): app.include_router(router)
plugin = PWAInstallPlugin()
