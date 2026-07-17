from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase
import random
from datetime import datetime, timedelta
router = APIRouter(prefix="/calendario-humor", tags=["Humor"])
@router.get("", response_class=HTMLResponse)
async def calendario():
    hoje = datetime.now()
    dias = [{"data":(hoje-timedelta(days=i)).strftime("%d/%m"),"humor":random.randint(0,4) if random.random()>0.35 else None} for i in range(364,-1,-1)]
    cores = {None:"#2d2d2d",0:"#e53e3e",1:"#dd6b20",2:"#d69e2e",3:"#38a169",4:"#667eea"}
    labels = {None:"Sem dado",0:"Muito mal",1:"Mal",2:"Neutro",3:"Bem",4:"Muito bem"}
    cells = "".join(f'<div style="width:12px;height:12px;background:{cores.get(d["humor"],"#2d2d2d")};border-radius:2px;cursor:pointer" title="{d["data"]} {labels.get(d["humor"],"")}"></div>' for d in dias)
    reg = len([d for d in dias if d["humor"] is not None])
    med = sum(d["humor"] for d in dias if d["humor"] is not None)/max(1,reg)
    return HTMLResponse(f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Calendario de Humor</title>
<style>body{{font-family:sans-serif;background:#0d1117;color:white;padding:28px;margin:0}}.container{{max-width:900px;margin:0 auto}}h1{{color:#667eea;margin-bottom:6px}}.stats{{display:flex;gap:20px;margin:20px 0;flex-wrap:wrap}}.stat{{background:#161b22;border-radius:12px;padding:16px 24px;border:1px solid #21262d}}.sn{{font-size:28px;font-weight:800;color:#667eea}}.sl{{color:#8b949e;font-size:13px}}.grid{{display:grid;grid-template-columns:repeat(53,14px);gap:2px;margin:20px 0}}.leg{{display:flex;gap:10px;align-items:center;flex-wrap:wrap;color:#8b949e;font-size:13px}}.li{{display:flex;align-items:center;gap:4px}}.lb{{width:12px;height:12px;border-radius:2px}}</style></head>
<body><div class="container">
<a href="/" style="color:#667eea;text-decoration:none">Voltar</a>
<h1 style="margin-top:12px">Calendario de Humor</h1>
<p style="color:#8b949e">Historico dos ultimos 365 dias</p>
<div class="stats">
<div class="stat"><div class="sn">{reg}</div><div class="sl">Dias registrados</div></div>
<div class="stat"><div class="sn">{med:.1f}/4</div><div class="sl">Humor medio</div></div>
</div>
<div class="grid">{cells}</div>
<div class="leg"><span>Menos</span><div class="li"><div class="lb" style="background:#e53e3e"></div><span>Muito mal</span></div><div class="li"><div class="lb" style="background:#d69e2e"></div><span>Neutro</span></div><div class="li"><div class="lb" style="background:#667eea"></div><span>Muito bem</span></div><span>Mais</span></div>
<div style="background:#667eea;border-radius:12px;padding:20px;text-align:center;margin-top:20px">
<p style="margin:0 0 10px">Registre seu humor hoje</p>
<a href="/api/v1/humor/check-in" style="background:white;color:#667eea;padding:12px 24px;border-radius:8px;text-decoration:none;font-weight:700">Fazer check-in</a>
</div></div></body></html>""")
class Plugin(PluginBase):
    name = "calendario_humor_visual"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
