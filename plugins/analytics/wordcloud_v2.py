from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase
import re
from collections import Counter
router = APIRouter(prefix="/api/v1/wordcloud", tags=["Analytics"])
SW = {"de","a","o","que","e","do","da","em","um","para","com","uma","os","no","se","na","por","mas","foi","ao","ele","das","tem","seu","sua","ou","ser","quando","muito","ja","esta","eu","tambem","so","pelo"}
@router.post("/gerar")
async def gerar(request: Request):
    d=await request.json(); ws=[]
    for t in d.get("textos",[]): ws.extend([w for w in re.findall(r"[a-z]{4,}",t.lower()) if w not in SW])
    c=Counter(ws).most_common(25)
    return JSONResponse({"palavras":[{"palavra":p,"count":n} for p,n in c]})
@router.get("/demo", response_class=HTMLResponse)
async def demo():
    pals=[("ansioso",15),("triste",12),("esperanca",10),("melhora",9),("cansado",8),("gratidao",8),("familia",7),("sono",6),("progresso",6),("calmo",5),("superacao",5),("conquista",4),("paz",3)]
    mx=pals[0][1]; cores=["#667eea","#764ba2","#38a169","#e53e3e","#f59e0b","#3182ce"]
    spans=" ".join(f'<span style="font-size:{14+int((c/mx)*26)}px;color:{cores[i%len(cores)]};padding:6px;display:inline-block;font-weight:600">{p}</span>' for i,(p,c) in enumerate(pals))
    return HTMLResponse(f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><title>Wordcloud Emocional</title>
<style>body{{font-family:sans-serif;background:#1a1a2e;min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:40px;margin:0}}.cloud{{max-width:700px;text-align:center;line-height:2.8}}</style></head>
<body><h1 style="color:white;margin-bottom:6px">Wordcloud Emocional</h1>
<p style="color:rgba(255,255,255,0.6);margin-bottom:32px">Palavras mais usadas no seu diario</p>
<div class="cloud">{spans}</div>
<p style="color:rgba(255,255,255,0.4);margin-top:24px;font-size:13px">Baseado nas suas entradas</p>
<a href="/app/diario" style="margin-top:14px;background:#667eea;color:white;padding:12px 24px;border-radius:8px;text-decoration:none;font-weight:700">Escrever no diario</a>
</body></html>""")
class Plugin(PluginBase):
    name = "wordcloud_v2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
