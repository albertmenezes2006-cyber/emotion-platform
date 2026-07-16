"""Plugin: Protocolo de Crise — gestão de crises emocionais"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid, logging
logger=logging.getLogger(__name__)
router=APIRouter(prefix="/api/v1/protocolo-crise",tags=["crises"])
_crises, _protocolos_ativos = {}, {}

class ProtocoloCrisePlugin(PluginBase):
    name="protocolo_crise"; version="1.0.0"; description="Protocolos de gestão de crises emocionais"; category="crises"
    def setup(self,app): app.include_router(router); logger.info("[protocolo_crise] OK")
    def health_check(self): return {"status":"healthy","crises_registradas":len(_crises),"protocolos_ativos":len(_protocolos_ativos)}

@router.post("/acionar")
async def acionar_protocolo(user_id:str, nivel:str="moderado", sintomas:list=None, contato_emergencia:str=""):
    if nivel not in ["leve","moderado","grave","critico"]: raise HTTPException(400,"Nível inválido")
    crise_id=str(uuid.uuid4())[:8]
    steps={"leve":["Respire fundo","Técnica 5-4-3-2-1","Contate seu terapeuta"],"moderado":["Para o que está fazendo","Ligue para alguém de confiança","CVV: 188","Técnicas de grounding"],"grave":["Não fique sozinho","Ligue CVV 188 agora","Vá para UPA/UBS","Contate familiar"],"critico":["LIGUE 192 (SAMU)","Não fique sozinho","CVV: 188","Vá à emergência imediatamente"]}
    _crises[crise_id]={"id":crise_id,"user_id":user_id,"nivel":nivel,"sintomas":sintomas or [],"contato":contato_emergencia,"steps":steps[nivel],"status":"em_andamento","inicio":datetime.utcnow().isoformat()}
    _protocolos_ativos[user_id]=crise_id
    return {"crise_id":crise_id,"nivel":nivel,"steps_imediatos":steps[nivel],"recursos":{"cvv":"188","samu":"192","caps":"Procure o CAPS mais próximo"}}

@router.post("/{crise_id}/resolver")
async def resolver(crise_id:str, resolucao:str=""):
    if crise_id not in _crises: raise HTTPException(404,"Crise não encontrada")
    _crises[crise_id].update({"status":"resolvida","resolucao":resolucao,"fim":datetime.utcnow().isoformat()})
    uid=_crises[crise_id]["user_id"]
    if uid in _protocolos_ativos: del _protocolos_ativos[uid]
    return {"status":"resolvida","crise_id":crise_id}

@router.get("/historico/{user_id}")
async def historico(user_id:str):
    crises=[c for c in _crises.values() if c["user_id"]==user_id]
    return {"total":len(crises),"crises":sorted(crises,key=lambda x:x["inicio"],reverse=True)}

@router.get("/recursos-emergencia")
async def recursos(): return {"cvv":{"tel":"188","24h":True},"samu":"192","bombeiros":"193","policia":"190","disque100":"100"}

@router.get("/status")
async def status(): return {"plugin":"protocolo_crise","crises":len(_crises),"ativos":len(_protocolos_ativos)}

plugin=ProtocoloCrisePlugin()
