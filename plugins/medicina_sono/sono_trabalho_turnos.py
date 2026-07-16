"""Plugin: sono_trabalho_turnos | medicina_sono | Sono em trabalhadores de turno"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid, logging
logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/sono-trabalho-turnos", tags=["medicina_sono"])
_db = {}

class SonoTrabalhoTurnosPlugin(PluginBase):
    name = "sono_trabalho_turnos"; version = "1.0.0"
    description = "Sono em trabalhadores de turno"; category = "medicina_sono"
    def setup(self, app):
        app.include_router(router)
        logger.info(f"[sono_trabalho_turnos] OK")
    def health_check(self):
        return {"status":"healthy","total":len(_db)}

@router.get("/status")
async def status():
    return {"plugin":"sono_trabalho_turnos","cat":"medicina_sono","total":len(_db),"ts":datetime.utcnow().isoformat()}

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

plugin = SonoTrabalhoTurnosPlugin()
