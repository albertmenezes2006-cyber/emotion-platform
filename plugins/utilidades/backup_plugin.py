
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, BackgroundTasks
import json, subprocess, pathlib, logging
from datetime import datetime
logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/backup", tags=["Backup"])
BDIR = pathlib.Path("backups")
BDIR.mkdir(exist_ok=True)

def fazer_backup():
    ts   = datetime.now().strftime("%Y%m%d_%H%M%S")
    info = {"timestamp":ts,"versao":"24.4.0","git":{},"stats":{}}
    try:
        r  = subprocess.run(["git","log","--oneline","-5"],capture_output=True,text=True)
        r2 = subprocess.run(["git","rev-parse","HEAD"],capture_output=True,text=True)
        info["git"] = {"commits":r.stdout.strip().split("\n"),"head":r2.stdout.strip()}
    except: pass
    pdir = pathlib.Path("plugins")
    info["stats"]["plugins"] = sum(1 for f in pdir.rglob("*.py") if f.name not in {"__init__.py","loader.py","plugin_base.py","db_manager.py"})
    req = pathlib.Path("requirements.txt")
    if req.exists(): info["requirements"] = req.read_text()[:500]
    bp = BDIR / f"backup_{ts}.json"
    bp.write_text(json.dumps(info,indent=2,ensure_ascii=False))
    for old in sorted(BDIR.glob("backup_*.json"))[:-7]: old.unlink()
    logger.info(f"[Backup] {bp.name}")
    return bp.name

@router.post("/criar")
async def criar(bg: BackgroundTasks):
    bg.add_task(fazer_backup)
    return {"msg":"Backup iniciado","status":"ok"}

@router.get("/listar")
async def listar():
    bs = sorted(BDIR.glob("backup_*.json"),reverse=True)
    return {"backups":[{"arquivo":b.name,"kb":round(b.stat().st_size/1024,1)} for b in bs],"total":len(bs)}

@router.get("/ultimo")
async def ultimo():
    bs = sorted(BDIR.glob("backup_*.json"),reverse=True)
    if not bs:
        nome = fazer_backup()
        return {"msg":"Primeiro backup criado!","arquivo":nome}
    d = json.loads(bs[0].read_text())
    return {"arquivo":bs[0].name,"timestamp":d.get("timestamp"),"plugins":d.get("stats",{}).get("plugins",0)}

@router.get("/status")
async def status():
    bs = list(BDIR.glob("backup_*.json"))
    return {"status":"online","total":len(bs),"retencao":"7 dias","dir":str(BDIR)}



@router.get('/recente')
async def recente():
    bs = sorted(BDIR.glob('backup_*.json'), reverse=True)
    if not bs:
        return {'msg': 'Nenhum backup ainda', 'total': 0, 'status': 'vazio'}
    d = __import__('json').loads(bs[0].read_text())
    return {'arquivo': bs[0].name, 'timestamp': d.get('timestamp'),
            'versao': d.get('versao'), 'plugins': d.get('stats',{}).get('plugins',0),
            'total': len(bs)}
class BackupPlugin(PluginBase):
    name="backup_plugin"; version="1.0.0"
    description="Backup automatico diario"; category="utilidades"
    def setup(self,app):
        app.include_router(router)
        try: fazer_backup()
        except Exception as e: logger.warning(f"[Backup] {e}")
        logger.info("[Backup] OK")
    def health_check(self):
        return {"status":"healthy","backups":len(list(BDIR.glob("backup_*.json")))}

plugin = BackupPlugin()
