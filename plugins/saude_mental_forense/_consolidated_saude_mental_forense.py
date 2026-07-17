from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_NICHD_protocol = APIRouter(prefix="/api/v1/saude_mental/NICHD_protocol", tags=["saude_mental_forense"])
router_Stockholm_syndrome = APIRouter(prefix="/api/v1/saude_mental/Stockholm_syndrome", tags=["saude_mental_forense"])
router_abel_assessment = APIRouter(prefix="/api/v1/saude_mental/abel_assessment", tags=["saude_mental_forense"])
router_actuarial_risk = APIRouter(prefix="/api/v1/saude_mental/actuarial_risk", tags=["saude_mental_forense"])
router_automatism = APIRouter(prefix="/api/v1/saude_mental/automatism", tags=["saude_mental_forense"])
router_avaliacao_pericial2 = APIRouter(prefix="/api/v1/saude_mental/avaliacao_pericial2", tags=["saude_mental_forense"])
router_battered_woman_syndr = APIRouter(prefix="/api/v1/saude_mental/battered_woman_syndrome", tags=["saude_mental_forense"])
router_best_interests_child = APIRouter(prefix="/api/v1/saude_mental/best_interests_child", tags=["saude_mental_forense"])
router_brain_scanning_foren = APIRouter(prefix="/api/v1/saude_mental/brain_scanning_forensic", tags=["saude_mental_forense"])
router_capacidade_civil2 = APIRouter(prefix="/api/v1/saude_mental/capacidade_civil2", tags=["saude_mental_forense"])
router_child_abuse_assessme = APIRouter(prefix="/api/v1/saude_mental/child_abuse_assessment", tags=["saude_mental_forense"])
router_child_interview = APIRouter(prefix="/api/v1/saude_mental/child_interview", tags=["saude_mental_forense"])
router_child_testimony = APIRouter(prefix="/api/v1/saude_mental/child_testimony", tags=["saude_mental_forense"])
router_clinical_risk = APIRouter(prefix="/api/v1/saude_mental/clinical_risk", tags=["saude_mental_forense"])
router_coercive_control_for = APIRouter(prefix="/api/v1/saude_mental/coercive_control_forensic", tags=["saude_mental_forense"])
router_coercive_interrogati = APIRouter(prefix="/api/v1/saude_mental/coercive_interrogation", tags=["saude_mental_forense"])
router_cognitive_interview = APIRouter(prefix="/api/v1/saude_mental/cognitive_interview", tags=["saude_mental_forense"])
router_community_sentencing = APIRouter(prefix="/api/v1/saude_mental/community_sentencing", tags=["saude_mental_forense"])
router_competencia_processu = APIRouter(prefix="/api/v1/saude_mental/competencia_processual", tags=["saude_mental_forense"])
router_competency_stand = APIRouter(prefix="/api/v1/saude_mental/competency_stand", tags=["saude_mental_forense"])
router_criminal_responsibil = APIRouter(prefix="/api/v1/saude_mental/criminal_responsibility", tags=["saude_mental_forense"])
router_curatela2 = APIRouter(prefix="/api/v1/saude_mental/curatela2", tags=["saude_mental_forense"])
router_custody_evaluation = APIRouter(prefix="/api/v1/saude_mental/custody_evaluation", tags=["saude_mental_forense"])
router_diminished_responsib = APIRouter(prefix="/api/v1/saude_mental/diminished_responsibility", tags=["saude_mental_forense"])
router_diversion_programs = APIRouter(prefix="/api/v1/saude_mental/diversion_programs", tags=["saude_mental_forense"])
router_domestic_violence_ri = APIRouter(prefix="/api/v1/saude_mental/domestic_violence_risk", tags=["saude_mental_forense"])
router_emotional_abuse_asse = APIRouter(prefix="/api/v1/saude_mental/emotional_abuse_assessmen", tags=["saude_mental_forense"])
router_exhibitionism_assess = APIRouter(prefix="/api/v1/saude_mental/exhibitionism_assess", tags=["saude_mental_forense"])
router_extreme_emotional = APIRouter(prefix="/api/v1/saude_mental/extreme_emotional", tags=["saude_mental_forense"])
router_eyewitness_testimony = APIRouter(prefix="/api/v1/saude_mental/eyewitness_testimony", tags=["saude_mental_forense"])
router_false_confession = APIRouter(prefix="/api/v1/saude_mental/false_confession", tags=["saude_mental_forense"])
router_false_memory = APIRouter(prefix="/api/v1/saude_mental/false_memory", tags=["saude_mental_forense"])
router_feigning_cognitive = APIRouter(prefix="/api/v1/saude_mental/feigning_cognitive", tags=["saude_mental_forense"])
router_feigning_pain = APIRouter(prefix="/api/v1/saude_mental/feigning_pain", tags=["saude_mental_forense"])
router_feigning_psychopatho = APIRouter(prefix="/api/v1/saude_mental/feigning_psychopathology", tags=["saude_mental_forense"])
router_feigning_ptsd = APIRouter(prefix="/api/v1/saude_mental/feigning_ptsd", tags=["saude_mental_forense"])
router_fetishism_assess = APIRouter(prefix="/api/v1/saude_mental/fetishism_assess", tags=["saude_mental_forense"])
router_forensic_child_inter = APIRouter(prefix="/api/v1/saude_mental/forensic_child_interview", tags=["saude_mental_forense"])
router_frotteurism_assess = APIRouter(prefix="/api/v1/saude_mental/frotteurism_assess", tags=["saude_mental_forense"])
router_guilty_mind = APIRouter(prefix="/api/v1/saude_mental/guilty_mind", tags=["saude_mental_forense"])
router_hcr_20 = APIRouter(prefix="/api/v1/saude_mental/hcr_20", tags=["saude_mental_forense"])
router_heat_passion = APIRouter(prefix="/api/v1/saude_mental/heat_passion", tags=["saude_mental_forense"])
router_homicide_risk = APIRouter(prefix="/api/v1/saude_mental/homicide_risk", tags=["saude_mental_forense"])
router_imputabilidade_penal = APIRouter(prefix="/api/v1/saude_mental/imputabilidade_penal", tags=["saude_mental_forense"])
router_inimputabilidade = APIRouter(prefix="/api/v1/saude_mental/inimputabilidade", tags=["saude_mental_forense"])
router_insanity_defense = APIRouter(prefix="/api/v1/saude_mental/insanity_defense", tags=["saude_mental_forense"])
router_interdição_legal = APIRouter(prefix="/api/v1/saude_mental/interdição_legal", tags=["saude_mental_forense"])
router_interrogation_psycho = APIRouter(prefix="/api/v1/saude_mental/interrogation_psychology", tags=["saude_mental_forense"])
router_laudo_psicologico2 = APIRouter(prefix="/api/v1/saude_mental/laudo_psicologico2", tags=["saude_mental_forense"])
router_learned_helplessness = APIRouter(prefix="/api/v1/saude_mental/learned_helplessness_fore", tags=["saude_mental_forense"])
router_malingering_detectio = APIRouter(prefix="/api/v1/saude_mental/malingering_detection", tags=["saude_mental_forense"])
router_masochism_assess = APIRouter(prefix="/api/v1/saude_mental/masochism_assess", tags=["saude_mental_forense"])
router_memory_accuracy = APIRouter(prefix="/api/v1/saude_mental/memory_accuracy", tags=["saude_mental_forense"])
router_mental_state_offense = APIRouter(prefix="/api/v1/saude_mental/mental_state_offense", tags=["saude_mental_forense"])
router_miranda_rights = APIRouter(prefix="/api/v1/saude_mental/miranda_rights", tags=["saude_mental_forense"])
router_negative_response_bi = APIRouter(prefix="/api/v1/saude_mental/negative_response_bias", tags=["saude_mental_forense"])
router_neglect_assessment = APIRouter(prefix="/api/v1/saude_mental/neglect_assessment", tags=["saude_mental_forense"])
router_neuroimaging_legal = APIRouter(prefix="/api/v1/saude_mental/neuroimaging_legal", tags=["saude_mental_forense"])
router_paraphilia_assess = APIRouter(prefix="/api/v1/saude_mental/paraphilia_assess", tags=["saude_mental_forense"])
router_parental_alienation_ = APIRouter(prefix="/api/v1/saude_mental/parental_alienation_foren", tags=["saude_mental_forense"])
router_pedophile_assessment = APIRouter(prefix="/api/v1/saude_mental/pedophile_assessment", tags=["saude_mental_forense"])
router_performance_validity = APIRouter(prefix="/api/v1/saude_mental/performance_validity", tags=["saude_mental_forense"])
router_pericia_civel = APIRouter(prefix="/api/v1/saude_mental/pericia_civel", tags=["saude_mental_forense"])
router_pericia_criminal = APIRouter(prefix="/api/v1/saude_mental/pericia_criminal", tags=["saude_mental_forense"])
router_pericia_familia = APIRouter(prefix="/api/v1/saude_mental/pericia_familia", tags=["saude_mental_forense"])
router_pericia_previdenciar = APIRouter(prefix="/api/v1/saude_mental/pericia_previdenciaria", tags=["saude_mental_forense"])
router_pericia_trabalhista = APIRouter(prefix="/api/v1/saude_mental/pericia_trabalhista", tags=["saude_mental_forense"])
router_phallometric_testing = APIRouter(prefix="/api/v1/saude_mental/phallometric_testing", tags=["saude_mental_forense"])
router_physical_abuse_asses = APIRouter(prefix="/api/v1/saude_mental/physical_abuse_assessment", tags=["saude_mental_forense"])
router_police_interview = APIRouter(prefix="/api/v1/saude_mental/police_interview", tags=["saude_mental_forense"])
router_polygraph_forensic = APIRouter(prefix="/api/v1/saude_mental/polygraph_forensic", tags=["saude_mental_forense"])
router_psicologia_forense2 = APIRouter(prefix="/api/v1/saude_mental/psicologia_forense2", tags=["saude_mental_forense"])
router_psychopathy_checklis = APIRouter(prefix="/api/v1/saude_mental/psychopathy_checklist", tags=["saude_mental_forense"])
router_psychopathy_pcl = APIRouter(prefix="/api/v1/saude_mental/psychopathy_pcl", tags=["saude_mental_forense"])
router_rapist_typology = APIRouter(prefix="/api/v1/saude_mental/rapist_typology", tags=["saude_mental_forense"])
router_recidivism_risk = APIRouter(prefix="/api/v1/saude_mental/recidivism_risk", tags=["saude_mental_forense"])
router_reid_technique = APIRouter(prefix="/api/v1/saude_mental/reid_technique", tags=["saude_mental_forense"])
router_response_bias = APIRouter(prefix="/api/v1/saude_mental/response_bias", tags=["saude_mental_forense"])
router_restorative_justice = APIRouter(prefix="/api/v1/saude_mental/restorative_justice", tags=["saude_mental_forense"])
router_risk_assessment2 = APIRouter(prefix="/api/v1/saude_mental/risk_assessment2", tags=["saude_mental_forense"])
router_sadism_assess = APIRouter(prefix="/api/v1/saude_mental/sadism_assess", tags=["saude_mental_forense"])
router_secondary_victimizat = APIRouter(prefix="/api/v1/saude_mental/secondary_victimization", tags=["saude_mental_forense"])
router_semi_imputabilidade = APIRouter(prefix="/api/v1/saude_mental/semi_imputabilidade", tags=["saude_mental_forense"])
router_sex_offender_assessm = APIRouter(prefix="/api/v1/saude_mental/sex_offender_assessment", tags=["saude_mental_forense"])
router_sexual_abuse_assessm = APIRouter(prefix="/api/v1/saude_mental/sexual_abuse_assessment", tags=["saude_mental_forense"])
router_sexual_violence_risk = APIRouter(prefix="/api/v1/saude_mental/sexual_violence_risk", tags=["saude_mental_forense"])
router_simulacao_avaliacao = APIRouter(prefix="/api/v1/saude_mental/simulacao_avaliacao", tags=["saude_mental_forense"])
router_sobreposicao = APIRouter(prefix="/api/v1/saude_mental/sobreposicao", tags=["saude_mental_forense"])
router_spj_approach = APIRouter(prefix="/api/v1/saude_mental/spj_approach", tags=["saude_mental_forense"])
router_spr_inf = APIRouter(prefix="/api/v1/saude_mental/spr_inf", tags=["saude_mental_forense"])
router_stalking_risk = APIRouter(prefix="/api/v1/saude_mental/stalking_risk", tags=["saude_mental_forense"])
router_static_99 = APIRouter(prefix="/api/v1/saude_mental/static_99", tags=["saude_mental_forense"])
router_structured_risk = APIRouter(prefix="/api/v1/saude_mental/structured_risk", tags=["saude_mental_forense"])
router_suggestibility = APIRouter(prefix="/api/v1/saude_mental/suggestibility", tags=["saude_mental_forense"])
router_suicide_risk_forensi = APIRouter(prefix="/api/v1/saude_mental/suicide_risk_forensic", tags=["saude_mental_forense"])
router_symptom_validity = APIRouter(prefix="/api/v1/saude_mental/symptom_validity", tags=["saude_mental_forense"])
router_testamentaria = APIRouter(prefix="/api/v1/saude_mental/testamentaria", tags=["saude_mental_forense"])
router_therapeutic_jurispru = APIRouter(prefix="/api/v1/saude_mental/therapeutic_jurisprudence", tags=["saude_mental_forense"])
router_validity_testing = APIRouter(prefix="/api/v1/saude_mental/validity_testing", tags=["saude_mental_forense"])
router_victim_blaming = APIRouter(prefix="/api/v1/saude_mental/victim_blaming", tags=["saude_mental_forense"])
router_victim_psychology = APIRouter(prefix="/api/v1/saude_mental/victim_psychology", tags=["saude_mental_forense"])
router_victimology = APIRouter(prefix="/api/v1/saude_mental/victimology", tags=["saude_mental_forense"])
router_violence_risk = APIRouter(prefix="/api/v1/saude_mental/violence_risk", tags=["saude_mental_forense"])
router_voice_stress = APIRouter(prefix="/api/v1/saude_mental/voice_stress", tags=["saude_mental_forense"])
router_voyeur_assess = APIRouter(prefix="/api/v1/saude_mental/voyeur_assess", tags=["saude_mental_forense"])
router_vrag_risk = APIRouter(prefix="/api/v1/saude_mental/vrag_risk", tags=["saude_mental_forense"])

@router_NICHD_protocol.get("")
async def i_NICHD_protocol():
    return {"p":"saude_mental_fo_NICHD_protocol","s":"ativo","t":datetime.utcnow().isoformat()}
@router_Stockholm_syndrome.get("")
async def i_Stockholm_syndrome():
    return {"p":"saude_mental_fo_Stockholm_syndrome","s":"ativo","t":datetime.utcnow().isoformat()}
@router_abel_assessment.get("")
async def i_abel_assessment():
    return {"p":"saude_mental_fo_abel_assessment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_actuarial_risk.get("")
async def i_actuarial_risk():
    return {"p":"saude_mental_fo_actuarial_risk","s":"ativo","t":datetime.utcnow().isoformat()}
@router_automatism.get("")
async def i_automatism():
    return {"p":"saude_mental_fo_automatism","s":"ativo","t":datetime.utcnow().isoformat()}
@router_avaliacao_pericial2.get("")
async def i_avaliacao_pericial2():
    return {"p":"saude_mental_fo_avaliacao_pericial2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_battered_woman_syndr.get("")
async def i_battered_woman_syndr():
    return {"p":"saude_mental_fo_battered_woman_syndr","s":"ativo","t":datetime.utcnow().isoformat()}
@router_best_interests_child.get("")
async def i_best_interests_child():
    return {"p":"saude_mental_fo_best_interests_child","s":"ativo","t":datetime.utcnow().isoformat()}
@router_brain_scanning_foren.get("")
async def i_brain_scanning_foren():
    return {"p":"saude_mental_fo_brain_scanning_foren","s":"ativo","t":datetime.utcnow().isoformat()}
@router_capacidade_civil2.get("")
async def i_capacidade_civil2():
    return {"p":"saude_mental_fo_capacidade_civil2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_child_abuse_assessme.get("")
async def i_child_abuse_assessme():
    return {"p":"saude_mental_fo_child_abuse_assessme","s":"ativo","t":datetime.utcnow().isoformat()}
@router_child_interview.get("")
async def i_child_interview():
    return {"p":"saude_mental_fo_child_interview","s":"ativo","t":datetime.utcnow().isoformat()}
@router_child_testimony.get("")
async def i_child_testimony():
    return {"p":"saude_mental_fo_child_testimony","s":"ativo","t":datetime.utcnow().isoformat()}
@router_clinical_risk.get("")
async def i_clinical_risk():
    return {"p":"saude_mental_fo_clinical_risk","s":"ativo","t":datetime.utcnow().isoformat()}
@router_coercive_control_for.get("")
async def i_coercive_control_for():
    return {"p":"saude_mental_fo_coercive_control_for","s":"ativo","t":datetime.utcnow().isoformat()}
@router_coercive_interrogati.get("")
async def i_coercive_interrogati():
    return {"p":"saude_mental_fo_coercive_interrogati","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cognitive_interview.get("")
async def i_cognitive_interview():
    return {"p":"saude_mental_fo_cognitive_interview","s":"ativo","t":datetime.utcnow().isoformat()}
@router_community_sentencing.get("")
async def i_community_sentencing():
    return {"p":"saude_mental_fo_community_sentencing","s":"ativo","t":datetime.utcnow().isoformat()}
@router_competencia_processu.get("")
async def i_competencia_processu():
    return {"p":"saude_mental_fo_competencia_processu","s":"ativo","t":datetime.utcnow().isoformat()}
@router_competency_stand.get("")
async def i_competency_stand():
    return {"p":"saude_mental_fo_competency_stand","s":"ativo","t":datetime.utcnow().isoformat()}
@router_criminal_responsibil.get("")
async def i_criminal_responsibil():
    return {"p":"saude_mental_fo_criminal_responsibil","s":"ativo","t":datetime.utcnow().isoformat()}
@router_curatela2.get("")
async def i_curatela2():
    return {"p":"saude_mental_fo_curatela2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_custody_evaluation.get("")
async def i_custody_evaluation():
    return {"p":"saude_mental_fo_custody_evaluation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_diminished_responsib.get("")
async def i_diminished_responsib():
    return {"p":"saude_mental_fo_diminished_responsib","s":"ativo","t":datetime.utcnow().isoformat()}
@router_diversion_programs.get("")
async def i_diversion_programs():
    return {"p":"saude_mental_fo_diversion_programs","s":"ativo","t":datetime.utcnow().isoformat()}
@router_domestic_violence_ri.get("")
async def i_domestic_violence_ri():
    return {"p":"saude_mental_fo_domestic_violence_ri","s":"ativo","t":datetime.utcnow().isoformat()}
@router_emotional_abuse_asse.get("")
async def i_emotional_abuse_asse():
    return {"p":"saude_mental_fo_emotional_abuse_asse","s":"ativo","t":datetime.utcnow().isoformat()}
@router_exhibitionism_assess.get("")
async def i_exhibitionism_assess():
    return {"p":"saude_mental_fo_exhibitionism_assess","s":"ativo","t":datetime.utcnow().isoformat()}
@router_extreme_emotional.get("")
async def i_extreme_emotional():
    return {"p":"saude_mental_fo_extreme_emotional","s":"ativo","t":datetime.utcnow().isoformat()}
@router_eyewitness_testimony.get("")
async def i_eyewitness_testimony():
    return {"p":"saude_mental_fo_eyewitness_testimony","s":"ativo","t":datetime.utcnow().isoformat()}
@router_false_confession.get("")
async def i_false_confession():
    return {"p":"saude_mental_fo_false_confession","s":"ativo","t":datetime.utcnow().isoformat()}
@router_false_memory.get("")
async def i_false_memory():
    return {"p":"saude_mental_fo_false_memory","s":"ativo","t":datetime.utcnow().isoformat()}
@router_feigning_cognitive.get("")
async def i_feigning_cognitive():
    return {"p":"saude_mental_fo_feigning_cognitive","s":"ativo","t":datetime.utcnow().isoformat()}
@router_feigning_pain.get("")
async def i_feigning_pain():
    return {"p":"saude_mental_fo_feigning_pain","s":"ativo","t":datetime.utcnow().isoformat()}
@router_feigning_psychopatho.get("")
async def i_feigning_psychopatho():
    return {"p":"saude_mental_fo_feigning_psychopatho","s":"ativo","t":datetime.utcnow().isoformat()}
@router_feigning_ptsd.get("")
async def i_feigning_ptsd():
    return {"p":"saude_mental_fo_feigning_ptsd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fetishism_assess.get("")
async def i_fetishism_assess():
    return {"p":"saude_mental_fo_fetishism_assess","s":"ativo","t":datetime.utcnow().isoformat()}
@router_forensic_child_inter.get("")
async def i_forensic_child_inter():
    return {"p":"saude_mental_fo_forensic_child_inter","s":"ativo","t":datetime.utcnow().isoformat()}
@router_frotteurism_assess.get("")
async def i_frotteurism_assess():
    return {"p":"saude_mental_fo_frotteurism_assess","s":"ativo","t":datetime.utcnow().isoformat()}
@router_guilty_mind.get("")
async def i_guilty_mind():
    return {"p":"saude_mental_fo_guilty_mind","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hcr_20.get("")
async def i_hcr_20():
    return {"p":"saude_mental_fo_hcr_20","s":"ativo","t":datetime.utcnow().isoformat()}
@router_heat_passion.get("")
async def i_heat_passion():
    return {"p":"saude_mental_fo_heat_passion","s":"ativo","t":datetime.utcnow().isoformat()}
@router_homicide_risk.get("")
async def i_homicide_risk():
    return {"p":"saude_mental_fo_homicide_risk","s":"ativo","t":datetime.utcnow().isoformat()}
@router_imputabilidade_penal.get("")
async def i_imputabilidade_penal():
    return {"p":"saude_mental_fo_imputabilidade_penal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_inimputabilidade.get("")
async def i_inimputabilidade():
    return {"p":"saude_mental_fo_inimputabilidade","s":"ativo","t":datetime.utcnow().isoformat()}
@router_insanity_defense.get("")
async def i_insanity_defense():
    return {"p":"saude_mental_fo_insanity_defense","s":"ativo","t":datetime.utcnow().isoformat()}
@router_interdição_legal.get("")
async def i_interdição_legal():
    return {"p":"saude_mental_fo_interdição_legal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_interrogation_psycho.get("")
async def i_interrogation_psycho():
    return {"p":"saude_mental_fo_interrogation_psycho","s":"ativo","t":datetime.utcnow().isoformat()}
@router_laudo_psicologico2.get("")
async def i_laudo_psicologico2():
    return {"p":"saude_mental_fo_laudo_psicologico2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_learned_helplessness.get("")
async def i_learned_helplessness():
    return {"p":"saude_mental_fo_learned_helplessness","s":"ativo","t":datetime.utcnow().isoformat()}
@router_malingering_detectio.get("")
async def i_malingering_detectio():
    return {"p":"saude_mental_fo_malingering_detectio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_masochism_assess.get("")
async def i_masochism_assess():
    return {"p":"saude_mental_fo_masochism_assess","s":"ativo","t":datetime.utcnow().isoformat()}
@router_memory_accuracy.get("")
async def i_memory_accuracy():
    return {"p":"saude_mental_fo_memory_accuracy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mental_state_offense.get("")
async def i_mental_state_offense():
    return {"p":"saude_mental_fo_mental_state_offense","s":"ativo","t":datetime.utcnow().isoformat()}
@router_miranda_rights.get("")
async def i_miranda_rights():
    return {"p":"saude_mental_fo_miranda_rights","s":"ativo","t":datetime.utcnow().isoformat()}
@router_negative_response_bi.get("")
async def i_negative_response_bi():
    return {"p":"saude_mental_fo_negative_response_bi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neglect_assessment.get("")
async def i_neglect_assessment():
    return {"p":"saude_mental_fo_neglect_assessment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neuroimaging_legal.get("")
async def i_neuroimaging_legal():
    return {"p":"saude_mental_fo_neuroimaging_legal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_paraphilia_assess.get("")
async def i_paraphilia_assess():
    return {"p":"saude_mental_fo_paraphilia_assess","s":"ativo","t":datetime.utcnow().isoformat()}
@router_parental_alienation_.get("")
async def i_parental_alienation_():
    return {"p":"saude_mental_fo_parental_alienation_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pedophile_assessment.get("")
async def i_pedophile_assessment():
    return {"p":"saude_mental_fo_pedophile_assessment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_performance_validity.get("")
async def i_performance_validity():
    return {"p":"saude_mental_fo_performance_validity","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pericia_civel.get("")
async def i_pericia_civel():
    return {"p":"saude_mental_fo_pericia_civel","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pericia_criminal.get("")
async def i_pericia_criminal():
    return {"p":"saude_mental_fo_pericia_criminal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pericia_familia.get("")
async def i_pericia_familia():
    return {"p":"saude_mental_fo_pericia_familia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pericia_previdenciar.get("")
async def i_pericia_previdenciar():
    return {"p":"saude_mental_fo_pericia_previdenciar","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pericia_trabalhista.get("")
async def i_pericia_trabalhista():
    return {"p":"saude_mental_fo_pericia_trabalhista","s":"ativo","t":datetime.utcnow().isoformat()}
@router_phallometric_testing.get("")
async def i_phallometric_testing():
    return {"p":"saude_mental_fo_phallometric_testing","s":"ativo","t":datetime.utcnow().isoformat()}
@router_physical_abuse_asses.get("")
async def i_physical_abuse_asses():
    return {"p":"saude_mental_fo_physical_abuse_asses","s":"ativo","t":datetime.utcnow().isoformat()}
@router_police_interview.get("")
async def i_police_interview():
    return {"p":"saude_mental_fo_police_interview","s":"ativo","t":datetime.utcnow().isoformat()}
@router_polygraph_forensic.get("")
async def i_polygraph_forensic():
    return {"p":"saude_mental_fo_polygraph_forensic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicologia_forense2.get("")
async def i_psicologia_forense2():
    return {"p":"saude_mental_fo_psicologia_forense2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psychopathy_checklis.get("")
async def i_psychopathy_checklis():
    return {"p":"saude_mental_fo_psychopathy_checklis","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psychopathy_pcl.get("")
async def i_psychopathy_pcl():
    return {"p":"saude_mental_fo_psychopathy_pcl","s":"ativo","t":datetime.utcnow().isoformat()}
@router_rapist_typology.get("")
async def i_rapist_typology():
    return {"p":"saude_mental_fo_rapist_typology","s":"ativo","t":datetime.utcnow().isoformat()}
@router_recidivism_risk.get("")
async def i_recidivism_risk():
    return {"p":"saude_mental_fo_recidivism_risk","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reid_technique.get("")
async def i_reid_technique():
    return {"p":"saude_mental_fo_reid_technique","s":"ativo","t":datetime.utcnow().isoformat()}
@router_response_bias.get("")
async def i_response_bias():
    return {"p":"saude_mental_fo_response_bias","s":"ativo","t":datetime.utcnow().isoformat()}
@router_restorative_justice.get("")
async def i_restorative_justice():
    return {"p":"saude_mental_fo_restorative_justice","s":"ativo","t":datetime.utcnow().isoformat()}
@router_risk_assessment2.get("")
async def i_risk_assessment2():
    return {"p":"saude_mental_fo_risk_assessment2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sadism_assess.get("")
async def i_sadism_assess():
    return {"p":"saude_mental_fo_sadism_assess","s":"ativo","t":datetime.utcnow().isoformat()}
@router_secondary_victimizat.get("")
async def i_secondary_victimizat():
    return {"p":"saude_mental_fo_secondary_victimizat","s":"ativo","t":datetime.utcnow().isoformat()}
@router_semi_imputabilidade.get("")
async def i_semi_imputabilidade():
    return {"p":"saude_mental_fo_semi_imputabilidade","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sex_offender_assessm.get("")
async def i_sex_offender_assessm():
    return {"p":"saude_mental_fo_sex_offender_assessm","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sexual_abuse_assessm.get("")
async def i_sexual_abuse_assessm():
    return {"p":"saude_mental_fo_sexual_abuse_assessm","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sexual_violence_risk.get("")
async def i_sexual_violence_risk():
    return {"p":"saude_mental_fo_sexual_violence_risk","s":"ativo","t":datetime.utcnow().isoformat()}
@router_simulacao_avaliacao.get("")
async def i_simulacao_avaliacao():
    return {"p":"saude_mental_fo_simulacao_avaliacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sobreposicao.get("")
async def i_sobreposicao():
    return {"p":"saude_mental_fo_sobreposicao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_spj_approach.get("")
async def i_spj_approach():
    return {"p":"saude_mental_fo_spj_approach","s":"ativo","t":datetime.utcnow().isoformat()}
@router_spr_inf.get("")
async def i_spr_inf():
    return {"p":"saude_mental_fo_spr_inf","s":"ativo","t":datetime.utcnow().isoformat()}
@router_stalking_risk.get("")
async def i_stalking_risk():
    return {"p":"saude_mental_fo_stalking_risk","s":"ativo","t":datetime.utcnow().isoformat()}
@router_static_99.get("")
async def i_static_99():
    return {"p":"saude_mental_fo_static_99","s":"ativo","t":datetime.utcnow().isoformat()}
@router_structured_risk.get("")
async def i_structured_risk():
    return {"p":"saude_mental_fo_structured_risk","s":"ativo","t":datetime.utcnow().isoformat()}
@router_suggestibility.get("")
async def i_suggestibility():
    return {"p":"saude_mental_fo_suggestibility","s":"ativo","t":datetime.utcnow().isoformat()}
@router_suicide_risk_forensi.get("")
async def i_suicide_risk_forensi():
    return {"p":"saude_mental_fo_suicide_risk_forensi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_symptom_validity.get("")
async def i_symptom_validity():
    return {"p":"saude_mental_fo_symptom_validity","s":"ativo","t":datetime.utcnow().isoformat()}
@router_testamentaria.get("")
async def i_testamentaria():
    return {"p":"saude_mental_fo_testamentaria","s":"ativo","t":datetime.utcnow().isoformat()}
@router_therapeutic_jurispru.get("")
async def i_therapeutic_jurispru():
    return {"p":"saude_mental_fo_therapeutic_jurispru","s":"ativo","t":datetime.utcnow().isoformat()}
@router_validity_testing.get("")
async def i_validity_testing():
    return {"p":"saude_mental_fo_validity_testing","s":"ativo","t":datetime.utcnow().isoformat()}
@router_victim_blaming.get("")
async def i_victim_blaming():
    return {"p":"saude_mental_fo_victim_blaming","s":"ativo","t":datetime.utcnow().isoformat()}
@router_victim_psychology.get("")
async def i_victim_psychology():
    return {"p":"saude_mental_fo_victim_psychology","s":"ativo","t":datetime.utcnow().isoformat()}
@router_victimology.get("")
async def i_victimology():
    return {"p":"saude_mental_fo_victimology","s":"ativo","t":datetime.utcnow().isoformat()}
@router_violence_risk.get("")
async def i_violence_risk():
    return {"p":"saude_mental_fo_violence_risk","s":"ativo","t":datetime.utcnow().isoformat()}
@router_voice_stress.get("")
async def i_voice_stress():
    return {"p":"saude_mental_fo_voice_stress","s":"ativo","t":datetime.utcnow().isoformat()}
@router_voyeur_assess.get("")
async def i_voyeur_assess():
    return {"p":"saude_mental_fo_voyeur_assess","s":"ativo","t":datetime.utcnow().isoformat()}
@router_vrag_risk.get("")
async def i_vrag_risk():
    return {"p":"saude_mental_fo_vrag_risk","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_saude_mental_forense(PluginBase):
    name = "consolidated_saude_mental_forense"
    def setup(self, app):
        app.include_router(router_NICHD_protocol)
        app.include_router(router_Stockholm_syndrome)
        app.include_router(router_abel_assessment)
        app.include_router(router_actuarial_risk)
        app.include_router(router_automatism)
        app.include_router(router_avaliacao_pericial2)
        app.include_router(router_battered_woman_syndr)
        app.include_router(router_best_interests_child)
        app.include_router(router_brain_scanning_foren)
        app.include_router(router_capacidade_civil2)
        app.include_router(router_child_abuse_assessme)
        app.include_router(router_child_interview)
        app.include_router(router_child_testimony)
        app.include_router(router_clinical_risk)
        app.include_router(router_coercive_control_for)
        app.include_router(router_coercive_interrogati)
        app.include_router(router_cognitive_interview)
        app.include_router(router_community_sentencing)
        app.include_router(router_competencia_processu)
        app.include_router(router_competency_stand)
        app.include_router(router_criminal_responsibil)
        app.include_router(router_curatela2)
        app.include_router(router_custody_evaluation)
        app.include_router(router_diminished_responsib)
        app.include_router(router_diversion_programs)
        app.include_router(router_domestic_violence_ri)
        app.include_router(router_emotional_abuse_asse)
        app.include_router(router_exhibitionism_assess)
        app.include_router(router_extreme_emotional)
        app.include_router(router_eyewitness_testimony)
        app.include_router(router_false_confession)
        app.include_router(router_false_memory)
        app.include_router(router_feigning_cognitive)
        app.include_router(router_feigning_pain)
        app.include_router(router_feigning_psychopatho)
        app.include_router(router_feigning_ptsd)
        app.include_router(router_fetishism_assess)
        app.include_router(router_forensic_child_inter)
        app.include_router(router_frotteurism_assess)
        app.include_router(router_guilty_mind)
        app.include_router(router_hcr_20)
        app.include_router(router_heat_passion)
        app.include_router(router_homicide_risk)
        app.include_router(router_imputabilidade_penal)
        app.include_router(router_inimputabilidade)
        app.include_router(router_insanity_defense)
        app.include_router(router_interdição_legal)
        app.include_router(router_interrogation_psycho)
        app.include_router(router_laudo_psicologico2)
        app.include_router(router_learned_helplessness)
        app.include_router(router_malingering_detectio)
        app.include_router(router_masochism_assess)
        app.include_router(router_memory_accuracy)
        app.include_router(router_mental_state_offense)
        app.include_router(router_miranda_rights)
        app.include_router(router_negative_response_bi)
        app.include_router(router_neglect_assessment)
        app.include_router(router_neuroimaging_legal)
        app.include_router(router_paraphilia_assess)
        app.include_router(router_parental_alienation_)
        app.include_router(router_pedophile_assessment)
        app.include_router(router_performance_validity)
        app.include_router(router_pericia_civel)
        app.include_router(router_pericia_criminal)
        app.include_router(router_pericia_familia)
        app.include_router(router_pericia_previdenciar)
        app.include_router(router_pericia_trabalhista)
        app.include_router(router_phallometric_testing)
        app.include_router(router_physical_abuse_asses)
        app.include_router(router_police_interview)
        app.include_router(router_polygraph_forensic)
        app.include_router(router_psicologia_forense2)
        app.include_router(router_psychopathy_checklis)
        app.include_router(router_psychopathy_pcl)
        app.include_router(router_rapist_typology)
        app.include_router(router_recidivism_risk)
        app.include_router(router_reid_technique)
        app.include_router(router_response_bias)
        app.include_router(router_restorative_justice)
        app.include_router(router_risk_assessment2)
        app.include_router(router_sadism_assess)
        app.include_router(router_secondary_victimizat)
        app.include_router(router_semi_imputabilidade)
        app.include_router(router_sex_offender_assessm)
        app.include_router(router_sexual_abuse_assessm)
        app.include_router(router_sexual_violence_risk)
        app.include_router(router_simulacao_avaliacao)
        app.include_router(router_sobreposicao)
        app.include_router(router_spj_approach)
        app.include_router(router_spr_inf)
        app.include_router(router_stalking_risk)
        app.include_router(router_static_99)
        app.include_router(router_structured_risk)
        app.include_router(router_suggestibility)
        app.include_router(router_suicide_risk_forensi)
        app.include_router(router_symptom_validity)
        app.include_router(router_testamentaria)
        app.include_router(router_therapeutic_jurispru)
        app.include_router(router_validity_testing)
        app.include_router(router_victim_blaming)
        app.include_router(router_victim_psychology)
        app.include_router(router_victimology)
        app.include_router(router_violence_risk)
        app.include_router(router_voice_stress)
        app.include_router(router_voyeur_assess)
        app.include_router(router_vrag_risk)


plugin = Plugin_saude_mental_forense()
