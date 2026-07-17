from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_4_7_8_avancado = APIRouter(prefix="/api/v1/terapias_cor/4_7_8_avancado", tags=["terapias_corpo_mente"])
router_EMDR_lite = APIRouter(prefix="/api/v1/terapias_cor/EMDR_lite", tags=["terapias_corpo_mente"])
router_Resource_installatio = APIRouter(prefix="/api/v1/terapias_cor/Resource_installation", tags=["terapias_corpo_mente"])
router_alternate_nostril = APIRouter(prefix="/api/v1/terapias_cor/alternate_nostril", tags=["terapias_corpo_mente"])
router_applied_relaxation = APIRouter(prefix="/api/v1/terapias_cor/applied_relaxation", tags=["terapias_corpo_mente"])
router_autogenic_discharge = APIRouter(prefix="/api/v1/terapias_cor/autogenic_discharge", tags=["terapias_corpo_mente"])
router_autogenic_meditative = APIRouter(prefix="/api/v1/terapias_cor/autogenic_meditative", tags=["terapias_corpo_mente"])
router_autogenic_standard = APIRouter(prefix="/api/v1/terapias_cor/autogenic_standard", tags=["terapias_corpo_mente"])
router_autogenic_training = APIRouter(prefix="/api/v1/terapias_cor/autogenic_training", tags=["terapias_corpo_mente"])
router_benson_technique = APIRouter(prefix="/api/v1/terapias_cor/benson_technique", tags=["terapias_corpo_mente"])
router_bhramari_bee = APIRouter(prefix="/api/v1/terapias_cor/bhramari_bee", tags=["terapias_corpo_mente"])
router_biofeedback_eda2 = APIRouter(prefix="/api/v1/terapias_cor/biofeedback_eda2", tags=["terapias_corpo_mente"])
router_biofeedback_eeg2 = APIRouter(prefix="/api/v1/terapias_cor/biofeedback_eeg2", tags=["terapias_corpo_mente"])
router_biofeedback_emg = APIRouter(prefix="/api/v1/terapias_cor/biofeedback_emg", tags=["terapias_corpo_mente"])
router_biofeedback_hrv2 = APIRouter(prefix="/api/v1/terapias_cor/biofeedback_hrv2", tags=["terapias_corpo_mente"])
router_body_awareness_train = APIRouter(prefix="/api/v1/terapias_cor/body_awareness_training", tags=["terapias_corpo_mente"])
router_body_scan_mbsr = APIRouter(prefix="/api/v1/terapias_cor/body_scan_mbsr", tags=["terapias_corpo_mente"])
router_box_breathing2 = APIRouter(prefix="/api/v1/terapias_cor/box_breathing2", tags=["terapias_corpo_mente"])
router_breath_somatic = APIRouter(prefix="/api/v1/terapias_cor/breath_somatic", tags=["terapias_corpo_mente"])
router_butterfly_hug = APIRouter(prefix="/api/v1/terapias_cor/butterfly_hug", tags=["terapias_corpo_mente"])
router_chandra_bhedana = APIRouter(prefix="/api/v1/terapias_cor/chandra_bhedana", tags=["terapias_corpo_mente"])
router_co_regulation = APIRouter(prefix="/api/v1/terapias_cor/co_regulation", tags=["terapias_corpo_mente"])
router_cognitive_interweave = APIRouter(prefix="/api/v1/terapias_cor/cognitive_interweave", tags=["terapias_corpo_mente"])
router_coherent_breathing = APIRouter(prefix="/api/v1/terapias_cor/coherent_breathing", tags=["terapias_corpo_mente"])
router_cold_shower_protocol = APIRouter(prefix="/api/v1/terapias_cor/cold_shower_protocol", tags=["terapias_corpo_mente"])
router_cold_water_immersion = APIRouter(prefix="/api/v1/terapias_cor/cold_water_immersion", tags=["terapias_corpo_mente"])
router_completion_somatic = APIRouter(prefix="/api/v1/terapias_cor/completion_somatic", tags=["terapias_corpo_mente"])
router_containment_therapy = APIRouter(prefix="/api/v1/terapias_cor/containment_therapy", tags=["terapias_corpo_mente"])
router_contrast_therapy = APIRouter(prefix="/api/v1/terapias_cor/contrast_therapy", tags=["terapias_corpo_mente"])
router_cryotherapy2 = APIRouter(prefix="/api/v1/terapias_cor/cryotherapy2", tags=["terapias_corpo_mente"])
router_discharge_somatic = APIRouter(prefix="/api/v1/terapias_cor/discharge_somatic", tags=["terapias_corpo_mente"])
router_dorsal_vagal_regulat = APIRouter(prefix="/api/v1/terapias_cor/dorsal_vagal_regulation", tags=["terapias_corpo_mente"])
router_dual_attention_stimu = APIRouter(prefix="/api/v1/terapias_cor/dual_attention_stimulus", tags=["terapias_corpo_mente"])
router_eye_contact_therapy = APIRouter(prefix="/api/v1/terapias_cor/eye_contact_therapy", tags=["terapias_corpo_mente"])
router_eye_movement_desensi = APIRouter(prefix="/api/v1/terapias_cor/eye_movement_desensit", tags=["terapias_corpo_mente"])
router_facial_muscles_regul = APIRouter(prefix="/api/v1/terapias_cor/facial_muscles_regulation", tags=["terapias_corpo_mente"])
router_felt_sense = APIRouter(prefix="/api/v1/terapias_cor/felt_sense", tags=["terapias_corpo_mente"])
router_float_anxiety = APIRouter(prefix="/api/v1/terapias_cor/float_anxiety", tags=["terapias_corpo_mente"])
router_float_rest_tank = APIRouter(prefix="/api/v1/terapias_cor/float_rest_tank", tags=["terapias_corpo_mente"])
router_flotation_therapy = APIRouter(prefix="/api/v1/terapias_cor/flotation_therapy", tags=["terapias_corpo_mente"])
router_future_template = APIRouter(prefix="/api/v1/terapias_cor/future_template", tags=["terapias_corpo_mente"])
router_grounding_somatic = APIRouter(prefix="/api/v1/terapias_cor/grounding_somatic", tags=["terapias_corpo_mente"])
router_heart_brain_coherenc = APIRouter(prefix="/api/v1/terapias_cor/heart_brain_coherence", tags=["terapias_corpo_mente"])
router_heartmath_technique = APIRouter(prefix="/api/v1/terapias_cor/heartmath_technique", tags=["terapias_corpo_mente"])
router_heat_therapy = APIRouter(prefix="/api/v1/terapias_cor/heat_therapy", tags=["terapias_corpo_mente"])
router_hrv_training = APIRouter(prefix="/api/v1/terapias_cor/hrv_training", tags=["terapias_corpo_mente"])
router_hydrotherapy = APIRouter(prefix="/api/v1/terapias_cor/hydrotherapy", tags=["terapias_corpo_mente"])
router_interoceptive_awaren = APIRouter(prefix="/api/v1/terapias_cor/interoceptive_awareness", tags=["terapias_corpo_mente"])
router_kapalabhati = APIRouter(prefix="/api/v1/terapias_cor/kapalabhati", tags=["terapias_corpo_mente"])
router_kumbhaka_retention = APIRouter(prefix="/api/v1/terapias_cor/kumbhaka_retention", tags=["terapias_corpo_mente"])
router_middle_ear_muscles = APIRouter(prefix="/api/v1/terapias_cor/middle_ear_muscles", tags=["terapias_corpo_mente"])
router_mindful_movement = APIRouter(prefix="/api/v1/terapias_cor/mindful_movement", tags=["terapias_corpo_mente"])
router_nadi_shodhana = APIRouter(prefix="/api/v1/terapias_cor/nadi_shodhana", tags=["terapias_corpo_mente"])
router_neuroception_safety = APIRouter(prefix="/api/v1/terapias_cor/neuroception_safety", tags=["terapias_corpo_mente"])
router_neurofeedback_alpha = APIRouter(prefix="/api/v1/terapias_cor/neurofeedback_alpha", tags=["terapias_corpo_mente"])
router_neurofeedback_beta = APIRouter(prefix="/api/v1/terapias_cor/neurofeedback_beta", tags=["terapias_corpo_mente"])
router_neurofeedback_connec = APIRouter(prefix="/api/v1/terapias_cor/neurofeedback_connectivit", tags=["terapias_corpo_mente"])
router_neurofeedback_delta = APIRouter(prefix="/api/v1/terapias_cor/neurofeedback_delta", tags=["terapias_corpo_mente"])
router_neurofeedback_gamma = APIRouter(prefix="/api/v1/terapias_cor/neurofeedback_gamma", tags=["terapias_corpo_mente"])
router_neurofeedback_infra_ = APIRouter(prefix="/api/v1/terapias_cor/neurofeedback_infra_low", tags=["terapias_corpo_mente"])
router_neurofeedback_smr = APIRouter(prefix="/api/v1/terapias_cor/neurofeedback_smr", tags=["terapias_corpo_mente"])
router_neurofeedback_theta = APIRouter(prefix="/api/v1/terapias_cor/neurofeedback_theta", tags=["terapias_corpo_mente"])
router_orientation_somatic = APIRouter(prefix="/api/v1/terapias_cor/orientation_somatic", tags=["terapias_corpo_mente"])
router_passive_concentratio = APIRouter(prefix="/api/v1/terapias_cor/passive_concentration", tags=["terapias_corpo_mente"])
router_pendulation = APIRouter(prefix="/api/v1/terapias_cor/pendulation", tags=["terapias_corpo_mente"])
router_polyvagal_exercises = APIRouter(prefix="/api/v1/terapias_cor/polyvagal_exercises", tags=["terapias_corpo_mente"])
router_progressive_relaxati = APIRouter(prefix="/api/v1/terapias_cor/progressive_relaxation2", tags=["terapias_corpo_mente"])
router_relaxation_response = APIRouter(prefix="/api/v1/terapias_cor/relaxation_response", tags=["terapias_corpo_mente"])
router_resonant_frequency = APIRouter(prefix="/api/v1/terapias_cor/resonant_frequency", tags=["terapias_corpo_mente"])
router_resourcing_somatic = APIRouter(prefix="/api/v1/terapias_cor/resourcing_somatic", tags=["terapias_corpo_mente"])
router_rhythmic_movement = APIRouter(prefix="/api/v1/terapias_cor/rhythmic_movement", tags=["terapias_corpo_mente"])
router_rocking_soothing = APIRouter(prefix="/api/v1/terapias_cor/rocking_soothing", tags=["terapias_corpo_mente"])
router_sauna_protocol = APIRouter(prefix="/api/v1/terapias_cor/sauna_protocol", tags=["terapias_corpo_mente"])
router_self_regulation_body = APIRouter(prefix="/api/v1/terapias_cor/self_regulation_body", tags=["terapias_corpo_mente"])
router_sensorimotor_rhythm = APIRouter(prefix="/api/v1/terapias_cor/sensorimotor_rhythm", tags=["terapias_corpo_mente"])
router_sensory_deprivation = APIRouter(prefix="/api/v1/terapias_cor/sensory_deprivation", tags=["terapias_corpo_mente"])
router_settling_somatic = APIRouter(prefix="/api/v1/terapias_cor/settling_somatic", tags=["terapias_corpo_mente"])
router_sitali_cooling = APIRouter(prefix="/api/v1/terapias_cor/sitali_cooling", tags=["terapias_corpo_mente"])
router_slow_breathing_train = APIRouter(prefix="/api/v1/terapias_cor/slow_breathing_training", tags=["terapias_corpo_mente"])
router_social_engagement_sy = APIRouter(prefix="/api/v1/terapias_cor/social_engagement_system", tags=["terapias_corpo_mente"])
router_somatic_tracking = APIRouter(prefix="/api/v1/terapias_cor/somatic_tracking", tags=["terapias_corpo_mente"])
router_steam_therapy = APIRouter(prefix="/api/v1/terapias_cor/steam_therapy", tags=["terapias_corpo_mente"])
router_surya_bhedana = APIRouter(prefix="/api/v1/terapias_cor/surya_bhedana", tags=["terapias_corpo_mente"])
router_sympathetic_downregu = APIRouter(prefix="/api/v1/terapias_cor/sympathetic_downregulatio", tags=["terapias_corpo_mente"])
router_tapping_sequences = APIRouter(prefix="/api/v1/terapias_cor/tapping_sequences", tags=["terapias_corpo_mente"])
router_therapeutic_holding = APIRouter(prefix="/api/v1/terapias_cor/therapeutic_holding", tags=["terapias_corpo_mente"])
router_titration_somatic = APIRouter(prefix="/api/v1/terapias_cor/titration_somatic", tags=["terapias_corpo_mente"])
router_touch_therapy_clinic = APIRouter(prefix="/api/v1/terapias_cor/touch_therapy_clinical", tags=["terapias_corpo_mente"])
router_ujjayi_ocean = APIRouter(prefix="/api/v1/terapias_cor/ujjayi_ocean", tags=["terapias_corpo_mente"])
router_ventral_vagal_activa = APIRouter(prefix="/api/v1/terapias_cor/ventral_vagal_activation", tags=["terapias_corpo_mente"])
router_voice_prosody_therap = APIRouter(prefix="/api/v1/terapias_cor/voice_prosody_therapy", tags=["terapias_corpo_mente"])
router_wim_hof_avancado = APIRouter(prefix="/api/v1/terapias_cor/wim_hof_avancado", tags=["terapias_corpo_mente"])
router_yoga_nidra = APIRouter(prefix="/api/v1/terapias_cor/yoga_nidra", tags=["terapias_corpo_mente"])
router_yoga_nidra_resolutio = APIRouter(prefix="/api/v1/terapias_cor/yoga_nidra_resolution", tags=["terapias_corpo_mente"])
router_yoga_nidra_rotation = APIRouter(prefix="/api/v1/terapias_cor/yoga_nidra_rotation", tags=["terapias_corpo_mente"])
router_yoga_nidra_visualiza = APIRouter(prefix="/api/v1/terapias_cor/yoga_nidra_visualization", tags=["terapias_corpo_mente"])

@router_4_7_8_avancado.get("")
async def i_4_7_8_avancado():
    return {"p":"terapias_corpo__4_7_8_avancado","s":"ativo","t":datetime.utcnow().isoformat()}
@router_EMDR_lite.get("")
async def i_EMDR_lite():
    return {"p":"terapias_corpo__EMDR_lite","s":"ativo","t":datetime.utcnow().isoformat()}
@router_Resource_installatio.get("")
async def i_Resource_installatio():
    return {"p":"terapias_corpo__Resource_installatio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_alternate_nostril.get("")
async def i_alternate_nostril():
    return {"p":"terapias_corpo__alternate_nostril","s":"ativo","t":datetime.utcnow().isoformat()}
@router_applied_relaxation.get("")
async def i_applied_relaxation():
    return {"p":"terapias_corpo__applied_relaxation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autogenic_discharge.get("")
async def i_autogenic_discharge():
    return {"p":"terapias_corpo__autogenic_discharge","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autogenic_meditative.get("")
async def i_autogenic_meditative():
    return {"p":"terapias_corpo__autogenic_meditative","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autogenic_standard.get("")
async def i_autogenic_standard():
    return {"p":"terapias_corpo__autogenic_standard","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autogenic_training.get("")
async def i_autogenic_training():
    return {"p":"terapias_corpo__autogenic_training","s":"ativo","t":datetime.utcnow().isoformat()}
@router_benson_technique.get("")
async def i_benson_technique():
    return {"p":"terapias_corpo__benson_technique","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bhramari_bee.get("")
async def i_bhramari_bee():
    return {"p":"terapias_corpo__bhramari_bee","s":"ativo","t":datetime.utcnow().isoformat()}
@router_biofeedback_eda2.get("")
async def i_biofeedback_eda2():
    return {"p":"terapias_corpo__biofeedback_eda2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_biofeedback_eeg2.get("")
async def i_biofeedback_eeg2():
    return {"p":"terapias_corpo__biofeedback_eeg2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_biofeedback_emg.get("")
async def i_biofeedback_emg():
    return {"p":"terapias_corpo__biofeedback_emg","s":"ativo","t":datetime.utcnow().isoformat()}
@router_biofeedback_hrv2.get("")
async def i_biofeedback_hrv2():
    return {"p":"terapias_corpo__biofeedback_hrv2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_body_awareness_train.get("")
async def i_body_awareness_train():
    return {"p":"terapias_corpo__body_awareness_train","s":"ativo","t":datetime.utcnow().isoformat()}
@router_body_scan_mbsr.get("")
async def i_body_scan_mbsr():
    return {"p":"terapias_corpo__body_scan_mbsr","s":"ativo","t":datetime.utcnow().isoformat()}
@router_box_breathing2.get("")
async def i_box_breathing2():
    return {"p":"terapias_corpo__box_breathing2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_breath_somatic.get("")
async def i_breath_somatic():
    return {"p":"terapias_corpo__breath_somatic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_butterfly_hug.get("")
async def i_butterfly_hug():
    return {"p":"terapias_corpo__butterfly_hug","s":"ativo","t":datetime.utcnow().isoformat()}
@router_chandra_bhedana.get("")
async def i_chandra_bhedana():
    return {"p":"terapias_corpo__chandra_bhedana","s":"ativo","t":datetime.utcnow().isoformat()}
@router_co_regulation.get("")
async def i_co_regulation():
    return {"p":"terapias_corpo__co_regulation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cognitive_interweave.get("")
async def i_cognitive_interweave():
    return {"p":"terapias_corpo__cognitive_interweave","s":"ativo","t":datetime.utcnow().isoformat()}
@router_coherent_breathing.get("")
async def i_coherent_breathing():
    return {"p":"terapias_corpo__coherent_breathing","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cold_shower_protocol.get("")
async def i_cold_shower_protocol():
    return {"p":"terapias_corpo__cold_shower_protocol","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cold_water_immersion.get("")
async def i_cold_water_immersion():
    return {"p":"terapias_corpo__cold_water_immersion","s":"ativo","t":datetime.utcnow().isoformat()}
@router_completion_somatic.get("")
async def i_completion_somatic():
    return {"p":"terapias_corpo__completion_somatic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_containment_therapy.get("")
async def i_containment_therapy():
    return {"p":"terapias_corpo__containment_therapy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_contrast_therapy.get("")
async def i_contrast_therapy():
    return {"p":"terapias_corpo__contrast_therapy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cryotherapy2.get("")
async def i_cryotherapy2():
    return {"p":"terapias_corpo__cryotherapy2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_discharge_somatic.get("")
async def i_discharge_somatic():
    return {"p":"terapias_corpo__discharge_somatic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dorsal_vagal_regulat.get("")
async def i_dorsal_vagal_regulat():
    return {"p":"terapias_corpo__dorsal_vagal_regulat","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dual_attention_stimu.get("")
async def i_dual_attention_stimu():
    return {"p":"terapias_corpo__dual_attention_stimu","s":"ativo","t":datetime.utcnow().isoformat()}
@router_eye_contact_therapy.get("")
async def i_eye_contact_therapy():
    return {"p":"terapias_corpo__eye_contact_therapy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_eye_movement_desensi.get("")
async def i_eye_movement_desensi():
    return {"p":"terapias_corpo__eye_movement_desensi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_facial_muscles_regul.get("")
async def i_facial_muscles_regul():
    return {"p":"terapias_corpo__facial_muscles_regul","s":"ativo","t":datetime.utcnow().isoformat()}
@router_felt_sense.get("")
async def i_felt_sense():
    return {"p":"terapias_corpo__felt_sense","s":"ativo","t":datetime.utcnow().isoformat()}
@router_float_anxiety.get("")
async def i_float_anxiety():
    return {"p":"terapias_corpo__float_anxiety","s":"ativo","t":datetime.utcnow().isoformat()}
@router_float_rest_tank.get("")
async def i_float_rest_tank():
    return {"p":"terapias_corpo__float_rest_tank","s":"ativo","t":datetime.utcnow().isoformat()}
@router_flotation_therapy.get("")
async def i_flotation_therapy():
    return {"p":"terapias_corpo__flotation_therapy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_future_template.get("")
async def i_future_template():
    return {"p":"terapias_corpo__future_template","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grounding_somatic.get("")
async def i_grounding_somatic():
    return {"p":"terapias_corpo__grounding_somatic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_heart_brain_coherenc.get("")
async def i_heart_brain_coherenc():
    return {"p":"terapias_corpo__heart_brain_coherenc","s":"ativo","t":datetime.utcnow().isoformat()}
@router_heartmath_technique.get("")
async def i_heartmath_technique():
    return {"p":"terapias_corpo__heartmath_technique","s":"ativo","t":datetime.utcnow().isoformat()}
@router_heat_therapy.get("")
async def i_heat_therapy():
    return {"p":"terapias_corpo__heat_therapy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hrv_training.get("")
async def i_hrv_training():
    return {"p":"terapias_corpo__hrv_training","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hydrotherapy.get("")
async def i_hydrotherapy():
    return {"p":"terapias_corpo__hydrotherapy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_interoceptive_awaren.get("")
async def i_interoceptive_awaren():
    return {"p":"terapias_corpo__interoceptive_awaren","s":"ativo","t":datetime.utcnow().isoformat()}
@router_kapalabhati.get("")
async def i_kapalabhati():
    return {"p":"terapias_corpo__kapalabhati","s":"ativo","t":datetime.utcnow().isoformat()}
@router_kumbhaka_retention.get("")
async def i_kumbhaka_retention():
    return {"p":"terapias_corpo__kumbhaka_retention","s":"ativo","t":datetime.utcnow().isoformat()}
@router_middle_ear_muscles.get("")
async def i_middle_ear_muscles():
    return {"p":"terapias_corpo__middle_ear_muscles","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindful_movement.get("")
async def i_mindful_movement():
    return {"p":"terapias_corpo__mindful_movement","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nadi_shodhana.get("")
async def i_nadi_shodhana():
    return {"p":"terapias_corpo__nadi_shodhana","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neuroception_safety.get("")
async def i_neuroception_safety():
    return {"p":"terapias_corpo__neuroception_safety","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neurofeedback_alpha.get("")
async def i_neurofeedback_alpha():
    return {"p":"terapias_corpo__neurofeedback_alpha","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neurofeedback_beta.get("")
async def i_neurofeedback_beta():
    return {"p":"terapias_corpo__neurofeedback_beta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neurofeedback_connec.get("")
async def i_neurofeedback_connec():
    return {"p":"terapias_corpo__neurofeedback_connec","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neurofeedback_delta.get("")
async def i_neurofeedback_delta():
    return {"p":"terapias_corpo__neurofeedback_delta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neurofeedback_gamma.get("")
async def i_neurofeedback_gamma():
    return {"p":"terapias_corpo__neurofeedback_gamma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neurofeedback_infra_.get("")
async def i_neurofeedback_infra_():
    return {"p":"terapias_corpo__neurofeedback_infra_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neurofeedback_smr.get("")
async def i_neurofeedback_smr():
    return {"p":"terapias_corpo__neurofeedback_smr","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neurofeedback_theta.get("")
async def i_neurofeedback_theta():
    return {"p":"terapias_corpo__neurofeedback_theta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_orientation_somatic.get("")
async def i_orientation_somatic():
    return {"p":"terapias_corpo__orientation_somatic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_passive_concentratio.get("")
async def i_passive_concentratio():
    return {"p":"terapias_corpo__passive_concentratio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pendulation.get("")
async def i_pendulation():
    return {"p":"terapias_corpo__pendulation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_polyvagal_exercises.get("")
async def i_polyvagal_exercises():
    return {"p":"terapias_corpo__polyvagal_exercises","s":"ativo","t":datetime.utcnow().isoformat()}
@router_progressive_relaxati.get("")
async def i_progressive_relaxati():
    return {"p":"terapias_corpo__progressive_relaxati","s":"ativo","t":datetime.utcnow().isoformat()}
@router_relaxation_response.get("")
async def i_relaxation_response():
    return {"p":"terapias_corpo__relaxation_response","s":"ativo","t":datetime.utcnow().isoformat()}
@router_resonant_frequency.get("")
async def i_resonant_frequency():
    return {"p":"terapias_corpo__resonant_frequency","s":"ativo","t":datetime.utcnow().isoformat()}
@router_resourcing_somatic.get("")
async def i_resourcing_somatic():
    return {"p":"terapias_corpo__resourcing_somatic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_rhythmic_movement.get("")
async def i_rhythmic_movement():
    return {"p":"terapias_corpo__rhythmic_movement","s":"ativo","t":datetime.utcnow().isoformat()}
@router_rocking_soothing.get("")
async def i_rocking_soothing():
    return {"p":"terapias_corpo__rocking_soothing","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sauna_protocol.get("")
async def i_sauna_protocol():
    return {"p":"terapias_corpo__sauna_protocol","s":"ativo","t":datetime.utcnow().isoformat()}
@router_self_regulation_body.get("")
async def i_self_regulation_body():
    return {"p":"terapias_corpo__self_regulation_body","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sensorimotor_rhythm.get("")
async def i_sensorimotor_rhythm():
    return {"p":"terapias_corpo__sensorimotor_rhythm","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sensory_deprivation.get("")
async def i_sensory_deprivation():
    return {"p":"terapias_corpo__sensory_deprivation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_settling_somatic.get("")
async def i_settling_somatic():
    return {"p":"terapias_corpo__settling_somatic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sitali_cooling.get("")
async def i_sitali_cooling():
    return {"p":"terapias_corpo__sitali_cooling","s":"ativo","t":datetime.utcnow().isoformat()}
@router_slow_breathing_train.get("")
async def i_slow_breathing_train():
    return {"p":"terapias_corpo__slow_breathing_train","s":"ativo","t":datetime.utcnow().isoformat()}
@router_social_engagement_sy.get("")
async def i_social_engagement_sy():
    return {"p":"terapias_corpo__social_engagement_sy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_somatic_tracking.get("")
async def i_somatic_tracking():
    return {"p":"terapias_corpo__somatic_tracking","s":"ativo","t":datetime.utcnow().isoformat()}
@router_steam_therapy.get("")
async def i_steam_therapy():
    return {"p":"terapias_corpo__steam_therapy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_surya_bhedana.get("")
async def i_surya_bhedana():
    return {"p":"terapias_corpo__surya_bhedana","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sympathetic_downregu.get("")
async def i_sympathetic_downregu():
    return {"p":"terapias_corpo__sympathetic_downregu","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tapping_sequences.get("")
async def i_tapping_sequences():
    return {"p":"terapias_corpo__tapping_sequences","s":"ativo","t":datetime.utcnow().isoformat()}
@router_therapeutic_holding.get("")
async def i_therapeutic_holding():
    return {"p":"terapias_corpo__therapeutic_holding","s":"ativo","t":datetime.utcnow().isoformat()}
@router_titration_somatic.get("")
async def i_titration_somatic():
    return {"p":"terapias_corpo__titration_somatic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_touch_therapy_clinic.get("")
async def i_touch_therapy_clinic():
    return {"p":"terapias_corpo__touch_therapy_clinic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ujjayi_ocean.get("")
async def i_ujjayi_ocean():
    return {"p":"terapias_corpo__ujjayi_ocean","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ventral_vagal_activa.get("")
async def i_ventral_vagal_activa():
    return {"p":"terapias_corpo__ventral_vagal_activa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_voice_prosody_therap.get("")
async def i_voice_prosody_therap():
    return {"p":"terapias_corpo__voice_prosody_therap","s":"ativo","t":datetime.utcnow().isoformat()}
@router_wim_hof_avancado.get("")
async def i_wim_hof_avancado():
    return {"p":"terapias_corpo__wim_hof_avancado","s":"ativo","t":datetime.utcnow().isoformat()}
@router_yoga_nidra.get("")
async def i_yoga_nidra():
    return {"p":"terapias_corpo__yoga_nidra","s":"ativo","t":datetime.utcnow().isoformat()}
@router_yoga_nidra_resolutio.get("")
async def i_yoga_nidra_resolutio():
    return {"p":"terapias_corpo__yoga_nidra_resolutio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_yoga_nidra_rotation.get("")
async def i_yoga_nidra_rotation():
    return {"p":"terapias_corpo__yoga_nidra_rotation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_yoga_nidra_visualiza.get("")
async def i_yoga_nidra_visualiza():
    return {"p":"terapias_corpo__yoga_nidra_visualiza","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_terapias_corpo_mente(PluginBase):
    name = "consolidated_terapias_corpo_mente"
    def setup(self, app):
        app.include_router(router_4_7_8_avancado)
        app.include_router(router_EMDR_lite)
        app.include_router(router_Resource_installatio)
        app.include_router(router_alternate_nostril)
        app.include_router(router_applied_relaxation)
        app.include_router(router_autogenic_discharge)
        app.include_router(router_autogenic_meditative)
        app.include_router(router_autogenic_standard)
        app.include_router(router_autogenic_training)
        app.include_router(router_benson_technique)
        app.include_router(router_bhramari_bee)
        app.include_router(router_biofeedback_eda2)
        app.include_router(router_biofeedback_eeg2)
        app.include_router(router_biofeedback_emg)
        app.include_router(router_biofeedback_hrv2)
        app.include_router(router_body_awareness_train)
        app.include_router(router_body_scan_mbsr)
        app.include_router(router_box_breathing2)
        app.include_router(router_breath_somatic)
        app.include_router(router_butterfly_hug)
        app.include_router(router_chandra_bhedana)
        app.include_router(router_co_regulation)
        app.include_router(router_cognitive_interweave)
        app.include_router(router_coherent_breathing)
        app.include_router(router_cold_shower_protocol)
        app.include_router(router_cold_water_immersion)
        app.include_router(router_completion_somatic)
        app.include_router(router_containment_therapy)
        app.include_router(router_contrast_therapy)
        app.include_router(router_cryotherapy2)
        app.include_router(router_discharge_somatic)
        app.include_router(router_dorsal_vagal_regulat)
        app.include_router(router_dual_attention_stimu)
        app.include_router(router_eye_contact_therapy)
        app.include_router(router_eye_movement_desensi)
        app.include_router(router_facial_muscles_regul)
        app.include_router(router_felt_sense)
        app.include_router(router_float_anxiety)
        app.include_router(router_float_rest_tank)
        app.include_router(router_flotation_therapy)
        app.include_router(router_future_template)
        app.include_router(router_grounding_somatic)
        app.include_router(router_heart_brain_coherenc)
        app.include_router(router_heartmath_technique)
        app.include_router(router_heat_therapy)
        app.include_router(router_hrv_training)
        app.include_router(router_hydrotherapy)
        app.include_router(router_interoceptive_awaren)
        app.include_router(router_kapalabhati)
        app.include_router(router_kumbhaka_retention)
        app.include_router(router_middle_ear_muscles)
        app.include_router(router_mindful_movement)
        app.include_router(router_nadi_shodhana)
        app.include_router(router_neuroception_safety)
        app.include_router(router_neurofeedback_alpha)
        app.include_router(router_neurofeedback_beta)
        app.include_router(router_neurofeedback_connec)
        app.include_router(router_neurofeedback_delta)
        app.include_router(router_neurofeedback_gamma)
        app.include_router(router_neurofeedback_infra_)
        app.include_router(router_neurofeedback_smr)
        app.include_router(router_neurofeedback_theta)
        app.include_router(router_orientation_somatic)
        app.include_router(router_passive_concentratio)
        app.include_router(router_pendulation)
        app.include_router(router_polyvagal_exercises)
        app.include_router(router_progressive_relaxati)
        app.include_router(router_relaxation_response)
        app.include_router(router_resonant_frequency)
        app.include_router(router_resourcing_somatic)
        app.include_router(router_rhythmic_movement)
        app.include_router(router_rocking_soothing)
        app.include_router(router_sauna_protocol)
        app.include_router(router_self_regulation_body)
        app.include_router(router_sensorimotor_rhythm)
        app.include_router(router_sensory_deprivation)
        app.include_router(router_settling_somatic)
        app.include_router(router_sitali_cooling)
        app.include_router(router_slow_breathing_train)
        app.include_router(router_social_engagement_sy)
        app.include_router(router_somatic_tracking)
        app.include_router(router_steam_therapy)
        app.include_router(router_surya_bhedana)
        app.include_router(router_sympathetic_downregu)
        app.include_router(router_tapping_sequences)
        app.include_router(router_therapeutic_holding)
        app.include_router(router_titration_somatic)
        app.include_router(router_touch_therapy_clinic)
        app.include_router(router_ujjayi_ocean)
        app.include_router(router_ventral_vagal_activa)
        app.include_router(router_voice_prosody_therap)
        app.include_router(router_wim_hof_avancado)
        app.include_router(router_yoga_nidra)
        app.include_router(router_yoga_nidra_resolutio)
        app.include_router(router_yoga_nidra_rotation)
        app.include_router(router_yoga_nidra_visualiza)


plugin = Plugin_terapias_corpo_mente()
