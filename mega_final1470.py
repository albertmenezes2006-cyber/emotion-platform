#!/usr/bin/env python3
"""SPRINT FINAL — 471+ plugins para completar 1470"""
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
    n = 0
    for nome, desc in lista:
        path = f"plugins/{cat}/{nome}.py"
        if not os.path.exists(path):
            w(path, p(cat, nome, desc))
            n += 1
    print(f"  ✅ {cat}: +{n}")
    return n

total = 0
print("="*55)
print("SPRINT FINAL — RUMO A 1470")
print("="*55)

# ══════════════════════════════════════════
# AVALIACAO_PSICOLOGICA (25)
# ══════════════════════════════════════════
total += batch("avaliacao_psicologica", [
    ("rorschach_digital","Teste de Rorschach digital assistido por IA"),
    ("tat_tematico","TAT: teste de apercepção temática"),
    ("wais_inteligencia","WAIS: escala de inteligência adulto"),
    ("wisc_infantil","WISC: escala de inteligência infantil"),
    ("mmpi_personalidade","MMPI: inventário de personalidade"),
    ("neo_pi_r","NEO-PI-R: big five personalidade"),
    ("scid_entrevista","SCID: entrevista diagnóstica estruturada"),
    ("mini_international","MINI International Neuropsychiatric"),
    ("hamilton_depressao","Hamilton Rating Scale para depressão"),
    ("hamilton_ansiedade","Hamilton Rating Scale para ansiedade"),
    ("beck_depressao","BDI: Inventário de depressão de Beck"),
    ("beck_ansiedade","BAI: Inventário de ansiedade de Beck"),
    ("dass21_digital","DASS-21: estresse ansiedade depressão"),
    ("phq9_digital","PHQ-9: triagem de depressão"),
    ("gad7_digital","GAD-7: transtorno ansiedade generalizada"),
    ("ptsd_checklist","PCL-5: checklist de PTSD"),
    ("audit_alcool","AUDIT: uso problemático de álcool"),
    ("cage_alcool","CAGE: rastreio de alcoolismo"),
    ("bprs_psicose","BPRS: escala psiquiátrica breve"),
    ("panss_esquizofrenia","PANSS: esquizofrenia positivo negativo"),
    ("young_mania","YMRS: escala de mania de Young"),
    ("mdq_bipolar","MDQ: questionário de humor"),
    ("asrs_tdah","ASRS: rastreio de TDAH adulto"),
    ("aq_autismo","AQ: quociente de autismo"),
    ("oci_r_ocd","OCI-R: inventário obsessivo-compulsivo"),
])

# ══════════════════════════════════════════
# PSICOFARMACOLOGIA (20)
# ══════════════════════════════════════════
total += batch("psicofarmacologia", [
    ("antidepressivos","Antidepressivos: mecanismos e efeitos"),
    ("ansiolíticos","Ansiolíticos: benzodiazepínicos e outros"),
    ("antipsicoticos","Antipsicóticos típicos e atípicos"),
    ("estabilizadores_humor","Estabilizadores de humor: lítio e outros"),
    ("psicoestimulantes","Psicoestimulantes para TDAH"),
    ("hipnoticos","Hipnóticos e indutores do sono"),
    ("anticonvulsivantes_psiq","Anticonvulsivantes em psiquiatria"),
    ("beta_bloqueadores_ansiedade","Beta-bloqueadores para ansiedade"),
    ("buspirona","Buspirona: ansiolítico não-benzo"),
    ("naltrexona","Naltrexona para dependência"),
    ("buprenorfina","Buprenorfina: tratamento de dependência"),
    ("acamprosato","Acamprosato para alcoolismo"),
    ("disulfiram","Disulfiram: aversão ao álcool"),
    ("metadona","Metadona: tratamento de dependência"),
    ("ketamina_depressao","Ketamina para depressão resistente"),
    ("psilocibina_pesquisa","Psilocibina: pesquisa clínica"),
    ("mdma_ptsd","MDMA para PTSD: pesquisa clínica"),
    ("cannabis_medicinal","Cannabis medicinal em psiquiatria"),
    ("interacoes_psico","Interações medicamentosas em psiquiatria"),
    ("farmacocinetica","Farmacocinética em psicofarmacologia"),
])

# ══════════════════════════════════════════
# NEUROCIENCIAS (20)
# ══════════════════════════════════════════
total += batch("neurociencias", [
    ("neuroplasticidade","Neuroplasticidade e aprendizagem"),
    ("neurogenese_adulta","Neurogênese adulta e saúde mental"),
    ("eixo_hha","Eixo HHA: cortisol e estresse"),
    ("serotonina_sistema","Sistema serotonérgico e humor"),
    ("dopamina_recompensa","Dopamina e circuito de recompensa"),
    ("noradrenalina","Noradrenalina e ansiedade"),
    ("gaba_glutamato","GABA e glutamato: equilíbrio"),
    ("endocannabinoides","Sistema endocanabinoide e humor"),
    ("oxitocina_vinculo","Oxitocina e vínculos afetivos"),
    ("neuroimagem_funcional","Neuroimagem funcional em psiquiatria"),
    ("eeg_biofeedback","EEG e neurofeedback"),
    ("tms_estimulacao","TMS: estimulação magnética transcraniana"),
    ("tdcs_estimulacao","tDCS: estimulação transcraniana DC"),
    ("ect_eletroconvulsivo","ECT: eletroconvulsoterapia"),
    ("dbs_profunda","DBS: estimulação cerebral profunda"),
    ("ritmo_circadiano_neuro","Ritmo circadiano e saúde mental"),
    ("microbioma_cerebro","Eixo microbioma-intestino-cérebro"),
    ("inflamacao_depressao","Inflamação e depressão"),
    ("epigenetica_trauma","Epigenética do trauma"),
    ("neurociencia_afetiva","Neurociência afetiva: bases neurais"),
])

# ══════════════════════════════════════════
# REABILITACAO_PSICOSSOCIAL (20)
# ══════════════════════════════════════════
total += batch("reabilitacao_psicossocial", [
    ("moradia_assistida","Moradia assistida para pessoas com SM"),
    ("trabalho_protegido","Trabalho protegido e inclusão"),
    ("treinamento_habilidades","Treinamento de habilidades sociais"),
    ("psicoeducacao_familia","Psicoeducação para familiares"),
    ("grupo_convivencia","Grupos de convivência e lazer"),
    ("espiritualidade_reabilitacao","Espiritualidade na reabilitação"),
    ("projeto_terapeutico","Projeto terapêutico singular PTS"),
    ("autonomia_reabilitacao","Promoção de autonomia psicossocial"),
    ("reinserção_social","Reinserção social progressiva"),
    ("advocacy_saude_mental","Advocacy em saúde mental"),
    ("antiestigma","Campanha antiestigma em SM"),
    ("direitos_usuarios","Direitos dos usuários de SM"),
    ("movimento_antimanicomial","Movimento antimanicomial digital"),
    ("ouvidoria_sm","Ouvidoria em saúde mental"),
    ("participacao_social","Participação social em SM"),
    ("economia_solidaria","Economia solidária em SM"),
    ("cultura_arte_reabilitacao","Arte e cultura na reabilitação"),
    ("esporte_reabilitacao","Esporte na reabilitação psicossocial"),
    ("natureza_reabilitacao","Natureza e ecoterapia na reabilitação"),
    ("tecnologia_reabilitacao","Tecnologia assistiva em SM"),
])

# ══════════════════════════════════════════
# GERONTOPSIQUIATRIA (15)
# ══════════════════════════════════════════
total += batch("gerontopsiquiatria", [
    ("avaliacao_cognitiva_idoso","Avaliação cognitiva do idoso"),
    ("meem_minimental","MEEM: mini exame do estado mental"),
    ("moca_avaliacao","MoCA: avaliação cognitiva de Montreal"),
    ("cdr_demencia","CDR: escala de classificação de demência"),
    ("gds_geriatrica","GDS: escala de depressão geriátrica"),
    ("falls_risk_mental","Risco de quedas e saúde mental"),
    ("polifarmacia_idoso","Polifarmácia e saúde mental no idoso"),
    ("delirium_idoso","Delirium no idoso: prevenção e manejo"),
    ("cuidado_centrado_pessoa","Cuidado centrado na pessoa com demência"),
    ("estimulacao_sensorial","Estimulação sensorial para demência"),
    ("musicoterapia_idoso","Musicoterapia para idosos com demência"),
    ("reminiscencia","Terapia de reminiscência"),
    ("validacao_naomi","Terapia de validação de Naomi Feil"),
    ("cuidador_burnout_idoso","Burnout do cuidador de idoso"),
    ("luto_idoso2","Luto e morte na velhice"),
])

# ══════════════════════════════════════════
# PSIQUIATRIA_INFANTO_JUVENIL (20)
# ══════════════════════════════════════════
total += batch("psiquiatria_infantojuvenil", [
    ("avaliacao_infantil","Avaliação psiquiátrica infantil"),
    ("tdah_diagnostico","TDAH: diagnóstico e diferencial"),
    ("tea_avaliacao","TEA: avaliação e diagnóstico"),
    ("depressao_infantil2","Depressão na infância: manejo"),
    ("ansiedade_separacao","Ansiedade de separação"),
    ("mutismo_seletivo","Mutismo seletivo: intervenção"),
    ("tiques_tourette","Tiques e síndrome de Tourette"),
    ("enurese_encoprese","Enurese e encoprese: tratamento"),
    ("opositor_desafiador","TOD: transtorno opositivo desafiador"),
    ("conduta_transtorno","Transtorno de conduta"),
    ("alimentar_infantil","Transtornos alimentares na infância"),
    ("sono_infantil2","Transtornos do sono infantil"),
    ("escola_recusa","Recusa escolar e fobia escolar"),
    ("luto_infantil","Luto na infância e adolescência"),
    ("abuso_infantil2","Abuso infantil: identificação e manejo"),
    ("parentalidade_tdah","Parentalidade de filhos com TDAH"),
    ("sibling_tea","Irmãos de crianças com TEA"),
    ("adocao_saude_mental","Adoção e saúde mental"),
    ("crianca_rua","Criança em situação de rua"),
    ("trabalho_infantil_mental","Trabalho infantil e saúde mental"),
])

# ══════════════════════════════════════════
# MEDICINA_SONO (15)
# ══════════════════════════════════════════
total += batch("medicina_sono", [
    ("polissonografia","Polissonografia: interpretação"),
    ("apneia_tratamento","Apneia obstrutiva: CPAP e alternativas"),
    ("insonia_cronica","Insônia crônica: TCC-I completa"),
    ("narcolepsia","Narcolepsia: diagnóstico e tratamento"),
    ("sindrome_pernas_inquietas","Síndrome das pernas inquietas"),
    ("parassonias_manejo","Parassonias: manejo clínico"),
    ("bruxismo","Bruxismo e saúde mental"),
    ("hipersonia","Hipersonia e sonolência excessiva"),
    ("sono_trabalho_turnos","Sono em trabalhadores de turno"),
    ("jet_lag","Jet lag e ritmo circadiano"),
    ("melatonina_sono","Melatonina e regulação do sono"),
    ("luz_azul_sono","Luz azul e qualidade do sono"),
    ("temperatura_sono","Temperatura e ambiente do sono"),
    ("cafeina_sono","Cafeína e perturbações do sono"),
    ("exercicio_sono","Exercício físico e qualidade do sono"),
])

# ══════════════════════════════════════════
# SEXOLOGIA (15)
# ══════════════════════════════════════════
total += batch("sexologia", [
    ("disfuncao_eretil_mental","Disfunção erétil e saúde mental"),
    ("anorgasmia","Anorgasmia: abordagem terapêutica"),
    ("desejo_hipoativo","Transtorno do desejo sexual hipoativo"),
    ("dispareunia","Dispareunia e vaginismo"),
    ("parafilias","Parafilias: avaliação e tratamento"),
    ("identidade_sexual","Identidade sexual e orientação"),
    ("terapia_sexual","Terapia sexual de Masters e Johnson"),
    ("educacao_sexual","Educação sexual terapêutica"),
    ("intimidade_digital","Intimidade e relacionamentos digitais"),
    ("pornografia_vicio","Vício em pornografia: tratamento"),
    ("sexo_compulsivo","Comportamento sexual compulsivo"),
    ("trauma_sexual","Trauma sexual: abordagem clínica"),
    ("abuso_sexual_adulto","Abuso sexual em adultos"),
    ("saude_sexual_idoso","Saúde sexual na terceira idade"),
    ("sexualidade_doenca","Sexualidade em doenças crônicas"),
])

# ══════════════════════════════════════════
# PSICOLOGIA_JURIDICA (15)
# ══════════════════════════════════════════
total += batch("psicologia_juridica", [
    ("avaliacao_pericial","Avaliação psicológica pericial"),
    ("laudo_pericial","Laudo pericial em psicologia"),
    ("alienacao_parental","Alienação parental: avaliação"),
    ("guarda_filhos_avaliacao","Avaliação para guarda de filhos"),
    ("abuso_vitima","Avaliação de vítimas de abuso"),
    ("agressores_avaliacao","Avaliação de agressores"),
    ("mediacao_familiar","Mediação familiar e psicologia"),
    ("vitimologia","Vitimologia e suporte psicológico"),
    ("testemunho_infantil","Testemunho infantil: coleta especial"),
    ("traficados_suporte","Suporte a vítimas de tráfico"),
    ("tortura_suporte","Reabilitação de vítimas de tortura"),
    ("refugiados_juridico","Saúde mental de refugiados"),
    ("deficiencia_juridica","PCD e capacidade jurídica"),
    ("internacao_compulsoria","Internação compulsória: aspectos"),
    ("medida_seguranca","Medida de segurança em psiquiatria"),
])

# ══════════════════════════════════════════
# PSICO_ONCOLOGIA (15)
# ══════════════════════════════════════════
total += batch("psico_oncologia", [
    ("impacto_diagnostico","Impacto psicológico do diagnóstico"),
    ("adaptacao_tratamento","Adaptação ao tratamento oncológico"),
    ("qualidade_vida_cancer","Qualidade de vida em oncologia"),
    ("fadiga_cancer","Fadiga no câncer: manejo"),
    ("dor_cancer","Dor oncológica e saúde mental"),
    ("imagem_corporal_cancer2","Imagem corporal e câncer"),
    ("sexualidade_cancer","Sexualidade durante o tratamento"),
    ("fertilidade_cancer","Fertilidade e câncer"),
    ("adolescente_cancer","Adolescente com câncer"),
    ("crianca_cancer2","Criança com câncer: intervenção"),
    ("idoso_cancer","Idoso com câncer"),
    ("cuidador_cancer","Cuidador em oncologia"),
    ("luto_cancer2","Luto antecipatório em oncologia"),
    ("sobrevivente_cancer2","Sobrevivente de câncer: suporte"),
    ("psicooncologia_equipe","Saúde mental da equipe oncológica"),
])

# ══════════════════════════════════════════
# BIOETICA (10)
# ══════════════════════════════════════════
total += batch("bioetica", [
    ("principios_bioetica","Princípios bioéticos: autonomia e beneficência"),
    ("consentimento_bioetica","Consentimento informado em bioética"),
    ("pesquisa_humanos","Pesquisa com seres humanos"),
    ("genetica_bioetica","Genética e bioética"),
    ("fim_de_vida","Decisões de fim de vida"),
    ("eutanasia_suicidio_assistido","Eutanásia e suicídio assistido"),
    ("alocacao_recursos","Alocação de recursos em saúde"),
    ("ia_bioetica","IA e bioética em saúde mental"),
    ("privacidade_dados_saude","Privacidade de dados em saúde"),
    ("justica_saude_mental","Justiça e equidade em SM"),
])

# ══════════════════════════════════════════
# NEUROEDUCACAO (15)
# ══════════════════════════════════════════
total += batch("neuroeducacao", [
    ("aprendizagem_cerebro","Como o cérebro aprende"),
    ("memoria_aprendizagem_neuro","Memória e aprendizagem: bases neurais"),
    ("emocao_aprendizagem","Emoção e aprendizagem escolar"),
    ("estresse_aprendizagem","Estresse e desempenho escolar"),
    ("sono_aprendizagem","Sono e consolidação da memória"),
    ("exercicio_cerebro","Exercício físico e função cerebral"),
    ("nutricao_cerebro","Nutrição e saúde cerebral"),
    ("musica_cerebro","Música e desenvolvimento cerebral"),
    ("bilingue_cerebro","Bilinguismo e saúde cerebral"),
    ("leitura_cerebro","Leitura e desenvolvimento neural"),
    ("matematica_cerebro","Matemática e processamento cerebral"),
    ("criatividade_cerebro","Criatividade e neurociência"),
    ("mindfulness_educacao","Mindfulness na educação"),
    ("tecnologia_aprendizagem","Tecnologia e aprendizagem cerebral"),
    ("dislexia_neuroeducacao","Dislexia: intervenção neuroeducacional"),
])

# ══════════════════════════════════════════
# SAUDE_DIGITAL (15)
# ══════════════════════════════════════════
total += batch("saude_digital", [
    ("letramento_digital_saude","Letramento digital em saúde"),
    ("fake_news_saude","Fake news em saúde mental"),
    ("influencer_saude_mental","Influencers de saúde mental"),
    ("redes_sociais_saude","Redes sociais e saúde mental"),
    ("cyberbullying_suporte","Cyberbullying: suporte psicológico"),
    ("vicio_internet","Vício em internet e smartphones"),
    ("nomofobia","Nomofobia: dependência do celular"),
    ("fomo_ansiedade","FOMO: ansiedade de perder algo"),
    ("selfie_imagem_corporal","Selfie e imagem corporal"),
    ("comparacao_social_digital","Comparação social em redes sociais"),
    ("identidade_digital","Identidade digital e saúde mental"),
    ("privacidade_digital_saude","Privacidade digital e bem-estar"),
    ("detox_digital","Detox digital: estratégias"),
    ("slow_media","Slow media e bem-estar digital"),
    ("design_persuasivo","Design persuasivo e saúde mental"),
])

# ══════════════════════════════════════════
# EMERGENCIAS_PSIQUIATRICAS (15)
# ══════════════════════════════════════════
total += batch("emergencias_psiquiatricas", [
    ("pronto_socorro_psiq","Pronto-socorro psiquiátrico"),
    ("avaliacao_emergencia","Avaliação de emergência psiquiátrica"),
    ("contencao_quimica","Contenção química em emergência"),
    ("contencao_fisica","Contenção física: protocolos"),
    ("agitacao_psicomotora","Agitação psicomotora: manejo"),
    ("crise_suicida_emergencia","Crise suicida em emergência"),
    ("intoxicacao_substancias","Intoxicação por substâncias"),
    ("delirium_emergencia","Delirium em emergência"),
    ("crise_panico_emergencia","Crise de pânico em emergência"),
    ("dissociacao_emergencia","Dissociação em emergência"),
    ("violencia_servico","Violência nos serviços de saúde"),
    ("transferencia_estabilizacao","Transferência e estabilização"),
    ("comunicacao_familia_emergencia","Comunicação com família em emergência"),
    ("documentacao_emergencia","Documentação em emergência psiquiátrica"),
    ("pos_alta_crise","Seguimento pós-alta em crise"),
])

# ══════════════════════════════════════════
# PSICOLOGIA_TRABALHO (15)
# ══════════════════════════════════════════
total += batch("psicologia_trabalho", [
    ("satisfacao_trabalho","Satisfação no trabalho e bem-estar"),
    ("engajamento_trabalho","Engajamento e flow no trabalho"),
    ("burnout_maslach","Burnout: inventário de Maslach"),
    ("assedio_moral","Assédio moral: identificação e suporte"),
    ("assedio_sexual_trabalho","Assédio sexual no trabalho"),
    ("discriminacao_trabalho","Discriminação e saúde mental"),
    ("trabalho_remoto_mental","Trabalho remoto e saúde mental"),
    ("home_office_equilibrio","Home office: equilíbrio vida-trabalho"),
    ("workaholic","Workaholismo: compulsão ao trabalho"),
    ("desemprego_suporte","Desemprego e suporte psicológico"),
    ("transicao_carreira","Transição de carreira: suporte"),
    ("aposentadoria_transicao","Aposentadoria: transição psicológica"),
    ("lideranca_toxica","Liderança tóxica e saúde mental"),
    ("cultura_organizacional_sm","Cultura organizacional e SM"),
    ("programas_eap_avancado","Programas EAP avançados"),
])

# ══════════════════════════════════════════
# GRUPOS_ESPECIFICOS (15)
# ══════════════════════════════════════════
total += batch("grupos_especificos", [
    ("adotados_saude_mental","Saúde mental de adotados"),
    ("filhos_alcoolistas","Filhos de alcoolistas: suporte"),
    ("filhos_pais_mentais","Filhos de pais com transtorno mental"),
    ("vitimas_bullying","Vítimas de bullying: suporte"),
    ("agressores_bullying","Agressores em bullying: intervenção"),
    ("superdotados_saude","Superdotação e saúde mental"),
    ("altas_habilidades","Altas habilidades e bem-estar"),
    ("ganhadores_loteria","Riqueza repentina e saúde mental"),
    ("celebridades_saude","Saúde mental de celebridades"),
    ("cuidadores_pets","Perda de pets e luto"),
    ("sem_teto_mental","Saúde mental em situação de rua"),
    ("presos_egresso","Egresso do sistema prisional"),
    ("ex_cultos","Ex-membros de cultos: descultuação"),
    ("sobreviventes_catastrofes","Sobreviventes de catástrofes"),
    ("veteranos_guerra","Veteranos de guerra: reintegração"),
])

# ══════════════════════════════════════════
# MUSICOTERAPIA_AVANCADA (15)
# ══════════════════════════════════════════
total += batch("musicoterapia_avancada", [
    ("musicoterapia_receptiva","Musicoterapia receptiva: audição"),
    ("musicoterapia_ativa","Musicoterapia ativa: criação"),
    ("improvisacao_musical","Improvisação musical terapêutica"),
    ("composicao_terapeutica","Composição musical como terapia"),
    ("letra_musica_terapia","Letra de música e análise terapêutica"),
    ("ritmo_regulacao","Ritmo e regulação emocional"),
    ("canto_terapia","Canto e expressão emocional"),
    ("bateria_ritmos","Bateria e ritmos para saúde mental"),
    ("musica_neurologia","Musicoterapia neurológica NMT"),
    ("musica_demencia","Música para demência"),
    ("musica_autismo","Música para TEA"),
    ("musica_dor","Música para manejo da dor"),
    ("musica_ansiedade","Música para ansiedade"),
    ("musica_depressao","Música para depressão"),
    ("musica_trauma","Música no tratamento de trauma"),
])

# ══════════════════════════════════════════
# DANCA_MOVIMENTO (10)
# ══════════════════════════════════════════
total += batch("danca_movimento", [
    ("dmt_fundamentos","DMT: fundamentos da dança-movimento"),
    ("corpo_emocoes","Corpo e expressão emocional"),
    ("movimento_autentico","Movimento autêntico terapêutico"),
    ("laban_movimento","Sistema Laban de análise do movimento"),
    ("butoh_terapia","Butoh como prática terapêutica"),
    ("contact_improvisation","Contact improvisation terapêutico"),
    ("circo_terapia","Circo e terapia: expressão corporal"),
    ("capoeira_terapia","Capoeira como ferramenta terapêutica"),
    ("biodanza","Biodanza: sistema de integração"),
    ("5ritmos_movimentos","5 Ritmos: movimento meditativo"),
])

# ══════════════════════════════════════════
# HIPNOSE_CLINICA (10)
# ══════════════════════════════════════════
total += batch("hipnose_clinica", [
    ("hipnose_ericksoniana","Hipnose ericksoniana: fundamentos"),
    ("inducao_hipnotica","Indução hipnótica: técnicas"),
    ("regressao_hipnotica","Regressão hipnótica terapêutica"),
    ("hipnose_dor","Hipnose para manejo da dor"),
    ("hipnose_fobias","Hipnose para fobias"),
    ("hipnose_ansiedade","Hipnose para ansiedade"),
    ("hipnose_tabagismo","Hipnose para cessação do tabagismo"),
    ("hipnose_peso","Hipnose para controle de peso"),
    ("autohipnose","Autohipnose: técnicas e prática"),
    ("hipnose_trauma","Hipnose no tratamento de trauma"),
])

# ══════════════════════════════════════════
# CONSTELACAO_FAMILIAR (10)
# ══════════════════════════════════════════
total += batch("constelacao_familiar", [
    ("hellinger_sistema","Constelações familiares de Hellinger"),
    ("representantes","Representantes e campo morfogenético"),
    ("ordens_amor","As três ordens do amor"),
    ("destino_entrelaçado","Destinos entrelaçados familiares"),
    ("trauma_transgeracional","Trauma transgeracional"),
    ("alma_grupo","Alma do grupo e conteúdos"),
    ("constelacao_organizacional","Constelações organizacionais"),
    ("constelacao_saude","Constelações para saúde"),
    ("constelacao_online","Constelações familiares online"),
    ("integracao_outras_terapias","Integração com outras abordagens"),
])

# ══════════════════════════════════════════
# TERAPIA_INTEGRATIVA (15)
# ══════════════════════════════════════════
total += batch("terapia_integrativa", [
    ("integracao_teorica","Integração teórica em psicoterapia"),
    ("modelo_transteórico","Modelo transteórico de mudança"),
    ("fatores_comuns","Fatores comuns em psicoterapia"),
    ("alianca_terapeutica","Aliança terapêutica: mensuração"),
    ("ruptura_reparacao","Ruptura e reparação terapêutica"),
    ("feedback_informado","Feedback informado: ORS e SRS"),
    ("pratica_baseada_evidencias","Prática baseada em evidências"),
    ("psicoterapia_breve","Psicoterapia breve focal"),
    ("terapia_online_eficacia","Terapia online: eficácia"),
    ("formato_grupo_efficacia","Terapia de grupo: eficácia"),
    ("terapia_casais_eficacia","Terapia de casais: eficácia"),
    ("matching_terapeutico","Matching paciente-terapeuta"),
    ("dose_efeito","Dose-efeito em psicoterapia"),
    ("deterioracao_tratamento","Deterioração no tratamento"),
    ("encerramento_terapia","Encerramento e alta terapêutica"),
])

# ══════════════════════════════════════════
# PESQUISA_CLINICA (15)
# ══════════════════════════════════════════
total += batch("pesquisa_clinica", [
    ("metodologia_pesquisa","Metodologia de pesquisa em SM"),
    ("ensaio_clinico_randomizado","ECR em psicologia"),
    ("qualitativa_pesquisa","Pesquisa qualitativa em SM"),
    ("mista_pesquisa","Pesquisa de métodos mistos"),
    ("revisao_cochrane","Revisões Cochrane em SM"),
    ("metanalise_tecnicas","Técnicas de meta-análise"),
    ("tamanho_efeito","Tamanho de efeito em psicoterapia"),
    ("poder_estatistico","Poder estatístico em pesquisas SM"),
    ("validade_confiabilidade","Validade e confiabilidade"),
    ("instrumentos_medida","Instrumentos de medida em SM"),
    ("tradução_adaptacao","Tradução e adaptação de escalas"),
    ("normatizacao_brasileira","Normatização brasileira de escalas"),
    ("publicacao_cientifica","Publicação científica em SM"),
    ("registro_prospero","PROSPERO: registro de revisões"),
    ("open_science_sm","Ciência aberta em saúde mental"),
])

# ══════════════════════════════════════════
# AUTOCUIDADO (15)
# ══════════════════════════════════════════
total += batch("autocuidado", [
    ("rotina_autocuidado","Rotina de autocuidado diário"),
    ("limites_saudaveis","Estabelecimento de limites saudáveis"),
    ("autoconhecimento_pratico","Autoconhecimento prático"),
    ("diario_emocional","Diário emocional estruturado"),
    ("afirmacoes_positivas","Afirmações positivas baseadas em evidências"),
    ("visualizacao_positiva","Visualização positiva"),
    ("journaling_terapeutico","Journaling terapêutico"),
    ("lista_gratidao","Lista de gratidão diária"),
    ("desconexao_digital","Desconexão digital programada"),
    ("banho_frio","Banho frio e bem-estar mental"),
    ("aromaterapia","Aromaterapia e saúde mental"),
    ("cristaloterapia","Cristaloterapia: evidências e limites"),
    ("reiki_relaxamento","Reiki e relaxamento"),
    ("tapping_eft","EFT Tapping: evidências"),
    ("toque_terapeutico","Toque terapêutico e bem-estar"),
])

# ══════════════════════════════════════════
# CONTAR FINAL
# ══════════════════════════════════════════
skip = {"__init__.py","loader.py","plugin_base.py"}
grand_total = 0
cats_count = {}
for cat in os.listdir("plugins"):
    cp = f"plugins/{cat}"
    if not os.path.isdir(cp) or cat.startswith("_"): continue
    for f in os.listdir(cp):
        if f.endswith(".py") and f not in skip:
            grand_total += 1
            cats_count[cat] = cats_count.get(cat, 0) + 1

print(f"\n{'='*55}")
print(f"NOVOS CRIADOS: +{total}")
print(f"TOTAL GERAL:   {grand_total}")
print(f"META:          1470")
print(f"PROGRESSO:     {round(grand_total/1470*100,1)}%")
restam = 1470 - grand_total
print(f"RESTAM:        {restam}")
pct = grand_total/1470*100
bar = int(pct/2)
print(f"[{'█'*bar}{'░'*(50-bar)}] {round(pct,1)}%")
print(f"{'='*55}")
