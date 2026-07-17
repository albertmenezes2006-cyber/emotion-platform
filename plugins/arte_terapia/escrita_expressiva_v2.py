from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase
from pathlib import Path
import json
from datetime import datetime
router = APIRouter(prefix="/escrita-expressiva", tags=["Escrita"])
ARQ = Path("escrita_expressiva.json")
def load(): return json.loads(ARQ.read_text()) if ARQ.exists() else []
@router.post("/salvar")
async def salvar(request: Request):
    d=await request.json(); e=load()
    e.append({**d,"data":datetime.utcnow().strftime("%d/%m/%Y"),"palavras":len(d.get("texto","").split())})
    ARQ.write_text(json.dumps(e,ensure_ascii=False,indent=2))
    return JSONResponse({"ok":True,"total_dias":len(e)})
@router.get("", response_class=HTMLResponse)
async def pagina():
    entradas=load(); dia=min(len(entradas)+1,3)
    instrucoes={1:"Escreva sobre o evento mais perturbador da sua vida. Inclua seus sentimentos mais profundos. Nao se preocupe com gramatica.",2:"Continue sobre o mesmo evento. Explore como se relaciona com outras partes da sua vida, passado e futuro.",3:"Escreva o que aprendeu e como cresceu a partir dessa experiencia. Como se sente sobre ela hoje?"}
    inst=instrucoes.get(dia,instrucoes[1])
    feitos=len(entradas)
    return HTMLResponse(f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Escrita Expressiva</title>
<style>body{{font-family:sans-serif;background:#f8f4ff;padding:20px;margin:0}}.c{{max-width:700px;margin:0 auto}}.h{{background:linear-gradient(135deg,#7c3aed,#a855f7);color:white;border-radius:16px;padding:28px;margin-bottom:22px}}.dias{{display:flex;gap:8px;margin-bottom:16px}}.dia{{background:#f0e6ff;border:2px solid #e0c8ff;border-radius:8px;padding:8px 14px;font-size:13px;font-weight:700;color:#7c3aed}}.dia.a{{background:#7c3aed;color:white;border-color:#7c3aed}}.dia.f{{background:#e8f5e9;border-color:#4caf50;color:#2e7d32}}.inst{{background:white;border-radius:12px;padding:18px;margin-bottom:14px;box-shadow:0 2px 8px rgba(0,0,0,0.06);border-left:4px solid #7c3aed}}textarea{{width:100%;padding:14px;border-radius:12px;border:2px solid #e0e0e0;font-size:15px;resize:vertical;min-height:180px;box-sizing:border-box;font-family:inherit;line-height:1.7}}textarea:focus{{border-color:#7c3aed;outline:none}}.cnt{{color:#888;font-size:13px;text-align:right;margin-top:4px}}button{{background:linear-gradient(135deg,#7c3aed,#a855f7);color:white;border:none;border-radius:12px;padding:14px;font-size:16px;font-weight:700;width:100%;cursor:pointer;margin-top:8px}}.sci{{background:#e8f5e9;border-radius:12px;padding:14px;margin-top:14px;border-left:4px solid #38a169}}</style></head>
<body><div class="c"><a href="/" style="color:#7c3aed;text-decoration:none">Voltar</a>
<div class="h"><h1 style="margin:0 0 6px">Escrita Expressiva</h1><p style="opacity:0.9;margin:0">Protocolo Pennebaker - 3 dias, 20min por dia</p></div>
<div class="dias">{"".join(f'<div class="dia {"f" if i<feitos else "a" if i+1==dia else ""}">Dia {i+1} {"✓" if i<feitos else ""}</div>' for i in range(3))}</div>
{"<h2 style='color:#2e7d32;text-align:center;padding:20px'>Protocolo Completo! Parabens!</h2>" if feitos>=3 else f'<div class="inst"><h2 style="color:#7c3aed;margin:0 0 8px">Dia {dia} de 3</h2><p style="color:#555;margin:0;line-height:1.7">{inst}</p></div><textarea id="txt" placeholder="Escreva livremente por 20 minutos..." oninput="cnt()"></textarea><div class="cnt" id="cnt">0 palavras</div><button onclick="salvar()">Salvar Dia {dia}</button>'}
<div class="sci"><strong style="color:#2e7d32">Por que funciona?</strong><p style="color:#555;font-size:14px;margin:6px 0 0">Escrita expressiva reduz visitas medicas em 50%, melhora humor e fortalece imunidade (Pennebaker, 1986-2020).</p></div>
</div><script>
var ini=Date.now();
function cnt(){{var t=document.getElementById("txt");if(!t)return;var p=t.value.trim()?t.value.trim().split(/\s+/).length:0;document.getElementById("cnt").textContent=p+" palavras - "+Math.floor((Date.now()-ini)/60000)+"min";}}
function salvar(){{var el=document.getElementById("txt");if(!el)return;var txt=el.value;if(txt.trim().split(/\s+/).length<30){{alert("Escreva pelo menos 30 palavras");return;}}
fetch("/escrita-expressiva/salvar",{{method:"POST",headers:{{"Content-Type":"application/json"}},body:JSON.stringify({{"dia":{dia},"texto":txt}})}}).then(r=>r.json()).then(function(){{alert("Dia {dia} salvo! Volte amanha.");location.reload();}});}}
</script></body></html>""")
class Plugin(PluginBase):
    name = "escrita_expressiva_v2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
