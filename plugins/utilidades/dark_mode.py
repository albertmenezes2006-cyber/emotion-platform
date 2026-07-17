#!/usr/bin/env python3
"""Dark mode toggle"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/api/v1/darkmode", tags=["UI"])

@router.get("/toggle", response_class=HTMLResponse)
async def dark_toggle():
    return HTMLResponse("""
<button id="dark-btn" onclick="toggleDark()"
    style="position:fixed;top:16px;right:16px;background:rgba(0,0,0,0.1);
           border:none;border-radius:50%;width:44px;height:44px;cursor:pointer;
           font-size:20px;z-index:9995;transition:background 0.2s"
    title="Alternar modo escuro">🌙</button>
<style>
body.dark-mode { background: #1a1a2e !important; color: #e0e0e0 !important; }
body.dark-mode .card, body.dark-mode div[style*="background:white"] {
    background: #16213e !important; color: #e0e0e0 !important; }
</style>
<script>
var dark = localStorage.getItem('dark') === '1';
if (dark) { document.body.classList.add('dark-mode'); document.getElementById('dark-btn').textContent = '☀️'; }
function toggleDark() {
    dark = !dark;
    localStorage.setItem('dark', dark ? '1' : '0');
    document.body.classList.toggle('dark-mode');
    document.getElementById('dark-btn').textContent = dark ? '☀️' : '🌙';
}
</script>""")

class DarkPlugin(PluginBase):
    name = "dark_mode"
    def setup(self, app): app.include_router(router)
plugin = DarkPlugin()
