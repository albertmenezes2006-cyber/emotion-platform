from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_PETTLEP_model = APIRouter(prefix="/api/v1/saude_mental/PETTLEP_model", tags=["saude_mental_esporte"])
router_abuse_sport = APIRouter(prefix="/api/v1/saude_mental/abuse_sport", tags=["saude_mental_esporte"])
router_achievement_goal_the = APIRouter(prefix="/api/v1/saude_mental/achievement_goal_theory", tags=["saude_mental_esporte"])
router_athletic_burnout = APIRouter(prefix="/api/v1/saude_mental/athletic_burnout", tags=["saude_mental_esporte"])
router_athletic_identity = APIRouter(prefix="/api/v1/saude_mental/athletic_identity", tags=["saude_mental_esporte"])
router_attentional_focus = APIRouter(prefix="/api/v1/saude_mental/attentional_focus", tags=["saude_mental_esporte"])
router_attentional_style = APIRouter(prefix="/api/v1/saude_mental/attentional_style", tags=["saude_mental_esporte"])
router_auditory_imagery = APIRouter(prefix="/api/v1/saude_mental/auditory_imagery", tags=["saude_mental_esporte"])
router_autonomy_sport = APIRouter(prefix="/api/v1/saude_mental/autonomy_sport", tags=["saude_mental_esporte"])
router_basic_needs_sport = APIRouter(prefix="/api/v1/saude_mental/basic_needs_sport", tags=["saude_mental_esporte"])
router_broad_focus = APIRouter(prefix="/api/v1/saude_mental/broad_focus", tags=["saude_mental_esporte"])
router_burnout_sport2 = APIRouter(prefix="/api/v1/saude_mental/burnout_sport2", tags=["saude_mental_esporte"])
router_career_transition_sp = APIRouter(prefix="/api/v1/saude_mental/career_transition_sport", tags=["saude_mental_esporte"])
router_choking_under_pressu = APIRouter(prefix="/api/v1/saude_mental/choking_under_pressure", tags=["saude_mental_esporte"])
router_cognitive_anxiety_sp = APIRouter(prefix="/api/v1/saude_mental/cognitive_anxiety_sport", tags=["saude_mental_esporte"])
router_cognitive_restructur = APIRouter(prefix="/api/v1/saude_mental/cognitive_restructuring_s", tags=["saude_mental_esporte"])
router_competence_sport = APIRouter(prefix="/api/v1/saude_mental/competence_sport", tags=["saude_mental_esporte"])
router_competition_plan = APIRouter(prefix="/api/v1/saude_mental/competition_plan", tags=["saude_mental_esporte"])
router_competition_simulati = APIRouter(prefix="/api/v1/saude_mental/competition_simulation", tags=["saude_mental_esporte"])
router_competitive_anxiety = APIRouter(prefix="/api/v1/saude_mental/competitive_anxiety", tags=["saude_mental_esporte"])
router_confidence_sport = APIRouter(prefix="/api/v1/saude_mental/confidence_sport", tags=["saude_mental_esporte"])
router_controllability_imag = APIRouter(prefix="/api/v1/saude_mental/controllability_imagery", tags=["saude_mental_esporte"])
router_cue_words = APIRouter(prefix="/api/v1/saude_mental/cue_words", tags=["saude_mental_esporte"])
router_dual_career_athletes = APIRouter(prefix="/api/v1/saude_mental/dual_career_athletes", tags=["saude_mental_esporte"])
router_emotional_imagery = APIRouter(prefix="/api/v1/saude_mental/emotional_imagery", tags=["saude_mental_esporte"])
router_external_focus = APIRouter(prefix="/api/v1/saude_mental/external_focus", tags=["saude_mental_esporte"])
router_extrinsic_motivation = APIRouter(prefix="/api/v1/saude_mental/extrinsic_motivation_spor", tags=["saude_mental_esporte"])
router_game_plan = APIRouter(prefix="/api/v1/saude_mental/game_plan", tags=["saude_mental_esporte"])
router_goal_setting_sport = APIRouter(prefix="/api/v1/saude_mental/goal_setting_sport", tags=["saude_mental_esporte"])
router_goal_setting_theory2 = APIRouter(prefix="/api/v1/saude_mental/goal_setting_theory2", tags=["saude_mental_esporte"])
router_grit_sport = APIRouter(prefix="/api/v1/saude_mental/grit_sport", tags=["saude_mental_esporte"])
router_group_dynamics_sport = APIRouter(prefix="/api/v1/saude_mental/group_dynamics_sport", tags=["saude_mental_esporte"])
router_gustatory_imagery = APIRouter(prefix="/api/v1/saude_mental/gustatory_imagery", tags=["saude_mental_esporte"])
router_hazing_sport = APIRouter(prefix="/api/v1/saude_mental/hazing_sport", tags=["saude_mental_esporte"])
router_identity_foreclosure = APIRouter(prefix="/api/v1/saude_mental/identity_foreclosure_spor", tags=["saude_mental_esporte"])
router_imagery_sport = APIRouter(prefix="/api/v1/saude_mental/imagery_sport", tags=["saude_mental_esporte"])
router_injury_psychology = APIRouter(prefix="/api/v1/saude_mental/injury_psychology", tags=["saude_mental_esporte"])
router_injury_rehabilitatio = APIRouter(prefix="/api/v1/saude_mental/injury_rehabilitation", tags=["saude_mental_esporte"])
router_instructional_self_t = APIRouter(prefix="/api/v1/saude_mental/instructional_self_talk", tags=["saude_mental_esporte"])
router_internal_external_im = APIRouter(prefix="/api/v1/saude_mental/internal_external_imagery", tags=["saude_mental_esporte"])
router_internal_focus = APIRouter(prefix="/api/v1/saude_mental/internal_focus", tags=["saude_mental_esporte"])
router_intrinsic_motivation = APIRouter(prefix="/api/v1/saude_mental/intrinsic_motivation_spor", tags=["saude_mental_esporte"])
router_kinesthetic_imagery = APIRouter(prefix="/api/v1/saude_mental/kinesthetic_imagery", tags=["saude_mental_esporte"])
router_leadership_sport = APIRouter(prefix="/api/v1/saude_mental/leadership_sport", tags=["saude_mental_esporte"])
router_locke_latham_goals = APIRouter(prefix="/api/v1/saude_mental/locke_latham_goals", tags=["saude_mental_esporte"])
router_locker_room_culture = APIRouter(prefix="/api/v1/saude_mental/locker_room_culture", tags=["saude_mental_esporte"])
router_long_term_goals_spor = APIRouter(prefix="/api/v1/saude_mental/long_term_goals_sport", tags=["saude_mental_esporte"])
router_mastery_climate = APIRouter(prefix="/api/v1/saude_mental/mastery_climate", tags=["saude_mental_esporte"])
router_mental_health_olympi = APIRouter(prefix="/api/v1/saude_mental/mental_health_olympics", tags=["saude_mental_esporte"])
router_mental_rehearsal = APIRouter(prefix="/api/v1/saude_mental/mental_rehearsal", tags=["saude_mental_esporte"])
router_mental_skills_traini = APIRouter(prefix="/api/v1/saude_mental/mental_skills_training", tags=["saude_mental_esporte"])
router_mental_strength = APIRouter(prefix="/api/v1/saude_mental/mental_strength", tags=["saude_mental_esporte"])
router_mental_toughness = APIRouter(prefix="/api/v1/saude_mental/mental_toughness", tags=["saude_mental_esporte"])
router_motivational_self_ta = APIRouter(prefix="/api/v1/saude_mental/motivational_self_talk", tags=["saude_mental_esporte"])
router_narrow_focus = APIRouter(prefix="/api/v1/saude_mental/narrow_focus", tags=["saude_mental_esporte"])
router_negative_self_talk = APIRouter(prefix="/api/v1/saude_mental/negative_self_talk", tags=["saude_mental_esporte"])
router_olfactory_imagery = APIRouter(prefix="/api/v1/saude_mental/olfactory_imagery", tags=["saude_mental_esporte"])
router_optimal_anxiety = APIRouter(prefix="/api/v1/saude_mental/optimal_anxiety", tags=["saude_mental_esporte"])
router_outcome_goals = APIRouter(prefix="/api/v1/saude_mental/outcome_goals", tags=["saude_mental_esporte"])
router_overtraining_syndrom = APIRouter(prefix="/api/v1/saude_mental/overtraining_syndrome", tags=["saude_mental_esporte"])
router_pain_tolerance = APIRouter(prefix="/api/v1/saude_mental/pain_tolerance", tags=["saude_mental_esporte"])
router_performance_anxiety_ = APIRouter(prefix="/api/v1/saude_mental/performance_anxiety_sport", tags=["saude_mental_esporte"])
router_performance_climate = APIRouter(prefix="/api/v1/saude_mental/performance_climate", tags=["saude_mental_esporte"])
router_performance_goals = APIRouter(prefix="/api/v1/saude_mental/performance_goals", tags=["saude_mental_esporte"])
router_performance_psycholo = APIRouter(prefix="/api/v1/saude_mental/performance_psychology", tags=["saude_mental_esporte"])
router_positive_self_talk = APIRouter(prefix="/api/v1/saude_mental/positive_self_talk", tags=["saude_mental_esporte"])
router_pre_competition_rout = APIRouter(prefix="/api/v1/saude_mental/pre_competition_routine", tags=["saude_mental_esporte"])
router_pre_performance_rout = APIRouter(prefix="/api/v1/saude_mental/pre_performance_routine", tags=["saude_mental_esporte"])
router_process_goals = APIRouter(prefix="/api/v1/saude_mental/process_goals", tags=["saude_mental_esporte"])
router_professional_athlete = APIRouter(prefix="/api/v1/saude_mental/professional_athlete_ment", tags=["saude_mental_esporte"])
router_psychological_resili = APIRouter(prefix="/api/v1/saude_mental/psychological_resilience_", tags=["saude_mental_esporte"])
router_race_plan = APIRouter(prefix="/api/v1/saude_mental/race_plan", tags=["saude_mental_esporte"])
router_reframing_sport = APIRouter(prefix="/api/v1/saude_mental/reframing_sport", tags=["saude_mental_esporte"])
router_relatedness_sport = APIRouter(prefix="/api/v1/saude_mental/relatedness_sport", tags=["saude_mental_esporte"])
router_retirement_sport = APIRouter(prefix="/api/v1/saude_mental/retirement_sport", tags=["saude_mental_esporte"])
router_return_to_sport = APIRouter(prefix="/api/v1/saude_mental/return_to_sport", tags=["saude_mental_esporte"])
router_self_confidence_spor = APIRouter(prefix="/api/v1/saude_mental/self_confidence_sport", tags=["saude_mental_esporte"])
router_self_determination_s = APIRouter(prefix="/api/v1/saude_mental/self_determination_sport", tags=["saude_mental_esporte"])
router_self_efficacy_sport = APIRouter(prefix="/api/v1/saude_mental/self_efficacy_sport", tags=["saude_mental_esporte"])
router_self_talk_sport = APIRouter(prefix="/api/v1/saude_mental/self_talk_sport", tags=["saude_mental_esporte"])
router_sexual_harassment_sp = APIRouter(prefix="/api/v1/saude_mental/sexual_harassment_sport", tags=["saude_mental_esporte"])
router_short_term_goals_spo = APIRouter(prefix="/api/v1/saude_mental/short_term_goals_sport", tags=["saude_mental_esporte"])
router_social_cohesion = APIRouter(prefix="/api/v1/saude_mental/social_cohesion", tags=["saude_mental_esporte"])
router_somatic_anxiety_spor = APIRouter(prefix="/api/v1/saude_mental/somatic_anxiety_sport", tags=["saude_mental_esporte"])
router_sport_psychology2 = APIRouter(prefix="/api/v1/saude_mental/sport_psychology2", tags=["saude_mental_esporte"])
router_state_anxiety_sport = APIRouter(prefix="/api/v1/saude_mental/state_anxiety_sport", tags=["saude_mental_esporte"])
router_student_athlete = APIRouter(prefix="/api/v1/saude_mental/student_athlete", tags=["saude_mental_esporte"])
router_task_cohesion = APIRouter(prefix="/api/v1/saude_mental/task_cohesion", tags=["saude_mental_esporte"])
router_team_cohesion = APIRouter(prefix="/api/v1/saude_mental/team_cohesion", tags=["saude_mental_esporte"])
router_team_culture = APIRouter(prefix="/api/v1/saude_mental/team_culture", tags=["saude_mental_esporte"])
router_thought_stopping = APIRouter(prefix="/api/v1/saude_mental/thought_stopping", tags=["saude_mental_esporte"])
router_trait_anxiety_sport = APIRouter(prefix="/api/v1/saude_mental/trait_anxiety_sport", tags=["saude_mental_esporte"])
router_visual_imagery = APIRouter(prefix="/api/v1/saude_mental/visual_imagery", tags=["saude_mental_esporte"])
router_vividness = APIRouter(prefix="/api/v1/saude_mental/vividness", tags=["saude_mental_esporte"])
router_zone_performance = APIRouter(prefix="/api/v1/saude_mental/zone_performance", tags=["saude_mental_esporte"])

@router_PETTLEP_model.get("")
async def i_PETTLEP_model():
    return {"p":"saude_mental_es_PETTLEP_model","s":"ativo","t":datetime.utcnow().isoformat()}
@router_abuse_sport.get("")
async def i_abuse_sport():
    return {"p":"saude_mental_es_abuse_sport","s":"ativo","t":datetime.utcnow().isoformat()}
@router_achievement_goal_the.get("")
async def i_achievement_goal_the():
    return {"p":"saude_mental_es_achievement_goal_the","s":"ativo","t":datetime.utcnow().isoformat()}
@router_athletic_burnout.get("")
async def i_athletic_burnout():
    return {"p":"saude_mental_es_athletic_burnout","s":"ativo","t":datetime.utcnow().isoformat()}
@router_athletic_identity.get("")
async def i_athletic_identity():
    return {"p":"saude_mental_es_athletic_identity","s":"ativo","t":datetime.utcnow().isoformat()}
@router_attentional_focus.get("")
async def i_attentional_focus():
    return {"p":"saude_mental_es_attentional_focus","s":"ativo","t":datetime.utcnow().isoformat()}
@router_attentional_style.get("")
async def i_attentional_style():
    return {"p":"saude_mental_es_attentional_style","s":"ativo","t":datetime.utcnow().isoformat()}
@router_auditory_imagery.get("")
async def i_auditory_imagery():
    return {"p":"saude_mental_es_auditory_imagery","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autonomy_sport.get("")
async def i_autonomy_sport():
    return {"p":"saude_mental_es_autonomy_sport","s":"ativo","t":datetime.utcnow().isoformat()}
@router_basic_needs_sport.get("")
async def i_basic_needs_sport():
    return {"p":"saude_mental_es_basic_needs_sport","s":"ativo","t":datetime.utcnow().isoformat()}
@router_broad_focus.get("")
async def i_broad_focus():
    return {"p":"saude_mental_es_broad_focus","s":"ativo","t":datetime.utcnow().isoformat()}
@router_burnout_sport2.get("")
async def i_burnout_sport2():
    return {"p":"saude_mental_es_burnout_sport2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_career_transition_sp.get("")
async def i_career_transition_sp():
    return {"p":"saude_mental_es_career_transition_sp","s":"ativo","t":datetime.utcnow().isoformat()}
@router_choking_under_pressu.get("")
async def i_choking_under_pressu():
    return {"p":"saude_mental_es_choking_under_pressu","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cognitive_anxiety_sp.get("")
async def i_cognitive_anxiety_sp():
    return {"p":"saude_mental_es_cognitive_anxiety_sp","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cognitive_restructur.get("")
async def i_cognitive_restructur():
    return {"p":"saude_mental_es_cognitive_restructur","s":"ativo","t":datetime.utcnow().isoformat()}
@router_competence_sport.get("")
async def i_competence_sport():
    return {"p":"saude_mental_es_competence_sport","s":"ativo","t":datetime.utcnow().isoformat()}
@router_competition_plan.get("")
async def i_competition_plan():
    return {"p":"saude_mental_es_competition_plan","s":"ativo","t":datetime.utcnow().isoformat()}
@router_competition_simulati.get("")
async def i_competition_simulati():
    return {"p":"saude_mental_es_competition_simulati","s":"ativo","t":datetime.utcnow().isoformat()}
@router_competitive_anxiety.get("")
async def i_competitive_anxiety():
    return {"p":"saude_mental_es_competitive_anxiety","s":"ativo","t":datetime.utcnow().isoformat()}
@router_confidence_sport.get("")
async def i_confidence_sport():
    return {"p":"saude_mental_es_confidence_sport","s":"ativo","t":datetime.utcnow().isoformat()}
@router_controllability_imag.get("")
async def i_controllability_imag():
    return {"p":"saude_mental_es_controllability_imag","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cue_words.get("")
async def i_cue_words():
    return {"p":"saude_mental_es_cue_words","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dual_career_athletes.get("")
async def i_dual_career_athletes():
    return {"p":"saude_mental_es_dual_career_athletes","s":"ativo","t":datetime.utcnow().isoformat()}
@router_emotional_imagery.get("")
async def i_emotional_imagery():
    return {"p":"saude_mental_es_emotional_imagery","s":"ativo","t":datetime.utcnow().isoformat()}
@router_external_focus.get("")
async def i_external_focus():
    return {"p":"saude_mental_es_external_focus","s":"ativo","t":datetime.utcnow().isoformat()}
@router_extrinsic_motivation.get("")
async def i_extrinsic_motivation():
    return {"p":"saude_mental_es_extrinsic_motivation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_game_plan.get("")
async def i_game_plan():
    return {"p":"saude_mental_es_game_plan","s":"ativo","t":datetime.utcnow().isoformat()}
@router_goal_setting_sport.get("")
async def i_goal_setting_sport():
    return {"p":"saude_mental_es_goal_setting_sport","s":"ativo","t":datetime.utcnow().isoformat()}
@router_goal_setting_theory2.get("")
async def i_goal_setting_theory2():
    return {"p":"saude_mental_es_goal_setting_theory2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grit_sport.get("")
async def i_grit_sport():
    return {"p":"saude_mental_es_grit_sport","s":"ativo","t":datetime.utcnow().isoformat()}
@router_group_dynamics_sport.get("")
async def i_group_dynamics_sport():
    return {"p":"saude_mental_es_group_dynamics_sport","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gustatory_imagery.get("")
async def i_gustatory_imagery():
    return {"p":"saude_mental_es_gustatory_imagery","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hazing_sport.get("")
async def i_hazing_sport():
    return {"p":"saude_mental_es_hazing_sport","s":"ativo","t":datetime.utcnow().isoformat()}
@router_identity_foreclosure.get("")
async def i_identity_foreclosure():
    return {"p":"saude_mental_es_identity_foreclosure","s":"ativo","t":datetime.utcnow().isoformat()}
@router_imagery_sport.get("")
async def i_imagery_sport():
    return {"p":"saude_mental_es_imagery_sport","s":"ativo","t":datetime.utcnow().isoformat()}
@router_injury_psychology.get("")
async def i_injury_psychology():
    return {"p":"saude_mental_es_injury_psychology","s":"ativo","t":datetime.utcnow().isoformat()}
@router_injury_rehabilitatio.get("")
async def i_injury_rehabilitatio():
    return {"p":"saude_mental_es_injury_rehabilitatio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_instructional_self_t.get("")
async def i_instructional_self_t():
    return {"p":"saude_mental_es_instructional_self_t","s":"ativo","t":datetime.utcnow().isoformat()}
@router_internal_external_im.get("")
async def i_internal_external_im():
    return {"p":"saude_mental_es_internal_external_im","s":"ativo","t":datetime.utcnow().isoformat()}
@router_internal_focus.get("")
async def i_internal_focus():
    return {"p":"saude_mental_es_internal_focus","s":"ativo","t":datetime.utcnow().isoformat()}
@router_intrinsic_motivation.get("")
async def i_intrinsic_motivation():
    return {"p":"saude_mental_es_intrinsic_motivation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_kinesthetic_imagery.get("")
async def i_kinesthetic_imagery():
    return {"p":"saude_mental_es_kinesthetic_imagery","s":"ativo","t":datetime.utcnow().isoformat()}
@router_leadership_sport.get("")
async def i_leadership_sport():
    return {"p":"saude_mental_es_leadership_sport","s":"ativo","t":datetime.utcnow().isoformat()}
@router_locke_latham_goals.get("")
async def i_locke_latham_goals():
    return {"p":"saude_mental_es_locke_latham_goals","s":"ativo","t":datetime.utcnow().isoformat()}
@router_locker_room_culture.get("")
async def i_locker_room_culture():
    return {"p":"saude_mental_es_locker_room_culture","s":"ativo","t":datetime.utcnow().isoformat()}
@router_long_term_goals_spor.get("")
async def i_long_term_goals_spor():
    return {"p":"saude_mental_es_long_term_goals_spor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mastery_climate.get("")
async def i_mastery_climate():
    return {"p":"saude_mental_es_mastery_climate","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mental_health_olympi.get("")
async def i_mental_health_olympi():
    return {"p":"saude_mental_es_mental_health_olympi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mental_rehearsal.get("")
async def i_mental_rehearsal():
    return {"p":"saude_mental_es_mental_rehearsal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mental_skills_traini.get("")
async def i_mental_skills_traini():
    return {"p":"saude_mental_es_mental_skills_traini","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mental_strength.get("")
async def i_mental_strength():
    return {"p":"saude_mental_es_mental_strength","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mental_toughness.get("")
async def i_mental_toughness():
    return {"p":"saude_mental_es_mental_toughness","s":"ativo","t":datetime.utcnow().isoformat()}
@router_motivational_self_ta.get("")
async def i_motivational_self_ta():
    return {"p":"saude_mental_es_motivational_self_ta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_narrow_focus.get("")
async def i_narrow_focus():
    return {"p":"saude_mental_es_narrow_focus","s":"ativo","t":datetime.utcnow().isoformat()}
@router_negative_self_talk.get("")
async def i_negative_self_talk():
    return {"p":"saude_mental_es_negative_self_talk","s":"ativo","t":datetime.utcnow().isoformat()}
@router_olfactory_imagery.get("")
async def i_olfactory_imagery():
    return {"p":"saude_mental_es_olfactory_imagery","s":"ativo","t":datetime.utcnow().isoformat()}
@router_optimal_anxiety.get("")
async def i_optimal_anxiety():
    return {"p":"saude_mental_es_optimal_anxiety","s":"ativo","t":datetime.utcnow().isoformat()}
@router_outcome_goals.get("")
async def i_outcome_goals():
    return {"p":"saude_mental_es_outcome_goals","s":"ativo","t":datetime.utcnow().isoformat()}
@router_overtraining_syndrom.get("")
async def i_overtraining_syndrom():
    return {"p":"saude_mental_es_overtraining_syndrom","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pain_tolerance.get("")
async def i_pain_tolerance():
    return {"p":"saude_mental_es_pain_tolerance","s":"ativo","t":datetime.utcnow().isoformat()}
@router_performance_anxiety_.get("")
async def i_performance_anxiety_():
    return {"p":"saude_mental_es_performance_anxiety_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_performance_climate.get("")
async def i_performance_climate():
    return {"p":"saude_mental_es_performance_climate","s":"ativo","t":datetime.utcnow().isoformat()}
@router_performance_goals.get("")
async def i_performance_goals():
    return {"p":"saude_mental_es_performance_goals","s":"ativo","t":datetime.utcnow().isoformat()}
@router_performance_psycholo.get("")
async def i_performance_psycholo():
    return {"p":"saude_mental_es_performance_psycholo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_positive_self_talk.get("")
async def i_positive_self_talk():
    return {"p":"saude_mental_es_positive_self_talk","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pre_competition_rout.get("")
async def i_pre_competition_rout():
    return {"p":"saude_mental_es_pre_competition_rout","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pre_performance_rout.get("")
async def i_pre_performance_rout():
    return {"p":"saude_mental_es_pre_performance_rout","s":"ativo","t":datetime.utcnow().isoformat()}
@router_process_goals.get("")
async def i_process_goals():
    return {"p":"saude_mental_es_process_goals","s":"ativo","t":datetime.utcnow().isoformat()}
@router_professional_athlete.get("")
async def i_professional_athlete():
    return {"p":"saude_mental_es_professional_athlete","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psychological_resili.get("")
async def i_psychological_resili():
    return {"p":"saude_mental_es_psychological_resili","s":"ativo","t":datetime.utcnow().isoformat()}
@router_race_plan.get("")
async def i_race_plan():
    return {"p":"saude_mental_es_race_plan","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reframing_sport.get("")
async def i_reframing_sport():
    return {"p":"saude_mental_es_reframing_sport","s":"ativo","t":datetime.utcnow().isoformat()}
@router_relatedness_sport.get("")
async def i_relatedness_sport():
    return {"p":"saude_mental_es_relatedness_sport","s":"ativo","t":datetime.utcnow().isoformat()}
@router_retirement_sport.get("")
async def i_retirement_sport():
    return {"p":"saude_mental_es_retirement_sport","s":"ativo","t":datetime.utcnow().isoformat()}
@router_return_to_sport.get("")
async def i_return_to_sport():
    return {"p":"saude_mental_es_return_to_sport","s":"ativo","t":datetime.utcnow().isoformat()}
@router_self_confidence_spor.get("")
async def i_self_confidence_spor():
    return {"p":"saude_mental_es_self_confidence_spor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_self_determination_s.get("")
async def i_self_determination_s():
    return {"p":"saude_mental_es_self_determination_s","s":"ativo","t":datetime.utcnow().isoformat()}
@router_self_efficacy_sport.get("")
async def i_self_efficacy_sport():
    return {"p":"saude_mental_es_self_efficacy_sport","s":"ativo","t":datetime.utcnow().isoformat()}
@router_self_talk_sport.get("")
async def i_self_talk_sport():
    return {"p":"saude_mental_es_self_talk_sport","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sexual_harassment_sp.get("")
async def i_sexual_harassment_sp():
    return {"p":"saude_mental_es_sexual_harassment_sp","s":"ativo","t":datetime.utcnow().isoformat()}
@router_short_term_goals_spo.get("")
async def i_short_term_goals_spo():
    return {"p":"saude_mental_es_short_term_goals_spo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_social_cohesion.get("")
async def i_social_cohesion():
    return {"p":"saude_mental_es_social_cohesion","s":"ativo","t":datetime.utcnow().isoformat()}
@router_somatic_anxiety_spor.get("")
async def i_somatic_anxiety_spor():
    return {"p":"saude_mental_es_somatic_anxiety_spor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sport_psychology2.get("")
async def i_sport_psychology2():
    return {"p":"saude_mental_es_sport_psychology2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_state_anxiety_sport.get("")
async def i_state_anxiety_sport():
    return {"p":"saude_mental_es_state_anxiety_sport","s":"ativo","t":datetime.utcnow().isoformat()}
@router_student_athlete.get("")
async def i_student_athlete():
    return {"p":"saude_mental_es_student_athlete","s":"ativo","t":datetime.utcnow().isoformat()}
@router_task_cohesion.get("")
async def i_task_cohesion():
    return {"p":"saude_mental_es_task_cohesion","s":"ativo","t":datetime.utcnow().isoformat()}
@router_team_cohesion.get("")
async def i_team_cohesion():
    return {"p":"saude_mental_es_team_cohesion","s":"ativo","t":datetime.utcnow().isoformat()}
@router_team_culture.get("")
async def i_team_culture():
    return {"p":"saude_mental_es_team_culture","s":"ativo","t":datetime.utcnow().isoformat()}
@router_thought_stopping.get("")
async def i_thought_stopping():
    return {"p":"saude_mental_es_thought_stopping","s":"ativo","t":datetime.utcnow().isoformat()}
@router_trait_anxiety_sport.get("")
async def i_trait_anxiety_sport():
    return {"p":"saude_mental_es_trait_anxiety_sport","s":"ativo","t":datetime.utcnow().isoformat()}
@router_visual_imagery.get("")
async def i_visual_imagery():
    return {"p":"saude_mental_es_visual_imagery","s":"ativo","t":datetime.utcnow().isoformat()}
@router_vividness.get("")
async def i_vividness():
    return {"p":"saude_mental_es_vividness","s":"ativo","t":datetime.utcnow().isoformat()}
@router_zone_performance.get("")
async def i_zone_performance():
    return {"p":"saude_mental_es_zone_performance","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_saude_mental_esporte(PluginBase):
    name = "consolidated_saude_mental_esporte"
    def setup(self, app):
        app.include_router(router_PETTLEP_model)
        app.include_router(router_abuse_sport)
        app.include_router(router_achievement_goal_the)
        app.include_router(router_athletic_burnout)
        app.include_router(router_athletic_identity)
        app.include_router(router_attentional_focus)
        app.include_router(router_attentional_style)
        app.include_router(router_auditory_imagery)
        app.include_router(router_autonomy_sport)
        app.include_router(router_basic_needs_sport)
        app.include_router(router_broad_focus)
        app.include_router(router_burnout_sport2)
        app.include_router(router_career_transition_sp)
        app.include_router(router_choking_under_pressu)
        app.include_router(router_cognitive_anxiety_sp)
        app.include_router(router_cognitive_restructur)
        app.include_router(router_competence_sport)
        app.include_router(router_competition_plan)
        app.include_router(router_competition_simulati)
        app.include_router(router_competitive_anxiety)
        app.include_router(router_confidence_sport)
        app.include_router(router_controllability_imag)
        app.include_router(router_cue_words)
        app.include_router(router_dual_career_athletes)
        app.include_router(router_emotional_imagery)
        app.include_router(router_external_focus)
        app.include_router(router_extrinsic_motivation)
        app.include_router(router_game_plan)
        app.include_router(router_goal_setting_sport)
        app.include_router(router_goal_setting_theory2)
        app.include_router(router_grit_sport)
        app.include_router(router_group_dynamics_sport)
        app.include_router(router_gustatory_imagery)
        app.include_router(router_hazing_sport)
        app.include_router(router_identity_foreclosure)
        app.include_router(router_imagery_sport)
        app.include_router(router_injury_psychology)
        app.include_router(router_injury_rehabilitatio)
        app.include_router(router_instructional_self_t)
        app.include_router(router_internal_external_im)
        app.include_router(router_internal_focus)
        app.include_router(router_intrinsic_motivation)
        app.include_router(router_kinesthetic_imagery)
        app.include_router(router_leadership_sport)
        app.include_router(router_locke_latham_goals)
        app.include_router(router_locker_room_culture)
        app.include_router(router_long_term_goals_spor)
        app.include_router(router_mastery_climate)
        app.include_router(router_mental_health_olympi)
        app.include_router(router_mental_rehearsal)
        app.include_router(router_mental_skills_traini)
        app.include_router(router_mental_strength)
        app.include_router(router_mental_toughness)
        app.include_router(router_motivational_self_ta)
        app.include_router(router_narrow_focus)
        app.include_router(router_negative_self_talk)
        app.include_router(router_olfactory_imagery)
        app.include_router(router_optimal_anxiety)
        app.include_router(router_outcome_goals)
        app.include_router(router_overtraining_syndrom)
        app.include_router(router_pain_tolerance)
        app.include_router(router_performance_anxiety_)
        app.include_router(router_performance_climate)
        app.include_router(router_performance_goals)
        app.include_router(router_performance_psycholo)
        app.include_router(router_positive_self_talk)
        app.include_router(router_pre_competition_rout)
        app.include_router(router_pre_performance_rout)
        app.include_router(router_process_goals)
        app.include_router(router_professional_athlete)
        app.include_router(router_psychological_resili)
        app.include_router(router_race_plan)
        app.include_router(router_reframing_sport)
        app.include_router(router_relatedness_sport)
        app.include_router(router_retirement_sport)
        app.include_router(router_return_to_sport)
        app.include_router(router_self_confidence_spor)
        app.include_router(router_self_determination_s)
        app.include_router(router_self_efficacy_sport)
        app.include_router(router_self_talk_sport)
        app.include_router(router_sexual_harassment_sp)
        app.include_router(router_short_term_goals_spo)
        app.include_router(router_social_cohesion)
        app.include_router(router_somatic_anxiety_spor)
        app.include_router(router_sport_psychology2)
        app.include_router(router_state_anxiety_sport)
        app.include_router(router_student_athlete)
        app.include_router(router_task_cohesion)
        app.include_router(router_team_cohesion)
        app.include_router(router_team_culture)
        app.include_router(router_thought_stopping)
        app.include_router(router_trait_anxiety_sport)
        app.include_router(router_visual_imagery)
        app.include_router(router_vividness)
        app.include_router(router_zone_performance)


plugin = Plugin_saude_mental_esporte()
