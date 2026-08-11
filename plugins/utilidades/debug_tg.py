
from fastapi import APIRouter
from plugins.plugin_base import PluginBase
import os

router = APIRouter(prefix="/api/v1/debug", tags=["Debug"])

@router.get("/tg-sync")
def tg_sync():
    import requests
    tok = os.getenv("TELEGRAM_TOKEN")
    cid = os.getenv("TELEGRAM_CHAT_ID")
    if not tok or not cid:
        return {"erro": "sem token/chat_id"}
    try:
        r = requests.post(
            f"https://api.telegram.org/bot{tok}/sendMessage",
            json={"chat_id": cid, "text": "TESTE SYNC OK"},
            timeout=10
        )
        return {"status": r.status_code, "resp": r.text[:200]}
    except Exception as e:
        return {"erro": str(e), "tipo": type(e).__name__}

class DbgPlugin(PluginBase):
    name = "debug_tg"
    def setup(self, app):
        app.include_router(router)

plugin = DbgPlugin()
