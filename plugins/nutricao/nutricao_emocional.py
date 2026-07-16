"""Plugin: Nutrição Emocional — correlação entre dieta e humor"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid, logging
logger=logging.getLogger(__name__)
router=APIRouter(prefix="/api/v1/nutricao-emocional",tags=["nutricao"])
_registros={}
ALIMENTOS_HUMOR={
    "banana":{"humor":0.7,"nutrientes":["triptofano","potássio"],"efeito":"melhora humor e energia"},
    "chocolate_amargo":{"humor":0.8,"nutrientes":["magnesio","flavonoides"],"efeito":"libera endorfinas"},
    "salmão":{"humor":0.75,"nutrientes":["omega3","vit_d"],"efeito":"reduz inflamação e depressão"},
    "aveia":{"humor":0.65,"nutrientes":["fibras","b1"],"efeito":"estabiliza glicemia e humor"},
    "espinafre":{"humor":0.7,"nutrientes":["folato","mg"],"efeito":"reduz depressão"},
    "nozes":{"humor":0.72,"nutrientes":["omega3","e"],"efeito":"neuroprotetor"},
    "iogurte":{"humor":0.68,"nutrientes":["probioticos","ca"],"efeito":"eixo intestino-cérebro"},
    "açúcar":{"humor":-0.3,"nutrientes":[],"efeito":"pico e queda de energia"},
    "cafeína":{"humor":0.4,"nutrientes":[],"efeito":"alerta temporário mas pode aumentar ansiedade"},
    "álcool":{"humor":-0.6,"nutrientes":[],"efeito":"depressor do SNC"}
}

class NutricaoEmocionalPlugin(PluginBase):
    name="nutricao_emocional"; version="1.0.0"; description="Correlação nutrição e estados emocionais"; category="nutricao"
    def setup(self,app): app.include_router(router); logger.info("[nutricao_emocional] OK")
    def health_check(self): return {"status":"healthy","registros":len(_registros),"alimentos_mapeados":len(ALIMENTOS_HUMOR)}

@router.post("/registrar-refeicao")
async def registrar(user_id:str, alimentos:list, humor_antes:float=5.0, humor_depois:float=None):
    rid=str(uuid.uuid4())[:8]
    analise=[{"alimento":a,"info":ALIMENTOS_HUMOR.get(a.lower(),{"humor":0,"efeito":"não mapeado"})} for a in alimentos]
    score_total=sum(i["info"].get("humor",0) for i in analise)
    _registros[rid]={"id":rid,"user_id":user_id,"alimentos":alimentos,"analise":analise,"score_nutricional":round(score_total,3),"humor_antes":humor_antes,"humor_depois":humor_depois,"ts":datetime.utcnow().isoformat()}
    return {"registro_id":rid,"score_nutricional":round(score_total,3),"recomendacao":"Dieta com impacto positivo no humor!" if score_total>0.5 else "Considere incluir alimentos neuroprotetores"}

@router.get("/alimentos")
async def listar_alimentos(): return {"total":len(ALIMENTOS_HUMOR),"alimentos":ALIMENTOS_HUMOR}

@router.get("/historico/{user_id}")
async def historico(user_id:str):
    regs=[r for r in _registros.values() if r["user_id"]==user_id]
    return {"total":len(regs),"registros":regs}

@router.get("/status")
async def status(): return {"plugin":"nutricao_emocional"}

plugin=NutricaoEmocionalPlugin()
