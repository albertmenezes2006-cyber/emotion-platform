from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase
from pathlib import Path
import json
from datetime import datetime
router = APIRouter(prefix="/cbt/pensamentos", tags=["CBT"])
ARQ = Path("registros_pensamentos.json")
def load(): return json.loads(ARQ.read_text()) if ARQ.exists() else []
@router.post("/registrar")
async def registrar(request: Request):
    d=await request.json(); r=load()
    r.append({**d,"id":len(r)+1,"data":datetime.utcnow().strftime("%d/%m/%Y %H:%M")})
    ARQ.write_text(json.dumps(r,ensure_ascii=False,indent=2))
    return JSONResponse({"ok":True,"id":len(r)})
@router.get("/listar")
async def listar(): r=load(); return JSONResponse({"registros":r[-10:],"total":len(r)})
@router.get("", response_class=HTMLResponse)
async def pagina():
    return HTMLResponse("""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Registro de Pensamentos CBT</title>
<style>body{font-family:sans-serif;background:#f0f4ff;padding:20px;margin:0}.c{max-width:700px;margin:0 auto}.card{background:white;border-radius:16px;padding:22px;margin-bottom:12px;box-shadow:0 4px 20px rgba(0,0,0,0.08)}.et{background:#e8f0fe;border-radius:8px;padding:5px 12px;font-size:12px;color:#667eea;font-weight:700;margin-bottom:8px;display:inline-block}h2{color:#333;margin:0 0 8px;font-size:16px}textarea{width:100%;padding:12px;border-radius:8px;border:2px solid #e0e0e0;font-size:14px;resize:vertical;height:68px;box-sizing:border-box;font-family:inherit}textarea:focus{border-color:#667eea;outline:none}input[type=range]{width:100%;accent-color:#667eea}button{background:linear-gradient(135deg,#667eea,#764ba2);color:white;border:none;border-radius:12px;padding:14px;font-size:16px;font-weight:700;width:100%;cursor:pointer;margin-top:8px}</style></head>
<body><div class="c"><a href="/" style="color:#667eea;text-decoration:none">Voltar</a>
<h1 style="color:#333;margin:12px 0">Registro de Pensamentos CBT</h1>
<div class="card"><div class="et">Etapa 1</div><h2>Situacao</h2><textarea id="s" placeholder="O que aconteceu? Onde, quando..."></textarea></div>
<div class="card"><div class="et">Etapa 2</div><h2>Pensamento automatico</h2><textarea id="p" placeholder="O que passou pela sua mente?"></textarea>
<p style="color:#666;font-size:13px;margin:6px 0 2px">Crenca: <span id="cv">70%</span></p>
<input type="range" id="c" min="0" max="100" value="70" oninput="document.getElementById('cv').textContent=this.value+'%'"></div>
<div class="card"><div class="et">Etapa 3</div><h2>Emocoes</h2><textarea id="e" placeholder="Quais emocoes sentiu?"></textarea></div>
<div class="card"><div class="et">Etapa 4</div><h2>Evidencias</h2>
<textarea id="f" placeholder="A FAVOR do pensamento..."></textarea>
<textarea id="ct" placeholder="CONTRA o pensamento..." style="margin-top:8px"></textarea></div>
<div class="card"><div class="et">Etapa 5</div><h2>Pensamento alternativo</h2><textarea id="a" placeholder="Reescreva de forma mais equilibrada..."></textarea></div>
<button onclick="salvar()">Salvar registro</button>
</div><script>
function salvar(){
  var d={situacao:document.getElementById("s").value,pensamento:document.getElementById("p").value,crenca:document.getElementById("c").value,emocoes:document.getElementById("e").value,favor:document.getElementById("f").value,contra:document.getElementById("ct").value,alternativo:document.getElementById("a").value};
  if(!d.situacao||!d.pensamento){alert("Preencha situacao e pensamento");return;}
  fetch("/cbt/pensamentos/registrar",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(d)}).then(r=>r.json()).then(function(){alert("Registro salvo!");location.reload();});
}
</script></body></html>""")
class Plugin(PluginBase):
    name = "cbt_thought_record_v2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
