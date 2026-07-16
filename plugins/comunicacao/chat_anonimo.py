"""
Plugin: Chat Anônimo
Categoria: comunicacao
Descrição: Sistema de chat anônimo para suporte emocional entre usuários
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/chat-anonimo", tags=["comunicacao"])

# Armazenamento em memória (produção usaria Redis/DB)
salas_anonimas = {}
mensagens_anonimas = {}
usuarios_anonimos = {}


class ChatAnonimoPlugin(PluginBase):
    name = "chat_anonimo"
    version = "1.0.0"
    description = "Sistema de chat anônimo para suporte emocional"
    category = "comunicacao"

    def setup(self, app):
        app.include_router(router)
        logger.info(f"[{self.name}] Plugin carregado com sucesso")

    def health_check(self):
        return {
            "status": "healthy",
            "salas_ativas": len(salas_anonimas),
            "usuarios_online": len(usuarios_anonimos)
        }


@router.post("/sala/criar")
async def criar_sala_anonima(tema: str = "suporte_geral", max_participantes: int = 10):
    """Cria uma sala de chat anônima"""
    sala_id = str(uuid.uuid4())[:8]
    salas_anonimas[sala_id] = {
        "id": sala_id,
        "tema": tema,
        "max_participantes": max_participantes,
        "participantes": [],
        "criado_em": datetime.utcnow().isoformat(),
        "ativa": True
    }
    mensagens_anonimas[sala_id] = []
    return {
        "sala_id": sala_id,
        "tema": tema,
        "status": "sala criada com sucesso",
        "link": f"/chat-anonimo/{sala_id}"
    }


@router.post("/sala/{sala_id}/entrar")
async def entrar_sala(sala_id: str):
    """Entra em uma sala anônima com identidade gerada"""
    if sala_id not in salas_anonimas:
        raise HTTPException(status_code=404, detail="Sala não encontrada")

    sala = salas_anonimas[sala_id]
    if len(sala["participantes"]) >= sala["max_participantes"]:
        raise HTTPException(status_code=400, detail="Sala cheia")

    # Gerar identidade anônima
    nomes_anonimos = [
        "Estrela", "Lua", "Sol", "Nuvem", "Rio", "Mar", "Montanha",
        "Floresta", "Vento", "Chuva", "Aurora", "Cometa", "Raio",
        "Brisa", "Onda", "Coral", "Cristal", "Safira", "Rubi", "Jade"
    ]
    numero = len(sala["participantes"]) + 1
    nome_idx = (numero - 1) % len(nomes_anonimos)
    nome_anonimo = f"{nomes_anonimos[nome_idx]}_{numero}"

    user_id = str(uuid.uuid4())[:8]
    usuarios_anonimos[user_id] = {
        "id": user_id,
        "nome_anonimo": nome_anonimo,
        "sala_id": sala_id,
        "entrou_em": datetime.utcnow().isoformat()
    }
    sala["participantes"].append(user_id)

    return {
        "user_id": user_id,
        "nome_anonimo": nome_anonimo,
        "sala_id": sala_id,
        "participantes_na_sala": len(sala["participantes"])
    }


@router.post("/sala/{sala_id}/mensagem")
async def enviar_mensagem(sala_id: str, user_id: str, texto: str):
    """Envia mensagem anônima na sala"""
    if sala_id not in salas_anonimas:
        raise HTTPException(status_code=404, detail="Sala não encontrada")
    if user_id not in usuarios_anonimos:
        raise HTTPException(status_code=403, detail="Usuário não registrado")

    usuario = usuarios_anonimos[user_id]
    mensagem = {
        "id": str(uuid.uuid4())[:8],
        "de": usuario["nome_anonimo"],
        "texto": texto[:500],  # Limite de 500 chars
        "timestamp": datetime.utcnow().isoformat(),
        "tipo": "texto"
    }
    mensagens_anonimas[sala_id].append(mensagem)

    # Manter apenas últimas 200 mensagens por sala
    if len(mensagens_anonimas[sala_id]) > 200:
        mensagens_anonimas[sala_id] = mensagens_anonimas[sala_id][-200:]

    return {"status": "enviada", "mensagem": mensagem}


@router.get("/sala/{sala_id}/mensagens")
async def listar_mensagens(sala_id: str, ultimas: int = 50):
    """Lista mensagens da sala"""
    if sala_id not in salas_anonimas:
        raise HTTPException(status_code=404, detail="Sala não encontrada")

    msgs = mensagens_anonimas.get(sala_id, [])
    return {
        "sala_id": sala_id,
        "total": len(msgs),
        "mensagens": msgs[-ultimas:]
    }


@router.get("/salas")
async def listar_salas():
    """Lista salas ativas"""
    salas = []
    for sid, sala in salas_anonimas.items():
        if sala["ativa"]:
            salas.append({
                "id": sid,
                "tema": sala["tema"],
                "participantes": len(sala["participantes"]),
                "max": sala["max_participantes"],
                "criado_em": sala["criado_em"]
            })
    return {"salas_ativas": len(salas), "salas": salas}


plugin = ChatAnonimoPlugin()
