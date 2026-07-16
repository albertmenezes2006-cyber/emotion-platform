"""Plugin: api_mock | api2 | Mock server para desenvolvimento"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid
import logging
logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/api-mock", tags=["api2"])
_db = {}

class ApiMockPlugin(PluginBase):
    name = "api_mock"; version = "1.0.0"
    description = "Mock server para desenvolvimento"; category = "api2"
    def setup(self, app):
        app.include_router(router)
        logger.info("[api_mock] carregado")
    def health_check(self):
        return {"status": "healthy", "total": len(_db)}

@router.get("/status")
async def status():
    return {"plugin": "api_mock", "categoria": "api2", "total": len(_db), "ts": datetime.utcnow().isoformat()}

@router.post("/criar")
async def criar(nome: str, valor: str = "", user_id: str = ""):
    item_id = str(uuid.uuid4())[:8]
    _db[item_id] = {"id": item_id, "nome": nome, "valor": valor, "user_id": user_id, "ts": datetime.utcnow().isoformat()}
    return {"id": item_id, "status": "criado"}

@router.get("/listar")
async def listar(limite: int = 50):
    return {"total": len(_db), "items": list(_db.values())[-limite:]}

@router.get("/{item_id}")
async def obter(item_id: str):
    if item_id not in _db: raise HTTPException(404, "Nao encontrado")
    return _db[item_id]

@router.delete("/{item_id}")
async def deletar(item_id: str):
    if item_id not in _db: raise HTTPException(404, "Nao encontrado")
    del _db[item_id]; return {"status": "deletado"}

plugin = ApiMockPlugin()
