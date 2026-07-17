from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_ace_iii = APIRouter(prefix="/api/v1/avaliacao_ne/ace_iii", tags=["avaliacao_neuropsicologica"])
router_adhd_neuropsych = APIRouter(prefix="/api/v1/avaliacao_ne/adhd_neuropsych", tags=["avaliacao_neuropsicologica"])
router_aging_memory = APIRouter(prefix="/api/v1/avaliacao_ne/aging_memory", tags=["avaliacao_neuropsicologica"])
router_alternating_fluency = APIRouter(prefix="/api/v1/avaliacao_ne/alternating_fluency", tags=["avaliacao_neuropsicologica"])
router_alzheimer_neuropsych = APIRouter(prefix="/api/v1/avaliacao_ne/alzheimer_neuropsych", tags=["avaliacao_neuropsicologica"])
router_anxiety_memory = APIRouter(prefix="/api/v1/avaliacao_ne/anxiety_memory", tags=["avaliacao_neuropsicologica"])
router_arithmetic_subtest = APIRouter(prefix="/api/v1/avaliacao_ne/arithmetic_subtest", tags=["avaliacao_neuropsicologica"])
router_autism_neuropsych = APIRouter(prefix="/api/v1/avaliacao_ne/autism_neuropsych", tags=["avaliacao_neuropsicologica"])
router_benton_visual_retent = APIRouter(prefix="/api/v1/avaliacao_ne/benton_visual_retention", tags=["avaliacao_neuropsicologica"])
router_block_design = APIRouter(prefix="/api/v1/avaliacao_ne/block_design", tags=["avaliacao_neuropsicologica"])
router_boston_naming = APIRouter(prefix="/api/v1/avaliacao_ne/boston_naming", tags=["avaliacao_neuropsicologica"])
router_california_verbal_le = APIRouter(prefix="/api/v1/avaliacao_ne/california_verbal_learnin", tags=["avaliacao_neuropsicologica"])
router_cancellation_test = APIRouter(prefix="/api/v1/avaliacao_ne/cancellation_test", tags=["avaliacao_neuropsicologica"])
router_category_fluency = APIRouter(prefix="/api/v1/avaliacao_ne/category_fluency", tags=["avaliacao_neuropsicologica"])
router_cerad_battery = APIRouter(prefix="/api/v1/avaliacao_ne/cerad_battery", tags=["avaliacao_neuropsicologica"])
router_coding_subtest = APIRouter(prefix="/api/v1/avaliacao_ne/coding_subtest", tags=["avaliacao_neuropsicologica"])
router_cognitive_flexibilit = APIRouter(prefix="/api/v1/avaliacao_ne/cognitive_flexibility_bat", tags=["avaliacao_neuropsicologica"])
router_comprehension_subtes = APIRouter(prefix="/api/v1/avaliacao_ne/comprehension_subtest", tags=["avaliacao_neuropsicologica"])
router_consolidation_assess = APIRouter(prefix="/api/v1/avaliacao_ne/consolidation_assessment", tags=["avaliacao_neuropsicologica"])
router_context_memory = APIRouter(prefix="/api/v1/avaliacao_ne/context_memory", tags=["avaliacao_neuropsicologica"])
router_continuous_visual = APIRouter(prefix="/api/v1/avaliacao_ne/continuous_visual", tags=["avaliacao_neuropsicologica"])
router_convergent_thinking = APIRouter(prefix="/api/v1/avaliacao_ne/convergent_thinking", tags=["avaliacao_neuropsicologica"])
router_creativity_tests = APIRouter(prefix="/api/v1/avaliacao_ne/creativity_tests", tags=["avaliacao_neuropsicologica"])
router_depression_memory = APIRouter(prefix="/api/v1/avaliacao_ne/depression_memory", tags=["avaliacao_neuropsicologica"])
router_design_fluency = APIRouter(prefix="/api/v1/avaliacao_ne/design_fluency", tags=["avaliacao_neuropsicologica"])
router_digit_span_backward = APIRouter(prefix="/api/v1/avaliacao_ne/digit_span_backward", tags=["avaliacao_neuropsicologica"])
router_digit_span_forward = APIRouter(prefix="/api/v1/avaliacao_ne/digit_span_forward", tags=["avaliacao_neuropsicologica"])
router_digit_span_sequencin = APIRouter(prefix="/api/v1/avaliacao_ne/digit_span_sequencing", tags=["avaliacao_neuropsicologica"])
router_divergent_thinking = APIRouter(prefix="/api/v1/avaliacao_ne/divergent_thinking", tags=["avaliacao_neuropsicologica"])
router_dual_task_assessment = APIRouter(prefix="/api/v1/avaliacao_ne/dual_task_assessment", tags=["avaliacao_neuropsicologica"])
router_dyscalculia_assess = APIRouter(prefix="/api/v1/avaliacao_ne/dyscalculia_assess", tags=["avaliacao_neuropsicologica"])
router_dyslexia_neuropsych = APIRouter(prefix="/api/v1/avaliacao_ne/dyslexia_neuropsych", tags=["avaliacao_neuropsicologica"])
router_ecological_memory = APIRouter(prefix="/api/v1/avaliacao_ne/ecological_memory", tags=["avaliacao_neuropsicologica"])
router_encoding_strategies = APIRouter(prefix="/api/v1/avaliacao_ne/encoding_strategies", tags=["avaliacao_neuropsicologica"])
router_epilepsy_neuropsych = APIRouter(prefix="/api/v1/avaliacao_ne/epilepsy_neuropsych", tags=["avaliacao_neuropsicologica"])
router_everyday_memory = APIRouter(prefix="/api/v1/avaliacao_ne/everyday_memory", tags=["avaliacao_neuropsicologica"])
router_executive_function_b = APIRouter(prefix="/api/v1/avaliacao_ne/executive_function_batter", tags=["avaliacao_neuropsicologica"])
router_face_name_associatio = APIRouter(prefix="/api/v1/avaliacao_ne/face_name_association", tags=["avaliacao_neuropsicologica"])
router_figura_complexa_rey = APIRouter(prefix="/api/v1/avaliacao_ne/figura_complexa_rey", tags=["avaliacao_neuropsicologica"])
router_figure_weights = APIRouter(prefix="/api/v1/avaliacao_ne/figure_weights", tags=["avaliacao_neuropsicologica"])
router_frontotemporal_batte = APIRouter(prefix="/api/v1/avaliacao_ne/frontotemporal_battery", tags=["avaliacao_neuropsicologica"])
router_frontotemporal_demen = APIRouter(prefix="/api/v1/avaliacao_ne/frontotemporal_dementia_a", tags=["avaliacao_neuropsicologica"])
router_full_scale_iq = APIRouter(prefix="/api/v1/avaliacao_ne/full_scale_iq", tags=["avaliacao_neuropsicologica"])
router_halstead_reitan = APIRouter(prefix="/api/v1/avaliacao_ne/halstead_reitan", tags=["avaliacao_neuropsicologica"])
router_huntington_neuropsyc = APIRouter(prefix="/api/v1/avaliacao_ne/huntington_neuropsych", tags=["avaliacao_neuropsicologica"])
router_ideational_fluency = APIRouter(prefix="/api/v1/avaliacao_ne/ideational_fluency", tags=["avaliacao_neuropsicologica"])
router_information_subtest = APIRouter(prefix="/api/v1/avaliacao_ne/information_subtest", tags=["avaliacao_neuropsicologica"])
router_inhibition_battery = APIRouter(prefix="/api/v1/avaliacao_ne/inhibition_battery", tags=["avaliacao_neuropsicologica"])
router_letter_number_sequen = APIRouter(prefix="/api/v1/avaliacao_ne/letter_number_sequencing", tags=["avaliacao_neuropsicologica"])
router_lewy_body_assess = APIRouter(prefix="/api/v1/avaliacao_ne/lewy_body_assess", tags=["avaliacao_neuropsicologica"])
router_luria_nebraska = APIRouter(prefix="/api/v1/avaliacao_ne/luria_nebraska", tags=["avaliacao_neuropsicologica"])
router_matrix_reasoning = APIRouter(prefix="/api/v1/avaliacao_ne/matrix_reasoning", tags=["avaliacao_neuropsicologica"])
router_metamemory_assessmen = APIRouter(prefix="/api/v1/avaliacao_ne/metamemory_assessment", tags=["avaliacao_neuropsicologica"])
router_mild_cognitive_impai = APIRouter(prefix="/api/v1/avaliacao_ne/mild_cognitive_impairment", tags=["avaliacao_neuropsicologica"])
router_moca_blind = APIRouter(prefix="/api/v1/avaliacao_ne/moca_blind", tags=["avaliacao_neuropsicologica"])
router_multiple_sclerosis_c = APIRouter(prefix="/api/v1/avaliacao_ne/multiple_sclerosis_cog", tags=["avaliacao_neuropsicologica"])
router_neuropsych_battery = APIRouter(prefix="/api/v1/avaliacao_ne/neuropsych_battery", tags=["avaliacao_neuropsicologica"])
router_paired_associate_lea = APIRouter(prefix="/api/v1/avaliacao_ne/paired_associate_learning", tags=["avaliacao_neuropsicologica"])
router_parkinson_neuropsych = APIRouter(prefix="/api/v1/avaliacao_ne/parkinson_neuropsych", tags=["avaliacao_neuropsicologica"])
router_perceptual_reasoning = APIRouter(prefix="/api/v1/avaliacao_ne/perceptual_reasoning", tags=["avaliacao_neuropsicologica"])
router_performance_iq = APIRouter(prefix="/api/v1/avaliacao_ne/performance_iq", tags=["avaliacao_neuropsicologica"])
router_phonemic_fluency = APIRouter(prefix="/api/v1/avaliacao_ne/phonemic_fluency", tags=["avaliacao_neuropsicologica"])
router_picture_completion = APIRouter(prefix="/api/v1/avaliacao_ne/picture_completion", tags=["avaliacao_neuropsicologica"])
router_planning_battery = APIRouter(prefix="/api/v1/avaliacao_ne/planning_battery", tags=["avaliacao_neuropsicologica"])
router_processing_speed_ind = APIRouter(prefix="/api/v1/avaliacao_ne/processing_speed_index", tags=["avaliacao_neuropsicologica"])
router_prospective_memory_t = APIRouter(prefix="/api/v1/avaliacao_ne/prospective_memory_test", tags=["avaliacao_neuropsicologica"])
router_prospective_planning = APIRouter(prefix="/api/v1/avaliacao_ne/prospective_planning", tags=["avaliacao_neuropsicologica"])
router_recall_vs_recognitio = APIRouter(prefix="/api/v1/avaliacao_ne/recall_vs_recognition", tags=["avaliacao_neuropsicologica"])
router_recognition_memory = APIRouter(prefix="/api/v1/avaliacao_ne/recognition_memory", tags=["avaliacao_neuropsicologica"])
router_remote_associates = APIRouter(prefix="/api/v1/avaliacao_ne/remote_associates", tags=["avaliacao_neuropsicologica"])
router_retrieval_cues = APIRouter(prefix="/api/v1/avaliacao_ne/retrieval_cues", tags=["avaliacao_neuropsicologica"])
router_rey_auditory_verbal = APIRouter(prefix="/api/v1/avaliacao_ne/rey_auditory_verbal", tags=["avaliacao_neuropsicologica"])
router_semantic_fluency = APIRouter(prefix="/api/v1/avaliacao_ne/semantic_fluency", tags=["avaliacao_neuropsicologica"])
router_shifting_battery = APIRouter(prefix="/api/v1/avaliacao_ne/shifting_battery", tags=["avaliacao_neuropsicologica"])
router_similarities_subtest = APIRouter(prefix="/api/v1/avaliacao_ne/similarities_subtest", tags=["avaliacao_neuropsicologica"])
router_sleep_memory_consoli = APIRouter(prefix="/api/v1/avaliacao_ne/sleep_memory_consolidatio", tags=["avaliacao_neuropsicologica"])
router_source_memory = APIRouter(prefix="/api/v1/avaliacao_ne/source_memory", tags=["avaliacao_neuropsicologica"])
router_spatial_span = APIRouter(prefix="/api/v1/avaliacao_ne/spatial_span", tags=["avaliacao_neuropsicologica"])
router_story_recall = APIRouter(prefix="/api/v1/avaliacao_ne/story_recall", tags=["avaliacao_neuropsicologica"])
router_stress_memory_impair = APIRouter(prefix="/api/v1/avaliacao_ne/stress_memory_impairment", tags=["avaliacao_neuropsicologica"])
router_stroke_neuropsych = APIRouter(prefix="/api/v1/avaliacao_ne/stroke_neuropsych", tags=["avaliacao_neuropsicologica"])
router_stroop_cores = APIRouter(prefix="/api/v1/avaliacao_ne/stroop_cores", tags=["avaliacao_neuropsicologica"])
router_stroop_interferencia = APIRouter(prefix="/api/v1/avaliacao_ne/stroop_interferencia", tags=["avaliacao_neuropsicologica"])
router_stroop_palavras = APIRouter(prefix="/api/v1/avaliacao_ne/stroop_palavras", tags=["avaliacao_neuropsicologica"])
router_symbol_search = APIRouter(prefix="/api/v1/avaliacao_ne/symbol_search", tags=["avaliacao_neuropsicologica"])
router_temporal_order = APIRouter(prefix="/api/v1/avaliacao_ne/temporal_order", tags=["avaliacao_neuropsicologica"])
router_tower_hanoi = APIRouter(prefix="/api/v1/avaliacao_ne/tower_hanoi", tags=["avaliacao_neuropsicologica"])
router_tower_london = APIRouter(prefix="/api/v1/avaliacao_ne/tower_london", tags=["avaliacao_neuropsicologica"])
router_traumatic_brain_neur = APIRouter(prefix="/api/v1/avaliacao_ne/traumatic_brain_neuropsyc", tags=["avaliacao_neuropsicologica"])
router_trilhas_forma_a = APIRouter(prefix="/api/v1/avaliacao_ne/trilhas_forma_a", tags=["avaliacao_neuropsicologica"])
router_trilhas_forma_b = APIRouter(prefix="/api/v1/avaliacao_ne/trilhas_forma_b", tags=["avaliacao_neuropsicologica"])
router_updating_battery = APIRouter(prefix="/api/v1/avaliacao_ne/updating_battery", tags=["avaliacao_neuropsicologica"])
router_vascular_dementia = APIRouter(prefix="/api/v1/avaliacao_ne/vascular_dementia", tags=["avaliacao_neuropsicologica"])
router_verbal_comprehension = APIRouter(prefix="/api/v1/avaliacao_ne/verbal_comprehension", tags=["avaliacao_neuropsicologica"])
router_verbal_fluency_fis = APIRouter(prefix="/api/v1/avaliacao_ne/verbal_fluency_fis", tags=["avaliacao_neuropsicologica"])
router_verbal_iq = APIRouter(prefix="/api/v1/avaliacao_ne/verbal_iq", tags=["avaliacao_neuropsicologica"])
router_visual_puzzles = APIRouter(prefix="/api/v1/avaliacao_ne/visual_puzzles", tags=["avaliacao_neuropsicologica"])
router_vocabulary_subtest = APIRouter(prefix="/api/v1/avaliacao_ne/vocabulary_subtest", tags=["avaliacao_neuropsicologica"])
router_wisconsin_card_sort = APIRouter(prefix="/api/v1/avaliacao_ne/wisconsin_card_sort", tags=["avaliacao_neuropsicologica"])
router_wms_logical_memory = APIRouter(prefix="/api/v1/avaliacao_ne/wms_logical_memory", tags=["avaliacao_neuropsicologica"])
router_wms_visual_reproduct = APIRouter(prefix="/api/v1/avaliacao_ne/wms_visual_reproduction", tags=["avaliacao_neuropsicologica"])
router_working_memory_index = APIRouter(prefix="/api/v1/avaliacao_ne/working_memory_index", tags=["avaliacao_neuropsicologica"])

@router_ace_iii.get("")
async def i_ace_iii():
    return {"p":"avaliacao_neuro_ace_iii","s":"ativo","t":datetime.utcnow().isoformat()}
@router_adhd_neuropsych.get("")
async def i_adhd_neuropsych():
    return {"p":"avaliacao_neuro_adhd_neuropsych","s":"ativo","t":datetime.utcnow().isoformat()}
@router_aging_memory.get("")
async def i_aging_memory():
    return {"p":"avaliacao_neuro_aging_memory","s":"ativo","t":datetime.utcnow().isoformat()}
@router_alternating_fluency.get("")
async def i_alternating_fluency():
    return {"p":"avaliacao_neuro_alternating_fluency","s":"ativo","t":datetime.utcnow().isoformat()}
@router_alzheimer_neuropsych.get("")
async def i_alzheimer_neuropsych():
    return {"p":"avaliacao_neuro_alzheimer_neuropsych","s":"ativo","t":datetime.utcnow().isoformat()}
@router_anxiety_memory.get("")
async def i_anxiety_memory():
    return {"p":"avaliacao_neuro_anxiety_memory","s":"ativo","t":datetime.utcnow().isoformat()}
@router_arithmetic_subtest.get("")
async def i_arithmetic_subtest():
    return {"p":"avaliacao_neuro_arithmetic_subtest","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autism_neuropsych.get("")
async def i_autism_neuropsych():
    return {"p":"avaliacao_neuro_autism_neuropsych","s":"ativo","t":datetime.utcnow().isoformat()}
@router_benton_visual_retent.get("")
async def i_benton_visual_retent():
    return {"p":"avaliacao_neuro_benton_visual_retent","s":"ativo","t":datetime.utcnow().isoformat()}
@router_block_design.get("")
async def i_block_design():
    return {"p":"avaliacao_neuro_block_design","s":"ativo","t":datetime.utcnow().isoformat()}
@router_boston_naming.get("")
async def i_boston_naming():
    return {"p":"avaliacao_neuro_boston_naming","s":"ativo","t":datetime.utcnow().isoformat()}
@router_california_verbal_le.get("")
async def i_california_verbal_le():
    return {"p":"avaliacao_neuro_california_verbal_le","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cancellation_test.get("")
async def i_cancellation_test():
    return {"p":"avaliacao_neuro_cancellation_test","s":"ativo","t":datetime.utcnow().isoformat()}
@router_category_fluency.get("")
async def i_category_fluency():
    return {"p":"avaliacao_neuro_category_fluency","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cerad_battery.get("")
async def i_cerad_battery():
    return {"p":"avaliacao_neuro_cerad_battery","s":"ativo","t":datetime.utcnow().isoformat()}
@router_coding_subtest.get("")
async def i_coding_subtest():
    return {"p":"avaliacao_neuro_coding_subtest","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cognitive_flexibilit.get("")
async def i_cognitive_flexibilit():
    return {"p":"avaliacao_neuro_cognitive_flexibilit","s":"ativo","t":datetime.utcnow().isoformat()}
@router_comprehension_subtes.get("")
async def i_comprehension_subtes():
    return {"p":"avaliacao_neuro_comprehension_subtes","s":"ativo","t":datetime.utcnow().isoformat()}
@router_consolidation_assess.get("")
async def i_consolidation_assess():
    return {"p":"avaliacao_neuro_consolidation_assess","s":"ativo","t":datetime.utcnow().isoformat()}
@router_context_memory.get("")
async def i_context_memory():
    return {"p":"avaliacao_neuro_context_memory","s":"ativo","t":datetime.utcnow().isoformat()}
@router_continuous_visual.get("")
async def i_continuous_visual():
    return {"p":"avaliacao_neuro_continuous_visual","s":"ativo","t":datetime.utcnow().isoformat()}
@router_convergent_thinking.get("")
async def i_convergent_thinking():
    return {"p":"avaliacao_neuro_convergent_thinking","s":"ativo","t":datetime.utcnow().isoformat()}
@router_creativity_tests.get("")
async def i_creativity_tests():
    return {"p":"avaliacao_neuro_creativity_tests","s":"ativo","t":datetime.utcnow().isoformat()}
@router_depression_memory.get("")
async def i_depression_memory():
    return {"p":"avaliacao_neuro_depression_memory","s":"ativo","t":datetime.utcnow().isoformat()}
@router_design_fluency.get("")
async def i_design_fluency():
    return {"p":"avaliacao_neuro_design_fluency","s":"ativo","t":datetime.utcnow().isoformat()}
@router_digit_span_backward.get("")
async def i_digit_span_backward():
    return {"p":"avaliacao_neuro_digit_span_backward","s":"ativo","t":datetime.utcnow().isoformat()}
@router_digit_span_forward.get("")
async def i_digit_span_forward():
    return {"p":"avaliacao_neuro_digit_span_forward","s":"ativo","t":datetime.utcnow().isoformat()}
@router_digit_span_sequencin.get("")
async def i_digit_span_sequencin():
    return {"p":"avaliacao_neuro_digit_span_sequencin","s":"ativo","t":datetime.utcnow().isoformat()}
@router_divergent_thinking.get("")
async def i_divergent_thinking():
    return {"p":"avaliacao_neuro_divergent_thinking","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dual_task_assessment.get("")
async def i_dual_task_assessment():
    return {"p":"avaliacao_neuro_dual_task_assessment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dyscalculia_assess.get("")
async def i_dyscalculia_assess():
    return {"p":"avaliacao_neuro_dyscalculia_assess","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dyslexia_neuropsych.get("")
async def i_dyslexia_neuropsych():
    return {"p":"avaliacao_neuro_dyslexia_neuropsych","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ecological_memory.get("")
async def i_ecological_memory():
    return {"p":"avaliacao_neuro_ecological_memory","s":"ativo","t":datetime.utcnow().isoformat()}
@router_encoding_strategies.get("")
async def i_encoding_strategies():
    return {"p":"avaliacao_neuro_encoding_strategies","s":"ativo","t":datetime.utcnow().isoformat()}
@router_epilepsy_neuropsych.get("")
async def i_epilepsy_neuropsych():
    return {"p":"avaliacao_neuro_epilepsy_neuropsych","s":"ativo","t":datetime.utcnow().isoformat()}
@router_everyday_memory.get("")
async def i_everyday_memory():
    return {"p":"avaliacao_neuro_everyday_memory","s":"ativo","t":datetime.utcnow().isoformat()}
@router_executive_function_b.get("")
async def i_executive_function_b():
    return {"p":"avaliacao_neuro_executive_function_b","s":"ativo","t":datetime.utcnow().isoformat()}
@router_face_name_associatio.get("")
async def i_face_name_associatio():
    return {"p":"avaliacao_neuro_face_name_associatio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_figura_complexa_rey.get("")
async def i_figura_complexa_rey():
    return {"p":"avaliacao_neuro_figura_complexa_rey","s":"ativo","t":datetime.utcnow().isoformat()}
@router_figure_weights.get("")
async def i_figure_weights():
    return {"p":"avaliacao_neuro_figure_weights","s":"ativo","t":datetime.utcnow().isoformat()}
@router_frontotemporal_batte.get("")
async def i_frontotemporal_batte():
    return {"p":"avaliacao_neuro_frontotemporal_batte","s":"ativo","t":datetime.utcnow().isoformat()}
@router_frontotemporal_demen.get("")
async def i_frontotemporal_demen():
    return {"p":"avaliacao_neuro_frontotemporal_demen","s":"ativo","t":datetime.utcnow().isoformat()}
@router_full_scale_iq.get("")
async def i_full_scale_iq():
    return {"p":"avaliacao_neuro_full_scale_iq","s":"ativo","t":datetime.utcnow().isoformat()}
@router_halstead_reitan.get("")
async def i_halstead_reitan():
    return {"p":"avaliacao_neuro_halstead_reitan","s":"ativo","t":datetime.utcnow().isoformat()}
@router_huntington_neuropsyc.get("")
async def i_huntington_neuropsyc():
    return {"p":"avaliacao_neuro_huntington_neuropsyc","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ideational_fluency.get("")
async def i_ideational_fluency():
    return {"p":"avaliacao_neuro_ideational_fluency","s":"ativo","t":datetime.utcnow().isoformat()}
@router_information_subtest.get("")
async def i_information_subtest():
    return {"p":"avaliacao_neuro_information_subtest","s":"ativo","t":datetime.utcnow().isoformat()}
@router_inhibition_battery.get("")
async def i_inhibition_battery():
    return {"p":"avaliacao_neuro_inhibition_battery","s":"ativo","t":datetime.utcnow().isoformat()}
@router_letter_number_sequen.get("")
async def i_letter_number_sequen():
    return {"p":"avaliacao_neuro_letter_number_sequen","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lewy_body_assess.get("")
async def i_lewy_body_assess():
    return {"p":"avaliacao_neuro_lewy_body_assess","s":"ativo","t":datetime.utcnow().isoformat()}
@router_luria_nebraska.get("")
async def i_luria_nebraska():
    return {"p":"avaliacao_neuro_luria_nebraska","s":"ativo","t":datetime.utcnow().isoformat()}
@router_matrix_reasoning.get("")
async def i_matrix_reasoning():
    return {"p":"avaliacao_neuro_matrix_reasoning","s":"ativo","t":datetime.utcnow().isoformat()}
@router_metamemory_assessmen.get("")
async def i_metamemory_assessmen():
    return {"p":"avaliacao_neuro_metamemory_assessmen","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mild_cognitive_impai.get("")
async def i_mild_cognitive_impai():
    return {"p":"avaliacao_neuro_mild_cognitive_impai","s":"ativo","t":datetime.utcnow().isoformat()}
@router_moca_blind.get("")
async def i_moca_blind():
    return {"p":"avaliacao_neuro_moca_blind","s":"ativo","t":datetime.utcnow().isoformat()}
@router_multiple_sclerosis_c.get("")
async def i_multiple_sclerosis_c():
    return {"p":"avaliacao_neuro_multiple_sclerosis_c","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neuropsych_battery.get("")
async def i_neuropsych_battery():
    return {"p":"avaliacao_neuro_neuropsych_battery","s":"ativo","t":datetime.utcnow().isoformat()}
@router_paired_associate_lea.get("")
async def i_paired_associate_lea():
    return {"p":"avaliacao_neuro_paired_associate_lea","s":"ativo","t":datetime.utcnow().isoformat()}
@router_parkinson_neuropsych.get("")
async def i_parkinson_neuropsych():
    return {"p":"avaliacao_neuro_parkinson_neuropsych","s":"ativo","t":datetime.utcnow().isoformat()}
@router_perceptual_reasoning.get("")
async def i_perceptual_reasoning():
    return {"p":"avaliacao_neuro_perceptual_reasoning","s":"ativo","t":datetime.utcnow().isoformat()}
@router_performance_iq.get("")
async def i_performance_iq():
    return {"p":"avaliacao_neuro_performance_iq","s":"ativo","t":datetime.utcnow().isoformat()}
@router_phonemic_fluency.get("")
async def i_phonemic_fluency():
    return {"p":"avaliacao_neuro_phonemic_fluency","s":"ativo","t":datetime.utcnow().isoformat()}
@router_picture_completion.get("")
async def i_picture_completion():
    return {"p":"avaliacao_neuro_picture_completion","s":"ativo","t":datetime.utcnow().isoformat()}
@router_planning_battery.get("")
async def i_planning_battery():
    return {"p":"avaliacao_neuro_planning_battery","s":"ativo","t":datetime.utcnow().isoformat()}
@router_processing_speed_ind.get("")
async def i_processing_speed_ind():
    return {"p":"avaliacao_neuro_processing_speed_ind","s":"ativo","t":datetime.utcnow().isoformat()}
@router_prospective_memory_t.get("")
async def i_prospective_memory_t():
    return {"p":"avaliacao_neuro_prospective_memory_t","s":"ativo","t":datetime.utcnow().isoformat()}
@router_prospective_planning.get("")
async def i_prospective_planning():
    return {"p":"avaliacao_neuro_prospective_planning","s":"ativo","t":datetime.utcnow().isoformat()}
@router_recall_vs_recognitio.get("")
async def i_recall_vs_recognitio():
    return {"p":"avaliacao_neuro_recall_vs_recognitio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_recognition_memory.get("")
async def i_recognition_memory():
    return {"p":"avaliacao_neuro_recognition_memory","s":"ativo","t":datetime.utcnow().isoformat()}
@router_remote_associates.get("")
async def i_remote_associates():
    return {"p":"avaliacao_neuro_remote_associates","s":"ativo","t":datetime.utcnow().isoformat()}
@router_retrieval_cues.get("")
async def i_retrieval_cues():
    return {"p":"avaliacao_neuro_retrieval_cues","s":"ativo","t":datetime.utcnow().isoformat()}
@router_rey_auditory_verbal.get("")
async def i_rey_auditory_verbal():
    return {"p":"avaliacao_neuro_rey_auditory_verbal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_semantic_fluency.get("")
async def i_semantic_fluency():
    return {"p":"avaliacao_neuro_semantic_fluency","s":"ativo","t":datetime.utcnow().isoformat()}
@router_shifting_battery.get("")
async def i_shifting_battery():
    return {"p":"avaliacao_neuro_shifting_battery","s":"ativo","t":datetime.utcnow().isoformat()}
@router_similarities_subtest.get("")
async def i_similarities_subtest():
    return {"p":"avaliacao_neuro_similarities_subtest","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sleep_memory_consoli.get("")
async def i_sleep_memory_consoli():
    return {"p":"avaliacao_neuro_sleep_memory_consoli","s":"ativo","t":datetime.utcnow().isoformat()}
@router_source_memory.get("")
async def i_source_memory():
    return {"p":"avaliacao_neuro_source_memory","s":"ativo","t":datetime.utcnow().isoformat()}
@router_spatial_span.get("")
async def i_spatial_span():
    return {"p":"avaliacao_neuro_spatial_span","s":"ativo","t":datetime.utcnow().isoformat()}
@router_story_recall.get("")
async def i_story_recall():
    return {"p":"avaliacao_neuro_story_recall","s":"ativo","t":datetime.utcnow().isoformat()}
@router_stress_memory_impair.get("")
async def i_stress_memory_impair():
    return {"p":"avaliacao_neuro_stress_memory_impair","s":"ativo","t":datetime.utcnow().isoformat()}
@router_stroke_neuropsych.get("")
async def i_stroke_neuropsych():
    return {"p":"avaliacao_neuro_stroke_neuropsych","s":"ativo","t":datetime.utcnow().isoformat()}
@router_stroop_cores.get("")
async def i_stroop_cores():
    return {"p":"avaliacao_neuro_stroop_cores","s":"ativo","t":datetime.utcnow().isoformat()}
@router_stroop_interferencia.get("")
async def i_stroop_interferencia():
    return {"p":"avaliacao_neuro_stroop_interferencia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_stroop_palavras.get("")
async def i_stroop_palavras():
    return {"p":"avaliacao_neuro_stroop_palavras","s":"ativo","t":datetime.utcnow().isoformat()}
@router_symbol_search.get("")
async def i_symbol_search():
    return {"p":"avaliacao_neuro_symbol_search","s":"ativo","t":datetime.utcnow().isoformat()}
@router_temporal_order.get("")
async def i_temporal_order():
    return {"p":"avaliacao_neuro_temporal_order","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tower_hanoi.get("")
async def i_tower_hanoi():
    return {"p":"avaliacao_neuro_tower_hanoi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tower_london.get("")
async def i_tower_london():
    return {"p":"avaliacao_neuro_tower_london","s":"ativo","t":datetime.utcnow().isoformat()}
@router_traumatic_brain_neur.get("")
async def i_traumatic_brain_neur():
    return {"p":"avaliacao_neuro_traumatic_brain_neur","s":"ativo","t":datetime.utcnow().isoformat()}
@router_trilhas_forma_a.get("")
async def i_trilhas_forma_a():
    return {"p":"avaliacao_neuro_trilhas_forma_a","s":"ativo","t":datetime.utcnow().isoformat()}
@router_trilhas_forma_b.get("")
async def i_trilhas_forma_b():
    return {"p":"avaliacao_neuro_trilhas_forma_b","s":"ativo","t":datetime.utcnow().isoformat()}
@router_updating_battery.get("")
async def i_updating_battery():
    return {"p":"avaliacao_neuro_updating_battery","s":"ativo","t":datetime.utcnow().isoformat()}
@router_vascular_dementia.get("")
async def i_vascular_dementia():
    return {"p":"avaliacao_neuro_vascular_dementia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_verbal_comprehension.get("")
async def i_verbal_comprehension():
    return {"p":"avaliacao_neuro_verbal_comprehension","s":"ativo","t":datetime.utcnow().isoformat()}
@router_verbal_fluency_fis.get("")
async def i_verbal_fluency_fis():
    return {"p":"avaliacao_neuro_verbal_fluency_fis","s":"ativo","t":datetime.utcnow().isoformat()}
@router_verbal_iq.get("")
async def i_verbal_iq():
    return {"p":"avaliacao_neuro_verbal_iq","s":"ativo","t":datetime.utcnow().isoformat()}
@router_visual_puzzles.get("")
async def i_visual_puzzles():
    return {"p":"avaliacao_neuro_visual_puzzles","s":"ativo","t":datetime.utcnow().isoformat()}
@router_vocabulary_subtest.get("")
async def i_vocabulary_subtest():
    return {"p":"avaliacao_neuro_vocabulary_subtest","s":"ativo","t":datetime.utcnow().isoformat()}
@router_wisconsin_card_sort.get("")
async def i_wisconsin_card_sort():
    return {"p":"avaliacao_neuro_wisconsin_card_sort","s":"ativo","t":datetime.utcnow().isoformat()}
@router_wms_logical_memory.get("")
async def i_wms_logical_memory():
    return {"p":"avaliacao_neuro_wms_logical_memory","s":"ativo","t":datetime.utcnow().isoformat()}
@router_wms_visual_reproduct.get("")
async def i_wms_visual_reproduct():
    return {"p":"avaliacao_neuro_wms_visual_reproduct","s":"ativo","t":datetime.utcnow().isoformat()}
@router_working_memory_index.get("")
async def i_working_memory_index():
    return {"p":"avaliacao_neuro_working_memory_index","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_avaliacao_neuropsico(PluginBase):
    name = "consolidated_avaliacao_neuropsicologica"
    def setup(self, app):
        app.include_router(router_ace_iii)
        app.include_router(router_adhd_neuropsych)
        app.include_router(router_aging_memory)
        app.include_router(router_alternating_fluency)
        app.include_router(router_alzheimer_neuropsych)
        app.include_router(router_anxiety_memory)
        app.include_router(router_arithmetic_subtest)
        app.include_router(router_autism_neuropsych)
        app.include_router(router_benton_visual_retent)
        app.include_router(router_block_design)
        app.include_router(router_boston_naming)
        app.include_router(router_california_verbal_le)
        app.include_router(router_cancellation_test)
        app.include_router(router_category_fluency)
        app.include_router(router_cerad_battery)
        app.include_router(router_coding_subtest)
        app.include_router(router_cognitive_flexibilit)
        app.include_router(router_comprehension_subtes)
        app.include_router(router_consolidation_assess)
        app.include_router(router_context_memory)
        app.include_router(router_continuous_visual)
        app.include_router(router_convergent_thinking)
        app.include_router(router_creativity_tests)
        app.include_router(router_depression_memory)
        app.include_router(router_design_fluency)
        app.include_router(router_digit_span_backward)
        app.include_router(router_digit_span_forward)
        app.include_router(router_digit_span_sequencin)
        app.include_router(router_divergent_thinking)
        app.include_router(router_dual_task_assessment)
        app.include_router(router_dyscalculia_assess)
        app.include_router(router_dyslexia_neuropsych)
        app.include_router(router_ecological_memory)
        app.include_router(router_encoding_strategies)
        app.include_router(router_epilepsy_neuropsych)
        app.include_router(router_everyday_memory)
        app.include_router(router_executive_function_b)
        app.include_router(router_face_name_associatio)
        app.include_router(router_figura_complexa_rey)
        app.include_router(router_figure_weights)
        app.include_router(router_frontotemporal_batte)
        app.include_router(router_frontotemporal_demen)
        app.include_router(router_full_scale_iq)
        app.include_router(router_halstead_reitan)
        app.include_router(router_huntington_neuropsyc)
        app.include_router(router_ideational_fluency)
        app.include_router(router_information_subtest)
        app.include_router(router_inhibition_battery)
        app.include_router(router_letter_number_sequen)
        app.include_router(router_lewy_body_assess)
        app.include_router(router_luria_nebraska)
        app.include_router(router_matrix_reasoning)
        app.include_router(router_metamemory_assessmen)
        app.include_router(router_mild_cognitive_impai)
        app.include_router(router_moca_blind)
        app.include_router(router_multiple_sclerosis_c)
        app.include_router(router_neuropsych_battery)
        app.include_router(router_paired_associate_lea)
        app.include_router(router_parkinson_neuropsych)
        app.include_router(router_perceptual_reasoning)
        app.include_router(router_performance_iq)
        app.include_router(router_phonemic_fluency)
        app.include_router(router_picture_completion)
        app.include_router(router_planning_battery)
        app.include_router(router_processing_speed_ind)
        app.include_router(router_prospective_memory_t)
        app.include_router(router_prospective_planning)
        app.include_router(router_recall_vs_recognitio)
        app.include_router(router_recognition_memory)
        app.include_router(router_remote_associates)
        app.include_router(router_retrieval_cues)
        app.include_router(router_rey_auditory_verbal)
        app.include_router(router_semantic_fluency)
        app.include_router(router_shifting_battery)
        app.include_router(router_similarities_subtest)
        app.include_router(router_sleep_memory_consoli)
        app.include_router(router_source_memory)
        app.include_router(router_spatial_span)
        app.include_router(router_story_recall)
        app.include_router(router_stress_memory_impair)
        app.include_router(router_stroke_neuropsych)
        app.include_router(router_stroop_cores)
        app.include_router(router_stroop_interferencia)
        app.include_router(router_stroop_palavras)
        app.include_router(router_symbol_search)
        app.include_router(router_temporal_order)
        app.include_router(router_tower_hanoi)
        app.include_router(router_tower_london)
        app.include_router(router_traumatic_brain_neur)
        app.include_router(router_trilhas_forma_a)
        app.include_router(router_trilhas_forma_b)
        app.include_router(router_updating_battery)
        app.include_router(router_vascular_dementia)
        app.include_router(router_verbal_comprehension)
        app.include_router(router_verbal_fluency_fis)
        app.include_router(router_verbal_iq)
        app.include_router(router_visual_puzzles)
        app.include_router(router_vocabulary_subtest)
        app.include_router(router_wisconsin_card_sort)
        app.include_router(router_wms_logical_memory)
        app.include_router(router_wms_visual_reproduct)
        app.include_router(router_working_memory_index)


plugin = Plugin_avaliacao_neuropsico()
