"""
Plugin: Transcrição ao Vivo
Categoria: comunicacao
Descrição: Sistema de transcrição em tempo real para sessões terapêuticas
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/transcricao-live", tags=["comunicacao"])

sessoes_transcricao = {}
segmentos_db = {}


class TranscricaoAoVivoPlugin(PluginBase):
    name = "transcricao_ao_vivo"
    version = "1.0.0"
    description = "Transcrição em tempo real para sessões terapêuticas"
    category = "comunicacao"

    def setup(self, app):
        app.include_router(router)
        logger.info(f"[{self.name}] Plugin carregado com sucesso")

    def health_check(self):
        return {
            "status": "healthy",
            "sessoes_ativas": sum(1 for s in sessoes_transcricao.values() if s["status"] == "ativa")
        }


@router.post("/sessao/iniciar")
async def iniciar_sessao(
    terapeuta_id: str,
    paciente_id: str = "anonimo",
    idioma: str = "pt-BR"
):
    """Inicia uma sessão de transcrição ao vivo"""
    sessao_id = str(uuid.uuid4())[:8]
    sessoes_transcricao[sessao_id] = {
        "id": sessao_id,
        "terapeuta_id": terapeuta_id,
        "paciente_id": paciente_id,
        "idioma": idioma,
        "status": "ativa",
        "inicio": datetime.utcnow().isoformat(),
        "fim": None,
        "total_segmentos": 0,
        "palavras_totais": 0,
        "emocoes_detectadas": []
    }
    segmentos_db[sessao_id] = []

    return {
        "sessao_id": sessao_id,
        "status": "sessão de transcrição iniciada",
        "idioma": idioma
    }


@router.post("/sessao/{sessao_id}/segmento")
async def adicionar_segmento(
    sessao_id: str,
    texto: str,
    falante: str = "paciente",
    emocao: str = "neutro",
    confianca: float = 0.9
):
    """Adiciona um segmento de transcrição"""
    if sessao_id not in sessoes_transcricao:
        raise HTTPException(status_code=404, detail="Sessão não encontrada")

    sessao = sessoes_transcricao[sessao_id]
    if sessao["status"] != "ativa":
        raise HTTPException(status_code=400, detail="Sessão não está ativa")

    segmento = {
        "id": len(segmentos_db[sessao_id]) + 1,
        "texto": texto,
        "falante": falante,
        "emocao": emocao,
        "confianca": confianca,
        "timestamp": datetime.utcnow().isoformat(),
        "palavras": len(texto.split())
    }
    segmentos_db[sessao_id].append(segmento)

    # Atualizar stats da sessão
    sessao["total_segmentos"] += 1
    sessao["palavras_totais"] += segmento["palavras"]
    if emocao != "neutro":
        sessao["emocoes_detectadas"].append(emocao)

    return {"status": "segmento adicionado", "segmento": segmento}


@router.post("/sessao/{sessao_id}/finalizar")
async def finalizar_sessao(sessao_id: str):
    """Finaliza sessão de transcrição"""
    if sessao_id not in sessoes_transcricao:
        raise HTTPException(status_code=404, detail="Sessão não encontrada")

    sessao = sessoes_transcricao[sessao_id]
    sessao["status"] = "finalizada"
    sessao["fim"] = datetime.utcnow().isoformat()

    # Gerar resumo
    segmentos = segmentos_db.get(sessao_id, [])
    emocoes_count = {}
    for seg in segmentos:
        e = seg.get("emocao", "neutro")
        emocoes_count[e] = emocoes_count.get(e, 0) + 1

    resumo = {
        "sessao_id": sessao_id,
        "duracao_segmentos": sessao["total_segmentos"],
        "palavras_totais": sessao["palavras_totais"],
        "distribuicao_emocoes": emocoes_count,
        "emocao_predominante": max(emocoes_count, key=emocoes_count.get) if emocoes_count else "neutro"
    }

    return {"status": "finalizada", "resumo": resumo}


@router.get("/sessao/{sessao_id}")
async def obter_sessao(sessao_id: str):
    """Obtém detalhes da sessão"""
    if sessao_id not in sessoes_transcricao:
        raise HTTPException(status_code=404, detail="Sessão não encontrada")

    return {
        "sessao": sessoes_transcricao[sessao_id],
        "segmentos": segmentos_db.get(sessao_id, [])[-50:]
    }


@router.get("/sessoes/ativas")
async def listar_sessoes_ativas():
    """Lista sessões de transcrição ativas"""
    ativas = [s for s in sessoes_transcricao.values() if s["status"] == "ativa"]
    return {"total_ativas": len(ativas), "sessoes": ativas}


plugin = TranscricaoAoVivoPlugin()
