from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_adjacency_pairs = APIRouter(prefix="/api/v1/pesquisa_qua/adjacency_pairs", tags=["pesquisa_qualitativa_avancada"])
router_analytical_autoethno = APIRouter(prefix="/api/v1/pesquisa_qua/analytical_autoethnograph", tags=["pesquisa_qualitativa_avancada"])
router_authenticity_qualita = APIRouter(prefix="/api/v1/pesquisa_qua/authenticity_qualitative", tags=["pesquisa_qualitativa_avancada"])
router_autoethnography2 = APIRouter(prefix="/api/v1/pesquisa_qua/autoethnography2", tags=["pesquisa_qualitativa_avancada"])
router_bracketing = APIRouter(prefix="/api/v1/pesquisa_qua/bracketing", tags=["pesquisa_qualitativa_avancada"])
router_braun_clarke = APIRouter(prefix="/api/v1/pesquisa_qua/braun_clarke", tags=["pesquisa_qualitativa_avancada"])
router_casp_qualitative = APIRouter(prefix="/api/v1/pesquisa_qua/casp_qualitative", tags=["pesquisa_qualitativa_avancada"])
router_classical_gt = APIRouter(prefix="/api/v1/pesquisa_qua/classical_gt", tags=["pesquisa_qualitativa_avancada"])
router_collaborative_autoet = APIRouter(prefix="/api/v1/pesquisa_qua/collaborative_autoethnogr", tags=["pesquisa_qualitativa_avancada"])
router_confirmability = APIRouter(prefix="/api/v1/pesquisa_qua/confirmability", tags=["pesquisa_qualitativa_avancada"])
router_consolidation_qualit = APIRouter(prefix="/api/v1/pesquisa_qua/consolidation_qualitative", tags=["pesquisa_qualitativa_avancada"])
router_constructionist = APIRouter(prefix="/api/v1/pesquisa_qua/constructionist", tags=["pesquisa_qualitativa_avancada"])
router_constructivist_gt = APIRouter(prefix="/api/v1/pesquisa_qua/constructivist_gt", tags=["pesquisa_qualitativa_avancada"])
router_content_analysis2 = APIRouter(prefix="/api/v1/pesquisa_qua/content_analysis2", tags=["pesquisa_qualitativa_avancada"])
router_conversation_analysi = APIRouter(prefix="/api/v1/pesquisa_qua/conversation_analysis", tags=["pesquisa_qualitativa_avancada"])
router_coreq_reporting = APIRouter(prefix="/api/v1/pesquisa_qua/coreq_reporting", tags=["pesquisa_qualitativa_avancada"])
router_credibility_qualitat = APIRouter(prefix="/api/v1/pesquisa_qua/credibility_qualitative", tags=["pesquisa_qualitativa_avancada"])
router_critical_appraisal_q = APIRouter(prefix="/api/v1/pesquisa_qua/critical_appraisal_qualit", tags=["pesquisa_qualitativa_avancada"])
router_critical_discourse = APIRouter(prefix="/api/v1/pesquisa_qua/critical_discourse", tags=["pesquisa_qualitativa_avancada"])
router_data_triangulation = APIRouter(prefix="/api/v1/pesquisa_qua/data_triangulation", tags=["pesquisa_qualitativa_avancada"])
router_dependability_qualit = APIRouter(prefix="/api/v1/pesquisa_qua/dependability_qualitative", tags=["pesquisa_qualitativa_avancada"])
router_descriptive_phenomen = APIRouter(prefix="/api/v1/pesquisa_qua/descriptive_phenomenology", tags=["pesquisa_qualitativa_avancada"])
router_directed_content = APIRouter(prefix="/api/v1/pesquisa_qua/directed_content", tags=["pesquisa_qualitativa_avancada"])
router_discourse_analysis2 = APIRouter(prefix="/api/v1/pesquisa_qua/discourse_analysis2", tags=["pesquisa_qualitativa_avancada"])
router_duoethnography = APIRouter(prefix="/api/v1/pesquisa_qua/duoethnography", tags=["pesquisa_qualitativa_avancada"])
router_emplotment = APIRouter(prefix="/api/v1/pesquisa_qua/emplotment", tags=["pesquisa_qualitativa_avancada"])
router_equator_qualitative = APIRouter(prefix="/api/v1/pesquisa_qua/equator_qualitative", tags=["pesquisa_qualitativa_avancada"])
router_ethnographic_intervi = APIRouter(prefix="/api/v1/pesquisa_qua/ethnographic_interview", tags=["pesquisa_qualitativa_avancada"])
router_ethnography2 = APIRouter(prefix="/api/v1/pesquisa_qua/ethnography2", tags=["pesquisa_qualitativa_avancada"])
router_evocative_autoethnog = APIRouter(prefix="/api/v1/pesquisa_qua/evocative_autoethnography", tags=["pesquisa_qualitativa_avancada"])
router_existential_phenomen = APIRouter(prefix="/api/v1/pesquisa_qua/existential_phenomenology", tags=["pesquisa_qualitativa_avancada"])
router_field_notes = APIRouter(prefix="/api/v1/pesquisa_qua/field_notes", tags=["pesquisa_qualitativa_avancada"])
router_gadamer_hermeneutic = APIRouter(prefix="/api/v1/pesquisa_qua/gadamer_hermeneutic", tags=["pesquisa_qualitativa_avancada"])
router_geertz_culture = APIRouter(prefix="/api/v1/pesquisa_qua/geertz_culture", tags=["pesquisa_qualitativa_avancada"])
router_going_native = APIRouter(prefix="/api/v1/pesquisa_qua/going_native", tags=["pesquisa_qualitativa_avancada"])
router_grounded_theory2 = APIRouter(prefix="/api/v1/pesquisa_qua/grounded_theory2", tags=["pesquisa_qualitativa_avancada"])
router_heidegger_analysis = APIRouter(prefix="/api/v1/pesquisa_qua/heidegger_analysis", tags=["pesquisa_qualitativa_avancada"])
router_hermeneutic_phenomen = APIRouter(prefix="/api/v1/pesquisa_qua/hermeneutic_phenomenology", tags=["pesquisa_qualitativa_avancada"])
router_husserl_analysis = APIRouter(prefix="/api/v1/pesquisa_qua/husserl_analysis", tags=["pesquisa_qualitativa_avancada"])
router_identity_constructio = APIRouter(prefix="/api/v1/pesquisa_qua/identity_construction", tags=["pesquisa_qualitativa_avancada"])
router_interpretive_phenome = APIRouter(prefix="/api/v1/pesquisa_qua/interpretive_phenomenolog", tags=["pesquisa_qualitativa_avancada"])
router_interpretive_themati = APIRouter(prefix="/api/v1/pesquisa_qua/interpretive_thematic", tags=["pesquisa_qualitativa_avancada"])
router_investigator_triangu = APIRouter(prefix="/api/v1/pesquisa_qua/investigator_triangulatio", tags=["pesquisa_qualitativa_avancada"])
router_key_informant = APIRouter(prefix="/api/v1/pesquisa_qua/key_informant", tags=["pesquisa_qualitativa_avancada"])
router_landscape_inquiry = APIRouter(prefix="/api/v1/pesquisa_qua/landscape_inquiry", tags=["pesquisa_qualitativa_avancada"])
router_latent_content = APIRouter(prefix="/api/v1/pesquisa_qua/latent_content", tags=["pesquisa_qualitativa_avancada"])
router_latent_themes = APIRouter(prefix="/api/v1/pesquisa_qua/latent_themes", tags=["pesquisa_qualitativa_avancada"])
router_lifeworld = APIRouter(prefix="/api/v1/pesquisa_qua/lifeworld", tags=["pesquisa_qualitativa_avancada"])
router_line_of_argument = APIRouter(prefix="/api/v1/pesquisa_qua/line_of_argument", tags=["pesquisa_qualitativa_avancada"])
router_manifest_content = APIRouter(prefix="/api/v1/pesquisa_qua/manifest_content", tags=["pesquisa_qualitativa_avancada"])
router_member_checking = APIRouter(prefix="/api/v1/pesquisa_qua/member_checking", tags=["pesquisa_qualitativa_avancada"])
router_membership_categoriz = APIRouter(prefix="/api/v1/pesquisa_qua/membership_categorization", tags=["pesquisa_qualitativa_avancada"])
router_merleau_ponty_body = APIRouter(prefix="/api/v1/pesquisa_qua/merleau_ponty_body", tags=["pesquisa_qualitativa_avancada"])
router_meta_ethnography = APIRouter(prefix="/api/v1/pesquisa_qua/meta_ethnography", tags=["pesquisa_qualitativa_avancada"])
router_method_triangulation = APIRouter(prefix="/api/v1/pesquisa_qua/method_triangulation", tags=["pesquisa_qualitativa_avancada"])
router_narrative_inquiry2 = APIRouter(prefix="/api/v1/pesquisa_qua/narrative_inquiry2", tags=["pesquisa_qualitativa_avancada"])
router_narrative_turn = APIRouter(prefix="/api/v1/pesquisa_qua/narrative_turn", tags=["pesquisa_qualitativa_avancada"])
router_negative_case = APIRouter(prefix="/api/v1/pesquisa_qua/negative_case", tags=["pesquisa_qualitativa_avancada"])
router_noblit_hare = APIRouter(prefix="/api/v1/pesquisa_qua/noblit_hare", tags=["pesquisa_qualitativa_avancada"])
router_participant_observat = APIRouter(prefix="/api/v1/pesquisa_qua/participant_observation", tags=["pesquisa_qualitativa_avancada"])
router_peer_debriefing = APIRouter(prefix="/api/v1/pesquisa_qua/peer_debriefing", tags=["pesquisa_qualitativa_avancada"])
router_personal_narrative = APIRouter(prefix="/api/v1/pesquisa_qua/personal_narrative", tags=["pesquisa_qualitativa_avancada"])
router_phenomenology2 = APIRouter(prefix="/api/v1/pesquisa_qua/phenomenology2", tags=["pesquisa_qualitativa_avancada"])
router_positionality = APIRouter(prefix="/api/v1/pesquisa_qua/positionality", tags=["pesquisa_qualitativa_avancada"])
router_preference_organizat = APIRouter(prefix="/api/v1/pesquisa_qua/preference_organization", tags=["pesquisa_qualitativa_avancada"])
router_prolonged_engagement = APIRouter(prefix="/api/v1/pesquisa_qua/prolonged_engagement", tags=["pesquisa_qualitativa_avancada"])
router_qualitative_meta_syn = APIRouter(prefix="/api/v1/pesquisa_qua/qualitative_meta_synthesi", tags=["pesquisa_qualitativa_avancada"])
router_realist_thematic = APIRouter(prefix="/api/v1/pesquisa_qua/realist_thematic", tags=["pesquisa_qualitativa_avancada"])
router_reciprocal_translati = APIRouter(prefix="/api/v1/pesquisa_qua/reciprocal_translation", tags=["pesquisa_qualitativa_avancada"])
router_reflexive_thematic = APIRouter(prefix="/api/v1/pesquisa_qua/reflexive_thematic", tags=["pesquisa_qualitativa_avancada"])
router_reflexivity_ethnogra = APIRouter(prefix="/api/v1/pesquisa_qua/reflexivity_ethnography", tags=["pesquisa_qualitativa_avancada"])
router_refutational_synthes = APIRouter(prefix="/api/v1/pesquisa_qua/refutational_synthesis", tags=["pesquisa_qualitativa_avancada"])
router_repair_sequences = APIRouter(prefix="/api/v1/pesquisa_qua/repair_sequences", tags=["pesquisa_qualitativa_avancada"])
router_ricoeur_narrative = APIRouter(prefix="/api/v1/pesquisa_qua/ricoeur_narrative", tags=["pesquisa_qualitativa_avancada"])
router_saturacao_qualitativ = APIRouter(prefix="/api/v1/pesquisa_qua/saturacao_qualitativa", tags=["pesquisa_qualitativa_avancada"])
router_semantic_themes = APIRouter(prefix="/api/v1/pesquisa_qua/semantic_themes", tags=["pesquisa_qualitativa_avancada"])
router_sequential_organizat = APIRouter(prefix="/api/v1/pesquisa_qua/sequential_organization", tags=["pesquisa_qualitativa_avancada"])
router_situational_analysis = APIRouter(prefix="/api/v1/pesquisa_qua/situational_analysis", tags=["pesquisa_qualitativa_avancada"])
router_srqr_reporting = APIRouter(prefix="/api/v1/pesquisa_qua/srqr_reporting", tags=["pesquisa_qualitativa_avancada"])
router_storied_lives = APIRouter(prefix="/api/v1/pesquisa_qua/storied_lives", tags=["pesquisa_qualitativa_avancada"])
router_summative_content = APIRouter(prefix="/api/v1/pesquisa_qua/summative_content", tags=["pesquisa_qualitativa_avancada"])
router_talk_in_interaction = APIRouter(prefix="/api/v1/pesquisa_qua/talk_in_interaction", tags=["pesquisa_qualitativa_avancada"])
router_temporal_sequence = APIRouter(prefix="/api/v1/pesquisa_qua/temporal_sequence", tags=["pesquisa_qualitativa_avancada"])
router_thematic_analysis = APIRouter(prefix="/api/v1/pesquisa_qua/thematic_analysis", tags=["pesquisa_qualitativa_avancada"])
router_theoretical_triangul = APIRouter(prefix="/api/v1/pesquisa_qua/theoretical_triangulation", tags=["pesquisa_qualitativa_avancada"])
router_thick_description = APIRouter(prefix="/api/v1/pesquisa_qua/thick_description", tags=["pesquisa_qualitativa_avancada"])
router_three_dimensional_sp = APIRouter(prefix="/api/v1/pesquisa_qua/three_dimensional_space", tags=["pesquisa_qualitativa_avancada"])
router_transfer_qualitative = APIRouter(prefix="/api/v1/pesquisa_qua/transfer_qualitative", tags=["pesquisa_qualitativa_avancada"])
router_triangulation_qualit = APIRouter(prefix="/api/v1/pesquisa_qua/triangulation_qualitative", tags=["pesquisa_qualitativa_avancada"])
router_trustworthiness_qual = APIRouter(prefix="/api/v1/pesquisa_qua/trustworthiness_qualitati", tags=["pesquisa_qualitativa_avancada"])
router_turn_taking = APIRouter(prefix="/api/v1/pesquisa_qua/turn_taking", tags=["pesquisa_qualitativa_avancada"])

@router_adjacency_pairs.get("")
async def i_adjacency_pairs():
    return {"p":"pesquisa_qualit_adjacency_pairs","s":"ativo","t":datetime.utcnow().isoformat()}
@router_analytical_autoethno.get("")
async def i_analytical_autoethno():
    return {"p":"pesquisa_qualit_analytical_autoethno","s":"ativo","t":datetime.utcnow().isoformat()}
@router_authenticity_qualita.get("")
async def i_authenticity_qualita():
    return {"p":"pesquisa_qualit_authenticity_qualita","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autoethnography2.get("")
async def i_autoethnography2():
    return {"p":"pesquisa_qualit_autoethnography2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bracketing.get("")
async def i_bracketing():
    return {"p":"pesquisa_qualit_bracketing","s":"ativo","t":datetime.utcnow().isoformat()}
@router_braun_clarke.get("")
async def i_braun_clarke():
    return {"p":"pesquisa_qualit_braun_clarke","s":"ativo","t":datetime.utcnow().isoformat()}
@router_casp_qualitative.get("")
async def i_casp_qualitative():
    return {"p":"pesquisa_qualit_casp_qualitative","s":"ativo","t":datetime.utcnow().isoformat()}
@router_classical_gt.get("")
async def i_classical_gt():
    return {"p":"pesquisa_qualit_classical_gt","s":"ativo","t":datetime.utcnow().isoformat()}
@router_collaborative_autoet.get("")
async def i_collaborative_autoet():
    return {"p":"pesquisa_qualit_collaborative_autoet","s":"ativo","t":datetime.utcnow().isoformat()}
@router_confirmability.get("")
async def i_confirmability():
    return {"p":"pesquisa_qualit_confirmability","s":"ativo","t":datetime.utcnow().isoformat()}
@router_consolidation_qualit.get("")
async def i_consolidation_qualit():
    return {"p":"pesquisa_qualit_consolidation_qualit","s":"ativo","t":datetime.utcnow().isoformat()}
@router_constructionist.get("")
async def i_constructionist():
    return {"p":"pesquisa_qualit_constructionist","s":"ativo","t":datetime.utcnow().isoformat()}
@router_constructivist_gt.get("")
async def i_constructivist_gt():
    return {"p":"pesquisa_qualit_constructivist_gt","s":"ativo","t":datetime.utcnow().isoformat()}
@router_content_analysis2.get("")
async def i_content_analysis2():
    return {"p":"pesquisa_qualit_content_analysis2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_conversation_analysi.get("")
async def i_conversation_analysi():
    return {"p":"pesquisa_qualit_conversation_analysi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_coreq_reporting.get("")
async def i_coreq_reporting():
    return {"p":"pesquisa_qualit_coreq_reporting","s":"ativo","t":datetime.utcnow().isoformat()}
@router_credibility_qualitat.get("")
async def i_credibility_qualitat():
    return {"p":"pesquisa_qualit_credibility_qualitat","s":"ativo","t":datetime.utcnow().isoformat()}
@router_critical_appraisal_q.get("")
async def i_critical_appraisal_q():
    return {"p":"pesquisa_qualit_critical_appraisal_q","s":"ativo","t":datetime.utcnow().isoformat()}
@router_critical_discourse.get("")
async def i_critical_discourse():
    return {"p":"pesquisa_qualit_critical_discourse","s":"ativo","t":datetime.utcnow().isoformat()}
@router_data_triangulation.get("")
async def i_data_triangulation():
    return {"p":"pesquisa_qualit_data_triangulation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dependability_qualit.get("")
async def i_dependability_qualit():
    return {"p":"pesquisa_qualit_dependability_qualit","s":"ativo","t":datetime.utcnow().isoformat()}
@router_descriptive_phenomen.get("")
async def i_descriptive_phenomen():
    return {"p":"pesquisa_qualit_descriptive_phenomen","s":"ativo","t":datetime.utcnow().isoformat()}
@router_directed_content.get("")
async def i_directed_content():
    return {"p":"pesquisa_qualit_directed_content","s":"ativo","t":datetime.utcnow().isoformat()}
@router_discourse_analysis2.get("")
async def i_discourse_analysis2():
    return {"p":"pesquisa_qualit_discourse_analysis2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_duoethnography.get("")
async def i_duoethnography():
    return {"p":"pesquisa_qualit_duoethnography","s":"ativo","t":datetime.utcnow().isoformat()}
@router_emplotment.get("")
async def i_emplotment():
    return {"p":"pesquisa_qualit_emplotment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_equator_qualitative.get("")
async def i_equator_qualitative():
    return {"p":"pesquisa_qualit_equator_qualitative","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ethnographic_intervi.get("")
async def i_ethnographic_intervi():
    return {"p":"pesquisa_qualit_ethnographic_intervi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ethnography2.get("")
async def i_ethnography2():
    return {"p":"pesquisa_qualit_ethnography2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_evocative_autoethnog.get("")
async def i_evocative_autoethnog():
    return {"p":"pesquisa_qualit_evocative_autoethnog","s":"ativo","t":datetime.utcnow().isoformat()}
@router_existential_phenomen.get("")
async def i_existential_phenomen():
    return {"p":"pesquisa_qualit_existential_phenomen","s":"ativo","t":datetime.utcnow().isoformat()}
@router_field_notes.get("")
async def i_field_notes():
    return {"p":"pesquisa_qualit_field_notes","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gadamer_hermeneutic.get("")
async def i_gadamer_hermeneutic():
    return {"p":"pesquisa_qualit_gadamer_hermeneutic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_geertz_culture.get("")
async def i_geertz_culture():
    return {"p":"pesquisa_qualit_geertz_culture","s":"ativo","t":datetime.utcnow().isoformat()}
@router_going_native.get("")
async def i_going_native():
    return {"p":"pesquisa_qualit_going_native","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grounded_theory2.get("")
async def i_grounded_theory2():
    return {"p":"pesquisa_qualit_grounded_theory2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_heidegger_analysis.get("")
async def i_heidegger_analysis():
    return {"p":"pesquisa_qualit_heidegger_analysis","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hermeneutic_phenomen.get("")
async def i_hermeneutic_phenomen():
    return {"p":"pesquisa_qualit_hermeneutic_phenomen","s":"ativo","t":datetime.utcnow().isoformat()}
@router_husserl_analysis.get("")
async def i_husserl_analysis():
    return {"p":"pesquisa_qualit_husserl_analysis","s":"ativo","t":datetime.utcnow().isoformat()}
@router_identity_constructio.get("")
async def i_identity_constructio():
    return {"p":"pesquisa_qualit_identity_constructio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_interpretive_phenome.get("")
async def i_interpretive_phenome():
    return {"p":"pesquisa_qualit_interpretive_phenome","s":"ativo","t":datetime.utcnow().isoformat()}
@router_interpretive_themati.get("")
async def i_interpretive_themati():
    return {"p":"pesquisa_qualit_interpretive_themati","s":"ativo","t":datetime.utcnow().isoformat()}
@router_investigator_triangu.get("")
async def i_investigator_triangu():
    return {"p":"pesquisa_qualit_investigator_triangu","s":"ativo","t":datetime.utcnow().isoformat()}
@router_key_informant.get("")
async def i_key_informant():
    return {"p":"pesquisa_qualit_key_informant","s":"ativo","t":datetime.utcnow().isoformat()}
@router_landscape_inquiry.get("")
async def i_landscape_inquiry():
    return {"p":"pesquisa_qualit_landscape_inquiry","s":"ativo","t":datetime.utcnow().isoformat()}
@router_latent_content.get("")
async def i_latent_content():
    return {"p":"pesquisa_qualit_latent_content","s":"ativo","t":datetime.utcnow().isoformat()}
@router_latent_themes.get("")
async def i_latent_themes():
    return {"p":"pesquisa_qualit_latent_themes","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lifeworld.get("")
async def i_lifeworld():
    return {"p":"pesquisa_qualit_lifeworld","s":"ativo","t":datetime.utcnow().isoformat()}
@router_line_of_argument.get("")
async def i_line_of_argument():
    return {"p":"pesquisa_qualit_line_of_argument","s":"ativo","t":datetime.utcnow().isoformat()}
@router_manifest_content.get("")
async def i_manifest_content():
    return {"p":"pesquisa_qualit_manifest_content","s":"ativo","t":datetime.utcnow().isoformat()}
@router_member_checking.get("")
async def i_member_checking():
    return {"p":"pesquisa_qualit_member_checking","s":"ativo","t":datetime.utcnow().isoformat()}
@router_membership_categoriz.get("")
async def i_membership_categoriz():
    return {"p":"pesquisa_qualit_membership_categoriz","s":"ativo","t":datetime.utcnow().isoformat()}
@router_merleau_ponty_body.get("")
async def i_merleau_ponty_body():
    return {"p":"pesquisa_qualit_merleau_ponty_body","s":"ativo","t":datetime.utcnow().isoformat()}
@router_meta_ethnography.get("")
async def i_meta_ethnography():
    return {"p":"pesquisa_qualit_meta_ethnography","s":"ativo","t":datetime.utcnow().isoformat()}
@router_method_triangulation.get("")
async def i_method_triangulation():
    return {"p":"pesquisa_qualit_method_triangulation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_narrative_inquiry2.get("")
async def i_narrative_inquiry2():
    return {"p":"pesquisa_qualit_narrative_inquiry2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_narrative_turn.get("")
async def i_narrative_turn():
    return {"p":"pesquisa_qualit_narrative_turn","s":"ativo","t":datetime.utcnow().isoformat()}
@router_negative_case.get("")
async def i_negative_case():
    return {"p":"pesquisa_qualit_negative_case","s":"ativo","t":datetime.utcnow().isoformat()}
@router_noblit_hare.get("")
async def i_noblit_hare():
    return {"p":"pesquisa_qualit_noblit_hare","s":"ativo","t":datetime.utcnow().isoformat()}
@router_participant_observat.get("")
async def i_participant_observat():
    return {"p":"pesquisa_qualit_participant_observat","s":"ativo","t":datetime.utcnow().isoformat()}
@router_peer_debriefing.get("")
async def i_peer_debriefing():
    return {"p":"pesquisa_qualit_peer_debriefing","s":"ativo","t":datetime.utcnow().isoformat()}
@router_personal_narrative.get("")
async def i_personal_narrative():
    return {"p":"pesquisa_qualit_personal_narrative","s":"ativo","t":datetime.utcnow().isoformat()}
@router_phenomenology2.get("")
async def i_phenomenology2():
    return {"p":"pesquisa_qualit_phenomenology2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_positionality.get("")
async def i_positionality():
    return {"p":"pesquisa_qualit_positionality","s":"ativo","t":datetime.utcnow().isoformat()}
@router_preference_organizat.get("")
async def i_preference_organizat():
    return {"p":"pesquisa_qualit_preference_organizat","s":"ativo","t":datetime.utcnow().isoformat()}
@router_prolonged_engagement.get("")
async def i_prolonged_engagement():
    return {"p":"pesquisa_qualit_prolonged_engagement","s":"ativo","t":datetime.utcnow().isoformat()}
@router_qualitative_meta_syn.get("")
async def i_qualitative_meta_syn():
    return {"p":"pesquisa_qualit_qualitative_meta_syn","s":"ativo","t":datetime.utcnow().isoformat()}
@router_realist_thematic.get("")
async def i_realist_thematic():
    return {"p":"pesquisa_qualit_realist_thematic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reciprocal_translati.get("")
async def i_reciprocal_translati():
    return {"p":"pesquisa_qualit_reciprocal_translati","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reflexive_thematic.get("")
async def i_reflexive_thematic():
    return {"p":"pesquisa_qualit_reflexive_thematic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reflexivity_ethnogra.get("")
async def i_reflexivity_ethnogra():
    return {"p":"pesquisa_qualit_reflexivity_ethnogra","s":"ativo","t":datetime.utcnow().isoformat()}
@router_refutational_synthes.get("")
async def i_refutational_synthes():
    return {"p":"pesquisa_qualit_refutational_synthes","s":"ativo","t":datetime.utcnow().isoformat()}
@router_repair_sequences.get("")
async def i_repair_sequences():
    return {"p":"pesquisa_qualit_repair_sequences","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ricoeur_narrative.get("")
async def i_ricoeur_narrative():
    return {"p":"pesquisa_qualit_ricoeur_narrative","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saturacao_qualitativ.get("")
async def i_saturacao_qualitativ():
    return {"p":"pesquisa_qualit_saturacao_qualitativ","s":"ativo","t":datetime.utcnow().isoformat()}
@router_semantic_themes.get("")
async def i_semantic_themes():
    return {"p":"pesquisa_qualit_semantic_themes","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sequential_organizat.get("")
async def i_sequential_organizat():
    return {"p":"pesquisa_qualit_sequential_organizat","s":"ativo","t":datetime.utcnow().isoformat()}
@router_situational_analysis.get("")
async def i_situational_analysis():
    return {"p":"pesquisa_qualit_situational_analysis","s":"ativo","t":datetime.utcnow().isoformat()}
@router_srqr_reporting.get("")
async def i_srqr_reporting():
    return {"p":"pesquisa_qualit_srqr_reporting","s":"ativo","t":datetime.utcnow().isoformat()}
@router_storied_lives.get("")
async def i_storied_lives():
    return {"p":"pesquisa_qualit_storied_lives","s":"ativo","t":datetime.utcnow().isoformat()}
@router_summative_content.get("")
async def i_summative_content():
    return {"p":"pesquisa_qualit_summative_content","s":"ativo","t":datetime.utcnow().isoformat()}
@router_talk_in_interaction.get("")
async def i_talk_in_interaction():
    return {"p":"pesquisa_qualit_talk_in_interaction","s":"ativo","t":datetime.utcnow().isoformat()}
@router_temporal_sequence.get("")
async def i_temporal_sequence():
    return {"p":"pesquisa_qualit_temporal_sequence","s":"ativo","t":datetime.utcnow().isoformat()}
@router_thematic_analysis.get("")
async def i_thematic_analysis():
    return {"p":"pesquisa_qualit_thematic_analysis","s":"ativo","t":datetime.utcnow().isoformat()}
@router_theoretical_triangul.get("")
async def i_theoretical_triangul():
    return {"p":"pesquisa_qualit_theoretical_triangul","s":"ativo","t":datetime.utcnow().isoformat()}
@router_thick_description.get("")
async def i_thick_description():
    return {"p":"pesquisa_qualit_thick_description","s":"ativo","t":datetime.utcnow().isoformat()}
@router_three_dimensional_sp.get("")
async def i_three_dimensional_sp():
    return {"p":"pesquisa_qualit_three_dimensional_sp","s":"ativo","t":datetime.utcnow().isoformat()}
@router_transfer_qualitative.get("")
async def i_transfer_qualitative():
    return {"p":"pesquisa_qualit_transfer_qualitative","s":"ativo","t":datetime.utcnow().isoformat()}
@router_triangulation_qualit.get("")
async def i_triangulation_qualit():
    return {"p":"pesquisa_qualit_triangulation_qualit","s":"ativo","t":datetime.utcnow().isoformat()}
@router_trustworthiness_qual.get("")
async def i_trustworthiness_qual():
    return {"p":"pesquisa_qualit_trustworthiness_qual","s":"ativo","t":datetime.utcnow().isoformat()}
@router_turn_taking.get("")
async def i_turn_taking():
    return {"p":"pesquisa_qualit_turn_taking","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_pesquisa_qualitativa(PluginBase):
    name = "consolidated_pesquisa_qualitativa_avancada"
    def setup(self, app):
        app.include_router(router_adjacency_pairs)
        app.include_router(router_analytical_autoethno)
        app.include_router(router_authenticity_qualita)
        app.include_router(router_autoethnography2)
        app.include_router(router_bracketing)
        app.include_router(router_braun_clarke)
        app.include_router(router_casp_qualitative)
        app.include_router(router_classical_gt)
        app.include_router(router_collaborative_autoet)
        app.include_router(router_confirmability)
        app.include_router(router_consolidation_qualit)
        app.include_router(router_constructionist)
        app.include_router(router_constructivist_gt)
        app.include_router(router_content_analysis2)
        app.include_router(router_conversation_analysi)
        app.include_router(router_coreq_reporting)
        app.include_router(router_credibility_qualitat)
        app.include_router(router_critical_appraisal_q)
        app.include_router(router_critical_discourse)
        app.include_router(router_data_triangulation)
        app.include_router(router_dependability_qualit)
        app.include_router(router_descriptive_phenomen)
        app.include_router(router_directed_content)
        app.include_router(router_discourse_analysis2)
        app.include_router(router_duoethnography)
        app.include_router(router_emplotment)
        app.include_router(router_equator_qualitative)
        app.include_router(router_ethnographic_intervi)
        app.include_router(router_ethnography2)
        app.include_router(router_evocative_autoethnog)
        app.include_router(router_existential_phenomen)
        app.include_router(router_field_notes)
        app.include_router(router_gadamer_hermeneutic)
        app.include_router(router_geertz_culture)
        app.include_router(router_going_native)
        app.include_router(router_grounded_theory2)
        app.include_router(router_heidegger_analysis)
        app.include_router(router_hermeneutic_phenomen)
        app.include_router(router_husserl_analysis)
        app.include_router(router_identity_constructio)
        app.include_router(router_interpretive_phenome)
        app.include_router(router_interpretive_themati)
        app.include_router(router_investigator_triangu)
        app.include_router(router_key_informant)
        app.include_router(router_landscape_inquiry)
        app.include_router(router_latent_content)
        app.include_router(router_latent_themes)
        app.include_router(router_lifeworld)
        app.include_router(router_line_of_argument)
        app.include_router(router_manifest_content)
        app.include_router(router_member_checking)
        app.include_router(router_membership_categoriz)
        app.include_router(router_merleau_ponty_body)
        app.include_router(router_meta_ethnography)
        app.include_router(router_method_triangulation)
        app.include_router(router_narrative_inquiry2)
        app.include_router(router_narrative_turn)
        app.include_router(router_negative_case)
        app.include_router(router_noblit_hare)
        app.include_router(router_participant_observat)
        app.include_router(router_peer_debriefing)
        app.include_router(router_personal_narrative)
        app.include_router(router_phenomenology2)
        app.include_router(router_positionality)
        app.include_router(router_preference_organizat)
        app.include_router(router_prolonged_engagement)
        app.include_router(router_qualitative_meta_syn)
        app.include_router(router_realist_thematic)
        app.include_router(router_reciprocal_translati)
        app.include_router(router_reflexive_thematic)
        app.include_router(router_reflexivity_ethnogra)
        app.include_router(router_refutational_synthes)
        app.include_router(router_repair_sequences)
        app.include_router(router_ricoeur_narrative)
        app.include_router(router_saturacao_qualitativ)
        app.include_router(router_semantic_themes)
        app.include_router(router_sequential_organizat)
        app.include_router(router_situational_analysis)
        app.include_router(router_srqr_reporting)
        app.include_router(router_storied_lives)
        app.include_router(router_summative_content)
        app.include_router(router_talk_in_interaction)
        app.include_router(router_temporal_sequence)
        app.include_router(router_thematic_analysis)
        app.include_router(router_theoretical_triangul)
        app.include_router(router_thick_description)
        app.include_router(router_three_dimensional_sp)
        app.include_router(router_transfer_qualitative)
        app.include_router(router_triangulation_qualit)
        app.include_router(router_trustworthiness_qual)
        app.include_router(router_turn_taking)


plugin = Plugin_pesquisa_qualitativa()
