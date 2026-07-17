from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_access_digital = APIRouter(prefix="/api/v1/intervencoes/access_digital", tags=["intervencoes_digitais_especificas"])
router_adoption_digital = APIRouter(prefix="/api/v1/intervencoes/adoption_digital", tags=["intervencoes_digitais_especificas"])
router_app_intervention_val = APIRouter(prefix="/api/v1/intervencoes/app_intervention_validate", tags=["intervencoes_digitais_especificas"])
router_asynchronous_therapy = APIRouter(prefix="/api/v1/intervencoes/asynchronous_therapy", tags=["intervencoes_digitais_especificas"])
router_behavior_change_digi = APIRouter(prefix="/api/v1/intervencoes/behavior_change_digital", tags=["intervencoes_digitais_especificas"])
router_bibliotherapy_digita = APIRouter(prefix="/api/v1/intervencoes/bibliotherapy_digital", tags=["intervencoes_digitais_especificas"])
router_blended_therapy = APIRouter(prefix="/api/v1/intervencoes/blended_therapy", tags=["intervencoes_digitais_especificas"])
router_chat_therapy = APIRouter(prefix="/api/v1/intervencoes/chat_therapy", tags=["intervencoes_digitais_especificas"])
router_context_sensitive_in = APIRouter(prefix="/api/v1/intervencoes/context_sensitive_interve", tags=["intervencoes_digitais_especificas"])
router_cost_benefit_digital = APIRouter(prefix="/api/v1/intervencoes/cost_benefit_digital", tags=["intervencoes_digitais_especificas"])
router_cost_effectiveness_d = APIRouter(prefix="/api/v1/intervencoes/cost_effectiveness_digita", tags=["intervencoes_digitais_especificas"])
router_diffusion_digital = APIRouter(prefix="/api/v1/intervencoes/diffusion_digital", tags=["intervencoes_digitais_especificas"])
router_digital_assessment_t = APIRouter(prefix="/api/v1/intervencoes/digital_assessment_tool", tags=["intervencoes_digitais_especificas"])
router_dissemination_digita = APIRouter(prefix="/api/v1/intervencoes/dissemination_digital", tags=["intervencoes_digitais_especificas"])
router_dropout_prevention_d = APIRouter(prefix="/api/v1/intervencoes/dropout_prevention_digita", tags=["intervencoes_digitais_especificas"])
router_ecological_momentary = APIRouter(prefix="/api/v1/intervencoes/ecological_momentary_inte", tags=["intervencoes_digitais_especificas"])
router_ecological_validity_ = APIRouter(prefix="/api/v1/intervencoes/ecological_validity_digit", tags=["intervencoes_digitais_especificas"])
router_effectiveness_digita = APIRouter(prefix="/api/v1/intervencoes/effectiveness_digital", tags=["intervencoes_digitais_especificas"])
router_efficacy_digital = APIRouter(prefix="/api/v1/intervencoes/efficacy_digital", tags=["intervencoes_digitais_especificas"])
router_email_therapy = APIRouter(prefix="/api/v1/intervencoes/email_therapy", tags=["intervencoes_digitais_especificas"])
router_engagement_digital = APIRouter(prefix="/api/v1/intervencoes/engagement_digital", tags=["intervencoes_digitais_especificas"])
router_equity_digital = APIRouter(prefix="/api/v1/intervencoes/equity_digital", tags=["intervencoes_digitais_especificas"])
router_feedback_informed_di = APIRouter(prefix="/api/v1/intervencoes/feedback_informed_digital", tags=["intervencoes_digitais_especificas"])
router_gamification_clinica = APIRouter(prefix="/api/v1/intervencoes/gamification_clinical", tags=["intervencoes_digitais_especificas"])
router_goal_setting_digital = APIRouter(prefix="/api/v1/intervencoes/goal_setting_digital", tags=["intervencoes_digitais_especificas"])
router_guided_self_help2 = APIRouter(prefix="/api/v1/intervencoes/guided_self_help2", tags=["intervencoes_digitais_especificas"])
router_habit_formation_digi = APIRouter(prefix="/api/v1/intervencoes/habit_formation_digital", tags=["intervencoes_digitais_especificas"])
router_hybrid_therapy = APIRouter(prefix="/api/v1/intervencoes/hybrid_therapy", tags=["intervencoes_digitais_especificas"])
router_iact_tools = APIRouter(prefix="/api/v1/intervencoes/iact_tools", tags=["intervencoes_digitais_especificas"])
router_icbt_anxiety = APIRouter(prefix="/api/v1/intervencoes/icbt_anxiety", tags=["intervencoes_digitais_especificas"])
router_icbt_depression = APIRouter(prefix="/api/v1/intervencoes/icbt_depression", tags=["intervencoes_digitais_especificas"])
router_icbt_eating = APIRouter(prefix="/api/v1/intervencoes/icbt_eating", tags=["intervencoes_digitais_especificas"])
router_icbt_insomnia = APIRouter(prefix="/api/v1/intervencoes/icbt_insomnia", tags=["intervencoes_digitais_especificas"])
router_icbt_ocd = APIRouter(prefix="/api/v1/intervencoes/icbt_ocd", tags=["intervencoes_digitais_especificas"])
router_icbt_pain = APIRouter(prefix="/api/v1/intervencoes/icbt_pain", tags=["intervencoes_digitais_especificas"])
router_icbt_ptsd = APIRouter(prefix="/api/v1/intervencoes/icbt_ptsd", tags=["intervencoes_digitais_especificas"])
router_icbt_substance = APIRouter(prefix="/api/v1/intervencoes/icbt_substance", tags=["intervencoes_digitais_especificas"])
router_idbt_skills = APIRouter(prefix="/api/v1/intervencoes/idbt_skills", tags=["intervencoes_digitais_especificas"])
router_iexp_exposure = APIRouter(prefix="/api/v1/intervencoes/iexp_exposure", tags=["intervencoes_digitais_especificas"])
router_imbct_mindfulness = APIRouter(prefix="/api/v1/intervencoes/imbct_mindfulness", tags=["intervencoes_digitais_especificas"])
router_imbi_motivational = APIRouter(prefix="/api/v1/intervencoes/imbi_motivational", tags=["intervencoes_digitais_especificas"])
router_implementation_digit = APIRouter(prefix="/api/v1/intervencoes/implementation_digital", tags=["intervencoes_digitais_especificas"])
router_just_in_time_adaptiv = APIRouter(prefix="/api/v1/intervencoes/just_in_time_adaptive", tags=["intervencoes_digitais_especificas"])
router_machine_learning_int = APIRouter(prefix="/api/v1/intervencoes/machine_learning_interven", tags=["intervencoes_digitais_especificas"])
router_maintenance_digital = APIRouter(prefix="/api/v1/intervencoes/maintenance_digital", tags=["intervencoes_digitais_especificas"])
router_measurement_based_di = APIRouter(prefix="/api/v1/intervencoes/measurement_based_digital", tags=["intervencoes_digitais_especificas"])
router_motivation_digital = APIRouter(prefix="/api/v1/intervencoes/motivation_digital", tags=["intervencoes_digitais_especificas"])
router_nlp_chatbot_clinical = APIRouter(prefix="/api/v1/intervencoes/nlp_chatbot_clinical", tags=["intervencoes_digitais_especificas"])
router_online_community_men = APIRouter(prefix="/api/v1/intervencoes/online_community_mental", tags=["intervencoes_digitais_especificas"])
router_outcome_monitoring_d = APIRouter(prefix="/api/v1/intervencoes/outcome_monitoring_digita", tags=["intervencoes_digitais_especificas"])
router_peer_support_digital = APIRouter(prefix="/api/v1/intervencoes/peer_support_digital", tags=["intervencoes_digitais_especificas"])
router_podcasts_therapeutic = APIRouter(prefix="/api/v1/intervencoes/podcasts_therapeutic", tags=["intervencoes_digitais_especificas"])
router_progress_monitoring_ = APIRouter(prefix="/api/v1/intervencoes/progress_monitoring_digit", tags=["intervencoes_digitais_especificas"])
router_reach_digital = APIRouter(prefix="/api/v1/intervencoes/reach_digital", tags=["intervencoes_digitais_especificas"])
router_reward_systems_clini = APIRouter(prefix="/api/v1/intervencoes/reward_systems_clinical", tags=["intervencoes_digitais_especificas"])
router_roi_digital = APIRouter(prefix="/api/v1/intervencoes/roi_digital", tags=["intervencoes_digitais_especificas"])
router_scale_digital = APIRouter(prefix="/api/v1/intervencoes/scale_digital", tags=["intervencoes_digitais_especificas"])
router_self_assessment_digi = APIRouter(prefix="/api/v1/intervencoes/self_assessment_digital", tags=["intervencoes_digitais_especificas"])
router_self_monitoring_digi = APIRouter(prefix="/api/v1/intervencoes/self_monitoring_digital", tags=["intervencoes_digitais_especificas"])
router_self_report_digital = APIRouter(prefix="/api/v1/intervencoes/self_report_digital", tags=["intervencoes_digitais_especificas"])
router_sensor_triggered_int = APIRouter(prefix="/api/v1/intervencoes/sensor_triggered_interven", tags=["intervencoes_digitais_especificas"])
router_smartphone_intervent = APIRouter(prefix="/api/v1/intervencoes/smartphone_intervention", tags=["intervencoes_digitais_especificas"])
router_social_media_interve = APIRouter(prefix="/api/v1/intervencoes/social_media_intervention", tags=["intervencoes_digitais_especificas"])
router_stepped_care_digital = APIRouter(prefix="/api/v1/intervencoes/stepped_care_digital2", tags=["intervencoes_digitais_especificas"])
router_sustainability_digit = APIRouter(prefix="/api/v1/intervencoes/sustainability_digital", tags=["intervencoes_digitais_especificas"])
router_synchronous_therapy = APIRouter(prefix="/api/v1/intervencoes/synchronous_therapy", tags=["intervencoes_digitais_especificas"])
router_text_therapy = APIRouter(prefix="/api/v1/intervencoes/text_therapy", tags=["intervencoes_digitais_especificas"])
router_typing_pattern_inter = APIRouter(prefix="/api/v1/intervencoes/typing_pattern_interventi", tags=["intervencoes_digitais_especificas"])
router_unguided_self_help = APIRouter(prefix="/api/v1/intervencoes/unguided_self_help", tags=["intervencoes_digitais_especificas"])
router_value_digital = APIRouter(prefix="/api/v1/intervencoes/value_digital", tags=["intervencoes_digitais_especificas"])
router_videos_therapeutic = APIRouter(prefix="/api/v1/intervencoes/videos_therapeutic", tags=["intervencoes_digitais_especificas"])
router_virtual_support_grou = APIRouter(prefix="/api/v1/intervencoes/virtual_support_group", tags=["intervencoes_digitais_especificas"])
router_voice_analysis_inter = APIRouter(prefix="/api/v1/intervencoes/voice_analysis_interventi", tags=["intervencoes_digitais_especificas"])
router_wearable_interventio = APIRouter(prefix="/api/v1/intervencoes/wearable_intervention", tags=["intervencoes_digitais_especificas"])

@router_access_digital.get("")
async def i_access_digital():
    return {"p":"intervencoes_di_access_digital","s":"ativo","t":datetime.utcnow().isoformat()}
@router_adoption_digital.get("")
async def i_adoption_digital():
    return {"p":"intervencoes_di_adoption_digital","s":"ativo","t":datetime.utcnow().isoformat()}
@router_app_intervention_val.get("")
async def i_app_intervention_val():
    return {"p":"intervencoes_di_app_intervention_val","s":"ativo","t":datetime.utcnow().isoformat()}
@router_asynchronous_therapy.get("")
async def i_asynchronous_therapy():
    return {"p":"intervencoes_di_asynchronous_therapy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_behavior_change_digi.get("")
async def i_behavior_change_digi():
    return {"p":"intervencoes_di_behavior_change_digi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bibliotherapy_digita.get("")
async def i_bibliotherapy_digita():
    return {"p":"intervencoes_di_bibliotherapy_digita","s":"ativo","t":datetime.utcnow().isoformat()}
@router_blended_therapy.get("")
async def i_blended_therapy():
    return {"p":"intervencoes_di_blended_therapy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_chat_therapy.get("")
async def i_chat_therapy():
    return {"p":"intervencoes_di_chat_therapy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_context_sensitive_in.get("")
async def i_context_sensitive_in():
    return {"p":"intervencoes_di_context_sensitive_in","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cost_benefit_digital.get("")
async def i_cost_benefit_digital():
    return {"p":"intervencoes_di_cost_benefit_digital","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cost_effectiveness_d.get("")
async def i_cost_effectiveness_d():
    return {"p":"intervencoes_di_cost_effectiveness_d","s":"ativo","t":datetime.utcnow().isoformat()}
@router_diffusion_digital.get("")
async def i_diffusion_digital():
    return {"p":"intervencoes_di_diffusion_digital","s":"ativo","t":datetime.utcnow().isoformat()}
@router_digital_assessment_t.get("")
async def i_digital_assessment_t():
    return {"p":"intervencoes_di_digital_assessment_t","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dissemination_digita.get("")
async def i_dissemination_digita():
    return {"p":"intervencoes_di_dissemination_digita","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dropout_prevention_d.get("")
async def i_dropout_prevention_d():
    return {"p":"intervencoes_di_dropout_prevention_d","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ecological_momentary.get("")
async def i_ecological_momentary():
    return {"p":"intervencoes_di_ecological_momentary","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ecological_validity_.get("")
async def i_ecological_validity_():
    return {"p":"intervencoes_di_ecological_validity_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_effectiveness_digita.get("")
async def i_effectiveness_digita():
    return {"p":"intervencoes_di_effectiveness_digita","s":"ativo","t":datetime.utcnow().isoformat()}
@router_efficacy_digital.get("")
async def i_efficacy_digital():
    return {"p":"intervencoes_di_efficacy_digital","s":"ativo","t":datetime.utcnow().isoformat()}
@router_email_therapy.get("")
async def i_email_therapy():
    return {"p":"intervencoes_di_email_therapy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_engagement_digital.get("")
async def i_engagement_digital():
    return {"p":"intervencoes_di_engagement_digital","s":"ativo","t":datetime.utcnow().isoformat()}
@router_equity_digital.get("")
async def i_equity_digital():
    return {"p":"intervencoes_di_equity_digital","s":"ativo","t":datetime.utcnow().isoformat()}
@router_feedback_informed_di.get("")
async def i_feedback_informed_di():
    return {"p":"intervencoes_di_feedback_informed_di","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gamification_clinica.get("")
async def i_gamification_clinica():
    return {"p":"intervencoes_di_gamification_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_goal_setting_digital.get("")
async def i_goal_setting_digital():
    return {"p":"intervencoes_di_goal_setting_digital","s":"ativo","t":datetime.utcnow().isoformat()}
@router_guided_self_help2.get("")
async def i_guided_self_help2():
    return {"p":"intervencoes_di_guided_self_help2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_habit_formation_digi.get("")
async def i_habit_formation_digi():
    return {"p":"intervencoes_di_habit_formation_digi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hybrid_therapy.get("")
async def i_hybrid_therapy():
    return {"p":"intervencoes_di_hybrid_therapy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_iact_tools.get("")
async def i_iact_tools():
    return {"p":"intervencoes_di_iact_tools","s":"ativo","t":datetime.utcnow().isoformat()}
@router_icbt_anxiety.get("")
async def i_icbt_anxiety():
    return {"p":"intervencoes_di_icbt_anxiety","s":"ativo","t":datetime.utcnow().isoformat()}
@router_icbt_depression.get("")
async def i_icbt_depression():
    return {"p":"intervencoes_di_icbt_depression","s":"ativo","t":datetime.utcnow().isoformat()}
@router_icbt_eating.get("")
async def i_icbt_eating():
    return {"p":"intervencoes_di_icbt_eating","s":"ativo","t":datetime.utcnow().isoformat()}
@router_icbt_insomnia.get("")
async def i_icbt_insomnia():
    return {"p":"intervencoes_di_icbt_insomnia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_icbt_ocd.get("")
async def i_icbt_ocd():
    return {"p":"intervencoes_di_icbt_ocd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_icbt_pain.get("")
async def i_icbt_pain():
    return {"p":"intervencoes_di_icbt_pain","s":"ativo","t":datetime.utcnow().isoformat()}
@router_icbt_ptsd.get("")
async def i_icbt_ptsd():
    return {"p":"intervencoes_di_icbt_ptsd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_icbt_substance.get("")
async def i_icbt_substance():
    return {"p":"intervencoes_di_icbt_substance","s":"ativo","t":datetime.utcnow().isoformat()}
@router_idbt_skills.get("")
async def i_idbt_skills():
    return {"p":"intervencoes_di_idbt_skills","s":"ativo","t":datetime.utcnow().isoformat()}
@router_iexp_exposure.get("")
async def i_iexp_exposure():
    return {"p":"intervencoes_di_iexp_exposure","s":"ativo","t":datetime.utcnow().isoformat()}
@router_imbct_mindfulness.get("")
async def i_imbct_mindfulness():
    return {"p":"intervencoes_di_imbct_mindfulness","s":"ativo","t":datetime.utcnow().isoformat()}
@router_imbi_motivational.get("")
async def i_imbi_motivational():
    return {"p":"intervencoes_di_imbi_motivational","s":"ativo","t":datetime.utcnow().isoformat()}
@router_implementation_digit.get("")
async def i_implementation_digit():
    return {"p":"intervencoes_di_implementation_digit","s":"ativo","t":datetime.utcnow().isoformat()}
@router_just_in_time_adaptiv.get("")
async def i_just_in_time_adaptiv():
    return {"p":"intervencoes_di_just_in_time_adaptiv","s":"ativo","t":datetime.utcnow().isoformat()}
@router_machine_learning_int.get("")
async def i_machine_learning_int():
    return {"p":"intervencoes_di_machine_learning_int","s":"ativo","t":datetime.utcnow().isoformat()}
@router_maintenance_digital.get("")
async def i_maintenance_digital():
    return {"p":"intervencoes_di_maintenance_digital","s":"ativo","t":datetime.utcnow().isoformat()}
@router_measurement_based_di.get("")
async def i_measurement_based_di():
    return {"p":"intervencoes_di_measurement_based_di","s":"ativo","t":datetime.utcnow().isoformat()}
@router_motivation_digital.get("")
async def i_motivation_digital():
    return {"p":"intervencoes_di_motivation_digital","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nlp_chatbot_clinical.get("")
async def i_nlp_chatbot_clinical():
    return {"p":"intervencoes_di_nlp_chatbot_clinical","s":"ativo","t":datetime.utcnow().isoformat()}
@router_online_community_men.get("")
async def i_online_community_men():
    return {"p":"intervencoes_di_online_community_men","s":"ativo","t":datetime.utcnow().isoformat()}
@router_outcome_monitoring_d.get("")
async def i_outcome_monitoring_d():
    return {"p":"intervencoes_di_outcome_monitoring_d","s":"ativo","t":datetime.utcnow().isoformat()}
@router_peer_support_digital.get("")
async def i_peer_support_digital():
    return {"p":"intervencoes_di_peer_support_digital","s":"ativo","t":datetime.utcnow().isoformat()}
@router_podcasts_therapeutic.get("")
async def i_podcasts_therapeutic():
    return {"p":"intervencoes_di_podcasts_therapeutic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_progress_monitoring_.get("")
async def i_progress_monitoring_():
    return {"p":"intervencoes_di_progress_monitoring_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reach_digital.get("")
async def i_reach_digital():
    return {"p":"intervencoes_di_reach_digital","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reward_systems_clini.get("")
async def i_reward_systems_clini():
    return {"p":"intervencoes_di_reward_systems_clini","s":"ativo","t":datetime.utcnow().isoformat()}
@router_roi_digital.get("")
async def i_roi_digital():
    return {"p":"intervencoes_di_roi_digital","s":"ativo","t":datetime.utcnow().isoformat()}
@router_scale_digital.get("")
async def i_scale_digital():
    return {"p":"intervencoes_di_scale_digital","s":"ativo","t":datetime.utcnow().isoformat()}
@router_self_assessment_digi.get("")
async def i_self_assessment_digi():
    return {"p":"intervencoes_di_self_assessment_digi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_self_monitoring_digi.get("")
async def i_self_monitoring_digi():
    return {"p":"intervencoes_di_self_monitoring_digi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_self_report_digital.get("")
async def i_self_report_digital():
    return {"p":"intervencoes_di_self_report_digital","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sensor_triggered_int.get("")
async def i_sensor_triggered_int():
    return {"p":"intervencoes_di_sensor_triggered_int","s":"ativo","t":datetime.utcnow().isoformat()}
@router_smartphone_intervent.get("")
async def i_smartphone_intervent():
    return {"p":"intervencoes_di_smartphone_intervent","s":"ativo","t":datetime.utcnow().isoformat()}
@router_social_media_interve.get("")
async def i_social_media_interve():
    return {"p":"intervencoes_di_social_media_interve","s":"ativo","t":datetime.utcnow().isoformat()}
@router_stepped_care_digital.get("")
async def i_stepped_care_digital():
    return {"p":"intervencoes_di_stepped_care_digital","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sustainability_digit.get("")
async def i_sustainability_digit():
    return {"p":"intervencoes_di_sustainability_digit","s":"ativo","t":datetime.utcnow().isoformat()}
@router_synchronous_therapy.get("")
async def i_synchronous_therapy():
    return {"p":"intervencoes_di_synchronous_therapy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_text_therapy.get("")
async def i_text_therapy():
    return {"p":"intervencoes_di_text_therapy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_typing_pattern_inter.get("")
async def i_typing_pattern_inter():
    return {"p":"intervencoes_di_typing_pattern_inter","s":"ativo","t":datetime.utcnow().isoformat()}
@router_unguided_self_help.get("")
async def i_unguided_self_help():
    return {"p":"intervencoes_di_unguided_self_help","s":"ativo","t":datetime.utcnow().isoformat()}
@router_value_digital.get("")
async def i_value_digital():
    return {"p":"intervencoes_di_value_digital","s":"ativo","t":datetime.utcnow().isoformat()}
@router_videos_therapeutic.get("")
async def i_videos_therapeutic():
    return {"p":"intervencoes_di_videos_therapeutic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_virtual_support_grou.get("")
async def i_virtual_support_grou():
    return {"p":"intervencoes_di_virtual_support_grou","s":"ativo","t":datetime.utcnow().isoformat()}
@router_voice_analysis_inter.get("")
async def i_voice_analysis_inter():
    return {"p":"intervencoes_di_voice_analysis_inter","s":"ativo","t":datetime.utcnow().isoformat()}
@router_wearable_interventio.get("")
async def i_wearable_interventio():
    return {"p":"intervencoes_di_wearable_interventio","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_intervencoes_digitai(PluginBase):
    name = "consolidated_intervencoes_digitais_especifi"
    def setup(self, app):
        app.include_router(router_access_digital)
        app.include_router(router_adoption_digital)
        app.include_router(router_app_intervention_val)
        app.include_router(router_asynchronous_therapy)
        app.include_router(router_behavior_change_digi)
        app.include_router(router_bibliotherapy_digita)
        app.include_router(router_blended_therapy)
        app.include_router(router_chat_therapy)
        app.include_router(router_context_sensitive_in)
        app.include_router(router_cost_benefit_digital)
        app.include_router(router_cost_effectiveness_d)
        app.include_router(router_diffusion_digital)
        app.include_router(router_digital_assessment_t)
        app.include_router(router_dissemination_digita)
        app.include_router(router_dropout_prevention_d)
        app.include_router(router_ecological_momentary)
        app.include_router(router_ecological_validity_)
        app.include_router(router_effectiveness_digita)
        app.include_router(router_efficacy_digital)
        app.include_router(router_email_therapy)
        app.include_router(router_engagement_digital)
        app.include_router(router_equity_digital)
        app.include_router(router_feedback_informed_di)
        app.include_router(router_gamification_clinica)
        app.include_router(router_goal_setting_digital)
        app.include_router(router_guided_self_help2)
        app.include_router(router_habit_formation_digi)
        app.include_router(router_hybrid_therapy)
        app.include_router(router_iact_tools)
        app.include_router(router_icbt_anxiety)
        app.include_router(router_icbt_depression)
        app.include_router(router_icbt_eating)
        app.include_router(router_icbt_insomnia)
        app.include_router(router_icbt_ocd)
        app.include_router(router_icbt_pain)
        app.include_router(router_icbt_ptsd)
        app.include_router(router_icbt_substance)
        app.include_router(router_idbt_skills)
        app.include_router(router_iexp_exposure)
        app.include_router(router_imbct_mindfulness)
        app.include_router(router_imbi_motivational)
        app.include_router(router_implementation_digit)
        app.include_router(router_just_in_time_adaptiv)
        app.include_router(router_machine_learning_int)
        app.include_router(router_maintenance_digital)
        app.include_router(router_measurement_based_di)
        app.include_router(router_motivation_digital)
        app.include_router(router_nlp_chatbot_clinical)
        app.include_router(router_online_community_men)
        app.include_router(router_outcome_monitoring_d)
        app.include_router(router_peer_support_digital)
        app.include_router(router_podcasts_therapeutic)
        app.include_router(router_progress_monitoring_)
        app.include_router(router_reach_digital)
        app.include_router(router_reward_systems_clini)
        app.include_router(router_roi_digital)
        app.include_router(router_scale_digital)
        app.include_router(router_self_assessment_digi)
        app.include_router(router_self_monitoring_digi)
        app.include_router(router_self_report_digital)
        app.include_router(router_sensor_triggered_int)
        app.include_router(router_smartphone_intervent)
        app.include_router(router_social_media_interve)
        app.include_router(router_stepped_care_digital)
        app.include_router(router_sustainability_digit)
        app.include_router(router_synchronous_therapy)
        app.include_router(router_text_therapy)
        app.include_router(router_typing_pattern_inter)
        app.include_router(router_unguided_self_help)
        app.include_router(router_value_digital)
        app.include_router(router_videos_therapeutic)
        app.include_router(router_virtual_support_grou)
        app.include_router(router_voice_analysis_inter)
        app.include_router(router_wearable_interventio)


plugin = Plugin_intervencoes_digitai()
