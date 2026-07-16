"""
Plugin: Threat Intelligence — Inteligencia de Ameacas
Categoria: seguranca
"""
VERSAO = "1.0"
NOME = "threat_intelligence"
DESCRICAO = "IOCs, feeds de ameacas e correlacao de eventos de seguranca"
CATEGORIA = "seguranca"

import os
import hashlib
from datetime import datetime, timedelta
from collections import defaultdict

_iocs_database = {"ips": set(), "dominios": set(), "hashes": set(), "urls": set()}
_threat_feeds = []
_eventos_correlacionados = defaultdict(list)
_alertas_ti = []

FEEDS_PUBLICOS = [
    {"nome": "AbuseIPDB", "url": "https://api.abuseipdb.com/api/v2/blacklist", "tipo": "ip"},
    {"nome": "URLhaus", "url": "https://urlhaus-api.abuse.ch/v1/urls/recent/", "tipo": "url"},
    {"nome": "Feodo Tracker", "url": "https://feodotracker.abuse.ch/downloads/ipblocklist.txt", "tipo": "ip"},
]

ABUSEIPDB_KEY = os.getenv("ABUSEIPDB_API_KEY", "")

async def verificar_ip_abuseipdb(ip: str) -> dict:
    if not ABUSEIPDB_KEY:
        return {"ip": ip, "disponivel": False}
    try:
        import httpx
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.get(
                "https://api.abuseipdb.com/api/v2/check",
                headers={"Key": ABUSEIPDB_KEY, "Accept": "application/json"},
                params={"ipAddress": ip, "maxAgeInDays": 90}
            )
            data = r.json().get("data", {})
            return {
                "ip": ip,
                "abusivo": data.get("abuseConfidenceScore", 0) > 50,
                "score": data.get("abuseConfidenceScore", 0),
                "pais": data.get("countryCode", ""),
                "total_reports": data.get("totalReports", 0),
                "fonte": "AbuseIPDB"
            }
    except Exception as e:
        return {"ip": ip, "erro": str(e)}

def adicionar_ioc(tipo: str, valor: str, fonte: str = "manual", severidade: str = "media"):
    if tipo in _iocs_database:
        _iocs_database[tipo].add(valor)
    _threat_feeds.append({
        "tipo": tipo,
        "valor": valor,
        "fonte": fonte,
        "severidade": severidade,
        "adicionado_em": datetime.now().isoformat()
    })

def verificar_ioc(tipo: str, valor: str) -> dict:
    if tipo not in _iocs_database:
        return {"encontrado": False, "erro": "Tipo invalido"}
    encontrado = valor in _iocs_database[tipo]
    if not encontrado and tipo == "ip":
        partes_valor = valor.split(".")[:2]
        for ioc in _iocs_database["ips"]:
            if ioc.startswith(".".join(partes_valor)):
                encontrado = True
                break
    return {
        "encontrado": encontrado,
        "tipo": tipo,
        "valor": valor,
        "risco": "alto" if encontrado else "baixo",
        "acao_recomendada": "Bloquear acesso" if encontrado else "Permitir"
    }

def correlacionar_eventos_seguranca(ip: str, eventos: list) -> dict:
    _eventos_correlacionados[ip].extend(eventos)
    todos_eventos = _eventos_correlacionados[ip]
    tipos_ameaca = [e.get("tipo","") for e in todos_eventos[-20:]]
    from collections import Counter
    contagem = Counter(tipos_ameaca)
    score_risco = 0
    if contagem.get("sql_injection", 0) > 0:
        score_risco += 40
    if contagem.get("xss", 0) > 0:
        score_risco += 30
    if contagem.get("brute_force", 0) > 3:
        score_risco += 50
    if contagem.get("honeypot", 0) > 0:
        score_risco += 60
    nivel = "critico" if score_risco >= 80 else "alto" if score_risco >= 50 else "medio" if score_risco >= 20 else "baixo"
    if nivel in ("critico", "alto"):
        _alertas_ti.append({"ip": ip, "nivel": nivel, "score": score_risco, "ts": datetime.now().isoformat()})
    return {
        "ip": ip,
        "score_risco": score_risco,
        "nivel": nivel,
        "eventos_analisados": len(todos_eventos),
        "tipos_detectados": dict(contagem),
        "acao": "Bloquear" if nivel in ("critico","alto") else "Monitorar"
    }

def gerar_relatorio_ti() -> dict:
    return {
        "iocs_total": {k: len(v) for k, v in _iocs_database.items()},
        "feeds_carregados": len(_threat_feeds),
        "alertas_ativos": len(_alertas_ti),
        "ips_monitorados": len(_eventos_correlacionados),
        "ultimo_alerta": _alertas_ti[-1] if _alertas_ti else None,
        "gerado_em": datetime.now().isoformat()
    }

def stats_threat_intelligence() -> dict:
    return {
        "iocs_database": {k: len(v) for k, v in _iocs_database.items()},
        "feeds_publicos": len(FEEDS_PUBLICOS),
        "abuseipdb": bool(ABUSEIPDB_KEY),
        "alertas": len(_alertas_ti),
        "plugin": "threat_intelligence v1.0"
    }
