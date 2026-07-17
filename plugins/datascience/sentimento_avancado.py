"""Plugin: Análise de Sentimento Avançada com léxico PT-BR"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid
import re
import logging
logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/sentimento-avancado", tags=["datascience"])
_analises, _historico = {}, {}
POS={"feliz":0.9,"alegre":0.85,"contente":0.8,"animado":0.8,"grato":0.85,"otimista":0.8,"satisfeito":0.75,"tranquilo":0.7,"calmo":0.65,"ótimo":0.9,"excelente":0.95,"amor":0.9,"paz":0.75,"coragem":0.8,"confiante":0.8,"esperança":0.75,"vitória":0.9,"conquista":0.85}
NEG={"triste":-0.8,"deprimido":-0.9,"ansioso":-0.7,"angustiado":-0.8,"desesperado":-0.95,"sozinho":-0.7,"medo":-0.75,"raiva":-0.7,"furioso":-0.85,"cansado":-0.5,"exausto":-0.7,"culpado":-0.7,"inútil":-0.85,"fracasso":-0.85,"péssimo":-0.9,"terrível":-0.9}
NEG_WORDS={"não","nunca","jamais","nem","nada","sem"}
INT={"muito":1.5,"bastante":1.3,"extremamente":1.8,"super":1.4,"pouco":0.5}

class SentimentoAvancadoPlugin(PluginBase):
    name="sentimento_avancado"; version="1.0.0"; description="Análise sentimento PT-BR léxico completo"; category="datascience"
    def setup(self,app): app.include_router(router); logger.info("[sentimento_avancado] OK")
    def health_check(self): return {"status":"healthy","analises":len(_analises),"lexico_pos":len(POS),"lexico_neg":len(NEG)}

@router.post("/analisar")
async def analisar(texto:str, user_id:str=None):
    if len(texto.strip())<2: raise HTTPException(400,"Texto muito curto")
    words=re.findall(r"\b\w+\b",texto.lower()); score=0.0; found=[]; neg=False
    for i,w in enumerate(words):
        if w in NEG_WORDS: neg=True; continue
        if i>0 and words[i-1] not in NEG_WORDS: neg=False
        mult=INT.get(words[i-1] if i>0 else "",1.0)
        s=0
        if w in POS: s=POS[w]*mult*((-0.7) if neg else 1)
        elif w in NEG: s=NEG[w]*mult*((-0.7) if neg else 1)
        if s!=0: score+=s; found.append({"palavra":w,"score":round(s,3)})
    norm=max(-1,min(1,score/max(len(found),1)))
    sent="muito_positivo" if norm>=0.5 else "positivo" if norm>=0.1 else "neutro" if norm>=-0.1 else "negativo" if norm>=-0.5 else "muito_negativo"
    aid=str(uuid.uuid4())[:8]
    res={"id":aid,"score":round(norm,4),"sentimento":sent,"palavras":found,"ts":datetime.utcnow().isoformat()}
    _analises[aid]=res
    if user_id:
        _historico.setdefault(user_id,[]).append({"score":norm,"sent":sent,"ts":res["ts"]})
        if len(_historico[user_id])>100: _historico[user_id]=_historico[user_id][-100:]
    return res

@router.post("/lote")
async def lote(textos:list, user_id:str=None):
    if len(textos)>50: raise HTTPException(400,"Máximo 50")
    res=[]; scores=[]
    for t in textos:
        if t and len(t.strip())>=2:
            r=await analisar(t,user_id); res.append(r); scores.append(r["score"])
    med=sum(scores)/len(scores) if scores else 0
    return {"total":len(res),"media":round(med,4),"geral":"positivo" if med>0.1 else "negativo" if med<-0.1 else "neutro","resultados":res}

@router.get("/historico/{user_id}")
async def historico(user_id:str):
    h=_historico.get(user_id,[])
    if not h: return {"user_id":user_id,"historico":[]}
    scores=[x["score"] for x in h]
    return {"user_id":user_id,"total":len(h),"media":round(sum(scores)/len(scores),4),"tendencia":"melhora" if len(scores)>1 and scores[-1]>scores[0] else "piora" if len(scores)>1 and scores[-1]<scores[0] else "estavel","historico":h[-30:]}

plugin=SentimentoAvancadoPlugin()

plugin = SentimentoAvancadoPlugin()
