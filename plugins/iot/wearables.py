"""Plugin: Wearables — integração com dispositivos vestíveis"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid, logging
logger=logging.getLogger(__name__)
router=APIRouter(prefix="/api/v1/wearables",tags=["iot"])
_dispositivos, _leituras = {}, {}

class WearablesPlugin(PluginBase):
    name="wearables"; version="1.0.0"; description="Integração com wearables e biométricos"; category="iot"
    def setup(self,app): app.include_router(router); logger.info("[wearables] OK")
    def health_check(self): return {"status":"healthy","dispositivos":len(_dispositivos),"leituras":len(_leituras)}

@router.post("/registrar-dispositivo")
async def registrar(user_id:str, tipo:str="smartwatch", modelo:str=""):
    did=str(uuid.uuid4())[:8]
    _dispositivos[did]={"id":did,"user_id":user_id,"tipo":tipo,"modelo":modelo,"ativo":True,"registrado_em":datetime.utcnow().isoformat()}
    return {"dispositivo_id":did,"status":"registrado"}

@router.post("/leitura")
async def leitura(dispositivo_id:str, freq_cardiaca:float=70, spo2:float=98, passos:int=5000, calorias:float=200, stress_score:float=3.5, qualidade_sono:float=7.0):
    if dispositivo_id not in _dispositivos: raise HTTPException(404,"Dispositivo não encontrado")
    lid=str(uuid.uuid4())[:8]
    _leituras[lid]={"id":lid,"dispositivo_id":dispositivo_id,"freq_cardiaca":freq_cardiaca,"spo2":spo2,"passos":passos,"calorias":calorias,"stress_score":stress_score,"qualidade_sono":qualidade_sono,"estado_emocional_estimado":"calmo" if stress_score<4 else "estressado" if stress_score<7 else "alto_estresse","ts":datetime.utcnow().isoformat()}
    return {"leitura_id":lid,"estado":_leituras[lid]["estado_emocional_estimado"]}

@router.get("/leituras/{dispositivo_id}")
async def ver_leituras(dispositivo_id:str, limite:int=20):
    leituras=[l for l in _leituras.values() if l["dispositivo_id"]==dispositivo_id]
    return {"total":len(leituras),"leituras":sorted(leituras,key=lambda x:x["ts"],reverse=True)[:limite]}

@router.get("/dispositivos/{user_id}")
async def dispositivos_usuario(user_id:str):
    devs=[d for d in _dispositivos.values() if d["user_id"]==user_id]
    return {"total":len(devs),"dispositivos":devs}

@router.get("/status")
async def status(): return {"plugin":"wearables","dispositivos":len(_dispositivos),"leituras":len(_leituras)}

plugin=WearablesPlugin()
