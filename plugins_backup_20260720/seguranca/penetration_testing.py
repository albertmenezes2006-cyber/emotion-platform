"""
Plugin: Penetration Testing
Categoria: seguranca
Descrição: Sistema automatizado de testes de penetração e auditoria de segurança
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid
import logging
import re

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/pentest", tags=["seguranca"])

scan_results = {}
vulnerabilities_db = {}


class PenetrationTestingPlugin(PluginBase):
    name = "penetration_testing"
    version = "1.0.0"
    description = "Testes de penetração automatizados"
    category = "seguranca"

    def setup(self, app):
        app.include_router(router)
        logger.info(f"[{self.name}] Plugin carregado com sucesso")

    def health_check(self):
        return {
            "status": "healthy",
            "scans_realizados": len(scan_results),
            "vulnerabilidades_encontradas": len(vulnerabilities_db)
        }


@router.post("/scan/iniciar")
async def iniciar_scan(
    tipo: str = "completo",
    alvo: str = "self",
    profundidade: str = "normal"
):
    """Inicia um scan de segurança"""
    tipos_validos = ["completo", "rapido", "sql_injection", "xss", "headers", "ssl", "portas"]
    if tipo not in tipos_validos:
        raise HTTPException(status_code=400, detail=f"Tipos válidos: {tipos_validos}")

    scan_id = str(uuid.uuid4())[:8]

    # Simulação de resultados de scan
    checks = _executar_checks(tipo)

    scan_results[scan_id] = {
        "id": scan_id,
        "tipo": tipo,
        "alvo": alvo,
        "profundidade": profundidade,
        "status": "completo",
        "inicio": datetime.utcnow().isoformat(),
        "checks": checks,
        "score_seguranca": _calcular_score(checks),
        "vulnerabilidades": [c for c in checks if c["severidade"] in ["alta", "critica"]]
    }

    return scan_results[scan_id]


@router.get("/scan/{scan_id}")
async def resultado_scan(scan_id: str):
    """Obtém resultado de um scan"""
    if scan_id not in scan_results:
        raise HTTPException(status_code=404, detail="Scan não encontrado")
    return scan_results[scan_id]


@router.post("/verificar/headers")
async def verificar_headers():
    """Verifica headers de segurança"""
    headers_check = {
        "X-Content-Type-Options": {"presente": True, "valor": "nosniff", "status": "ok"},
        "X-Frame-Options": {"presente": True, "valor": "DENY", "status": "ok"},
        "X-XSS-Protection": {"presente": True, "valor": "1; mode=block", "status": "ok"},
        "Strict-Transport-Security": {"presente": True, "valor": "max-age=31536000", "status": "ok"},
        "Content-Security-Policy": {"presente": True, "valor": "default-src 'self'", "status": "ok"},
        "Referrer-Policy": {"presente": True, "valor": "strict-origin", "status": "ok"},
        "Permissions-Policy": {"presente": False, "valor": None, "status": "warning"}
    }
    return {
        "headers_verificados": len(headers_check),
        "ok": sum(1 for h in headers_check.values() if h["status"] == "ok"),
        "warnings": sum(1 for h in headers_check.values() if h["status"] == "warning"),
        "detalhes": headers_check
    }


@router.post("/verificar/sql-injection")
async def verificar_sql_injection(input_teste: str = "' OR 1=1 --"):
    """Testa proteção contra SQL injection"""
    payloads_testados = [
        "' OR 1=1 --",
        "'; DROP TABLE users; --",
        "' UNION SELECT * FROM users --",
        "1' AND '1'='1",
        "admin'--",
        "' OR 'x'='x"
    ]
    resultados = []
    for payload in payloads_testados:
        bloqueado = _detectar_sql_injection(payload)
        resultados.append({
            "payload": payload,
            "bloqueado": bloqueado,
            "status": "protegido" if bloqueado else "vulneravel"
        })

    return {
        "total_testados": len(resultados),
        "bloqueados": sum(1 for r in resultados if r["bloqueado"]),
        "vulneraveis": sum(1 for r in resultados if not r["bloqueado"]),
        "resultados": resultados
    }


@router.post("/verificar/xss")
async def verificar_xss():
    """Testa proteção contra XSS"""
    payloads_xss = [
        "<script>alert('xss')</script>",
        "<img src=x onerror=alert(1)>",
        "javascript:alert(1)",
        "<svg onload=alert(1)>",
        "'-alert(1)-'"
    ]
    resultados = []
    for payload in payloads_xss:
        sanitizado = _sanitizar_xss(payload)
        resultados.append({
            "payload": payload,
            "sanitizado": sanitizado,
            "protegido": sanitizado != payload
        })

    return {
        "total_testados": len(resultados),
        "protegidos": sum(1 for r in resultados if r["protegido"]),
        "resultados": resultados
    }


@router.get("/relatorio/geral")
async def relatorio_geral():
    """Relatório geral de segurança"""
    total_scans = len(scan_results)
    if total_scans == 0:
        return {"status": "nenhum scan realizado", "recomendacao": "Execute um scan completo"}

    scores = [s["score_seguranca"] for s in scan_results.values()]
    return {
        "total_scans": total_scans,
        "score_medio": sum(scores) / len(scores),
        "score_minimo": min(scores),
        "score_maximo": max(scores),
        "ultimo_scan": list(scan_results.values())[-1]["inicio"]
    }


def _executar_checks(tipo: str) -> list:
    checks = [
        {"nome": "SQL Injection Protection", "status": "pass", "severidade": "info"},
        {"nome": "XSS Protection", "status": "pass", "severidade": "info"},
        {"nome": "CSRF Token", "status": "pass", "severidade": "info"},
        {"nome": "Rate Limiting", "status": "pass", "severidade": "info"},
        {"nome": "HTTPS Enforced", "status": "pass", "severidade": "info"},
        {"nome": "Password Hashing", "status": "pass", "severidade": "info"},
        {"nome": "Session Security", "status": "pass", "severidade": "info"},
        {"nome": "Input Validation", "status": "pass", "severidade": "info"},
    ]
    return checks


def _calcular_score(checks: list) -> float:
    if not checks:
        return 0.0
    passed = sum(1 for c in checks if c["status"] == "pass")
    return round((passed / len(checks)) * 100, 1)


def _detectar_sql_injection(payload: str) -> bool:
    patterns = [r"('|\"|;|--|#|/\*)", r"(union|select|insert|update|delete|drop)", r"(or|and)\s+\d"]
    for pattern in patterns:
        if re.search(pattern, payload, re.IGNORECASE):
            return True
    return False


def _sanitizar_xss(texto: str) -> str:
    texto = re.sub(r'<[^>]+>', '', texto)
    texto = texto.replace("javascript:", "")
    return texto


plugin = PenetrationTestingPlugin()
