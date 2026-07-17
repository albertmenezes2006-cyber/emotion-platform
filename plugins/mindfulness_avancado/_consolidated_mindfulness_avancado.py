from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_MSC_intensive = APIRouter(prefix="/api/v1/mindfulness_/MSC_intensive", tags=["mindfulness_avancado"])
router_MSC_online = APIRouter(prefix="/api/v1/mindfulness_/MSC_online", tags=["mindfulness_avancado"])
router_MSC_program = APIRouter(prefix="/api/v1/mindfulness_/MSC_program", tags=["mindfulness_avancado"])
router_NVC_mindful = APIRouter(prefix="/api/v1/mindfulness_/NVC_mindful", tags=["mindfulness_avancado"])
router_PLEASE_mindful = APIRouter(prefix="/api/v1/mindfulness_/PLEASE_mindful", tags=["mindfulness_avancado"])
router_RAIN_technique = APIRouter(prefix="/api/v1/mindfulness_/RAIN_technique", tags=["mindfulness_avancado"])
router_STOP_technique = APIRouter(prefix="/api/v1/mindfulness_/STOP_technique", tags=["mindfulness_avancado"])
router_TIPP_mindful = APIRouter(prefix="/api/v1/mindfulness_/TIPP_mindful", tags=["mindfulness_avancado"])
router_acceptance_commitmen = APIRouter(prefix="/api/v1/mindfulness_/acceptance_commitment_adv", tags=["mindfulness_avancado"])
router_active_listening2 = APIRouter(prefix="/api/v1/mindfulness_/active_listening2", tags=["mindfulness_avancado"])
router_beginner_mind = APIRouter(prefix="/api/v1/mindfulness_/beginner_mind", tags=["mindfulness_avancado"])
router_bodhicitta_practice = APIRouter(prefix="/api/v1/mindfulness_/bodhicitta_practice", tags=["mindfulness_avancado"])
router_brahmaviharas_practi = APIRouter(prefix="/api/v1/mindfulness_/brahmaviharas_practice", tags=["mindfulness_avancado"])
router_build_mastery_mindfu = APIRouter(prefix="/api/v1/mindfulness_/build_mastery_mindful", tags=["mindfulness_avancado"])
router_check_facts_mindful = APIRouter(prefix="/api/v1/mindfulness_/check_facts_mindful", tags=["mindfulness_avancado"])
router_cognitively_based_co = APIRouter(prefix="/api/v1/mindfulness_/cognitively_based_compass", tags=["mindfulness_avancado"])
router_common_humanity_prac = APIRouter(prefix="/api/v1/mindfulness_/common_humanity_practice", tags=["mindfulness_avancado"])
router_compassion_cultivati = APIRouter(prefix="/api/v1/mindfulness_/compassion_cultivation", tags=["mindfulness_avancado"])
router_compassion_fatigue_p = APIRouter(prefix="/api/v1/mindfulness_/compassion_fatigue_preven", tags=["mindfulness_avancado"])
router_compassion_focused_m = APIRouter(prefix="/api/v1/mindfulness_/compassion_focused_mindfu", tags=["mindfulness_avancado"])
router_compassion_meditatio = APIRouter(prefix="/api/v1/mindfulness_/compassion_meditation", tags=["mindfulness_avancado"])
router_conscious_communicat = APIRouter(prefix="/api/v1/mindfulness_/conscious_communication", tags=["mindfulness_avancado"])
router_cope_ahead_mindful = APIRouter(prefix="/api/v1/mindfulness_/cope_ahead_mindful", tags=["mindfulness_avancado"])
router_deep_listening = APIRouter(prefix="/api/v1/mindfulness_/deep_listening", tags=["mindfulness_avancado"])
router_describe_mindful = APIRouter(prefix="/api/v1/mindfulness_/describe_mindful", tags=["mindfulness_avancado"])
router_dialectical_behavior = APIRouter(prefix="/api/v1/mindfulness_/dialectical_behavior_mind", tags=["mindfulness_avancado"])
router_effective_mind = APIRouter(prefix="/api/v1/mindfulness_/effective_mind", tags=["mindfulness_avancado"])
router_emotion_mind2 = APIRouter(prefix="/api/v1/mindfulness_/emotion_mind2", tags=["mindfulness_avancado"])
router_empathic_listening = APIRouter(prefix="/api/v1/mindfulness_/empathic_listening", tags=["mindfulness_avancado"])
router_empathy_compassion = APIRouter(prefix="/api/v1/mindfulness_/empathy_compassion", tags=["mindfulness_avancado"])
router_equanimity_practice = APIRouter(prefix="/api/v1/mindfulness_/equanimity_practice", tags=["mindfulness_avancado"])
router_fierce_self_compassi = APIRouter(prefix="/api/v1/mindfulness_/fierce_self_compassion", tags=["mindfulness_avancado"])
router_flow_mindful = APIRouter(prefix="/api/v1/mindfulness_/flow_mindful", tags=["mindfulness_avancado"])
router_four_immeasurables = APIRouter(prefix="/api/v1/mindfulness_/four_immeasurables", tags=["mindfulness_avancado"])
router_informal_mindfulness = APIRouter(prefix="/api/v1/mindfulness_/informal_mindfulness", tags=["mindfulness_avancado"])
router_inner_critic_self_co = APIRouter(prefix="/api/v1/mindfulness_/inner_critic_self_compass", tags=["mindfulness_avancado"])
router_just_like_me = APIRouter(prefix="/api/v1/mindfulness_/just_like_me", tags=["mindfulness_avancado"])
router_karuna_compassion = APIRouter(prefix="/api/v1/mindfulness_/karuna_compassion", tags=["mindfulness_avancado"])
router_loving_kindness_adva = APIRouter(prefix="/api/v1/mindfulness_/loving_kindness_advanced", tags=["mindfulness_avancado"])
router_metta_tonglen_practi = APIRouter(prefix="/api/v1/mindfulness_/metta_tonglen_practice", tags=["mindfulness_avancado"])
router_mindful_aging = APIRouter(prefix="/api/v1/mindfulness_/mindful_aging", tags=["mindfulness_avancado"])
router_mindful_athletes = APIRouter(prefix="/api/v1/mindfulness_/mindful_athletes", tags=["mindfulness_avancado"])
router_mindful_communicatio = APIRouter(prefix="/api/v1/mindfulness_/mindful_communication", tags=["mindfulness_avancado"])
router_mindful_creativity = APIRouter(prefix="/api/v1/mindfulness_/mindful_creativity", tags=["mindfulness_avancado"])
router_mindful_dying = APIRouter(prefix="/api/v1/mindfulness_/mindful_dying", tags=["mindfulness_avancado"])
router_mindful_eating2 = APIRouter(prefix="/api/v1/mindfulness_/mindful_eating2", tags=["mindfulness_avancado"])
router_mindful_emotion_regu = APIRouter(prefix="/api/v1/mindfulness_/mindful_emotion_regulatio", tags=["mindfulness_avancado"])
router_mindful_grief = APIRouter(prefix="/api/v1/mindfulness_/mindful_grief", tags=["mindfulness_avancado"])
router_mindful_illness = APIRouter(prefix="/api/v1/mindfulness_/mindful_illness", tags=["mindfulness_avancado"])
router_mindful_leadership = APIRouter(prefix="/api/v1/mindfulness_/mindful_leadership", tags=["mindfulness_avancado"])
router_mindful_military = APIRouter(prefix="/api/v1/mindfulness_/mindful_military", tags=["mindfulness_avancado"])
router_mindful_pain = APIRouter(prefix="/api/v1/mindfulness_/mindful_pain", tags=["mindfulness_avancado"])
router_mindful_parenting2 = APIRouter(prefix="/api/v1/mindfulness_/mindful_parenting2", tags=["mindfulness_avancado"])
router_mindful_recovery = APIRouter(prefix="/api/v1/mindfulness_/mindful_recovery", tags=["mindfulness_avancado"])
router_mindful_relationship = APIRouter(prefix="/api/v1/mindfulness_/mindful_relationship", tags=["mindfulness_avancado"])
router_mindful_schools = APIRouter(prefix="/api/v1/mindfulness_/mindful_schools", tags=["mindfulness_avancado"])
router_mindful_self_compass = APIRouter(prefix="/api/v1/mindfulness_/mindful_self_compassion", tags=["mindfulness_avancado"])
router_mindful_sexuality = APIRouter(prefix="/api/v1/mindfulness_/mindful_sexuality", tags=["mindfulness_avancado"])
router_mindful_sobriety = APIRouter(prefix="/api/v1/mindfulness_/mindful_sobriety", tags=["mindfulness_avancado"])
router_mindful_speaking = APIRouter(prefix="/api/v1/mindfulness_/mindful_speaking", tags=["mindfulness_avancado"])
router_mindful_trauma = APIRouter(prefix="/api/v1/mindfulness_/mindful_trauma", tags=["mindfulness_avancado"])
router_mindful_walking2 = APIRouter(prefix="/api/v1/mindfulness_/mindful_walking2", tags=["mindfulness_avancado"])
router_mindful_working = APIRouter(prefix="/api/v1/mindfulness_/mindful_working", tags=["mindfulness_avancado"])
router_mindful_workplace = APIRouter(prefix="/api/v1/mindfulness_/mindful_workplace", tags=["mindfulness_avancado"])
router_mindfulness_based_ca = APIRouter(prefix="/api/v1/mindfulness_/mindfulness_based_cancer", tags=["mindfulness_avancado"])
router_mindfulness_based_ch = APIRouter(prefix="/api/v1/mindfulness_/mindfulness_based_childbi", tags=["mindfulness_avancado"])
router_mindfulness_based_co = APIRouter(prefix="/api/v1/mindfulness_/mindfulness_based_cogniti", tags=["mindfulness_avancado"])
router_mindfulness_based_ea = APIRouter(prefix="/api/v1/mindfulness_/mindfulness_based_eating", tags=["mindfulness_avancado"])
router_mindfulness_based_el = APIRouter(prefix="/api/v1/mindfulness_/mindfulness_based_elderca", tags=["mindfulness_avancado"])
router_mindfulness_based_pa = APIRouter(prefix="/api/v1/mindfulness_/mindfulness_based_parenti", tags=["mindfulness_avancado"])
router_mindfulness_based_re = APIRouter(prefix="/api/v1/mindfulness_/mindfulness_based_relapse", tags=["mindfulness_avancado"])
router_mindfulness_based_re = APIRouter(prefix="/api/v1/mindfulness_/mindfulness_based_relatio", tags=["mindfulness_avancado"])
router_mindfulness_based_st = APIRouter(prefix="/api/v1/mindfulness_/mindfulness_based_stress", tags=["mindfulness_avancado"])
router_mindfulness_daily_li = APIRouter(prefix="/api/v1/mindfulness_/mindfulness_daily_life", tags=["mindfulness_avancado"])
router_mudita_practice = APIRouter(prefix="/api/v1/mindfulness_/mudita_practice", tags=["mindfulness_avancado"])
router_non_judgmental_mind = APIRouter(prefix="/api/v1/mindfulness_/non_judgmental_mind", tags=["mindfulness_avancado"])
router_nonviolent_communica = APIRouter(prefix="/api/v1/mindfulness_/nonviolent_communication2", tags=["mindfulness_avancado"])
router_observe_label_regula = APIRouter(prefix="/api/v1/mindfulness_/observe_label_regulate", tags=["mindfulness_avancado"])
router_observe_mindful = APIRouter(prefix="/api/v1/mindfulness_/observe_mindful", tags=["mindfulness_avancado"])
router_one_mind = APIRouter(prefix="/api/v1/mindfulness_/one_mind", tags=["mindfulness_avancado"])
router_open_questions_mindf = APIRouter(prefix="/api/v1/mindfulness_/open_questions_mindful", tags=["mindfulness_avancado"])
router_opposite_action_mind = APIRouter(prefix="/api/v1/mindfulness_/opposite_action_mindful", tags=["mindfulness_avancado"])
router_participate_mindful = APIRouter(prefix="/api/v1/mindfulness_/participate_mindful", tags=["mindfulness_avancado"])
router_pause_before_respond = APIRouter(prefix="/api/v1/mindfulness_/pause_before_respond", tags=["mindfulness_avancado"])
router_peak_mindful = APIRouter(prefix="/api/v1/mindfulness_/peak_mindful", tags=["mindfulness_avancado"])
router_perfectionism_self_c = APIRouter(prefix="/api/v1/mindfulness_/perfectionism_self_compas", tags=["mindfulness_avancado"])
router_performance_mindful = APIRouter(prefix="/api/v1/mindfulness_/performance_mindful", tags=["mindfulness_avancado"])
router_problem_solve_mindfu = APIRouter(prefix="/api/v1/mindfulness_/problem_solve_mindful", tags=["mindfulness_avancado"])
router_reasonable_mind2 = APIRouter(prefix="/api/v1/mindfulness_/reasonable_mind2", tags=["mindfulness_avancado"])
router_reflective_listening = APIRouter(prefix="/api/v1/mindfulness_/reflective_listening2", tags=["mindfulness_avancado"])
router_ride_wave_emotion = APIRouter(prefix="/api/v1/mindfulness_/ride_wave_emotion", tags=["mindfulness_avancado"])
router_self_compassion_brea = APIRouter(prefix="/api/v1/mindfulness_/self_compassion_break", tags=["mindfulness_avancado"])
router_self_compassion_resi = APIRouter(prefix="/api/v1/mindfulness_/self_compassion_resilienc", tags=["mindfulness_avancado"])
router_shame_self_compassio = APIRouter(prefix="/api/v1/mindfulness_/shame_self_compassion", tags=["mindfulness_avancado"])
router_silence_mindful = APIRouter(prefix="/api/v1/mindfulness_/silence_mindful", tags=["mindfulness_avancado"])
router_sport_psychology_min = APIRouter(prefix="/api/v1/mindfulness_/sport_psychology_mindful", tags=["mindfulness_avancado"])
router_surf_urge = APIRouter(prefix="/api/v1/mindfulness_/surf_urge", tags=["mindfulness_avancado"])
router_sympathetic_joy = APIRouter(prefix="/api/v1/mindfulness_/sympathetic_joy", tags=["mindfulness_avancado"])
router_teflon_mind = APIRouter(prefix="/api/v1/mindfulness_/teflon_mind", tags=["mindfulness_avancado"])
router_tender_self_compassi = APIRouter(prefix="/api/v1/mindfulness_/tender_self_compassion", tags=["mindfulness_avancado"])
router_tonglen_advanced = APIRouter(prefix="/api/v1/mindfulness_/tonglen_advanced", tags=["mindfulness_avancado"])
router_wise_mind2 = APIRouter(prefix="/api/v1/mindfulness_/wise_mind2", tags=["mindfulness_avancado"])

@router_MSC_intensive.get("")
async def i_MSC_intensive():
    return {"p":"mindfulness_ava_MSC_intensive","s":"ativo","t":datetime.utcnow().isoformat()}
@router_MSC_online.get("")
async def i_MSC_online():
    return {"p":"mindfulness_ava_MSC_online","s":"ativo","t":datetime.utcnow().isoformat()}
@router_MSC_program.get("")
async def i_MSC_program():
    return {"p":"mindfulness_ava_MSC_program","s":"ativo","t":datetime.utcnow().isoformat()}
@router_NVC_mindful.get("")
async def i_NVC_mindful():
    return {"p":"mindfulness_ava_NVC_mindful","s":"ativo","t":datetime.utcnow().isoformat()}
@router_PLEASE_mindful.get("")
async def i_PLEASE_mindful():
    return {"p":"mindfulness_ava_PLEASE_mindful","s":"ativo","t":datetime.utcnow().isoformat()}
@router_RAIN_technique.get("")
async def i_RAIN_technique():
    return {"p":"mindfulness_ava_RAIN_technique","s":"ativo","t":datetime.utcnow().isoformat()}
@router_STOP_technique.get("")
async def i_STOP_technique():
    return {"p":"mindfulness_ava_STOP_technique","s":"ativo","t":datetime.utcnow().isoformat()}
@router_TIPP_mindful.get("")
async def i_TIPP_mindful():
    return {"p":"mindfulness_ava_TIPP_mindful","s":"ativo","t":datetime.utcnow().isoformat()}
@router_acceptance_commitmen.get("")
async def i_acceptance_commitmen():
    return {"p":"mindfulness_ava_acceptance_commitmen","s":"ativo","t":datetime.utcnow().isoformat()}
@router_active_listening2.get("")
async def i_active_listening2():
    return {"p":"mindfulness_ava_active_listening2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_beginner_mind.get("")
async def i_beginner_mind():
    return {"p":"mindfulness_ava_beginner_mind","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bodhicitta_practice.get("")
async def i_bodhicitta_practice():
    return {"p":"mindfulness_ava_bodhicitta_practice","s":"ativo","t":datetime.utcnow().isoformat()}
@router_brahmaviharas_practi.get("")
async def i_brahmaviharas_practi():
    return {"p":"mindfulness_ava_brahmaviharas_practi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_build_mastery_mindfu.get("")
async def i_build_mastery_mindfu():
    return {"p":"mindfulness_ava_build_mastery_mindfu","s":"ativo","t":datetime.utcnow().isoformat()}
@router_check_facts_mindful.get("")
async def i_check_facts_mindful():
    return {"p":"mindfulness_ava_check_facts_mindful","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cognitively_based_co.get("")
async def i_cognitively_based_co():
    return {"p":"mindfulness_ava_cognitively_based_co","s":"ativo","t":datetime.utcnow().isoformat()}
@router_common_humanity_prac.get("")
async def i_common_humanity_prac():
    return {"p":"mindfulness_ava_common_humanity_prac","s":"ativo","t":datetime.utcnow().isoformat()}
@router_compassion_cultivati.get("")
async def i_compassion_cultivati():
    return {"p":"mindfulness_ava_compassion_cultivati","s":"ativo","t":datetime.utcnow().isoformat()}
@router_compassion_fatigue_p.get("")
async def i_compassion_fatigue_p():
    return {"p":"mindfulness_ava_compassion_fatigue_p","s":"ativo","t":datetime.utcnow().isoformat()}
@router_compassion_focused_m.get("")
async def i_compassion_focused_m():
    return {"p":"mindfulness_ava_compassion_focused_m","s":"ativo","t":datetime.utcnow().isoformat()}
@router_compassion_meditatio.get("")
async def i_compassion_meditatio():
    return {"p":"mindfulness_ava_compassion_meditatio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_conscious_communicat.get("")
async def i_conscious_communicat():
    return {"p":"mindfulness_ava_conscious_communicat","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cope_ahead_mindful.get("")
async def i_cope_ahead_mindful():
    return {"p":"mindfulness_ava_cope_ahead_mindful","s":"ativo","t":datetime.utcnow().isoformat()}
@router_deep_listening.get("")
async def i_deep_listening():
    return {"p":"mindfulness_ava_deep_listening","s":"ativo","t":datetime.utcnow().isoformat()}
@router_describe_mindful.get("")
async def i_describe_mindful():
    return {"p":"mindfulness_ava_describe_mindful","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dialectical_behavior.get("")
async def i_dialectical_behavior():
    return {"p":"mindfulness_ava_dialectical_behavior","s":"ativo","t":datetime.utcnow().isoformat()}
@router_effective_mind.get("")
async def i_effective_mind():
    return {"p":"mindfulness_ava_effective_mind","s":"ativo","t":datetime.utcnow().isoformat()}
@router_emotion_mind2.get("")
async def i_emotion_mind2():
    return {"p":"mindfulness_ava_emotion_mind2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_empathic_listening.get("")
async def i_empathic_listening():
    return {"p":"mindfulness_ava_empathic_listening","s":"ativo","t":datetime.utcnow().isoformat()}
@router_empathy_compassion.get("")
async def i_empathy_compassion():
    return {"p":"mindfulness_ava_empathy_compassion","s":"ativo","t":datetime.utcnow().isoformat()}
@router_equanimity_practice.get("")
async def i_equanimity_practice():
    return {"p":"mindfulness_ava_equanimity_practice","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fierce_self_compassi.get("")
async def i_fierce_self_compassi():
    return {"p":"mindfulness_ava_fierce_self_compassi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_flow_mindful.get("")
async def i_flow_mindful():
    return {"p":"mindfulness_ava_flow_mindful","s":"ativo","t":datetime.utcnow().isoformat()}
@router_four_immeasurables.get("")
async def i_four_immeasurables():
    return {"p":"mindfulness_ava_four_immeasurables","s":"ativo","t":datetime.utcnow().isoformat()}
@router_informal_mindfulness.get("")
async def i_informal_mindfulness():
    return {"p":"mindfulness_ava_informal_mindfulness","s":"ativo","t":datetime.utcnow().isoformat()}
@router_inner_critic_self_co.get("")
async def i_inner_critic_self_co():
    return {"p":"mindfulness_ava_inner_critic_self_co","s":"ativo","t":datetime.utcnow().isoformat()}
@router_just_like_me.get("")
async def i_just_like_me():
    return {"p":"mindfulness_ava_just_like_me","s":"ativo","t":datetime.utcnow().isoformat()}
@router_karuna_compassion.get("")
async def i_karuna_compassion():
    return {"p":"mindfulness_ava_karuna_compassion","s":"ativo","t":datetime.utcnow().isoformat()}
@router_loving_kindness_adva.get("")
async def i_loving_kindness_adva():
    return {"p":"mindfulness_ava_loving_kindness_adva","s":"ativo","t":datetime.utcnow().isoformat()}
@router_metta_tonglen_practi.get("")
async def i_metta_tonglen_practi():
    return {"p":"mindfulness_ava_metta_tonglen_practi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindful_aging.get("")
async def i_mindful_aging():
    return {"p":"mindfulness_ava_mindful_aging","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindful_athletes.get("")
async def i_mindful_athletes():
    return {"p":"mindfulness_ava_mindful_athletes","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindful_communicatio.get("")
async def i_mindful_communicatio():
    return {"p":"mindfulness_ava_mindful_communicatio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindful_creativity.get("")
async def i_mindful_creativity():
    return {"p":"mindfulness_ava_mindful_creativity","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindful_dying.get("")
async def i_mindful_dying():
    return {"p":"mindfulness_ava_mindful_dying","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindful_eating2.get("")
async def i_mindful_eating2():
    return {"p":"mindfulness_ava_mindful_eating2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindful_emotion_regu.get("")
async def i_mindful_emotion_regu():
    return {"p":"mindfulness_ava_mindful_emotion_regu","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindful_grief.get("")
async def i_mindful_grief():
    return {"p":"mindfulness_ava_mindful_grief","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindful_illness.get("")
async def i_mindful_illness():
    return {"p":"mindfulness_ava_mindful_illness","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindful_leadership.get("")
async def i_mindful_leadership():
    return {"p":"mindfulness_ava_mindful_leadership","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindful_military.get("")
async def i_mindful_military():
    return {"p":"mindfulness_ava_mindful_military","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindful_pain.get("")
async def i_mindful_pain():
    return {"p":"mindfulness_ava_mindful_pain","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindful_parenting2.get("")
async def i_mindful_parenting2():
    return {"p":"mindfulness_ava_mindful_parenting2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindful_recovery.get("")
async def i_mindful_recovery():
    return {"p":"mindfulness_ava_mindful_recovery","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindful_relationship.get("")
async def i_mindful_relationship():
    return {"p":"mindfulness_ava_mindful_relationship","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindful_schools.get("")
async def i_mindful_schools():
    return {"p":"mindfulness_ava_mindful_schools","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindful_self_compass.get("")
async def i_mindful_self_compass():
    return {"p":"mindfulness_ava_mindful_self_compass","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindful_sexuality.get("")
async def i_mindful_sexuality():
    return {"p":"mindfulness_ava_mindful_sexuality","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindful_sobriety.get("")
async def i_mindful_sobriety():
    return {"p":"mindfulness_ava_mindful_sobriety","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindful_speaking.get("")
async def i_mindful_speaking():
    return {"p":"mindfulness_ava_mindful_speaking","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindful_trauma.get("")
async def i_mindful_trauma():
    return {"p":"mindfulness_ava_mindful_trauma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindful_walking2.get("")
async def i_mindful_walking2():
    return {"p":"mindfulness_ava_mindful_walking2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindful_working.get("")
async def i_mindful_working():
    return {"p":"mindfulness_ava_mindful_working","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindful_workplace.get("")
async def i_mindful_workplace():
    return {"p":"mindfulness_ava_mindful_workplace","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindfulness_based_ca.get("")
async def i_mindfulness_based_ca():
    return {"p":"mindfulness_ava_mindfulness_based_ca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindfulness_based_ch.get("")
async def i_mindfulness_based_ch():
    return {"p":"mindfulness_ava_mindfulness_based_ch","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindfulness_based_co.get("")
async def i_mindfulness_based_co():
    return {"p":"mindfulness_ava_mindfulness_based_co","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindfulness_based_ea.get("")
async def i_mindfulness_based_ea():
    return {"p":"mindfulness_ava_mindfulness_based_ea","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindfulness_based_el.get("")
async def i_mindfulness_based_el():
    return {"p":"mindfulness_ava_mindfulness_based_el","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindfulness_based_pa.get("")
async def i_mindfulness_based_pa():
    return {"p":"mindfulness_ava_mindfulness_based_pa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindfulness_based_re.get("")
async def i_mindfulness_based_re():
    return {"p":"mindfulness_ava_mindfulness_based_re","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindfulness_based_re.get("")
async def i_mindfulness_based_re():
    return {"p":"mindfulness_ava_mindfulness_based_re","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindfulness_based_st.get("")
async def i_mindfulness_based_st():
    return {"p":"mindfulness_ava_mindfulness_based_st","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindfulness_daily_li.get("")
async def i_mindfulness_daily_li():
    return {"p":"mindfulness_ava_mindfulness_daily_li","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mudita_practice.get("")
async def i_mudita_practice():
    return {"p":"mindfulness_ava_mudita_practice","s":"ativo","t":datetime.utcnow().isoformat()}
@router_non_judgmental_mind.get("")
async def i_non_judgmental_mind():
    return {"p":"mindfulness_ava_non_judgmental_mind","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nonviolent_communica.get("")
async def i_nonviolent_communica():
    return {"p":"mindfulness_ava_nonviolent_communica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_observe_label_regula.get("")
async def i_observe_label_regula():
    return {"p":"mindfulness_ava_observe_label_regula","s":"ativo","t":datetime.utcnow().isoformat()}
@router_observe_mindful.get("")
async def i_observe_mindful():
    return {"p":"mindfulness_ava_observe_mindful","s":"ativo","t":datetime.utcnow().isoformat()}
@router_one_mind.get("")
async def i_one_mind():
    return {"p":"mindfulness_ava_one_mind","s":"ativo","t":datetime.utcnow().isoformat()}
@router_open_questions_mindf.get("")
async def i_open_questions_mindf():
    return {"p":"mindfulness_ava_open_questions_mindf","s":"ativo","t":datetime.utcnow().isoformat()}
@router_opposite_action_mind.get("")
async def i_opposite_action_mind():
    return {"p":"mindfulness_ava_opposite_action_mind","s":"ativo","t":datetime.utcnow().isoformat()}
@router_participate_mindful.get("")
async def i_participate_mindful():
    return {"p":"mindfulness_ava_participate_mindful","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pause_before_respond.get("")
async def i_pause_before_respond():
    return {"p":"mindfulness_ava_pause_before_respond","s":"ativo","t":datetime.utcnow().isoformat()}
@router_peak_mindful.get("")
async def i_peak_mindful():
    return {"p":"mindfulness_ava_peak_mindful","s":"ativo","t":datetime.utcnow().isoformat()}
@router_perfectionism_self_c.get("")
async def i_perfectionism_self_c():
    return {"p":"mindfulness_ava_perfectionism_self_c","s":"ativo","t":datetime.utcnow().isoformat()}
@router_performance_mindful.get("")
async def i_performance_mindful():
    return {"p":"mindfulness_ava_performance_mindful","s":"ativo","t":datetime.utcnow().isoformat()}
@router_problem_solve_mindfu.get("")
async def i_problem_solve_mindfu():
    return {"p":"mindfulness_ava_problem_solve_mindfu","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reasonable_mind2.get("")
async def i_reasonable_mind2():
    return {"p":"mindfulness_ava_reasonable_mind2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reflective_listening.get("")
async def i_reflective_listening():
    return {"p":"mindfulness_ava_reflective_listening","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ride_wave_emotion.get("")
async def i_ride_wave_emotion():
    return {"p":"mindfulness_ava_ride_wave_emotion","s":"ativo","t":datetime.utcnow().isoformat()}
@router_self_compassion_brea.get("")
async def i_self_compassion_brea():
    return {"p":"mindfulness_ava_self_compassion_brea","s":"ativo","t":datetime.utcnow().isoformat()}
@router_self_compassion_resi.get("")
async def i_self_compassion_resi():
    return {"p":"mindfulness_ava_self_compassion_resi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_shame_self_compassio.get("")
async def i_shame_self_compassio():
    return {"p":"mindfulness_ava_shame_self_compassio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_silence_mindful.get("")
async def i_silence_mindful():
    return {"p":"mindfulness_ava_silence_mindful","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sport_psychology_min.get("")
async def i_sport_psychology_min():
    return {"p":"mindfulness_ava_sport_psychology_min","s":"ativo","t":datetime.utcnow().isoformat()}
@router_surf_urge.get("")
async def i_surf_urge():
    return {"p":"mindfulness_ava_surf_urge","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sympathetic_joy.get("")
async def i_sympathetic_joy():
    return {"p":"mindfulness_ava_sympathetic_joy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_teflon_mind.get("")
async def i_teflon_mind():
    return {"p":"mindfulness_ava_teflon_mind","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tender_self_compassi.get("")
async def i_tender_self_compassi():
    return {"p":"mindfulness_ava_tender_self_compassi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tonglen_advanced.get("")
async def i_tonglen_advanced():
    return {"p":"mindfulness_ava_tonglen_advanced","s":"ativo","t":datetime.utcnow().isoformat()}
@router_wise_mind2.get("")
async def i_wise_mind2():
    return {"p":"mindfulness_ava_wise_mind2","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_mindfulness_avancado(PluginBase):
    name = "consolidated_mindfulness_avancado"
    def setup(self, app):
        app.include_router(router_MSC_intensive)
        app.include_router(router_MSC_online)
        app.include_router(router_MSC_program)
        app.include_router(router_NVC_mindful)
        app.include_router(router_PLEASE_mindful)
        app.include_router(router_RAIN_technique)
        app.include_router(router_STOP_technique)
        app.include_router(router_TIPP_mindful)
        app.include_router(router_acceptance_commitmen)
        app.include_router(router_active_listening2)
        app.include_router(router_beginner_mind)
        app.include_router(router_bodhicitta_practice)
        app.include_router(router_brahmaviharas_practi)
        app.include_router(router_build_mastery_mindfu)
        app.include_router(router_check_facts_mindful)
        app.include_router(router_cognitively_based_co)
        app.include_router(router_common_humanity_prac)
        app.include_router(router_compassion_cultivati)
        app.include_router(router_compassion_fatigue_p)
        app.include_router(router_compassion_focused_m)
        app.include_router(router_compassion_meditatio)
        app.include_router(router_conscious_communicat)
        app.include_router(router_cope_ahead_mindful)
        app.include_router(router_deep_listening)
        app.include_router(router_describe_mindful)
        app.include_router(router_dialectical_behavior)
        app.include_router(router_effective_mind)
        app.include_router(router_emotion_mind2)
        app.include_router(router_empathic_listening)
        app.include_router(router_empathy_compassion)
        app.include_router(router_equanimity_practice)
        app.include_router(router_fierce_self_compassi)
        app.include_router(router_flow_mindful)
        app.include_router(router_four_immeasurables)
        app.include_router(router_informal_mindfulness)
        app.include_router(router_inner_critic_self_co)
        app.include_router(router_just_like_me)
        app.include_router(router_karuna_compassion)
        app.include_router(router_loving_kindness_adva)
        app.include_router(router_metta_tonglen_practi)
        app.include_router(router_mindful_aging)
        app.include_router(router_mindful_athletes)
        app.include_router(router_mindful_communicatio)
        app.include_router(router_mindful_creativity)
        app.include_router(router_mindful_dying)
        app.include_router(router_mindful_eating2)
        app.include_router(router_mindful_emotion_regu)
        app.include_router(router_mindful_grief)
        app.include_router(router_mindful_illness)
        app.include_router(router_mindful_leadership)
        app.include_router(router_mindful_military)
        app.include_router(router_mindful_pain)
        app.include_router(router_mindful_parenting2)
        app.include_router(router_mindful_recovery)
        app.include_router(router_mindful_relationship)
        app.include_router(router_mindful_schools)
        app.include_router(router_mindful_self_compass)
        app.include_router(router_mindful_sexuality)
        app.include_router(router_mindful_sobriety)
        app.include_router(router_mindful_speaking)
        app.include_router(router_mindful_trauma)
        app.include_router(router_mindful_walking2)
        app.include_router(router_mindful_working)
        app.include_router(router_mindful_workplace)
        app.include_router(router_mindfulness_based_ca)
        app.include_router(router_mindfulness_based_ch)
        app.include_router(router_mindfulness_based_co)
        app.include_router(router_mindfulness_based_ea)
        app.include_router(router_mindfulness_based_el)
        app.include_router(router_mindfulness_based_pa)
        app.include_router(router_mindfulness_based_re)
        app.include_router(router_mindfulness_based_re)
        app.include_router(router_mindfulness_based_st)
        app.include_router(router_mindfulness_daily_li)
        app.include_router(router_mudita_practice)
        app.include_router(router_non_judgmental_mind)
        app.include_router(router_nonviolent_communica)
        app.include_router(router_observe_label_regula)
        app.include_router(router_observe_mindful)
        app.include_router(router_one_mind)
        app.include_router(router_open_questions_mindf)
        app.include_router(router_opposite_action_mind)
        app.include_router(router_participate_mindful)
        app.include_router(router_pause_before_respond)
        app.include_router(router_peak_mindful)
        app.include_router(router_perfectionism_self_c)
        app.include_router(router_performance_mindful)
        app.include_router(router_problem_solve_mindfu)
        app.include_router(router_reasonable_mind2)
        app.include_router(router_reflective_listening)
        app.include_router(router_ride_wave_emotion)
        app.include_router(router_self_compassion_brea)
        app.include_router(router_self_compassion_resi)
        app.include_router(router_shame_self_compassio)
        app.include_router(router_silence_mindful)
        app.include_router(router_sport_psychology_min)
        app.include_router(router_surf_urge)
        app.include_router(router_sympathetic_joy)
        app.include_router(router_teflon_mind)
        app.include_router(router_tender_self_compassi)
        app.include_router(router_tonglen_advanced)
        app.include_router(router_wise_mind2)


plugin = Plugin_mindfulness_avancado()
