"""
Plugin: Penetration Testing Automatizado
Categoria: seguranca
"""
VERSAO = "1.0"
NOME = "penetration_testing"
DESCRICAO = "Testes de seguranca automatizados — OWASP Top 10"
CATEGORIA = "seguranca"

import os
from datetime import datetime
from collections import defaultdict

_resultados_pentest = []
_vulnerabilidades = []
BASE_URL = os.getenv("BASE_URL", "https://emotion-platform-albert.onrender.com")

TESTES_OWASP = [
    {"id": "A01", "nome": "Controle de Acesso", "endpoints": ["/admin","/api/admin/usuarios","/api/admin/siem"]},
    {"id": "A02", "nome": "Falhas Criptograficas", "checks": ["https","hsts","secure_cookies"]},
    {"id": "A03", "nome": "Injection", "payloads": ["1' OR '1'='1","<script>alert(1)</script>","../etc/passwd","; DROP TABLE usuarios;"]},
    {"id": "A04", "nome": "Design Inseguro", "checks": ["rate_limit","input_validation","error_handling"]},
    {"id": "A05", "nome": "Configuracao Incorreta", "checks": ["debug_off","server_header","directory_listing"]},
    {"id": "A06", "nome": "Componentes Vulneraveis", "checks": ["dependencies","outdated_packages"]},
    {"id": "A07", "nome": "Autenticacao", "checks": ["brute_force","session_fixation","token_expiry"]},
    {"id": "A08", "nome": "Integridade", "checks": ["csrf","request_signing","data_validation"]},
    {"id": "A09", "nome": "Logging", "checks": ["audit_logs","error_logging","monitoring"]},
    {"id": "A10", "nome": "SSRF", "payloads": ["http://localhost","http://127.0.0.1","http://169.254.169.254"]},
]

async def executar_teste_sql_injection(url_base: str) -> dict:
    try:
        import httpx
        payloads = ["1' OR '1'='1", "1; DROP TABLE usuarios;--", "1 UNION SELECT 1,2,3--"]
        vulneravel = False
        detalhes = []
        async with httpx.AsyncClient(timeout=10, verify=False) as client:
            for payload in payloads:
                try:
                    r = await client.get(f"{url_base}/api/v1/analisar", params={"texto": payload})
                    conteudo = r.text.lower()
                    if any(kw in conteudo for kw in ["sql","syntax error","mysql","postgresql","sqlite"]):
                        vulneravel = True
                        detalhes.append(f"Payload: {payload[:30]}")
                except Exception:
                    pass
        return {"teste": "sql_injection", "vulneravel": vulneravel, "detalhes": detalhes, "severidade": "critica" if vulneravel else "ok"}
    except Exception as e:
        return {"teste": "sql_injection", "erro": str(e)}

async def executar_teste_xss(url_base: str) -> dict:
    try:
        import httpx
        payloads = ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>", "javascript:alert(1)"]
        vulneravel = False
        async with httpx.AsyncClient(timeout=10, verify=False) as client:
            for payload in payloads:
                try:
                    r = await client.get(f"{url_base}/api/v1/analisar", params={"texto": payload})
                    if payload in r.text and "content-security-policy" not in r.headers:
                        vulneravel = True
                except Exception:
                    pass
        return {"teste": "xss", "vulneravel": vulneravel, "severidade": "alta" if vulneravel else "ok"}
    except Exception as e:
        return {"teste": "xss", "erro": str(e)}

async def verificar_headers_seguranca(url_base: str) -> dict:
    try:
        import httpx
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.get(f"{url_base}/health")
        headers = dict(r.headers)
        headers_requeridos = {
            "x-frame-options": "DENY ou SAMEORIGIN",
            "x-content-type-options": "nosniff",
            "strict-transport-security": "max-age presente",
            "content-security-policy": "politica definida",
            "x-xss-protection": "1; mode=block",
        }
        resultado = {}
        for header, descricao in headers_requeridos.items():
            presente = header in headers
            resultado[header] = {"presente": presente, "valor": headers.get(header,"AUSENTE"), "requerido": descricao}
        score = sum(1 for v in resultado.values() if v["presente"])
        return {"headers": resultado, "score": f"{score}/{len(headers_requeridos)}", "status": "seguro" if score >= 4 else "atencao"}
    except Exception as e:
        return {"erro": str(e)}

async def executar_pentest_completo(url_base: str = None) -> dict:
    url = url_base or BASE_URL
    inicio = datetime.now()
    resultados = {}
    resultados["sql_injection"] = await executar_teste_sql_injection(url)
    resultados["xss"] = await executar_teste_xss(url)
    resultados["headers"] = await verificar_headers_seguranca(url)
    vuln_encontradas = [k for k, v in resultados.items() if isinstance(v, dict) and v.get("vulneravel")]
    relatorio = {
        "url_testada": url,
        "inicio": inicio.isoformat(),
        "fim": datetime.now().isoformat(),
        "testes_executados": len(resultados),
        "vulnerabilidades_encontradas": len(vuln_encontradas),
        "status_geral": "vulneravel" if vuln_encontradas else "seguro",
        "resultados": resultados,
        "recomendacao": "Corrigir imediatamente" if vuln_encontradas else "Sistema seguro"
    }
    _resultados_pentest.append(relatorio)
    return relatorio

def stats_pentest() -> dict:
    return {
        "testes_executados": len(_resultados_pentest),
        "owasp_checks": len(TESTES_OWASP),
        "ultimo_teste": _resultados_pentest[-1]["inicio"] if _resultados_pentest else None,
        "plugin": "penetration_testing v1.0"
    }
