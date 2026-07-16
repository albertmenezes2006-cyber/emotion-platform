"""Plugin: Sessões de Meditação — guiadas e personalizadas"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid, logging
logger=logging.getLogger(__name__)
router=APIRouter(prefix="/api/v1/meditacao",tags=["meditacao"])
_sessoes, _registros = {}, {}
MEDITACOES=[
    {"id":"1","titulo":"Respiração 4-7-8","tipo":"respiracao","duracao_min":5,"nivel":"iniciante","descricao":"Inspire 4s, segure 7s, expire 8s. Ativa o parassimpático."},
    {"id":"2","titulo":"Body Scan","tipo":"mindfulness","duracao_min":15,"nivel":"iniciante","descricao":"Varredura corporal para relaxamento profundo."},
    {"id":"3","titulo":"Loving Kindness","tipo":"compaixao","duracao_min":20,"nivel":"intermediario","descricao":"Meditação de bondade amorosa para si e outros."},
    {"id":"4","titulo":"Mindfulness MBSR","tipo":"mindfulness","duracao_min":30,"nivel":"avancado","descricao":"Protocolo oficial de redução de estresse baseado em mindfulness."},
    {"id":"5","titulo":"Visualização Criativa","tipo":"visualizacao","duracao_min":12,"nivel":"iniciante","descricao":"Técnica de visualização positiva para bem-estar."}
]

class SessoesMeditacaoPlugin(PluginBase):
    name="sessoes_meditacao"; version="1.0.0"; description="Sessões de meditação guiadas e registro de prática"; category="meditacao"
    def setup(self,app):
        app.include_router(router); logger.info("[sessoes_meditacao] OK")
        for m in MEDITACOES: _sessoes[m["id"]]=m
    def health_check(self): return {"status":"healthy","meditacoes":len(_sessoes),"sessoes_realizadas":len(_registros)}

@router.get("/listar")
async def listar(tipo:str=None, nivel:str=None):
    items=list(_sessoes.values())
    if tipo: items=[i for i in items if i["tipo"]==tipo]
    if nivel: items=[i for i in items if i["nivel"]==nivel]
    return {"total":len(items),"meditacoes":items}

@router.post("/iniciar/{med_id}")
async def iniciar(med_id:str, user_id:str):
    if med_id not in _sessoes: raise HTTPException(404,"Meditação não encontrada")
    sid=str(uuid.uuid4())[:8]
    _registros[sid]={"id":sid,"user_id":user_id,"meditacao_id":med_id,"meditacao":_sessoes[med_id]["titulo"],"inicio":datetime.utcnow().isoformat(),"concluida":False}
    return {"sessao_id":sid,"meditacao":_sessoes[med_id],"status":"iniciada"}

@router.post("/concluir/{sessao_id}")
async def concluir(sessao_id:str, humor_antes:float=5, humor_depois:float=7, nota:str=""):
    if sessao_id not in _registros: raise HTTPException(404,"Sessão não encontrada")
    _registros[sessao_id].update({"concluida":True,"humor_antes":humor_antes,"humor_depois":humor_depois,"impacto":round(humor_depois-humor_antes,2),"nota":nota,"fim":datetime.utcnow().isoformat()})
    return {"status":"concluída","impacto_humor":round(humor_depois-humor_antes,2)}

@router.get("/historico/{user_id}")
async def historico(user_id:str):
    sess=[s for s in _registros.values() if s["user_id"]==user_id]
    total_min=sum(_sessoes.get(s["meditacao_id"],{}).get("duracao_min",0) for s in sess if s["concluida"])
    return {"total_sessoes":len(sess),"concluidas":sum(1 for s in sess if s["concluida"]),"minutos_totais":total_min,"sessoes":sess}

@router.get("/status")
async def status(): return {"plugin":"sessoes_meditacao","meditacoes":len(_sessoes)}

plugin=SessoesMeditacaoPlugin()
