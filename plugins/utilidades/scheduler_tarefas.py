"""Agendador de tarefas automaticas (backup diario, etc)"""
import os
import logging
from datetime import datetime
from fastapi import APIRouter
from plugins.plugin_base import PluginBase
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import asyncio

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/scheduler", tags=["Scheduler"])

scheduler = BackgroundScheduler(timezone="America/Sao_Paulo")

async def tarefa_backup_diario():
    """Executa backup e envia por email todo dia"""
    try:
        from plugins.seguranca.backup_real import fazer_backup_sql, enviar_backup_email, alertar_telegram, BACKUP_DIR, limpar_backups_antigos
        
        resultado = fazer_backup_sql()
        if not resultado["sucesso"]:
            await alertar_telegram(f"❌ BACKUP AUTOMATICO FALHOU\n\nErro: {resultado.get('erro','')}")
            return
        
        limpar_backups_antigos(dias=7)
        arquivo_path = BACKUP_DIR / resultado["arquivo"]
        email_ok = await enviar_backup_email(arquivo_path)
        
        if email_ok:
            await alertar_telegram(
                f"💾 BACKUP AUTOMATICO DIARIO\n\n"
                f"Arquivo: {resultado['arquivo']}\n"
                f"Tamanho: {resultado['tamanho_kb']} KB\n"
                f"Tabelas: {resultado['total_tabelas']}\n"
                f"Registros: {resultado['total_registros']}\n\n"
                f"Salvo no seu Gmail!"
            )
        else:
            await alertar_telegram(
                f"⚠️ BACKUP FEITO MAS EMAIL FALHOU\n\n"
                f"Arquivo: {resultado['arquivo']}"
            )
    except Exception as e:
        logger.error(f"Erro backup diario: {e}")

def executar_tarefa_async(tarefa):
    """Wrapper para rodar tarefa async no scheduler"""
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(tarefa())
        loop.close()
    except Exception as e:
        logger.error(f"Erro executar tarefa: {e}")

def iniciar_agendador():
    """Inicia o agendador com todas as tarefas"""
    try:
        if scheduler.running:
            return
        
        # Backup todo dia as 3h da manha
        scheduler.add_job(
            executar_tarefa_async,
            trigger=CronTrigger(hour=3, minute=0),
            args=[tarefa_backup_diario],
            id="backup_diario",
            replace_existing=True,
            name="Backup diario do banco"
        )
        
        scheduler.start()
        logger.info("Scheduler iniciado")
    except Exception as e:
        logger.error(f"Erro iniciar scheduler: {e}")

@router.get("/status")
async def status():
    jobs = []
    if scheduler.running:
        for job in scheduler.get_jobs():
            jobs.append({
                "id": job.id,
                "nome": job.name,
                "proxima_execucao": job.next_run_time.isoformat() if job.next_run_time else None
            })
    return {
        "scheduler_ativo": scheduler.running,
        "total_tarefas": len(jobs),
        "tarefas": jobs
    }

@router.post("/executar/{tarefa_id}")
async def executar_manual(tarefa_id: str):
    """Executa uma tarefa manualmente"""
    if tarefa_id == "backup_diario":
        await tarefa_backup_diario()
        return {"status": "executado", "tarefa": tarefa_id}
    return {"erro": "tarefa nao encontrada"}

class SchedulerPlugin(PluginBase):
    name = "scheduler_tarefas"
    def setup(self, app):
        app.include_router(router)
        iniciar_agendador()

plugin = SchedulerPlugin()
