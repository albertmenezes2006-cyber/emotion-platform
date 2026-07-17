from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase
from pathlib import Path
import json
from datetime import datetime
router = APIRouter(prefix="/api/v1/lembretes", tags=["Lembretes"])
ARQ = Path("lembretes.json")
def load(): return json.loads(ARQ.read_text()) if ARQ.exists() else []
@router.post("/criar")
async def criar(request: Request):
    d=await request.json(); l=load()
    l.append({"id":len(l)+1,"titulo":d.get("titulo",""),"horario":d.get("horario",""),"dias":d.get("dias",[]),"ativo":True})
    ARQ.write_text(json.dumps(l,ensure_ascii=False,indent=2))
    return JSONResponse({"ok":True,"total":len(l)})
@router.get("/listar")
async def listar(): return JSONResponse({"lembretes":load()})
@router.get("/pagina", response_class=HTMLResponse)
async def pagina():
    ls=load()
    cards="".join(f'<div style="background:white;border-radius:12px;padding:16px;margin-bottom:10px;box-shadow:0 2px 8px rgba(0,0,0,0.06);display:flex;justify-content:space-between;align-items:center;border-left:4px solid #667eea"><div><div style="font-weight:700;color:#333">{x["titulo"]}</div><div style="color:#888;font-size:13px">Horario: {x.get("horario","N/A")}</div></div><span style="background:#e8f0fe;color:#667eea;padding:4px 10px;border-radius:20px;font-size:12px">Ativo</span></div>' for x in ls)
    return HTMLResponse(f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Lembretes</title>
<style>body{{font-family:sans-serif;background:#f0f4ff;padding:20px;margin:0}}.c{{max-width:600px;margin:0 auto}}.form{{background:white;border-radius:16px;padding:22px;margin-bottom:18px;box-shadow:0 4px 20px rgba(0,0,0,0.08)}}input{{width:100%;padding:10px;border-radius:8px;border:2px solid #e0e0e0;margin-bottom:8px;font-size:14px;box-sizing:border-box}}input:focus{{border-color:#667eea;outline:none}}.dias{{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:8px}}.dia{{background:#f0f4ff;border:2px solid #e0e0e0;border-radius:8px;padding:6px 10px;cursor:pointer;font-size:13px;font-weight:600;color:#667eea}}.dia.s{{background:#667eea;color:white;border-color:#667eea}}button{{background:linear-gradient(135deg,#667eea,#764ba2);color:white;border:none;border-radius:12px;padding:12px;font-size:15px;font-weight:700;width:100%;cursor:pointer}}</style></head>
<body><div class="c"><a href="/" style="color:#667eea;text-decoration:none">Voltar</a>
<h1 style="color:#333;margin:12px 0">Lembretes</h1>
<div class="form">
<input type="text" id="titulo" placeholder="Ex: Fazer avaliacao PHQ-9">
<input type="time" id="horario">
<div class="dias" id="dc">{"".join(f'<div class="dia" onclick="td(this,'{d}')">{d}</div>' for d in ["Seg","Ter","Qua","Qui","Sex","Sab","Dom"])}</div>
<button onclick="criar()">Criar lembrete</button></div>
<h2 style="color:#333;margin-bottom:12px">Meus Lembretes</h2>
{cards if cards else "<p style='color:#888'>Nenhum lembrete ainda.</p>"}
</div><script>
var ds=[];
function td(el,d){{el.classList.toggle("s");if(ds.includes(d))ds=ds.filter(x=>x!==d);else ds.push(d);}}
function criar(){{var t=document.getElementById("titulo").value;if(!t){{alert("Digite o titulo");return;}}
fetch("/api/v1/lembretes/criar",{{method:"POST",headers:{{"Content-Type":"application/json"}},body:JSON.stringify({{titulo:t,horario:document.getElementById("horario").value,dias:ds}})}}).then(()=>location.reload());}}
</script></body></html>""")
class Plugin(PluginBase):
    name = "lembretes_v2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
