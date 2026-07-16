"""Plugin: Registro Imutável — blockchain para dados clínicos"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid, hashlib, logging
logger=logging.getLogger(__name__)
router=APIRouter(prefix="/api/v1/blockchain",tags=["blockchain"])
_chain=[]; _index={}

class RegistroImutavelPlugin(PluginBase):
    name="registro_imutavel"; version="1.0.0"; description="Blockchain para registros clínicos imutáveis"; category="blockchain"
    def setup(self,app): app.include_router(router); logger.info("[blockchain] OK"); _iniciar_genesis()
    def health_check(self): return {"status":"healthy","blocos":len(_chain)}

def _hash_bloco(bloco):
    return hashlib.sha256(str(bloco).encode()).hexdigest()

def _iniciar_genesis():
    if not _chain:
        genesis={"index":0,"ts":datetime.utcnow().isoformat(),"dados":"GENESIS","hash_anterior":"0"*64,"nonce":0}
        genesis["hash"]=_hash_bloco(genesis)
        _chain.append(genesis)

@router.post("/registrar")
async def registrar(tipo:str, dados:str, user_id:str, assinatura:str=""):
    ultimo=_chain[-1]
    bloco={"index":len(_chain),"ts":datetime.utcnow().isoformat(),"tipo":tipo,"dados":dados,"user_id":user_id,"assinatura":assinatura,"hash_anterior":ultimo["hash"],"nonce":0}
    bloco["hash"]=_hash_bloco(bloco)
    _chain.append(bloco)
    _index[bloco["hash"][:8]]=len(_chain)-1
    return {"hash":bloco["hash"][:16]+"...","bloco":bloco["index"],"status":"registrado_imutavelmente"}

@router.get("/verificar/{hash_id}")
async def verificar(hash_id:str):
    idx=_index.get(hash_id)
    if idx is None: raise HTTPException(404,"Hash não encontrado")
    bloco=_chain[idx]
    valido=bloco["hash"]==_hash_bloco({k:v for k,v in bloco.items() if k!="hash"})
    return {"valido":valido,"bloco":bloco}

@router.get("/chain")
async def ver_chain(ultimos:int=10): return {"total_blocos":len(_chain),"ultimos":_chain[-ultimos:]}

@router.get("/status")
async def status(): return {"blocos":len(_chain),"plugin":"blockchain"}

plugin=RegistroImutavelPlugin()
