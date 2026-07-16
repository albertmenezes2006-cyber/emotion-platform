"""
Plugin: Relatorios Academicos e Citacoes
Categoria: pesquisa
"""
VERSAO = "1.0"
NOME = "relatorios_academicos"
DESCRICAO = "Geracao de relatorios academicos, citacoes APA e ABNT"
CATEGORIA = "pesquisa"

from datetime import datetime

def gerar_relatorio_caso(usuario_id_hash: str, dados_sessao: dict) -> dict:
    return {
        "tipo": "relatorio_caso_clinico",
        "participante": usuario_id_hash,
        "data_avaliacao": datetime.now().strftime("%d/%m/%Y"),
        "instrumento": "Emotion Intelligence Platform v21.0",
        "dados": {
            "emocao_predominante": dados_sessao.get("emocao", "neutro"),
            "score_ie": dados_sessao.get("score_ie", 0),
            "nivel_ie": dados_sessao.get("nivel_ie", "Iniciante"),
            "total_sessoes": dados_sessao.get("total_sessoes", 0),
            "periodo_avaliacao_dias": dados_sessao.get("periodo", 30),
        },
        "observacoes": "Dados coletados via plataforma digital com consentimento informado",
        "limitacoes": "Autoavaliacao digital. Requer validacao por profissional qualificado.",
        "recomendacoes": dados_sessao.get("recomendacoes", "Continuar acompanhamento")
    }

def citacao_apa(titulo: str = "Emotion Intelligence Platform", ano: int = None) -> str:
    ano = ano or datetime.now().year
    return (f"Menezes, A. ({ano}). {titulo} [Software]. "
            f"https://emotion-platform-albert.onrender.com")

def citacao_abnt(titulo: str = "Emotion Intelligence Platform", ano: int = None) -> str:
    ano = ano or datetime.now().year
    return (f"MENEZES, Albert. {titulo.upper()}. {ano}. "
            f"Disponivel em: https://emotion-platform-albert.onrender.com. "
            f"Acesso em: {datetime.now().strftime('%d %b. %Y')}.")

def citacao_vancouver(titulo: str = "Emotion Intelligence Platform", ano: int = None) -> str:
    ano = ano or datetime.now().year
    return (f"Menezes A. {titulo} [Internet]. {ano} [citado {datetime.now().strftime('%Y %b %d')}]. "
            f"Disponivel em: https://emotion-platform-albert.onrender.com")

def gerar_abstract_portugues(dados_estudo: dict) -> str:
    n = dados_estudo.get("n_participantes", 0)
    periodo = dados_estudo.get("periodo_dias", 30)
    emocao_principal = dados_estudo.get("emocao_predominante", "ansiedade")
    return (f"Objetivo: Investigar padroes emocionais em usuarios de plataforma digital de saude mental. "
            f"Metodo: Estudo transversal com {n} participantes ao longo de {periodo} dias, "
            f"utilizando a Emotion Intelligence Platform para coleta e analise de dados. "
            f"Resultados: A emocao predominante foi {emocao_principal}. "
            f"Conclusao: A plataforma digital demonstrou potencial como ferramenta de rastreamento emocional. "
            f"Descritores: Inteligencia emocional; Saude mental digital; Inteligencia artificial.")

def gerar_tabela_resultados(dados: list) -> str:
    if not dados:
        return "Tabela 1. Sem dados disponíveis."
    cabecalho = "Tabela 1. Distribuicao de emocoes por frequencia\n"
    cabecalho += "-" * 40 + "\n"
    cabecalho += f"{"Emocao":<20} {"Frequencia":>10} {"%":>8}\n"
    cabecalho += "-" * 40 + "
"
    total = sum(d.get("count", 0) for d in dados)
    linhas = []
    for d in dados[:10]:
        emocao = d.get("emocao", "")[:20]
        count = d.get("count", 0)
        pct = round(count/total*100, 1) if total > 0 else 0
        linhas.append(f"{emocao:<20} {count:>10} {pct:>7.1f}%")
    return cabecalho + "
".join(linhas) + "
" + "-"*40

def stats_relatorios() -> dict:
    return {"formatos_citacao": ["APA","ABNT","Vancouver","IEEE"], "plugin": "relatorios_academicos v1.0"}
