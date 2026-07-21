import shutil
from pathlib import Path

# Plugins para REMOVER
REMOVER = [
    # Muito nichados / não fazem sentido num SaaS geral
    "andropausa", "menopausa", "neonatal", "prematuridade", "perinatal",
    "gestacao", "pos_parto", "infertilidade", "prisional", "sem_teto",
    "refugiados", "bombeiros_policia", "militares", "rural", "desastres",
    "pandemia", "paliativo", "oncologia", "oncologia_psico", "psico_oncologia",
    "farmacia", "farmacologia_psiquiatrica_avancada", "psicofarmacologia",
    "psicofarmacologia_clinica", "neuropsicologia_forense", "juridico_avancado",
    "psicologia_juridica",

    # Muito teóricos / acadêmicos
    "epistemologia_psicologia", "fenomenologia_psicologica", "filosofia_psico",
    "neurobiologia_transtornos", "neurociencia_computacional",
    "neurogenomica_mental", "psicofisiologia_avancada", "psicopatologia_avancada",
    "farmacogenomica_mental", "imuno_psico", "endocrino_psico", "cardiologia_psico",
    "cardiologia", "economia_saude", "arquitetura_saude", "ecologia_saude",
    "paisagem_saude", "territorio_saude", "lugar_saude", "som_espaco",
    "luz_cor_saude", "sistemas_saude", "complexidade_saude", "sinergismo",
    "transdisciplinar", "interdisciplinar", "holismo", "integratividade",
    "complementaridade",

    # Terapias muito específicas / não digitais
    "ceramica_terapia", "costura_terapia", "jardim_terapia", "viagem_terapia",
    "culinaria_terapia", "escultura_terapia", "pedra_cristal_info",
    "cromoterapia2", "aromaterapia2", "aventura_terapia", "cerimonia_terapia",
    "contos_terapia", "fantasia_terapia", "historia_terapia", "humor_terapia",
    "legado_terapia", "metafora_terapia", "ritual_terapia", "silencio_terapia",
    "simbolo_terapia", "tradicao_terapia", "vocacao_terapia",
    "voluntariado_terapia", "comunidade_terapia", "cultura_terapia",
    "design_terapeutico", "espaco_terapeutico", "teatroterapia",
    "brinquedo_terapia", "danca_movimento", "dancaroterapia",
    "arte_terapia", "musica_terapia", "biblioterapia2",
    "cinematerapia", "jogo_terapia", "terapia_ambiental",
    "natureza_cura", "ambiente_cura", "planta_terapia",

    # Duplicados / redundantes
    "blockchain", "iot", "mlpipeline", "datascience", "devops",
    "epidemiologia", "neuroimagem_clinica", "neurobiologia_molecular",
    "ia2", "ia_avancada", "frontend2", "social2", "seguranca2",
    "musicoterapia2", "musicoterapia_avancada", "psicologia_positiva2",
    "psicologia_positiva_aplicada", "psicologia_positiva_avancada",
    "saude3", "integracao2", "relacionamentos2", "pesquisa2",
    "auditoria2", "automacao2", "backup2", "audio2", "relatorios2",
    "autoconhecimento2", "autoestima2", "identidade2",
    "inteligencia_emocional2", "personalidade2", "fotografia2",
    "telemedicina2", "psicologia_meia_idade2", "api2",

    # Muito específicos demais
    "saude_mental_esporte", "saude_mental_forense", "saude_mental_midia",
    "saude_mental_militar", "saude_mental_politicas_avancadas",
    "saude_mental_trabalho_tecnicas", "saude_mental_juridico_avancado",
    "saude_mental_internacional", "saude_mental_diversidade_avancada",
    "saude_mental_infancia_avancada", "saude_mental_adolescencia_avancada",
    "saude_mental_idoso_avancado", "saude_mental_grupos_especificos",
    "saude_mental_emergencia", "saude_mental_digital_avancado",
    "neurociencia_clinica", "neuropsicologia", "neuroeducacao",
    "neurociencias", "neurologica", "neurociencia",
    "psicologia_ambiental_avancada", "psicologia_clinica_avancada",
    "psicologia_organizacional_avancada", "psicologia_saude_avancada",
    "psicologia_social_avancada", "psicologia_contemporanea",
    "psicoterapia_grupo_avancada", "psicoterapia_adolescentes_tecnicas",
    "psicoterapia_criancas_tecnicas", "psicoterapia_idosos_tecnicas",
    "intervencao_crise_avancada", "intervencoes_digitais_especificas",
    "intervencoes_especificas", "avaliacao_neuropsicologica",
    "avaliacao_avancada", "avaliacao_psicologica",
    "instrumentos_avaliacao_br", "tecnicas_avaliacao",
    "pesquisa_qualitativa_avancada", "pesquisa_cientifica",
    "pesquisa_clinica", "pesquisa_saude_mental",
    "farmacologia_psiquiatrica_avancada", "psiquiatria_infantojuvenil",
    "gerontopsiquiatria", "gerontologia",
    "terapia_trauma_avancada", "terapias_corporais", "terapias_corpo_mente",
    "medicina_alternativa", "medicina_sono",
    "estados_expandidos", "transcendencia", "inteligencia_espiritual",
    "espiritualidade", "cerimonia_terapia", "ancestralidade",
    "identidade_cultural", "cross_cultural", "cultura",
    "i18n", "bienestar", "bioetica", "bioética",
    "compliance2", "etica_clinica", "etica",
    "epidemiologia", "politicas_publicas", "saude_publica",
    "saude_coletiva_mental", "saude_coletiva",
    "multiprofissional", "equipe_saude", "interconsulta_clinica",
    "consultoria_clinica", "mentoria_clinica", "supervisao_pares",
    "segunda_opiniao", "interdisciplinar", "multiprofissional",
    "wearables", "tecnologias_emergentes_saude", "tecnologia_saude",
    "diagnostico_digital", "diagnostico_diferencial",
    "machine_learning", "nlp",
    "psicologia_adulto", "meia_idade", "crise_meia_idade",
    "ciclos_vida", "marcos_vida", "transicao_vida",
    "desenvolvimento_adulto", "jovem_adulto", "terceira_idade",
    "idoso_avancado", "pediatria", "crianca_avancado",
    "adolescente", "adocao",
    "imigrantes", "minorias", "diversidade", "genero",
    "lgbtqia_plus", "populacoes", "grupos_especificos",
    "contextos", "saude_mental_contextos",
    "urbano", "ambiente", "natureza",
    "clima_mental", "ecologia_saude",
]

plugins_dir = Path("plugins")
removidos = 0
nao_encontrados = 0

for nome in REMOVER:
    caminho = plugins_dir / nome
    if caminho.exists():
        shutil.rmtree(caminho)
        print(f"✅ Removido: {nome}")
        removidos += 1
    else:
        nao_encontrados += 1

print(f"\n{'='*40}")
print(f"Removidos:      {removidos}")
print(f"Não existiam:   {nao_encontrados}")
print(f"Restantes:      {len(list(plugins_dir.iterdir()))}")
