from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_CTE_military = APIRouter(prefix="/api/v1/saude_mental/CTE_military", tags=["saude_mental_militar"])
router_DCoE_resources = APIRouter(prefix="/api/v1/saude_mental/DCoE_resources", tags=["saude_mental_militar"])
router_EFMP_military = APIRouter(prefix="/api/v1/saude_mental/EFMP_military", tags=["saude_mental_militar"])
router_MST_military = APIRouter(prefix="/api/v1/saude_mental/MST_military", tags=["saude_mental_militar"])
router_VA_mental_health = APIRouter(prefix="/api/v1/saude_mental/VA_mental_health", tags=["saude_mental_militar"])
router_assault_military = APIRouter(prefix="/api/v1/saude_mental/assault_military", tags=["saude_mental_militar"])
router_attention_control_mi = APIRouter(prefix="/api/v1/saude_mental/attention_control_militar", tags=["saude_mental_militar"])
router_betrayal_military = APIRouter(prefix="/api/v1/saude_mental/betrayal_military", tags=["saude_mental_militar"])
router_blast_injury = APIRouter(prefix="/api/v1/saude_mental/blast_injury", tags=["saude_mental_militar"])
router_caregiver_military = APIRouter(prefix="/api/v1/saude_mental/caregiver_military", tags=["saude_mental_militar"])
router_chronic_traumatic_en = APIRouter(prefix="/api/v1/saude_mental/chronic_traumatic_enceph", tags=["saude_mental_militar"])
router_civilian_culture_adj = APIRouter(prefix="/api/v1/saude_mental/civilian_culture_adjustme", tags=["saude_mental_militar"])
router_combat_exposure = APIRouter(prefix="/api/v1/saude_mental/combat_exposure", tags=["saude_mental_militar"])
router_combat_psychology = APIRouter(prefix="/api/v1/saude_mental/combat_psychology", tags=["saude_mental_militar"])
router_community_provider_m = APIRouter(prefix="/api/v1/saude_mental/community_provider_milita", tags=["saude_mental_militar"])
router_comprehensive_soldie = APIRouter(prefix="/api/v1/saude_mental/comprehensive_soldier_fit", tags=["saude_mental_militar"])
router_concussion_military = APIRouter(prefix="/api/v1/saude_mental/concussion_military", tags=["saude_mental_militar"])
router_cultural_competence_ = APIRouter(prefix="/api/v1/saude_mental/cultural_competence_milit", tags=["saude_mental_militar"])
router_deployment_child = APIRouter(prefix="/api/v1/saude_mental/deployment_child", tags=["saude_mental_militar"])
router_deployment_phase = APIRouter(prefix="/api/v1/saude_mental/deployment_phase", tags=["saude_mental_militar"])
router_deployment_psycholog = APIRouter(prefix="/api/v1/saude_mental/deployment_psychology", tags=["saude_mental_militar"])
router_education_military_c = APIRouter(prefix="/api/v1/saude_mental/education_military_child", tags=["saude_mental_militar"])
router_employment_veterans = APIRouter(prefix="/api/v1/saude_mental/employment_veterans", tags=["saude_mental_militar"])
router_energy_management_mi = APIRouter(prefix="/api/v1/saude_mental/energy_management_militar", tags=["saude_mental_militar"])
router_esprit_de_corps = APIRouter(prefix="/api/v1/saude_mental/esprit_de_corps", tags=["saude_mental_militar"])
router_family_reintegration = APIRouter(prefix="/api/v1/saude_mental/family_reintegration", tags=["saude_mental_militar"])
router_family_veteran_menta = APIRouter(prefix="/api/v1/saude_mental/family_veteran_mental", tags=["saude_mental_militar"])
router_goal_setting_militar = APIRouter(prefix="/api/v1/saude_mental/goal_setting_military", tags=["saude_mental_militar"])
router_gun_access_veterans = APIRouter(prefix="/api/v1/saude_mental/gun_access_veterans", tags=["saude_mental_militar"])
router_harassment_military = APIRouter(prefix="/api/v1/saude_mental/harassment_military", tags=["saude_mental_militar"])
router_help_seeking_militar = APIRouter(prefix="/api/v1/saude_mental/help_seeking_military", tags=["saude_mental_militar"])
router_homecoming_mental = APIRouter(prefix="/api/v1/saude_mental/homecoming_mental", tags=["saude_mental_militar"])
router_homelessness_veteran = APIRouter(prefix="/api/v1/saude_mental/homelessness_veterans", tags=["saude_mental_militar"])
router_identity_transition_ = APIRouter(prefix="/api/v1/saude_mental/identity_transition_vet", tags=["saude_mental_militar"])
router_incarceration_vetera = APIRouter(prefix="/api/v1/saude_mental/incarceration_veterans", tags=["saude_mental_militar"])
router_invisible_wounds = APIRouter(prefix="/api/v1/saude_mental/invisible_wounds", tags=["saude_mental_militar"])
router_leadership_military = APIRouter(prefix="/api/v1/saude_mental/leadership_military", tags=["saude_mental_militar"])
router_mTBI_military = APIRouter(prefix="/api/v1/saude_mental/mTBI_military", tags=["saude_mental_militar"])
router_make_the_connection = APIRouter(prefix="/api/v1/saude_mental/make_the_connection", tags=["saude_mental_militar"])
router_master_resilience = APIRouter(prefix="/api/v1/saude_mental/master_resilience", tags=["saude_mental_militar"])
router_means_restriction_ve = APIRouter(prefix="/api/v1/saude_mental/means_restriction_vet", tags=["saude_mental_militar"])
router_mental_toughness_mil = APIRouter(prefix="/api/v1/saude_mental/mental_toughness_military", tags=["saude_mental_militar"])
router_military_child = APIRouter(prefix="/api/v1/saude_mental/military_child", tags=["saude_mental_militar"])
router_military_culture = APIRouter(prefix="/api/v1/saude_mental/military_culture", tags=["saude_mental_militar"])
router_military_history_tak = APIRouter(prefix="/api/v1/saude_mental/military_history_taking", tags=["saude_mental_militar"])
router_military_informed_ca = APIRouter(prefix="/api/v1/saude_mental/military_informed_care", tags=["saude_mental_militar"])
router_military_psychology = APIRouter(prefix="/api/v1/saude_mental/military_psychology", tags=["saude_mental_militar"])
router_military_sexual_trau = APIRouter(prefix="/api/v1/saude_mental/military_sexual_trauma", tags=["saude_mental_militar"])
router_moral_injury_militar = APIRouter(prefix="/api/v1/saude_mental/moral_injury_military", tags=["saude_mental_militar"])
router_operational_psycholo = APIRouter(prefix="/api/v1/saude_mental/operational_psychology", tags=["saude_mental_militar"])
router_peer_support_veteran = APIRouter(prefix="/api/v1/saude_mental/peer_support_veterans", tags=["saude_mental_militar"])
router_perpetration_militar = APIRouter(prefix="/api/v1/saude_mental/perpetration_military", tags=["saude_mental_militar"])
router_post_deployment = APIRouter(prefix="/api/v1/saude_mental/post_deployment", tags=["saude_mental_militar"])
router_pre_deployment = APIRouter(prefix="/api/v1/saude_mental/pre_deployment", tags=["saude_mental_militar"])
router_ptsd_military = APIRouter(prefix="/api/v1/saude_mental/ptsd_military", tags=["saude_mental_militar"])
router_real_warriors = APIRouter(prefix="/api/v1/saude_mental/real_warriors", tags=["saude_mental_militar"])
router_recharge_military = APIRouter(prefix="/api/v1/saude_mental/recharge_military", tags=["saude_mental_militar"])
router_reintegration_milita = APIRouter(prefix="/api/v1/saude_mental/reintegration_military", tags=["saude_mental_militar"])
router_reporting_military = APIRouter(prefix="/api/v1/saude_mental/reporting_military", tags=["saude_mental_militar"])
router_resilience_training_ = APIRouter(prefix="/api/v1/saude_mental/resilience_training_milit", tags=["saude_mental_militar"])
router_resilient_military_k = APIRouter(prefix="/api/v1/saude_mental/resilient_military_kid", tags=["saude_mental_militar"])
router_retaliation_military = APIRouter(prefix="/api/v1/saude_mental/retaliation_military", tags=["saude_mental_militar"])
router_reunion_military = APIRouter(prefix="/api/v1/saude_mental/reunion_military", tags=["saude_mental_militar"])
router_special_needs_milita = APIRouter(prefix="/api/v1/saude_mental/special_needs_military", tags=["saude_mental_militar"])
router_spiritual_injury_mil = APIRouter(prefix="/api/v1/saude_mental/spiritual_injury_military", tags=["saude_mental_militar"])
router_stigma_military = APIRouter(prefix="/api/v1/saude_mental/stigma_military", tags=["saude_mental_militar"])
router_substance_abuse_vete = APIRouter(prefix="/api/v1/saude_mental/substance_abuse_veterans", tags=["saude_mental_militar"])
router_suicide_military = APIRouter(prefix="/api/v1/saude_mental/suicide_military", tags=["saude_mental_militar"])
router_suicide_prevention_m = APIRouter(prefix="/api/v1/saude_mental/suicide_prevention_milita", tags=["saude_mental_militar"])
router_tactical_breathing_m = APIRouter(prefix="/api/v1/saude_mental/tactical_breathing_milita", tags=["saude_mental_militar"])
router_tbi_military = APIRouter(prefix="/api/v1/saude_mental/tbi_military", tags=["saude_mental_militar"])
router_team_building_milita = APIRouter(prefix="/api/v1/saude_mental/team_building_military", tags=["saude_mental_militar"])
router_telehealth_veterans = APIRouter(prefix="/api/v1/saude_mental/telehealth_veterans", tags=["saude_mental_militar"])
router_transition_civilian = APIRouter(prefix="/api/v1/saude_mental/transition_civilian", tags=["saude_mental_militar"])
router_traumatic_exposure_m = APIRouter(prefix="/api/v1/saude_mental/traumatic_exposure_milita", tags=["saude_mental_militar"])
router_unit_cohesion = APIRouter(prefix="/api/v1/saude_mental/unit_cohesion", tags=["saude_mental_militar"])
router_vet_center = APIRouter(prefix="/api/v1/saude_mental/vet_center", tags=["saude_mental_militar"])
router_vet_to_vet = APIRouter(prefix="/api/v1/saude_mental/vet_to_vet", tags=["saude_mental_militar"])
router_veteran_mental_healt = APIRouter(prefix="/api/v1/saude_mental/veteran_mental_health", tags=["saude_mental_militar"])
router_veteran_service_orga = APIRouter(prefix="/api/v1/saude_mental/veteran_service_organizat", tags=["saude_mental_militar"])
router_veteran_suicide = APIRouter(prefix="/api/v1/saude_mental/veteran_suicide", tags=["saude_mental_militar"])
router_warrior_ethos = APIRouter(prefix="/api/v1/saude_mental/warrior_ethos", tags=["saude_mental_militar"])
router_witnessing_military = APIRouter(prefix="/api/v1/saude_mental/witnessing_military", tags=["saude_mental_militar"])

@router_CTE_military.get("")
async def i_CTE_military():
    return {"p":"saude_mental_mi_CTE_military","s":"ativo","t":datetime.utcnow().isoformat()}
@router_DCoE_resources.get("")
async def i_DCoE_resources():
    return {"p":"saude_mental_mi_DCoE_resources","s":"ativo","t":datetime.utcnow().isoformat()}
@router_EFMP_military.get("")
async def i_EFMP_military():
    return {"p":"saude_mental_mi_EFMP_military","s":"ativo","t":datetime.utcnow().isoformat()}
@router_MST_military.get("")
async def i_MST_military():
    return {"p":"saude_mental_mi_MST_military","s":"ativo","t":datetime.utcnow().isoformat()}
@router_VA_mental_health.get("")
async def i_VA_mental_health():
    return {"p":"saude_mental_mi_VA_mental_health","s":"ativo","t":datetime.utcnow().isoformat()}
@router_assault_military.get("")
async def i_assault_military():
    return {"p":"saude_mental_mi_assault_military","s":"ativo","t":datetime.utcnow().isoformat()}
@router_attention_control_mi.get("")
async def i_attention_control_mi():
    return {"p":"saude_mental_mi_attention_control_mi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_betrayal_military.get("")
async def i_betrayal_military():
    return {"p":"saude_mental_mi_betrayal_military","s":"ativo","t":datetime.utcnow().isoformat()}
@router_blast_injury.get("")
async def i_blast_injury():
    return {"p":"saude_mental_mi_blast_injury","s":"ativo","t":datetime.utcnow().isoformat()}
@router_caregiver_military.get("")
async def i_caregiver_military():
    return {"p":"saude_mental_mi_caregiver_military","s":"ativo","t":datetime.utcnow().isoformat()}
@router_chronic_traumatic_en.get("")
async def i_chronic_traumatic_en():
    return {"p":"saude_mental_mi_chronic_traumatic_en","s":"ativo","t":datetime.utcnow().isoformat()}
@router_civilian_culture_adj.get("")
async def i_civilian_culture_adj():
    return {"p":"saude_mental_mi_civilian_culture_adj","s":"ativo","t":datetime.utcnow().isoformat()}
@router_combat_exposure.get("")
async def i_combat_exposure():
    return {"p":"saude_mental_mi_combat_exposure","s":"ativo","t":datetime.utcnow().isoformat()}
@router_combat_psychology.get("")
async def i_combat_psychology():
    return {"p":"saude_mental_mi_combat_psychology","s":"ativo","t":datetime.utcnow().isoformat()}
@router_community_provider_m.get("")
async def i_community_provider_m():
    return {"p":"saude_mental_mi_community_provider_m","s":"ativo","t":datetime.utcnow().isoformat()}
@router_comprehensive_soldie.get("")
async def i_comprehensive_soldie():
    return {"p":"saude_mental_mi_comprehensive_soldie","s":"ativo","t":datetime.utcnow().isoformat()}
@router_concussion_military.get("")
async def i_concussion_military():
    return {"p":"saude_mental_mi_concussion_military","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cultural_competence_.get("")
async def i_cultural_competence_():
    return {"p":"saude_mental_mi_cultural_competence_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_deployment_child.get("")
async def i_deployment_child():
    return {"p":"saude_mental_mi_deployment_child","s":"ativo","t":datetime.utcnow().isoformat()}
@router_deployment_phase.get("")
async def i_deployment_phase():
    return {"p":"saude_mental_mi_deployment_phase","s":"ativo","t":datetime.utcnow().isoformat()}
@router_deployment_psycholog.get("")
async def i_deployment_psycholog():
    return {"p":"saude_mental_mi_deployment_psycholog","s":"ativo","t":datetime.utcnow().isoformat()}
@router_education_military_c.get("")
async def i_education_military_c():
    return {"p":"saude_mental_mi_education_military_c","s":"ativo","t":datetime.utcnow().isoformat()}
@router_employment_veterans.get("")
async def i_employment_veterans():
    return {"p":"saude_mental_mi_employment_veterans","s":"ativo","t":datetime.utcnow().isoformat()}
@router_energy_management_mi.get("")
async def i_energy_management_mi():
    return {"p":"saude_mental_mi_energy_management_mi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_esprit_de_corps.get("")
async def i_esprit_de_corps():
    return {"p":"saude_mental_mi_esprit_de_corps","s":"ativo","t":datetime.utcnow().isoformat()}
@router_family_reintegration.get("")
async def i_family_reintegration():
    return {"p":"saude_mental_mi_family_reintegration","s":"ativo","t":datetime.utcnow().isoformat()}
@router_family_veteran_menta.get("")
async def i_family_veteran_menta():
    return {"p":"saude_mental_mi_family_veteran_menta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_goal_setting_militar.get("")
async def i_goal_setting_militar():
    return {"p":"saude_mental_mi_goal_setting_militar","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gun_access_veterans.get("")
async def i_gun_access_veterans():
    return {"p":"saude_mental_mi_gun_access_veterans","s":"ativo","t":datetime.utcnow().isoformat()}
@router_harassment_military.get("")
async def i_harassment_military():
    return {"p":"saude_mental_mi_harassment_military","s":"ativo","t":datetime.utcnow().isoformat()}
@router_help_seeking_militar.get("")
async def i_help_seeking_militar():
    return {"p":"saude_mental_mi_help_seeking_militar","s":"ativo","t":datetime.utcnow().isoformat()}
@router_homecoming_mental.get("")
async def i_homecoming_mental():
    return {"p":"saude_mental_mi_homecoming_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_homelessness_veteran.get("")
async def i_homelessness_veteran():
    return {"p":"saude_mental_mi_homelessness_veteran","s":"ativo","t":datetime.utcnow().isoformat()}
@router_identity_transition_.get("")
async def i_identity_transition_():
    return {"p":"saude_mental_mi_identity_transition_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_incarceration_vetera.get("")
async def i_incarceration_vetera():
    return {"p":"saude_mental_mi_incarceration_vetera","s":"ativo","t":datetime.utcnow().isoformat()}
@router_invisible_wounds.get("")
async def i_invisible_wounds():
    return {"p":"saude_mental_mi_invisible_wounds","s":"ativo","t":datetime.utcnow().isoformat()}
@router_leadership_military.get("")
async def i_leadership_military():
    return {"p":"saude_mental_mi_leadership_military","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mTBI_military.get("")
async def i_mTBI_military():
    return {"p":"saude_mental_mi_mTBI_military","s":"ativo","t":datetime.utcnow().isoformat()}
@router_make_the_connection.get("")
async def i_make_the_connection():
    return {"p":"saude_mental_mi_make_the_connection","s":"ativo","t":datetime.utcnow().isoformat()}
@router_master_resilience.get("")
async def i_master_resilience():
    return {"p":"saude_mental_mi_master_resilience","s":"ativo","t":datetime.utcnow().isoformat()}
@router_means_restriction_ve.get("")
async def i_means_restriction_ve():
    return {"p":"saude_mental_mi_means_restriction_ve","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mental_toughness_mil.get("")
async def i_mental_toughness_mil():
    return {"p":"saude_mental_mi_mental_toughness_mil","s":"ativo","t":datetime.utcnow().isoformat()}
@router_military_child.get("")
async def i_military_child():
    return {"p":"saude_mental_mi_military_child","s":"ativo","t":datetime.utcnow().isoformat()}
@router_military_culture.get("")
async def i_military_culture():
    return {"p":"saude_mental_mi_military_culture","s":"ativo","t":datetime.utcnow().isoformat()}
@router_military_history_tak.get("")
async def i_military_history_tak():
    return {"p":"saude_mental_mi_military_history_tak","s":"ativo","t":datetime.utcnow().isoformat()}
@router_military_informed_ca.get("")
async def i_military_informed_ca():
    return {"p":"saude_mental_mi_military_informed_ca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_military_psychology.get("")
async def i_military_psychology():
    return {"p":"saude_mental_mi_military_psychology","s":"ativo","t":datetime.utcnow().isoformat()}
@router_military_sexual_trau.get("")
async def i_military_sexual_trau():
    return {"p":"saude_mental_mi_military_sexual_trau","s":"ativo","t":datetime.utcnow().isoformat()}
@router_moral_injury_militar.get("")
async def i_moral_injury_militar():
    return {"p":"saude_mental_mi_moral_injury_militar","s":"ativo","t":datetime.utcnow().isoformat()}
@router_operational_psycholo.get("")
async def i_operational_psycholo():
    return {"p":"saude_mental_mi_operational_psycholo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_peer_support_veteran.get("")
async def i_peer_support_veteran():
    return {"p":"saude_mental_mi_peer_support_veteran","s":"ativo","t":datetime.utcnow().isoformat()}
@router_perpetration_militar.get("")
async def i_perpetration_militar():
    return {"p":"saude_mental_mi_perpetration_militar","s":"ativo","t":datetime.utcnow().isoformat()}
@router_post_deployment.get("")
async def i_post_deployment():
    return {"p":"saude_mental_mi_post_deployment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pre_deployment.get("")
async def i_pre_deployment():
    return {"p":"saude_mental_mi_pre_deployment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ptsd_military.get("")
async def i_ptsd_military():
    return {"p":"saude_mental_mi_ptsd_military","s":"ativo","t":datetime.utcnow().isoformat()}
@router_real_warriors.get("")
async def i_real_warriors():
    return {"p":"saude_mental_mi_real_warriors","s":"ativo","t":datetime.utcnow().isoformat()}
@router_recharge_military.get("")
async def i_recharge_military():
    return {"p":"saude_mental_mi_recharge_military","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reintegration_milita.get("")
async def i_reintegration_milita():
    return {"p":"saude_mental_mi_reintegration_milita","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reporting_military.get("")
async def i_reporting_military():
    return {"p":"saude_mental_mi_reporting_military","s":"ativo","t":datetime.utcnow().isoformat()}
@router_resilience_training_.get("")
async def i_resilience_training_():
    return {"p":"saude_mental_mi_resilience_training_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_resilient_military_k.get("")
async def i_resilient_military_k():
    return {"p":"saude_mental_mi_resilient_military_k","s":"ativo","t":datetime.utcnow().isoformat()}
@router_retaliation_military.get("")
async def i_retaliation_military():
    return {"p":"saude_mental_mi_retaliation_military","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reunion_military.get("")
async def i_reunion_military():
    return {"p":"saude_mental_mi_reunion_military","s":"ativo","t":datetime.utcnow().isoformat()}
@router_special_needs_milita.get("")
async def i_special_needs_milita():
    return {"p":"saude_mental_mi_special_needs_milita","s":"ativo","t":datetime.utcnow().isoformat()}
@router_spiritual_injury_mil.get("")
async def i_spiritual_injury_mil():
    return {"p":"saude_mental_mi_spiritual_injury_mil","s":"ativo","t":datetime.utcnow().isoformat()}
@router_stigma_military.get("")
async def i_stigma_military():
    return {"p":"saude_mental_mi_stigma_military","s":"ativo","t":datetime.utcnow().isoformat()}
@router_substance_abuse_vete.get("")
async def i_substance_abuse_vete():
    return {"p":"saude_mental_mi_substance_abuse_vete","s":"ativo","t":datetime.utcnow().isoformat()}
@router_suicide_military.get("")
async def i_suicide_military():
    return {"p":"saude_mental_mi_suicide_military","s":"ativo","t":datetime.utcnow().isoformat()}
@router_suicide_prevention_m.get("")
async def i_suicide_prevention_m():
    return {"p":"saude_mental_mi_suicide_prevention_m","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tactical_breathing_m.get("")
async def i_tactical_breathing_m():
    return {"p":"saude_mental_mi_tactical_breathing_m","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tbi_military.get("")
async def i_tbi_military():
    return {"p":"saude_mental_mi_tbi_military","s":"ativo","t":datetime.utcnow().isoformat()}
@router_team_building_milita.get("")
async def i_team_building_milita():
    return {"p":"saude_mental_mi_team_building_milita","s":"ativo","t":datetime.utcnow().isoformat()}
@router_telehealth_veterans.get("")
async def i_telehealth_veterans():
    return {"p":"saude_mental_mi_telehealth_veterans","s":"ativo","t":datetime.utcnow().isoformat()}
@router_transition_civilian.get("")
async def i_transition_civilian():
    return {"p":"saude_mental_mi_transition_civilian","s":"ativo","t":datetime.utcnow().isoformat()}
@router_traumatic_exposure_m.get("")
async def i_traumatic_exposure_m():
    return {"p":"saude_mental_mi_traumatic_exposure_m","s":"ativo","t":datetime.utcnow().isoformat()}
@router_unit_cohesion.get("")
async def i_unit_cohesion():
    return {"p":"saude_mental_mi_unit_cohesion","s":"ativo","t":datetime.utcnow().isoformat()}
@router_vet_center.get("")
async def i_vet_center():
    return {"p":"saude_mental_mi_vet_center","s":"ativo","t":datetime.utcnow().isoformat()}
@router_vet_to_vet.get("")
async def i_vet_to_vet():
    return {"p":"saude_mental_mi_vet_to_vet","s":"ativo","t":datetime.utcnow().isoformat()}
@router_veteran_mental_healt.get("")
async def i_veteran_mental_healt():
    return {"p":"saude_mental_mi_veteran_mental_healt","s":"ativo","t":datetime.utcnow().isoformat()}
@router_veteran_service_orga.get("")
async def i_veteran_service_orga():
    return {"p":"saude_mental_mi_veteran_service_orga","s":"ativo","t":datetime.utcnow().isoformat()}
@router_veteran_suicide.get("")
async def i_veteran_suicide():
    return {"p":"saude_mental_mi_veteran_suicide","s":"ativo","t":datetime.utcnow().isoformat()}
@router_warrior_ethos.get("")
async def i_warrior_ethos():
    return {"p":"saude_mental_mi_warrior_ethos","s":"ativo","t":datetime.utcnow().isoformat()}
@router_witnessing_military.get("")
async def i_witnessing_military():
    return {"p":"saude_mental_mi_witnessing_military","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_saude_mental_militar(PluginBase):
    name = "consolidated_saude_mental_militar"
    def setup(self, app):
        app.include_router(router_CTE_military)
        app.include_router(router_DCoE_resources)
        app.include_router(router_EFMP_military)
        app.include_router(router_MST_military)
        app.include_router(router_VA_mental_health)
        app.include_router(router_assault_military)
        app.include_router(router_attention_control_mi)
        app.include_router(router_betrayal_military)
        app.include_router(router_blast_injury)
        app.include_router(router_caregiver_military)
        app.include_router(router_chronic_traumatic_en)
        app.include_router(router_civilian_culture_adj)
        app.include_router(router_combat_exposure)
        app.include_router(router_combat_psychology)
        app.include_router(router_community_provider_m)
        app.include_router(router_comprehensive_soldie)
        app.include_router(router_concussion_military)
        app.include_router(router_cultural_competence_)
        app.include_router(router_deployment_child)
        app.include_router(router_deployment_phase)
        app.include_router(router_deployment_psycholog)
        app.include_router(router_education_military_c)
        app.include_router(router_employment_veterans)
        app.include_router(router_energy_management_mi)
        app.include_router(router_esprit_de_corps)
        app.include_router(router_family_reintegration)
        app.include_router(router_family_veteran_menta)
        app.include_router(router_goal_setting_militar)
        app.include_router(router_gun_access_veterans)
        app.include_router(router_harassment_military)
        app.include_router(router_help_seeking_militar)
        app.include_router(router_homecoming_mental)
        app.include_router(router_homelessness_veteran)
        app.include_router(router_identity_transition_)
        app.include_router(router_incarceration_vetera)
        app.include_router(router_invisible_wounds)
        app.include_router(router_leadership_military)
        app.include_router(router_mTBI_military)
        app.include_router(router_make_the_connection)
        app.include_router(router_master_resilience)
        app.include_router(router_means_restriction_ve)
        app.include_router(router_mental_toughness_mil)
        app.include_router(router_military_child)
        app.include_router(router_military_culture)
        app.include_router(router_military_history_tak)
        app.include_router(router_military_informed_ca)
        app.include_router(router_military_psychology)
        app.include_router(router_military_sexual_trau)
        app.include_router(router_moral_injury_militar)
        app.include_router(router_operational_psycholo)
        app.include_router(router_peer_support_veteran)
        app.include_router(router_perpetration_militar)
        app.include_router(router_post_deployment)
        app.include_router(router_pre_deployment)
        app.include_router(router_ptsd_military)
        app.include_router(router_real_warriors)
        app.include_router(router_recharge_military)
        app.include_router(router_reintegration_milita)
        app.include_router(router_reporting_military)
        app.include_router(router_resilience_training_)
        app.include_router(router_resilient_military_k)
        app.include_router(router_retaliation_military)
        app.include_router(router_reunion_military)
        app.include_router(router_special_needs_milita)
        app.include_router(router_spiritual_injury_mil)
        app.include_router(router_stigma_military)
        app.include_router(router_substance_abuse_vete)
        app.include_router(router_suicide_military)
        app.include_router(router_suicide_prevention_m)
        app.include_router(router_tactical_breathing_m)
        app.include_router(router_tbi_military)
        app.include_router(router_team_building_milita)
        app.include_router(router_telehealth_veterans)
        app.include_router(router_transition_civilian)
        app.include_router(router_traumatic_exposure_m)
        app.include_router(router_unit_cohesion)
        app.include_router(router_vet_center)
        app.include_router(router_vet_to_vet)
        app.include_router(router_veteran_mental_healt)
        app.include_router(router_veteran_service_orga)
        app.include_router(router_veteran_suicide)
        app.include_router(router_warrior_ethos)
        app.include_router(router_witnessing_military)


plugin = Plugin_saude_mental_militar()
