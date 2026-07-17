from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase
router = APIRouter(prefix="/dbt", tags=["DBT"])
@router.get("", response_class=HTMLResponse)
async def dbt():
    return HTMLResponse(open("templates/index.html").read() if False else """<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>DBT Skills</title>
<style>body{font-family:sans-serif;background:#f8f9fa;padding:20px;margin:0}.container{max-width:700px;margin:0 auto}.header{background:linear-gradient(135deg,#e53e3e,#c53030);color:white;border-radius:20px;padding:28px;margin-bottom:24px;text-align:center}.modulo{background:white;border-radius:16px;padding:24px;margin-bottom:20px;box-shadow:0 4px 20px rgba(0,0,0,0.08)}details{margin-bottom:10px;border-radius:8px;overflow:hidden;border:1px solid #eee}summary{padding:12px 16px;cursor:pointer;font-weight:600;background:#f8f9fa;list-style:none}summary::-webkit-details-marker{display:none}.detalhe{padding:16px}.ex{border-radius:8px;padding:12px;margin-top:8px;border-left:4px solid}</style></head>
<body><div class="container">
<a href="/" style="color:#e53e3e;text-decoration:none">Voltar</a>
<div class="header"><h1 style="margin:0 0 8px">DBT Skills</h1><p style="opacity:0.9;margin:0">Terapia Comportamental Dialetica</p></div>
<div class="modulo"><h2 style="color:#e53e3e">Mindfulness</h2>
<details><summary>Mente Sabia</summary><div class="detalhe"><p>Equilibrio entre mente emocional e racional.</p><div class="ex" style="background:#f0f4ff;border-color:#667eea">Respire fundo 3x. Pergunte: O que minha mente sabia diria sobre isso?</div></div></details>
<details><summary>Observar sem Julgar</summary><div class="detalhe"><p>Notar experiencias sem avalia-las.</p><div class="ex" style="background:#f0f4ff;border-color:#667eea">Por 5 minutos observe seus pensamentos como nuvens passando.</div></div></details></div>
<div class="modulo"><h2 style="color:#dd6b20">Tolerancia ao Mal-Estar</h2>
<details><summary>TIPP</summary><div class="detalhe"><p>Temperatura, Exercicio, Respiracao, Relaxamento.</p><div class="ex" style="background:#fff7ed;border-color:#dd6b20">Coloque rosto em agua gelada por 30s.</div></div></details>
<details><summary>Aceitacao Radical</summary><div class="detalhe"><p>Aceitar a realidade como ela e.</p><div class="ex" style="background:#fff7ed;border-color:#dd6b20">Repita: Este momento e como deveria ser. Eu aceito.</div></div></details></div>
<div class="modulo"><h2 style="color:#38a169">Regulacao Emocional</h2>
<details><summary>PLEASE</summary><div class="detalhe"><p>tratar doenca Fisica, medicAmento, Alimentacao, Sono, Exercicio.</p><div class="ex" style="background:#f0fff4;border-color:#38a169">Avalie: dormi bem? Comi? Tomei medicacao? Exercitei?</div></div></details>
<details><summary>Acao Oposta</summary><div class="detalhe"><p>Agir de forma oposta a emocao.</p><div class="ex" style="background:#f0fff4;border-color:#38a169">Se com raiva: relaxe, fale devagar, afaste-se.</div></div></details></div>
<div style="text-align:center;padding:20px;background:white;border-radius:16px;box-shadow:0 4px 20px rgba(0,0,0,0.08)"><a href="/api/v1/agenda/pagina" style="background:#e53e3e;color:white;padding:14px 28px;border-radius:12px;text-decoration:none;font-weight:700">Agendar sessao</a></div>
</div></body></html>""")
class Plugin(PluginBase):
    name = "dbt_skills_completo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
