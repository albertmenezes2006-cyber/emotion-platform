from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase
router = APIRouter(prefix="/act", tags=["ACT"])
@router.get("", response_class=HTMLResponse)
async def act():
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>ACT Terapia</title>
<style>body{font-family:sans-serif;background:#f0fff4;padding:20px;margin:0}.container{max-width:700px;margin:0 auto}.header{background:linear-gradient(135deg,#38a169,#2d6a4f);color:white;border-radius:20px;padding:28px;margin-bottom:24px;text-align:center}.processo{background:white;border-radius:16px;padding:24px;margin-bottom:14px;box-shadow:0 4px 20px rgba(0,0,0,0.08);border-left:5px solid}.ex{border-radius:10px;padding:12px;margin-top:10px;border-left:4px solid}details summary{cursor:pointer;font-weight:700;padding:6px 0;list-style:none}details summary::-webkit-details-marker{display:none}</style></head>
<body><div class="container">
<a href="/" style="color:#38a169;text-decoration:none">Voltar</a>
<div class="header"><h1 style="margin:0 0 8px">ACT</h1><p style="opacity:0.9;margin:0">Terapia de Aceitacao e Compromisso - 6 Processos</p></div>
<div class="processo" style="border-color:#667eea"><h2 style="color:#667eea;margin:0 0 8px">Aceitacao</h2><p style="color:#555">Abrir espaco para pensamentos dificeis sem lutar.</p><details><summary style="color:#667eea">Ver exercicio</summary><div class="ex" style="background:#f0f4ff;border-color:#667eea">Imagine seus pensamentos como ondas do mar. Observe-os chegando e indo.</div></details></div>
<div class="processo" style="border-color:#764ba2"><h2 style="color:#764ba2;margin:0 0 8px">Defusao Cognitiva</h2><p style="color:#555">Criar distancia de pensamentos.</p><details><summary style="color:#764ba2">Ver exercicio</summary><div class="ex" style="background:#f5f3ff;border-color:#764ba2">Diga: Estou tendo o pensamento de que... antes do pensamento dificil.</div></details></div>
<div class="processo" style="border-color:#38a169"><h2 style="color:#38a169;margin:0 0 8px">Momento Presente</h2><p style="color:#555">Estar no aqui e agora com abertura.</p><details><summary style="color:#38a169">Ver exercicio</summary><div class="ex" style="background:#f0fff4;border-color:#38a169">5-4-3-2-1: Nomeie 5 coisas que ve, 4 que toca, 3 que ouve, 2 que cheira, 1 que saboreia.</div></details></div>
<div class="processo" style="border-color:#f59e0b"><h2 style="color:#f59e0b;margin:0 0 8px">Valores</h2><p style="color:#555">Clarificar o que realmente importa.</p><details><summary style="color:#f59e0b">Ver exercicio</summary><div class="ex" style="background:#fefce8;border-color:#f59e0b">Imagine seu funeral. O que gostaria que dissessem de voce?</div></details></div>
<div class="processo" style="border-color:#3182ce"><h2 style="color:#3182ce;margin:0 0 8px">Acao Comprometida</h2><p style="color:#555">Agir de acordo com seus valores.</p><details><summary style="color:#3182ce">Ver exercicio</summary><div class="ex" style="background:#ebf8ff;border-color:#3182ce">Escolha um valor. Defina UMA acao pequena que fara HOJE.</div></details></div>
<div style="text-align:center;padding:20px;background:white;border-radius:16px;box-shadow:0 4px 20px rgba(0,0,0,0.08)"><a href="/api/v1/agenda/pagina" style="background:#38a169;color:white;padding:14px 28px;border-radius:12px;text-decoration:none;font-weight:700">Praticar ACT com psicologo</a></div>
</div></body></html>""")
class Plugin(PluginBase):
    name = "act_terapia_completo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
