from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_actor_observer_bias = APIRouter(prefix="/api/v1/psicologia_s/actor_observer_bias", tags=["psicologia_social_avancada"])
router_ambivalent_sexism = APIRouter(prefix="/api/v1/psicologia_s/ambivalent_sexism", tags=["psicologia_social_avancada"])
router_anchoring_bias = APIRouter(prefix="/api/v1/psicologia_s/anchoring_bias", tags=["psicologia_social_avancada"])
router_asch_experimento = APIRouter(prefix="/api/v1/psicologia_s/asch_experimento", tags=["psicologia_social_avancada"])
router_atitude_formacao = APIRouter(prefix="/api/v1/psicologia_s/atitude_formacao", tags=["psicologia_social_avancada"])
router_atitude_mudanca = APIRouter(prefix="/api/v1/psicologia_s/atitude_mudanca", tags=["psicologia_social_avancada"])
router_atratividade_fonte = APIRouter(prefix="/api/v1/psicologia_s/atratividade_fonte", tags=["psicologia_social_avancada"])
router_attribution_theory = APIRouter(prefix="/api/v1/psicologia_s/attribution_theory", tags=["psicologia_social_avancada"])
router_audience_effect = APIRouter(prefix="/api/v1/psicologia_s/audience_effect", tags=["psicologia_social_avancada"])
router_authority_influence = APIRouter(prefix="/api/v1/psicologia_s/authority_influence", tags=["psicologia_social_avancada"])
router_authority_principle = APIRouter(prefix="/api/v1/psicologia_s/authority_principle", tags=["psicologia_social_avancada"])
router_availability = APIRouter(prefix="/api/v1/psicologia_s/availability", tags=["psicologia_social_avancada"])
router_backfire_effect = APIRouter(prefix="/api/v1/psicologia_s/backfire_effect", tags=["psicologia_social_avancada"])
router_base_rate_fallacy = APIRouter(prefix="/api/v1/psicologia_s/base_rate_fallacy", tags=["psicologia_social_avancada"])
router_benevolent_sexism = APIRouter(prefix="/api/v1/psicologia_s/benevolent_sexism", tags=["psicologia_social_avancada"])
router_bystander_effect = APIRouter(prefix="/api/v1/psicologia_s/bystander_effect", tags=["psicologia_social_avancada"])
router_cautious_shift = APIRouter(prefix="/api/v1/psicologia_s/cautious_shift", tags=["psicologia_social_avancada"])
router_central_peripheral_r = APIRouter(prefix="/api/v1/psicologia_s/central_peripheral_route", tags=["psicologia_social_avancada"])
router_coaction_effect = APIRouter(prefix="/api/v1/psicologia_s/coaction_effect", tags=["psicologia_social_avancada"])
router_cognitive_dissonance = APIRouter(prefix="/api/v1/psicologia_s/cognitive_dissonance2", tags=["psicologia_social_avancada"])
router_collective_efficacy = APIRouter(prefix="/api/v1/psicologia_s/collective_efficacy", tags=["psicologia_social_avancada"])
router_colorblind_racism = APIRouter(prefix="/api/v1/psicologia_s/colorblind_racism", tags=["psicologia_social_avancada"])
router_commitment_consisten = APIRouter(prefix="/api/v1/psicologia_s/commitment_consistency", tags=["psicologia_social_avancada"])
router_confirmation_bias = APIRouter(prefix="/api/v1/psicologia_s/confirmation_bias", tags=["psicologia_social_avancada"])
router_conformidade_social = APIRouter(prefix="/api/v1/psicologia_s/conformidade_social", tags=["psicologia_social_avancada"])
router_consistency_minority = APIRouter(prefix="/api/v1/psicologia_s/consistency_minority", tags=["psicologia_social_avancada"])
router_contact_hypothesis = APIRouter(prefix="/api/v1/psicologia_s/contact_hypothesis", tags=["psicologia_social_avancada"])
router_credibilidade_fonte = APIRouter(prefix="/api/v1/psicologia_s/credibilidade_fonte", tags=["psicologia_social_avancada"])
router_deindividuation = APIRouter(prefix="/api/v1/psicologia_s/deindividuation", tags=["psicologia_social_avancada"])
router_diffusion_responsibi = APIRouter(prefix="/api/v1/psicologia_s/diffusion_responsibility", tags=["psicologia_social_avancada"])
router_discrimination = APIRouter(prefix="/api/v1/psicologia_s/discrimination", tags=["psicologia_social_avancada"])
router_dispositional_attrib = APIRouter(prefix="/api/v1/psicologia_s/dispositional_attribution", tags=["psicologia_social_avancada"])
router_dual_process = APIRouter(prefix="/api/v1/psicologia_s/dual_process", tags=["psicologia_social_avancada"])
router_dunning_kruger = APIRouter(prefix="/api/v1/psicologia_s/dunning_kruger", tags=["psicologia_social_avancada"])
router_elaboration_likeliho = APIRouter(prefix="/api/v1/psicologia_s/elaboration_likelihood", tags=["psicologia_social_avancada"])
router_external_attribution = APIRouter(prefix="/api/v1/psicologia_s/external_attribution", tags=["psicologia_social_avancada"])
router_fear_appeal = APIRouter(prefix="/api/v1/psicologia_s/fear_appeal", tags=["psicologia_social_avancada"])
router_flexibility_minority = APIRouter(prefix="/api/v1/psicologia_s/flexibility_minority", tags=["psicologia_social_avancada"])
router_free_rider_problem = APIRouter(prefix="/api/v1/psicologia_s/free_rider_problem", tags=["psicologia_social_avancada"])
router_fundamental_attribut = APIRouter(prefix="/api/v1/psicologia_s/fundamental_attribution", tags=["psicologia_social_avancada"])
router_genovese_syndrome = APIRouter(prefix="/api/v1/psicologia_s/genovese_syndrome", tags=["psicologia_social_avancada"])
router_glass_ceiling2 = APIRouter(prefix="/api/v1/psicologia_s/glass_ceiling2", tags=["psicologia_social_avancada"])
router_group_polarization = APIRouter(prefix="/api/v1/psicologia_s/group_polarization", tags=["psicologia_social_avancada"])
router_groupthink = APIRouter(prefix="/api/v1/psicologia_s/groupthink", tags=["psicologia_social_avancada"])
router_heuristic_systematic = APIRouter(prefix="/api/v1/psicologia_s/heuristic_systematic", tags=["psicologia_social_avancada"])
router_hostile_sexism = APIRouter(prefix="/api/v1/psicologia_s/hostile_sexism", tags=["psicologia_social_avancada"])
router_humor_appeal = APIRouter(prefix="/api/v1/psicologia_s/humor_appeal", tags=["psicologia_social_avancada"])
router_identification = APIRouter(prefix="/api/v1/psicologia_s/identification", tags=["psicologia_social_avancada"])
router_illusory_superiority = APIRouter(prefix="/api/v1/psicologia_s/illusory_superiority", tags=["psicologia_social_avancada"])
router_implicit_association = APIRouter(prefix="/api/v1/psicologia_s/implicit_association", tags=["psicologia_social_avancada"])
router_informational = APIRouter(prefix="/api/v1/psicologia_s/informational", tags=["psicologia_social_avancada"])
router_ingroup_outgroup = APIRouter(prefix="/api/v1/psicologia_s/ingroup_outgroup", tags=["psicologia_social_avancada"])
router_institutional_racism = APIRouter(prefix="/api/v1/psicologia_s/institutional_racism", tags=["psicologia_social_avancada"])
router_intergroup_contact = APIRouter(prefix="/api/v1/psicologia_s/intergroup_contact", tags=["psicologia_social_avancada"])
router_internal_attribution = APIRouter(prefix="/api/v1/psicologia_s/internal_attribution", tags=["psicologia_social_avancada"])
router_legitimacy = APIRouter(prefix="/api/v1/psicologia_s/legitimacy", tags=["psicologia_social_avancada"])
router_liking_principle2 = APIRouter(prefix="/api/v1/psicologia_s/liking_principle2", tags=["psicologia_social_avancada"])
router_media_influence2 = APIRouter(prefix="/api/v1/psicologia_s/media_influence2", tags=["psicologia_social_avancada"])
router_mensagem_framing = APIRouter(prefix="/api/v1/psicologia_s/mensagem_framing", tags=["psicologia_social_avancada"])
router_microaggression2 = APIRouter(prefix="/api/v1/psicologia_s/microaggression2", tags=["psicologia_social_avancada"])
router_milgram_experimento = APIRouter(prefix="/api/v1/psicologia_s/milgram_experimento", tags=["psicologia_social_avancada"])
router_minimal_group = APIRouter(prefix="/api/v1/psicologia_s/minimal_group", tags=["psicologia_social_avancada"])
router_minority_influence = APIRouter(prefix="/api/v1/psicologia_s/minority_influence", tags=["psicologia_social_avancada"])
router_modelagem_social = APIRouter(prefix="/api/v1/psicologia_s/modelagem_social", tags=["psicologia_social_avancada"])
router_narrative_persuasion = APIRouter(prefix="/api/v1/psicologia_s/narrative_persuasion", tags=["psicologia_social_avancada"])
router_normative_influence = APIRouter(prefix="/api/v1/psicologia_s/normative_influence", tags=["psicologia_social_avancada"])
router_obediencia_autoridad = APIRouter(prefix="/api/v1/psicologia_s/obediencia_autoridade", tags=["psicologia_social_avancada"])
router_observacional_learni = APIRouter(prefix="/api/v1/psicologia_s/observacional_learning", tags=["psicologia_social_avancada"])
router_parasocial_relations = APIRouter(prefix="/api/v1/psicologia_s/parasocial_relationship", tags=["psicologia_social_avancada"])
router_persuasao_social = APIRouter(prefix="/api/v1/psicologia_s/persuasao_social", tags=["psicologia_social_avancada"])
router_prejudice_reduction = APIRouter(prefix="/api/v1/psicologia_s/prejudice_reduction", tags=["psicologia_social_avancada"])
router_proxy_efficacy = APIRouter(prefix="/api/v1/psicologia_s/proxy_efficacy", tags=["psicologia_social_avancada"])
router_racism_types = APIRouter(prefix="/api/v1/psicologia_s/racism_types", tags=["psicologia_social_avancada"])
router_reactance = APIRouter(prefix="/api/v1/psicologia_s/reactance", tags=["psicologia_social_avancada"])
router_reciprocity_principl = APIRouter(prefix="/api/v1/psicologia_s/reciprocity_principle", tags=["psicologia_social_avancada"])
router_representativeness = APIRouter(prefix="/api/v1/psicologia_s/representativeness", tags=["psicologia_social_avancada"])
router_ringelmann_effect = APIRouter(prefix="/api/v1/psicologia_s/ringelmann_effect", tags=["psicologia_social_avancada"])
router_risky_shift = APIRouter(prefix="/api/v1/psicologia_s/risky_shift", tags=["psicologia_social_avancada"])
router_scarcity_principle = APIRouter(prefix="/api/v1/psicologia_s/scarcity_principle", tags=["psicologia_social_avancada"])
router_self_categorization = APIRouter(prefix="/api/v1/psicologia_s/self_categorization", tags=["psicologia_social_avancada"])
router_self_efficacy_bandur = APIRouter(prefix="/api/v1/psicologia_s/self_efficacy_bandura2", tags=["psicologia_social_avancada"])
router_self_serving_bias = APIRouter(prefix="/api/v1/psicologia_s/self_serving_bias", tags=["psicologia_social_avancada"])
router_situational = APIRouter(prefix="/api/v1/psicologia_s/situational", tags=["psicologia_social_avancada"])
router_snowball_minority = APIRouter(prefix="/api/v1/psicologia_s/snowball_minority", tags=["psicologia_social_avancada"])
router_social_facilitation = APIRouter(prefix="/api/v1/psicologia_s/social_facilitation", tags=["psicologia_social_avancada"])
router_social_identity_theo = APIRouter(prefix="/api/v1/psicologia_s/social_identity_theory", tags=["psicologia_social_avancada"])
router_social_learning_band = APIRouter(prefix="/api/v1/psicologia_s/social_learning_bandura", tags=["psicologia_social_avancada"])
router_social_loafing = APIRouter(prefix="/api/v1/psicologia_s/social_loafing", tags=["psicologia_social_avancada"])
router_social_proof2 = APIRouter(prefix="/api/v1/psicologia_s/social_proof2", tags=["psicologia_social_avancada"])
router_stereotype_threat = APIRouter(prefix="/api/v1/psicologia_s/stereotype_threat", tags=["psicologia_social_avancada"])
router_systemic = APIRouter(prefix="/api/v1/psicologia_s/systemic", tags=["psicologia_social_avancada"])
router_tokenism = APIRouter(prefix="/api/v1/psicologia_s/tokenism", tags=["psicologia_social_avancada"])
router_transportation_theor = APIRouter(prefix="/api/v1/psicologia_s/transportation_theory", tags=["psicologia_social_avancada"])
router_ultimate_attribution = APIRouter(prefix="/api/v1/psicologia_s/ultimate_attribution", tags=["psicologia_social_avancada"])
router_unity_cialdini = APIRouter(prefix="/api/v1/psicologia_s/unity_cialdini", tags=["psicologia_social_avancada"])
router_vicarious_reinforcem = APIRouter(prefix="/api/v1/psicologia_s/vicarious_reinforcement", tags=["psicologia_social_avancada"])
router_zajonc_arousal = APIRouter(prefix="/api/v1/psicologia_s/zajonc_arousal", tags=["psicologia_social_avancada"])

@router_actor_observer_bias.get("")
async def i_actor_observer_bias():
    return {"p":"psicologia_soci_actor_observer_bias","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ambivalent_sexism.get("")
async def i_ambivalent_sexism():
    return {"p":"psicologia_soci_ambivalent_sexism","s":"ativo","t":datetime.utcnow().isoformat()}
@router_anchoring_bias.get("")
async def i_anchoring_bias():
    return {"p":"psicologia_soci_anchoring_bias","s":"ativo","t":datetime.utcnow().isoformat()}
@router_asch_experimento.get("")
async def i_asch_experimento():
    return {"p":"psicologia_soci_asch_experimento","s":"ativo","t":datetime.utcnow().isoformat()}
@router_atitude_formacao.get("")
async def i_atitude_formacao():
    return {"p":"psicologia_soci_atitude_formacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_atitude_mudanca.get("")
async def i_atitude_mudanca():
    return {"p":"psicologia_soci_atitude_mudanca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_atratividade_fonte.get("")
async def i_atratividade_fonte():
    return {"p":"psicologia_soci_atratividade_fonte","s":"ativo","t":datetime.utcnow().isoformat()}
@router_attribution_theory.get("")
async def i_attribution_theory():
    return {"p":"psicologia_soci_attribution_theory","s":"ativo","t":datetime.utcnow().isoformat()}
@router_audience_effect.get("")
async def i_audience_effect():
    return {"p":"psicologia_soci_audience_effect","s":"ativo","t":datetime.utcnow().isoformat()}
@router_authority_influence.get("")
async def i_authority_influence():
    return {"p":"psicologia_soci_authority_influence","s":"ativo","t":datetime.utcnow().isoformat()}
@router_authority_principle.get("")
async def i_authority_principle():
    return {"p":"psicologia_soci_authority_principle","s":"ativo","t":datetime.utcnow().isoformat()}
@router_availability.get("")
async def i_availability():
    return {"p":"psicologia_soci_availability","s":"ativo","t":datetime.utcnow().isoformat()}
@router_backfire_effect.get("")
async def i_backfire_effect():
    return {"p":"psicologia_soci_backfire_effect","s":"ativo","t":datetime.utcnow().isoformat()}
@router_base_rate_fallacy.get("")
async def i_base_rate_fallacy():
    return {"p":"psicologia_soci_base_rate_fallacy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_benevolent_sexism.get("")
async def i_benevolent_sexism():
    return {"p":"psicologia_soci_benevolent_sexism","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bystander_effect.get("")
async def i_bystander_effect():
    return {"p":"psicologia_soci_bystander_effect","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cautious_shift.get("")
async def i_cautious_shift():
    return {"p":"psicologia_soci_cautious_shift","s":"ativo","t":datetime.utcnow().isoformat()}
@router_central_peripheral_r.get("")
async def i_central_peripheral_r():
    return {"p":"psicologia_soci_central_peripheral_r","s":"ativo","t":datetime.utcnow().isoformat()}
@router_coaction_effect.get("")
async def i_coaction_effect():
    return {"p":"psicologia_soci_coaction_effect","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cognitive_dissonance.get("")
async def i_cognitive_dissonance():
    return {"p":"psicologia_soci_cognitive_dissonance","s":"ativo","t":datetime.utcnow().isoformat()}
@router_collective_efficacy.get("")
async def i_collective_efficacy():
    return {"p":"psicologia_soci_collective_efficacy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_colorblind_racism.get("")
async def i_colorblind_racism():
    return {"p":"psicologia_soci_colorblind_racism","s":"ativo","t":datetime.utcnow().isoformat()}
@router_commitment_consisten.get("")
async def i_commitment_consisten():
    return {"p":"psicologia_soci_commitment_consisten","s":"ativo","t":datetime.utcnow().isoformat()}
@router_confirmation_bias.get("")
async def i_confirmation_bias():
    return {"p":"psicologia_soci_confirmation_bias","s":"ativo","t":datetime.utcnow().isoformat()}
@router_conformidade_social.get("")
async def i_conformidade_social():
    return {"p":"psicologia_soci_conformidade_social","s":"ativo","t":datetime.utcnow().isoformat()}
@router_consistency_minority.get("")
async def i_consistency_minority():
    return {"p":"psicologia_soci_consistency_minority","s":"ativo","t":datetime.utcnow().isoformat()}
@router_contact_hypothesis.get("")
async def i_contact_hypothesis():
    return {"p":"psicologia_soci_contact_hypothesis","s":"ativo","t":datetime.utcnow().isoformat()}
@router_credibilidade_fonte.get("")
async def i_credibilidade_fonte():
    return {"p":"psicologia_soci_credibilidade_fonte","s":"ativo","t":datetime.utcnow().isoformat()}
@router_deindividuation.get("")
async def i_deindividuation():
    return {"p":"psicologia_soci_deindividuation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_diffusion_responsibi.get("")
async def i_diffusion_responsibi():
    return {"p":"psicologia_soci_diffusion_responsibi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_discrimination.get("")
async def i_discrimination():
    return {"p":"psicologia_soci_discrimination","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dispositional_attrib.get("")
async def i_dispositional_attrib():
    return {"p":"psicologia_soci_dispositional_attrib","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dual_process.get("")
async def i_dual_process():
    return {"p":"psicologia_soci_dual_process","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dunning_kruger.get("")
async def i_dunning_kruger():
    return {"p":"psicologia_soci_dunning_kruger","s":"ativo","t":datetime.utcnow().isoformat()}
@router_elaboration_likeliho.get("")
async def i_elaboration_likeliho():
    return {"p":"psicologia_soci_elaboration_likeliho","s":"ativo","t":datetime.utcnow().isoformat()}
@router_external_attribution.get("")
async def i_external_attribution():
    return {"p":"psicologia_soci_external_attribution","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fear_appeal.get("")
async def i_fear_appeal():
    return {"p":"psicologia_soci_fear_appeal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_flexibility_minority.get("")
async def i_flexibility_minority():
    return {"p":"psicologia_soci_flexibility_minority","s":"ativo","t":datetime.utcnow().isoformat()}
@router_free_rider_problem.get("")
async def i_free_rider_problem():
    return {"p":"psicologia_soci_free_rider_problem","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fundamental_attribut.get("")
async def i_fundamental_attribut():
    return {"p":"psicologia_soci_fundamental_attribut","s":"ativo","t":datetime.utcnow().isoformat()}
@router_genovese_syndrome.get("")
async def i_genovese_syndrome():
    return {"p":"psicologia_soci_genovese_syndrome","s":"ativo","t":datetime.utcnow().isoformat()}
@router_glass_ceiling2.get("")
async def i_glass_ceiling2():
    return {"p":"psicologia_soci_glass_ceiling2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_group_polarization.get("")
async def i_group_polarization():
    return {"p":"psicologia_soci_group_polarization","s":"ativo","t":datetime.utcnow().isoformat()}
@router_groupthink.get("")
async def i_groupthink():
    return {"p":"psicologia_soci_groupthink","s":"ativo","t":datetime.utcnow().isoformat()}
@router_heuristic_systematic.get("")
async def i_heuristic_systematic():
    return {"p":"psicologia_soci_heuristic_systematic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hostile_sexism.get("")
async def i_hostile_sexism():
    return {"p":"psicologia_soci_hostile_sexism","s":"ativo","t":datetime.utcnow().isoformat()}
@router_humor_appeal.get("")
async def i_humor_appeal():
    return {"p":"psicologia_soci_humor_appeal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_identification.get("")
async def i_identification():
    return {"p":"psicologia_soci_identification","s":"ativo","t":datetime.utcnow().isoformat()}
@router_illusory_superiority.get("")
async def i_illusory_superiority():
    return {"p":"psicologia_soci_illusory_superiority","s":"ativo","t":datetime.utcnow().isoformat()}
@router_implicit_association.get("")
async def i_implicit_association():
    return {"p":"psicologia_soci_implicit_association","s":"ativo","t":datetime.utcnow().isoformat()}
@router_informational.get("")
async def i_informational():
    return {"p":"psicologia_soci_informational","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ingroup_outgroup.get("")
async def i_ingroup_outgroup():
    return {"p":"psicologia_soci_ingroup_outgroup","s":"ativo","t":datetime.utcnow().isoformat()}
@router_institutional_racism.get("")
async def i_institutional_racism():
    return {"p":"psicologia_soci_institutional_racism","s":"ativo","t":datetime.utcnow().isoformat()}
@router_intergroup_contact.get("")
async def i_intergroup_contact():
    return {"p":"psicologia_soci_intergroup_contact","s":"ativo","t":datetime.utcnow().isoformat()}
@router_internal_attribution.get("")
async def i_internal_attribution():
    return {"p":"psicologia_soci_internal_attribution","s":"ativo","t":datetime.utcnow().isoformat()}
@router_legitimacy.get("")
async def i_legitimacy():
    return {"p":"psicologia_soci_legitimacy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_liking_principle2.get("")
async def i_liking_principle2():
    return {"p":"psicologia_soci_liking_principle2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_media_influence2.get("")
async def i_media_influence2():
    return {"p":"psicologia_soci_media_influence2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mensagem_framing.get("")
async def i_mensagem_framing():
    return {"p":"psicologia_soci_mensagem_framing","s":"ativo","t":datetime.utcnow().isoformat()}
@router_microaggression2.get("")
async def i_microaggression2():
    return {"p":"psicologia_soci_microaggression2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_milgram_experimento.get("")
async def i_milgram_experimento():
    return {"p":"psicologia_soci_milgram_experimento","s":"ativo","t":datetime.utcnow().isoformat()}
@router_minimal_group.get("")
async def i_minimal_group():
    return {"p":"psicologia_soci_minimal_group","s":"ativo","t":datetime.utcnow().isoformat()}
@router_minority_influence.get("")
async def i_minority_influence():
    return {"p":"psicologia_soci_minority_influence","s":"ativo","t":datetime.utcnow().isoformat()}
@router_modelagem_social.get("")
async def i_modelagem_social():
    return {"p":"psicologia_soci_modelagem_social","s":"ativo","t":datetime.utcnow().isoformat()}
@router_narrative_persuasion.get("")
async def i_narrative_persuasion():
    return {"p":"psicologia_soci_narrative_persuasion","s":"ativo","t":datetime.utcnow().isoformat()}
@router_normative_influence.get("")
async def i_normative_influence():
    return {"p":"psicologia_soci_normative_influence","s":"ativo","t":datetime.utcnow().isoformat()}
@router_obediencia_autoridad.get("")
async def i_obediencia_autoridad():
    return {"p":"psicologia_soci_obediencia_autoridad","s":"ativo","t":datetime.utcnow().isoformat()}
@router_observacional_learni.get("")
async def i_observacional_learni():
    return {"p":"psicologia_soci_observacional_learni","s":"ativo","t":datetime.utcnow().isoformat()}
@router_parasocial_relations.get("")
async def i_parasocial_relations():
    return {"p":"psicologia_soci_parasocial_relations","s":"ativo","t":datetime.utcnow().isoformat()}
@router_persuasao_social.get("")
async def i_persuasao_social():
    return {"p":"psicologia_soci_persuasao_social","s":"ativo","t":datetime.utcnow().isoformat()}
@router_prejudice_reduction.get("")
async def i_prejudice_reduction():
    return {"p":"psicologia_soci_prejudice_reduction","s":"ativo","t":datetime.utcnow().isoformat()}
@router_proxy_efficacy.get("")
async def i_proxy_efficacy():
    return {"p":"psicologia_soci_proxy_efficacy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_racism_types.get("")
async def i_racism_types():
    return {"p":"psicologia_soci_racism_types","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reactance.get("")
async def i_reactance():
    return {"p":"psicologia_soci_reactance","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reciprocity_principl.get("")
async def i_reciprocity_principl():
    return {"p":"psicologia_soci_reciprocity_principl","s":"ativo","t":datetime.utcnow().isoformat()}
@router_representativeness.get("")
async def i_representativeness():
    return {"p":"psicologia_soci_representativeness","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ringelmann_effect.get("")
async def i_ringelmann_effect():
    return {"p":"psicologia_soci_ringelmann_effect","s":"ativo","t":datetime.utcnow().isoformat()}
@router_risky_shift.get("")
async def i_risky_shift():
    return {"p":"psicologia_soci_risky_shift","s":"ativo","t":datetime.utcnow().isoformat()}
@router_scarcity_principle.get("")
async def i_scarcity_principle():
    return {"p":"psicologia_soci_scarcity_principle","s":"ativo","t":datetime.utcnow().isoformat()}
@router_self_categorization.get("")
async def i_self_categorization():
    return {"p":"psicologia_soci_self_categorization","s":"ativo","t":datetime.utcnow().isoformat()}
@router_self_efficacy_bandur.get("")
async def i_self_efficacy_bandur():
    return {"p":"psicologia_soci_self_efficacy_bandur","s":"ativo","t":datetime.utcnow().isoformat()}
@router_self_serving_bias.get("")
async def i_self_serving_bias():
    return {"p":"psicologia_soci_self_serving_bias","s":"ativo","t":datetime.utcnow().isoformat()}
@router_situational.get("")
async def i_situational():
    return {"p":"psicologia_soci_situational","s":"ativo","t":datetime.utcnow().isoformat()}
@router_snowball_minority.get("")
async def i_snowball_minority():
    return {"p":"psicologia_soci_snowball_minority","s":"ativo","t":datetime.utcnow().isoformat()}
@router_social_facilitation.get("")
async def i_social_facilitation():
    return {"p":"psicologia_soci_social_facilitation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_social_identity_theo.get("")
async def i_social_identity_theo():
    return {"p":"psicologia_soci_social_identity_theo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_social_learning_band.get("")
async def i_social_learning_band():
    return {"p":"psicologia_soci_social_learning_band","s":"ativo","t":datetime.utcnow().isoformat()}
@router_social_loafing.get("")
async def i_social_loafing():
    return {"p":"psicologia_soci_social_loafing","s":"ativo","t":datetime.utcnow().isoformat()}
@router_social_proof2.get("")
async def i_social_proof2():
    return {"p":"psicologia_soci_social_proof2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_stereotype_threat.get("")
async def i_stereotype_threat():
    return {"p":"psicologia_soci_stereotype_threat","s":"ativo","t":datetime.utcnow().isoformat()}
@router_systemic.get("")
async def i_systemic():
    return {"p":"psicologia_soci_systemic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tokenism.get("")
async def i_tokenism():
    return {"p":"psicologia_soci_tokenism","s":"ativo","t":datetime.utcnow().isoformat()}
@router_transportation_theor.get("")
async def i_transportation_theor():
    return {"p":"psicologia_soci_transportation_theor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ultimate_attribution.get("")
async def i_ultimate_attribution():
    return {"p":"psicologia_soci_ultimate_attribution","s":"ativo","t":datetime.utcnow().isoformat()}
@router_unity_cialdini.get("")
async def i_unity_cialdini():
    return {"p":"psicologia_soci_unity_cialdini","s":"ativo","t":datetime.utcnow().isoformat()}
@router_vicarious_reinforcem.get("")
async def i_vicarious_reinforcem():
    return {"p":"psicologia_soci_vicarious_reinforcem","s":"ativo","t":datetime.utcnow().isoformat()}
@router_zajonc_arousal.get("")
async def i_zajonc_arousal():
    return {"p":"psicologia_soci_zajonc_arousal","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_psicologia_social_av(PluginBase):
    name = "consolidated_psicologia_social_avancada"
    def setup(self, app):
        app.include_router(router_actor_observer_bias)
        app.include_router(router_ambivalent_sexism)
        app.include_router(router_anchoring_bias)
        app.include_router(router_asch_experimento)
        app.include_router(router_atitude_formacao)
        app.include_router(router_atitude_mudanca)
        app.include_router(router_atratividade_fonte)
        app.include_router(router_attribution_theory)
        app.include_router(router_audience_effect)
        app.include_router(router_authority_influence)
        app.include_router(router_authority_principle)
        app.include_router(router_availability)
        app.include_router(router_backfire_effect)
        app.include_router(router_base_rate_fallacy)
        app.include_router(router_benevolent_sexism)
        app.include_router(router_bystander_effect)
        app.include_router(router_cautious_shift)
        app.include_router(router_central_peripheral_r)
        app.include_router(router_coaction_effect)
        app.include_router(router_cognitive_dissonance)
        app.include_router(router_collective_efficacy)
        app.include_router(router_colorblind_racism)
        app.include_router(router_commitment_consisten)
        app.include_router(router_confirmation_bias)
        app.include_router(router_conformidade_social)
        app.include_router(router_consistency_minority)
        app.include_router(router_contact_hypothesis)
        app.include_router(router_credibilidade_fonte)
        app.include_router(router_deindividuation)
        app.include_router(router_diffusion_responsibi)
        app.include_router(router_discrimination)
        app.include_router(router_dispositional_attrib)
        app.include_router(router_dual_process)
        app.include_router(router_dunning_kruger)
        app.include_router(router_elaboration_likeliho)
        app.include_router(router_external_attribution)
        app.include_router(router_fear_appeal)
        app.include_router(router_flexibility_minority)
        app.include_router(router_free_rider_problem)
        app.include_router(router_fundamental_attribut)
        app.include_router(router_genovese_syndrome)
        app.include_router(router_glass_ceiling2)
        app.include_router(router_group_polarization)
        app.include_router(router_groupthink)
        app.include_router(router_heuristic_systematic)
        app.include_router(router_hostile_sexism)
        app.include_router(router_humor_appeal)
        app.include_router(router_identification)
        app.include_router(router_illusory_superiority)
        app.include_router(router_implicit_association)
        app.include_router(router_informational)
        app.include_router(router_ingroup_outgroup)
        app.include_router(router_institutional_racism)
        app.include_router(router_intergroup_contact)
        app.include_router(router_internal_attribution)
        app.include_router(router_legitimacy)
        app.include_router(router_liking_principle2)
        app.include_router(router_media_influence2)
        app.include_router(router_mensagem_framing)
        app.include_router(router_microaggression2)
        app.include_router(router_milgram_experimento)
        app.include_router(router_minimal_group)
        app.include_router(router_minority_influence)
        app.include_router(router_modelagem_social)
        app.include_router(router_narrative_persuasion)
        app.include_router(router_normative_influence)
        app.include_router(router_obediencia_autoridad)
        app.include_router(router_observacional_learni)
        app.include_router(router_parasocial_relations)
        app.include_router(router_persuasao_social)
        app.include_router(router_prejudice_reduction)
        app.include_router(router_proxy_efficacy)
        app.include_router(router_racism_types)
        app.include_router(router_reactance)
        app.include_router(router_reciprocity_principl)
        app.include_router(router_representativeness)
        app.include_router(router_ringelmann_effect)
        app.include_router(router_risky_shift)
        app.include_router(router_scarcity_principle)
        app.include_router(router_self_categorization)
        app.include_router(router_self_efficacy_bandur)
        app.include_router(router_self_serving_bias)
        app.include_router(router_situational)
        app.include_router(router_snowball_minority)
        app.include_router(router_social_facilitation)
        app.include_router(router_social_identity_theo)
        app.include_router(router_social_learning_band)
        app.include_router(router_social_loafing)
        app.include_router(router_social_proof2)
        app.include_router(router_stereotype_threat)
        app.include_router(router_systemic)
        app.include_router(router_tokenism)
        app.include_router(router_transportation_theor)
        app.include_router(router_ultimate_attribution)
        app.include_router(router_unity_cialdini)
        app.include_router(router_vicarious_reinforcem)
        app.include_router(router_zajonc_arousal)


plugin = Plugin_psicologia_social_av()
