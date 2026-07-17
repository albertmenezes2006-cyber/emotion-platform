from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from pathlib import Path
import json
router = APIRouter(prefix="/api/v1/features", tags=["Features"])
ARQ = Path("feature_flags.json")
DEF = {"pix_ativo":True,"blog_ativo":True,"nps_ativo":True,"chat_ia":True,"gamificacao":True,"widget_embed":True,"referral_ativo":True,"cupons_ativos":True}
def load(): return json.loads(ARQ.read_text()) if ARQ.exists() else DEF
@router.get("") 
async def listar(): return JSONResponse(load())
@router.get("/{flag}")
async def ver(flag:str): return JSONResponse({"flag":flag,"ativo":load().get(flag,False)})
@router.put("/{flag}")
async def set_flag(flag:str,request:Request):
    d=await request.json(); flags=load(); flags[flag]=d.get("ativo",False)
    ARQ.write_text(json.dumps(flags,indent=2))
    return JSONResponse({"ok":True,"flag":flag,"ativo":flags[flag]})
class Plugin(PluginBase):
    name = "feature_flags_v2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
