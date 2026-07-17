from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase
router = APIRouter(prefix="/plano-seguranca", tags=["Crise"])
@router.get("", response_class=HTMLResponse)
async def plano():
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Plano de Seguranca</title>
<style>body{font-family:sans-serif;background:#fff5f5;padding:20px;margin:0}.container{max-width:600px;margin:0 auto}.urgente{background:#e53e3e;color:white;border-radius:16px;padding:24px;margin-bottom:20px}.card{background:white;border-radius:14px;padding:20px;margin-bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,0.08)}h2{color:#333;margin:0 0 10px;font-size:16px}input,textarea{width:100%;padding:10px;border-radius:8px;border:2px solid #eee;font-size:14px;box-sizing:border-box;margin-bottom:6px;font-family:inherit}input:focus,textarea:focus{border-color:#667eea;outline:none}.bc{display:block;border-radius:10px;padding:14px;text-align:center;text-decoration:none;font-weight:800;font-size:17px;margin-bottom:8px}.bs{background:#667eea;color:white;border:none;border-radius:12px;padding:14px;font-size:16px;font-weight:700;width:100%;cursor:pointer}</style></head>
<body><div class="container">
<div class="urgente"><h1 style="margin:0 0 8px">Plano de Seguranca</h1>
<p style="margin:0 0 12px">Em crise AGORA? Ligue imediatamente:</p>
<a href="tel:188" class="bc" style="background:white;color:#e53e3e">CVV 188 - 24h Gratuito</a>
<a href="tel:192" class="bc" style="background:rgba(255,255,255,0.2);color:white">SAMU 192</a></div>
<div class="card"><h2>1. Meus sinais de alerta</h2><textarea id="sinais" rows="3" placeholder="O que percebo antes de uma crise?"></textarea></div>
<div class="card"><h2>2. O que me ajuda internamente</h2><textarea id="interno" rows="3" placeholder="Ex: respiracao profunda, musica..."></textarea></div>
<div class="card"><h2>3. Pessoas que posso contatar</h2><input id="c1" placeholder="Nome - Telefone"><input id="c2" placeholder="Nome - Telefone"><input id="c3" placeholder="Psicologo - Telefone"></div>
<div class="card"><h2>4. Razoes para continuar</h2><textarea id="razoes" rows="3" placeholder="O que torna sua vida valiosa?"></textarea></div>
<button class="bs" onclick="salvar()">Salvar meu plano</button>
</div>
<script>
function salvar(){var d={sinais:document.getElementById("sinais").value,interno:document.getElementById("interno").value,c1:document.getElementById("c1").value,c2:document.getElementById("c2").value,c3:document.getElementById("c3").value,razoes:document.getElementById("razoes").value};localStorage.setItem("plano_seg",JSON.stringify(d));alert("Plano salvo!");}
var s=localStorage.getItem("plano_seg");if(s){var p=JSON.parse(s);["sinais","interno","c1","c2","c3","razoes"].forEach(function(k){var el=document.getElementById(k);if(el)el.value=p[k]||"";});}
</script></body></html>""")
class Plugin(PluginBase):
    name = "plano_seguranca_crise"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
