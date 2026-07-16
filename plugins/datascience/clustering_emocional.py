"""Plugin: Clustering Emocional — segmentação de perfis emocionais"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid, math, random, logging
logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/clustering", tags=["datascience"])
_perfis, _modelos, _clusters = {}, {}, {}

class ClusteringEmocionalPlugin(PluginBase):
    name = "clustering_emocional"; version = "1.0.0"
    description = "Clustering K-Means de perfis emocionais"; category = "datascience"
    def setup(self, app): app.include_router(router); logger.info("[clustering_emocional] OK")
    def health_check(self): return {"status":"healthy","perfis":len(_perfis),"modelos":len(_modelos)}

@router.get("/status")
async def status(): return {"plugin":"clustering_emocional","perfis":len(_perfis),"modelos":len(_modelos)}

@router.post("/perfil/adicionar")
async def add_perfil(user_id:str, valencia:float=0.5, ativacao:float=0.5, ansiedade:float=0.3, depressao:float=0.2, estresse:float=0.4, bem_estar:float=0.6):
    _perfis[user_id]={"user_id":user_id,"features":{"valencia":min(max(valencia,0),1),"ativacao":min(max(ativacao,0),1),"ansiedade":min(max(ansiedade,0),1),"depressao":min(max(depressao,0),1),"estresse":min(max(estresse,0),1),"bem_estar":min(max(bem_estar,0),1)},"cluster_id":None,"ts":datetime.utcnow().isoformat()}
    return {"status":"adicionado","user_id":user_id}

@router.post("/treinar")
async def treinar(k:int=4, iteracoes:int=50):
    if len(_perfis)<k: raise HTTPException(400,f"Mínimo {k} perfis")
    perfis=list(_perfis.values()); keys=list(perfis[0]["features"].keys())
    centroides=[dict(random.choice(perfis)["features"]) for _ in range(k)]
    assigns={}
    for _ in range(iteracoes):
        na={}
        for p in perfis:
            dists=[math.sqrt(sum((p["features"][k2]-c[k2])**2 for k2 in keys)) for c in centroides]
            na[p["user_id"]]=dists.index(min(dists))
        if na==assigns: break
        assigns=na
        for ci in range(k):
            membros=[p for p in perfis if assigns.get(p["user_id"])==ci]
            if membros:
                for feat in keys: centroides[ci][feat]=sum(m["features"][feat] for m in membros)/len(membros)
    for uid,cid in assigns.items():
        if uid in _perfis: _perfis[uid]["cluster_id"]=cid
    mid=str(uuid.uuid4())[:8]
    _modelos[mid]={"id":mid,"k":k,"centroides":centroides,"assigns":assigns,"ts":datetime.utcnow().isoformat()}
    _clusters[mid]=[{"id":i,"membros":sum(1 for v in assigns.values() if v==i),"centroide":{k2:round(centroides[i][k2],3) for k2 in keys}} for i in range(k)]
    return {"modelo_id":mid,"k":k,"clusters":_clusters[mid]}

@router.get("/clusters/{modelo_id}")
async def ver_clusters(modelo_id:str):
    if modelo_id not in _modelos: raise HTTPException(404,"Modelo não encontrado")
    return {"modelo_id":modelo_id,"clusters":_clusters.get(modelo_id,[])}

@router.get("/perfil/{user_id}")
async def ver_perfil(user_id:str):
    if user_id not in _perfis: raise HTTPException(404,"Perfil não encontrado")
    return _perfis[user_id]

plugin=ClusteringEmocionalPlugin()
