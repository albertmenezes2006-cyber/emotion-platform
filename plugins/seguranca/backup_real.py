"""Backup automatico real do PostgreSQL Neon"""
import os
import logging
import subprocess
import gzip
from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from plugins.plugin_base import PluginBase
from pathlib import Path
import httpx

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/backup-real", tags=["Backup"])

BACKUP_DIR = Path("/tmp/backups_emotionai")
BACKUP_DIR.mkdir(exist_ok=True)

def get_db_url():
    return os.getenv("DATABASE_URL", "")

async def alertar_telegram(msg: str):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        return
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            await client.post(
                f"https://api.telegram.org/bot{token}/sendMessage",
                json={"chat_id": chat_id, "text": msg}
            )
    except:
        pass

def fazer_backup_sql():
    """Faz backup via SELECT (sem pg_dump)"""
    try:
        import psycopg2
        conn = psycopg2.connect(get_db_url())
        cur = conn.cursor()
        
        # Lista todas as tabelas
        cur.execute("SELECT tablename FROM pg_tables WHERE schemaname = \'public\'")
        tabelas = [r[0] for r in cur.fetchall()]
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        arquivo = BACKUP_DIR / f"backup_{timestamp}.sql.gz"
        
        total_registros = 0
        with gzip.open(arquivo, "wt", encoding="utf-8") as f:
            f.write(f"-- Backup EmotionAI - {datetime.now().isoformat()}\n\n")
            
            for tabela in tabelas:
                try:
                    cur.execute(f"SELECT COUNT(*) FROM {tabela}")
                    n = cur.fetchone()[0]
                    total_registros += n
                    f.write(f"\n-- Tabela: {tabela} ({n} registros)\n")
                    
                    if n > 0 and n < 10000:  # Só exporta tabelas com menos de 10k registros
                        cur.execute(f"SELECT * FROM {tabela}")
                        colunas = [d[0] for d in cur.description]
                        for row in cur.fetchall():
                            valores = ["NULL" if v is None else repr(str(v)) for v in row]
                            f.write(f"INSERT INTO {tabela} ({','.join(colunas)}) VALUES ({','.join(valores)});\n")
                except Exception as e:
                    f.write(f"-- Erro tabela {tabela}: {e}\n")
        
        cur.close()
        conn.close()
        
        tamanho = arquivo.stat().st_size / 1024
        return {
            "sucesso": True,
            "arquivo": str(arquivo.name),
            "tamanho_kb": round(tamanho, 2),
            "total_tabelas": len(tabelas),
            "total_registros": total_registros,
            "timestamp": timestamp
        }
    except Exception as e:
        logger.error(f"Erro backup: {e}")
        return {"sucesso": False, "erro": str(e)}

def limpar_backups_antigos(dias: int = 7):
    """Remove backups com mais de N dias"""
    limite = datetime.now() - timedelta(days=dias)
    removidos = 0
    for arq in BACKUP_DIR.glob("backup_*.sql.gz"):
        if datetime.fromtimestamp(arq.stat().st_mtime) < limite:
            arq.unlink()
            removidos += 1
    return removidos

@router.post("/executar")
async def executar_backup():
    """Faz backup manual agora"""
    resultado = fazer_backup_sql()
    if resultado["sucesso"]:
        limpar_backups_antigos(dias=7)
        await alertar_telegram(
            f"💾 BACKUP REALIZADO\n\n"
            f"Arquivo: {resultado['arquivo']}\n"
            f"Tamanho: {resultado['tamanho_kb']} KB\n"
            f"Tabelas: {resultado['total_tabelas']}\n"
            f"Registros: {resultado['total_registros']}"
        )
    return resultado

@router.get("/listar")
async def listar_backups():
    arquivos = sorted(BACKUP_DIR.glob("backup_*.sql.gz"), reverse=True)
    return {
        "total": len(arquivos),
        "backups": [
            {
                "nome": a.name,
                "tamanho_kb": round(a.stat().st_size / 1024, 2),
                "criado_em": datetime.fromtimestamp(a.stat().st_mtime).isoformat()
            }
            for a in arquivos[:20]
        ]
    }

@router.get("/download/{nome_arquivo}")
async def download_backup(nome_arquivo: str):
    arquivo = BACKUP_DIR / nome_arquivo
    if not arquivo.exists() or ".." in nome_arquivo:
        raise HTTPException(404, "Backup nao encontrado")
    return FileResponse(str(arquivo), filename=nome_arquivo, media_type="application/gzip")

@router.get("/status")
async def status():
    arquivos = list(BACKUP_DIR.glob("backup_*.sql.gz"))
    ultimo = None
    if arquivos:
        mais_recente = max(arquivos, key=lambda a: a.stat().st_mtime)
        ultimo = {
            "nome": mais_recente.name,
            "quando": datetime.fromtimestamp(mais_recente.stat().st_mtime).isoformat(),
            "tamanho_kb": round(mais_recente.stat().st_size / 1024, 2)
        }
    return {
        "total_backups": len(arquivos),
        "ultimo_backup": ultimo,
        "pasta": str(BACKUP_DIR)
    }

class BackupRealPlugin(PluginBase):
    name = "backup_real"
    def setup(self, app):
        app.include_router(router)

plugin = BackupRealPlugin()
