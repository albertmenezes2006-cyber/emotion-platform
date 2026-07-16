"""
Plugin: Crypto Pagamentos — Web3
Categoria: monetizacao
"""
VERSAO = "1.0"
NOME = "crypto_pagamentos"
DESCRICAO = "Pagamentos em criptomoedas — Bitcoin, Ethereum e stablecoins"
CATEGORIA = "monetizacao"

import os
import hashlib
from datetime import datetime, timedelta
from collections import defaultdict

COINBASE_COMMERCE_KEY = os.getenv("COINBASE_COMMERCE_KEY", "")
INFURA_PROJECT_ID = os.getenv("INFURA_PROJECT_ID", "")
WALLET_ETH = os.getenv("WALLET_ETH", "")
WALLET_BTC = os.getenv("WALLET_BTC", "")

_pagamentos_crypto = {}
_transacoes_pendentes = defaultdict(list)

CRIPTOS_ACEITAS = {
    "BTC":  {"nome": "Bitcoin",  "rede": "mainnet", "decimais": 8},
    "ETH":  {"nome": "Ethereum", "rede": "mainnet", "decimais": 18},
    "USDT": {"nome": "Tether",   "rede": "ERC-20",  "decimais": 6},
    "USDC": {"nome": "USD Coin", "rede": "ERC-20",  "decimais": 6},
    "PIX":  {"nome": "PIX (BRL)","rede": "brasil",  "decimais": 2},
}

TAXAS_CONVERSAO_BRL = {
    "BTC": 350000.0,
    "ETH": 18000.0,
    "USDT": 5.0,
    "USDC": 5.0,
}

async def criar_cobranca_coinbase(valor_brl: float, plano: str, usuario_id: int) -> dict:
    if not COINBASE_COMMERCE_KEY:
        return _criar_cobranca_simulada(valor_brl, plano, usuario_id)
    try:
        import httpx
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.post(
                "https://api.commerce.coinbase.com/charges",
                headers={"X-CC-Api-Key": COINBASE_COMMERCE_KEY, "X-CC-Version": "2018-03-22", "Content-Type": "application/json"},
                json={
                    "name": f"Emotion Intelligence — {plano}",
                    "description": f"Plano {plano} — Emotion Intelligence Platform",
                    "pricing_type": "fixed_price",
                    "local_price": {"amount": str(valor_brl), "currency": "BRL"},
                    "metadata": {"usuario_id": str(usuario_id), "plano": plano}
                }
            )
            return r.json().get("data", {})
    except Exception as e:
        return _criar_cobranca_simulada(valor_brl, plano, usuario_id)

def _criar_cobranca_simulada(valor_brl: float, plano: str, usuario_id: int) -> dict:
    import secrets
    charge_id = secrets.token_hex(16)
    enderecos = {}
    if WALLET_ETH:
        enderecos["ETH"] = WALLET_ETH
        enderecos["USDT"] = WALLET_ETH
        enderecos["USDC"] = WALLET_ETH
    if WALLET_BTC:
        enderecos["BTC"] = WALLET_BTC
    valores_crypto = {cripto: round(valor_brl / taxa, 8) for cripto, taxa in TAXAS_CONVERSAO_BRL.items()}
    cobranca = {
        "id": charge_id,
        "usuario_id": usuario_id,
        "plano": plano,
        "valor_brl": valor_brl,
        "valores_crypto": valores_crypto,
        "enderecos": enderecos,
        "status": "pendente",
        "expira_em": (datetime.now() + timedelta(hours=1)).isoformat(),
        "criado_em": datetime.now().isoformat()
    }
    _pagamentos_crypto[charge_id] = cobranca
    return cobranca

def verificar_status_pagamento_crypto(charge_id: str) -> dict:
    if charge_id in _pagamentos_crypto:
        return _pagamentos_crypto[charge_id]
    return {"erro": "Cobranca nao encontrada"}

def calcular_valor_crypto(valor_brl: float, cripto: str) -> dict:
    taxa = TAXAS_CONVERSAO_BRL.get(cripto, 5.0)
    valor_cripto = round(valor_brl / taxa, 8)
    return {
        "valor_brl": valor_brl,
        "cripto": cripto,
        "valor_cripto": valor_cripto,
        "taxa_usada": taxa,
        "nota": "Taxa aproximada. Valor final baseado na cotacao no momento do pagamento."
    }

def gerar_endereco_pagamento(cripto: str) -> str:
    if cripto in ("ETH","USDT","USDC"):
        return WALLET_ETH or "Configure WALLET_ETH no Render"
    if cripto == "BTC":
        return WALLET_BTC or "Configure WALLET_BTC no Render"
    return ""

def stats_crypto() -> dict:
    return {
        "coinbase_commerce": bool(COINBASE_COMMERCE_KEY),
        "criptos_aceitas": list(CRIPTOS_ACEITAS.keys()),
        "pagamentos_registrados": len(_pagamentos_crypto),
        "wallets_configuradas": sum([bool(WALLET_ETH), bool(WALLET_BTC)]),
        "plugin": "crypto_pagamentos v1.0"
    }
