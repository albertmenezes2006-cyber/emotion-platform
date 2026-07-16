"""
Plugin: Dashboard Analytics
Categoria: datascience
Descrição: Dashboard centralizado de analytics emocionais em tempo real
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter
from datetime import datetime, timedelta
import uuid
import random
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/dashboard-analytics", tags=["datascience"])

eventos_db = []
metricas_cache = {}


class DashboardAnalyticsPlugin(PluginBase):
    name = "dashboard_analytics"
    version = "1.0.0"
    description = "Dashboard centralizado de analytics emocionais"
    category = "datascience"

    def setup(self, app):
        app.include_router(router)
        logger.info(f"[{self.name}] Plugin carregado com sucesso")

    def health_check(self):
        return {
            "status": "healthy",
            "eventos_registrados": len(eventos_db)
        }


@router.post("/evento")
async def registrar_evento(
    tipo: str,
    user_id: str = None,
    valor: float = None,
    metadata: dict = None
):
    """Registra um evento de analytics"""
    evento = {
        "id": str(uuid.uuid4())[:8],
        "tipo": tipo,
        "user_id": user_id,
        "valor": valor,
        "metadata": metadata or {},
        "timestamp": datetime.utcnow().isoformat()
    }
    eventos_db.append(evento)
    if len(eventos_db) > 10000:
        eventos_db.pop(0)
    return {"status": "evento registrado", "evento_id": evento["id"]}


@router.get("/overview")
async def dashboard_overview():
    """Visão geral do dashboard"""
    agora = datetime.utcnow()
    inicio_hoje = agora.replace(hour=0, minute=0, second=0, microsecond=0)
    inicio_semana = agora - timedelta(days=7)

    eventos_hoje = [e for e in eventos_db if e["timestamp"] >= inicio_hoje.isoformat()]
    eventos_semana = [e for e in eventos_db if e["timestamp"] >= inicio_semana.isoformat()]

    usuarios_unicos = len(set(e["user_id"] for e in eventos_semana if e.get("user_id")))

    # Distribuição por tipo
    tipos = {}
    for e in eventos_semana:
        t = e["tipo"]
        tipos[t] = tipos.get(t, 0) + 1

    # Métricas simuladas se poucos dados reais
    if not eventos_db:
        return {
            "status": "sem dados",
            "recomendacao": "Registre eventos usando POST /api/v1/dashboard-analytics/evento"
        }

    return {
        "periodo": "últimos 7 dias",
        "gerado_em": agora.isoformat(),
        "resumo": {
            "eventos_hoje": len(eventos_hoje),
            "eventos_semana": len(eventos_semana),
            "usuarios_ativos_semana": usuarios_unicos,
            "tipos_eventos": len(tipos)
        },
        "distribuicao_eventos": tipos,
        "tendencia_diaria": _calcular_tendencia_diaria(),
        "top_usuarios": _top_usuarios(eventos_semana, 5)
    }


@router.get("/metricas/emocional")
async def metricas_emocionais():
    """Métricas emocionais agregadas"""
    eventos_emocao = [e for e in eventos_db if e["tipo"].startswith("emocao_")]

    if not eventos_emocao:
        return {"status": "sem dados emocionais", "dica": "Use tipo='emocao_*' ao registrar eventos"}

    valores = [e["valor"] for e in eventos_emocao if e.get("valor") is not None]
    media_bem_estar = sum(valores) / len(valores) if valores else 0

    return {
        "total_registros_emocionais": len(eventos_emocao),
        "media_bem_estar": round(media_bem_estar, 3),
        "distribuicao": _distribuicao_emocional(eventos_emocao)
    }


@router.get("/metricas/engajamento")
async def metricas_engajamento():
    """Métricas de engajamento da plataforma"""
    total = len(eventos_db)
    usuarios = set(e["user_id"] for e in eventos_db if e.get("user_id"))

    return {
        "total_eventos": total,
        "usuarios_unicos": len(usuarios),
        "media_eventos_por_usuario": round(total / max(len(usuarios), 1), 2),
        "tipos_mais_usados": _top_tipos(10),
        "horarios_pico": _horarios_pico()
    }


@router.get("/relatorio/diario")
async def relatorio_diario():
    """Relatório diário consolidado"""
    hoje = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    eventos_hoje = [e for e in eventos_db if e["timestamp"] >= hoje.isoformat()]

    tipos_hoje = {}
    for e in eventos_hoje:
        t = e["tipo"]
        tipos_hoje[t] = tipos_hoje.get(t, 0) + 1

    return {
        "data": hoje.strftime("%Y-%m-%d"),
        "total_eventos": len(eventos_hoje),
        "por_tipo": tipos_hoje,
        "usuarios_ativos": len(set(e.get("user_id", "") for e in eventos_hoje)),
        "gerado_em": datetime.utcnow().isoformat()
    }


def _calcular_tendencia_diaria() -> list:
    """Calcula eventos por dia dos últimos 7 dias"""
    resultado = []
    for i in range(7, 0, -1):
        data = (datetime.utcnow() - timedelta(days=i)).strftime("%Y-%m-%d")
        count = sum(1 for e in eventos_db if e["timestamp"].startswith(data))
        resultado.append({"data": data, "eventos": count})
    return resultado


def _top_usuarios(eventos: list, n: int) -> list:
    contagem = {}
    for e in eventos:
        uid = e.get("user_id", "anonimo")
        contagem[uid] = contagem.get(uid, 0) + 1
    return sorted([{"user_id": k, "eventos": v} for k, v in contagem.items()],
                  key=lambda x: x["eventos"], reverse=True)[:n]


def _top_tipos(n: int) -> list:
    tipos = {}
    for e in eventos_db:
        t = e["tipo"]
        tipos[t] = tipos.get(t, 0) + 1
    return sorted([{"tipo": k, "count": v} for k, v in tipos.items()],
                  key=lambda x: x["count"], reverse=True)[:n]


def _horarios_pico() -> list:
    horas = {}
    for e in eventos_db:
        try:
            hora = int(e["timestamp"][11:13])
            horas[hora] = horas.get(hora, 0) + 1
        except Exception:
            pass
    return sorted([{"hora": k, "eventos": v} for k, v in horas.items()],
                  key=lambda x: x["eventos"], reverse=True)[:5]


def _distribuicao_emocional(eventos: list) -> dict:
    dist = {}
    for e in eventos:
        tipo = e["tipo"].replace("emocao_", "")
        dist[tipo] = dist.get(tipo, 0) + 1
    return dist


plugin = DashboardAnalyticsPlugin()
