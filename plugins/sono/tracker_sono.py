"""Plugin: Tracker de Sono — monitoramento completo do sono"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid, logging
logger=logging.getLogger(__name__)
router=APIRouter(prefix="/api/v1/sono",tags=["sono"])
_registros={}

class TrackerSonoPlugin(PluginBase):
    name="tracker_sono"; version="1.0.0"; description="Monitoramento completo de qualidade do sono"; category="sono"
    def setup(self,app): app.include_router(router); logger.info("[tracker_sono] OK")
    def health_check(self): return {"status":"healthy","registros":len(_registros)}

@router.post("/registrar")
async def registrar(user_id:str, hora_dormir:str="23:00", hora_acordar:str="07:00", qualidade:int=7, sonhos:bool=False, despertares:int=0, humor_manha:float=6.0):
    rid=str(uuid.uuid4())[:8]
    partes_d=[int(x) for x in hora_dormir.split(":")]; partes_a=[int(x) for x in hora_acordar.split(":")]
    duracao_h=((partes_a[0]*60+partes_a[1])-(partes_d[0]*60+partes_d[1]))/60
    if duracao_h<0: duracao_h+=24
    eficiencia=max(0,min(100,int((1-despertares*0.1)*qualidade/10*100)))
    status_sono="excelente" if duracao_h>=8 and qualidade>=8 else "bom" if duracao_h>=7 and qualidade>=6 else "regular" if duracao_h>=6 else "insuficiente"
    _registros[rid]={"id":rid,"user_id":user_id,"hora_dormir":hora_dormir,"hora_acordar":hora_acordar,"duracao_h":round(duracao_h,1),"qualidade":qualidade,"sonhos":sonhos,"despertares":despertares,"eficiencia":eficiencia,"status":status_sono,"humor_manha":humor_manha,"ts":datetime.utcnow().isoformat()}
    return {"registro_id":rid,"duracao_h":round(duracao_h,1),"status":status_sono,"eficiencia":eficiencia}

@router.get("/historico/{user_id}")
async def historico(user_id:str, limite:int=30):
    regs=[r for r in _registros.values() if r["user_id"]==user_id]
    regs=sorted(regs,key=lambda x:x["ts"],reverse=True)[:limite]
    if regs:
        media_dur=sum(r["duracao_h"] for r in regs)/len(regs)
        media_qual=sum(r["qualidade"] for r in regs)/len(regs)
        return {"total":len(regs),"media_duracao_h":round(media_dur,1),"media_qualidade":round(media_qual,1),"registros":regs}
    return {"total":0,"registros":[]}

@router.get("/dicas")
async def dicas_sono(): return {"dicas":["Mantenha horário regular","Evite telas 1h antes","Quarto escuro e fresco","Evite cafeína após 14h","Pratique relaxamento antes de dormir"]}

@router.get("/status")
async def status(): return {"plugin":"tracker_sono","registros":len(_registros)}

plugin=TrackerSonoPlugin()
