"""
Plugin: Voice Notes
Categoria: comunicacao
Descrição: Sistema de notas de voz para comunicação emocional assíncrona
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException, UploadFile, File
from datetime import datetime
import uuid
import base64
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/voice-notes", tags=["comunicacao"])

voice_notes_db = {}
transcricoes_db = {}


class VoiceNotesPlugin(PluginBase):
    name = "voice_notes"
    version = "1.0.0"
    description = "Sistema de notas de voz para comunicação emocional"
    category = "comunicacao"

    def setup(self, app):
        app.include_router(router)
        logger.info(f"[{self.name}] Plugin carregado com sucesso")

    def health_check(self):
        return {
            "status": "healthy",
            "total_notas": len(voice_notes_db)
        }


@router.post("/gravar")
async def gravar_voice_note(
    user_id: str,
    duracao_segundos: float = 0,
    emocao_detectada: str = "neutro",
    descricao: str = ""
):
    """Registra uma nota de voz"""
    nota_id = str(uuid.uuid4())[:8]
    voice_notes_db[nota_id] = {
        "id": nota_id,
        "user_id": user_id,
        "duracao_segundos": duracao_segundos,
        "emocao_detectada": emocao_detectada,
        "descricao": descricao,
        "criado_em": datetime.utcnow().isoformat(),
        "transcrito": False,
        "analise_emocional": {
            "emocao_principal": emocao_detectada,
            "confianca": 0.85,
            "valencia": _calcular_valencia(emocao_detectada),
            "intensidade": 0.7
        }
    }
    return {
        "nota_id": nota_id,
        "status": "gravada",
        "analise": voice_notes_db[nota_id]["analise_emocional"]
    }


@router.get("/usuario/{user_id}")
async def listar_notas_usuario(user_id: str, limite: int = 20):
    """Lista notas de voz de um usuário"""
    notas = [n for n in voice_notes_db.values() if n["user_id"] == user_id]
    notas.sort(key=lambda x: x["criado_em"], reverse=True)
    return {
        "user_id": user_id,
        "total": len(notas),
        "notas": notas[:limite]
    }


@router.get("/{nota_id}")
async def obter_nota(nota_id: str):
    """Obtém detalhes de uma nota de voz"""
    if nota_id not in voice_notes_db:
        raise HTTPException(status_code=404, detail="Nota não encontrada")
    return voice_notes_db[nota_id]


@router.post("/{nota_id}/transcrever")
async def transcrever_nota(nota_id: str):
    """Simula transcrição de nota de voz"""
    if nota_id not in voice_notes_db:
        raise HTTPException(status_code=404, detail="Nota não encontrada")

    # Simulação de transcrição
    transcricao = {
        "nota_id": nota_id,
        "texto": f"[Transcrição simulada da nota {nota_id}]",
        "idioma": "pt-BR",
        "confianca": 0.92,
        "palavras_chave": ["emoção", "sentimento", "reflexão"],
        "transcrito_em": datetime.utcnow().isoformat()
    }
    transcricoes_db[nota_id] = transcricao
    voice_notes_db[nota_id]["transcrito"] = True

    return transcricao


@router.get("/stats/resumo")
async def stats_voice_notes():
    """Estatísticas gerais de voice notes"""
    total = len(voice_notes_db)
    emocoes = {}
    duracao_total = 0
    for nota in voice_notes_db.values():
        emocao = nota.get("emocao_detectada", "neutro")
        emocoes[emocao] = emocoes.get(emocao, 0) + 1
        duracao_total += nota.get("duracao_segundos", 0)

    return {
        "total_notas": total,
        "duracao_total_segundos": duracao_total,
        "emocoes_distribuicao": emocoes,
        "media_duracao": duracao_total / total if total > 0 else 0
    }


def _calcular_valencia(emocao: str) -> float:
    valenciais = {
        "feliz": 0.9, "alegre": 0.85, "grato": 0.8, "calmo": 0.7,
        "neutro": 0.5, "ansioso": 0.3, "triste": 0.2, "raiva": 0.1,
        "medo": 0.15, "surpreso": 0.6
    }
    return valenciais.get(emocao.lower(), 0.5)


plugin = VoiceNotesPlugin()
