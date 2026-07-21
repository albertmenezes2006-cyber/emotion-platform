"""
Plugin: Revenue Analytics Avancado
Categoria: monetizacao
"""
VERSAO = "1.0"
NOME = "revenue_analytics"
DESCRICAO = "Analytics de receita — MRR, ARR, cohort, expansion, contraction"
CATEGORIA = "monetizacao"

from datetime import datetime, timedelta
from collections import defaultdict

_receita_mensal = defaultdict(float)
_novos_mrr = defaultdict(float)
_expansion_mrr = defaultdict(float)
_contraction_mrr = defaultdict(float)
_churned_mrr = defaultdict(float)
_cohorts = defaultdict(lambda: defaultdict(set))

def registrar_receita(usuario_id: int, valor: float, tipo: str = "novo", plano: str = "premium"):
    mes = datetime.now().strftime("%Y-%m")
    _receita_mensal[mes] = round(_receita_mensal[mes] + valor, 2)
    if tipo == "novo":
        _novos_mrr[mes] = round(_novos_mrr[mes] + valor, 2)
        _cohorts[mes]["usuarios"].add(usuario_id)
    elif tipo == "expansion":
        _expansion_mrr[mes] = round(_expansion_mrr[mes] + valor, 2)
    elif tipo == "contraction":
        _contraction_mrr[mes] = round(_contraction_mrr[mes] + valor, 2)
    elif tipo == "churn":
        _churned_mrr[mes] = round(_churned_mrr[mes] + valor, 2)

def calcular_net_mrr_movement(mes: str = None) -> dict:
    mes = mes or datetime.now().strftime("%Y-%m")
    novo = _novos_mrr.get(mes, 0)
    expansion = _expansion_mrr.get(mes, 0)
    contraction = _contraction_mrr.get(mes, 0)
    churned = _churned_mrr.get(mes, 0)
    net = round(novo + expansion - contraction - churned, 2)
    return {
        "mes": mes,
        "novo_mrr": novo,
        "expansion_mrr": expansion,
        "contraction_mrr": contraction,
        "churned_mrr": churned,
        "net_mrr": net,
        "crescimento": "positivo" if net > 0 else "negativo" if net < 0 else "estavel"
    }

def analisar_cohort(mes_cohort: str) -> dict:
    cohort = _cohorts.get(mes_cohort, {})
    usuarios_originais = len(cohort.get("usuarios", set()))
    if usuarios_originais == 0:
        return {"erro": "Cohort sem dados"}
    mes_atual = datetime.now().strftime("%Y-%m")
    usuarios_ativos = len(cohort.get("ativos_" + mes_atual, set()))
    retencao = round((usuarios_ativos / usuarios_originais) * 100, 1) if usuarios_originais > 0 else 0
    return {
        "cohort": mes_cohort,
        "usuarios_originais": usuarios_originais,
        "usuarios_ativos_hoje": usuarios_ativos,
        "retencao_pct": retencao,
        "churn_pct": round(100 - retencao, 1)
    }

def projetar_mrr(meses: int = 6) -> list:
    meses_historico = sorted(_receita_mensal.keys())[-3:]
    if len(meses_historico) < 2:
        return []
    valores = [_receita_mensal[m] for m in meses_historico]
    if len(valores) >= 2:
        crescimento_medio = (valores[-1] - valores[0]) / max(len(valores)-1, 1)
    else:
        crescimento_medio = 0
    projecoes = []
    ultimo_mrr = valores[-1] if valores else 0
    for i in range(1, meses+1):
        mes = (datetime.now() + timedelta(days=30*i)).strftime("%Y-%m")
        mrr_projetado = round(max(0, ultimo_mrr + crescimento_medio * i), 2)
        projecoes.append({"mes": mes, "mrr_projetado": mrr_projetado})
    return projecoes

def relatorio_revenue_completo() -> dict:
    mes_atual = datetime.now().strftime("%Y-%m")
    meses = sorted(_receita_mensal.keys())
    return {
        "mrr_atual": _receita_mensal.get(mes_atual, 0),
        "arr_projetado": round(_receita_mensal.get(mes_atual, 0) * 12, 2),
        "historico_6_meses": {m: _receita_mensal[m] for m in meses[-6:]},
        "net_mrr_movement": calcular_net_mrr_movement(),
        "projecao_6_meses": projetar_mrr(6),
        "total_receita_acumulada": round(sum(_receita_mensal.values()), 2),
    }

def stats_revenue_analytics() -> dict:
    return {
        "meses_com_dados": len(_receita_mensal),
        "receita_total": round(sum(_receita_mensal.values()), 2),
        "cohorts_analisados": len(_cohorts),
        "plugin": "revenue_analytics v1.0"
    }
