"""Plugin: Psicoeducação — conteúdo educativo em saúde mental"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid, logging
logger=logging.getLogger(__name__)
router=APIRouter(prefix="/api/v1/psicoeducacao",tags=["educacao"])
_conteudos, _progresso = {}, {}
CONTEUDOS_PADRAO=[
    {"id":"1","titulo":"O que é ansiedade?","categoria":"ansiedade","nivel":"basico","duracao_min":5,"conteudo":"A ansiedade é uma resposta natural do organismo...","tags":["ansiedade","emoções"]},
    {"id":"2","titulo":"Técnicas de respiração","categoria":"mindfulness","nivel":"basico","duracao_min":8,"conteudo":"A respiração diafragmática ativa o sistema nervoso parassimpático...","tags":["respiração","mindfulness"]},
    {"id":"3","titulo":"Regulação emocional","categoria":"habilidades","nivel":"intermediario","duracao_min":12,"conteudo":"Regulação emocional é a capacidade de gerenciar...","tags":["emoções","habilidades"]},
    {"id":"4","titulo":"Pensamentos automáticos","categoria":"tcc","nivel":"intermediario","duracao_min":15,"conteudo":"Pensamentos automáticos são pensamentos involuntários...","tags":["tcc","pensamentos"]},
    {"id":"5","titulo":"Autocompaixão","categoria":"bem-estar","nivel":"avancado","duracao_min":20,"conteudo":"Autocompaixão envolve tratar a si mesmo com bondade...","tags":["autocompaixão","bem-estar"]}
]

class PsicoeducacaoPlugin(PluginBase):
    name="psicoeducacao"; version="1.0.0"; description="Psicoeducação em saúde mental com trilhas de aprendizado"; category="educacao"
    def setup(self,app):
        app.include_router(router); logger.info("[psicoeducacao] OK")
        for c in CONTEUDOS_PADRAO: _conteudos[c["id"]]=c
    def health_check(self): return {"status":"healthy","conteudos":len(_conteudos),"usuarios":len(_progresso)}

@router.get("/conteudos")
async def listar(categoria:str=None, nivel:str=None):
    itens=list(_conteudos.values())
    if categoria: itens=[i for i in itens if i["categoria"]==categoria]
    if nivel: itens=[i for i in itens if i["nivel"]==nivel]
    return {"total":len(itens),"conteudos":itens}

@router.get("/conteudos/{cid}")
async def obter(cid:str):
    if cid not in _conteudos: raise HTTPException(404,"Conteúdo não encontrado")
    return _conteudos[cid]

@router.post("/progresso")
async def registrar_progresso(user_id:str, conteudo_id:str, concluido:bool=True, avaliacao:int=5):
    if conteudo_id not in _conteudos: raise HTTPException(404,"Conteúdo não encontrado")
    _progresso.setdefault(user_id,[]).append({"conteudo_id":conteudo_id,"concluido":concluido,"avaliacao":avaliacao,"ts":datetime.utcnow().isoformat()})
    return {"status":"progresso registrado","total_concluidos":sum(1 for p in _progresso[user_id] if p["concluido"])}

@router.get("/progresso/{user_id}")
async def ver_progresso(user_id:str):
    prog=_progresso.get(user_id,[])
    return {"total":len(prog),"concluidos":sum(1 for p in prog if p["concluido"]),"historico":prog}

@router.post("/conteudos/criar")
async def criar_conteudo(titulo:str, categoria:str, nivel:str, conteudo:str, duracao_min:int=10):
    cid=str(uuid.uuid4())[:8]
    _conteudos[cid]={"id":cid,"titulo":titulo,"categoria":categoria,"nivel":nivel,"conteudo":conteudo,"duracao_min":duracao_min,"criado_em":datetime.utcnow().isoformat()}
    return {"conteudo_id":cid,"status":"criado"}

@router.get("/status")
async def status(): return {"plugin":"psicoeducacao","conteudos":len(_conteudos)}

plugin=PsicoeducacaoPlugin()
