"""
Plugin: Data Validation
Categoria: mlpipeline
Descrição: Validação de qualidade de dados para pipelines ML
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid
import statistics
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/data-validation", tags=["mlpipeline"])

validacoes_db = {}
schemas_db = {}


class DataValidationPlugin(PluginBase):
    name = "data_validation"
    version = "1.0.0"
    description = "Validação de qualidade de dados para ML"
    category = "mlpipeline"

    def setup(self, app):
        app.include_router(router)
        logger.info(f"[{self.name}] Plugin carregado com sucesso")

    def health_check(self):
        return {
            "status": "healthy",
            "validacoes_realizadas": len(validacoes_db),
            "schemas_definidos": len(schemas_db)
        }


@router.post("/schema/definir")
async def definir_schema(
    nome: str,
    campos: dict
):
    """Define schema de validação para um dataset"""
    schema_id = str(uuid.uuid4())[:8]
    schemas_db[schema_id] = {
        "id": schema_id,
        "nome": nome,
        "campos": campos,
        "criado_em": datetime.utcnow().isoformat()
    }
    return {"schema_id": schema_id, "campos": len(campos), "status": "schema definido"}


@router.post("/validar/dataset")
async def validar_dataset(dados: list, schema_id: str = None):
    """Valida qualidade de um dataset"""
    if not dados:
        raise HTTPException(status_code=400, detail="Dataset vazio")

    if len(dados) > 10000:
        raise HTTPException(status_code=400, detail="Máximo 10.000 registros por validação")

    problemas = []
    metricas = {}

    # Verificar campos
    campos = set()
    for registro in dados:
        campos.update(registro.keys())

    # Verificar valores nulos
    for campo in campos:
        valores = [r.get(campo) for r in dados]
        nulos = sum(1 for v in valores if v is None or v == "")
        if nulos > 0:
            taxa_nulo = nulos / len(dados)
            if taxa_nulo > 0.1:
                problemas.append({
                    "tipo": "valores_nulos",
                    "campo": campo,
                    "count": nulos,
                    "taxa": round(taxa_nulo, 4),
                    "severidade": "alta" if taxa_nulo > 0.3 else "media"
                })

        # Verificar outliers para campos numéricos
        numericos = [v for v in valores if isinstance(v, (int, float)) and v is not None]
        if len(numericos) > 5:
            try:
                media = statistics.mean(numericos)
                desvio = statistics.stdev(numericos)
                outliers = sum(1 for v in numericos if abs(v - media) > 3 * desvio)
                if outliers > 0:
                    problemas.append({
                        "tipo": "outliers",
                        "campo": campo,
                        "count": outliers,
                        "taxa": round(outliers / len(numericos), 4),
                        "severidade": "baixa"
                    })
            except statistics.StatisticsError:
                pass

        metricas[campo] = {
            "total": len(valores),
            "nulos": nulos,
            "taxa_preenchimento": round(1 - nulos / len(dados), 4)
        }

    # Verificar duplicatas
    registros_str = [str(sorted(r.items())) for r in dados]
    duplicatas = len(registros_str) - len(set(registros_str))
    if duplicatas > 0:
        problemas.append({
            "tipo": "duplicatas",
            "count": duplicatas,
            "taxa": round(duplicatas / len(dados), 4),
            "severidade": "media"
        })

    # Score de qualidade
    score = 100
    for p in problemas:
        if p["severidade"] == "alta":
            score -= 20
        elif p["severidade"] == "media":
            score -= 10
        else:
            score -= 5
    score = max(0, score)

    val_id = str(uuid.uuid4())[:8]
    validacao = {
        "id": val_id,
        "total_registros": len(dados),
        "campos": list(campos),
        "score_qualidade": score,
        "status": "aprovado" if score >= 70 else "reprovado",
        "problemas": problemas,
        "metricas_por_campo": metricas,
        "validado_em": datetime.utcnow().isoformat()
    }
    validacoes_db[val_id] = validacao

    return validacao


@router.get("/validacao/{val_id}")
async def obter_validacao(val_id: str):
    """Obtém resultado de uma validação"""
    if val_id not in validacoes_db:
        raise HTTPException(status_code=404, detail="Validação não encontrada")
    return validacoes_db[val_id]


@router.get("/stats")
async def stats_validacao():
    """Estatísticas das validações"""
    total = len(validacoes_db)
    aprovados = sum(1 for v in validacoes_db.values() if v["status"] == "aprovado")
    return {
        "total_validacoes": total,
        "aprovados": aprovados,
        "reprovados": total - aprovados,
        "taxa_aprovacao": round(aprovados / total, 4) if total > 0 else 0
    }


plugin = DataValidationPlugin()
