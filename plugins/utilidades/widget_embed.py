#!/usr/bin/env python3
"""Widget embeddable — psicologos colocam no site deles"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, Response
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/widget", tags=["Widget"])

@router.get("/embed.js")
async def widget_js():
    js = """
(function() {
    var btn = document.createElement('div');
    btn.innerHTML = '🧠 Avaliar Humor';
    btn.style.cssText = 'position:fixed;bottom:20px;right:20px;' +
        'background:linear-gradient(135deg,#667eea,#764ba2);' +
        'color:white;padding:12px 20px;border-radius:50px;' +
        'cursor:pointer;font-family:sans-serif;font-weight:700;' +
        'box-shadow:0 4px 15px rgba(102,126,234,0.5);' +
        'z-index:9999;transition:transform 0.2s;font-size:14px;';
    btn.onmouseover = function(){ this.style.transform='scale(1.05)'; };
    btn.onmouseout = function(){ this.style.transform='scale(1)'; };
    btn.onclick = function(){
        window.open('https://emotion-platform-albert.onrender.com/app/avaliacao',
            '_blank','width=500,height=700');
    };
    document.body.appendChild(btn);
})();
"""
    return Response(content=js, media_type="application/javascript")

@router.get("/demo", response_class=HTMLResponse)
async def widget_demo():
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Widget Demo — Emotion Platform</title>
    <style>
        body { font-family: sans-serif; max-width: 800px; margin: 40px auto; padding: 20px; }
        h1 { color: #667eea; }
        .code-box { background: #1a1a2e; color: #00ff88; padding: 20px;
                    border-radius: 12px; font-family: monospace; font-size: 14px; }
        .btn { background: linear-gradient(135deg,#667eea,#764ba2); color: white;
               padding: 12px 24px; border-radius: 8px; border: none;
               cursor: pointer; font-size: 16px; margin-top: 16px; }
    </style>
</head>
<body>
    <h1>🧠 Widget Emotion Platform</h1>
    <p>Adicione este botao ao seu site e seus pacientes podem se avaliar diretamente:</p>

    <div class="code-box">
&lt;script src="https://emotion-platform-albert.onrender.com/widget/embed.js"&gt;&lt;/script&gt;
    </div>

    <button class="btn" onclick="copiar()">📋 Copiar codigo</button>

    <h2 style="margin-top:40px">Preview ao vivo:</h2>
    <div style="height:200px;background:#f0f4ff;border-radius:12px;
                display:flex;align-items:center;justify-content:center;
                color:#888;position:relative;">
        Seu site aqui
    </div>

    <script src="/widget/embed.js"></script>
    <script>
        function copiar() {
            navigator.clipboard.writeText(
                '<script src="https://emotion-platform-albert.onrender.com/widget/embed.js"></script>'
            );
            alert("Copiado!");
        }
    </script>
</body>
</html>""")

class WidgetPlugin(PluginBase):
    name = "widget_embed"
    def setup(self, app):
        app.include_router(router)

plugin = WidgetPlugin()
