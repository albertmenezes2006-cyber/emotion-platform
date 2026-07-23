from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase

router = APIRouter(tags=["Download"])

@router.get("/baixar", response_class=HTMLResponse)
async def pagina_download():
    return """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Baixar EmotionAI App</title>
    <style>
        body { font-family: sans-serif; background: #f8fafc; display: flex; align-items: center; justify-content: center; min-height: 100vh; margin: 0; }
        .card { background: white; padding: 2rem; border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); text-align: center; max-width: 400px; width: 90%; }
        h1 { color: #667eea; font-size: 1.5rem; margin-bottom: 1rem; }
        p { color: #4a5568; line-height: 1.6; margin-bottom: 2rem; }
        .btn { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 1rem 2rem; border-radius: 50px; text-decoration: none; font-weight: bold; display: inline-block; transition: transform 0.2s; }
        .btn:hover { transform: scale(1.05); }
        .footer { margin-top: 2rem; font-size: 0.8rem; color: #718096; }
    </style>
</head>
<body>
    <div class="card">
        <div style="font-size: 4rem; margin-bottom: 1rem;">🧠</div>
        <h1>Instalar EmotionAI</h1>
        <p>Leve sua prática clínica para o celular. Clique no botão abaixo para baixar o instalador oficial.</p>
        <a href="/static/downloads/emotionai.apk" class="btn">Baixar Agora (APK)</a>
        <div class="footer">✓ Versão 1.0.0 (Oficial)<br>✓ Seguro e Criptografado</div>
    </div>
</body>
</html>"""

class Plugin(PluginBase):
    name = "pagina_download"
    def setup(self, app): app.include_router(router)

plugin = Plugin()
