#!/usr/bin/env python3
"""Sofia IA - Modulo especializado v2.0
Blocos: 4, 5, 16, 17, 18, 19
"""

VERSAO = "2.0"
MODULO = "sofia"

# BLOCO 4 - Especialidades
ESPECIALIDADES = {
    "trauma": {
        "palavras": ["trauma", "abuso", "violencia", "agressao", "estupro", "assedio", "ptsd", "flashback", "pesadelo"],
        "resposta": "Percebo que voce esta tocando em algo muito delicado e doloroso. Voce e corajoso(a) por falar sobre isso. O trauma deixa marcas reais no cerebro e no corpo - nao e fraqueza, e uma resposta normal a situacoes anormais. Tecnica grounding 5-4-3-2-1: Nomeie 5 coisas que ve, 4 que toca, 3 que ouve, 2 que cheira, 1 que saboreia. Recomendo buscar um psicologo especializado em trauma (EMDR e TCC-T sao muito eficazes). Se estiver em perigo: ligue 190 (Policia) ou 180 (Central da Mulher)."
    },
    "luto": {
        "palavras": ["luto", "perda", "morreu", "faleceu", "morte", "perdi", "saudade", "falecimento"],
        "resposta": "Sinto muito pela sua perda. O luto nao tem prazo nem formula certa. O que voce sente e valido - tristeza, raiva, culpa, dormencia. Permita-se sentir. Nao ha forma errada de viver o luto. Estou aqui para ouvir. Quer me contar sobre essa pessoa especial?"
    },
    "lgbtqia": {
        "palavras": ["gay", "lesbica", "bissexual", "trans", "nao binario", "queer", "lgbtq", "homossexual", "armario", "identidade de genero"],
        "resposta": "Voce e valido(a) e merece amor e respeito exatamente como e. Sua identidade nao e uma doenca - OMS retirou homossexualidade da CID em 1990. Recursos de apoio: CVV 188 (24h, sigilo total), Grupo Gay da Bahia: ggb.org.br, ANTRA: antrabrasil.org. Como posso te ajudar hoje?"
    },
    "crise": {
        "palavras": ["suicidio", "me matar", "nao quero viver", "acabar com tudo", "me machucar", "autolesao", "sem saida", "desaparecer"],
        "resposta": "Estou aqui com voce agora. O que voce esta sentindo e real e eu me importo. Por favor, ligue agora para o CVV: 188 - gratuito, 24 horas, total sigilo. Se estiver em perigo imediato: SAMU 192 ou Pronto-Socorro. Enquanto isso, me conta: o que esta acontecendo com voce?"
    }
}

# BLOCO 5 - Plano terapeutico
PLANOS_TERAPEUTICOS = {
    "ansiedade": {
        "semana_1": ["Respiracao diafragmatica 2x ao dia", "Diario de ansiedade", "Caminhada 20min"],
        "semana_2": ["Tecnica 5-4-3-2-1 grounding", "Registro de pensamentos automaticos", "Reducao de cafeina"],
        "semana_3": ["Exposicao gradual a situacoes evitadas", "Meditacao mindfulness 10min", "Higiene do sono"],
        "semana_4": ["Revisao de progresso", "Tecnicas de resolucao de problemas", "Plano de manutencao"],
        "recursos": ["/respiracao", "/mindfulness", "/app/avaliacao"]
    },
    "depressao": {
        "semana_1": ["Ativacao comportamental - 1 atividade prazerosa/dia", "Registro de humor", "Rotina de sono"],
        "semana_2": ["Identificar pensamentos negativos automaticos", "Exercicio fisico leve", "Conexao social"],
        "semana_3": ["Reestruturacao cognitiva", "Projeto de vida pequeno", "Gratidao diaria"],
        "semana_4": ["Consolidacao de ganhos", "Prevencao de recaida", "Rede de apoio"],
        "recursos": ["/journaling", "/app/diario", "/app/avaliacao"]
    },
    "estresse": {
        "semana_1": ["Identificar fontes de estresse", "Tecnica Pomodoro", "Pausas ativas"],
        "semana_2": ["Gerenciamento de tempo", "Assertividade - aprender a dizer nao", "Relaxamento muscular"],
        "semana_3": ["Mindfulness no trabalho", "Limite entre trabalho e vida pessoal", "Hobbies"],
        "semana_4": ["Revisao de valores e prioridades", "Plano de autocuidado sustentavel"],
        "recursos": ["/pomodoro", "/mindfulness", "/respiracao"]
    }
}

def gerar_plano(condicao):
    plano = PLANOS_TERAPEUTICOS.get(condicao)
    if not plano:
        return ""
    texto = "Plano Terapeutico Personalizado - " + condicao.title() + "\n\n"
    for semana, atividades in plano.items():
        if semana.startswith("semana"):
            n = semana.split("_")[1]
            texto += "Semana " + n + ":\n"
            for a in atividades:
                texto += "- " + a + "\n"
            texto += "\n"
    texto += "Recursos recomendados: " + " | ".join(plano.get("recursos", []))
    return texto

# BLOCO 16 - Detecta evasao de temas
TEMAS_EVITADOS = {
    "familia": ["familia", "mae", "pai", "irmao", "parente"],
    "relacionamento": ["namorado", "namorada", "casamento", "divorcio", "separacao"],
    "trabalho": ["trabalho", "emprego", "chefe", "demitido", "demissao"],
    "financeiro": ["dinheiro", "divida", "financeiro", "falencia"],
    "saude": ["doenca", "diagnostico", "hospital", "medico"]
}

_historico_temas = {}

def detectar_evasao(session_id, mensagem):
    msg = mensagem.lower()
    temas_atuais = set()
    for tema, palavras in TEMAS_EVITADOS.items():
        if any(p in msg for p in palavras):
            temas_atuais.add(tema)
    if not temas_atuais:
        return None
    hist = _historico_temas.get(session_id, {})
    for tema in temas_atuais:
        hist[tema] = hist.get(tema, 0) + 1
    _historico_temas[session_id] = hist
    temas_frequentes = [t for t, c in hist.items() if c >= 3]
    if temas_frequentes:
        tema = temas_frequentes[0]
        return "Percebi que o tema " + tema + " aparece bastante nas nossas conversas. Gostaria de explorar isso com mais profundidade? Estou aqui para ouvir sem julgamento."
    return None

# BLOCO 17 - Personalidade adaptativa
PERFIS = {
    "analitico": {
        "palavras": ["por que", "como funciona", "evidencia", "estudo", "pesquisa", "dado"],
        "estilo": "formal_cientifico"
    },
    "emocional": {
        "palavras": ["sinto", "senti", "emocao", "coracao", "amor", "medo"],
        "estilo": "empatico_acolhedor"
    },
    "pratico": {
        "palavras": ["o que fazer", "como resolver", "solucao", "dica", "passo a passo"],
        "estilo": "direto_objetivo"
    },
    "espiritual": {
        "palavras": ["deus", "espirito", "fe", "oracao", "universo", "energia"],
        "estilo": "espiritualizado_respeitoso"
    }
}

_perfis_usuarios = {}

def detectar_perfil(session_id, mensagem):
    msg = mensagem.lower()
    perfil_atual = _perfis_usuarios.get(session_id, {})
    for perfil, dados in PERFIS.items():
        if any(p in msg for p in dados["palavras"]):
            perfil_atual[perfil] = perfil_atual.get(perfil, 0) + 1
    _perfis_usuarios[session_id] = perfil_atual
    if not perfil_atual:
        return "empatico_acolhedor"
    return PERFIS.get(max(perfil_atual, key=perfil_atual.get), {}).get("estilo", "empatico_acolhedor")

ESTILOS_RESPOSTA = {
    "formal_cientifico": "Responda de forma tecnicamente precisa, citando evidencias cientificas quando possivel.",
    "empatico_acolhedor": "Responda com muito acolhimento, empatia e carinho.",
    "direto_objetivo": "Seja direto e pratico. Use listas e passos claros. Sem rodeios.",
    "espiritualizado_respeitoso": "Respeite a espiritualidade do usuario. Integre aspectos espirituais com psicologia."
}

# BLOCO 18 - Mindfulness MBSR 8 semanas
MBSR_PROGRAMA = {
    1: {"titulo": "Piloto Automatico", "pratica": "Meditacao da uva passa - coma algo lentamente com atencao plena total", "duracao": "10 minutos", "reflexao": "Em que momentos voce age no piloto automatico?"},
    2: {"titulo": "Como Percebemos as Coisas", "pratica": "Body scan - varreda corporal deitado por 20 minutos", "duracao": "20 minutos", "reflexao": "Que sensacoes voce notou no corpo que nao percebia antes?"},
    3: {"titulo": "Mente em Casa no Corpo", "pratica": "Yoga mindful + meditacao sentado", "duracao": "20 minutos", "reflexao": "Como seu corpo reage ao estresse?"},
    4: {"titulo": "Estresse - Reagindo vs Respondendo", "pratica": "Meditacao dos 4 elementos", "duracao": "20 minutos", "reflexao": "Qual a diferenca entre reagir e responder?"},
    5: {"titulo": "Deixar Ser", "pratica": "Meditacao com dificuldades - sentar com o desconfortavel", "duracao": "25 minutos", "reflexao": "O que acontece quando voce para de lutar contra o que e dificil?"},
    6: {"titulo": "Comunicacao Atenta", "pratica": "Escuta mindful em conversas do dia a dia", "duracao": "Durante o dia", "reflexao": "Voce realmente ouve ou fica pensando na sua resposta?"},
    7: {"titulo": "Como Cuidar de Si Mesmo", "pratica": "Criar seu proprio plano de autocuidado mindful", "duracao": "Planejamento 30 min", "reflexao": "O que te nutre? O que te drena?"},
    8: {"titulo": "Usando o que Aprendeu", "pratica": "Revisao de todas as praticas. Escolher 2-3 para continuar", "duracao": "30 minutos", "reflexao": "O que mudou em voce ao longo dessas 8 semanas?"}
}

def get_sessao_mbsr(semana):
    if semana < 1 or semana > 8:
        return "Programa MBSR tem 8 semanas. Informe uma semana entre 1 e 8."
    s = MBSR_PROGRAMA[semana]
    return "MBSR - Semana " + str(semana) + ": " + s["titulo"] + "\nPratica: " + s["pratica"] + "\nDuracao: " + s["duracao"] + "\nReflexao: " + s["reflexao"]

# BLOCO 19 - Psicoeducacao automatica
PSICOEDUCACAO = {
    "ansiedade": "A ansiedade e uma resposta normal do cerebro ao perigo. O problema e quando ela dispara sem ameaca real. O que ajuda: Respiracao lenta (ativa o nervo vago), Exposicao gradual (destreina o medo), TCC (muda pensamentos catastroficos). A ansiedade nao e perigo real - e o alarme com defeito. Voce pode treinar seu cerebro a desligar esse alarme.",
    "depressao": "Depressao e uma doenca cerebral real - nao e fraqueza, preguica ou frescura. Envolve reducao de serotonina, dopamina e noradrenalina. O que ajuda: Ativacao comportamental, Exercicio fisico, Psicoterapia, Conexao social. Recuperacao e possivel - 80% melhora com tratamento adequado.",
    "tcc": "A TCC e a abordagem mais estudada da psicologia. O triangulo cognitivo: Pensamentos - Emocoes - Comportamentos. Distorcoes cognitivas comuns: Catastrofizacao, Leitura mental, Generalizacao, Rotulacao. Como aplicar: 1) Identifique o pensamento automatico 2) Questione as evidencias 3) Crie pensamento alternativo 4) Observe como sua emocao muda.",
    "mindfulness": "Mindfulness significa prestar atencao ao momento presente, intencionalmente e sem julgamento. Beneficios comprovados: Reduz cortisol em 30%, Melhora foco e memoria, Reduz ansiedade e depressao. Como comecar: Sente-se, feche os olhos, foque na respiracao, quando a mente vagar gentilmente volte. Sem julgamento - isso e normal!"
}

def get_psicoeducacao(tema):
    for chave, conteudo in PSICOEDUCACAO.items():
        if chave in tema.lower():
            return conteudo
    return ""

# FUNCAO PRINCIPAL
def processar_sofia(mensagem, session_id="anonimo"):
    msg = mensagem.lower()
    resultado = {
        "especialidade": None,
        "plano": None,
        "evasao": None,
        "perfil": detectar_perfil(session_id, mensagem),
        "mbsr": None,
        "psicoeducacao": None,
        "estilo_resposta": ""
    }
    for esp, dados in ESPECIALIDADES.items():
        if any(p in msg for p in dados["palavras"]):
            resultado["especialidade"] = {"tipo": esp, "resposta": dados["resposta"]}
            break
    for condicao in ["ansiedade", "depressao", "estresse"]:
        if condicao in msg:
            resultado["plano"] = gerar_plano(condicao)
            break
    resultado["evasao"] = detectar_evasao(session_id, mensagem)
    resultado["estilo_resposta"] = ESTILOS_RESPOSTA.get(resultado["perfil"], ESTILOS_RESPOSTA["empatico_acolhedor"])
    import re
    if "mbsr" in msg or ("mindfulness" in msg and "semana" in msg):
        nums = re.findall(r"\d+", mensagem)
        if nums:
            resultado["mbsr"] = get_sessao_mbsr(int(nums[0]))
    for tema in ["ansiedade", "depressao", "tcc", "mindfulness"]:
        if tema in msg:
            resultado["psicoeducacao"] = get_psicoeducacao(tema)
            break
    return resultado
