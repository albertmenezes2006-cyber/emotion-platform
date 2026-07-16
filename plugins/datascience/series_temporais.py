"""Plugin: Séries Temporais Emocionais"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import statistics
import logging
logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/series-temporais", tags=["datascience"])
_series = {}

class SeriesTemporaisPlugin(PluginBase):
    name = "series_temporais"; version = "1.0.0"
    description = "Séries temporais emocionais com tendência e previsão"; category = "datascience"
    def setup(self, app): app.include_router(router); logger.info("[series_temporais] OK")
    def health_check(self): return {"status":"healthy","series":len(_series)}

@router.post("/criar")
async def criar(user_id:str, tipo:str="bem_estar"):
    sid=f"{user_id}_{tipo}"; _series[sid]={"id":sid,"user_id":user_id,"tipo":tipo,"pontos":[],"criado_em":datetime.utcnow().isoformat()}
    return {"serie_id":sid}

@router.post("/{serie_id}/ponto")
async def ponto(serie_id:str, valor:float, contexto:str=""):
    if serie_id not in _series: raise HTTPException(404,"Série não encontrada")
    _series[serie_id]["pontos"].append({"valor":min(max(valor,0),10),"ts":datetime.utcnow().isoformat(),"contexto":contexto})
    if len(_series[serie_id]["pontos"])>365: _series[serie_id]["pontos"]=_series[serie_id]["pontos"][-365:]
    return {"total":len(_series[serie_id]["pontos"])}

@router.get("/{serie_id}/analisar")
async def analisar(serie_id:str):
    if serie_id not in _series: raise HTTPException(404,"Não encontrada")
    pts=_series[serie_id]["pontos"]
    if len(pts)<3: return {"erro":"mínimo 3 pontos","atual":len(pts)}
    vals=[p["valor"] for p in pts]
    media=statistics.mean(vals); desvio=statistics.stdev(vals) if len(vals)>1 else 0
    n=len(vals); slope=sum((i-n/2)*(v-media) for i,v in enumerate(vals))/max(sum((i-n/2)**2 for i in range(n)),1)
    return {"total":len(vals),"media":round(media,3),"desvio":round(desvio,3),"min":min(vals),"max":max(vals),"ultimo":vals[-1],"tendencia":"crescente" if slope>0.05 else "decrescente" if slope<-0.05 else "estavel","previsao_prox":round(min(max(vals[-1]+slope,0),10),3)}

@router.get("/usuario/{user_id}")
async def por_usuario(user_id:str):
    series=[s for s in _series.values() if s["user_id"]==user_id]
    return {"total":len(series),"series":[{"id":s["id"],"tipo":s["tipo"],"pontos":len(s["pontos"])} for s in series]}

plugin=SeriesTemporaisPlugin()
