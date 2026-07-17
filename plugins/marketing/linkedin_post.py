#!/usr/bin/env python3
"""Gerador de posts para LinkedIn"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse, HTMLResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/api/v1/linkedin", tags=["Marketing"])

POSTS = [
    {
        "titulo": "Lançamento da plataforma",
        "texto": """🧠 Acabei de lançar o Emotion Intelligence Platform — a ferramenta #1 para psicólogos brasileiros!

✅ PHQ-9 e GAD-7 digitais e validados
✅ Chat com IA em português 24h
✅ Prontuário eletrônico completo
✅ Relatórios automáticos em PDF
✅ 100% gratuito para começar

Se você é psicólogo e quer transformar sua prática com tecnologia, acesse:
🔗 emotion-platform-albert.onrender.com

💬 Me conta: você usa alguma ferramenta digital no consultório?

#Psicologia #SaudeMental #InteligenciaArtificial #TecnologiaEmSaude #PsicologiaBrasil"""
    },
    {
        "titulo": "Dica de ferramenta",
        "texto": """💡 3 minutos que podem mudar sua prática clínica:

O PHQ-9 é o instrumento de rastreio de depressão mais usado no mundo.

Mas aplicar manualmente pode levar 20-30 minutos por paciente.

Com o Emotion Platform:
⚡ Aplicação digital em 3 minutos
📊 Score calculado automaticamente  
📈 Evolução visual ao longo do tempo
📋 Relatório PDF gerado na hora

Resultado: você foca no que importa — o paciente.

🔗 Teste grátis: emotion-platform-albert.onrender.com

#Psicologia #PHQ9 #FerramentasParaPsicologos #SaudeMentalDigital"""
    }
]

@router.get("/posts")
async def listar_posts():
    return JSONResponse(POSTS)

@router.get("/pagina", response_class=HTMLResponse)
async def pagina_posts():
    cards = ""
    for i, p in enumerate(POSTS):
        cards += f"""
        <div style="background:white;border-radius:16px;padding:24px;
                    margin-bottom:20px;box-shadow:0 4px 20px rgba(0,0,0,0.08)">
            <h3 style="color:#667eea;margin:0 0 12px">{p['titulo']}</h3>
            <pre id="post{i}" style="white-space:pre-wrap;font-family:sans-serif;
                 color:#555;line-height:1.6;font-size:14px;
                 background:#f8f9fa;padding:16px;border-radius:8px">{p['texto']}</pre>
            <button onclick="copiar('post{i}')"
                style="background:#667eea;color:white;border:none;border-radius:8px;
                       padding:10px 20px;cursor:pointer;font-weight:700;margin-top:12px">
                📋 Copiar post
            </button>
        </div>"""
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<title>Posts LinkedIn — Emotion Platform</title>
<style>body{{font-family:sans-serif;background:#f8f9fa;padding:20px;margin:0}}
.container{{max-width:700px;margin:0 auto}}</style></head><body>
<div class="container">
<a href="/" style="color:#667eea;text-decoration:none">← Voltar</a>
<h1 style="color:#333;margin:16px 0">💼 Posts Prontos para LinkedIn</h1>
<p style="color:#888">Copie e publique no LinkedIn para atrair psicólogos</p>
{cards}
</div>
<script>
function copiar(id){{
  var texto=document.getElementById(id).textContent;
  navigator.clipboard.writeText(texto).then(function(){{
    alert("✅ Copiado! Cole no LinkedIn agora.");
  }});
}}
</script></body></html>""")

class LinkedInPlugin(PluginBase):
    name = "linkedin_posts"
    def setup(self, app): app.include_router(router)
plugin = LinkedInPlugin()
