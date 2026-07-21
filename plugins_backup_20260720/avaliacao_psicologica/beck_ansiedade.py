"""Plugin: beck_ansiedade | avaliacao_psicologica | BAI: Inventário de ansiedade de Beck"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid
import logging
logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/beck-ansiedade", tags=["avaliacao_psicologica"])
_db = {}

class BeckAnsiedadePlugin(PluginBase):
    name = "beck_ansiedade"; version = "1.0.0"
    description = "BAI: Inventário de ansiedade de Beck"; category = "avaliacao_psicologica"
    def setup(self, app):
        app.include_router(router)
        logger.info("[beck_ansiedade] OK")
    def health_check(self):
        return {"status":"healthy","total":len(_db)}

@router.get("/status")
async def status():
    return {"plugin":"beck_ansiedade","cat":"avaliacao_psicologica","total":len(_db),"ts":datetime.utcnow().isoformat()}

@router.post("/criar")
async def criar(nome:str, valor:str="", user_id:str=""):
    i=str(uuid.uuid4())[:8]
    _db[i]={"id":i,"nome":nome,"valor":valor,"user_id":user_id,"ts":datetime.utcnow().isoformat()}
    return {"id":i,"status":"criado"}

@router.get("/listar")
async def listar(limite:int=50):
    return {"total":len(_db),"items":list(_db.values())[-limite:]}

@router.get("/{item_id}")
async def obter(item_id:str):
    if item_id not in _db: raise HTTPException(404,"Nao encontrado")
    return _db[item_id]

@router.delete("/{item_id}")
async def deletar(item_id:str):
    if item_id not in _db: raise HTTPException(404,"Nao encontrado")
    del _db[item_id]; return {"status":"deletado"}

plugin = BeckAnsiedadePlugin()
