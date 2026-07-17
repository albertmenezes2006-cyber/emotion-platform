from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_BASIC_ID = APIRouter(prefix="/api/v1/abordagens_i/BASIC_ID", tags=["abordagens_integrativas"])
router_CFT_DBT_integration = APIRouter(prefix="/api/v1/abordagens_i/CFT_DBT_integration", tags=["abordagens_integrativas"])
router_DBT_ACT_integration = APIRouter(prefix="/api/v1/abordagens_i/DBT_ACT_integration", tags=["abordagens_integrativas"])
router_EMDR_integrative = APIRouter(prefix="/api/v1/abordagens_i/EMDR_integrative", tags=["abordagens_integrativas"])
router_EMDR_somatic = APIRouter(prefix="/api/v1/abordagens_i/EMDR_somatic", tags=["abordagens_integrativas"])
router_IPT_CBT = APIRouter(prefix="/api/v1/abordagens_i/IPT_CBT", tags=["abordagens_integrativas"])
router_anti_oppressive = APIRouter(prefix="/api/v1/abordagens_i/anti_oppressive", tags=["abordagens_integrativas"])
router_app_CBT = APIRouter(prefix="/api/v1/abordagens_i/app_CBT", tags=["abordagens_integrativas"])
router_assimilativa_integra = APIRouter(prefix="/api/v1/abordagens_i/assimilativa_integration", tags=["abordagens_integrativas"])
router_attachment_informed = APIRouter(prefix="/api/v1/abordagens_i/attachment_informed", tags=["abordagens_integrativas"])
router_bibliotherapy_CBT = APIRouter(prefix="/api/v1/abordagens_i/bibliotherapy_CBT", tags=["abordagens_integrativas"])
router_blended_CBT = APIRouter(prefix="/api/v1/abordagens_i/blended_CBT", tags=["abordagens_integrativas"])
router_body_oriented_integr = APIRouter(prefix="/api/v1/abordagens_i/body_oriented_integrative", tags=["abordagens_integrativas"])
router_brief_CBT = APIRouter(prefix="/api/v1/abordagens_i/brief_CBT", tags=["abordagens_integrativas"])
router_brief_strategic_fami = APIRouter(prefix="/api/v1/abordagens_i/brief_strategic_family", tags=["abordagens_integrativas"])
router_common_factors_appro = APIRouter(prefix="/api/v1/abordagens_i/common_factors_approach", tags=["abordagens_integrativas"])
router_community_psychology = APIRouter(prefix="/api/v1/abordagens_i/community_psychology_clin", tags=["abordagens_integrativas"])
router_computerized_CBT = APIRouter(prefix="/api/v1/abordagens_i/computerized_CBT", tags=["abordagens_integrativas"])
router_core_beliefs_integra = APIRouter(prefix="/api/v1/abordagens_i/core_beliefs_integrative", tags=["abordagens_integrativas"])
router_culturally_adapted = APIRouter(prefix="/api/v1/abordagens_i/culturally_adapted", tags=["abordagens_integrativas"])
router_culturally_humble_ap = APIRouter(prefix="/api/v1/abordagens_i/culturally_humble_approac", tags=["abordagens_integrativas"])
router_culturally_tailored = APIRouter(prefix="/api/v1/abordagens_i/culturally_tailored", tags=["abordagens_integrativas"])
router_developmental_couple = APIRouter(prefix="/api/v1/abordagens_i/developmental_couple", tags=["abordagens_integrativas"])
router_eclecticismo_asistem = APIRouter(prefix="/api/v1/abordagens_i/eclecticismo_asistematico", tags=["abordagens_integrativas"])
router_eclecticismo_tecnico = APIRouter(prefix="/api/v1/abordagens_i/eclecticismo_tecnico", tags=["abordagens_integrativas"])
router_emotionally_focused = APIRouter(prefix="/api/v1/abordagens_i/emotionally_focused", tags=["abordagens_integrativas"])
router_family_based2 = APIRouter(prefix="/api/v1/abordagens_i/family_based2", tags=["abordagens_integrativas"])
router_family_systems_indiv = APIRouter(prefix="/api/v1/abordagens_i/family_systems_individual", tags=["abordagens_integrativas"])
router_functional_family = APIRouter(prefix="/api/v1/abordagens_i/functional_family", tags=["abordagens_integrativas"])
router_gottman_method = APIRouter(prefix="/api/v1/abordagens_i/gottman_method", tags=["abordagens_integrativas"])
router_group_CBT = APIRouter(prefix="/api/v1/abordagens_i/group_CBT", tags=["abordagens_integrativas"])
router_high_frequency_CBT = APIRouter(prefix="/api/v1/abordagens_i/high_frequency_CBT", tags=["abordagens_integrativas"])
router_hold_me_tight = APIRouter(prefix="/api/v1/abordagens_i/hold_me_tight", tags=["abordagens_integrativas"])
router_imago_therapy = APIRouter(prefix="/api/v1/abordagens_i/imago_therapy", tags=["abordagens_integrativas"])
router_integracao_tecnica = APIRouter(prefix="/api/v1/abordagens_i/integracao_tecnica", tags=["abordagens_integrativas"])
router_integracao_teorica = APIRouter(prefix="/api/v1/abordagens_i/integracao_teorica", tags=["abordagens_integrativas"])
router_intensive_CBT = APIRouter(prefix="/api/v1/abordagens_i/intensive_CBT", tags=["abordagens_integrativas"])
router_intersectionality_cl = APIRouter(prefix="/api/v1/abordagens_i/intersectionality_clinica", tags=["abordagens_integrativas"])
router_liberation_psycholog = APIRouter(prefix="/api/v1/abordagens_i/liberation_psychology_cli", tags=["abordagens_integrativas"])
router_low_intensity_CBT = APIRouter(prefix="/api/v1/abordagens_i/low_intensity_CBT", tags=["abordagens_integrativas"])
router_milan_systemic2 = APIRouter(prefix="/api/v1/abordagens_i/milan_systemic2", tags=["abordagens_integrativas"])
router_mindfulness_ACT = APIRouter(prefix="/api/v1/abordagens_i/mindfulness_ACT", tags=["abordagens_integrativas"])
router_mindfulness_CBT = APIRouter(prefix="/api/v1/abordagens_i/mindfulness_CBT", tags=["abordagens_integrativas"])
router_mindfulness_DBT = APIRouter(prefix="/api/v1/abordagens_i/mindfulness_DBT", tags=["abordagens_integrativas"])
router_mindfulness_psychody = APIRouter(prefix="/api/v1/abordagens_i/mindfulness_psychodynamic", tags=["abordagens_integrativas"])
router_modular_treatment = APIRouter(prefix="/api/v1/abordagens_i/modular_treatment", tags=["abordagens_integrativas"])
router_motivational_CBT = APIRouter(prefix="/api/v1/abordagens_i/motivational_CBT", tags=["abordagens_integrativas"])
router_multidimensional_fam = APIRouter(prefix="/api/v1/abordagens_i/multidimensional_family", tags=["abordagens_integrativas"])
router_multimodal_therapy_l = APIRouter(prefix="/api/v1/abordagens_i/multimodal_therapy_lazaru", tags=["abordagens_integrativas"])
router_multisystemic = APIRouter(prefix="/api/v1/abordagens_i/multisystemic", tags=["abordagens_integrativas"])
router_narrative_CBT = APIRouter(prefix="/api/v1/abordagens_i/narrative_CBT", tags=["abordagens_integrativas"])
router_narrative_family = APIRouter(prefix="/api/v1/abordagens_i/narrative_family", tags=["abordagens_integrativas"])
router_neuroscience_informe = APIRouter(prefix="/api/v1/abordagens_i/neuroscience_informed", tags=["abordagens_integrativas"])
router_online_CBT = APIRouter(prefix="/api/v1/abordagens_i/online_CBT", tags=["abordagens_integrativas"])
router_parent_child_interac = APIRouter(prefix="/api/v1/abordagens_i/parent_child_interaction", tags=["abordagens_integrativas"])
router_parent_mediated = APIRouter(prefix="/api/v1/abordagens_i/parent_mediated", tags=["abordagens_integrativas"])
router_paul_therapy_questio = APIRouter(prefix="/api/v1/abordagens_i/paul_therapy_question", tags=["abordagens_integrativas"])
router_polyvagal_informed = APIRouter(prefix="/api/v1/abordagens_i/polyvagal_informed", tags=["abordagens_integrativas"])
router_positive_psychology_ = APIRouter(prefix="/api/v1/abordagens_i/positive_psychology_ACT", tags=["abordagens_integrativas"])
router_positive_psychology_ = APIRouter(prefix="/api/v1/abordagens_i/positive_psychology_CBT", tags=["abordagens_integrativas"])
router_positive_psychology_ = APIRouter(prefix="/api/v1/abordagens_i/positive_psychology_DBT", tags=["abordagens_integrativas"])
router_positive_psychology_ = APIRouter(prefix="/api/v1/abordagens_i/positive_psychology_mindf", tags=["abordagens_integrativas"])
router_prescriptive_matchin = APIRouter(prefix="/api/v1/abordagens_i/prescriptive_matching", tags=["abordagens_integrativas"])
router_psychobiological_cou = APIRouter(prefix="/api/v1/abordagens_i/psychobiological_couple", tags=["abordagens_integrativas"])
router_psychodynamic_cbt_in = APIRouter(prefix="/api/v1/abordagens_i/psychodynamic_cbt_integra", tags=["abordagens_integrativas"])
router_schema_EMDR = APIRouter(prefix="/api/v1/abordagens_i/schema_EMDR", tags=["abordagens_integrativas"])
router_schema_focused_integ = APIRouter(prefix="/api/v1/abordagens_i/schema_focused_integrativ", tags=["abordagens_integrativas"])
router_self_help_CBT = APIRouter(prefix="/api/v1/abordagens_i/self_help_CBT", tags=["abordagens_integrativas"])
router_sensorimotor_couple = APIRouter(prefix="/api/v1/abordagens_i/sensorimotor_couple", tags=["abordagens_integrativas"])
router_solution_family = APIRouter(prefix="/api/v1/abordagens_i/solution_family", tags=["abordagens_integrativas"])
router_solution_focused_CBT = APIRouter(prefix="/api/v1/abordagens_i/solution_focused_CBT", tags=["abordagens_integrativas"])
router_somatic_integrative = APIRouter(prefix="/api/v1/abordagens_i/somatic_integrative", tags=["abordagens_integrativas"])
router_stepped_CBT = APIRouter(prefix="/api/v1/abordagens_i/stepped_CBT", tags=["abordagens_integrativas"])
router_structural_family2 = APIRouter(prefix="/api/v1/abordagens_i/structural_family2", tags=["abordagens_integrativas"])
router_systemic_individual = APIRouter(prefix="/api/v1/abordagens_i/systemic_individual", tags=["abordagens_integrativas"])
router_telephone_CBT = APIRouter(prefix="/api/v1/abordagens_i/telephone_CBT", tags=["abordagens_integrativas"])
router_transdiagnostic_trea = APIRouter(prefix="/api/v1/abordagens_i/transdiagnostic_treatment", tags=["abordagens_integrativas"])
router_trauma_informed2 = APIRouter(prefix="/api/v1/abordagens_i/trauma_informed2", tags=["abordagens_integrativas"])
router_unified_protocol2 = APIRouter(prefix="/api/v1/abordagens_i/unified_protocol2", tags=["abordagens_integrativas"])
router_video_CBT = APIRouter(prefix="/api/v1/abordagens_i/video_CBT", tags=["abordagens_integrativas"])
router_wachtel_cyclical_psy = APIRouter(prefix="/api/v1/abordagens_i/wachtel_cyclical_psychody", tags=["abordagens_integrativas"])

@router_BASIC_ID.get("")
async def i_BASIC_ID():
    return {"p":"abordagens_inte_BASIC_ID","s":"ativo","t":datetime.utcnow().isoformat()}
@router_CFT_DBT_integration.get("")
async def i_CFT_DBT_integration():
    return {"p":"abordagens_inte_CFT_DBT_integration","s":"ativo","t":datetime.utcnow().isoformat()}
@router_DBT_ACT_integration.get("")
async def i_DBT_ACT_integration():
    return {"p":"abordagens_inte_DBT_ACT_integration","s":"ativo","t":datetime.utcnow().isoformat()}
@router_EMDR_integrative.get("")
async def i_EMDR_integrative():
    return {"p":"abordagens_inte_EMDR_integrative","s":"ativo","t":datetime.utcnow().isoformat()}
@router_EMDR_somatic.get("")
async def i_EMDR_somatic():
    return {"p":"abordagens_inte_EMDR_somatic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_IPT_CBT.get("")
async def i_IPT_CBT():
    return {"p":"abordagens_inte_IPT_CBT","s":"ativo","t":datetime.utcnow().isoformat()}
@router_anti_oppressive.get("")
async def i_anti_oppressive():
    return {"p":"abordagens_inte_anti_oppressive","s":"ativo","t":datetime.utcnow().isoformat()}
@router_app_CBT.get("")
async def i_app_CBT():
    return {"p":"abordagens_inte_app_CBT","s":"ativo","t":datetime.utcnow().isoformat()}
@router_assimilativa_integra.get("")
async def i_assimilativa_integra():
    return {"p":"abordagens_inte_assimilativa_integra","s":"ativo","t":datetime.utcnow().isoformat()}
@router_attachment_informed.get("")
async def i_attachment_informed():
    return {"p":"abordagens_inte_attachment_informed","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bibliotherapy_CBT.get("")
async def i_bibliotherapy_CBT():
    return {"p":"abordagens_inte_bibliotherapy_CBT","s":"ativo","t":datetime.utcnow().isoformat()}
@router_blended_CBT.get("")
async def i_blended_CBT():
    return {"p":"abordagens_inte_blended_CBT","s":"ativo","t":datetime.utcnow().isoformat()}
@router_body_oriented_integr.get("")
async def i_body_oriented_integr():
    return {"p":"abordagens_inte_body_oriented_integr","s":"ativo","t":datetime.utcnow().isoformat()}
@router_brief_CBT.get("")
async def i_brief_CBT():
    return {"p":"abordagens_inte_brief_CBT","s":"ativo","t":datetime.utcnow().isoformat()}
@router_brief_strategic_fami.get("")
async def i_brief_strategic_fami():
    return {"p":"abordagens_inte_brief_strategic_fami","s":"ativo","t":datetime.utcnow().isoformat()}
@router_common_factors_appro.get("")
async def i_common_factors_appro():
    return {"p":"abordagens_inte_common_factors_appro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_community_psychology.get("")
async def i_community_psychology():
    return {"p":"abordagens_inte_community_psychology","s":"ativo","t":datetime.utcnow().isoformat()}
@router_computerized_CBT.get("")
async def i_computerized_CBT():
    return {"p":"abordagens_inte_computerized_CBT","s":"ativo","t":datetime.utcnow().isoformat()}
@router_core_beliefs_integra.get("")
async def i_core_beliefs_integra():
    return {"p":"abordagens_inte_core_beliefs_integra","s":"ativo","t":datetime.utcnow().isoformat()}
@router_culturally_adapted.get("")
async def i_culturally_adapted():
    return {"p":"abordagens_inte_culturally_adapted","s":"ativo","t":datetime.utcnow().isoformat()}
@router_culturally_humble_ap.get("")
async def i_culturally_humble_ap():
    return {"p":"abordagens_inte_culturally_humble_ap","s":"ativo","t":datetime.utcnow().isoformat()}
@router_culturally_tailored.get("")
async def i_culturally_tailored():
    return {"p":"abordagens_inte_culturally_tailored","s":"ativo","t":datetime.utcnow().isoformat()}
@router_developmental_couple.get("")
async def i_developmental_couple():
    return {"p":"abordagens_inte_developmental_couple","s":"ativo","t":datetime.utcnow().isoformat()}
@router_eclecticismo_asistem.get("")
async def i_eclecticismo_asistem():
    return {"p":"abordagens_inte_eclecticismo_asistem","s":"ativo","t":datetime.utcnow().isoformat()}
@router_eclecticismo_tecnico.get("")
async def i_eclecticismo_tecnico():
    return {"p":"abordagens_inte_eclecticismo_tecnico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_emotionally_focused.get("")
async def i_emotionally_focused():
    return {"p":"abordagens_inte_emotionally_focused","s":"ativo","t":datetime.utcnow().isoformat()}
@router_family_based2.get("")
async def i_family_based2():
    return {"p":"abordagens_inte_family_based2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_family_systems_indiv.get("")
async def i_family_systems_indiv():
    return {"p":"abordagens_inte_family_systems_indiv","s":"ativo","t":datetime.utcnow().isoformat()}
@router_functional_family.get("")
async def i_functional_family():
    return {"p":"abordagens_inte_functional_family","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gottman_method.get("")
async def i_gottman_method():
    return {"p":"abordagens_inte_gottman_method","s":"ativo","t":datetime.utcnow().isoformat()}
@router_group_CBT.get("")
async def i_group_CBT():
    return {"p":"abordagens_inte_group_CBT","s":"ativo","t":datetime.utcnow().isoformat()}
@router_high_frequency_CBT.get("")
async def i_high_frequency_CBT():
    return {"p":"abordagens_inte_high_frequency_CBT","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hold_me_tight.get("")
async def i_hold_me_tight():
    return {"p":"abordagens_inte_hold_me_tight","s":"ativo","t":datetime.utcnow().isoformat()}
@router_imago_therapy.get("")
async def i_imago_therapy():
    return {"p":"abordagens_inte_imago_therapy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_integracao_tecnica.get("")
async def i_integracao_tecnica():
    return {"p":"abordagens_inte_integracao_tecnica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_integracao_teorica.get("")
async def i_integracao_teorica():
    return {"p":"abordagens_inte_integracao_teorica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_intensive_CBT.get("")
async def i_intensive_CBT():
    return {"p":"abordagens_inte_intensive_CBT","s":"ativo","t":datetime.utcnow().isoformat()}
@router_intersectionality_cl.get("")
async def i_intersectionality_cl():
    return {"p":"abordagens_inte_intersectionality_cl","s":"ativo","t":datetime.utcnow().isoformat()}
@router_liberation_psycholog.get("")
async def i_liberation_psycholog():
    return {"p":"abordagens_inte_liberation_psycholog","s":"ativo","t":datetime.utcnow().isoformat()}
@router_low_intensity_CBT.get("")
async def i_low_intensity_CBT():
    return {"p":"abordagens_inte_low_intensity_CBT","s":"ativo","t":datetime.utcnow().isoformat()}
@router_milan_systemic2.get("")
async def i_milan_systemic2():
    return {"p":"abordagens_inte_milan_systemic2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindfulness_ACT.get("")
async def i_mindfulness_ACT():
    return {"p":"abordagens_inte_mindfulness_ACT","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindfulness_CBT.get("")
async def i_mindfulness_CBT():
    return {"p":"abordagens_inte_mindfulness_CBT","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindfulness_DBT.get("")
async def i_mindfulness_DBT():
    return {"p":"abordagens_inte_mindfulness_DBT","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindfulness_psychody.get("")
async def i_mindfulness_psychody():
    return {"p":"abordagens_inte_mindfulness_psychody","s":"ativo","t":datetime.utcnow().isoformat()}
@router_modular_treatment.get("")
async def i_modular_treatment():
    return {"p":"abordagens_inte_modular_treatment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_motivational_CBT.get("")
async def i_motivational_CBT():
    return {"p":"abordagens_inte_motivational_CBT","s":"ativo","t":datetime.utcnow().isoformat()}
@router_multidimensional_fam.get("")
async def i_multidimensional_fam():
    return {"p":"abordagens_inte_multidimensional_fam","s":"ativo","t":datetime.utcnow().isoformat()}
@router_multimodal_therapy_l.get("")
async def i_multimodal_therapy_l():
    return {"p":"abordagens_inte_multimodal_therapy_l","s":"ativo","t":datetime.utcnow().isoformat()}
@router_multisystemic.get("")
async def i_multisystemic():
    return {"p":"abordagens_inte_multisystemic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_narrative_CBT.get("")
async def i_narrative_CBT():
    return {"p":"abordagens_inte_narrative_CBT","s":"ativo","t":datetime.utcnow().isoformat()}
@router_narrative_family.get("")
async def i_narrative_family():
    return {"p":"abordagens_inte_narrative_family","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neuroscience_informe.get("")
async def i_neuroscience_informe():
    return {"p":"abordagens_inte_neuroscience_informe","s":"ativo","t":datetime.utcnow().isoformat()}
@router_online_CBT.get("")
async def i_online_CBT():
    return {"p":"abordagens_inte_online_CBT","s":"ativo","t":datetime.utcnow().isoformat()}
@router_parent_child_interac.get("")
async def i_parent_child_interac():
    return {"p":"abordagens_inte_parent_child_interac","s":"ativo","t":datetime.utcnow().isoformat()}
@router_parent_mediated.get("")
async def i_parent_mediated():
    return {"p":"abordagens_inte_parent_mediated","s":"ativo","t":datetime.utcnow().isoformat()}
@router_paul_therapy_questio.get("")
async def i_paul_therapy_questio():
    return {"p":"abordagens_inte_paul_therapy_questio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_polyvagal_informed.get("")
async def i_polyvagal_informed():
    return {"p":"abordagens_inte_polyvagal_informed","s":"ativo","t":datetime.utcnow().isoformat()}
@router_positive_psychology_.get("")
async def i_positive_psychology_():
    return {"p":"abordagens_inte_positive_psychology_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_positive_psychology_.get("")
async def i_positive_psychology_():
    return {"p":"abordagens_inte_positive_psychology_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_positive_psychology_.get("")
async def i_positive_psychology_():
    return {"p":"abordagens_inte_positive_psychology_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_positive_psychology_.get("")
async def i_positive_psychology_():
    return {"p":"abordagens_inte_positive_psychology_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_prescriptive_matchin.get("")
async def i_prescriptive_matchin():
    return {"p":"abordagens_inte_prescriptive_matchin","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psychobiological_cou.get("")
async def i_psychobiological_cou():
    return {"p":"abordagens_inte_psychobiological_cou","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psychodynamic_cbt_in.get("")
async def i_psychodynamic_cbt_in():
    return {"p":"abordagens_inte_psychodynamic_cbt_in","s":"ativo","t":datetime.utcnow().isoformat()}
@router_schema_EMDR.get("")
async def i_schema_EMDR():
    return {"p":"abordagens_inte_schema_EMDR","s":"ativo","t":datetime.utcnow().isoformat()}
@router_schema_focused_integ.get("")
async def i_schema_focused_integ():
    return {"p":"abordagens_inte_schema_focused_integ","s":"ativo","t":datetime.utcnow().isoformat()}
@router_self_help_CBT.get("")
async def i_self_help_CBT():
    return {"p":"abordagens_inte_self_help_CBT","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sensorimotor_couple.get("")
async def i_sensorimotor_couple():
    return {"p":"abordagens_inte_sensorimotor_couple","s":"ativo","t":datetime.utcnow().isoformat()}
@router_solution_family.get("")
async def i_solution_family():
    return {"p":"abordagens_inte_solution_family","s":"ativo","t":datetime.utcnow().isoformat()}
@router_solution_focused_CBT.get("")
async def i_solution_focused_CBT():
    return {"p":"abordagens_inte_solution_focused_CBT","s":"ativo","t":datetime.utcnow().isoformat()}
@router_somatic_integrative.get("")
async def i_somatic_integrative():
    return {"p":"abordagens_inte_somatic_integrative","s":"ativo","t":datetime.utcnow().isoformat()}
@router_stepped_CBT.get("")
async def i_stepped_CBT():
    return {"p":"abordagens_inte_stepped_CBT","s":"ativo","t":datetime.utcnow().isoformat()}
@router_structural_family2.get("")
async def i_structural_family2():
    return {"p":"abordagens_inte_structural_family2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_systemic_individual.get("")
async def i_systemic_individual():
    return {"p":"abordagens_inte_systemic_individual","s":"ativo","t":datetime.utcnow().isoformat()}
@router_telephone_CBT.get("")
async def i_telephone_CBT():
    return {"p":"abordagens_inte_telephone_CBT","s":"ativo","t":datetime.utcnow().isoformat()}
@router_transdiagnostic_trea.get("")
async def i_transdiagnostic_trea():
    return {"p":"abordagens_inte_transdiagnostic_trea","s":"ativo","t":datetime.utcnow().isoformat()}
@router_trauma_informed2.get("")
async def i_trauma_informed2():
    return {"p":"abordagens_inte_trauma_informed2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_unified_protocol2.get("")
async def i_unified_protocol2():
    return {"p":"abordagens_inte_unified_protocol2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_video_CBT.get("")
async def i_video_CBT():
    return {"p":"abordagens_inte_video_CBT","s":"ativo","t":datetime.utcnow().isoformat()}
@router_wachtel_cyclical_psy.get("")
async def i_wachtel_cyclical_psy():
    return {"p":"abordagens_inte_wachtel_cyclical_psy","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_abordagens_integrati(PluginBase):
    name = "consolidated_abordagens_integrativas"
    def setup(self, app):
        app.include_router(router_BASIC_ID)
        app.include_router(router_CFT_DBT_integration)
        app.include_router(router_DBT_ACT_integration)
        app.include_router(router_EMDR_integrative)
        app.include_router(router_EMDR_somatic)
        app.include_router(router_IPT_CBT)
        app.include_router(router_anti_oppressive)
        app.include_router(router_app_CBT)
        app.include_router(router_assimilativa_integra)
        app.include_router(router_attachment_informed)
        app.include_router(router_bibliotherapy_CBT)
        app.include_router(router_blended_CBT)
        app.include_router(router_body_oriented_integr)
        app.include_router(router_brief_CBT)
        app.include_router(router_brief_strategic_fami)
        app.include_router(router_common_factors_appro)
        app.include_router(router_community_psychology)
        app.include_router(router_computerized_CBT)
        app.include_router(router_core_beliefs_integra)
        app.include_router(router_culturally_adapted)
        app.include_router(router_culturally_humble_ap)
        app.include_router(router_culturally_tailored)
        app.include_router(router_developmental_couple)
        app.include_router(router_eclecticismo_asistem)
        app.include_router(router_eclecticismo_tecnico)
        app.include_router(router_emotionally_focused)
        app.include_router(router_family_based2)
        app.include_router(router_family_systems_indiv)
        app.include_router(router_functional_family)
        app.include_router(router_gottman_method)
        app.include_router(router_group_CBT)
        app.include_router(router_high_frequency_CBT)
        app.include_router(router_hold_me_tight)
        app.include_router(router_imago_therapy)
        app.include_router(router_integracao_tecnica)
        app.include_router(router_integracao_teorica)
        app.include_router(router_intensive_CBT)
        app.include_router(router_intersectionality_cl)
        app.include_router(router_liberation_psycholog)
        app.include_router(router_low_intensity_CBT)
        app.include_router(router_milan_systemic2)
        app.include_router(router_mindfulness_ACT)
        app.include_router(router_mindfulness_CBT)
        app.include_router(router_mindfulness_DBT)
        app.include_router(router_mindfulness_psychody)
        app.include_router(router_modular_treatment)
        app.include_router(router_motivational_CBT)
        app.include_router(router_multidimensional_fam)
        app.include_router(router_multimodal_therapy_l)
        app.include_router(router_multisystemic)
        app.include_router(router_narrative_CBT)
        app.include_router(router_narrative_family)
        app.include_router(router_neuroscience_informe)
        app.include_router(router_online_CBT)
        app.include_router(router_parent_child_interac)
        app.include_router(router_parent_mediated)
        app.include_router(router_paul_therapy_questio)
        app.include_router(router_polyvagal_informed)
        app.include_router(router_positive_psychology_)
        app.include_router(router_positive_psychology_)
        app.include_router(router_positive_psychology_)
        app.include_router(router_positive_psychology_)
        app.include_router(router_prescriptive_matchin)
        app.include_router(router_psychobiological_cou)
        app.include_router(router_psychodynamic_cbt_in)
        app.include_router(router_schema_EMDR)
        app.include_router(router_schema_focused_integ)
        app.include_router(router_self_help_CBT)
        app.include_router(router_sensorimotor_couple)
        app.include_router(router_solution_family)
        app.include_router(router_solution_focused_CBT)
        app.include_router(router_somatic_integrative)
        app.include_router(router_stepped_CBT)
        app.include_router(router_structural_family2)
        app.include_router(router_systemic_individual)
        app.include_router(router_telephone_CBT)
        app.include_router(router_transdiagnostic_trea)
        app.include_router(router_trauma_informed2)
        app.include_router(router_unified_protocol2)
        app.include_router(router_video_CBT)
        app.include_router(router_wachtel_cyclical_psy)


plugin = Plugin_abordagens_integrati()
