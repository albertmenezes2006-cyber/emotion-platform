"""Plugin: tutorial_interativo | plataforma_final | Tutorial interativo passo a passo"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid, logging
logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/tutorial-interativo", tags=["plataforma_final"])
_db = {}

class TutorialInterativoPlugin(PluginBase):
    name = "tutorial_interativo"; version = "1.0.0"
    description = "Tutorial interativo passo a passo"; category = "plataforma_final"
    def setup(self, app):
        app.include_router(router)
        logger.info(f"[tutorial_interativo] OK")
    def health_check(self):
        return {"status":"healthy","total":len(_db)}

@router.get("/status")
async def status():
    return {"plugin":"tutorial_interativo","cat":"plataforma_final","total":len(_db),"ts":datetime.utcnow().isoformat()}

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

plugin = TutorialInterativoPlugin()
