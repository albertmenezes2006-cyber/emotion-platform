from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase
from pathlib import Path
from datetime import datetime
import json

router_l = APIRouter(prefix="/api/v1/lembretes", tags=["Lembretes"])
router_x = APIRouter(prefix="/api/v1/xp", tags=["XP"])
AL = Path("lembretes_fix.json")
AX = Path("xp_fix.json")

def jload(p, d):
    try: return json.loads(p.read_text()) if p.exists() else d
    except: return d
def jsave(p, d): p.write_text(json.dumps(d, ensure_ascii=False, indent=2))

@router_l.post("/criar")
async def criar_l(request: Request):
    d = await request.json()
    data = jload(AL, [])
    data.append({"id": len(data)+1, "titulo": d.get("titulo",""), "horario": d.get("horario",""), "dias": d.get("dias",[]), "ativo": True})
    jsave(AL, data)
    return JSONResponse({"ok": True, "total": len(data)})

@router_l.get("/listar")
async def listar_l(): return JSONResponse({"lembretes": jload(AL, [])})

@router_l.get("/pagina", response_class=HTMLResponse)
async def pagina_l():
    ls = jload(AL, [])
    cards = "".join(f'<div style="background:white;border-radius:12px;padding:16px;margin-bottom:10px;box-shadow:0 2px 8px rgba(0,0,0,0.06);display:flex;justify-content:space-between;align-items:center;border-left:4px solid #667eea"><div><div style="font-weight:700;color:#333">{x["titulo"]}</div><div style="color:#888;font-size:13px">{x.get("horario","")}</div></div><span style="background:#e8f0fe;color:#667eea;padding:4px 10px;border-radius:20px;font-size:12px">Ativo</span></div>' for x in ls)
    dias_html = "".join(f'<div class="dia" onclick="td(this,\'{d}\')">{d}</div>' for d in ["Seg","Ter","Qua","Qui","Sex","Sab","Dom"])
    return HTMLResponse(f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Lembretes</title>
<style>body{{font-family:sans-serif;background:#f0f4ff;padding:20px;margin:0}}.c{{max-width:600px;margin:0 auto}}.form{{background:white;border-radius:16px;padding:22px;margin-bottom:18px;box-shadow:0 4px 20px rgba(0,0,0,0.08)}}input{{width:100%;padding:10px;border-radius:8px;border:2px solid #e0e0e0;margin-bottom:8px;font-size:14px;box-sizing:border-box}}input:focus{{border-color:#667eea;outline:none}}.dias{{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:8px}}.dia{{background:#f0f4ff;border:2px solid #e0e0e0;border-radius:8px;padding:6px 10px;cursor:pointer;font-size:13px;font-weight:600;color:#667eea}}.dia.s{{background:#667eea;color:white;border-color:#667eea}}button{{background:linear-gradient(135deg,#667eea,#764ba2);color:white;border:none;border-radius:12px;padding:12px;font-size:15px;font-weight:700;width:100%;cursor:pointer}}</style></head>
<body><div class="c"><a href="/" style="color:#667eea;text-decoration:none">Voltar</a>
<h1 style="color:#333;margin:12px 0">Lembretes</h1>
<div class="form"><input type="text" id="tt" placeholder="Titulo do lembrete"><input type="time" id="hr">
<div class="dias">{dias_html}</div><button onclick="criar()">Criar lembrete</button></div>
<h2 style="color:#333;margin-bottom:12px">Meus lembretes</h2>
{cards if cards else "<p style='color:#888'>Nenhum lembrete ainda.</p>"}
</div><script>
var ds=[];
function td(el,d){{el.classList.toggle("s");if(ds.includes(d))ds=ds.filter(x=>x!==d);else ds.push(d);}}
function criar(){{var t=document.getElementById("tt").value;if(!t){{alert("Digite o titulo");return;}}
fetch("/api/v1/lembretes/criar",{{method:"POST",headers:{{"Content-Type":"application/json"}},body:JSON.stringify({{titulo:t,horario:document.getElementById("hr").value,dias:ds}})}}).then(()=>location.reload());}}
</script></body></html>""")

NIVEIS = [{"nivel":1,"nome":"Iniciante","xp_min":0,"icone":"🌱"},{"nivel":2,"nome":"Explorador","xp_min":100,"icone":"🔍"},{"nivel":3,"nome":"Expert","xp_min":300,"icone":"⭐"},{"nivel":4,"nome":"Mestre","xp_min":600,"icone":"🏆"},{"nivel":5,"nome":"Lenda","xp_min":1000,"icone":"👑"}]
ACOES = {"avaliacao_phq9":50,"avaliacao_gad7":50,"entrada_diario":20,"chat_ia":10,"login_diario":5,"indicar_amigo":200}

def get_nivel(xp):
    n=NIVEIS[0]
    for nv in NIVEIS:
        if xp>=nv["xp_min"]: n=nv
    return n

@router_x.post("/ganhar/{uid}/{acao}")
async def ganhar(uid:str,acao:str):
    p=ACOES.get(acao,10); d=jload(AX,{})
    if uid not in d: d[uid]={"xp":0,"acoes":[]}
    d[uid]["xp"]+=p; d[uid]["acoes"].append({"acao":acao,"xp":p,"ts":datetime.utcnow().isoformat()})
    jsave(AX,d)
    return JSONResponse({"xp_ganho":p,"xp_total":d[uid]["xp"],"nivel":get_nivel(d[uid]["xp"])})

@router_x.get("/perfil/{uid}")
async def perfil(uid:str):
    d=jload(AX,{}); u=d.get(uid,{"xp":0,"acoes":[]})
    return JSONResponse({"xp_total":u["xp"],"nivel":get_nivel(u["xp"]),"acoes":ACOES})

@router_x.get("/ranking")
async def ranking():
    d=jload(AX,{}); r=sorted(d.items(),key=lambda x:x[1]["xp"],reverse=True)[:10]
    return JSONResponse([{"user":u,"xp":dd["xp"],"nivel":get_nivel(dd["xp"])} for u,dd in r])

class Plugin(PluginBase):
    name = "aaa_lembretes_xp_fix"
    def setup(self, app):
        app.include_router(router_l)
        app.include_router(router_x)

plugin = Plugin()
