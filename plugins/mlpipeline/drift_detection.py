"""
Plugin: Drift Detection
Categoria: mlpipeline
Descrição: Detecção de data drift e concept drift em modelos ML em produção
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid
import statistics
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/drift", tags=["mlpipeline"])

monitores_db = {}
snapshots_db = {}
alertas_drift = []


class DriftDetectionPlugin(PluginBase):
    name = "drift_detection"
    version = "1.0.0"
    description = "Detecção de data drift e concept drift"
    category = "mlpipeline"

    def setup(self, app):
        app.include_router(router)
        logger.info(f"[{self.name}] Plugin carregado com sucesso")

    def health_check(self):
        return {
            "status": "healthy",
            "monitores_ativos": sum(1 for m in monitores_db.values() if m["ativo"]),
            "alertas_drift": len(alertas_drift)
        }


@router.post("/monitor/criar")
async def criar_monitor(
    nome: str,
    modelo_id: str,
    features_monitoradas: list,
    threshold_drift: float = 0.1
):
    """Cria monitor de drift para um modelo"""
    monitor_id = str(uuid.uuid4())[:8]
    monitores_db[monitor_id] = {
        "id": monitor_id,
        "nome": nome,
        "modelo_id": modelo_id,
        "features": features_monitoradas,
        "threshold": threshold_drift,
        "ativo": True,
        "criado_em": datetime.utcnow().isoformat(),
        "ultimo_check": None,
        "status_drift": "sem_drift"
    }
    snapshots_db[monitor_id] = []

    return {"monitor_id": monitor_id, "features": features_monitoradas, "status": "monitor criado"}


@router.post("/monitor/{monitor_id}/snapshot/referencia")
async def snapshot_referencia(monitor_id: str, dados: dict):
    """Cria snapshot de referência (dados de produção baseline)"""
    if monitor_id not in monitores_db:
        raise HTTPException(status_code=404, detail="Monitor não encontrado")

    snapshot = {
        "tipo": "referencia",
        "dados": dados,
        "estatisticas": _calcular_stats(dados),
        "criado_em": datetime.utcnow().isoformat()
    }
    snapshots_db[monitor_id].insert(0, snapshot)

    return {"status": "snapshot de referência criado", "estatisticas": snapshot["estatisticas"]}


@router.post("/monitor/{monitor_id}/checar-drift")
async def checar_drift(monitor_id: str, dados_atual: dict):
    """Verifica se há drift nos dados"""
    if monitor_id not in monitores_db:
        raise HTTPException(status_code=404, detail="Monitor não encontrado")

    monitor = monitores_db[monitor_id]
    snapshots = snapshots_db[monitor_id]

    # Precisar de referência
    ref = next((s for s in snapshots if s["tipo"] == "referencia"), None)
    if not ref:
        raise HTTPException(status_code=400, detail="Snapshot de referência necessário")

    stats_ref = ref["estatisticas"]
    stats_atual = _calcular_stats(dados_atual)

    # Calcular drift por feature
    drifts = {}
    features_com_drift = []

    for feature, stats in stats_ref.items():
        if feature in stats_atual:
            ref_media = stats.get("media", 0)
            atual_media = stats_atual[feature].get("media", 0)

            if ref_media != 0:
                drift = abs(atual_media - ref_media) / abs(ref_media)
            else:
                drift = abs(atual_media)

            drifts[feature] = {
                "drift_score": round(drift, 4),
                "referencia_media": ref_media,
                "atual_media": atual_media,
                "tem_drift": drift > monitor["threshold"]
            }
            if drift > monitor["threshold"]:
                features_com_drift.append(feature)

    nivel_drift = (
        "critico" if len(features_com_drift) >= len(drifts) * 0.7 else
        "moderado" if features_com_drift else
        "sem_drift"
    )

    monitor["ultimo_check"] = datetime.utcnow().isoformat()
    monitor["status_drift"] = nivel_drift

    if nivel_drift in ["critico", "moderado"]:
        alertas_drift.append({
            "monitor_id": monitor_id,
            "modelo_id": monitor["modelo_id"],
            "nivel": nivel_drift,
            "features_afetadas": features_com_drift,
            "timestamp": datetime.utcnow().isoformat()
        })

    return {
        "monitor_id": monitor_id,
        "nivel_drift": nivel_drift,
        "features_com_drift": features_com_drift,
        "detalhes": drifts,
        "recomendacao": "Re-treinar modelo" if nivel_drift == "critico" else
                        "Monitorar de perto" if nivel_drift == "moderado" else
                        "Modelo estável"
    }


@router.get("/alertas")
async def listar_alertas_drift():
    """Lista alertas de drift"""
    return {
        "total": len(alertas_drift),
        "alertas": alertas_drift[-20:]
    }


@router.get("/monitores")
async def listar_monitores():
    """Lista monitores ativos"""
    return {
        "total": len(monitores_db),
        "monitores": list(monitores_db.values())
    }


def _calcular_stats(dados: dict) -> dict:
    stats = {}
    for campo, valores in dados.items():
        if isinstance(valores, list):
            numericos = [v for v in valores if isinstance(v, (int, float))]
            if numericos:
                try:
                    stats[campo] = {
                        "media": round(statistics.mean(numericos), 4),
                        "desvio": round(statistics.stdev(numericos), 4) if len(numericos) > 1 else 0,
                        "min": round(min(numericos), 4),
                        "max": round(max(numericos), 4),
                        "n": len(numericos)
                    }
                except Exception:
                    stats[campo] = {"media": 0, "n": len(numericos)}
        elif isinstance(valores, (int, float)):
            stats[campo] = {"media": valores, "n": 1}
    return stats


plugin = DriftDetectionPlugin()
