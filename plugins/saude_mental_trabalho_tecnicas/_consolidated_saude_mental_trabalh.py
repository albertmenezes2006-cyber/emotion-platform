from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_absenteeism_interven = APIRouter(prefix="/api/v1/saude_mental/absenteeism_intervention", tags=["saude_mental_trabalho_tecnicas"])
router_accommodations_menta = APIRouter(prefix="/api/v1/saude_mental/accommodations_mental", tags=["saude_mental_trabalho_tecnicas"])
router_autonomy_interventio = APIRouter(prefix="/api/v1/saude_mental/autonomy_intervention", tags=["saude_mental_trabalho_tecnicas"])
router_brief_therapy_eap = APIRouter(prefix="/api/v1/saude_mental/brief_therapy_eap", tags=["saude_mental_trabalho_tecnicas"])
router_burnout_survey = APIRouter(prefix="/api/v1/saude_mental/burnout_survey", tags=["saude_mental_trabalho_tecnicas"])
router_career_counseling_ea = APIRouter(prefix="/api/v1/saude_mental/career_counseling_eap", tags=["saude_mental_trabalho_tecnicas"])
router_caregiving_support_w = APIRouter(prefix="/api/v1/saude_mental/caregiving_support_work", tags=["saude_mental_trabalho_tecnicas"])
router_cbt_eap = APIRouter(prefix="/api/v1/saude_mental/cbt_eap", tags=["saude_mental_trabalho_tecnicas"])
router_childcare_work = APIRouter(prefix="/api/v1/saude_mental/childcare_work", tags=["saude_mental_trabalho_tecnicas"])
router_climate_fairness = APIRouter(prefix="/api/v1/saude_mental/climate_fairness", tags=["saude_mental_trabalho_tecnicas"])
router_climate_survey = APIRouter(prefix="/api/v1/saude_mental/climate_survey", tags=["saude_mental_trabalho_tecnicas"])
router_coaching_eap = APIRouter(prefix="/api/v1/saude_mental/coaching_eap", tags=["saude_mental_trabalho_tecnicas"])
router_communication_work = APIRouter(prefix="/api/v1/saude_mental/communication_work", tags=["saude_mental_trabalho_tecnicas"])
router_conflict_resolution_ = APIRouter(prefix="/api/v1/saude_mental/conflict_resolution_work", tags=["saude_mental_trabalho_tecnicas"])
router_creativity_work2 = APIRouter(prefix="/api/v1/saude_mental/creativity_work2", tags=["saude_mental_trabalho_tecnicas"])
router_crisis_eap = APIRouter(prefix="/api/v1/saude_mental/crisis_eap", tags=["saude_mental_trabalho_tecnicas"])
router_critical_incident_ea = APIRouter(prefix="/api/v1/saude_mental/critical_incident_eap", tags=["saude_mental_trabalho_tecnicas"])
router_culture_assessment = APIRouter(prefix="/api/v1/saude_mental/culture_assessment", tags=["saude_mental_trabalho_tecnicas"])
router_debriefing_eap = APIRouter(prefix="/api/v1/saude_mental/debriefing_eap", tags=["saude_mental_trabalho_tecnicas"])
router_demand_control_inter = APIRouter(prefix="/api/v1/saude_mental/demand_control_interventi", tags=["saude_mental_trabalho_tecnicas"])
router_disability_managemen = APIRouter(prefix="/api/v1/saude_mental/disability_management", tags=["saude_mental_trabalho_tecnicas"])
router_eap_evaluation = APIRouter(prefix="/api/v1/saude_mental/eap_evaluation", tags=["saude_mental_trabalho_tecnicas"])
router_eap_implementation = APIRouter(prefix="/api/v1/saude_mental/eap_implementation", tags=["saude_mental_trabalho_tecnicas"])
router_eap_utilization = APIRouter(prefix="/api/v1/saude_mental/eap_utilization", tags=["saude_mental_trabalho_tecnicas"])
router_effort_reward_interv = APIRouter(prefix="/api/v1/saude_mental/effort_reward_interventio", tags=["saude_mental_trabalho_tecnicas"])
router_elder_care_work = APIRouter(prefix="/api/v1/saude_mental/elder_care_work", tags=["saude_mental_trabalho_tecnicas"])
router_engagement_survey = APIRouter(prefix="/api/v1/saude_mental/engagement_survey", tags=["saude_mental_trabalho_tecnicas"])
router_exercise_workplace = APIRouter(prefix="/api/v1/saude_mental/exercise_workplace", tags=["saude_mental_trabalho_tecnicas"])
router_family_counseling_ea = APIRouter(prefix="/api/v1/saude_mental/family_counseling_eap", tags=["saude_mental_trabalho_tecnicas"])
router_financial_counseling = APIRouter(prefix="/api/v1/saude_mental/financial_counseling_eap", tags=["saude_mental_trabalho_tecnicas"])
router_financial_wellness = APIRouter(prefix="/api/v1/saude_mental/financial_wellness", tags=["saude_mental_trabalho_tecnicas"])
router_flexible_working = APIRouter(prefix="/api/v1/saude_mental/flexible_working", tags=["saude_mental_trabalho_tecnicas"])
router_group_dynamics_work = APIRouter(prefix="/api/v1/saude_mental/group_dynamics_work", tags=["saude_mental_trabalho_tecnicas"])
router_hybrid_work_design = APIRouter(prefix="/api/v1/saude_mental/hybrid_work_design", tags=["saude_mental_trabalho_tecnicas"])
router_individual_intervent = APIRouter(prefix="/api/v1/saude_mental/individual_intervention", tags=["saude_mental_trabalho_tecnicas"])
router_innovation_mental = APIRouter(prefix="/api/v1/saude_mental/innovation_mental", tags=["saude_mental_trabalho_tecnicas"])
router_intervencao_trabalho = APIRouter(prefix="/api/v1/saude_mental/intervencao_trabalho", tags=["saude_mental_trabalho_tecnicas"])
router_job_demands_assessme = APIRouter(prefix="/api/v1/saude_mental/job_demands_assessment", tags=["saude_mental_trabalho_tecnicas"])
router_job_redesign = APIRouter(prefix="/api/v1/saude_mental/job_redesign", tags=["saude_mental_trabalho_tecnicas"])
router_leadership_developme = APIRouter(prefix="/api/v1/saude_mental/leadership_development_me", tags=["saude_mental_trabalho_tecnicas"])
router_legal_counseling_eap = APIRouter(prefix="/api/v1/saude_mental/legal_counseling_eap", tags=["saude_mental_trabalho_tecnicas"])
router_manager_training = APIRouter(prefix="/api/v1/saude_mental/manager_training", tags=["saude_mental_trabalho_tecnicas"])
router_mastery_intervention = APIRouter(prefix="/api/v1/saude_mental/mastery_intervention", tags=["saude_mental_trabalho_tecnicas"])
router_mindfulness_eap = APIRouter(prefix="/api/v1/saude_mental/mindfulness_eap", tags=["saude_mental_trabalho_tecnicas"])
router_mindfulness_workplac = APIRouter(prefix="/api/v1/saude_mental/mindfulness_workplace2", tags=["saude_mental_trabalho_tecnicas"])
router_nutrition_workplace = APIRouter(prefix="/api/v1/saude_mental/nutrition_workplace", tags=["saude_mental_trabalho_tecnicas"])
router_organizational_asses = APIRouter(prefix="/api/v1/saude_mental/organizational_assessment", tags=["saude_mental_trabalho_tecnicas"])
router_organizational_inter = APIRouter(prefix="/api/v1/saude_mental/organizational_interventi", tags=["saude_mental_trabalho_tecnicas"])
router_organizational_justi = APIRouter(prefix="/api/v1/saude_mental/organizational_justice2", tags=["saude_mental_trabalho_tecnicas"])
router_parental_leave_menta = APIRouter(prefix="/api/v1/saude_mental/parental_leave_mental", tags=["saude_mental_trabalho_tecnicas"])
router_performance_mental = APIRouter(prefix="/api/v1/saude_mental/performance_mental", tags=["saude_mental_trabalho_tecnicas"])
router_presenteeism_interve = APIRouter(prefix="/api/v1/saude_mental/presenteeism_intervention", tags=["saude_mental_trabalho_tecnicas"])
router_productivity_mental = APIRouter(prefix="/api/v1/saude_mental/productivity_mental", tags=["saude_mental_trabalho_tecnicas"])
router_programa_eap2 = APIRouter(prefix="/api/v1/saude_mental/programa_eap2", tags=["saude_mental_trabalho_tecnicas"])
router_psychological_contra = APIRouter(prefix="/api/v1/saude_mental/psychological_contract", tags=["saude_mental_trabalho_tecnicas"])
router_psychological_safety = APIRouter(prefix="/api/v1/saude_mental/psychological_safety_trai", tags=["saude_mental_trabalho_tecnicas"])
router_psychosocial_risk = APIRouter(prefix="/api/v1/saude_mental/psychosocial_risk", tags=["saude_mental_trabalho_tecnicas"])
router_purpose_work_interve = APIRouter(prefix="/api/v1/saude_mental/purpose_work_intervention", tags=["saude_mental_trabalho_tecnicas"])
router_remote_work_design = APIRouter(prefix="/api/v1/saude_mental/remote_work_design", tags=["saude_mental_trabalho_tecnicas"])
router_resilience_eap = APIRouter(prefix="/api/v1/saude_mental/resilience_eap", tags=["saude_mental_trabalho_tecnicas"])
router_resilience_training_ = APIRouter(prefix="/api/v1/saude_mental/resilience_training_work", tags=["saude_mental_trabalho_tecnicas"])
router_resources_assessment = APIRouter(prefix="/api/v1/saude_mental/resources_assessment", tags=["saude_mental_trabalho_tecnicas"])
router_return_to_work_menta = APIRouter(prefix="/api/v1/saude_mental/return_to_work_mental", tags=["saude_mental_trabalho_tecnicas"])
router_sleep_workplace = APIRouter(prefix="/api/v1/saude_mental/sleep_workplace", tags=["saude_mental_trabalho_tecnicas"])
router_social_support_work = APIRouter(prefix="/api/v1/saude_mental/social_support_work", tags=["saude_mental_trabalho_tecnicas"])
router_solution_focused_eap = APIRouter(prefix="/api/v1/saude_mental/solution_focused_eap", tags=["saude_mental_trabalho_tecnicas"])
router_stress_management_ea = APIRouter(prefix="/api/v1/saude_mental/stress_management_eap", tags=["saude_mental_trabalho_tecnicas"])
router_substance_eap = APIRouter(prefix="/api/v1/saude_mental/substance_eap", tags=["saude_mental_trabalho_tecnicas"])
router_supervisor_training = APIRouter(prefix="/api/v1/saude_mental/supervisor_training", tags=["saude_mental_trabalho_tecnicas"])
router_team_effectiveness = APIRouter(prefix="/api/v1/saude_mental/team_effectiveness", tags=["saude_mental_trabalho_tecnicas"])
router_trust_building = APIRouter(prefix="/api/v1/saude_mental/trust_building", tags=["saude_mental_trabalho_tecnicas"])
router_work_life_programs = APIRouter(prefix="/api/v1/saude_mental/work_life_programs", tags=["saude_mental_trabalho_tecnicas"])
router_work_schedule = APIRouter(prefix="/api/v1/saude_mental/work_schedule", tags=["saude_mental_trabalho_tecnicas"])
router_work_stress_interven = APIRouter(prefix="/api/v1/saude_mental/work_stress_intervention", tags=["saude_mental_trabalho_tecnicas"])
router_yoga_workplace = APIRouter(prefix="/api/v1/saude_mental/yoga_workplace", tags=["saude_mental_trabalho_tecnicas"])

@router_absenteeism_interven.get("")
async def i_absenteeism_interven():
    return {"p":"saude_mental_tr_absenteeism_interven","s":"ativo","t":datetime.utcnow().isoformat()}
@router_accommodations_menta.get("")
async def i_accommodations_menta():
    return {"p":"saude_mental_tr_accommodations_menta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autonomy_interventio.get("")
async def i_autonomy_interventio():
    return {"p":"saude_mental_tr_autonomy_interventio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_brief_therapy_eap.get("")
async def i_brief_therapy_eap():
    return {"p":"saude_mental_tr_brief_therapy_eap","s":"ativo","t":datetime.utcnow().isoformat()}
@router_burnout_survey.get("")
async def i_burnout_survey():
    return {"p":"saude_mental_tr_burnout_survey","s":"ativo","t":datetime.utcnow().isoformat()}
@router_career_counseling_ea.get("")
async def i_career_counseling_ea():
    return {"p":"saude_mental_tr_career_counseling_ea","s":"ativo","t":datetime.utcnow().isoformat()}
@router_caregiving_support_w.get("")
async def i_caregiving_support_w():
    return {"p":"saude_mental_tr_caregiving_support_w","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cbt_eap.get("")
async def i_cbt_eap():
    return {"p":"saude_mental_tr_cbt_eap","s":"ativo","t":datetime.utcnow().isoformat()}
@router_childcare_work.get("")
async def i_childcare_work():
    return {"p":"saude_mental_tr_childcare_work","s":"ativo","t":datetime.utcnow().isoformat()}
@router_climate_fairness.get("")
async def i_climate_fairness():
    return {"p":"saude_mental_tr_climate_fairness","s":"ativo","t":datetime.utcnow().isoformat()}
@router_climate_survey.get("")
async def i_climate_survey():
    return {"p":"saude_mental_tr_climate_survey","s":"ativo","t":datetime.utcnow().isoformat()}
@router_coaching_eap.get("")
async def i_coaching_eap():
    return {"p":"saude_mental_tr_coaching_eap","s":"ativo","t":datetime.utcnow().isoformat()}
@router_communication_work.get("")
async def i_communication_work():
    return {"p":"saude_mental_tr_communication_work","s":"ativo","t":datetime.utcnow().isoformat()}
@router_conflict_resolution_.get("")
async def i_conflict_resolution_():
    return {"p":"saude_mental_tr_conflict_resolution_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_creativity_work2.get("")
async def i_creativity_work2():
    return {"p":"saude_mental_tr_creativity_work2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_crisis_eap.get("")
async def i_crisis_eap():
    return {"p":"saude_mental_tr_crisis_eap","s":"ativo","t":datetime.utcnow().isoformat()}
@router_critical_incident_ea.get("")
async def i_critical_incident_ea():
    return {"p":"saude_mental_tr_critical_incident_ea","s":"ativo","t":datetime.utcnow().isoformat()}
@router_culture_assessment.get("")
async def i_culture_assessment():
    return {"p":"saude_mental_tr_culture_assessment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_debriefing_eap.get("")
async def i_debriefing_eap():
    return {"p":"saude_mental_tr_debriefing_eap","s":"ativo","t":datetime.utcnow().isoformat()}
@router_demand_control_inter.get("")
async def i_demand_control_inter():
    return {"p":"saude_mental_tr_demand_control_inter","s":"ativo","t":datetime.utcnow().isoformat()}
@router_disability_managemen.get("")
async def i_disability_managemen():
    return {"p":"saude_mental_tr_disability_managemen","s":"ativo","t":datetime.utcnow().isoformat()}
@router_eap_evaluation.get("")
async def i_eap_evaluation():
    return {"p":"saude_mental_tr_eap_evaluation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_eap_implementation.get("")
async def i_eap_implementation():
    return {"p":"saude_mental_tr_eap_implementation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_eap_utilization.get("")
async def i_eap_utilization():
    return {"p":"saude_mental_tr_eap_utilization","s":"ativo","t":datetime.utcnow().isoformat()}
@router_effort_reward_interv.get("")
async def i_effort_reward_interv():
    return {"p":"saude_mental_tr_effort_reward_interv","s":"ativo","t":datetime.utcnow().isoformat()}
@router_elder_care_work.get("")
async def i_elder_care_work():
    return {"p":"saude_mental_tr_elder_care_work","s":"ativo","t":datetime.utcnow().isoformat()}
@router_engagement_survey.get("")
async def i_engagement_survey():
    return {"p":"saude_mental_tr_engagement_survey","s":"ativo","t":datetime.utcnow().isoformat()}
@router_exercise_workplace.get("")
async def i_exercise_workplace():
    return {"p":"saude_mental_tr_exercise_workplace","s":"ativo","t":datetime.utcnow().isoformat()}
@router_family_counseling_ea.get("")
async def i_family_counseling_ea():
    return {"p":"saude_mental_tr_family_counseling_ea","s":"ativo","t":datetime.utcnow().isoformat()}
@router_financial_counseling.get("")
async def i_financial_counseling():
    return {"p":"saude_mental_tr_financial_counseling","s":"ativo","t":datetime.utcnow().isoformat()}
@router_financial_wellness.get("")
async def i_financial_wellness():
    return {"p":"saude_mental_tr_financial_wellness","s":"ativo","t":datetime.utcnow().isoformat()}
@router_flexible_working.get("")
async def i_flexible_working():
    return {"p":"saude_mental_tr_flexible_working","s":"ativo","t":datetime.utcnow().isoformat()}
@router_group_dynamics_work.get("")
async def i_group_dynamics_work():
    return {"p":"saude_mental_tr_group_dynamics_work","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hybrid_work_design.get("")
async def i_hybrid_work_design():
    return {"p":"saude_mental_tr_hybrid_work_design","s":"ativo","t":datetime.utcnow().isoformat()}
@router_individual_intervent.get("")
async def i_individual_intervent():
    return {"p":"saude_mental_tr_individual_intervent","s":"ativo","t":datetime.utcnow().isoformat()}
@router_innovation_mental.get("")
async def i_innovation_mental():
    return {"p":"saude_mental_tr_innovation_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_intervencao_trabalho.get("")
async def i_intervencao_trabalho():
    return {"p":"saude_mental_tr_intervencao_trabalho","s":"ativo","t":datetime.utcnow().isoformat()}
@router_job_demands_assessme.get("")
async def i_job_demands_assessme():
    return {"p":"saude_mental_tr_job_demands_assessme","s":"ativo","t":datetime.utcnow().isoformat()}
@router_job_redesign.get("")
async def i_job_redesign():
    return {"p":"saude_mental_tr_job_redesign","s":"ativo","t":datetime.utcnow().isoformat()}
@router_leadership_developme.get("")
async def i_leadership_developme():
    return {"p":"saude_mental_tr_leadership_developme","s":"ativo","t":datetime.utcnow().isoformat()}
@router_legal_counseling_eap.get("")
async def i_legal_counseling_eap():
    return {"p":"saude_mental_tr_legal_counseling_eap","s":"ativo","t":datetime.utcnow().isoformat()}
@router_manager_training.get("")
async def i_manager_training():
    return {"p":"saude_mental_tr_manager_training","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mastery_intervention.get("")
async def i_mastery_intervention():
    return {"p":"saude_mental_tr_mastery_intervention","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindfulness_eap.get("")
async def i_mindfulness_eap():
    return {"p":"saude_mental_tr_mindfulness_eap","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindfulness_workplac.get("")
async def i_mindfulness_workplac():
    return {"p":"saude_mental_tr_mindfulness_workplac","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nutrition_workplace.get("")
async def i_nutrition_workplace():
    return {"p":"saude_mental_tr_nutrition_workplace","s":"ativo","t":datetime.utcnow().isoformat()}
@router_organizational_asses.get("")
async def i_organizational_asses():
    return {"p":"saude_mental_tr_organizational_asses","s":"ativo","t":datetime.utcnow().isoformat()}
@router_organizational_inter.get("")
async def i_organizational_inter():
    return {"p":"saude_mental_tr_organizational_inter","s":"ativo","t":datetime.utcnow().isoformat()}
@router_organizational_justi.get("")
async def i_organizational_justi():
    return {"p":"saude_mental_tr_organizational_justi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_parental_leave_menta.get("")
async def i_parental_leave_menta():
    return {"p":"saude_mental_tr_parental_leave_menta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_performance_mental.get("")
async def i_performance_mental():
    return {"p":"saude_mental_tr_performance_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_presenteeism_interve.get("")
async def i_presenteeism_interve():
    return {"p":"saude_mental_tr_presenteeism_interve","s":"ativo","t":datetime.utcnow().isoformat()}
@router_productivity_mental.get("")
async def i_productivity_mental():
    return {"p":"saude_mental_tr_productivity_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_programa_eap2.get("")
async def i_programa_eap2():
    return {"p":"saude_mental_tr_programa_eap2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psychological_contra.get("")
async def i_psychological_contra():
    return {"p":"saude_mental_tr_psychological_contra","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psychological_safety.get("")
async def i_psychological_safety():
    return {"p":"saude_mental_tr_psychological_safety","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psychosocial_risk.get("")
async def i_psychosocial_risk():
    return {"p":"saude_mental_tr_psychosocial_risk","s":"ativo","t":datetime.utcnow().isoformat()}
@router_purpose_work_interve.get("")
async def i_purpose_work_interve():
    return {"p":"saude_mental_tr_purpose_work_interve","s":"ativo","t":datetime.utcnow().isoformat()}
@router_remote_work_design.get("")
async def i_remote_work_design():
    return {"p":"saude_mental_tr_remote_work_design","s":"ativo","t":datetime.utcnow().isoformat()}
@router_resilience_eap.get("")
async def i_resilience_eap():
    return {"p":"saude_mental_tr_resilience_eap","s":"ativo","t":datetime.utcnow().isoformat()}
@router_resilience_training_.get("")
async def i_resilience_training_():
    return {"p":"saude_mental_tr_resilience_training_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_resources_assessment.get("")
async def i_resources_assessment():
    return {"p":"saude_mental_tr_resources_assessment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_return_to_work_menta.get("")
async def i_return_to_work_menta():
    return {"p":"saude_mental_tr_return_to_work_menta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sleep_workplace.get("")
async def i_sleep_workplace():
    return {"p":"saude_mental_tr_sleep_workplace","s":"ativo","t":datetime.utcnow().isoformat()}
@router_social_support_work.get("")
async def i_social_support_work():
    return {"p":"saude_mental_tr_social_support_work","s":"ativo","t":datetime.utcnow().isoformat()}
@router_solution_focused_eap.get("")
async def i_solution_focused_eap():
    return {"p":"saude_mental_tr_solution_focused_eap","s":"ativo","t":datetime.utcnow().isoformat()}
@router_stress_management_ea.get("")
async def i_stress_management_ea():
    return {"p":"saude_mental_tr_stress_management_ea","s":"ativo","t":datetime.utcnow().isoformat()}
@router_substance_eap.get("")
async def i_substance_eap():
    return {"p":"saude_mental_tr_substance_eap","s":"ativo","t":datetime.utcnow().isoformat()}
@router_supervisor_training.get("")
async def i_supervisor_training():
    return {"p":"saude_mental_tr_supervisor_training","s":"ativo","t":datetime.utcnow().isoformat()}
@router_team_effectiveness.get("")
async def i_team_effectiveness():
    return {"p":"saude_mental_tr_team_effectiveness","s":"ativo","t":datetime.utcnow().isoformat()}
@router_trust_building.get("")
async def i_trust_building():
    return {"p":"saude_mental_tr_trust_building","s":"ativo","t":datetime.utcnow().isoformat()}
@router_work_life_programs.get("")
async def i_work_life_programs():
    return {"p":"saude_mental_tr_work_life_programs","s":"ativo","t":datetime.utcnow().isoformat()}
@router_work_schedule.get("")
async def i_work_schedule():
    return {"p":"saude_mental_tr_work_schedule","s":"ativo","t":datetime.utcnow().isoformat()}
@router_work_stress_interven.get("")
async def i_work_stress_interven():
    return {"p":"saude_mental_tr_work_stress_interven","s":"ativo","t":datetime.utcnow().isoformat()}
@router_yoga_workplace.get("")
async def i_yoga_workplace():
    return {"p":"saude_mental_tr_yoga_workplace","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_saude_mental_trabalh(PluginBase):
    name = "consolidated_saude_mental_trabalho_tecnicas"
    def setup(self, app):
        app.include_router(router_absenteeism_interven)
        app.include_router(router_accommodations_menta)
        app.include_router(router_autonomy_interventio)
        app.include_router(router_brief_therapy_eap)
        app.include_router(router_burnout_survey)
        app.include_router(router_career_counseling_ea)
        app.include_router(router_caregiving_support_w)
        app.include_router(router_cbt_eap)
        app.include_router(router_childcare_work)
        app.include_router(router_climate_fairness)
        app.include_router(router_climate_survey)
        app.include_router(router_coaching_eap)
        app.include_router(router_communication_work)
        app.include_router(router_conflict_resolution_)
        app.include_router(router_creativity_work2)
        app.include_router(router_crisis_eap)
        app.include_router(router_critical_incident_ea)
        app.include_router(router_culture_assessment)
        app.include_router(router_debriefing_eap)
        app.include_router(router_demand_control_inter)
        app.include_router(router_disability_managemen)
        app.include_router(router_eap_evaluation)
        app.include_router(router_eap_implementation)
        app.include_router(router_eap_utilization)
        app.include_router(router_effort_reward_interv)
        app.include_router(router_elder_care_work)
        app.include_router(router_engagement_survey)
        app.include_router(router_exercise_workplace)
        app.include_router(router_family_counseling_ea)
        app.include_router(router_financial_counseling)
        app.include_router(router_financial_wellness)
        app.include_router(router_flexible_working)
        app.include_router(router_group_dynamics_work)
        app.include_router(router_hybrid_work_design)
        app.include_router(router_individual_intervent)
        app.include_router(router_innovation_mental)
        app.include_router(router_intervencao_trabalho)
        app.include_router(router_job_demands_assessme)
        app.include_router(router_job_redesign)
        app.include_router(router_leadership_developme)
        app.include_router(router_legal_counseling_eap)
        app.include_router(router_manager_training)
        app.include_router(router_mastery_intervention)
        app.include_router(router_mindfulness_eap)
        app.include_router(router_mindfulness_workplac)
        app.include_router(router_nutrition_workplace)
        app.include_router(router_organizational_asses)
        app.include_router(router_organizational_inter)
        app.include_router(router_organizational_justi)
        app.include_router(router_parental_leave_menta)
        app.include_router(router_performance_mental)
        app.include_router(router_presenteeism_interve)
        app.include_router(router_productivity_mental)
        app.include_router(router_programa_eap2)
        app.include_router(router_psychological_contra)
        app.include_router(router_psychological_safety)
        app.include_router(router_psychosocial_risk)
        app.include_router(router_purpose_work_interve)
        app.include_router(router_remote_work_design)
        app.include_router(router_resilience_eap)
        app.include_router(router_resilience_training_)
        app.include_router(router_resources_assessment)
        app.include_router(router_return_to_work_menta)
        app.include_router(router_sleep_workplace)
        app.include_router(router_social_support_work)
        app.include_router(router_solution_focused_eap)
        app.include_router(router_stress_management_ea)
        app.include_router(router_substance_eap)
        app.include_router(router_supervisor_training)
        app.include_router(router_team_effectiveness)
        app.include_router(router_trust_building)
        app.include_router(router_work_life_programs)
        app.include_router(router_work_schedule)
        app.include_router(router_work_stress_interven)
        app.include_router(router_yoga_workplace)


plugin = Plugin_saude_mental_trabalh()
