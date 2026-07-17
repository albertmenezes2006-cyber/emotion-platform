from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase
router = APIRouter(prefix="/api/v1/big-five", tags=["Avaliacao"])
@router.get("", response_class=HTMLResponse)
async def big():
    return HTMLResponse("""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Big Five OCEAN</title>
<style>body{font-family:sans-serif;background:#f5f0ff;padding:20px;margin:0}.c{max-width:700px;margin:0 auto}.h{background:linear-gradient(135deg,#7c3aed,#4f46e5);color:white;border-radius:16px;padding:28px;margin-bottom:20px;text-align:center}.q{background:#f8f9fa;border-radius:10px;padding:14px;margin-bottom:10px}label{display:flex;align-items:center;gap:5px;cursor:pointer;padding:3px 0;font-size:13px;color:#555}button{background:linear-gradient(135deg,#7c3aed,#4f46e5);color:white;border:none;border-radius:12px;padding:14px;font-size:16px;font-weight:700;width:100%;cursor:pointer;margin-top:8px}</style></head>
<body><div class="c"><a href="/" style="color:#7c3aed;text-decoration:none">Voltar</a>
<div class="h"><h1 style="margin:0 0 8px">Big Five OCEAN</h1><p style="opacity:0.9;margin:0">Os 5 grandes fatores de personalidade</p></div>
<form onsubmit="calc(event)" id="form"></form>
<div id="res" style="margin-top:20px"></div>
</div><script>
var itens=[["Sou falante e extrovertido(a)","E",false],["Tendo a encontrar defeitos nos outros","A",true],["Faco um trabalho completo","C",false],["Sou deprimido(a) ou melancolico(a)","N",false],["Sou original e tenho novas ideias","O",false],["Sou reservado(a)","E",true],["Sou prestativo(a) e nao egoista","A",false],["Posso ser descuidado(a)","C",true],["Sou relaxado(a) e lido bem com estresse","N",true],["Sou curioso(a) sobre muitas coisas","O",false],["Sou cheio(a) de energia","E",false],["Tenho facilidade de me irritar","A",true],["Sou trabalhador(a) confiavel","C",false],["Posso ser tenso(a) e ansioso(a)","N",false],["Sou engenhoso(a) e penso profundamente","O",false]];
var opts=["Discordo totalmente","Discordo","Neutro","Concordo","Concordo totalmente"];
var form=document.getElementById("form");
itens.forEach(function(it,i){
  var div=document.createElement("div");div.className="q";
  var p=document.createElement("p");p.style="font-weight:600;color:#333;margin:0 0 8px";p.textContent=(i+1)+". "+it[0];
  div.appendChild(p);
  opts.forEach(function(o,j){var l=document.createElement("label");l.innerHTML="<input type='radio' name='q"+i+"' value='"+j+"'> "+o;div.appendChild(l);});
  form.appendChild(div);
});
var btn=document.createElement("button");btn.type="submit";btn.textContent="Ver meu perfil";form.appendChild(btn);
var dims={E:"Extroversao",A:"Amabilidade",C:"Conscienciosidade",N:"Neuroticismo",O:"Abertura"};
var cores={E:"#ef4444",A:"#10b981",C:"#f59e0b",N:"#3b82f6",O:"#8b5cf6"};
function calc(e){e.preventDefault();
  var s={E:0,A:0,C:0,N:0,O:0},n={E:0,A:0,C:0,N:0,O:0};
  for(var i=0;i<15;i++){var r=document.querySelector("input[name='q"+i+"']:checked");if(!r){alert("Responda todas");return;}var v=parseInt(r.value);var it=itens[i];s[it[1]]+=it[2]?(4-v):v;n[it[1]]++;}
  var h="<div style='background:white;border-radius:16px;padding:28px;box-shadow:0 4px 20px rgba(0,0,0,0.1)'><h2 style='color:#7c3aed;margin:0 0 20px'>Seu Perfil Big Five</h2>";
  Object.keys(s).forEach(function(d){var m=s[d]/n[d];var p=(m/4)*100;var nv=m>=3?"Alto":m>=2?"Moderado":"Baixo";
    h+="<div style='margin-bottom:14px'><div style='display:flex;justify-content:space-between;margin-bottom:4px'><strong style='color:"+cores[d]+"'>"+dims[d]+"</strong><span style='color:#888;font-size:13px'>"+nv+" ("+m.toFixed(1)+"/4)</span></div><div style='background:#f0f0f0;border-radius:20px;height:10px;overflow:hidden'><div style='background:"+cores[d]+";height:100%;width:"+p+"%'></div></div></div>";
  });h+="</div>";
  document.getElementById("res").innerHTML=h;window.scrollTo(0,document.getElementById("res").offsetTop-20);
}
</script></body></html>""")
class Plugin(PluginBase):
    name = "big_five_v2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
