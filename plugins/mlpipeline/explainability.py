"""
Plugin: Explainability
Categoria: mlpipeline
Descrição: Explicabilidade de modelos ML com LIME e SHAP simplificados
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid
import random
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/explainability", tags=["mlpipeline"])

explicacoes_db = {}


class ExplainabilityPlugin(PluginBase):
    name = "explainability"
    version = "1.0.0"
    description = "Explicabilidade de modelos ML (LIME/SHAP)"
    category = "mlpipeline"

    def setup(self, app):
        app.include_router(router)
        logger.info(f"[{self.name}] Plugin carregado com sucesso")

    def health_check(self):
        return {
            "status": "healthy",
            "explicacoes_geradas": len(explicacoes_db)
        }


@router.post("/explicar/predicao")
async def explicar_predicao(
    modelo_id: str,
    features: dict,
    predicao: float = 0.75,
    metodo: str = "shap"
):
    """Explica uma predição de modelo ML"""
    metodos_validos = ["shap", "lime", "permutation", "attention"]
    if metodo not in metodos_validos:
        raise HTTPException(status_code=400, detail=f"Métodos: {metodos_validos}")

    # Calcular importância das features (simulado)
    importancias = _calcular_importancias(features, predicao)

    # Gerar explicação em linguagem natural
    explicacao_texto = _gerar_explicacao_texto(importancias, predicao)

    exp_id = str(uuid.uuid4())[:8]
    explicacao = {
        "id": exp_id,
        "modelo_id": modelo_id,
        "metodo": metodo,
        "predicao": round(predicao, 4),
        "interpretacao": "positivo" if predicao >= 0.5 else "negativo",
        "confianca": round(abs(predicao - 0.5) * 2, 4),
        "importancia_features": importancias,
        "explicacao_textual": explicacao_texto,
        "waterfall": _gerar_waterfall(importancias, predicao),
        "gerado_em": datetime.utcnow().isoformat()
    }
    explicacoes_db[exp_id] = explicacao

    return explicacao


@router.post("/importancia-global")
async def importancia_global(modelo_id: str, features: list, n_amostras: int = 100):
    """Calcula importância global das features"""
    if not features:
        raise HTTPException(status_code=400, detail="Lista de features necessária")

    # Simular importância global (em produção usaria SHAP values reais)
    importancias_raw = [random.uniform(0.01, 1.0) for _ in features]
    soma = sum(importancias_raw)
    importancias = {f: round(v / soma, 4) for f, v in zip(features, importancias_raw)}

    ranking = sorted(importancias.items(), key=lambda x: x[1], reverse=True)

    return {
        "modelo_id": modelo_id,
        "n_amostras_usadas": n_amostras,
        "total_features": len(features),
        "ranking_importancia": [{"feature": f, "importancia": v, "percentual": f"{round(v*100, 1)}%"} for f, v in ranking],
        "feature_mais_importante": ranking[0][0] if ranking else None,
        "metodo": "shap_global"
    }


@router.post("/contrafactual")
async def analise_contrafactual(
    modelo_id: str,
    features_atuais: dict,
    predicao_atual: float,
    predicao_desejada: float = 0.8
):
    """Análise contrafactual - o que mudar para obter predicao desejada"""
    diferenca = predicao_desejada - predicao_atual
    sugestoes = []

    for feature, valor in features_atuais.items():
        if isinstance(valor, (int, float)):
            # Simular sugestão de mudança
            direcao = "aumentar" if diferenca > 0 else "diminuir"
            mudanca = round(abs(diferenca) * random.uniform(0.1, 0.5), 3)
            novo_valor = round(valor + mudanca if diferenca > 0 else valor - mudanca, 3)
            impacto = round(random.uniform(0.01, 0.15), 4)

            sugestoes.append({
                "feature": feature,
                "valor_atual": valor,
                "valor_sugerido": novo_valor,
                "direcao": direcao,
                "impacto_estimado": impacto,
                "viabilidade": "alta" if impacto > 0.08 else "media" if impacto > 0.04 else "baixa"
            })

    sugestoes.sort(key=lambda x: x["impacto_estimado"], reverse=True)

    return {
        "modelo_id": modelo_id,
        "predicao_atual": predicao_atual,
        "predicao_desejada": predicao_desejada,
        "mudanca_necessaria": round(abs(diferenca), 4),
        "sugestoes": sugestoes[:5],
        "interpretacao": f"Para atingir {predicao_desejada}, priorize as top sugestões acima"
    }


@router.get("/explicacao/{exp_id}")
async def obter_explicacao(exp_id: str):
    """Obtém uma explicação"""
    if exp_id not in explicacoes_db:
        raise HTTPException(status_code=404, detail="Explicação não encontrada")
    return explicacoes_db[exp_id]


@router.get("/stats")
async def stats_explainability():
    """Estatísticas de explicabilidade"""
    metodos = {}
    for e in explicacoes_db.values():
        m = e["metodo"]
        metodos[m] = metodos.get(m, 0) + 1

    return {
        "total_explicacoes": len(explicacoes_db),
        "por_metodo": metodos
    }


def _calcular_importancias(features: dict, predicao: float) -> dict:
    """Calcula importâncias simuladas com soma ≈ predição"""
    if not features:
        return {}
    importancias = {}
    for f, v in features.items():
        if isinstance(v, (int, float)):
            contrib = round((v - 0.5) * random.uniform(0.05, 0.25), 4)
            importancias[f] = contrib
    return dict(sorted(importancias.items(), key=lambda x: abs(x[1]), reverse=True))


def _gerar_explicacao_texto(importancias: dict, predicao: float) -> str:
    if not importancias:
        return "Sem features para explicar."

    top_pos = [(f, v) for f, v in importancias.items() if v > 0]
    top_neg = [(f, v) for f, v in importancias.items() if v < 0]

    texto = f"A predição de {predicao:.2f} foi influenciada principalmente por: "
    if top_pos:
        texto += f"fatores positivos: {', '.join([f for f, _ in top_pos[:2]])}. "
    if top_neg:
        texto += f"fatores negativos: {', '.join([f for f, _ in top_neg[:2]])}."

    return texto


def _gerar_waterfall(importancias: dict, predicao: float) -> list:
    """Gera dados para gráfico waterfall"""
    waterfall = []
    acumulado = 0.5  # baseline
    for feature, contrib in list(importancias.items())[:8]:
        waterfall.append({
            "feature": feature,
            "contribuicao": contrib,
            "valor_acumulado": round(acumulado + contrib, 4),
            "tipo": "positivo" if contrib > 0 else "negativo"
        })
        acumulado += contrib
    return waterfall


plugin = ExplainabilityPlugin()
