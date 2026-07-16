"""
Plugin: Reações a Mensagens
Categoria: comunicacao
Descrição: Sistema de reações emocionais a mensagens (emojis terapêuticos)
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/reacoes", tags=["comunicacao"])

reacoes_db = {}
mensagens_reacoes = {}

EMOJIS_TERAPEUTICOS = {
    "apoio": "🤗",
    "forca": "💪",
    "amor": "❤️",
    "escuta": "👂",
    "paz": "☮️",
    "esperanca": "🌟",
    "gratidao": "🙏",
    "empatia": "💙",
    "coragem": "🦁",
    "acolhimento": "🫂",
    "crescimento": "🌱",
    "luz": "✨",
    "cuidado": "🌈",
    "resiliencia": "🔥",
    "serenidade": "🕊️"
}


class ReacoesMensagensPlugin(PluginBase):
    name = "reacoes_mensagens"
    version = "1.0.0"
    description = "Sistema de reações emocionais terapêuticas"
    category = "comunicacao"

    def setup(self, app):
        app.include_router(router)
        logger.info(f"[{self.name}] Plugin carregado com sucesso")

    def health_check(self):
        return {
            "status": "healthy",
            "total_reacoes": len(reacoes_db),
            "emojis_disponiveis": len(EMOJIS_TERAPEUTICOS)
        }


@router.get("/emojis")
async def listar_emojis_terapeuticos():
    """Lista todos os emojis terapêuticos disponíveis"""
    return {
        "total": len(EMOJIS_TERAPEUTICOS),
        "emojis": EMOJIS_TERAPEUTICOS
    }


@router.post("/reagir")
async def reagir_mensagem(
    mensagem_id: str,
    user_id: str,
    tipo_reacao: str
):
    """Adiciona uma reação emocional a uma mensagem"""
    if tipo_reacao not in EMOJIS_TERAPEUTICOS:
        raise HTTPException(
            status_code=400,
            detail=f"Reação inválida. Use: {list(EMOJIS_TERAPEUTICOS.keys())}"
        )

    reacao_id = str(uuid.uuid4())[:8]
    reacao = {
        "id": reacao_id,
        "mensagem_id": mensagem_id,
        "user_id": user_id,
        "tipo": tipo_reacao,
        "emoji": EMOJIS_TERAPEUTICOS[tipo_reacao],
        "timestamp": datetime.utcnow().isoformat()
    }
    reacoes_db[reacao_id] = reacao

    # Agrupar por mensagem
    if mensagem_id not in mensagens_reacoes:
        mensagens_reacoes[mensagem_id] = []
    mensagens_reacoes[mensagem_id].append(reacao)

    return {"status": "reação adicionada", "reacao": reacao}


@router.get("/mensagem/{mensagem_id}")
async def obter_reacoes_mensagem(mensagem_id: str):
    """Obtém todas as reações de uma mensagem"""
    reacoes = mensagens_reacoes.get(mensagem_id, [])

    # Contar por tipo
    contagem = {}
    for r in reacoes:
        tipo = r["tipo"]
        if tipo not in contagem:
            contagem[tipo] = {"emoji": r["emoji"], "count": 0}
        contagem[tipo]["count"] += 1

    return {
        "mensagem_id": mensagem_id,
        "total_reacoes": len(reacoes),
        "resumo": contagem,
        "reacoes": reacoes[-20:]
    }


@router.delete("/remover/{reacao_id}")
async def remover_reacao(reacao_id: str, user_id: str):
    """Remove uma reação"""
    if reacao_id not in reacoes_db:
        raise HTTPException(status_code=404, detail="Reação não encontrada")

    reacao = reacoes_db[reacao_id]
    if reacao["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Sem permissão")

    del reacoes_db[reacao_id]
    return {"status": "reação removida"}


@router.get("/stats/populares")
async def reacoes_mais_populares():
    """Estatísticas das reações mais usadas"""
    contagem = {}
    for r in reacoes_db.values():
        tipo = r["tipo"]
        contagem[tipo] = contagem.get(tipo, 0) + 1

    ranking = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
    return {
        "total_reacoes": len(reacoes_db),
        "ranking": [
            {"tipo": t, "emoji": EMOJIS_TERAPEUTICOS.get(t, ""), "count": c}
            for t, c in ranking
        ]
    }


plugin = ReacoesMensagensPlugin()
