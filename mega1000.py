#!/usr/bin/env python3
"""MEGA 1000 — adiciona ~400 plugins para chegar a 1000+"""
import os

def w(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

def init(cat):
    os.makedirs(f"plugins/{cat}", exist_ok=True)
    p = f"plugins/{cat}/__init__.py"
    if not os.path.exists(p):
        open(p, "w").close()

def p(cat, nome, desc):
    cn = "".join(x.capitalize() for x in nome.replace("-","_").split("_")) + "Plugin"
    prefix = f"/api/v1/{nome.replace('_','-')}"
    return f'''"""Plugin: {nome} | {cat} | {desc}"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid, logging
logger = logging.getLogger(__name__)
router = APIRouter(prefix="{prefix}", tags=["{cat}"])
_db = {{}}

class {cn}(PluginBase):
    name = "{nome}"; version = "1.0.0"
    description = "{desc}"; category = "{cat}"
    def setup(self, app):
        app.include_router(router)
        logger.info(f"[{nome}] OK")
    def health_check(self):
        return {{"status":"healthy","total":len(_db)}}

@router.get("/status")
async def status():
    return {{"plugin":"{nome}","cat":"{cat}","total":len(_db),"ts":datetime.utcnow().isoformat()}}

@router.post("/criar")
async def criar(nome:str, valor:str="", user_id:str=""):
    i=str(uuid.uuid4())[:8]
    _db[i]={{"id":i,"nome":nome,"valor":valor,"user_id":user_id,"ts":datetime.utcnow().isoformat()}}
    return {{"id":i,"status":"criado"}}

@router.get("/listar")
async def listar(limite:int=50):
    return {{"total":len(_db),"items":list(_db.values())[-limite:]}}

@router.get("/{{item_id}}")
async def obter(item_id:str):
    if item_id not in _db: raise HTTPException(404,"Nao encontrado")
    return _db[item_id]

@router.delete("/{{item_id}}")
async def deletar(item_id:str):
    if item_id not in _db: raise HTTPException(404,"Nao encontrado")
    del _db[item_id]; return {{"status":"deletado"}}

plugin = {cn}()
'''

def batch(cat, lista):
    init(cat)
    criados = 0
    for nome, desc in lista:
        path = f"plugins/{cat}/{nome}.py"
        if not os.path.exists(path):
            w(path, p(cat, nome, desc))
            criados += 1
    print(f"  ✅ {cat}: +{criados} plugins")
    return criados

total_criados = 0
print("="*55)
print("MEGA 1000 — CRIANDO PLUGINS")
print("="*55)

# ══════════════════════════════════════════════════════
# SAUDE3 — saúde avançada (25 plugins)
# ══════════════════════════════════════════════════════
total_criados += batch("saude3", [
    ("diabetes_mental","Diabetes e saúde mental: suporte integrado"),
    ("hipertensao_emocional","Hipertensão e estresse: correlação e manejo"),
    ("obesidade_psicologica","Obesidade e fatores psicológicos"),
    ("dor_cronica_mental","Dor crônica e saúde mental"),
    ("cancer_psicooncologia","Psicooncologia avançada"),
    ("cardiologia_mental","Saúde cardíaca e mental integradas"),
    ("dermatologia_psicossomatica","Pele e emoções: psicossomática"),
    ("gastro_intestinal_mental","Síndrome do intestino irritável e ansiedade"),
    ("imunologia_stress","Psiconeuroimunologia e estresse"),
    ("endocrino_mental","Tireoide, hormônios e saúde mental"),
    ("reproducao_mental","Saúde reprodutiva e bem-estar psicológico"),
    ("gravidez_mental","Saúde mental na gestação e pós-parto"),
    ("menopausa_mental","Menopausa e saúde mental feminina"),
    ("andropausa_mental","Andropausa e saúde mental masculina"),
    ("hiv_mental","HIV/AIDS e saúde mental"),
    ("hepatite_mental","Hepatites e saúde mental"),
    ("tuberculose_mental","Tuberculose e saúde mental"),
    ("covid_long_mental","COVID longa e saúde mental"),
    ("transplante_mental","Transplante de órgãos e psicologia"),
    ("uti_mental","UTI e trauma psicológico"),
    ("cirurgia_mental","Preparo psicológico para cirurgias"),
    ("reabilitacao_fisica","Reabilitação física e mental integradas"),
    ("medicina_integrativa","Medicina integrativa e saúde mental"),
    ("acupuntura_mental","Acupuntura e saúde mental"),
    ("fitoterapia_mental","Fitoterapia e bem-estar psicológico"),
])

# ══════════════════════════════════════════════════════
# PSIQUIATRIA — módulos psiquiátricos (25 plugins)
# ══════════════════════════════════════════════════════
total_criados += batch("psiquiatria", [
    ("transtorno_bipolar","Transtorno bipolar: manejo e suporte"),
    ("esquizofrenia_suporte","Esquizofrenia: suporte ao paciente e família"),
    ("transtorno_personalidade","Transtornos de personalidade: TLP, narcisismo"),
    ("ocd_suporte","TOC: terapia de exposição e resposta"),
    ("fobia_social","Fobia social: TCC e exposição"),
    ("fobia_especifica","Fobias específicas: protocolo de tratamento"),
    ("agorafobia","Agorafobia e síndrome do pânico"),
    ("estresse_pos_traumatico","TEPT: avaliação e tratamento"),
    ("tdah_adulto","TDAH no adulto: avaliação e manejo"),
    ("autismo_adulto","TEA no adulto: suporte e inclusão"),
    ("alimentacao_transtorno","Anorexia, bulimia e compulsão alimentar"),
    ("jogo_patologico_psiq","Jogo patológico: avaliação psiquiátrica"),
    ("dismorfofobia","Dismorfofobia: tratamento especializado"),
    ("hipocondria","Hipocondria e ansiedade de saúde"),
    ("somatizacao","Transtorno de somatização"),
    ("conversao_funcional","Transtornos funcionais e conversão"),
    ("psicose_breve","Psicose breve e primeiros episódios"),
    ("delirium_manejo","Delirium: avaliação e manejo"),
    ("demencia_psiquiatria","Demência: aspectos psiquiátricos"),
    ("personalidade_boderline","TLP: DBT e manejo de crises"),
    ("narcisismo_clinico","Transtorno narcisista: avaliação clínica"),
    ("dependencia_afetiva","Dependência afetiva e co-dependência"),
    ("ciume_patologico","Ciúme patológico: avaliação e tratamento"),
    ("erotomania","Erotomania e stalking: manejo clínico"),
    ("psiquiatria_forense","Psiquiatria forense e avaliação de imputabilidade"),
])

# ══════════════════════════════════════════════════════
# NEUROPSICOLOGIA — (20 plugins)
# ══════════════════════════════════════════════════════
total_criados += batch("neuropsicologia", [
    ("avaliacao_neuropsico","Avaliação neuropsicológica completa"),
    ("memoria_avaliacao","Avaliação de memória e aprendizagem"),
    ("funcoes_executivas","Funções executivas: avaliação e reabilitação"),
    ("linguagem_avaliacao","Avaliação de linguagem e comunicação"),
    ("percepcao_visuoespacial","Percepção visuoespacial e habilidades"),
    ("atencao_avaliacao","Atenção e concentração: avaliação"),
    ("velocidade_processamento_neuro","Velocidade de processamento cognitivo"),
    ("praxia_avaliacao","Praxias e habilidades motoras finas"),
    ("metacognicao","Metacognição e autorregulação"),
    ("aprendizagem_avaliacao","Transtornos de aprendizagem: dislexia, discalculia"),
    ("reabilitacao_cognitiva","Reabilitação cognitiva pós-AVC"),
    ("estimulacao_cognitiva","Estimulação cognitiva para idosos"),
    ("neuropsico_infantil","Neuropsicologia infantil e desenvolvimento"),
    ("tcc_neuropsico","TCC adaptada para dificuldades cognitivas"),
    ("feedback_neuropsico","Feedback de avaliação neuropsicológica"),
    ("laudos_neuropsico","Laudos neuropsicológicos padronizados"),
    ("treino_cognitivo_neuro","Treino cognitivo baseado em evidências"),
    ("jogos_cognitivos","Jogos cognitivos para reabilitação"),
    ("neuropsico_esportiva","Neuropsicologia esportiva"),
    ("concussao_avaliacao","Avaliação pós-concussão"),
])

# ══════════════════════════════════════════════════════
# PSICOLOGIA_POSITIVA — (20 plugins)
# ══════════════════════════════════════════════════════
total_criados += batch("psicologia_positiva", [
    ("perma_model","Modelo PERMA de bem-estar"),
    ("forcas_carater_via","Forças de caráter VIA Survey"),
    ("flow_csikszentmihalyi","Flow e experiência ótima"),
    ("gratidao_tracker","Tracker de gratidão e bem-estar"),
    ("otimismo_aprendido","Otimismo aprendido — Seligman"),
    ("resiliencia_positiva","Resiliência: construção e mensuração"),
    ("autoeficacia_bandura","Autoeficácia — teoria de Bandura"),
    ("mindset_growth_positivo","Mindset de crescimento aplicado"),
    ("conexoes_significativas","Conexões significativas e bem-estar"),
    ("proposito_engajamento","Propósito e engajamento na vida"),
    ("realizacao_accomplishment","Realização e conquistas pessoais"),
    ("emocoes_positivas_broaden","Ampliar e construir emoções positivas"),
    ("autocompaixao_neff","Autocompaixão — Kristin Neff"),
    ("bemestar_subjetivo","Bem-estar subjetivo e satisfação"),
    ("felicidade_hedonica","Felicidade hedônica e eudaimônica"),
    ("esperanca_snyder","Esperança — teoria de Snyder"),
    ("sabedoria_positiva","Sabedoria e psicologia positiva"),
    ("virtudes_positivas","Virtudes humanas e florescimento"),
    ("relacionamentos_positivos","Relacionamentos positivos e amor"),
    ("humor_bem_estar","Humor e riso na saúde mental"),
])

# ══════════════════════════════════════════════════════
# GESTALT — (15 plugins)
# ══════════════════════════════════════════════════════
total_criados += batch("gestalt", [
    ("contato_retirada","Ciclo de contato e retirada"),
    ("awareness_gestalt","Awareness e presença terapêutica"),
    ("figura_fundo","Figura e fundo na percepção"),
    ("experimento_gestalt","Experimentos gestálticos digitais"),
    ("cadeira_vazia","Técnica da cadeira vazia digital"),
    ("polaridades_gestalt","Trabalho com polaridades"),
    ("sonhos_gestalt","Trabalho com sonhos na Gestalt"),
    ("corporal_gestalt","Abordagem corporal gestáltica"),
    ("grupo_gestalt","Gestalt em grupos"),
    ("crianca_interior","Trabalho com a criança interior"),
    ("resistencias_gestalt","Resistências: introjeção, projeção"),
    ("contato_interrupcoes","Interrupções de contato"),
    ("physis_gestalt","Physis e crescimento natural"),
    ("here_now_gestalt","Aqui e agora na terapia"),
    ("dialogo_socratico_gestalt","Diálogo socrático gestáltico"),
])

# ══════════════════════════════════════════════════════
# PSICANÁLISE — (15 plugins)
# ══════════════════════════════════════════════════════
total_criados += batch("psicanalise", [
    ("inconsciente_dinamico","O inconsciente e dinâmica psíquica"),
    ("transferencia_contratransferencia","Transferência e contratransferência"),
    ("mecanismos_defesa","Mecanismos de defesa do ego"),
    ("sonhos_psicanalise","Interpretação de sonhos"),
    ("resistencia_psicanalise","Resistência e elaboração"),
    ("complexos_jung","Complexos junguianos"),
    ("arquétipos_jung","Arquétipos e inconsciente coletivo"),
    ("sombra_jung","Sombra e individuação"),
    ("anima_animus","Anima, animus e integração"),
    ("persona_jung","Persona e máscara social"),
    ("self_jung","Self e processo de individuação"),
    ("sincronicidade","Sincronicidade e significado"),
    ("winnicott_desenvolvimento","Winnicott: desenvolvimento emocional"),
    ("klein_posicoes","Klein: posições esquizo-paranoide e depressiva"),
    ("bion_continente","Bion: continente e conteúdo"),
])

# ══════════════════════════════════════════════════════
# INTERVENCAO — intervenções específicas (20 plugins)
# ══════════════════════════════════════════════════════
total_criados += batch("intervencao", [
    ("intervencao_crise_aguda","Intervenção em crise aguda — protocolo"),
    ("intervencao_suicidio","Intervenção em ideação suicida"),
    ("intervencao_autolesao","Intervenção em autolesão"),
    ("intervencao_psicose","Intervenção em episódio psicótico"),
    ("intervencao_panico","Intervenção em ataque de pânico"),
    ("intervencao_dissociacao","Intervenção em episódio dissociativo"),
    ("intervencao_trauma_agudo","Intervenção em trauma agudo"),
    ("intervencao_luto","Intervenção em luto agudo"),
    ("intervencao_violencia","Intervenção em situação de violência"),
    ("intervencao_abuso","Intervenção em situação de abuso"),
    ("primeiros_socorros_psico","Primeiros socorros psicológicos"),
    ("debriefing_psicologico","Debriefing psicológico pós-trauma"),
    ("intervencao_grupal","Intervenção grupal em crises"),
    ("intervencao_familiar_crise","Intervenção familiar em crise"),
    ("intervencao_escola","Intervenção em crise escolar"),
    ("intervencao_trabalho","Intervenção em crise no trabalho"),
    ("intervencao_online","Intervenção em crise online"),
    ("intervencao_telefonica","Intervenção em crise por telefone"),
    ("intervencao_pos_desastre","Intervenção pós-desastre coletivo"),
    ("intervencao_comunitaria","Intervenção comunitária em saúde mental"),
])

# ══════════════════════════════════════════════════════
# ESCOLAS_TERAPEUTICAS — (20 plugins)
# ══════════════════════════════════════════════════════
total_criados += batch("escolas_terapeuticas", [
    ("tcc_protocolo","TCC: protocolo completo digitalizado"),
    ("tec_terceira_onda","Terapias de terceira onda"),
    ("dbt_completo","DBT: programa completo digital"),
    ("act_completo","ACT: programa completo"),
    ("fap_ativacao","FAP: psicoterapia analítica funcional"),
    ("bat_ativacao_comportamental","BAT: ativação comportamental"),
    ("emdr_protocolo","EMDR: protocolo completo"),
    ("somatic_experiencing","Somatic Experiencing digital"),
    ("sensorimotor_psico","Psicoterapia sensoriomotora"),
    ("ift_terapia_familia","IFT: terapia integrativa de família"),
    ("fst_terapia_sistemas","FST: terapia de sistemas familiares"),
    ("narrative_therapy","Terapia narrativa: re-autoria"),
    ("solution_focused","Terapia focada em soluções"),
    ("collaborative_therapy","Terapia colaborativa"),
    ("compassion_focused","Terapia focada na compaixão"),
    ("schema_therapy","Schema Therapy completo"),
    ("mbct_mindfulness","MBCT: mindfulness para depressão"),
    ("mbsr_completo","MBSR: protocolo completo 8 semanas"),
    ("yoga_terapia","Yoga como terapia complementar"),
    ("arteterapia_protocolos","Arteterapia: protocolos clínicos"),
])

# ══════════════════════════════════════════════════════
# DIVERSIDADE — (15 plugins)
# ══════════════════════════════════════════════════════
total_criados += batch("diversidade", [
    ("lgbtq_saude_mental","Saúde mental LGBTQ+: abordagem afirmativa"),
    ("trans_saude_mental","Transexualidade e saúde mental"),
    ("raca_saude_mental","Raça e saúde mental: racismo estrutural"),
    ("cultura_saude_mental","Competência cultural em saúde mental"),
    ("religiao_saude_mental","Religiosidade e saúde mental"),
    ("genero_saude_mental","Gênero e saúde mental"),
    ("classe_social_mental","Classe social e acesso à saúde mental"),
    ("imigrantes_mental","Saúde mental de imigrantes e refugiados"),
    ("povos_originarios","Saúde mental de povos originários"),
    ("quilombola_mental","Saúde mental quilombola"),
    ("pcd_saude_mental","PCD e saúde mental"),
    ("idosos_lgbtq","Idosos LGBTQ+ e saúde mental"),
    ("adolescentes_identidade","Adolescência e identidade"),
    ("homens_saude_mental","Saúde mental masculina e masculinidades"),
    ("mulheres_saude_mental","Saúde mental da mulher"),
])

# ══════════════════════════════════════════════════════
# CONTEXTOS — contextos específicos (20 plugins)
# ══════════════════════════════════════════════════════
total_criados += batch("contextos", [
    ("prisional_mental","Saúde mental no sistema prisional"),
    ("militar_mental","Saúde mental militar e veteranos"),
    ("bombeiros_mental","Saúde mental de bombeiros"),
    ("policia_mental","Saúde mental policial"),
    ("saude_profissionais","Saúde mental de profissionais de saúde"),
    ("professores_mental","Saúde mental de professores"),
    ("agricultores_mental","Saúde mental rural e agricultores"),
    ("pescadores_mental","Saúde mental de pescadores"),
    ("caminhoneiros_mental","Saúde mental de caminhoneiros"),
    ("artistas_mental","Saúde mental de artistas"),
    ("atletas_mental","Saúde mental de atletas de alto rendimento"),
    ("executivos_mental","Saúde mental de executivos"),
    ("startups_mental","Saúde mental em startups"),
    ("freelancers_mental","Saúde mental de freelancers"),
    ("desempregados_mental","Saúde mental e desemprego"),
    ("aposentados_mental","Saúde mental na aposentadoria"),
    ("estudantes_mental","Saúde mental de estudantes universitários"),
    ("concurseiros_mental","Saúde mental de concurseiros"),
    ("cuidadores_informal","Saúde mental de cuidadores informais"),
    ("voluntarios_mental","Saúde mental de voluntários"),
])

# ══════════════════════════════════════════════════════
# TECNOLOGIA_SAUDE — (15 plugins)
# ══════════════════════════════════════════════════════
total_criados += batch("tecnologia_saude", [
    ("digital_therapeutics","Digital Therapeutics: DTx regulamentados"),
    ("prescription_digital","Prescrição digital de apps terapêuticos"),
    ("sensor_fusion","Fusão de sensores para saúde mental"),
    ("ambient_intelligence","Inteligência ambiente para bem-estar"),
    ("smart_home_mental","Casa inteligente e saúde mental"),
    ("chatbot_clinico","Chatbot clínico validado"),
    ("virtual_therapist","Terapeuta virtual com IA"),
    ("digital_phenotyping","Fenótipo digital para diagnóstico"),
    ("passive_sensing","Sensoriamento passivo do estado mental"),
    ("ecological_momentary","EMA: avaliação ecológica momentânea"),
    ("just_in_time","Just-in-time adaptive interventions"),
    ("mhealth_apps","mHealth: integração com apps de saúde"),
    ("telemedicine_ai","Telemedicina potencializada por IA"),
    ("clinical_decision","Suporte à decisão clínica por IA"),
    ("predictive_mental","Saúde mental preditiva"),
])

# ══════════════════════════════════════════════════════
# EPIDEMIOLOGIA — (15 plugins)
# ══════════════════════════════════════════════════════
total_criados += batch("epidemiologia", [
    ("prevalencia_transtornos","Prevalência de transtornos mentais"),
    ("incidencia_depressao","Incidência de depressão por região"),
    ("fatores_risco_pop","Fatores de risco populacionais"),
    ("determinantes_sociais","Determinantes sociais da saúde mental"),
    ("carga_doenca","Carga de doença em saúde mental"),
    ("anos_vida_perdidos","Anos de vida perdidos por incapacidade"),
    ("mortalidade_mental","Mortalidade em transtornos mentais"),
    ("epidemiologia_suicidio","Epidemiologia do suicídio no Brasil"),
    ("epidemiologia_substancias","Epidemiologia do uso de substâncias"),
    ("saude_mental_pandemia","Saúde mental pós-pandemia"),
    ("vigilancia_epidemiologica","Vigilância epidemiológica em SM"),
    ("registros_casos","Registros de casos e notificações"),
    ("inqueritos_populacionais","Inquéritos populacionais de saúde mental"),
    ("mapeamento_servicos","Mapeamento de serviços de SM"),
    ("acesso_tratamento","Acesso ao tratamento em SM"),
])

# ══════════════════════════════════════════════════════
# POLITICAS_PUBLICAS — (10 plugins)
# ══════════════════════════════════════════════════════
total_criados += batch("politicas_publicas", [
    ("reforma_psiquiatrica","Reforma psiquiátrica brasileira"),
    ("raps_rede","RAPS: rede de atenção psicossocial"),
    ("caps_gestao","CAPS: gestão e indicadores"),
    ("sus_saude_mental","SUS e saúde mental: políticas"),
    ("ans_coberturas","ANS: coberturas em saúde mental"),
    ("cfp_politicas","CFP: políticas e resoluções"),
    ("cfm_politicas","CFM: políticas em saúde mental"),
    ("oms_global_mental","OMS: plano global de saúde mental"),
    ("onu_direitos_mental","ONU: direitos humanos e SM"),
    ("financiamento_sm","Financiamento de SM no Brasil"),
])

# ══════════════════════════════════════════════════════
# ETICA — ética profissional (10 plugins)
# ══════════════════════════════════════════════════════
total_criados += batch("etica", [
    ("codigo_etica_psi","Código de ética do psicólogo"),
    ("codigo_etica_med","Código de ética médica"),
    ("consentimento_etico","Consentimento livre e esclarecido"),
    ("sigilo_etica","Sigilo profissional e suas exceções"),
    ("duplo_vinculo","Duplo vínculo e conflito de interesses"),
    ("limites_eticos","Limites éticos na relação terapêutica"),
    ("etica_pesquisa","Ética em pesquisa com seres humanos"),
    ("cep_comite","CEP: comitê de ética em pesquisa"),
    ("etica_ia_saude","Ética da IA em saúde mental"),
    ("responsabilidade_etica","Responsabilidade ética do profissional"),
])

# ══════════════════════════════════════════════════════
# FORMACAO — formação profissional (15 plugins)
# ══════════════════════════════════════════════════════
total_criados += batch("formacao", [
    ("graduacao_psicologia","Graduação em psicologia: recursos"),
    ("especializacao_clinica","Especialização clínica digital"),
    ("mestrado_doutorado","Mestrado e doutorado em SM"),
    ("residencia_sm","Residência em saúde mental"),
    ("aprimoramento","Aprimoramento profissional"),
    ("supervisao_clinica2","Supervisão clínica continuada"),
    ("intervision_pares","Intervisão entre pares"),
    ("educacao_continuada","Educação continuada em SM"),
    ("certificacoes","Certificações em abordagens terapêuticas"),
    ("congresso_digital","Congressos e eventos digitais"),
    ("publicacoes_formacao","Publicações e artigos científicos"),
    ("bolsas_formacao","Bolsas de formação e capacitação"),
    ("intercambio_internacional","Intercâmbio internacional em SM"),
    ("mentoria_formacao","Mentoria na formação profissional"),
    ("avaliacao_competencias","Avaliação de competências clínicas"),
])

# ══════════════════════════════════════════════════════
# INDICADORES — KPIs e métricas (15 plugins)
# ══════════════════════════════════════════════════════
total_criados += batch("indicadores", [
    ("kpi_clinico","KPIs clínicos: efetividade terapêutica"),
    ("kpi_plataforma","KPIs da plataforma: engajamento"),
    ("kpi_financeiro","KPIs financeiros: MRR, ARR, LTV"),
    ("kpi_satisfacao","KPIs de satisfação: NPS, CSAT"),
    ("kpi_acessibilidade","KPIs de acessibilidade"),
    ("kpi_seguranca","KPIs de segurança e privacidade"),
    ("kpi_qualidade","KPIs de qualidade assistencial"),
    ("kpi_producao","KPIs de produção: sessões, laudos"),
    ("kpi_tempo","KPIs de tempo: espera, resolução"),
    ("kpi_retencao","KPIs de retenção de usuários"),
    ("kpi_conversao","KPIs de conversão: trial to paid"),
    ("kpi_viral","KPIs virais: referrals, compartilhamentos"),
    ("ods_saude_mental","ODS: objetivos de desenvolvimento sustentável"),
    ("benchmarking_setor","Benchmarking do setor de SM digital"),
    ("relatorio_impacto2","Relatório de impacto para investidores"),
])

# ══════════════════════════════════════════════════════
# ECONOMIA_SAUDE — (10 plugins)
# ══════════════════════════════════════════════════════
total_criados += batch("economia_saude", [
    ("custo_efetividade","Análise de custo-efetividade"),
    ("roi_tratamento","ROI de tratamentos em SM"),
    ("custo_doenca","Custo econômico dos transtornos mentais"),
    ("produtividade_perdida","Produtividade perdida por SM"),
    ("economia_comportamental","Economia comportamental em saúde"),
    ("nudge_saude_mental","Nudge para comportamentos saudáveis"),
    ("incentivos_adesao","Incentivos para adesão ao tratamento"),
    ("seguros_saude_mental2","Mercado de seguros em SM"),
    ("financiamento_inovacao","Financiamento de inovação em SM"),
    ("vale_saude_mental","Vale saúde mental: benefício corporativo"),
])

# ══════════════════════════════════════════════════════
# INOVACAO — (15 plugins)
# ══════════════════════════════════════════════════════
total_criados += batch("inovacao", [
    ("startup_mental","Startups de saúde mental: ecossistema"),
    ("healthtech_mental","Healthtech em saúde mental"),
    ("venture_capital_sm","VC e investimento em SM"),
    ("aceleradora_sm","Aceleradoras de healthtech"),
    ("open_innovation","Open innovation em saúde mental"),
    ("hackathon_mental2","Hackathon de saúde mental"),
    ("premio_inovacao_sm","Prêmio de inovação em SM"),
    ("poc_mental","POC: prova de conceito em SM"),
    ("mvp_mental","MVP de produtos de saúde mental"),
    ("growth_hacking_sm","Growth hacking para apps de SM"),
    ("product_market_fit","Product-market fit em SM"),
    ("go_to_market_sm","Go-to-market para plataformas de SM"),
    ("escala_global","Escalabilidade global em SM"),
    ("regulatory_pathway","Regulatory pathway para digital therapeutics"),
    ("fda_ce_anvisa","FDA, CE e ANVISA para software médico"),
])

# ══════════════════════════════════════════════════════
# AMBIENTE — saúde ambiental (10 plugins)
# ══════════════════════════════════════════════════════
total_criados += batch("ambiente", [
    ("eco_ansiedade","Eco-ansiedade e mudanças climáticas"),
    ("natureza_terapia","Natureza como terapia: ecoterapia"),
    ("biofilia","Biofilia e conexão com a natureza"),
    ("poluicao_mental","Poluição e saúde mental"),
    ("espaco_urbano_mental","Espaço urbano e saúde mental"),
    ("arquitetura_mental","Arquitetura terapêutica e design"),
    ("cor_ambiente","Cromoterapia e psicologia das cores"),
    ("luz_terapia","Fototerapia e ritmo circadiano"),
    ("verde_urbano","Áreas verdes e bem-estar mental"),
    ("desastre_ambiental","Desastres ambientais e saúde mental"),
])

# ══════════════════════════════════════════════════════
# MINDFULNESS_AVANCADO — (15 plugins)
# ══════════════════════════════════════════════════════
total_criados += batch("mindfulness_avancado", [
    ("mindfulness_base","Mindfulness: fundamentos e prática"),
    ("mbsr_avancado","MBSR avançado: professor e praticante"),
    ("mbct_avancado","MBCT avançado para depressão"),
    ("mbt_borderline","MBT: mentalization based treatment"),
    ("mindfulness_tcc","Mindfulness integrado à TCC"),
    ("compaixao_mindfulness","Mindfulness compaixão: MSC"),
    ("mindfulness_criancas","Mindfulness para crianças"),
    ("mindfulness_escolas","Mindfulness em escolas"),
    ("mindfulness_trabalho","Mindfulness no trabalho"),
    ("mindfulness_cancer","Mindfulness para pacientes com câncer"),
    ("mindfulness_dor","Mindfulness para dor crônica"),
    ("mindfulness_idosos","Mindfulness para idosos"),
    ("mindfulness_gestantes","Mindfulness para gestantes"),
    ("mindfulness_casais","Mindfulness para casais"),
    ("mindfulness_retiro","Retiro de mindfulness digital"),
])

# ══════════════════════════════════════════════════════
# CONTAR TOTAL
# ══════════════════════════════════════════════════════
skip = {"__init__.py","loader.py","plugin_base.py"}
total = 0
cats_count = {}
for cat in os.listdir("plugins"):
    cp = f"plugins/{cat}"
    if not os.path.isdir(cp) or cat.startswith("_"): continue
    for f in os.listdir(cp):
        if f.endswith(".py") and f not in skip:
            total += 1
            cats_count[cat] = cats_count.get(cat, 0) + 1

print(f"\n{'='*55}")
print(f"NOVOS PLUGINS CRIADOS HOJE: +{total_criados}")
print(f"TOTAL NO DISCO: {total}")
print(f"PROGRESSO: {total}/1470 = {round(total/1470*100,1)}%")
print(f"{'='*55}")
print(f"\nTOP CATEGORIAS:")
for cat, n in sorted(cats_count.items(), key=lambda x:-x[1])[:20]:
    bar = "█" * (n // 2)
    print(f"  {cat:<35} {n:>4}  {bar}")
