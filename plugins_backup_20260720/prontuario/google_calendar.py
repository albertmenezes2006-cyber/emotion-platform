#!/usr/bin/env python3
"""Integracao com Google Calendar"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse, HTMLResponse
from plugins.plugin_base import PluginBase
from datetime import datetime, timedelta
import urllib.parse

router = APIRouter(prefix="/api/v1/calendar", tags=["Calendar"])

def gerar_link_google_calendar(titulo: str, data: str, hora: str,
                                duracao_min: int = 60, descricao: str = "") -> str:
    try:
        dt_str = f"{data.replace('-','')}T{hora.replace(':','')}00"
        dt_obj = datetime.strptime(f"{data} {hora}", "%Y-%m-%d %H:%M")
        dt_fim = dt_obj + timedelta(minutes=duracao_min)
        dt_fim_str = dt_fim.strftime("%Y%m%dT%H%M%S")
        params = {
            "action": "TEMPLATE",
            "text": titulo,
            "dates": f"{dt_str}/{dt_fim_str}",
            "details": descricao or f"Sessão agendada pelo Emotion Platform",
            "location": "https://emotion-platform-albert.onrender.com"
        }
        return "https://calendar.google.com/calendar/render?" + urllib.parse.urlencode(params)
    except:
        return "https://calendar.google.com"

@router.get("/link")
async def link_calendar(titulo: str = "Sessão terapêutica",
                         data: str = "2026-08-01", hora: str = "10:00",
                         duracao: int = 60):
    link = gerar_link_google_calendar(titulo, data, hora, duracao)
    return JSONResponse({"link": link, "titulo": titulo, "data": data,
                         "hora": hora, "duracao_min": duracao})

@router.get("/pagina", response_class=HTMLResponse)
async def pagina_calendar():
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<title>Agendar no Google Calendar</title>
<style>body{font-family:sans-serif;background:#f8f9fa;padding:20px;margin:0}
.card{background:white;border-radius:16px;padding:32px;max-width:500px;margin:0 auto;
      box-shadow:0 4px 20px rgba(0,0,0,0.08)}
h1{color:#333;margin:0 0 20px} label{display:block;margin:12px 0 4px;font-weight:600;color:#444}
input{width:100%;padding:10px;border-radius:8px;border:2px solid #e0e0e0;
  font-size:14px;box-sizing:border-box}
input:focus{border-color:#667eea;outline:none}
.btn{display:block;background:linear-gradient(135deg,#667eea,#764ba2);color:white;
  padding:14px;border-radius:12px;text-align:center;text-decoration:none;
  font-weight:700;font-size:16px;margin-top:20px}</style>
</head><body>
<div class="card">
<h1>📅 Agendar no Google Calendar</h1>
<label>Título da sessão</label>
<input type="text" id="titulo" value="Sessão terapêutica">
<label>Data</label>
<input type="date" id="data">
<label>Hora</label>
<input type="time" id="hora" value="10:00">
<label>Duração (minutos)</label>
<input type="number" id="duracao" value="60" min="30" max="180">
<a id="link-btn" href="#" class="btn" onclick="abrir()">
  📅 Abrir no Google Calendar
</a>
</div>
<script>
function abrir(){
  var titulo=encodeURIComponent(document.getElementById("titulo").value);
  var data=document.getElementById("data").value;
  var hora=document.getElementById("hora").value;
  var dur=document.getElementById("duracao").value;
  if(!data){alert("Selecione uma data");return false;}
  window.open("/api/v1/calendar/link?titulo="+titulo+"&data="+data+"&hora="+hora+"&duracao="+dur);
  return false;
}
</script></body></html>""")

class CalendarPlugin(PluginBase):
    name = "google_calendar_integration"
    def setup(self, app): app.include_router(router)
plugin = CalendarPlugin()
