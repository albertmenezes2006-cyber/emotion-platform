"""
Plugin: Subscription Billing Avancado
Categoria: monetizacao
"""
VERSAO = "1.0"
NOME = "subscription_billing"
DESCRICAO = "Billing avancado — trials, upgrades, downgrades, pausas e cancelamentos"
CATEGORIA = "monetizacao"

from datetime import datetime, timedelta
from collections import defaultdict

_subscriptions = {}
_billing_events = defaultdict(list)
_dunning_status = {}

PLANOS = {
    "free":       {"preco": 0,     "ciclo": None,    "trial_dias": 0},
    "trial":      {"preco": 0,     "ciclo": "mensal","trial_dias": 7},
    "premium":    {"preco": 49.0,  "ciclo": "mensal","trial_dias": 0},
    "anual":      {"preco": 399.0, "ciclo": "anual", "trial_dias": 0},
    "enterprise": {"preco": 199.0, "ciclo": "mensal","trial_dias": 14},
}

def criar_subscription(usuario_id: int, plano: str, metodo_pagamento: str = "cartao") -> dict:
    import secrets
    sub_id = f"sub_{secrets.token_hex(8)}"
    plano_config = PLANOS.get(plano, PLANOS["free"])
    trial_dias = plano_config["trial_dias"]
    agora = datetime.now()
    _subscriptions[sub_id] = {
        "id": sub_id,
        "usuario_id": usuario_id,
        "plano": plano,
        "status": "trialing" if trial_dias > 0 else "active",
        "preco": plano_config["preco"],
        "ciclo": plano_config["ciclo"],
        "trial_fim": (agora + timedelta(days=trial_dias)).isoformat() if trial_dias > 0 else None,
        "proximo_faturamento": _calcular_proximo_faturamento(plano_config["ciclo"]),
        "metodo_pagamento": metodo_pagamento,
        "cancelamento_agendado": None,
        "pausado_ate": None,
        "criado_em": agora.isoformat(),
        "tentativas_cobranca": 0,
    }
    _registrar_evento(usuario_id, "subscription_created", {"plano": plano, "sub_id": sub_id})
    return _subscriptions[sub_id]

def _calcular_proximo_faturamento(ciclo: str) -> str:
    if not ciclo:
        return ""
    if ciclo == "mensal":
        return (datetime.now() + timedelta(days=30)).isoformat()
    return (datetime.now() + timedelta(days=365)).isoformat()

def upgrade_plano(sub_id: str, novo_plano: str) -> dict:
    if sub_id not in _subscriptions:
        return {"erro": "Subscription nao encontrada"}
    sub = _subscriptions[sub_id]
    plano_antigo = sub["plano"]
    sub["plano"] = novo_plano
    sub["preco"] = PLANOS.get(novo_plano, {}).get("preco", 0)
    sub["status"] = "active"
    sub["atualizado_em"] = datetime.now().isoformat()
    _registrar_evento(sub["usuario_id"], "plan_upgraded", {"de": plano_antigo, "para": novo_plano})
    return {"ok": True, "sub": sub}

def cancelar_subscription(sub_id: str, imediato: bool = False) -> dict:
    if sub_id not in _subscriptions:
        return {"erro": "Subscription nao encontrada"}
    sub = _subscriptions[sub_id]
    if imediato:
        sub["status"] = "canceled"
        sub["cancelado_em"] = datetime.now().isoformat()
    else:
        sub["cancelamento_agendado"] = sub["proximo_faturamento"]
        sub["status"] = "cancel_at_period_end"
    _registrar_evento(sub["usuario_id"], "subscription_canceled", {"imediato": imediato})
    return {"ok": True, "status": sub["status"]}

def pausar_subscription(sub_id: str, dias: int = 30) -> dict:
    if sub_id not in _subscriptions:
        return {"erro": "Subscription nao encontrada"}
    sub = _subscriptions[sub_id]
    sub["status"] = "paused"
    sub["pausado_ate"] = (datetime.now() + timedelta(days=dias)).isoformat()
    _registrar_evento(sub["usuario_id"], "subscription_paused", {"dias": dias})
    return {"ok": True, "pausado_ate": sub["pausado_ate"]}

def dunning_management(sub_id: str) -> dict:
    if sub_id not in _subscriptions:
        return {}
    sub = _subscriptions[sub_id]
    tentativas = sub.get("tentativas_cobranca", 0)
    sub["tentativas_cobranca"] = tentativas + 1
    if tentativas >= 3:
        sub["status"] = "past_due"
        return {"acao": "cancelar", "tentativas": tentativas}
    dias_retry = [3, 5, 7][min(tentativas, 2)]
    return {"acao": "retry", "dias_ate_retry": dias_retry, "tentativas": tentativas + 1}

def _registrar_evento(usuario_id: int, evento: str, dados: dict):
    _billing_events[usuario_id].append({"evento": evento, "dados": dados, "ts": datetime.now().isoformat()})

def calcular_mrr_detalhado() -> dict:
    subs_ativas = [s for s in _subscriptions.values() if s["status"] in ("active","trialing")]
    mrr_total = sum(s["preco"] for s in subs_ativas if s.get("ciclo") == "mensal")
    arr_total = sum(s["preco"]/12 for s in subs_ativas if s.get("ciclo") == "anual")
    mrr_por_plano = {}
    for s in subs_ativas:
        mrr_por_plano[s["plano"]] = mrr_por_plano.get(s["plano"], 0) + (s["preco"] if s.get("ciclo") == "mensal" else s["preco"]/12)
    return {
        "mrr": round(mrr_total + arr_total, 2),
        "arr": round((mrr_total + arr_total) * 12, 2),
        "por_plano": {k: round(v,2) for k, v in mrr_por_plano.items()},
        "total_subs_ativas": len(subs_ativas),
    }

def stats_billing() -> dict:
    return {
        "subscriptions_ativas": len([s for s in _subscriptions.values() if s["status"] == "active"]),
        "total_subscriptions": len(_subscriptions),
        "mrr": calcular_mrr_detalhado().get("mrr", 0),
        "planos_disponiveis": list(PLANOS.keys()),
        "plugin": "subscription_billing v1.0"
    }
