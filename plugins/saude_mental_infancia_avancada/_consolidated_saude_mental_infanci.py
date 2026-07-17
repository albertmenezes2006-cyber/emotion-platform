from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_CARE_program = APIRouter(prefix="/api/v1/saude_mental/CARE_program", tags=["saude_mental_infancia_avancada"])
router_COS_circle_security = APIRouter(prefix="/api/v1/saude_mental/COS_circle_security", tags=["saude_mental_infancia_avancada"])
router_DCSM_infant = APIRouter(prefix="/api/v1/saude_mental/DCSM_infant", tags=["saude_mental_infancia_avancada"])
router_DC_0_5_classificatio = APIRouter(prefix="/api/v1/saude_mental/DC_0_5_classification", tags=["saude_mental_infancia_avancada"])
router_PCIT2 = APIRouter(prefix="/api/v1/saude_mental/PCIT2", tags=["saude_mental_infancia_avancada"])
router_adverse_childhood_ex = APIRouter(prefix="/api/v1/saude_mental/adverse_childhood_experie", tags=["saude_mental_infancia_avancada"])
router_animal_child_mental = APIRouter(prefix="/api/v1/saude_mental/animal_child_mental", tags=["saude_mental_infancia_avancada"])
router_child_centered_play = APIRouter(prefix="/api/v1/saude_mental/child_centered_play", tags=["saude_mental_infancia_avancada"])
router_community_resilience = APIRouter(prefix="/api/v1/saude_mental/community_resilience", tags=["saude_mental_infancia_avancada"])
router_competition_developm = APIRouter(prefix="/api/v1/saude_mental/competition_development", tags=["saude_mental_infancia_avancada"])
router_complex_trauma_child = APIRouter(prefix="/api/v1/saude_mental/complex_trauma_child", tags=["saude_mental_infancia_avancada"])
router_constructive_play = APIRouter(prefix="/api/v1/saude_mental/constructive_play", tags=["saude_mental_infancia_avancada"])
router_cooperative_play = APIRouter(prefix="/api/v1/saude_mental/cooperative_play", tags=["saude_mental_infancia_avancada"])
router_cps_collaborative = APIRouter(prefix="/api/v1/saude_mental/cps_collaborative", tags=["saude_mental_infancia_avancada"])
router_cultural_resilience = APIRouter(prefix="/api/v1/saude_mental/cultural_resilience", tags=["saude_mental_infancia_avancada"])
router_cumulative_risk = APIRouter(prefix="/api/v1/saude_mental/cumulative_risk", tags=["saude_mental_infancia_avancada"])
router_cyberbullying_child = APIRouter(prefix="/api/v1/saude_mental/cyberbullying_child", tags=["saude_mental_infancia_avancada"])
router_developmental_psycho = APIRouter(prefix="/api/v1/saude_mental/developmental_psychopatho", tags=["saude_mental_infancia_avancada"])
router_developmental_trauma = APIRouter(prefix="/api/v1/saude_mental/developmental_trauma", tags=["saude_mental_infancia_avancada"])
router_directive_play = APIRouter(prefix="/api/v1/saude_mental/directive_play", tags=["saude_mental_infancia_avancada"])
router_dosage_risk = APIRouter(prefix="/api/v1/saude_mental/dosage_risk", tags=["saude_mental_infancia_avancada"])
router_dramatic_play = APIRouter(prefix="/api/v1/saude_mental/dramatic_play", tags=["saude_mental_infancia_avancada"])
router_dyadic_therapy = APIRouter(prefix="/api/v1/saude_mental/dyadic_therapy", tags=["saude_mental_infancia_avancada"])
router_early_adversity = APIRouter(prefix="/api/v1/saude_mental/early_adversity", tags=["saude_mental_infancia_avancada"])
router_early_childhood_educ = APIRouter(prefix="/api/v1/saude_mental/early_childhood_education", tags=["saude_mental_infancia_avancada"])
router_early_childhood_ment = APIRouter(prefix="/api/v1/saude_mental/early_childhood_mental", tags=["saude_mental_infancia_avancada"])
router_early_head_start = APIRouter(prefix="/api/v1/saude_mental/early_head_start", tags=["saude_mental_infancia_avancada"])
router_early_intervention = APIRouter(prefix="/api/v1/saude_mental/early_intervention", tags=["saude_mental_infancia_avancada"])
router_early_life_stress = APIRouter(prefix="/api/v1/saude_mental/early_life_stress", tags=["saude_mental_infancia_avancada"])
router_emotion_knowledge = APIRouter(prefix="/api/v1/saude_mental/emotion_knowledge", tags=["saude_mental_infancia_avancada"])
router_emotion_understandin = APIRouter(prefix="/api/v1/saude_mental/emotion_understanding", tags=["saude_mental_infancia_avancada"])
router_epigenetics_early = APIRouter(prefix="/api/v1/saude_mental/epigenetics_early", tags=["saude_mental_infancia_avancada"])
router_equifinality = APIRouter(prefix="/api/v1/saude_mental/equifinality", tags=["saude_mental_infancia_avancada"])
router_executive_function_d = APIRouter(prefix="/api/v1/saude_mental/executive_function_develo", tags=["saude_mental_infancia_avancada"])
router_fair_play = APIRouter(prefix="/api/v1/saude_mental/fair_play", tags=["saude_mental_infancia_avancada"])
router_family_resilience = APIRouter(prefix="/api/v1/saude_mental/family_resilience", tags=["saude_mental_infancia_avancada"])
router_fantasy_play = APIRouter(prefix="/api/v1/saude_mental/fantasy_play", tags=["saude_mental_infancia_avancada"])
router_filial_therapy2 = APIRouter(prefix="/api/v1/saude_mental/filial_therapy2", tags=["saude_mental_infancia_avancada"])
router_friendship_child = APIRouter(prefix="/api/v1/saude_mental/friendship_child", tags=["saude_mental_infancia_avancada"])
router_games_rules = APIRouter(prefix="/api/v1/saude_mental/games_rules", tags=["saude_mental_infancia_avancada"])
router_gaming_child = APIRouter(prefix="/api/v1/saude_mental/gaming_child", tags=["saude_mental_infancia_avancada"])
router_head_start = APIRouter(prefix="/api/v1/saude_mental/head_start", tags=["saude_mental_infancia_avancada"])
router_healthy_families = APIRouter(prefix="/api/v1/saude_mental/healthy_families", tags=["saude_mental_infancia_avancada"])
router_home_visiting = APIRouter(prefix="/api/v1/saude_mental/home_visiting", tags=["saude_mental_infancia_avancada"])
router_incredible_years2 = APIRouter(prefix="/api/v1/saude_mental/incredible_years2", tags=["saude_mental_infancia_avancada"])
router_infancia_precoce_men = APIRouter(prefix="/api/v1/saude_mental/infancia_precoce_mental", tags=["saude_mental_infancia_avancada"])
router_infant_mental_health = APIRouter(prefix="/api/v1/saude_mental/infant_mental_health", tags=["saude_mental_infancia_avancada"])
router_interaction_guidance = APIRouter(prefix="/api/v1/saude_mental/interaction_guidance", tags=["saude_mental_infancia_avancada"])
router_kindergarten_readine = APIRouter(prefix="/api/v1/saude_mental/kindergarten_readiness", tags=["saude_mental_infancia_avancada"])
router_losing_gracefully = APIRouter(prefix="/api/v1/saude_mental/losing_gracefully", tags=["saude_mental_infancia_avancada"])
router_media_use_child = APIRouter(prefix="/api/v1/saude_mental/media_use_child", tags=["saude_mental_infancia_avancada"])
router_multifinality = APIRouter(prefix="/api/v1/saude_mental/multifinality", tags=["saude_mental_infancia_avancada"])
router_nature_child = APIRouter(prefix="/api/v1/saude_mental/nature_child", tags=["saude_mental_infancia_avancada"])
router_non_directive_play = APIRouter(prefix="/api/v1/saude_mental/non_directive_play", tags=["saude_mental_infancia_avancada"])
router_nurse_family_partner = APIRouter(prefix="/api/v1/saude_mental/nurse_family_partnership", tags=["saude_mental_infancia_avancada"])
router_nutrition_child_ment = APIRouter(prefix="/api/v1/saude_mental/nutrition_child_mental2", tags=["saude_mental_infancia_avancada"])
router_online_safety_child = APIRouter(prefix="/api/v1/saude_mental/online_safety_child", tags=["saude_mental_infancia_avancada"])
router_outdoor_play = APIRouter(prefix="/api/v1/saude_mental/outdoor_play", tags=["saude_mental_infancia_avancada"])
router_parent_child_therapy = APIRouter(prefix="/api/v1/saude_mental/parent_child_therapy", tags=["saude_mental_infancia_avancada"])
router_parents_as_teachers = APIRouter(prefix="/api/v1/saude_mental/parents_as_teachers", tags=["saude_mental_infancia_avancada"])
router_peer_relationships_d = APIRouter(prefix="/api/v1/saude_mental/peer_relationships_develo", tags=["saude_mental_infancia_avancada"])
router_perspective_taking_d = APIRouter(prefix="/api/v1/saude_mental/perspective_taking_develo", tags=["saude_mental_infancia_avancada"])
router_pet_child_mental = APIRouter(prefix="/api/v1/saude_mental/pet_child_mental", tags=["saude_mental_infancia_avancada"])
router_physical_activity_ch = APIRouter(prefix="/api/v1/saude_mental/physical_activity_child", tags=["saude_mental_infancia_avancada"])
router_play_development = APIRouter(prefix="/api/v1/saude_mental/play_development", tags=["saude_mental_infancia_avancada"])
router_play_therapy2 = APIRouter(prefix="/api/v1/saude_mental/play_therapy2", tags=["saude_mental_infancia_avancada"])
router_prenatal_stress = APIRouter(prefix="/api/v1/saude_mental/prenatal_stress", tags=["saude_mental_infancia_avancada"])
router_preschool_mental_hea = APIRouter(prefix="/api/v1/saude_mental/preschool_mental_health", tags=["saude_mental_infancia_avancada"])
router_protective_factors_c = APIRouter(prefix="/api/v1/saude_mental/protective_factors_child", tags=["saude_mental_infancia_avancada"])
router_relational_disorders = APIRouter(prefix="/api/v1/saude_mental/relational_disorders", tags=["saude_mental_infancia_avancada"])
router_risk_resilience_chil = APIRouter(prefix="/api/v1/saude_mental/risk_resilience_child", tags=["saude_mental_infancia_avancada"])
router_rough_tumble_play = APIRouter(prefix="/api/v1/saude_mental/rough_tumble_play", tags=["saude_mental_infancia_avancada"])
router_school_readiness_men = APIRouter(prefix="/api/v1/saude_mental/school_readiness_mental", tags=["saude_mental_infancia_avancada"])
router_screen_time_child = APIRouter(prefix="/api/v1/saude_mental/screen_time_child", tags=["saude_mental_infancia_avancada"])
router_self_regulation_deve = APIRouter(prefix="/api/v1/saude_mental/self_regulation_developme", tags=["saude_mental_infancia_avancada"])
router_sensory_play = APIRouter(prefix="/api/v1/saude_mental/sensory_play", tags=["saude_mental_infancia_avancada"])
router_sleep_child_mental2 = APIRouter(prefix="/api/v1/saude_mental/sleep_child_mental2", tags=["saude_mental_infancia_avancada"])
router_social_competence_de = APIRouter(prefix="/api/v1/saude_mental/social_competence_develop", tags=["saude_mental_infancia_avancada"])
router_social_media_child = APIRouter(prefix="/api/v1/saude_mental/social_media_child", tags=["saude_mental_infancia_avancada"])
router_social_support_child = APIRouter(prefix="/api/v1/saude_mental/social_support_child", tags=["saude_mental_infancia_avancada"])
router_sports_development = APIRouter(prefix="/api/v1/saude_mental/sports_development", tags=["saude_mental_infancia_avancada"])
router_sportsmanship_develo = APIRouter(prefix="/api/v1/saude_mental/sportsmanship_development", tags=["saude_mental_infancia_avancada"])
router_symbolic_play = APIRouter(prefix="/api/v1/saude_mental/symbolic_play", tags=["saude_mental_infancia_avancada"])
router_technology_child = APIRouter(prefix="/api/v1/saude_mental/technology_child", tags=["saude_mental_infancia_avancada"])
router_theory_mind_developm = APIRouter(prefix="/api/v1/saude_mental/theory_mind_development", tags=["saude_mental_infancia_avancada"])
router_theraplay = APIRouter(prefix="/api/v1/saude_mental/theraplay", tags=["saude_mental_infancia_avancada"])
router_triple_p_advanced = APIRouter(prefix="/api/v1/saude_mental/triple_p_advanced", tags=["saude_mental_infancia_avancada"])
router_video_feedback = APIRouter(prefix="/api/v1/saude_mental/video_feedback", tags=["saude_mental_infancia_avancada"])
router_winning_gracefully = APIRouter(prefix="/api/v1/saude_mental/winning_gracefully", tags=["saude_mental_infancia_avancada"])
router_zero_three_mental = APIRouter(prefix="/api/v1/saude_mental/zero_three_mental", tags=["saude_mental_infancia_avancada"])
router_zero_to_three = APIRouter(prefix="/api/v1/saude_mental/zero_to_three", tags=["saude_mental_infancia_avancada"])

@router_CARE_program.get("")
async def i_CARE_program():
    return {"p":"saude_mental_in_CARE_program","s":"ativo","t":datetime.utcnow().isoformat()}
@router_COS_circle_security.get("")
async def i_COS_circle_security():
    return {"p":"saude_mental_in_COS_circle_security","s":"ativo","t":datetime.utcnow().isoformat()}
@router_DCSM_infant.get("")
async def i_DCSM_infant():
    return {"p":"saude_mental_in_DCSM_infant","s":"ativo","t":datetime.utcnow().isoformat()}
@router_DC_0_5_classificatio.get("")
async def i_DC_0_5_classificatio():
    return {"p":"saude_mental_in_DC_0_5_classificatio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_PCIT2.get("")
async def i_PCIT2():
    return {"p":"saude_mental_in_PCIT2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_adverse_childhood_ex.get("")
async def i_adverse_childhood_ex():
    return {"p":"saude_mental_in_adverse_childhood_ex","s":"ativo","t":datetime.utcnow().isoformat()}
@router_animal_child_mental.get("")
async def i_animal_child_mental():
    return {"p":"saude_mental_in_animal_child_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_child_centered_play.get("")
async def i_child_centered_play():
    return {"p":"saude_mental_in_child_centered_play","s":"ativo","t":datetime.utcnow().isoformat()}
@router_community_resilience.get("")
async def i_community_resilience():
    return {"p":"saude_mental_in_community_resilience","s":"ativo","t":datetime.utcnow().isoformat()}
@router_competition_developm.get("")
async def i_competition_developm():
    return {"p":"saude_mental_in_competition_developm","s":"ativo","t":datetime.utcnow().isoformat()}
@router_complex_trauma_child.get("")
async def i_complex_trauma_child():
    return {"p":"saude_mental_in_complex_trauma_child","s":"ativo","t":datetime.utcnow().isoformat()}
@router_constructive_play.get("")
async def i_constructive_play():
    return {"p":"saude_mental_in_constructive_play","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cooperative_play.get("")
async def i_cooperative_play():
    return {"p":"saude_mental_in_cooperative_play","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cps_collaborative.get("")
async def i_cps_collaborative():
    return {"p":"saude_mental_in_cps_collaborative","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cultural_resilience.get("")
async def i_cultural_resilience():
    return {"p":"saude_mental_in_cultural_resilience","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cumulative_risk.get("")
async def i_cumulative_risk():
    return {"p":"saude_mental_in_cumulative_risk","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cyberbullying_child.get("")
async def i_cyberbullying_child():
    return {"p":"saude_mental_in_cyberbullying_child","s":"ativo","t":datetime.utcnow().isoformat()}
@router_developmental_psycho.get("")
async def i_developmental_psycho():
    return {"p":"saude_mental_in_developmental_psycho","s":"ativo","t":datetime.utcnow().isoformat()}
@router_developmental_trauma.get("")
async def i_developmental_trauma():
    return {"p":"saude_mental_in_developmental_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_directive_play.get("")
async def i_directive_play():
    return {"p":"saude_mental_in_directive_play","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dosage_risk.get("")
async def i_dosage_risk():
    return {"p":"saude_mental_in_dosage_risk","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dramatic_play.get("")
async def i_dramatic_play():
    return {"p":"saude_mental_in_dramatic_play","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dyadic_therapy.get("")
async def i_dyadic_therapy():
    return {"p":"saude_mental_in_dyadic_therapy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_early_adversity.get("")
async def i_early_adversity():
    return {"p":"saude_mental_in_early_adversity","s":"ativo","t":datetime.utcnow().isoformat()}
@router_early_childhood_educ.get("")
async def i_early_childhood_educ():
    return {"p":"saude_mental_in_early_childhood_educ","s":"ativo","t":datetime.utcnow().isoformat()}
@router_early_childhood_ment.get("")
async def i_early_childhood_ment():
    return {"p":"saude_mental_in_early_childhood_ment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_early_head_start.get("")
async def i_early_head_start():
    return {"p":"saude_mental_in_early_head_start","s":"ativo","t":datetime.utcnow().isoformat()}
@router_early_intervention.get("")
async def i_early_intervention():
    return {"p":"saude_mental_in_early_intervention","s":"ativo","t":datetime.utcnow().isoformat()}
@router_early_life_stress.get("")
async def i_early_life_stress():
    return {"p":"saude_mental_in_early_life_stress","s":"ativo","t":datetime.utcnow().isoformat()}
@router_emotion_knowledge.get("")
async def i_emotion_knowledge():
    return {"p":"saude_mental_in_emotion_knowledge","s":"ativo","t":datetime.utcnow().isoformat()}
@router_emotion_understandin.get("")
async def i_emotion_understandin():
    return {"p":"saude_mental_in_emotion_understandin","s":"ativo","t":datetime.utcnow().isoformat()}
@router_epigenetics_early.get("")
async def i_epigenetics_early():
    return {"p":"saude_mental_in_epigenetics_early","s":"ativo","t":datetime.utcnow().isoformat()}
@router_equifinality.get("")
async def i_equifinality():
    return {"p":"saude_mental_in_equifinality","s":"ativo","t":datetime.utcnow().isoformat()}
@router_executive_function_d.get("")
async def i_executive_function_d():
    return {"p":"saude_mental_in_executive_function_d","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fair_play.get("")
async def i_fair_play():
    return {"p":"saude_mental_in_fair_play","s":"ativo","t":datetime.utcnow().isoformat()}
@router_family_resilience.get("")
async def i_family_resilience():
    return {"p":"saude_mental_in_family_resilience","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fantasy_play.get("")
async def i_fantasy_play():
    return {"p":"saude_mental_in_fantasy_play","s":"ativo","t":datetime.utcnow().isoformat()}
@router_filial_therapy2.get("")
async def i_filial_therapy2():
    return {"p":"saude_mental_in_filial_therapy2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_friendship_child.get("")
async def i_friendship_child():
    return {"p":"saude_mental_in_friendship_child","s":"ativo","t":datetime.utcnow().isoformat()}
@router_games_rules.get("")
async def i_games_rules():
    return {"p":"saude_mental_in_games_rules","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gaming_child.get("")
async def i_gaming_child():
    return {"p":"saude_mental_in_gaming_child","s":"ativo","t":datetime.utcnow().isoformat()}
@router_head_start.get("")
async def i_head_start():
    return {"p":"saude_mental_in_head_start","s":"ativo","t":datetime.utcnow().isoformat()}
@router_healthy_families.get("")
async def i_healthy_families():
    return {"p":"saude_mental_in_healthy_families","s":"ativo","t":datetime.utcnow().isoformat()}
@router_home_visiting.get("")
async def i_home_visiting():
    return {"p":"saude_mental_in_home_visiting","s":"ativo","t":datetime.utcnow().isoformat()}
@router_incredible_years2.get("")
async def i_incredible_years2():
    return {"p":"saude_mental_in_incredible_years2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_infancia_precoce_men.get("")
async def i_infancia_precoce_men():
    return {"p":"saude_mental_in_infancia_precoce_men","s":"ativo","t":datetime.utcnow().isoformat()}
@router_infant_mental_health.get("")
async def i_infant_mental_health():
    return {"p":"saude_mental_in_infant_mental_health","s":"ativo","t":datetime.utcnow().isoformat()}
@router_interaction_guidance.get("")
async def i_interaction_guidance():
    return {"p":"saude_mental_in_interaction_guidance","s":"ativo","t":datetime.utcnow().isoformat()}
@router_kindergarten_readine.get("")
async def i_kindergarten_readine():
    return {"p":"saude_mental_in_kindergarten_readine","s":"ativo","t":datetime.utcnow().isoformat()}
@router_losing_gracefully.get("")
async def i_losing_gracefully():
    return {"p":"saude_mental_in_losing_gracefully","s":"ativo","t":datetime.utcnow().isoformat()}
@router_media_use_child.get("")
async def i_media_use_child():
    return {"p":"saude_mental_in_media_use_child","s":"ativo","t":datetime.utcnow().isoformat()}
@router_multifinality.get("")
async def i_multifinality():
    return {"p":"saude_mental_in_multifinality","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nature_child.get("")
async def i_nature_child():
    return {"p":"saude_mental_in_nature_child","s":"ativo","t":datetime.utcnow().isoformat()}
@router_non_directive_play.get("")
async def i_non_directive_play():
    return {"p":"saude_mental_in_non_directive_play","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nurse_family_partner.get("")
async def i_nurse_family_partner():
    return {"p":"saude_mental_in_nurse_family_partner","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nutrition_child_ment.get("")
async def i_nutrition_child_ment():
    return {"p":"saude_mental_in_nutrition_child_ment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_online_safety_child.get("")
async def i_online_safety_child():
    return {"p":"saude_mental_in_online_safety_child","s":"ativo","t":datetime.utcnow().isoformat()}
@router_outdoor_play.get("")
async def i_outdoor_play():
    return {"p":"saude_mental_in_outdoor_play","s":"ativo","t":datetime.utcnow().isoformat()}
@router_parent_child_therapy.get("")
async def i_parent_child_therapy():
    return {"p":"saude_mental_in_parent_child_therapy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_parents_as_teachers.get("")
async def i_parents_as_teachers():
    return {"p":"saude_mental_in_parents_as_teachers","s":"ativo","t":datetime.utcnow().isoformat()}
@router_peer_relationships_d.get("")
async def i_peer_relationships_d():
    return {"p":"saude_mental_in_peer_relationships_d","s":"ativo","t":datetime.utcnow().isoformat()}
@router_perspective_taking_d.get("")
async def i_perspective_taking_d():
    return {"p":"saude_mental_in_perspective_taking_d","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pet_child_mental.get("")
async def i_pet_child_mental():
    return {"p":"saude_mental_in_pet_child_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_physical_activity_ch.get("")
async def i_physical_activity_ch():
    return {"p":"saude_mental_in_physical_activity_ch","s":"ativo","t":datetime.utcnow().isoformat()}
@router_play_development.get("")
async def i_play_development():
    return {"p":"saude_mental_in_play_development","s":"ativo","t":datetime.utcnow().isoformat()}
@router_play_therapy2.get("")
async def i_play_therapy2():
    return {"p":"saude_mental_in_play_therapy2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_prenatal_stress.get("")
async def i_prenatal_stress():
    return {"p":"saude_mental_in_prenatal_stress","s":"ativo","t":datetime.utcnow().isoformat()}
@router_preschool_mental_hea.get("")
async def i_preschool_mental_hea():
    return {"p":"saude_mental_in_preschool_mental_hea","s":"ativo","t":datetime.utcnow().isoformat()}
@router_protective_factors_c.get("")
async def i_protective_factors_c():
    return {"p":"saude_mental_in_protective_factors_c","s":"ativo","t":datetime.utcnow().isoformat()}
@router_relational_disorders.get("")
async def i_relational_disorders():
    return {"p":"saude_mental_in_relational_disorders","s":"ativo","t":datetime.utcnow().isoformat()}
@router_risk_resilience_chil.get("")
async def i_risk_resilience_chil():
    return {"p":"saude_mental_in_risk_resilience_chil","s":"ativo","t":datetime.utcnow().isoformat()}
@router_rough_tumble_play.get("")
async def i_rough_tumble_play():
    return {"p":"saude_mental_in_rough_tumble_play","s":"ativo","t":datetime.utcnow().isoformat()}
@router_school_readiness_men.get("")
async def i_school_readiness_men():
    return {"p":"saude_mental_in_school_readiness_men","s":"ativo","t":datetime.utcnow().isoformat()}
@router_screen_time_child.get("")
async def i_screen_time_child():
    return {"p":"saude_mental_in_screen_time_child","s":"ativo","t":datetime.utcnow().isoformat()}
@router_self_regulation_deve.get("")
async def i_self_regulation_deve():
    return {"p":"saude_mental_in_self_regulation_deve","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sensory_play.get("")
async def i_sensory_play():
    return {"p":"saude_mental_in_sensory_play","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sleep_child_mental2.get("")
async def i_sleep_child_mental2():
    return {"p":"saude_mental_in_sleep_child_mental2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_social_competence_de.get("")
async def i_social_competence_de():
    return {"p":"saude_mental_in_social_competence_de","s":"ativo","t":datetime.utcnow().isoformat()}
@router_social_media_child.get("")
async def i_social_media_child():
    return {"p":"saude_mental_in_social_media_child","s":"ativo","t":datetime.utcnow().isoformat()}
@router_social_support_child.get("")
async def i_social_support_child():
    return {"p":"saude_mental_in_social_support_child","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sports_development.get("")
async def i_sports_development():
    return {"p":"saude_mental_in_sports_development","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sportsmanship_develo.get("")
async def i_sportsmanship_develo():
    return {"p":"saude_mental_in_sportsmanship_develo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_symbolic_play.get("")
async def i_symbolic_play():
    return {"p":"saude_mental_in_symbolic_play","s":"ativo","t":datetime.utcnow().isoformat()}
@router_technology_child.get("")
async def i_technology_child():
    return {"p":"saude_mental_in_technology_child","s":"ativo","t":datetime.utcnow().isoformat()}
@router_theory_mind_developm.get("")
async def i_theory_mind_developm():
    return {"p":"saude_mental_in_theory_mind_developm","s":"ativo","t":datetime.utcnow().isoformat()}
@router_theraplay.get("")
async def i_theraplay():
    return {"p":"saude_mental_in_theraplay","s":"ativo","t":datetime.utcnow().isoformat()}
@router_triple_p_advanced.get("")
async def i_triple_p_advanced():
    return {"p":"saude_mental_in_triple_p_advanced","s":"ativo","t":datetime.utcnow().isoformat()}
@router_video_feedback.get("")
async def i_video_feedback():
    return {"p":"saude_mental_in_video_feedback","s":"ativo","t":datetime.utcnow().isoformat()}
@router_winning_gracefully.get("")
async def i_winning_gracefully():
    return {"p":"saude_mental_in_winning_gracefully","s":"ativo","t":datetime.utcnow().isoformat()}
@router_zero_three_mental.get("")
async def i_zero_three_mental():
    return {"p":"saude_mental_in_zero_three_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_zero_to_three.get("")
async def i_zero_to_three():
    return {"p":"saude_mental_in_zero_to_three","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_saude_mental_infanci(PluginBase):
    name = "consolidated_saude_mental_infancia_avancada"
    def setup(self, app):
        app.include_router(router_CARE_program)
        app.include_router(router_COS_circle_security)
        app.include_router(router_DCSM_infant)
        app.include_router(router_DC_0_5_classificatio)
        app.include_router(router_PCIT2)
        app.include_router(router_adverse_childhood_ex)
        app.include_router(router_animal_child_mental)
        app.include_router(router_child_centered_play)
        app.include_router(router_community_resilience)
        app.include_router(router_competition_developm)
        app.include_router(router_complex_trauma_child)
        app.include_router(router_constructive_play)
        app.include_router(router_cooperative_play)
        app.include_router(router_cps_collaborative)
        app.include_router(router_cultural_resilience)
        app.include_router(router_cumulative_risk)
        app.include_router(router_cyberbullying_child)
        app.include_router(router_developmental_psycho)
        app.include_router(router_developmental_trauma)
        app.include_router(router_directive_play)
        app.include_router(router_dosage_risk)
        app.include_router(router_dramatic_play)
        app.include_router(router_dyadic_therapy)
        app.include_router(router_early_adversity)
        app.include_router(router_early_childhood_educ)
        app.include_router(router_early_childhood_ment)
        app.include_router(router_early_head_start)
        app.include_router(router_early_intervention)
        app.include_router(router_early_life_stress)
        app.include_router(router_emotion_knowledge)
        app.include_router(router_emotion_understandin)
        app.include_router(router_epigenetics_early)
        app.include_router(router_equifinality)
        app.include_router(router_executive_function_d)
        app.include_router(router_fair_play)
        app.include_router(router_family_resilience)
        app.include_router(router_fantasy_play)
        app.include_router(router_filial_therapy2)
        app.include_router(router_friendship_child)
        app.include_router(router_games_rules)
        app.include_router(router_gaming_child)
        app.include_router(router_head_start)
        app.include_router(router_healthy_families)
        app.include_router(router_home_visiting)
        app.include_router(router_incredible_years2)
        app.include_router(router_infancia_precoce_men)
        app.include_router(router_infant_mental_health)
        app.include_router(router_interaction_guidance)
        app.include_router(router_kindergarten_readine)
        app.include_router(router_losing_gracefully)
        app.include_router(router_media_use_child)
        app.include_router(router_multifinality)
        app.include_router(router_nature_child)
        app.include_router(router_non_directive_play)
        app.include_router(router_nurse_family_partner)
        app.include_router(router_nutrition_child_ment)
        app.include_router(router_online_safety_child)
        app.include_router(router_outdoor_play)
        app.include_router(router_parent_child_therapy)
        app.include_router(router_parents_as_teachers)
        app.include_router(router_peer_relationships_d)
        app.include_router(router_perspective_taking_d)
        app.include_router(router_pet_child_mental)
        app.include_router(router_physical_activity_ch)
        app.include_router(router_play_development)
        app.include_router(router_play_therapy2)
        app.include_router(router_prenatal_stress)
        app.include_router(router_preschool_mental_hea)
        app.include_router(router_protective_factors_c)
        app.include_router(router_relational_disorders)
        app.include_router(router_risk_resilience_chil)
        app.include_router(router_rough_tumble_play)
        app.include_router(router_school_readiness_men)
        app.include_router(router_screen_time_child)
        app.include_router(router_self_regulation_deve)
        app.include_router(router_sensory_play)
        app.include_router(router_sleep_child_mental2)
        app.include_router(router_social_competence_de)
        app.include_router(router_social_media_child)
        app.include_router(router_social_support_child)
        app.include_router(router_sports_development)
        app.include_router(router_sportsmanship_develo)
        app.include_router(router_symbolic_play)
        app.include_router(router_technology_child)
        app.include_router(router_theory_mind_developm)
        app.include_router(router_theraplay)
        app.include_router(router_triple_p_advanced)
        app.include_router(router_video_feedback)
        app.include_router(router_winning_gracefully)
        app.include_router(router_zero_three_mental)
        app.include_router(router_zero_to_three)


plugin = Plugin_saude_mental_infanci()
