"""
Plugin: Compliance LGPD Completo
Categoria: seguranca
"""
VERSAO = "1.0"
NOME = "compliance_lgpd"
DESCRICAO = "LGPD compliance completo — consentimentos, direitos e DPO"
CATEGORIA = "seguranca"

import os
from datetime import datetime, timedelta
from collections import defaultdict

_consentimentos_lgpd = defaultdict(dict)
_solicitacoes_direitos = []
_registros_tratamento = []
_incidentes_seguranca = []
DPO_EMAIL = os.getenv("DPO_EMAIL", "dpo@emotionplatform.com.br")

BASES_LEGAIS = {
    "consentimento":         {"artigo": "Art. 7, I", "descricao": "Consentimento do titular"},
    "contrato":              {"artigo": "Art. 7, V", "descricao": "Execucao de contrato"},
    "obrigacao_legal":       {"artigo": "Art. 7, II", "descricao": "Cumprimento de obrigacao legal"},
    "interesse_legitimo":    {"artigo": "Art. 7, IX", "descricao": "Interesse legitimo do controlador"},
    "protecao_vida":         {"artigo": "Art. 7, VIII", "descricao": "Protecao da vida"},
}

DADOS_TRATADOS = {
    "nome":              {"sensivel": False, "finalidade": "Identificacao", "retencao_anos": 5, "base": "contrato"},
    "email":             {"sensivel": False, "finalidade": "Comunicacao", "retencao_anos": 5, "base": "contrato"},
    "analises_emocao":   {"sensivel": True,  "finalidade": "Servico principal", "retencao_anos": 2, "base": "consentimento"},
    "mensagens_sofia":   {"sensivel": True,  "finalidade": "Suporte psicologico", "retencao_anos": 1, "base": "consentimento"},
    "diarios":           {"sensivel": True,  "finalidade": "Registro pessoal", "retencao_anos": 2, "base": "consentimento"},
    "ip_acesso":         {"sensivel": False, "finalidade": "Seguranca", "retencao_anos": 1, "base": "interesse_legitimo"},
    "pagamentos":        {"sensivel": False, "finalidade": "Cobranca", "retencao_anos": 5, "base": "obrigacao_legal"},
}

def registrar_consentimento_lgpd(usuario_id: int, tipo_dado: str, aceito: bool, ip: str = "", versao: str = "2.0") -> dict:
    _consentimentos_lgpd[usuario_id][tipo_dado] = {
        "aceito": aceito,
        "data": datetime.now().isoformat(),
        "ip": ip[:20] if ip else "",
        "versao_politica": versao,
        "pode_revogar": True
    }
    return {"registrado": True, "tipo": tipo_dado, "aceito": aceito}

def verificar_consentimento(usuario_id: int, tipo_dado: str) -> bool:
    consent = _consentimentos_lgpd.get(usuario_id, {}).get(tipo_dado, {})
    return consent.get("aceito", False)

def revogar_consentimento(usuario_id: int, tipo_dado: str) -> dict:
    if usuario_id in _consentimentos_lgpd and tipo_dado in _consentimentos_lgpd[usuario_id]:
        _consentimentos_lgpd[usuario_id][tipo_dado]["aceito"] = False
        _consentimentos_lgpd[usuario_id][tipo_dado]["revogado_em"] = datetime.now().isoformat()
        return {"revogado": True, "tipo": tipo_dado}
    return {"erro": "Consentimento nao encontrado"}

def solicitar_direito(usuario_id: int, tipo_direito: str, detalhes: str = "") -> dict:
    import secrets
    protocolo = f"LGPD-{secrets.token_hex(4).upper()}"
    DIREITOS = {
        "acesso": "Art. 18, I — Acesso aos dados pessoais",
        "correcao": "Art. 18, III — Correcao de dados incompletos",
        "anonimizacao": "Art. 18, IV — Anonimizacao dos dados",
        "portabilidade": "Art. 18, V — Portabilidade dos dados",
        "exclusao": "Art. 18, VI — Exclusao dos dados",
        "revogacao": "Art. 18, IX — Revogacao do consentimento",
        "oposicao": "Art. 18, XI — Oposicao ao tratamento",
    }
    solicitacao = {
        "protocolo": protocolo,
        "usuario_id": usuario_id,
        "tipo_direito": tipo_direito,
        "descricao": DIREITOS.get(tipo_direito, "Direito nao mapeado"),
        "detalhes": detalhes[:500],
        "status": "recebida",
        "prazo_resposta": (datetime.now() + timedelta(days=15)).strftime("%d/%m/%Y"),
        "solicitado_em": datetime.now().isoformat(),
        "dpo_notificado": True
    }
    _solicitacoes_direitos.append(solicitacao)
    return solicitacao

def registrar_incidente_seguranca(descricao: str, dados_afetados: list, qtd_titulares: int) -> dict:
    import secrets
    incidente_id = f"INC-{secrets.token_hex(4).upper()}"
    prazo_anpd = datetime.now() + timedelta(hours=72)
    incidente = {
        "id": incidente_id,
        "descricao": descricao[:500],
        "dados_afetados": dados_afetados,
        "qtd_titulares_afetados": qtd_titulares,
        "detectado_em": datetime.now().isoformat(),
        "prazo_notificacao_anpd": prazo_anpd.isoformat(),
        "notificado_anpd": False,
        "medidas_tomadas": [],
        "severidade": "alta" if qtd_titulares > 100 else "media" if qtd_titulares > 10 else "baixa"
    }
    _incidentes_seguranca.append(incidente)
    return incidente

def gerar_relatorio_privacy() -> dict:
    return {
        "controlador": "Albert Menezes",
        "dpo": DPO_EMAIL,
        "bases_legais": BASES_LEGAIS,
        "dados_tratados": DADOS_TRATADOS,
        "direitos_titulares": ["acesso","correcao","anonimizacao","portabilidade","exclusao","revogacao","oposicao"],
        "solicitacoes_pendentes": len([s for s in _solicitacoes_direitos if s["status"] == "recebida"]),
        "incidentes": len(_incidentes_seguranca),
        "conformidade": "LGPD — Lei 13.709/2018",
        "ultima_atualizacao": datetime.now().strftime("%d/%m/%Y")
    }

def stats_lgpd() -> dict:
    return {
        "usuarios_com_consentimento": len(_consentimentos_lgpd),
        "solicitacoes_direitos": len(_solicitacoes_direitos),
        "incidentes_registrados": len(_incidentes_seguranca),
        "dados_mapeados": len(DADOS_TRATADOS),
        "plugin": "compliance_lgpd v1.0"
    }
