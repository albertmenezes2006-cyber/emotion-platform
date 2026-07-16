"""Plugin: Modelo de Risco Emocional"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid, logging
logger=logging.getLogger(__name__)
router=APIRouter(prefix="/api/v1/modelo-risco",tags=["datascience"])
_avaliacoes=[]; _alertas=[]
PESOS={"ideacao_suicida":0.40,"depressao_grave":0.20,"ansiedade_grave":0.15,"isolamento":0.10,"abuso_substancias":0.08,"hist_crise":0.07}
PROTECAO={"suporte_social":0.15,"terapia":0.12,"atividade_fisica":0.08,"sono":0.08,"coping":0.10}

class ModeloRiscoPlugin(PluginBase):
    name="modelo_risco"; version="1.0.0"; description="Modelo preditivo risco emocional"; category="datascience"
    def setup(self,app): app.include_router(router); logger.info("[modelo_risco] OK")
    def health_check(self): return {"status":"healthy","avaliacoes":len(_avaliacoes),"alertas":len(_alertas)}

@router.post("/avaliar")
async def avaliar(user_id:str,ideacao_suicida:float=0,depressao_grave:float=0,ansiedade_grave:float=0,isolamento:float=0,abuso_substancias:float=0,hist_crise:float=0,suporte_social:float=0.5,terapia:float=0.5,atividade_fisica:float=0.5,sono:float=0.7,coping:float=0.5):
    f={"ideacao_suicida":min(max(ideacao_suicida,0),1),"depressao_grave":min(max(depressao_grave,0),1),"ansiedade_grave":min(max(ansiedade_grave,0),1),"isolamento":min(max(isolamento,0),1),"abuso_substancias":min(max(abuso_substancias,0),1),"hist_crise":min(max(hist_crise,0),1)}
    p={"suporte_social":min(max(suporte_social,0),1),"terapia":min(max(terapia,0),1),"atividade_fisica":min(max(atividade_fisica,0),1),"sono":min(max(sono,0),1),"coping":min(max(coping,0),1)}
    score=sum(f[k]*PESOS[k] for k in f)-sum(p[k]*PROTECAO[k] for k in p)
    score=max(0,min(1,score))
    nivel="critico" if score>=0.7 else "alto" if score>=0.5 else "moderado" if score>=0.3 else "baixo" if score>=0.1 else "minimo"
    acao={"critico":"Encaminhar imediatamente profissional","alto":"Contato urgente terapeuta","moderado":"Acompanhamento regular","baixo":"Monitoramento preventivo","minimo":"Manter práticas bem-estar"}[nivel]
    r={"id":str(uuid.uuid4())[:8],"user_id":user_id,"score":round(score,4),"nivel":nivel,"acao":acao,"fatores":f,"protecao":p,"ts":datetime.utcnow().isoformat()}
    _avaliacoes.append(r)
    if nivel in ["alto","critico"]: _alertas.append({"user_id":user_id,"nivel":nivel,"score":score,"ts":r["ts"]})
    return r

@router.get("/alertas")
async def alertas(): return {"total":len(_alertas),"alertas":_alertas[-20:]}

@router.get("/historico/{user_id}")
async def historico(user_id:str): 
    h=[a for a in _avaliacoes if a["user_id"]==user_id]
    return {"total":len(h),"historico":h[-10:]}

@router.get("/recursos-emergencia")
async def recursos(): return {"cvv":{"tel":"188","site":"cvv.org.br"},"samu":"192","caps":"gov.br/saude"}

plugin=ModeloRiscoPlugin()
