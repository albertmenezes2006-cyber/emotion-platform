from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from pathlib import Path
import json
from datetime import datetime
router = APIRouter(prefix="/api/v1/xp-ranking", tags=["XP"])
ARQ = Path("xp_v2.json")
NIVEIS = [{"nivel":1,"nome":"Iniciante","xp_min":0,"icone":"🌱"},{"nivel":2,"nome":"Explorador","xp_min":100,"icone":"🔍"},{"nivel":3,"nome":"Expert","xp_min":300,"icone":"⭐"},{"nivel":4,"nome":"Mestre","xp_min":600,"icone":"🏆"}]
ACOES = {"avaliacao_phq9":50,"avaliacao_gad7":50,"entrada_diario":20,"chat_ia":10,"login_diario":5,"indicar_amigo":200}
def load(): return json.loads(ARQ.read_text()) if ARQ.exists() else {}
def get_nivel(xp):
    n=NIVEIS[0]
    for nv in NIVEIS:
        if xp>=nv["xp_min"]: n=nv
    return n
@router.post("/ganhar/{uid}/{acao}")
async def ganhar(uid:str,acao:str):
    pts=ACOES.get(acao,10); d=load()
    if uid not in d: d[uid]={"xp":0,"acoes":[]}
    d[uid]["xp"]+=pts; d[uid]["acoes"].append({"acao":acao,"xp":pts,"ts":datetime.utcnow().isoformat()})
    ARQ.write_text(json.dumps(d,ensure_ascii=False,indent=2))
    return JSONResponse({"xp_ganho":pts,"xp_total":d[uid]["xp"],"nivel":get_nivel(d[uid]["xp"])})
@router.get("/perfil/{uid}")
async def perfil(uid:str):
    d=load(); u=d.get(uid,{"xp":0,"acoes":[]})
    return JSONResponse({"xp_total":u["xp"],"nivel":get_nivel(u["xp"]),"acoes_possiveis":ACOES})
@router.get("/ranking")
async def ranking():
    d=load(); r=sorted(d.items(),key=lambda x:x[1]["xp"],reverse=True)[:10]
    return JSONResponse([{"user":u,"xp":dd["xp"],"nivel":get_nivel(dd["xp"])} for u,dd in r])
class Plugin(PluginBase):
    name = "xp_ranking_v2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
