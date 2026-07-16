"""Plugin: Saúde Mental Corporativa — programas empresariais"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid, logging
logger=logging.getLogger(__name__)
router=APIRouter(prefix="/api/v1/saude-mental-corp",tags=["rh"])
_empresas, _programas, _avaliacoes_corp = {}, {}, {}

class SaudeMentalCorporativaPlugin(PluginBase):
    name="saude_mental_corporativa"; version="1.0.0"; description="Programas de saúde mental corporativa"; category="rh"
    def setup(self,app): app.include_router(router); logger.info("[saude_mental_corporativa] OK")
    def health_check(self): return {"status":"healthy","empresas":len(_empresas),"programas":len(_programas)}

@router.post("/empresa/cadastrar")
async def cadastrar_empresa(nome:str, cnpj:str, setor:str, total_funcionarios:int):
    eid=str(uuid.uuid4())[:8]
    _empresas[eid]={"id":eid,"nome":nome,"cnpj":cnpj,"setor":setor,"total_funcionarios":total_funcionarios,"programas":[],"ts":datetime.utcnow().isoformat()}
    return {"empresa_id":eid,"status":"cadastrada"}

@router.post("/programa/criar")
async def criar_programa(empresa_id:str, nome:str, tipo:str, duracao_semanas:int=12, descricao:str=""):
    if empresa_id not in _empresas: raise HTTPException(404,"Empresa não encontrada")
    pid=str(uuid.uuid4())[:8]
    _programas[pid]={"id":pid,"empresa_id":empresa_id,"nome":nome,"tipo":tipo,"duracao_semanas":duracao_semanas,"descricao":descricao,"participantes":0,"ts":datetime.utcnow().isoformat()}
    _empresas[empresa_id]["programas"].append(pid)
    return {"programa_id":pid,"status":"criado"}

@router.post("/avaliacao-clima")
async def avaliacao_clima(empresa_id:str, satisfacao:float, estresse:float, engajamento:float, burnout:float):
    aid=str(uuid.uuid4())[:8]
    score=round((satisfacao*0.3+engajamento*0.3+(10-estresse)*0.2+(10-burnout)*0.2)/10,3)
    _avaliacoes_corp[aid]={"id":aid,"empresa_id":empresa_id,"satisfacao":satisfacao,"estresse":estresse,"engajamento":engajamento,"burnout":burnout,"score_clima":score,"nivel":"saudavel" if score>0.7 else "atencao" if score>0.5 else "critico","ts":datetime.utcnow().isoformat()}
    return {"avaliacao_id":aid,"score_clima":score,"nivel":_avaliacoes_corp[aid]["nivel"]}

@router.get("/dashboard/{empresa_id}")
async def dashboard(empresa_id:str):
    if empresa_id not in _empresas: raise HTTPException(404,"Empresa não encontrada")
    avs=[a for a in _avaliacoes_corp.values() if a["empresa_id"]==empresa_id]
    return {"empresa":_empresas[empresa_id],"total_avaliacoes":len(avs),"ultima_avaliacao":avs[-1] if avs else None}

@router.get("/status")
async def status(): return {"plugin":"saude_mental_corporativa","empresas":len(_empresas)}

plugin=SaudeMentalCorporativaPlugin()
