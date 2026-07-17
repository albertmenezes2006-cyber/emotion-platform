from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_adverse_experiences2 = APIRouter(prefix="/api/v1/terapia_trau/adverse_experiences2", tags=["terapia_trauma_avancada"])
router_apparently_normal = APIRouter(prefix="/api/v1/terapia_trau/apparently_normal", tags=["terapia_trauma_avancada"])
router_appease_response = APIRouter(prefix="/api/v1/terapia_trau/appease_response", tags=["terapia_trauma_avancada"])
router_assessment_emdr = APIRouter(prefix="/api/v1/terapia_trau/assessment_emdr", tags=["terapia_trauma_avancada"])
router_attachment_trauma2 = APIRouter(prefix="/api/v1/terapia_trau/attachment_trauma2", tags=["terapia_trauma_avancada"])
router_auditory_bilateral = APIRouter(prefix="/api/v1/terapia_trau/auditory_bilateral", tags=["terapia_trauma_avancada"])
router_avoidance_trauma = APIRouter(prefix="/api/v1/terapia_trau/avoidance_trauma", tags=["terapia_trauma_avancada"])
router_betrayal_trauma2 = APIRouter(prefix="/api/v1/terapia_trau/betrayal_trauma2", tags=["terapia_trauma_avancada"])
router_bilateral_stimulatio = APIRouter(prefix="/api/v1/terapia_trau/bilateral_stimulation", tags=["terapia_trauma_avancada"])
router_birth_trauma = APIRouter(prefix="/api/v1/terapia_trau/birth_trauma", tags=["terapia_trauma_avancada"])
router_body_scan_emdr = APIRouter(prefix="/api/v1/terapia_trau/body_scan_emdr", tags=["terapia_trauma_avancada"])
router_calm_place = APIRouter(prefix="/api/v1/terapia_trau/calm_place", tags=["terapia_trauma_avancada"])
router_closure_emdr = APIRouter(prefix="/api/v1/terapia_trau/closure_emdr", tags=["terapia_trauma_avancada"])
router_collective_trauma2 = APIRouter(prefix="/api/v1/terapia_trau/collective_trauma2", tags=["terapia_trauma_avancada"])
router_container_technique = APIRouter(prefix="/api/v1/terapia_trau/container_technique", tags=["terapia_trauma_avancada"])
router_cultural_trauma = APIRouter(prefix="/api/v1/terapia_trau/cultural_trauma", tags=["terapia_trauma_avancada"])
router_depersonalization_tr = APIRouter(prefix="/api/v1/terapia_trau/depersonalization_trauma", tags=["terapia_trauma_avancada"])
router_derealization_trauma = APIRouter(prefix="/api/v1/terapia_trau/derealization_trauma", tags=["terapia_trauma_avancada"])
router_desensitization_emdr = APIRouter(prefix="/api/v1/terapia_trau/desensitization_emdr", tags=["terapia_trauma_avancada"])
router_developmental_trauma = APIRouter(prefix="/api/v1/terapia_trau/developmental_trauma2", tags=["terapia_trauma_avancada"])
router_dissociation_trauma = APIRouter(prefix="/api/v1/terapia_trau/dissociation_trauma", tags=["terapia_trauma_avancada"])
router_dual_awareness = APIRouter(prefix="/api/v1/terapia_trau/dual_awareness", tags=["terapia_trauma_avancada"])
router_early_childhood_trau = APIRouter(prefix="/api/v1/terapia_trau/early_childhood_trauma", tags=["terapia_trauma_avancada"])
router_ego_states = APIRouter(prefix="/api/v1/terapia_trau/ego_states", tags=["terapia_trauma_avancada"])
router_emdr_phases = APIRouter(prefix="/api/v1/terapia_trau/emdr_phases", tags=["terapia_trauma_avancada"])
router_emotional_flashback = APIRouter(prefix="/api/v1/terapia_trau/emotional_flashback", tags=["terapia_trauma_avancada"])
router_emotional_parts = APIRouter(prefix="/api/v1/terapia_trau/emotional_parts", tags=["terapia_trauma_avancada"])
router_epigenetic_trauma2 = APIRouter(prefix="/api/v1/terapia_trau/epigenetic_trauma2", tags=["terapia_trauma_avancada"])
router_esteem_trauma = APIRouter(prefix="/api/v1/terapia_trau/esteem_trauma", tags=["terapia_trauma_avancada"])
router_eye_movement = APIRouter(prefix="/api/v1/terapia_trau/eye_movement", tags=["terapia_trauma_avancada"])
router_fawn_response = APIRouter(prefix="/api/v1/terapia_trau/fawn_response", tags=["terapia_trauma_avancada"])
router_fight_response = APIRouter(prefix="/api/v1/terapia_trau/fight_response", tags=["terapia_trauma_avancada"])
router_flight_response = APIRouter(prefix="/api/v1/terapia_trau/flight_response", tags=["terapia_trauma_avancada"])
router_fragmentation_trauma = APIRouter(prefix="/api/v1/terapia_trau/fragmentation_trauma", tags=["terapia_trauma_avancada"])
router_freeze_response = APIRouter(prefix="/api/v1/terapia_trau/freeze_response", tags=["terapia_trauma_avancada"])
router_future_vision = APIRouter(prefix="/api/v1/terapia_trau/future_vision", tags=["terapia_trauma_avancada"])
router_grounding_trauma = APIRouter(prefix="/api/v1/terapia_trau/grounding_trauma", tags=["terapia_trauma_avancada"])
router_here_now_then = APIRouter(prefix="/api/v1/terapia_trau/here_now_then", tags=["terapia_trauma_avancada"])
router_historical_trauma2 = APIRouter(prefix="/api/v1/terapia_trau/historical_trauma2", tags=["terapia_trauma_avancada"])
router_history_taking_emdr = APIRouter(prefix="/api/v1/terapia_trau/history_taking_emdr", tags=["terapia_trauma_avancada"])
router_hyperarousal = APIRouter(prefix="/api/v1/terapia_trau/hyperarousal", tags=["terapia_trauma_avancada"])
router_hypoarousal = APIRouter(prefix="/api/v1/terapia_trau/hypoarousal", tags=["terapia_trauma_avancada"])
router_identity_post_trauma = APIRouter(prefix="/api/v1/terapia_trau/identity_post_trauma", tags=["terapia_trauma_avancada"])
router_inner_advisor = APIRouter(prefix="/api/v1/terapia_trau/inner_advisor", tags=["terapia_trauma_avancada"])
router_installation_emdr = APIRouter(prefix="/api/v1/terapia_trau/installation_emdr", tags=["terapia_trauma_avancada"])
router_intergenerational_tr = APIRouter(prefix="/api/v1/terapia_trau/intergenerational_trauma2", tags=["terapia_trauma_avancada"])
router_intimacy_trauma = APIRouter(prefix="/api/v1/terapia_trau/intimacy_trauma", tags=["terapia_trauma_avancada"])
router_intrusive_trauma = APIRouter(prefix="/api/v1/terapia_trau/intrusive_trauma", tags=["terapia_trauma_avancada"])
router_meaning_trauma = APIRouter(prefix="/api/v1/terapia_trau/meaning_trauma", tags=["terapia_trauma_avancada"])
router_moral_injury3 = APIRouter(prefix="/api/v1/terapia_trau/moral_injury3", tags=["terapia_trauma_avancada"])
router_negative_cognition = APIRouter(prefix="/api/v1/terapia_trau/negative_cognition", tags=["terapia_trauma_avancada"])
router_parts_work = APIRouter(prefix="/api/v1/terapia_trau/parts_work", tags=["terapia_trauma_avancada"])
router_past_trauma = APIRouter(prefix="/api/v1/terapia_trau/past_trauma", tags=["terapia_trauma_avancada"])
router_pendulation_trauma = APIRouter(prefix="/api/v1/terapia_trau/pendulation_trauma", tags=["terapia_trauma_avancada"])
router_polyvagal_trauma = APIRouter(prefix="/api/v1/terapia_trau/polyvagal_trauma", tags=["terapia_trauma_avancada"])
router_positive_cognition = APIRouter(prefix="/api/v1/terapia_trau/positive_cognition", tags=["terapia_trauma_avancada"])
router_posttraumatic_growth = APIRouter(prefix="/api/v1/terapia_trau/posttraumatic_growth3", tags=["terapia_trauma_avancada"])
router_power_trauma = APIRouter(prefix="/api/v1/terapia_trau/power_trauma", tags=["terapia_trauma_avancada"])
router_prenatal_trauma = APIRouter(prefix="/api/v1/terapia_trau/prenatal_trauma", tags=["terapia_trauma_avancada"])
router_preparation_emdr = APIRouter(prefix="/api/v1/terapia_trau/preparation_emdr", tags=["terapia_trauma_avancada"])
router_present_resource = APIRouter(prefix="/api/v1/terapia_trau/present_resource", tags=["terapia_trauma_avancada"])
router_primary_structural = APIRouter(prefix="/api/v1/terapia_trau/primary_structural", tags=["terapia_trauma_avancada"])
router_reconnection_trauma = APIRouter(prefix="/api/v1/terapia_trau/reconnection_trauma", tags=["terapia_trauma_avancada"])
router_reevaluation_emdr = APIRouter(prefix="/api/v1/terapia_trau/reevaluation_emdr", tags=["terapia_trauma_avancada"])
router_relational_trauma = APIRouter(prefix="/api/v1/terapia_trau/relational_trauma", tags=["terapia_trauma_avancada"])
router_resource_development = APIRouter(prefix="/api/v1/terapia_trau/resource_development", tags=["terapia_trauma_avancada"])
router_resource_installatio = APIRouter(prefix="/api/v1/terapia_trau/resource_installation", tags=["terapia_trauma_avancada"])
router_safe_place = APIRouter(prefix="/api/v1/terapia_trau/safe_place", tags=["terapia_trauma_avancada"])
router_safety_trauma = APIRouter(prefix="/api/v1/terapia_trau/safety_trauma", tags=["terapia_trauma_avancada"])
router_secondary_structural = APIRouter(prefix="/api/v1/terapia_trau/secondary_structural", tags=["terapia_trauma_avancada"])
router_somatic_flashback = APIRouter(prefix="/api/v1/terapia_trau/somatic_flashback", tags=["terapia_trauma_avancada"])
router_spiritual_injury2 = APIRouter(prefix="/api/v1/terapia_trau/spiritual_injury2", tags=["terapia_trauma_avancada"])
router_structural_dissociat = APIRouter(prefix="/api/v1/terapia_trau/structural_dissociation", tags=["terapia_trauma_avancada"])
router_tapping_emdr = APIRouter(prefix="/api/v1/terapia_trau/tapping_emdr", tags=["terapia_trauma_avancada"])
router_team_resources = APIRouter(prefix="/api/v1/terapia_trau/team_resources", tags=["terapia_trauma_avancada"])
router_tertiary_structural = APIRouter(prefix="/api/v1/terapia_trau/tertiary_structural", tags=["terapia_trauma_avancada"])
router_titration_trauma = APIRouter(prefix="/api/v1/terapia_trau/titration_trauma", tags=["terapia_trauma_avancada"])
router_trauma_complex2 = APIRouter(prefix="/api/v1/terapia_trau/trauma_complex2", tags=["terapia_trauma_avancada"])
router_trauma_integration = APIRouter(prefix="/api/v1/terapia_trau/trauma_integration", tags=["terapia_trauma_avancada"])
router_trauma_narrative = APIRouter(prefix="/api/v1/terapia_trau/trauma_narrative", tags=["terapia_trauma_avancada"])
router_trauma_processing = APIRouter(prefix="/api/v1/terapia_trau/trauma_processing", tags=["terapia_trauma_avancada"])
router_trauma_recovery = APIRouter(prefix="/api/v1/terapia_trau/trauma_recovery", tags=["terapia_trauma_avancada"])
router_trust_trauma = APIRouter(prefix="/api/v1/terapia_trau/trust_trauma", tags=["terapia_trauma_avancada"])
router_window_tolerance = APIRouter(prefix="/api/v1/terapia_trau/window_tolerance", tags=["terapia_trauma_avancada"])

@router_adverse_experiences2.get("")
async def i_adverse_experiences2():
    return {"p":"terapia_trauma__adverse_experiences2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_apparently_normal.get("")
async def i_apparently_normal():
    return {"p":"terapia_trauma__apparently_normal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_appease_response.get("")
async def i_appease_response():
    return {"p":"terapia_trauma__appease_response","s":"ativo","t":datetime.utcnow().isoformat()}
@router_assessment_emdr.get("")
async def i_assessment_emdr():
    return {"p":"terapia_trauma__assessment_emdr","s":"ativo","t":datetime.utcnow().isoformat()}
@router_attachment_trauma2.get("")
async def i_attachment_trauma2():
    return {"p":"terapia_trauma__attachment_trauma2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_auditory_bilateral.get("")
async def i_auditory_bilateral():
    return {"p":"terapia_trauma__auditory_bilateral","s":"ativo","t":datetime.utcnow().isoformat()}
@router_avoidance_trauma.get("")
async def i_avoidance_trauma():
    return {"p":"terapia_trauma__avoidance_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_betrayal_trauma2.get("")
async def i_betrayal_trauma2():
    return {"p":"terapia_trauma__betrayal_trauma2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bilateral_stimulatio.get("")
async def i_bilateral_stimulatio():
    return {"p":"terapia_trauma__bilateral_stimulatio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_birth_trauma.get("")
async def i_birth_trauma():
    return {"p":"terapia_trauma__birth_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_body_scan_emdr.get("")
async def i_body_scan_emdr():
    return {"p":"terapia_trauma__body_scan_emdr","s":"ativo","t":datetime.utcnow().isoformat()}
@router_calm_place.get("")
async def i_calm_place():
    return {"p":"terapia_trauma__calm_place","s":"ativo","t":datetime.utcnow().isoformat()}
@router_closure_emdr.get("")
async def i_closure_emdr():
    return {"p":"terapia_trauma__closure_emdr","s":"ativo","t":datetime.utcnow().isoformat()}
@router_collective_trauma2.get("")
async def i_collective_trauma2():
    return {"p":"terapia_trauma__collective_trauma2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_container_technique.get("")
async def i_container_technique():
    return {"p":"terapia_trauma__container_technique","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cultural_trauma.get("")
async def i_cultural_trauma():
    return {"p":"terapia_trauma__cultural_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_depersonalization_tr.get("")
async def i_depersonalization_tr():
    return {"p":"terapia_trauma__depersonalization_tr","s":"ativo","t":datetime.utcnow().isoformat()}
@router_derealization_trauma.get("")
async def i_derealization_trauma():
    return {"p":"terapia_trauma__derealization_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_desensitization_emdr.get("")
async def i_desensitization_emdr():
    return {"p":"terapia_trauma__desensitization_emdr","s":"ativo","t":datetime.utcnow().isoformat()}
@router_developmental_trauma.get("")
async def i_developmental_trauma():
    return {"p":"terapia_trauma__developmental_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dissociation_trauma.get("")
async def i_dissociation_trauma():
    return {"p":"terapia_trauma__dissociation_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dual_awareness.get("")
async def i_dual_awareness():
    return {"p":"terapia_trauma__dual_awareness","s":"ativo","t":datetime.utcnow().isoformat()}
@router_early_childhood_trau.get("")
async def i_early_childhood_trau():
    return {"p":"terapia_trauma__early_childhood_trau","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ego_states.get("")
async def i_ego_states():
    return {"p":"terapia_trauma__ego_states","s":"ativo","t":datetime.utcnow().isoformat()}
@router_emdr_phases.get("")
async def i_emdr_phases():
    return {"p":"terapia_trauma__emdr_phases","s":"ativo","t":datetime.utcnow().isoformat()}
@router_emotional_flashback.get("")
async def i_emotional_flashback():
    return {"p":"terapia_trauma__emotional_flashback","s":"ativo","t":datetime.utcnow().isoformat()}
@router_emotional_parts.get("")
async def i_emotional_parts():
    return {"p":"terapia_trauma__emotional_parts","s":"ativo","t":datetime.utcnow().isoformat()}
@router_epigenetic_trauma2.get("")
async def i_epigenetic_trauma2():
    return {"p":"terapia_trauma__epigenetic_trauma2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_esteem_trauma.get("")
async def i_esteem_trauma():
    return {"p":"terapia_trauma__esteem_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_eye_movement.get("")
async def i_eye_movement():
    return {"p":"terapia_trauma__eye_movement","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fawn_response.get("")
async def i_fawn_response():
    return {"p":"terapia_trauma__fawn_response","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fight_response.get("")
async def i_fight_response():
    return {"p":"terapia_trauma__fight_response","s":"ativo","t":datetime.utcnow().isoformat()}
@router_flight_response.get("")
async def i_flight_response():
    return {"p":"terapia_trauma__flight_response","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fragmentation_trauma.get("")
async def i_fragmentation_trauma():
    return {"p":"terapia_trauma__fragmentation_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_freeze_response.get("")
async def i_freeze_response():
    return {"p":"terapia_trauma__freeze_response","s":"ativo","t":datetime.utcnow().isoformat()}
@router_future_vision.get("")
async def i_future_vision():
    return {"p":"terapia_trauma__future_vision","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grounding_trauma.get("")
async def i_grounding_trauma():
    return {"p":"terapia_trauma__grounding_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_here_now_then.get("")
async def i_here_now_then():
    return {"p":"terapia_trauma__here_now_then","s":"ativo","t":datetime.utcnow().isoformat()}
@router_historical_trauma2.get("")
async def i_historical_trauma2():
    return {"p":"terapia_trauma__historical_trauma2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_history_taking_emdr.get("")
async def i_history_taking_emdr():
    return {"p":"terapia_trauma__history_taking_emdr","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hyperarousal.get("")
async def i_hyperarousal():
    return {"p":"terapia_trauma__hyperarousal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hypoarousal.get("")
async def i_hypoarousal():
    return {"p":"terapia_trauma__hypoarousal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_identity_post_trauma.get("")
async def i_identity_post_trauma():
    return {"p":"terapia_trauma__identity_post_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_inner_advisor.get("")
async def i_inner_advisor():
    return {"p":"terapia_trauma__inner_advisor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_installation_emdr.get("")
async def i_installation_emdr():
    return {"p":"terapia_trauma__installation_emdr","s":"ativo","t":datetime.utcnow().isoformat()}
@router_intergenerational_tr.get("")
async def i_intergenerational_tr():
    return {"p":"terapia_trauma__intergenerational_tr","s":"ativo","t":datetime.utcnow().isoformat()}
@router_intimacy_trauma.get("")
async def i_intimacy_trauma():
    return {"p":"terapia_trauma__intimacy_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_intrusive_trauma.get("")
async def i_intrusive_trauma():
    return {"p":"terapia_trauma__intrusive_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_meaning_trauma.get("")
async def i_meaning_trauma():
    return {"p":"terapia_trauma__meaning_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_moral_injury3.get("")
async def i_moral_injury3():
    return {"p":"terapia_trauma__moral_injury3","s":"ativo","t":datetime.utcnow().isoformat()}
@router_negative_cognition.get("")
async def i_negative_cognition():
    return {"p":"terapia_trauma__negative_cognition","s":"ativo","t":datetime.utcnow().isoformat()}
@router_parts_work.get("")
async def i_parts_work():
    return {"p":"terapia_trauma__parts_work","s":"ativo","t":datetime.utcnow().isoformat()}
@router_past_trauma.get("")
async def i_past_trauma():
    return {"p":"terapia_trauma__past_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pendulation_trauma.get("")
async def i_pendulation_trauma():
    return {"p":"terapia_trauma__pendulation_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_polyvagal_trauma.get("")
async def i_polyvagal_trauma():
    return {"p":"terapia_trauma__polyvagal_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_positive_cognition.get("")
async def i_positive_cognition():
    return {"p":"terapia_trauma__positive_cognition","s":"ativo","t":datetime.utcnow().isoformat()}
@router_posttraumatic_growth.get("")
async def i_posttraumatic_growth():
    return {"p":"terapia_trauma__posttraumatic_growth","s":"ativo","t":datetime.utcnow().isoformat()}
@router_power_trauma.get("")
async def i_power_trauma():
    return {"p":"terapia_trauma__power_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_prenatal_trauma.get("")
async def i_prenatal_trauma():
    return {"p":"terapia_trauma__prenatal_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_preparation_emdr.get("")
async def i_preparation_emdr():
    return {"p":"terapia_trauma__preparation_emdr","s":"ativo","t":datetime.utcnow().isoformat()}
@router_present_resource.get("")
async def i_present_resource():
    return {"p":"terapia_trauma__present_resource","s":"ativo","t":datetime.utcnow().isoformat()}
@router_primary_structural.get("")
async def i_primary_structural():
    return {"p":"terapia_trauma__primary_structural","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reconnection_trauma.get("")
async def i_reconnection_trauma():
    return {"p":"terapia_trauma__reconnection_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reevaluation_emdr.get("")
async def i_reevaluation_emdr():
    return {"p":"terapia_trauma__reevaluation_emdr","s":"ativo","t":datetime.utcnow().isoformat()}
@router_relational_trauma.get("")
async def i_relational_trauma():
    return {"p":"terapia_trauma__relational_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_resource_development.get("")
async def i_resource_development():
    return {"p":"terapia_trauma__resource_development","s":"ativo","t":datetime.utcnow().isoformat()}
@router_resource_installatio.get("")
async def i_resource_installatio():
    return {"p":"terapia_trauma__resource_installatio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_safe_place.get("")
async def i_safe_place():
    return {"p":"terapia_trauma__safe_place","s":"ativo","t":datetime.utcnow().isoformat()}
@router_safety_trauma.get("")
async def i_safety_trauma():
    return {"p":"terapia_trauma__safety_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_secondary_structural.get("")
async def i_secondary_structural():
    return {"p":"terapia_trauma__secondary_structural","s":"ativo","t":datetime.utcnow().isoformat()}
@router_somatic_flashback.get("")
async def i_somatic_flashback():
    return {"p":"terapia_trauma__somatic_flashback","s":"ativo","t":datetime.utcnow().isoformat()}
@router_spiritual_injury2.get("")
async def i_spiritual_injury2():
    return {"p":"terapia_trauma__spiritual_injury2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_structural_dissociat.get("")
async def i_structural_dissociat():
    return {"p":"terapia_trauma__structural_dissociat","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tapping_emdr.get("")
async def i_tapping_emdr():
    return {"p":"terapia_trauma__tapping_emdr","s":"ativo","t":datetime.utcnow().isoformat()}
@router_team_resources.get("")
async def i_team_resources():
    return {"p":"terapia_trauma__team_resources","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tertiary_structural.get("")
async def i_tertiary_structural():
    return {"p":"terapia_trauma__tertiary_structural","s":"ativo","t":datetime.utcnow().isoformat()}
@router_titration_trauma.get("")
async def i_titration_trauma():
    return {"p":"terapia_trauma__titration_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_trauma_complex2.get("")
async def i_trauma_complex2():
    return {"p":"terapia_trauma__trauma_complex2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_trauma_integration.get("")
async def i_trauma_integration():
    return {"p":"terapia_trauma__trauma_integration","s":"ativo","t":datetime.utcnow().isoformat()}
@router_trauma_narrative.get("")
async def i_trauma_narrative():
    return {"p":"terapia_trauma__trauma_narrative","s":"ativo","t":datetime.utcnow().isoformat()}
@router_trauma_processing.get("")
async def i_trauma_processing():
    return {"p":"terapia_trauma__trauma_processing","s":"ativo","t":datetime.utcnow().isoformat()}
@router_trauma_recovery.get("")
async def i_trauma_recovery():
    return {"p":"terapia_trauma__trauma_recovery","s":"ativo","t":datetime.utcnow().isoformat()}
@router_trust_trauma.get("")
async def i_trust_trauma():
    return {"p":"terapia_trauma__trust_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_window_tolerance.get("")
async def i_window_tolerance():
    return {"p":"terapia_trauma__window_tolerance","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_terapia_trauma_avanc(PluginBase):
    name = "consolidated_terapia_trauma_avancada"
    def setup(self, app):
        app.include_router(router_adverse_experiences2)
        app.include_router(router_apparently_normal)
        app.include_router(router_appease_response)
        app.include_router(router_assessment_emdr)
        app.include_router(router_attachment_trauma2)
        app.include_router(router_auditory_bilateral)
        app.include_router(router_avoidance_trauma)
        app.include_router(router_betrayal_trauma2)
        app.include_router(router_bilateral_stimulatio)
        app.include_router(router_birth_trauma)
        app.include_router(router_body_scan_emdr)
        app.include_router(router_calm_place)
        app.include_router(router_closure_emdr)
        app.include_router(router_collective_trauma2)
        app.include_router(router_container_technique)
        app.include_router(router_cultural_trauma)
        app.include_router(router_depersonalization_tr)
        app.include_router(router_derealization_trauma)
        app.include_router(router_desensitization_emdr)
        app.include_router(router_developmental_trauma)
        app.include_router(router_dissociation_trauma)
        app.include_router(router_dual_awareness)
        app.include_router(router_early_childhood_trau)
        app.include_router(router_ego_states)
        app.include_router(router_emdr_phases)
        app.include_router(router_emotional_flashback)
        app.include_router(router_emotional_parts)
        app.include_router(router_epigenetic_trauma2)
        app.include_router(router_esteem_trauma)
        app.include_router(router_eye_movement)
        app.include_router(router_fawn_response)
        app.include_router(router_fight_response)
        app.include_router(router_flight_response)
        app.include_router(router_fragmentation_trauma)
        app.include_router(router_freeze_response)
        app.include_router(router_future_vision)
        app.include_router(router_grounding_trauma)
        app.include_router(router_here_now_then)
        app.include_router(router_historical_trauma2)
        app.include_router(router_history_taking_emdr)
        app.include_router(router_hyperarousal)
        app.include_router(router_hypoarousal)
        app.include_router(router_identity_post_trauma)
        app.include_router(router_inner_advisor)
        app.include_router(router_installation_emdr)
        app.include_router(router_intergenerational_tr)
        app.include_router(router_intimacy_trauma)
        app.include_router(router_intrusive_trauma)
        app.include_router(router_meaning_trauma)
        app.include_router(router_moral_injury3)
        app.include_router(router_negative_cognition)
        app.include_router(router_parts_work)
        app.include_router(router_past_trauma)
        app.include_router(router_pendulation_trauma)
        app.include_router(router_polyvagal_trauma)
        app.include_router(router_positive_cognition)
        app.include_router(router_posttraumatic_growth)
        app.include_router(router_power_trauma)
        app.include_router(router_prenatal_trauma)
        app.include_router(router_preparation_emdr)
        app.include_router(router_present_resource)
        app.include_router(router_primary_structural)
        app.include_router(router_reconnection_trauma)
        app.include_router(router_reevaluation_emdr)
        app.include_router(router_relational_trauma)
        app.include_router(router_resource_development)
        app.include_router(router_resource_installatio)
        app.include_router(router_safe_place)
        app.include_router(router_safety_trauma)
        app.include_router(router_secondary_structural)
        app.include_router(router_somatic_flashback)
        app.include_router(router_spiritual_injury2)
        app.include_router(router_structural_dissociat)
        app.include_router(router_tapping_emdr)
        app.include_router(router_team_resources)
        app.include_router(router_tertiary_structural)
        app.include_router(router_titration_trauma)
        app.include_router(router_trauma_complex2)
        app.include_router(router_trauma_integration)
        app.include_router(router_trauma_narrative)
        app.include_router(router_trauma_processing)
        app.include_router(router_trauma_recovery)
        app.include_router(router_trust_trauma)
        app.include_router(router_window_tolerance)


plugin = Plugin_terapia_trauma_avanc()
