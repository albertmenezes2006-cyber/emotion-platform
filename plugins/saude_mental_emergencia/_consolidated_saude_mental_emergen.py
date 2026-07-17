from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_AOT = APIRouter(prefix="/api/v1/saude_mental/AOT", tags=["saude_mental_emergencia"])
router_CAMS_protocol2 = APIRouter(prefix="/api/v1/saude_mental/CAMS_protocol2", tags=["saude_mental_emergencia"])
router_CISM_model = APIRouter(prefix="/api/v1/saude_mental/CISM_model", tags=["saude_mental_emergencia"])
router_I_PASS = APIRouter(prefix="/api/v1/saude_mental/I_PASS", tags=["saude_mental_emergencia"])
router_Roberts_7_stage = APIRouter(prefix="/api/v1/saude_mental/Roberts_7_stage", tags=["saude_mental_emergencia"])
router_SAFER_model = APIRouter(prefix="/api/v1/saude_mental/SAFER_model", tags=["saude_mental_emergencia"])
router_SBAR_mental2 = APIRouter(prefix="/api/v1/saude_mental/SBAR_mental2", tags=["saude_mental_emergencia"])
router_acute_psychiatric_em = APIRouter(prefix="/api/v1/saude_mental/acute_psychiatric_emergen", tags=["saude_mental_emergencia"])
router_bedside_manner_emerg = APIRouter(prefix="/api/v1/saude_mental/bedside_manner_emergency", tags=["saude_mental_emergencia"])
router_betrayal_trauma = APIRouter(prefix="/api/v1/saude_mental/betrayal_trauma", tags=["saude_mental_emergencia"])
router_burnout_helpers = APIRouter(prefix="/api/v1/saude_mental/burnout_helpers", tags=["saude_mental_emergencia"])
router_callout_emergency = APIRouter(prefix="/api/v1/saude_mental/callout_emergency", tags=["saude_mental_emergencia"])
router_checkback = APIRouter(prefix="/api/v1/saude_mental/checkback", tags=["saude_mental_emergencia"])
router_civil_commitment = APIRouter(prefix="/api/v1/saude_mental/civil_commitment", tags=["saude_mental_emergencia"])
router_closed_loop_communic = APIRouter(prefix="/api/v1/saude_mental/closed_loop_communication", tags=["saude_mental_emergencia"])
router_cognitive_load_emerg = APIRouter(prefix="/api/v1/saude_mental/cognitive_load_emergency", tags=["saude_mental_emergencia"])
router_collaborative_assess = APIRouter(prefix="/api/v1/saude_mental/collaborative_assessment", tags=["saude_mental_emergencia"])
router_combat_operational_s = APIRouter(prefix="/api/v1/saude_mental/combat_operational_stress", tags=["saude_mental_emergencia"])
router_communication_emerge = APIRouter(prefix="/api/v1/saude_mental/communication_emergency", tags=["saude_mental_emergencia"])
router_community_violence = APIRouter(prefix="/api/v1/saude_mental/community_violence", tags=["saude_mental_emergencia"])
router_compassion_fatigue2 = APIRouter(prefix="/api/v1/saude_mental/compassion_fatigue2", tags=["saude_mental_emergencia"])
router_crisis_intervention2 = APIRouter(prefix="/api/v1/saude_mental/crisis_intervention2", tags=["saude_mental_emergencia"])
router_crisis_theory = APIRouter(prefix="/api/v1/saude_mental/crisis_theory", tags=["saude_mental_emergencia"])
router_critical_incident = APIRouter(prefix="/api/v1/saude_mental/critical_incident", tags=["saude_mental_emergencia"])
router_cultural_competence_ = APIRouter(prefix="/api/v1/saude_mental/cultural_competence_emerg", tags=["saude_mental_emergencia"])
router_cumulative_stress = APIRouter(prefix="/api/v1/saude_mental/cumulative_stress", tags=["saude_mental_emergencia"])
router_debrief_emergency = APIRouter(prefix="/api/v1/saude_mental/debrief_emergency", tags=["saude_mental_emergencia"])
router_debriefing_controver = APIRouter(prefix="/api/v1/saude_mental/debriefing_controversy", tags=["saude_mental_emergencia"])
router_decision_fatigue_eme = APIRouter(prefix="/api/v1/saude_mental/decision_fatigue_emergenc", tags=["saude_mental_emergencia"])
router_disaster_mental_heal = APIRouter(prefix="/api/v1/saude_mental/disaster_mental_health", tags=["saude_mental_emergencia"])
router_emergency_hold = APIRouter(prefix="/api/v1/saude_mental/emergency_hold", tags=["saude_mental_emergencia"])
router_emergency_psychiatri = APIRouter(prefix="/api/v1/saude_mental/emergency_psychiatric", tags=["saude_mental_emergencia"])
router_family_emergency = APIRouter(prefix="/api/v1/saude_mental/family_emergency", tags=["saude_mental_emergencia"])
router_firefighter_mental = APIRouter(prefix="/api/v1/saude_mental/firefighter_mental", tags=["saude_mental_emergencia"])
router_first_responder_ment = APIRouter(prefix="/api/v1/saude_mental/first_responder_mental", tags=["saude_mental_emergencia"])
router_handoff_communicatio = APIRouter(prefix="/api/v1/saude_mental/handoff_communication", tags=["saude_mental_emergencia"])
router_handoff_mental = APIRouter(prefix="/api/v1/saude_mental/handoff_mental", tags=["saude_mental_emergencia"])
router_helper_wounded = APIRouter(prefix="/api/v1/saude_mental/helper_wounded", tags=["saude_mental_emergencia"])
router_homicidal_ideation = APIRouter(prefix="/api/v1/saude_mental/homicidal_ideation", tags=["saude_mental_emergencia"])
router_huddle_emergency = APIRouter(prefix="/api/v1/saude_mental/huddle_emergency", tags=["saude_mental_emergencia"])
router_human_factors_mental = APIRouter(prefix="/api/v1/saude_mental/human_factors_mental", tags=["saude_mental_emergencia"])
router_interpreter_emergenc = APIRouter(prefix="/api/v1/saude_mental/interpreter_emergency", tags=["saude_mental_emergencia"])
router_intimate_partner_eme = APIRouter(prefix="/api/v1/saude_mental/intimate_partner_emergenc", tags=["saude_mental_emergencia"])
router_involuntary_commitme = APIRouter(prefix="/api/v1/saude_mental/involuntary_commitment2", tags=["saude_mental_emergencia"])
router_language_emergency = APIRouter(prefix="/api/v1/saude_mental/language_emergency", tags=["saude_mental_emergencia"])
router_lethal_means = APIRouter(prefix="/api/v1/saude_mental/lethal_means", tags=["saude_mental_emergencia"])
router_mass_casualty_mental = APIRouter(prefix="/api/v1/saude_mental/mass_casualty_mental", tags=["saude_mental_emergencia"])
router_means_restriction2 = APIRouter(prefix="/api/v1/saude_mental/means_restriction2", tags=["saude_mental_emergencia"])
router_military_mental = APIRouter(prefix="/api/v1/saude_mental/military_mental", tags=["saude_mental_emergencia"])
router_mitchell_debriefing = APIRouter(prefix="/api/v1/saude_mental/mitchell_debriefing", tags=["saude_mental_emergencia"])
router_moral_injury2 = APIRouter(prefix="/api/v1/saude_mental/moral_injury2", tags=["saude_mental_emergencia"])
router_near_miss = APIRouter(prefix="/api/v1/saude_mental/near_miss", tags=["saude_mental_emergencia"])
router_organizational_suppo = APIRouter(prefix="/api/v1/saude_mental/organizational_support_em", tags=["saude_mental_emergencia"])
router_outpatient_commitmen = APIRouter(prefix="/api/v1/saude_mental/outpatient_commitment", tags=["saude_mental_emergencia"])
router_paramedic_mental = APIRouter(prefix="/api/v1/saude_mental/paramedic_mental", tags=["saude_mental_emergencia"])
router_peer_support_emergen = APIRouter(prefix="/api/v1/saude_mental/peer_support_emergency", tags=["saude_mental_emergencia"])
router_perpetration_trauma = APIRouter(prefix="/api/v1/saude_mental/perpetration_trauma", tags=["saude_mental_emergencia"])
router_police_mental_health = APIRouter(prefix="/api/v1/saude_mental/police_mental_health", tags=["saude_mental_emergencia"])
router_post_incident_suppor = APIRouter(prefix="/api/v1/saude_mental/post_incident_support", tags=["saude_mental_emergencia"])
router_pre_incident_trainin = APIRouter(prefix="/api/v1/saude_mental/pre_incident_training", tags=["saude_mental_emergencia"])
router_psychiatric_boarding = APIRouter(prefix="/api/v1/saude_mental/psychiatric_boarding", tags=["saude_mental_emergencia"])
router_psychiatric_triage = APIRouter(prefix="/api/v1/saude_mental/psychiatric_triage", tags=["saude_mental_emergencia"])
router_psychological_first_ = APIRouter(prefix="/api/v1/saude_mental/psychological_first_aid2", tags=["saude_mental_emergencia"])
router_recommendation_emerg = APIRouter(prefix="/api/v1/saude_mental/recommendation_emergency", tags=["saude_mental_emergencia"])
router_resilience_training = APIRouter(prefix="/api/v1/saude_mental/resilience_training", tags=["saude_mental_emergencia"])
router_root_cause_analysis = APIRouter(prefix="/api/v1/saude_mental/root_cause_analysis", tags=["saude_mental_emergencia"])
router_safety_planning2 = APIRouter(prefix="/api/v1/saude_mental/safety_planning2", tags=["saude_mental_emergencia"])
router_sbar_mental = APIRouter(prefix="/api/v1/saude_mental/sbar_mental", tags=["saude_mental_emergencia"])
router_school_violence = APIRouter(prefix="/api/v1/saude_mental/school_violence", tags=["saude_mental_emergencia"])
router_secondary_traumatic_ = APIRouter(prefix="/api/v1/saude_mental/secondary_traumatic_stres", tags=["saude_mental_emergencia"])
router_self_care_emergency = APIRouter(prefix="/api/v1/saude_mental/self_care_emergency", tags=["saude_mental_emergencia"])
router_sentinel_event = APIRouter(prefix="/api/v1/saude_mental/sentinel_event", tags=["saude_mental_emergencia"])
router_situation_awareness = APIRouter(prefix="/api/v1/saude_mental/situation_awareness", tags=["saude_mental_emergencia"])
router_situation_background = APIRouter(prefix="/api/v1/saude_mental/situation_background_asse", tags=["saude_mental_emergencia"])
router_stress_inoculation_e = APIRouter(prefix="/api/v1/saude_mental/stress_inoculation_emerge", tags=["saude_mental_emergencia"])
router_systems_approach = APIRouter(prefix="/api/v1/saude_mental/systems_approach", tags=["saude_mental_emergencia"])
router_targeted_violence = APIRouter(prefix="/api/v1/saude_mental/targeted_violence", tags=["saude_mental_emergencia"])
router_team_dynamics_emerge = APIRouter(prefix="/api/v1/saude_mental/team_dynamics_emergency", tags=["saude_mental_emergencia"])
router_threat_assessment = APIRouter(prefix="/api/v1/saude_mental/threat_assessment", tags=["saude_mental_emergencia"])
router_timeout_mental = APIRouter(prefix="/api/v1/saude_mental/timeout_mental", tags=["saude_mental_emergencia"])
router_trauma_informed_emer = APIRouter(prefix="/api/v1/saude_mental/trauma_informed_emergency", tags=["saude_mental_emergencia"])
router_vicarious_trauma2 = APIRouter(prefix="/api/v1/saude_mental/vicarious_trauma2", tags=["saude_mental_emergencia"])
router_violence_emergency = APIRouter(prefix="/api/v1/saude_mental/violence_emergency", tags=["saude_mental_emergencia"])
router_witness_trauma = APIRouter(prefix="/api/v1/saude_mental/witness_trauma", tags=["saude_mental_emergencia"])
router_workplace_violence_e = APIRouter(prefix="/api/v1/saude_mental/workplace_violence_emerge", tags=["saude_mental_emergencia"])
router_wounded_healer = APIRouter(prefix="/api/v1/saude_mental/wounded_healer", tags=["saude_mental_emergencia"])

@router_AOT.get("")
async def i_AOT():
    return {"p":"saude_mental_em_AOT","s":"ativo","t":datetime.utcnow().isoformat()}
@router_CAMS_protocol2.get("")
async def i_CAMS_protocol2():
    return {"p":"saude_mental_em_CAMS_protocol2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_CISM_model.get("")
async def i_CISM_model():
    return {"p":"saude_mental_em_CISM_model","s":"ativo","t":datetime.utcnow().isoformat()}
@router_I_PASS.get("")
async def i_I_PASS():
    return {"p":"saude_mental_em_I_PASS","s":"ativo","t":datetime.utcnow().isoformat()}
@router_Roberts_7_stage.get("")
async def i_Roberts_7_stage():
    return {"p":"saude_mental_em_Roberts_7_stage","s":"ativo","t":datetime.utcnow().isoformat()}
@router_SAFER_model.get("")
async def i_SAFER_model():
    return {"p":"saude_mental_em_SAFER_model","s":"ativo","t":datetime.utcnow().isoformat()}
@router_SBAR_mental2.get("")
async def i_SBAR_mental2():
    return {"p":"saude_mental_em_SBAR_mental2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_acute_psychiatric_em.get("")
async def i_acute_psychiatric_em():
    return {"p":"saude_mental_em_acute_psychiatric_em","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bedside_manner_emerg.get("")
async def i_bedside_manner_emerg():
    return {"p":"saude_mental_em_bedside_manner_emerg","s":"ativo","t":datetime.utcnow().isoformat()}
@router_betrayal_trauma.get("")
async def i_betrayal_trauma():
    return {"p":"saude_mental_em_betrayal_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_burnout_helpers.get("")
async def i_burnout_helpers():
    return {"p":"saude_mental_em_burnout_helpers","s":"ativo","t":datetime.utcnow().isoformat()}
@router_callout_emergency.get("")
async def i_callout_emergency():
    return {"p":"saude_mental_em_callout_emergency","s":"ativo","t":datetime.utcnow().isoformat()}
@router_checkback.get("")
async def i_checkback():
    return {"p":"saude_mental_em_checkback","s":"ativo","t":datetime.utcnow().isoformat()}
@router_civil_commitment.get("")
async def i_civil_commitment():
    return {"p":"saude_mental_em_civil_commitment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_closed_loop_communic.get("")
async def i_closed_loop_communic():
    return {"p":"saude_mental_em_closed_loop_communic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cognitive_load_emerg.get("")
async def i_cognitive_load_emerg():
    return {"p":"saude_mental_em_cognitive_load_emerg","s":"ativo","t":datetime.utcnow().isoformat()}
@router_collaborative_assess.get("")
async def i_collaborative_assess():
    return {"p":"saude_mental_em_collaborative_assess","s":"ativo","t":datetime.utcnow().isoformat()}
@router_combat_operational_s.get("")
async def i_combat_operational_s():
    return {"p":"saude_mental_em_combat_operational_s","s":"ativo","t":datetime.utcnow().isoformat()}
@router_communication_emerge.get("")
async def i_communication_emerge():
    return {"p":"saude_mental_em_communication_emerge","s":"ativo","t":datetime.utcnow().isoformat()}
@router_community_violence.get("")
async def i_community_violence():
    return {"p":"saude_mental_em_community_violence","s":"ativo","t":datetime.utcnow().isoformat()}
@router_compassion_fatigue2.get("")
async def i_compassion_fatigue2():
    return {"p":"saude_mental_em_compassion_fatigue2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_crisis_intervention2.get("")
async def i_crisis_intervention2():
    return {"p":"saude_mental_em_crisis_intervention2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_crisis_theory.get("")
async def i_crisis_theory():
    return {"p":"saude_mental_em_crisis_theory","s":"ativo","t":datetime.utcnow().isoformat()}
@router_critical_incident.get("")
async def i_critical_incident():
    return {"p":"saude_mental_em_critical_incident","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cultural_competence_.get("")
async def i_cultural_competence_():
    return {"p":"saude_mental_em_cultural_competence_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cumulative_stress.get("")
async def i_cumulative_stress():
    return {"p":"saude_mental_em_cumulative_stress","s":"ativo","t":datetime.utcnow().isoformat()}
@router_debrief_emergency.get("")
async def i_debrief_emergency():
    return {"p":"saude_mental_em_debrief_emergency","s":"ativo","t":datetime.utcnow().isoformat()}
@router_debriefing_controver.get("")
async def i_debriefing_controver():
    return {"p":"saude_mental_em_debriefing_controver","s":"ativo","t":datetime.utcnow().isoformat()}
@router_decision_fatigue_eme.get("")
async def i_decision_fatigue_eme():
    return {"p":"saude_mental_em_decision_fatigue_eme","s":"ativo","t":datetime.utcnow().isoformat()}
@router_disaster_mental_heal.get("")
async def i_disaster_mental_heal():
    return {"p":"saude_mental_em_disaster_mental_heal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_emergency_hold.get("")
async def i_emergency_hold():
    return {"p":"saude_mental_em_emergency_hold","s":"ativo","t":datetime.utcnow().isoformat()}
@router_emergency_psychiatri.get("")
async def i_emergency_psychiatri():
    return {"p":"saude_mental_em_emergency_psychiatri","s":"ativo","t":datetime.utcnow().isoformat()}
@router_family_emergency.get("")
async def i_family_emergency():
    return {"p":"saude_mental_em_family_emergency","s":"ativo","t":datetime.utcnow().isoformat()}
@router_firefighter_mental.get("")
async def i_firefighter_mental():
    return {"p":"saude_mental_em_firefighter_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_first_responder_ment.get("")
async def i_first_responder_ment():
    return {"p":"saude_mental_em_first_responder_ment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_handoff_communicatio.get("")
async def i_handoff_communicatio():
    return {"p":"saude_mental_em_handoff_communicatio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_handoff_mental.get("")
async def i_handoff_mental():
    return {"p":"saude_mental_em_handoff_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_helper_wounded.get("")
async def i_helper_wounded():
    return {"p":"saude_mental_em_helper_wounded","s":"ativo","t":datetime.utcnow().isoformat()}
@router_homicidal_ideation.get("")
async def i_homicidal_ideation():
    return {"p":"saude_mental_em_homicidal_ideation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_huddle_emergency.get("")
async def i_huddle_emergency():
    return {"p":"saude_mental_em_huddle_emergency","s":"ativo","t":datetime.utcnow().isoformat()}
@router_human_factors_mental.get("")
async def i_human_factors_mental():
    return {"p":"saude_mental_em_human_factors_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_interpreter_emergenc.get("")
async def i_interpreter_emergenc():
    return {"p":"saude_mental_em_interpreter_emergenc","s":"ativo","t":datetime.utcnow().isoformat()}
@router_intimate_partner_eme.get("")
async def i_intimate_partner_eme():
    return {"p":"saude_mental_em_intimate_partner_eme","s":"ativo","t":datetime.utcnow().isoformat()}
@router_involuntary_commitme.get("")
async def i_involuntary_commitme():
    return {"p":"saude_mental_em_involuntary_commitme","s":"ativo","t":datetime.utcnow().isoformat()}
@router_language_emergency.get("")
async def i_language_emergency():
    return {"p":"saude_mental_em_language_emergency","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lethal_means.get("")
async def i_lethal_means():
    return {"p":"saude_mental_em_lethal_means","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mass_casualty_mental.get("")
async def i_mass_casualty_mental():
    return {"p":"saude_mental_em_mass_casualty_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_means_restriction2.get("")
async def i_means_restriction2():
    return {"p":"saude_mental_em_means_restriction2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_military_mental.get("")
async def i_military_mental():
    return {"p":"saude_mental_em_military_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mitchell_debriefing.get("")
async def i_mitchell_debriefing():
    return {"p":"saude_mental_em_mitchell_debriefing","s":"ativo","t":datetime.utcnow().isoformat()}
@router_moral_injury2.get("")
async def i_moral_injury2():
    return {"p":"saude_mental_em_moral_injury2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_near_miss.get("")
async def i_near_miss():
    return {"p":"saude_mental_em_near_miss","s":"ativo","t":datetime.utcnow().isoformat()}
@router_organizational_suppo.get("")
async def i_organizational_suppo():
    return {"p":"saude_mental_em_organizational_suppo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_outpatient_commitmen.get("")
async def i_outpatient_commitmen():
    return {"p":"saude_mental_em_outpatient_commitmen","s":"ativo","t":datetime.utcnow().isoformat()}
@router_paramedic_mental.get("")
async def i_paramedic_mental():
    return {"p":"saude_mental_em_paramedic_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_peer_support_emergen.get("")
async def i_peer_support_emergen():
    return {"p":"saude_mental_em_peer_support_emergen","s":"ativo","t":datetime.utcnow().isoformat()}
@router_perpetration_trauma.get("")
async def i_perpetration_trauma():
    return {"p":"saude_mental_em_perpetration_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_police_mental_health.get("")
async def i_police_mental_health():
    return {"p":"saude_mental_em_police_mental_health","s":"ativo","t":datetime.utcnow().isoformat()}
@router_post_incident_suppor.get("")
async def i_post_incident_suppor():
    return {"p":"saude_mental_em_post_incident_suppor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pre_incident_trainin.get("")
async def i_pre_incident_trainin():
    return {"p":"saude_mental_em_pre_incident_trainin","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psychiatric_boarding.get("")
async def i_psychiatric_boarding():
    return {"p":"saude_mental_em_psychiatric_boarding","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psychiatric_triage.get("")
async def i_psychiatric_triage():
    return {"p":"saude_mental_em_psychiatric_triage","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psychological_first_.get("")
async def i_psychological_first_():
    return {"p":"saude_mental_em_psychological_first_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_recommendation_emerg.get("")
async def i_recommendation_emerg():
    return {"p":"saude_mental_em_recommendation_emerg","s":"ativo","t":datetime.utcnow().isoformat()}
@router_resilience_training.get("")
async def i_resilience_training():
    return {"p":"saude_mental_em_resilience_training","s":"ativo","t":datetime.utcnow().isoformat()}
@router_root_cause_analysis.get("")
async def i_root_cause_analysis():
    return {"p":"saude_mental_em_root_cause_analysis","s":"ativo","t":datetime.utcnow().isoformat()}
@router_safety_planning2.get("")
async def i_safety_planning2():
    return {"p":"saude_mental_em_safety_planning2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sbar_mental.get("")
async def i_sbar_mental():
    return {"p":"saude_mental_em_sbar_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_school_violence.get("")
async def i_school_violence():
    return {"p":"saude_mental_em_school_violence","s":"ativo","t":datetime.utcnow().isoformat()}
@router_secondary_traumatic_.get("")
async def i_secondary_traumatic_():
    return {"p":"saude_mental_em_secondary_traumatic_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_self_care_emergency.get("")
async def i_self_care_emergency():
    return {"p":"saude_mental_em_self_care_emergency","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sentinel_event.get("")
async def i_sentinel_event():
    return {"p":"saude_mental_em_sentinel_event","s":"ativo","t":datetime.utcnow().isoformat()}
@router_situation_awareness.get("")
async def i_situation_awareness():
    return {"p":"saude_mental_em_situation_awareness","s":"ativo","t":datetime.utcnow().isoformat()}
@router_situation_background.get("")
async def i_situation_background():
    return {"p":"saude_mental_em_situation_background","s":"ativo","t":datetime.utcnow().isoformat()}
@router_stress_inoculation_e.get("")
async def i_stress_inoculation_e():
    return {"p":"saude_mental_em_stress_inoculation_e","s":"ativo","t":datetime.utcnow().isoformat()}
@router_systems_approach.get("")
async def i_systems_approach():
    return {"p":"saude_mental_em_systems_approach","s":"ativo","t":datetime.utcnow().isoformat()}
@router_targeted_violence.get("")
async def i_targeted_violence():
    return {"p":"saude_mental_em_targeted_violence","s":"ativo","t":datetime.utcnow().isoformat()}
@router_team_dynamics_emerge.get("")
async def i_team_dynamics_emerge():
    return {"p":"saude_mental_em_team_dynamics_emerge","s":"ativo","t":datetime.utcnow().isoformat()}
@router_threat_assessment.get("")
async def i_threat_assessment():
    return {"p":"saude_mental_em_threat_assessment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_timeout_mental.get("")
async def i_timeout_mental():
    return {"p":"saude_mental_em_timeout_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_trauma_informed_emer.get("")
async def i_trauma_informed_emer():
    return {"p":"saude_mental_em_trauma_informed_emer","s":"ativo","t":datetime.utcnow().isoformat()}
@router_vicarious_trauma2.get("")
async def i_vicarious_trauma2():
    return {"p":"saude_mental_em_vicarious_trauma2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_violence_emergency.get("")
async def i_violence_emergency():
    return {"p":"saude_mental_em_violence_emergency","s":"ativo","t":datetime.utcnow().isoformat()}
@router_witness_trauma.get("")
async def i_witness_trauma():
    return {"p":"saude_mental_em_witness_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_workplace_violence_e.get("")
async def i_workplace_violence_e():
    return {"p":"saude_mental_em_workplace_violence_e","s":"ativo","t":datetime.utcnow().isoformat()}
@router_wounded_healer.get("")
async def i_wounded_healer():
    return {"p":"saude_mental_em_wounded_healer","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_saude_mental_emergen(PluginBase):
    name = "consolidated_saude_mental_emergencia"
    def setup(self, app):
        app.include_router(router_AOT)
        app.include_router(router_CAMS_protocol2)
        app.include_router(router_CISM_model)
        app.include_router(router_I_PASS)
        app.include_router(router_Roberts_7_stage)
        app.include_router(router_SAFER_model)
        app.include_router(router_SBAR_mental2)
        app.include_router(router_acute_psychiatric_em)
        app.include_router(router_bedside_manner_emerg)
        app.include_router(router_betrayal_trauma)
        app.include_router(router_burnout_helpers)
        app.include_router(router_callout_emergency)
        app.include_router(router_checkback)
        app.include_router(router_civil_commitment)
        app.include_router(router_closed_loop_communic)
        app.include_router(router_cognitive_load_emerg)
        app.include_router(router_collaborative_assess)
        app.include_router(router_combat_operational_s)
        app.include_router(router_communication_emerge)
        app.include_router(router_community_violence)
        app.include_router(router_compassion_fatigue2)
        app.include_router(router_crisis_intervention2)
        app.include_router(router_crisis_theory)
        app.include_router(router_critical_incident)
        app.include_router(router_cultural_competence_)
        app.include_router(router_cumulative_stress)
        app.include_router(router_debrief_emergency)
        app.include_router(router_debriefing_controver)
        app.include_router(router_decision_fatigue_eme)
        app.include_router(router_disaster_mental_heal)
        app.include_router(router_emergency_hold)
        app.include_router(router_emergency_psychiatri)
        app.include_router(router_family_emergency)
        app.include_router(router_firefighter_mental)
        app.include_router(router_first_responder_ment)
        app.include_router(router_handoff_communicatio)
        app.include_router(router_handoff_mental)
        app.include_router(router_helper_wounded)
        app.include_router(router_homicidal_ideation)
        app.include_router(router_huddle_emergency)
        app.include_router(router_human_factors_mental)
        app.include_router(router_interpreter_emergenc)
        app.include_router(router_intimate_partner_eme)
        app.include_router(router_involuntary_commitme)
        app.include_router(router_language_emergency)
        app.include_router(router_lethal_means)
        app.include_router(router_mass_casualty_mental)
        app.include_router(router_means_restriction2)
        app.include_router(router_military_mental)
        app.include_router(router_mitchell_debriefing)
        app.include_router(router_moral_injury2)
        app.include_router(router_near_miss)
        app.include_router(router_organizational_suppo)
        app.include_router(router_outpatient_commitmen)
        app.include_router(router_paramedic_mental)
        app.include_router(router_peer_support_emergen)
        app.include_router(router_perpetration_trauma)
        app.include_router(router_police_mental_health)
        app.include_router(router_post_incident_suppor)
        app.include_router(router_pre_incident_trainin)
        app.include_router(router_psychiatric_boarding)
        app.include_router(router_psychiatric_triage)
        app.include_router(router_psychological_first_)
        app.include_router(router_recommendation_emerg)
        app.include_router(router_resilience_training)
        app.include_router(router_root_cause_analysis)
        app.include_router(router_safety_planning2)
        app.include_router(router_sbar_mental)
        app.include_router(router_school_violence)
        app.include_router(router_secondary_traumatic_)
        app.include_router(router_self_care_emergency)
        app.include_router(router_sentinel_event)
        app.include_router(router_situation_awareness)
        app.include_router(router_situation_background)
        app.include_router(router_stress_inoculation_e)
        app.include_router(router_systems_approach)
        app.include_router(router_targeted_violence)
        app.include_router(router_team_dynamics_emerge)
        app.include_router(router_threat_assessment)
        app.include_router(router_timeout_mental)
        app.include_router(router_trauma_informed_emer)
        app.include_router(router_vicarious_trauma2)
        app.include_router(router_violence_emergency)
        app.include_router(router_witness_trauma)
        app.include_router(router_workplace_violence_e)
        app.include_router(router_wounded_healer)


plugin = Plugin_saude_mental_emergen()
