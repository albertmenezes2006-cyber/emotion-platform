#!/usr/bin/env python3
"""Desafio de 21 dias para habitos saudaveis"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime, timedelta
import json
from pathlib import Path

router = APIRouter(prefix="/desafio-21", tags=["Gamificação"])
ARQUIVO = Path("desafio_21_progresso.json")

DIAS = [
    {"dia": 1, "titulo": "Respiração consciente", "tarefa": "Faça 5 minutos de respiração 4-7-8", "icone": "🫁"},
    {"dia": 2, "titulo": "Gratidão", "tarefa": "Escreva 3 coisas pelas quais é grato", "icone": "💛"},
    {"dia": 3, "titulo": "Movimento", "tarefa": "30 minutos de caminhada consciente", "icone": "🚶"},
    {"dia": 4, "titulo": "Conexão social", "tarefa": "Ligue para alguém que você gosta", "icone": "📞"},
    {"dia": 5, "titulo": "Diário emocional", "tarefa": "Escreva sobre seus sentimentos hoje", "icone": "📔"},
    {"dia": 6, "titulo": "Alimentação consciente", "tarefa": "Faça uma refeição sem celular ou TV", "icone": "🥗"},
    {"dia": 7, "titulo": "Sono reparador", "tarefa": "Durma às 22h e acorde às 6h", "icone": "🌙"},
    {"dia": 8, "titulo": "Meditação", "tarefa": "10 minutos de meditação guiada", "icone": "🧘"},
    {"dia": 9, "titulo": "Natureza", "tarefa": "Passe 20 minutos em um parque ou jardim", "icone": "🌿"},
    {"dia": 10, "titulo": "Autocompaixão", "tarefa": "Escreva uma carta gentil para si mesmo", "icone": "💙"},
    {"dia": 11, "titulo": "Criatividade", "tarefa": "Desenhe, pinte, escreva ou cante", "icone": "🎨"},
    {"dia": 12, "titulo": "Presente", "tarefa": "Sem celular por 2 horas completas", "icone": "📵"},
    {"dia": 13, "titulo": "Bondade", "tarefa": "Faça uma gentileza para alguém", "icone": "🤝"},
    {"dia": 14, "titulo": "Revisão da semana", "tarefa": "Avalie seu progresso nas últimas 2 semanas", "icone": "📊"},
    {"dia": 15, "titulo": "Metas pessoais", "tarefa": "Defina 3 metas para os próximos 30 dias", "icone": "🎯"},
    {"dia": 16, "titulo": "Leitura", "tarefa": "Leia 30 minutos de um livro que você gosta", "icone": "📚"},
    {"dia": 17, "titulo": "Exercício intenso", "tarefa": "20 minutos de exercício aeróbico", "icone": "🏃"},
    {"dia": 18, "titulo": "Organização", "tarefa": "Organize um espaço da sua casa", "icone": "🏠"},
    {"dia": 19, "titulo": "Aprendizado", "tarefa": "Aprenda algo novo por 30 minutos", "icone": "🧠"},
    {"dia": 20, "titulo": "Descanso ativo", "tarefa": "Faça algo prazeroso sem culpa", "icone": "😊"},
    {"dia": 21, "titulo": "Celebração", "tarefa": "Comemore sua jornada! Você conseguiu!", "icone": "🎉"},
]

def carregar():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text())
    return {}

@router.post("/completar/{dia}")
async def completar_dia(dia: int, request: Request):
    dados = carregar()
    user = "default"
    if user not in dados:
        dados[user] = {"inicio": datetime.utcnow().isoformat(), "dias_completos": []}
    if dia not in dados[user]["dias_completos"]:
        dados[user]["dias_completos"].append(dia)
    ARQUIVO.write_text(json.dumps(dados, ensure_ascii=False, indent=2))
    xp = dia * 10
    return JSONResponse({"ok": True, "dia": dia, "xp_ganho": xp,
                         "total_dias": len(dados[user]["dias_completos"]),
                         "concluido": len(dados[user]["dias_completos"]) >= 21})

@router.get("/", response_class=HTMLResponse)
async def pagina_desafio():
    dados = carregar()
    completos = dados.get("default", {}).get("dias_completos", [])
    progresso = len(completos)
    cards = ""
    for d in DIAS:
        feito = d["dia"] in completos
        disponivel = d["dia"] <= progresso + 1
        cards += f"""
        <div style="background:{'#e8f5e9' if feito else 'white'};border-radius:14px;padding:18px;
                    display:flex;align-items:center;gap:14px;margin-bottom:10px;
                    box-shadow:0 2px 8px rgba(0,0,0,0.06);
                    opacity:{1 if disponivel else 0.5};
                    border:2px solid {'#38a169' if feito else '#eee'}">
          <div style="font-size:28px">{d['icone']}</div>
          <div style="flex:1">
            <div style="font-weight:700;color:#333">Dia {d['dia']}: {d['titulo']}</div>
            <div style="color:#666;font-size:13px;margin-top:2px">{d['tarefa']}</div>
          </div>
          {'<div style="color:#38a169;font-size:20px;font-weight:700">✓</div>' if feito else
           f'<button onclick="completar({d[\"dia\"]})" style="background:#667eea;color:white;border:none;border-radius:8px;padding:8px 14px;cursor:pointer;font-weight:700;font-size:13px" {"" if disponivel else "disabled"}>Completar</button>'}
        </div>"""
    pct = int(progresso/21*100)
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Desafio 21 Dias — Emotion Platform</title>
<style>body{{font-family:sans-serif;background:#f0f4ff;padding:20px;margin:0}}
.container{{max-width:600px;margin:0 auto}}
.header{{background:linear-gradient(135deg,#667eea,#764ba2);color:white;border-radius:20px;padding:28px;margin-bottom:24px;text-align:center}}
.prog{{background:rgba(255,255,255,0.2);border-radius:20px;height:12px;overflow:hidden;margin:12px 0}}
.prog-bar{{background:white;height:100%;border-radius:20px;transition:width 0.5s;width:{pct}%}}
</style></head><body><div class="container">
<a href="/" style="color:#667eea;text-decoration:none">← Voltar</a>
<div class="header">
  <h1 style="margin:0 0 8px">🔥 Desafio 21 Dias</h1>
  <p style="opacity:0.9;margin:0 0 12px">Construa hábitos saudáveis de saúde mental</p>
  <div class="prog"><div class="prog-bar"></div></div>
  <div style="font-size:24px;font-weight:800">{progresso}/21 dias · {pct}%</div>
</div>
{cards}
</div><script>
function completar(dia){{
  fetch("/desafio-21/completar/"+dia,{method:"POST",headers:{"Content-Type":"application/json"},body:"{}"})
  .then(r=>r.json()).then(function(d){{
    var msg="✅ Dia "+dia+" concluído! +"+d.xp_ganho+" XP";
    if(d.concluido) msg+="\n🎉 PARABÉNS! Você completou o desafio de 21 dias!";
    alert(msg);location.reload();
  }});
}}
</script></body></html>""")

class Desafio21Plugin(PluginBase):
    name = "desafio_21_dias_completo"
    def setup(self, app): app.include_router(router)
plugin = Desafio21Plugin()
