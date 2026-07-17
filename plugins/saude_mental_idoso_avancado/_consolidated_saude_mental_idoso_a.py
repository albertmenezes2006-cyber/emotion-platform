from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_PTSD_elder = APIRouter(prefix="/api/v1/saude_mental/PTSD_elder", tags=["saude_mental_idoso_avancado"])
router_adult_day_program = APIRouter(prefix="/api/v1/saude_mental/adult_day_program", tags=["saude_mental_idoso_avancado"])
router_agitation_dementia2 = APIRouter(prefix="/api/v1/saude_mental/agitation_dementia2", tags=["saude_mental_idoso_avancado"])
router_alcohol_elder = APIRouter(prefix="/api/v1/saude_mental/alcohol_elder", tags=["saude_mental_idoso_avancado"])
router_alzheimer_elder = APIRouter(prefix="/api/v1/saude_mental/alzheimer_elder", tags=["saude_mental_idoso_avancado"])
router_anxiety_dementia2 = APIRouter(prefix="/api/v1/saude_mental/anxiety_dementia2", tags=["saude_mental_idoso_avancado"])
router_anxiety_elder2 = APIRouter(prefix="/api/v1/saude_mental/anxiety_elder2", tags=["saude_mental_idoso_avancado"])
router_assisted_living_ment = APIRouter(prefix="/api/v1/saude_mental/assisted_living_mental", tags=["saude_mental_idoso_avancado"])
router_autoeficacia_idoso = APIRouter(prefix="/api/v1/saude_mental/autoeficacia_idoso", tags=["saude_mental_idoso_avancado"])
router_autoestima_idoso2 = APIRouter(prefix="/api/v1/saude_mental/autoestima_idoso2", tags=["saude_mental_idoso_avancado"])
router_behavioral_dementia = APIRouter(prefix="/api/v1/saude_mental/behavioral_dementia", tags=["saude_mental_idoso_avancado"])
router_bem_estar_idoso = APIRouter(prefix="/api/v1/saude_mental/bem_estar_idoso", tags=["saude_mental_idoso_avancado"])
router_caregiver_burden2 = APIRouter(prefix="/api/v1/saude_mental/caregiver_burden2", tags=["saude_mental_idoso_avancado"])
router_caregiver_dementia = APIRouter(prefix="/api/v1/saude_mental/caregiver_dementia", tags=["saude_mental_idoso_avancado"])
router_caregiver_depression = APIRouter(prefix="/api/v1/saude_mental/caregiver_depression", tags=["saude_mental_idoso_avancado"])
router_caregiver_grief = APIRouter(prefix="/api/v1/saude_mental/caregiver_grief", tags=["saude_mental_idoso_avancado"])
router_caregiver_identity = APIRouter(prefix="/api/v1/saude_mental/caregiver_identity", tags=["saude_mental_idoso_avancado"])
router_caregiver_support2 = APIRouter(prefix="/api/v1/saude_mental/caregiver_support2", tags=["saude_mental_idoso_avancado"])
router_chronic_pain_elder2 = APIRouter(prefix="/api/v1/saude_mental/chronic_pain_elder2", tags=["saude_mental_idoso_avancado"])
router_circadian_elder = APIRouter(prefix="/api/v1/saude_mental/circadian_elder", tags=["saude_mental_idoso_avancado"])
router_cognitive_assessment = APIRouter(prefix="/api/v1/saude_mental/cognitive_assessment_elde", tags=["saude_mental_idoso_avancado"])
router_compassionate_care_e = APIRouter(prefix="/api/v1/saude_mental/compassionate_care_elder", tags=["saude_mental_idoso_avancado"])
router_controle_percebido_i = APIRouter(prefix="/api/v1/saude_mental/controle_percebido_idoso", tags=["saude_mental_idoso_avancado"])
router_daytime_sleepiness_e = APIRouter(prefix="/api/v1/saude_mental/daytime_sleepiness_elder", tags=["saude_mental_idoso_avancado"])
router_death_acceptance = APIRouter(prefix="/api/v1/saude_mental/death_acceptance", tags=["saude_mental_idoso_avancado"])
router_death_anxiety_elder = APIRouter(prefix="/api/v1/saude_mental/death_anxiety_elder", tags=["saude_mental_idoso_avancado"])
router_dementia_elder2 = APIRouter(prefix="/api/v1/saude_mental/dementia_elder2", tags=["saude_mental_idoso_avancado"])
router_depression_dementia2 = APIRouter(prefix="/api/v1/saude_mental/depression_dementia2", tags=["saude_mental_idoso_avancado"])
router_depression_elder2 = APIRouter(prefix="/api/v1/saude_mental/depression_elder2", tags=["saude_mental_idoso_avancado"])
router_dignified_dying = APIRouter(prefix="/api/v1/saude_mental/dignified_dying", tags=["saude_mental_idoso_avancado"])
router_dignity_therapy2 = APIRouter(prefix="/api/v1/saude_mental/dignity_therapy2", tags=["saude_mental_idoso_avancado"])
router_dlb_elder = APIRouter(prefix="/api/v1/saude_mental/dlb_elder", tags=["saude_mental_idoso_avancado"])
router_eating_dementia = APIRouter(prefix="/api/v1/saude_mental/eating_dementia", tags=["saude_mental_idoso_avancado"])
router_envelhecimento_bem_s = APIRouter(prefix="/api/v1/saude_mental/envelhecimento_bem_sucedi", tags=["saude_mental_idoso_avancado"])
router_envelhecimento_sauda = APIRouter(prefix="/api/v1/saude_mental/envelhecimento_saudavel2", tags=["saude_mental_idoso_avancado"])
router_existential_death = APIRouter(prefix="/api/v1/saude_mental/existential_death", tags=["saude_mental_idoso_avancado"])
router_existential_therapy_ = APIRouter(prefix="/api/v1/saude_mental/existential_therapy_elder", tags=["saude_mental_idoso_avancado"])
router_falls_mental_elder = APIRouter(prefix="/api/v1/saude_mental/falls_mental_elder", tags=["saude_mental_idoso_avancado"])
router_flourishing_idoso = APIRouter(prefix="/api/v1/saude_mental/flourishing_idoso", tags=["saude_mental_idoso_avancado"])
router_ftd_elder = APIRouter(prefix="/api/v1/saude_mental/ftd_elder", tags=["saude_mental_idoso_avancado"])
router_generalized_anxiety_ = APIRouter(prefix="/api/v1/saude_mental/generalized_anxiety_elder", tags=["saude_mental_idoso_avancado"])
router_gerontopsicologia2 = APIRouter(prefix="/api/v1/saude_mental/gerontopsicologia2", tags=["saude_mental_idoso_avancado"])
router_gerotranscendencia = APIRouter(prefix="/api/v1/saude_mental/gerotranscendencia", tags=["saude_mental_idoso_avancado"])
router_good_death = APIRouter(prefix="/api/v1/saude_mental/good_death", tags=["saude_mental_idoso_avancado"])
router_home_care_mental = APIRouter(prefix="/api/v1/saude_mental/home_care_mental", tags=["saude_mental_idoso_avancado"])
router_identidade_envelheci = APIRouter(prefix="/api/v1/saude_mental/identidade_envelhecimento", tags=["saude_mental_idoso_avancado"])
router_insomnia_elder = APIRouter(prefix="/api/v1/saude_mental/insomnia_elder", tags=["saude_mental_idoso_avancado"])
router_integridade_ego = APIRouter(prefix="/api/v1/saude_mental/integridade_ego", tags=["saude_mental_idoso_avancado"])
router_late_life_spirituali = APIRouter(prefix="/api/v1/saude_mental/late_life_spirituality", tags=["saude_mental_idoso_avancado"])
router_late_onset_depressio = APIRouter(prefix="/api/v1/saude_mental/late_onset_depression", tags=["saude_mental_idoso_avancado"])
router_legado_idoso2 = APIRouter(prefix="/api/v1/saude_mental/legado_idoso2", tags=["saude_mental_idoso_avancado"])
router_life_review2 = APIRouter(prefix="/api/v1/saude_mental/life_review2", tags=["saude_mental_idoso_avancado"])
router_mci_elder = APIRouter(prefix="/api/v1/saude_mental/mci_elder", tags=["saude_mental_idoso_avancado"])
router_meaning_making_elder = APIRouter(prefix="/api/v1/saude_mental/meaning_making_elder", tags=["saude_mental_idoso_avancado"])
router_medication_adherence = APIRouter(prefix="/api/v1/saude_mental/medication_adherence_elde", tags=["saude_mental_idoso_avancado"])
router_medication_managemen = APIRouter(prefix="/api/v1/saude_mental/medication_management_eld", tags=["saude_mental_idoso_avancado"])
router_memory_care = APIRouter(prefix="/api/v1/saude_mental/memory_care", tags=["saude_mental_idoso_avancado"])
router_mixed_dementia = APIRouter(prefix="/api/v1/saude_mental/mixed_dementia", tags=["saude_mental_idoso_avancado"])
router_modelo_SOC = APIRouter(prefix="/api/v1/saude_mental/modelo_SOC", tags=["saude_mental_idoso_avancado"])
router_narrative_therapy_el = APIRouter(prefix="/api/v1/saude_mental/narrative_therapy_elder", tags=["saude_mental_idoso_avancado"])
router_neuropsychiatric_dem = APIRouter(prefix="/api/v1/saude_mental/neuropsychiatric_dementia", tags=["saude_mental_idoso_avancado"])
router_nursing_home_mental = APIRouter(prefix="/api/v1/saude_mental/nursing_home_mental", tags=["saude_mental_idoso_avancado"])
router_optimal_aging = APIRouter(prefix="/api/v1/saude_mental/optimal_aging", tags=["saude_mental_idoso_avancado"])
router_pain_dementia = APIRouter(prefix="/api/v1/saude_mental/pain_dementia", tags=["saude_mental_idoso_avancado"])
router_panic_elder = APIRouter(prefix="/api/v1/saude_mental/panic_elder", tags=["saude_mental_idoso_avancado"])
router_phobia_elder = APIRouter(prefix="/api/v1/saude_mental/phobia_elder", tags=["saude_mental_idoso_avancado"])
router_polypharmacy_elder = APIRouter(prefix="/api/v1/saude_mental/polypharmacy_elder", tags=["saude_mental_idoso_avancado"])
router_positive_aging2 = APIRouter(prefix="/api/v1/saude_mental/positive_aging2", tags=["saude_mental_idoso_avancado"])
router_preparation_death2 = APIRouter(prefix="/api/v1/saude_mental/preparation_death2", tags=["saude_mental_idoso_avancado"])
router_prescription_drug_el = APIRouter(prefix="/api/v1/saude_mental/prescription_drug_elder", tags=["saude_mental_idoso_avancado"])
router_productive_aging = APIRouter(prefix="/api/v1/saude_mental/productive_aging", tags=["saude_mental_idoso_avancado"])
router_pseudodementia = APIRouter(prefix="/api/v1/saude_mental/pseudodementia", tags=["saude_mental_idoso_avancado"])
router_psicologia_envelheci = APIRouter(prefix="/api/v1/saude_mental/psicologia_envelhecimento", tags=["saude_mental_idoso_avancado"])
router_psychosis_dementia = APIRouter(prefix="/api/v1/saude_mental/psychosis_dementia", tags=["saude_mental_idoso_avancado"])
router_religious_coping_eld = APIRouter(prefix="/api/v1/saude_mental/religious_coping_elder", tags=["saude_mental_idoso_avancado"])
router_reminiscencia_terapi = APIRouter(prefix="/api/v1/saude_mental/reminiscencia_terapia2", tags=["saude_mental_idoso_avancado"])
router_resiliencia_idoso2 = APIRouter(prefix="/api/v1/saude_mental/resiliencia_idoso2", tags=["saude_mental_idoso_avancado"])
router_respite_care = APIRouter(prefix="/api/v1/saude_mental/respite_care", tags=["saude_mental_idoso_avancado"])
router_satisfacao_vida_idos = APIRouter(prefix="/api/v1/saude_mental/satisfacao_vida_idoso", tags=["saude_mental_idoso_avancado"])
router_selecao_otimizacao_c = APIRouter(prefix="/api/v1/saude_mental/selecao_otimizacao_compen", tags=["saude_mental_idoso_avancado"])
router_sexual_behavior_deme = APIRouter(prefix="/api/v1/saude_mental/sexual_behavior_dementia", tags=["saude_mental_idoso_avancado"])
router_sleep_apnea_elder = APIRouter(prefix="/api/v1/saude_mental/sleep_apnea_elder", tags=["saude_mental_idoso_avancado"])
router_sleep_dementia = APIRouter(prefix="/api/v1/saude_mental/sleep_dementia", tags=["saude_mental_idoso_avancado"])
router_sleep_disorder_elder = APIRouter(prefix="/api/v1/saude_mental/sleep_disorder_elder", tags=["saude_mental_idoso_avancado"])
router_spiritual_care_elder = APIRouter(prefix="/api/v1/saude_mental/spiritual_care_elder", tags=["saude_mental_idoso_avancado"])
router_substance_abuse_elde = APIRouter(prefix="/api/v1/saude_mental/substance_abuse_elder", tags=["saude_mental_idoso_avancado"])
router_successful_aging = APIRouter(prefix="/api/v1/saude_mental/successful_aging", tags=["saude_mental_idoso_avancado"])
router_transcendencia_idoso = APIRouter(prefix="/api/v1/saude_mental/transcendencia_idoso", tags=["saude_mental_idoso_avancado"])
router_vascular_dementia_el = APIRouter(prefix="/api/v1/saude_mental/vascular_dementia_elder", tags=["saude_mental_idoso_avancado"])
router_vascular_depression = APIRouter(prefix="/api/v1/saude_mental/vascular_depression", tags=["saude_mental_idoso_avancado"])
router_wandering = APIRouter(prefix="/api/v1/saude_mental/wandering", tags=["saude_mental_idoso_avancado"])
router_wisdom_old_age = APIRouter(prefix="/api/v1/saude_mental/wisdom_old_age", tags=["saude_mental_idoso_avancado"])

@router_PTSD_elder.get("")
async def i_PTSD_elder():
    return {"p":"saude_mental_id_PTSD_elder","s":"ativo","t":datetime.utcnow().isoformat()}
@router_adult_day_program.get("")
async def i_adult_day_program():
    return {"p":"saude_mental_id_adult_day_program","s":"ativo","t":datetime.utcnow().isoformat()}
@router_agitation_dementia2.get("")
async def i_agitation_dementia2():
    return {"p":"saude_mental_id_agitation_dementia2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_alcohol_elder.get("")
async def i_alcohol_elder():
    return {"p":"saude_mental_id_alcohol_elder","s":"ativo","t":datetime.utcnow().isoformat()}
@router_alzheimer_elder.get("")
async def i_alzheimer_elder():
    return {"p":"saude_mental_id_alzheimer_elder","s":"ativo","t":datetime.utcnow().isoformat()}
@router_anxiety_dementia2.get("")
async def i_anxiety_dementia2():
    return {"p":"saude_mental_id_anxiety_dementia2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_anxiety_elder2.get("")
async def i_anxiety_elder2():
    return {"p":"saude_mental_id_anxiety_elder2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_assisted_living_ment.get("")
async def i_assisted_living_ment():
    return {"p":"saude_mental_id_assisted_living_ment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autoeficacia_idoso.get("")
async def i_autoeficacia_idoso():
    return {"p":"saude_mental_id_autoeficacia_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autoestima_idoso2.get("")
async def i_autoestima_idoso2():
    return {"p":"saude_mental_id_autoestima_idoso2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_behavioral_dementia.get("")
async def i_behavioral_dementia():
    return {"p":"saude_mental_id_behavioral_dementia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bem_estar_idoso.get("")
async def i_bem_estar_idoso():
    return {"p":"saude_mental_id_bem_estar_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_caregiver_burden2.get("")
async def i_caregiver_burden2():
    return {"p":"saude_mental_id_caregiver_burden2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_caregiver_dementia.get("")
async def i_caregiver_dementia():
    return {"p":"saude_mental_id_caregiver_dementia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_caregiver_depression.get("")
async def i_caregiver_depression():
    return {"p":"saude_mental_id_caregiver_depression","s":"ativo","t":datetime.utcnow().isoformat()}
@router_caregiver_grief.get("")
async def i_caregiver_grief():
    return {"p":"saude_mental_id_caregiver_grief","s":"ativo","t":datetime.utcnow().isoformat()}
@router_caregiver_identity.get("")
async def i_caregiver_identity():
    return {"p":"saude_mental_id_caregiver_identity","s":"ativo","t":datetime.utcnow().isoformat()}
@router_caregiver_support2.get("")
async def i_caregiver_support2():
    return {"p":"saude_mental_id_caregiver_support2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_chronic_pain_elder2.get("")
async def i_chronic_pain_elder2():
    return {"p":"saude_mental_id_chronic_pain_elder2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_circadian_elder.get("")
async def i_circadian_elder():
    return {"p":"saude_mental_id_circadian_elder","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cognitive_assessment.get("")
async def i_cognitive_assessment():
    return {"p":"saude_mental_id_cognitive_assessment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_compassionate_care_e.get("")
async def i_compassionate_care_e():
    return {"p":"saude_mental_id_compassionate_care_e","s":"ativo","t":datetime.utcnow().isoformat()}
@router_controle_percebido_i.get("")
async def i_controle_percebido_i():
    return {"p":"saude_mental_id_controle_percebido_i","s":"ativo","t":datetime.utcnow().isoformat()}
@router_daytime_sleepiness_e.get("")
async def i_daytime_sleepiness_e():
    return {"p":"saude_mental_id_daytime_sleepiness_e","s":"ativo","t":datetime.utcnow().isoformat()}
@router_death_acceptance.get("")
async def i_death_acceptance():
    return {"p":"saude_mental_id_death_acceptance","s":"ativo","t":datetime.utcnow().isoformat()}
@router_death_anxiety_elder.get("")
async def i_death_anxiety_elder():
    return {"p":"saude_mental_id_death_anxiety_elder","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dementia_elder2.get("")
async def i_dementia_elder2():
    return {"p":"saude_mental_id_dementia_elder2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_depression_dementia2.get("")
async def i_depression_dementia2():
    return {"p":"saude_mental_id_depression_dementia2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_depression_elder2.get("")
async def i_depression_elder2():
    return {"p":"saude_mental_id_depression_elder2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dignified_dying.get("")
async def i_dignified_dying():
    return {"p":"saude_mental_id_dignified_dying","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dignity_therapy2.get("")
async def i_dignity_therapy2():
    return {"p":"saude_mental_id_dignity_therapy2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dlb_elder.get("")
async def i_dlb_elder():
    return {"p":"saude_mental_id_dlb_elder","s":"ativo","t":datetime.utcnow().isoformat()}
@router_eating_dementia.get("")
async def i_eating_dementia():
    return {"p":"saude_mental_id_eating_dementia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_envelhecimento_bem_s.get("")
async def i_envelhecimento_bem_s():
    return {"p":"saude_mental_id_envelhecimento_bem_s","s":"ativo","t":datetime.utcnow().isoformat()}
@router_envelhecimento_sauda.get("")
async def i_envelhecimento_sauda():
    return {"p":"saude_mental_id_envelhecimento_sauda","s":"ativo","t":datetime.utcnow().isoformat()}
@router_existential_death.get("")
async def i_existential_death():
    return {"p":"saude_mental_id_existential_death","s":"ativo","t":datetime.utcnow().isoformat()}
@router_existential_therapy_.get("")
async def i_existential_therapy_():
    return {"p":"saude_mental_id_existential_therapy_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_falls_mental_elder.get("")
async def i_falls_mental_elder():
    return {"p":"saude_mental_id_falls_mental_elder","s":"ativo","t":datetime.utcnow().isoformat()}
@router_flourishing_idoso.get("")
async def i_flourishing_idoso():
    return {"p":"saude_mental_id_flourishing_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ftd_elder.get("")
async def i_ftd_elder():
    return {"p":"saude_mental_id_ftd_elder","s":"ativo","t":datetime.utcnow().isoformat()}
@router_generalized_anxiety_.get("")
async def i_generalized_anxiety_():
    return {"p":"saude_mental_id_generalized_anxiety_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gerontopsicologia2.get("")
async def i_gerontopsicologia2():
    return {"p":"saude_mental_id_gerontopsicologia2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gerotranscendencia.get("")
async def i_gerotranscendencia():
    return {"p":"saude_mental_id_gerotranscendencia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_good_death.get("")
async def i_good_death():
    return {"p":"saude_mental_id_good_death","s":"ativo","t":datetime.utcnow().isoformat()}
@router_home_care_mental.get("")
async def i_home_care_mental():
    return {"p":"saude_mental_id_home_care_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_identidade_envelheci.get("")
async def i_identidade_envelheci():
    return {"p":"saude_mental_id_identidade_envelheci","s":"ativo","t":datetime.utcnow().isoformat()}
@router_insomnia_elder.get("")
async def i_insomnia_elder():
    return {"p":"saude_mental_id_insomnia_elder","s":"ativo","t":datetime.utcnow().isoformat()}
@router_integridade_ego.get("")
async def i_integridade_ego():
    return {"p":"saude_mental_id_integridade_ego","s":"ativo","t":datetime.utcnow().isoformat()}
@router_late_life_spirituali.get("")
async def i_late_life_spirituali():
    return {"p":"saude_mental_id_late_life_spirituali","s":"ativo","t":datetime.utcnow().isoformat()}
@router_late_onset_depressio.get("")
async def i_late_onset_depressio():
    return {"p":"saude_mental_id_late_onset_depressio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_legado_idoso2.get("")
async def i_legado_idoso2():
    return {"p":"saude_mental_id_legado_idoso2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_life_review2.get("")
async def i_life_review2():
    return {"p":"saude_mental_id_life_review2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mci_elder.get("")
async def i_mci_elder():
    return {"p":"saude_mental_id_mci_elder","s":"ativo","t":datetime.utcnow().isoformat()}
@router_meaning_making_elder.get("")
async def i_meaning_making_elder():
    return {"p":"saude_mental_id_meaning_making_elder","s":"ativo","t":datetime.utcnow().isoformat()}
@router_medication_adherence.get("")
async def i_medication_adherence():
    return {"p":"saude_mental_id_medication_adherence","s":"ativo","t":datetime.utcnow().isoformat()}
@router_medication_managemen.get("")
async def i_medication_managemen():
    return {"p":"saude_mental_id_medication_managemen","s":"ativo","t":datetime.utcnow().isoformat()}
@router_memory_care.get("")
async def i_memory_care():
    return {"p":"saude_mental_id_memory_care","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mixed_dementia.get("")
async def i_mixed_dementia():
    return {"p":"saude_mental_id_mixed_dementia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_modelo_SOC.get("")
async def i_modelo_SOC():
    return {"p":"saude_mental_id_modelo_SOC","s":"ativo","t":datetime.utcnow().isoformat()}
@router_narrative_therapy_el.get("")
async def i_narrative_therapy_el():
    return {"p":"saude_mental_id_narrative_therapy_el","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neuropsychiatric_dem.get("")
async def i_neuropsychiatric_dem():
    return {"p":"saude_mental_id_neuropsychiatric_dem","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nursing_home_mental.get("")
async def i_nursing_home_mental():
    return {"p":"saude_mental_id_nursing_home_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_optimal_aging.get("")
async def i_optimal_aging():
    return {"p":"saude_mental_id_optimal_aging","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pain_dementia.get("")
async def i_pain_dementia():
    return {"p":"saude_mental_id_pain_dementia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_panic_elder.get("")
async def i_panic_elder():
    return {"p":"saude_mental_id_panic_elder","s":"ativo","t":datetime.utcnow().isoformat()}
@router_phobia_elder.get("")
async def i_phobia_elder():
    return {"p":"saude_mental_id_phobia_elder","s":"ativo","t":datetime.utcnow().isoformat()}
@router_polypharmacy_elder.get("")
async def i_polypharmacy_elder():
    return {"p":"saude_mental_id_polypharmacy_elder","s":"ativo","t":datetime.utcnow().isoformat()}
@router_positive_aging2.get("")
async def i_positive_aging2():
    return {"p":"saude_mental_id_positive_aging2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_preparation_death2.get("")
async def i_preparation_death2():
    return {"p":"saude_mental_id_preparation_death2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_prescription_drug_el.get("")
async def i_prescription_drug_el():
    return {"p":"saude_mental_id_prescription_drug_el","s":"ativo","t":datetime.utcnow().isoformat()}
@router_productive_aging.get("")
async def i_productive_aging():
    return {"p":"saude_mental_id_productive_aging","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pseudodementia.get("")
async def i_pseudodementia():
    return {"p":"saude_mental_id_pseudodementia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicologia_envelheci.get("")
async def i_psicologia_envelheci():
    return {"p":"saude_mental_id_psicologia_envelheci","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psychosis_dementia.get("")
async def i_psychosis_dementia():
    return {"p":"saude_mental_id_psychosis_dementia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_religious_coping_eld.get("")
async def i_religious_coping_eld():
    return {"p":"saude_mental_id_religious_coping_eld","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reminiscencia_terapi.get("")
async def i_reminiscencia_terapi():
    return {"p":"saude_mental_id_reminiscencia_terapi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_resiliencia_idoso2.get("")
async def i_resiliencia_idoso2():
    return {"p":"saude_mental_id_resiliencia_idoso2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_respite_care.get("")
async def i_respite_care():
    return {"p":"saude_mental_id_respite_care","s":"ativo","t":datetime.utcnow().isoformat()}
@router_satisfacao_vida_idos.get("")
async def i_satisfacao_vida_idos():
    return {"p":"saude_mental_id_satisfacao_vida_idos","s":"ativo","t":datetime.utcnow().isoformat()}
@router_selecao_otimizacao_c.get("")
async def i_selecao_otimizacao_c():
    return {"p":"saude_mental_id_selecao_otimizacao_c","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sexual_behavior_deme.get("")
async def i_sexual_behavior_deme():
    return {"p":"saude_mental_id_sexual_behavior_deme","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sleep_apnea_elder.get("")
async def i_sleep_apnea_elder():
    return {"p":"saude_mental_id_sleep_apnea_elder","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sleep_dementia.get("")
async def i_sleep_dementia():
    return {"p":"saude_mental_id_sleep_dementia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sleep_disorder_elder.get("")
async def i_sleep_disorder_elder():
    return {"p":"saude_mental_id_sleep_disorder_elder","s":"ativo","t":datetime.utcnow().isoformat()}
@router_spiritual_care_elder.get("")
async def i_spiritual_care_elder():
    return {"p":"saude_mental_id_spiritual_care_elder","s":"ativo","t":datetime.utcnow().isoformat()}
@router_substance_abuse_elde.get("")
async def i_substance_abuse_elde():
    return {"p":"saude_mental_id_substance_abuse_elde","s":"ativo","t":datetime.utcnow().isoformat()}
@router_successful_aging.get("")
async def i_successful_aging():
    return {"p":"saude_mental_id_successful_aging","s":"ativo","t":datetime.utcnow().isoformat()}
@router_transcendencia_idoso.get("")
async def i_transcendencia_idoso():
    return {"p":"saude_mental_id_transcendencia_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_vascular_dementia_el.get("")
async def i_vascular_dementia_el():
    return {"p":"saude_mental_id_vascular_dementia_el","s":"ativo","t":datetime.utcnow().isoformat()}
@router_vascular_depression.get("")
async def i_vascular_depression():
    return {"p":"saude_mental_id_vascular_depression","s":"ativo","t":datetime.utcnow().isoformat()}
@router_wandering.get("")
async def i_wandering():
    return {"p":"saude_mental_id_wandering","s":"ativo","t":datetime.utcnow().isoformat()}
@router_wisdom_old_age.get("")
async def i_wisdom_old_age():
    return {"p":"saude_mental_id_wisdom_old_age","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_saude_mental_idoso_a(PluginBase):
    name = "consolidated_saude_mental_idoso_avancado"
    def setup(self, app):
        app.include_router(router_PTSD_elder)
        app.include_router(router_adult_day_program)
        app.include_router(router_agitation_dementia2)
        app.include_router(router_alcohol_elder)
        app.include_router(router_alzheimer_elder)
        app.include_router(router_anxiety_dementia2)
        app.include_router(router_anxiety_elder2)
        app.include_router(router_assisted_living_ment)
        app.include_router(router_autoeficacia_idoso)
        app.include_router(router_autoestima_idoso2)
        app.include_router(router_behavioral_dementia)
        app.include_router(router_bem_estar_idoso)
        app.include_router(router_caregiver_burden2)
        app.include_router(router_caregiver_dementia)
        app.include_router(router_caregiver_depression)
        app.include_router(router_caregiver_grief)
        app.include_router(router_caregiver_identity)
        app.include_router(router_caregiver_support2)
        app.include_router(router_chronic_pain_elder2)
        app.include_router(router_circadian_elder)
        app.include_router(router_cognitive_assessment)
        app.include_router(router_compassionate_care_e)
        app.include_router(router_controle_percebido_i)
        app.include_router(router_daytime_sleepiness_e)
        app.include_router(router_death_acceptance)
        app.include_router(router_death_anxiety_elder)
        app.include_router(router_dementia_elder2)
        app.include_router(router_depression_dementia2)
        app.include_router(router_depression_elder2)
        app.include_router(router_dignified_dying)
        app.include_router(router_dignity_therapy2)
        app.include_router(router_dlb_elder)
        app.include_router(router_eating_dementia)
        app.include_router(router_envelhecimento_bem_s)
        app.include_router(router_envelhecimento_sauda)
        app.include_router(router_existential_death)
        app.include_router(router_existential_therapy_)
        app.include_router(router_falls_mental_elder)
        app.include_router(router_flourishing_idoso)
        app.include_router(router_ftd_elder)
        app.include_router(router_generalized_anxiety_)
        app.include_router(router_gerontopsicologia2)
        app.include_router(router_gerotranscendencia)
        app.include_router(router_good_death)
        app.include_router(router_home_care_mental)
        app.include_router(router_identidade_envelheci)
        app.include_router(router_insomnia_elder)
        app.include_router(router_integridade_ego)
        app.include_router(router_late_life_spirituali)
        app.include_router(router_late_onset_depressio)
        app.include_router(router_legado_idoso2)
        app.include_router(router_life_review2)
        app.include_router(router_mci_elder)
        app.include_router(router_meaning_making_elder)
        app.include_router(router_medication_adherence)
        app.include_router(router_medication_managemen)
        app.include_router(router_memory_care)
        app.include_router(router_mixed_dementia)
        app.include_router(router_modelo_SOC)
        app.include_router(router_narrative_therapy_el)
        app.include_router(router_neuropsychiatric_dem)
        app.include_router(router_nursing_home_mental)
        app.include_router(router_optimal_aging)
        app.include_router(router_pain_dementia)
        app.include_router(router_panic_elder)
        app.include_router(router_phobia_elder)
        app.include_router(router_polypharmacy_elder)
        app.include_router(router_positive_aging2)
        app.include_router(router_preparation_death2)
        app.include_router(router_prescription_drug_el)
        app.include_router(router_productive_aging)
        app.include_router(router_pseudodementia)
        app.include_router(router_psicologia_envelheci)
        app.include_router(router_psychosis_dementia)
        app.include_router(router_religious_coping_eld)
        app.include_router(router_reminiscencia_terapi)
        app.include_router(router_resiliencia_idoso2)
        app.include_router(router_respite_care)
        app.include_router(router_satisfacao_vida_idos)
        app.include_router(router_selecao_otimizacao_c)
        app.include_router(router_sexual_behavior_deme)
        app.include_router(router_sleep_apnea_elder)
        app.include_router(router_sleep_dementia)
        app.include_router(router_sleep_disorder_elder)
        app.include_router(router_spiritual_care_elder)
        app.include_router(router_substance_abuse_elde)
        app.include_router(router_successful_aging)
        app.include_router(router_transcendencia_idoso)
        app.include_router(router_vascular_dementia_el)
        app.include_router(router_vascular_depression)
        app.include_router(router_wandering)
        app.include_router(router_wisdom_old_age)


plugin = Plugin_saude_mental_idoso_a()
