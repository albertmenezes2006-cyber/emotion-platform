#!/usr/bin/env python3
"""Desafio 21 dias"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/desafio-21", tags=["Gamificacao"])

@router.get("", response_class=HTMLResponse)
async def pagina_desafio():
    dias = [
        {"dia":1,"titulo":"Respiracao","tarefa":"Pratique box breathing por 5 min","icone":"🫁"},
        {"dia":2,"titulo":"Gratidao","tarefa":"Escreva 3 coisas boas do dia","icone":"🙏"},
        {"dia":3,"titulo":"Movimento","tarefa":"Caminhe por 20 minutos","icone":"🚶"},
        {"dia":4,"titulo":"Hidratacao","tarefa":"Beba 2L de agua hoje","icone":"💧"},
        {"dia":5,"titulo":"Leitura","tarefa":"Leia por 15 minutos","icone":"📚"},
        {"dia":6,"titulo":"Meditacao","tarefa":"Medite por 10 minutos","icone":"🧘"},
        {"dia":7,"titulo":"Descanso","tarefa":"Durma 8 horas esta noite","icone":"😴"},
        {"dia":8,"titulo":"Alimentacao","tarefa":"Coma uma refeicao saudavel","icone":"🥗"},
        {"dia":9,"titulo":"Conexao","tarefa":"Ligue para alguem querido","icone":"📞"},
        {"dia":10,"titulo":"Criatividade","tarefa":"Desenhe ou escreva algo","icone":"✍️"},
        {"dia":11,"titulo":"Natureza","tarefa":"Passe 20 min ao ar livre","icone":"🌿"},
        {"dia":12,"titulo":"Diario","tarefa":"Escreva no diario emocional","icone":"📓"},
        {"dia":13,"titulo":"Silencio","tarefa":"10 min sem telas ou barulho","icone":"🔇"},
        {"dia":14,"titulo":"Alongamento","tarefa":"Faca 10 min de alongamento","icone":"🤸"},
        {"dia":15,"titulo":"Aprendizado","tarefa":"Aprenda algo novo hoje","icone":"🎓"},
        {"dia":16,"titulo":"Gentileza","tarefa":"Faca um ato gentil","icone":"💝"},
        {"dia":17,"titulo":"Organizacao","tarefa":"Organize um espaco da casa","icone":"🏠"},
        {"dia":18,"titulo":"Autocuidado","tarefa":"Faca algo so para voce","icone":"🛁"},
        {"dia":19,"titulo":"Reflexao","tarefa":"Reflita sobre seu progresso","icone":"🪞"},
        {"dia":20,"titulo":"Celebracao","tarefa":"Comemore suas conquistas","icone":"🎉"},
        {"dia":21,"titulo":"Compromisso","tarefa":"Planeje continuar os habitos","icone":"🏆"},
    ]
    cards = ""
    for d in dias:
        cards += f"""
        <div style="background:white;border-radius:12px;padding:16px;margin:8px 0;border:1px solid #eee;display:flex;align-items:center;gap:16px">
          <div style="font-size:32px">{d["icone"]}</div>
          <div>
            <div style="font-weight:700">Dia {d["dia"]}: {d["titulo"]}</div>
            <div style="color:#666;font-size:13px">{d["tarefa"]}</div>
          </div>
          <div style="margin-left:auto">
            <button onclick="completar({d["dia"]})" style="background:#667eea;color:white;border:none;border-radius:8px;padding:8px 14px;cursor:pointer">
              Completar
            </button>
          </div>
        </div>"""

    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Desafio 21 Dias</title>
<style>
body{{font-family:sans-serif;max-width:700px;margin:40px auto;padding:20px;background:#f8f9fa}}
h1{{color:#333}}
</style>
</head>
<body>
<a href="/" style="color:#667eea">← Voltar</a>
<h1>🔥 Desafio 21 Dias</h1>
<p>Complete um habito por dia durante 21 dias!</p>
{cards}
<script>
function completar(dia) {{
  fetch("/desafio-21/completar/" + dia, {{method:"POST", headers:{{"Content-Type":"application/json"}}, body:"{{}}" }})
    .then(function(r){{ return r.json(); }})
    .then(function(d){{ alert("Dia " + dia + " completado! Parabens!"); }})
    .catch(function(e){{ alert("Dia " + dia + " completado!"); }});
}}
</script>
</body>
</html>""")

@router.post("/completar/{dia}")
async def completar_dia(dia: int):
    return JSONResponse({"ok": True, "dia": dia, "xp_ganho": dia * 10})

class Desafio21Plugin(PluginBase):
    name = "desafio_21_dias_v2"
    def setup(self, app): app.include_router(router)
plugin = Desafio21Plugin()
