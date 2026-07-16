"""Plugin: Sistema XP — pontos de experiência terapêutica"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import logging
logger=logging.getLogger(__name__)
router=APIRouter(prefix="/api/v1/xp",tags=["gamificacao"])
_usuarios={}
NIVEIS={0:"Iniciante",100:"Explorador",300:"Praticante",600:"Consciente",1000:"Equilibrado",1500:"Resiliente",2500:"Mestre",4000:"Sábio"}

class SistemaXPPlugin(PluginBase):
    name="sistema_xp"; version="1.0.0"; description="Sistema de XP e níveis para jornada terapêutica"; category="gamificacao"
    def setup(self,app): app.include_router(router); logger.info("[sistema_xp] OK")
    def health_check(self): return {"status":"healthy","usuarios":len(_usuarios)}

@router.post("/ganhar")
async def ganhar_xp(user_id:str, acao:str, xp:int=10):
    if user_id not in _usuarios: _usuarios[user_id]={"user_id":user_id,"xp":0,"nivel":"Iniciante","historico":[],"streak":0}
    _usuarios[user_id]["xp"]+=max(0,min(xp,500))
    xp_total=_usuarios[user_id]["xp"]
    nivel=max((n for n,nome in NIVEIS.items() if xp_total>=n),default=0)
    _usuarios[user_id]["nivel"]=NIVEIS[nivel]
    _usuarios[user_id]["historico"].append({"acao":acao,"xp":xp,"ts":datetime.utcnow().isoformat()})
    return {"xp_ganho":xp,"xp_total":xp_total,"nivel":NIVEIS[nivel]}

@router.get("/{user_id}")
async def ver_xp(user_id:str):
    if user_id not in _usuarios: raise HTTPException(404,"Usuário não encontrado")
    return _usuarios[user_id]

@router.get("/ranking/top")
async def ranking(limite:int=10):
    ranked=sorted(_usuarios.values(),key=lambda x:x["xp"],reverse=True)[:limite]
    return {"ranking":[{"user_id":u["user_id"],"xp":u["xp"],"nivel":u["nivel"]} for u in ranked]}

@router.get("/status")
async def status(): return {"plugin":"sistema_xp","usuarios":len(_usuarios)}

plugin=SistemaXPPlugin()
