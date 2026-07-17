from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_active_inference2 = APIRouter(prefix="/api/v1/neurociencia/active_inference2", tags=["neurociencia_computacional"])
router_actor_critic = APIRouter(prefix="/api/v1/neurociencia/actor_critic", tags=["neurociencia_computacional"])
router_affordances_mental = APIRouter(prefix="/api/v1/neurociencia/affordances_mental", tags=["neurociencia_computacional"])
router_allostasis_computati = APIRouter(prefix="/api/v1/neurociencia/allostasis_computational", tags=["neurociencia_computacional"])
router_amygdala_model = APIRouter(prefix="/api/v1/neurociencia/amygdala_model", tags=["neurociencia_computacional"])
router_anti_hebbian = APIRouter(prefix="/api/v1/neurociencia/anti_hebbian", tags=["neurociencia_computacional"])
router_attractor_dynamics = APIRouter(prefix="/api/v1/neurociencia/attractor_dynamics", tags=["neurociencia_computacional"])
router_avalanche_neuro = APIRouter(prefix="/api/v1/neurociencia/avalanche_neuro", tags=["neurociencia_computacional"])
router_backpropagation = APIRouter(prefix="/api/v1/neurociencia/backpropagation", tags=["neurociencia_computacional"])
router_basal_ganglia_model = APIRouter(prefix="/api/v1/neurociencia/basal_ganglia_model", tags=["neurociencia_computacional"])
router_bayesian_brain2 = APIRouter(prefix="/api/v1/neurociencia/bayesian_brain2", tags=["neurociencia_computacional"])
router_bcm_rule = APIRouter(prefix="/api/v1/neurociencia/bcm_rule", tags=["neurociencia_computacional"])
router_belief_propagation = APIRouter(prefix="/api/v1/neurociencia/belief_propagation", tags=["neurociencia_computacional"])
router_bifurcation_neuro = APIRouter(prefix="/api/v1/neurociencia/bifurcation_neuro", tags=["neurociencia_computacional"])
router_bistability_neuro = APIRouter(prefix="/api/v1/neurociencia/bistability_neuro", tags=["neurociencia_computacional"])
router_boundary_cells = APIRouter(prefix="/api/v1/neurociencia/boundary_cells", tags=["neurociencia_computacional"])
router_cerebellar_model = APIRouter(prefix="/api/v1/neurociencia/cerebellar_model", tags=["neurociencia_computacional"])
router_cognitive_map = APIRouter(prefix="/api/v1/neurociencia/cognitive_map", tags=["neurociencia_computacional"])
router_criticality_neuro = APIRouter(prefix="/api/v1/neurociencia/criticality_neuro", tags=["neurociencia_computacional"])
router_cross_frequency2 = APIRouter(prefix="/api/v1/neurociencia/cross_frequency2", tags=["neurociencia_computacional"])
router_e_i_balance = APIRouter(prefix="/api/v1/neurociencia/e_i_balance", tags=["neurociencia_computacional"])
router_edge_criticality = APIRouter(prefix="/api/v1/neurociencia/edge_criticality", tags=["neurociencia_computacional"])
router_epistemic_value = APIRouter(prefix="/api/v1/neurociencia/epistemic_value", tags=["neurociencia_computacional"])
router_excitation_inhibitio = APIRouter(prefix="/api/v1/neurociencia/excitation_inhibition", tags=["neurociencia_computacional"])
router_free_energy2 = APIRouter(prefix="/api/v1/neurociencia/free_energy2", tags=["neurociencia_computacional"])
router_gamma_oscillation3 = APIRouter(prefix="/api/v1/neurociencia/gamma_oscillation3", tags=["neurociencia_computacional"])
router_gradient_descent = APIRouter(prefix="/api/v1/neurociencia/gradient_descent", tags=["neurociencia_computacional"])
router_grid_cells = APIRouter(prefix="/api/v1/neurociencia/grid_cells", tags=["neurociencia_computacional"])
router_head_direction = APIRouter(prefix="/api/v1/neurociencia/head_direction", tags=["neurociencia_computacional"])
router_hebbian_learning = APIRouter(prefix="/api/v1/neurociencia/hebbian_learning", tags=["neurociencia_computacional"])
router_hippocampal_model = APIRouter(prefix="/api/v1/neurociencia/hippocampal_model", tags=["neurociencia_computacional"])
router_homeostasis_computat = APIRouter(prefix="/api/v1/neurociencia/homeostasis_computational", tags=["neurociencia_computacional"])
router_interoception_comput = APIRouter(prefix="/api/v1/neurociencia/interoception_computation", tags=["neurociencia_computacional"])
router_long_range_correlati = APIRouter(prefix="/api/v1/neurociencia/long_range_correlation", tags=["neurociencia_computacional"])
router_markov_blanket = APIRouter(prefix="/api/v1/neurociencia/markov_blanket", tags=["neurociencia_computacional"])
router_mean_field = APIRouter(prefix="/api/v1/neurociencia/mean_field", tags=["neurociencia_computacional"])
router_metastability = APIRouter(prefix="/api/v1/neurociencia/metastability", tags=["neurociencia_computacional"])
router_model_based2 = APIRouter(prefix="/api/v1/neurociencia/model_based2", tags=["neurociencia_computacional"])
router_model_free2 = APIRouter(prefix="/api/v1/neurociencia/model_free2", tags=["neurociencia_computacional"])
router_modelo_computacional = APIRouter(prefix="/api/v1/neurociencia/modelo_computacional_neur", tags=["neurociencia_computacional"])
router_multistability = APIRouter(prefix="/api/v1/neurociencia/multistability", tags=["neurociencia_computacional"])
router_neocortex_model = APIRouter(prefix="/api/v1/neurociencia/neocortex_model", tags=["neurociencia_computacional"])
router_neural_network_bio = APIRouter(prefix="/api/v1/neurociencia/neural_network_bio", tags=["neurociencia_computacional"])
router_oja_rule = APIRouter(prefix="/api/v1/neurociencia/oja_rule", tags=["neurociencia_computacional"])
router_perceptron_neuro = APIRouter(prefix="/api/v1/neurociencia/perceptron_neuro", tags=["neurociencia_computacional"])
router_phase_precession = APIRouter(prefix="/api/v1/neurociencia/phase_precession", tags=["neurociencia_computacional"])
router_phase_transition_neu = APIRouter(prefix="/api/v1/neurociencia/phase_transition_neuro", tags=["neurociencia_computacional"])
router_place_cells = APIRouter(prefix="/api/v1/neurociencia/place_cells", tags=["neurociencia_computacional"])
router_policy_gradient = APIRouter(prefix="/api/v1/neurociencia/policy_gradient", tags=["neurociencia_computacional"])
router_population_coding = APIRouter(prefix="/api/v1/neurociencia/population_coding", tags=["neurociencia_computacional"])
router_power_law_neuro = APIRouter(prefix="/api/v1/neurociencia/power_law_neuro", tags=["neurociencia_computacional"])
router_pragmatic_value = APIRouter(prefix="/api/v1/neurociencia/pragmatic_value", tags=["neurociencia_computacional"])
router_predictive_coding2 = APIRouter(prefix="/api/v1/neurociencia/predictive_coding2", tags=["neurociencia_computacional"])
router_prefrontal_model = APIRouter(prefix="/api/v1/neurociencia/prefrontal_model", tags=["neurociencia_computacional"])
router_proprioception_compu = APIRouter(prefix="/api/v1/neurociencia/proprioception_computatio", tags=["neurociencia_computacional"])
router_q_learning = APIRouter(prefix="/api/v1/neurociencia/q_learning", tags=["neurociencia_computacional"])
router_rate_coding = APIRouter(prefix="/api/v1/neurociencia/rate_coding", tags=["neurociencia_computacional"])
router_regulation_computati = APIRouter(prefix="/api/v1/neurociencia/regulation_computational", tags=["neurociencia_computacional"])
router_reinforcement_neuro = APIRouter(prefix="/api/v1/neurociencia/reinforcement_neuro", tags=["neurociencia_computacional"])
router_self_evidencing = APIRouter(prefix="/api/v1/neurociencia/self_evidencing", tags=["neurociencia_computacional"])
router_self_organized_criti = APIRouter(prefix="/api/v1/neurociencia/self_organized_criticalit", tags=["neurociencia_computacional"])
router_sequence_replay = APIRouter(prefix="/api/v1/neurociencia/sequence_replay", tags=["neurociencia_computacional"])
router_sharp_wave_ripple = APIRouter(prefix="/api/v1/neurociencia/sharp_wave_ripple", tags=["neurociencia_computacional"])
router_spike_timing = APIRouter(prefix="/api/v1/neurociencia/spike_timing", tags=["neurociencia_computacional"])
router_spiking_neural = APIRouter(prefix="/api/v1/neurociencia/spiking_neural", tags=["neurociencia_computacional"])
router_stdp_learning = APIRouter(prefix="/api/v1/neurociencia/stdp_learning", tags=["neurociencia_computacional"])
router_striatal_model = APIRouter(prefix="/api/v1/neurociencia/striatal_model", tags=["neurociencia_computacional"])
router_successor_representa = APIRouter(prefix="/api/v1/neurociencia/successor_representation", tags=["neurociencia_computacional"])
router_synaptic_plasticity = APIRouter(prefix="/api/v1/neurociencia/synaptic_plasticity", tags=["neurociencia_computacional"])
router_temporal_difference2 = APIRouter(prefix="/api/v1/neurociencia/temporal_difference2", tags=["neurociencia_computacional"])
router_thalamic_model = APIRouter(prefix="/api/v1/neurociencia/thalamic_model", tags=["neurociencia_computacional"])
router_theta_oscillation2 = APIRouter(prefix="/api/v1/neurociencia/theta_oscillation2", tags=["neurociencia_computacional"])
router_theta_sequences = APIRouter(prefix="/api/v1/neurociencia/theta_sequences", tags=["neurociencia_computacional"])
router_time_cells = APIRouter(prefix="/api/v1/neurociencia/time_cells", tags=["neurociencia_computacional"])
router_variational_bayes = APIRouter(prefix="/api/v1/neurociencia/variational_bayes", tags=["neurociencia_computacional"])
router_working_memory_model = APIRouter(prefix="/api/v1/neurociencia/working_memory_model", tags=["neurociencia_computacional"])

@router_active_inference2.get("")
async def i_active_inference2():
    return {"p":"neurociencia_co_active_inference2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_actor_critic.get("")
async def i_actor_critic():
    return {"p":"neurociencia_co_actor_critic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_affordances_mental.get("")
async def i_affordances_mental():
    return {"p":"neurociencia_co_affordances_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_allostasis_computati.get("")
async def i_allostasis_computati():
    return {"p":"neurociencia_co_allostasis_computati","s":"ativo","t":datetime.utcnow().isoformat()}
@router_amygdala_model.get("")
async def i_amygdala_model():
    return {"p":"neurociencia_co_amygdala_model","s":"ativo","t":datetime.utcnow().isoformat()}
@router_anti_hebbian.get("")
async def i_anti_hebbian():
    return {"p":"neurociencia_co_anti_hebbian","s":"ativo","t":datetime.utcnow().isoformat()}
@router_attractor_dynamics.get("")
async def i_attractor_dynamics():
    return {"p":"neurociencia_co_attractor_dynamics","s":"ativo","t":datetime.utcnow().isoformat()}
@router_avalanche_neuro.get("")
async def i_avalanche_neuro():
    return {"p":"neurociencia_co_avalanche_neuro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_backpropagation.get("")
async def i_backpropagation():
    return {"p":"neurociencia_co_backpropagation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_basal_ganglia_model.get("")
async def i_basal_ganglia_model():
    return {"p":"neurociencia_co_basal_ganglia_model","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bayesian_brain2.get("")
async def i_bayesian_brain2():
    return {"p":"neurociencia_co_bayesian_brain2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bcm_rule.get("")
async def i_bcm_rule():
    return {"p":"neurociencia_co_bcm_rule","s":"ativo","t":datetime.utcnow().isoformat()}
@router_belief_propagation.get("")
async def i_belief_propagation():
    return {"p":"neurociencia_co_belief_propagation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bifurcation_neuro.get("")
async def i_bifurcation_neuro():
    return {"p":"neurociencia_co_bifurcation_neuro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bistability_neuro.get("")
async def i_bistability_neuro():
    return {"p":"neurociencia_co_bistability_neuro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_boundary_cells.get("")
async def i_boundary_cells():
    return {"p":"neurociencia_co_boundary_cells","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cerebellar_model.get("")
async def i_cerebellar_model():
    return {"p":"neurociencia_co_cerebellar_model","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cognitive_map.get("")
async def i_cognitive_map():
    return {"p":"neurociencia_co_cognitive_map","s":"ativo","t":datetime.utcnow().isoformat()}
@router_criticality_neuro.get("")
async def i_criticality_neuro():
    return {"p":"neurociencia_co_criticality_neuro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cross_frequency2.get("")
async def i_cross_frequency2():
    return {"p":"neurociencia_co_cross_frequency2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_e_i_balance.get("")
async def i_e_i_balance():
    return {"p":"neurociencia_co_e_i_balance","s":"ativo","t":datetime.utcnow().isoformat()}
@router_edge_criticality.get("")
async def i_edge_criticality():
    return {"p":"neurociencia_co_edge_criticality","s":"ativo","t":datetime.utcnow().isoformat()}
@router_epistemic_value.get("")
async def i_epistemic_value():
    return {"p":"neurociencia_co_epistemic_value","s":"ativo","t":datetime.utcnow().isoformat()}
@router_excitation_inhibitio.get("")
async def i_excitation_inhibitio():
    return {"p":"neurociencia_co_excitation_inhibitio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_free_energy2.get("")
async def i_free_energy2():
    return {"p":"neurociencia_co_free_energy2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gamma_oscillation3.get("")
async def i_gamma_oscillation3():
    return {"p":"neurociencia_co_gamma_oscillation3","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gradient_descent.get("")
async def i_gradient_descent():
    return {"p":"neurociencia_co_gradient_descent","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grid_cells.get("")
async def i_grid_cells():
    return {"p":"neurociencia_co_grid_cells","s":"ativo","t":datetime.utcnow().isoformat()}
@router_head_direction.get("")
async def i_head_direction():
    return {"p":"neurociencia_co_head_direction","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hebbian_learning.get("")
async def i_hebbian_learning():
    return {"p":"neurociencia_co_hebbian_learning","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hippocampal_model.get("")
async def i_hippocampal_model():
    return {"p":"neurociencia_co_hippocampal_model","s":"ativo","t":datetime.utcnow().isoformat()}
@router_homeostasis_computat.get("")
async def i_homeostasis_computat():
    return {"p":"neurociencia_co_homeostasis_computat","s":"ativo","t":datetime.utcnow().isoformat()}
@router_interoception_comput.get("")
async def i_interoception_comput():
    return {"p":"neurociencia_co_interoception_comput","s":"ativo","t":datetime.utcnow().isoformat()}
@router_long_range_correlati.get("")
async def i_long_range_correlati():
    return {"p":"neurociencia_co_long_range_correlati","s":"ativo","t":datetime.utcnow().isoformat()}
@router_markov_blanket.get("")
async def i_markov_blanket():
    return {"p":"neurociencia_co_markov_blanket","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mean_field.get("")
async def i_mean_field():
    return {"p":"neurociencia_co_mean_field","s":"ativo","t":datetime.utcnow().isoformat()}
@router_metastability.get("")
async def i_metastability():
    return {"p":"neurociencia_co_metastability","s":"ativo","t":datetime.utcnow().isoformat()}
@router_model_based2.get("")
async def i_model_based2():
    return {"p":"neurociencia_co_model_based2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_model_free2.get("")
async def i_model_free2():
    return {"p":"neurociencia_co_model_free2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_modelo_computacional.get("")
async def i_modelo_computacional():
    return {"p":"neurociencia_co_modelo_computacional","s":"ativo","t":datetime.utcnow().isoformat()}
@router_multistability.get("")
async def i_multistability():
    return {"p":"neurociencia_co_multistability","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neocortex_model.get("")
async def i_neocortex_model():
    return {"p":"neurociencia_co_neocortex_model","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neural_network_bio.get("")
async def i_neural_network_bio():
    return {"p":"neurociencia_co_neural_network_bio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_oja_rule.get("")
async def i_oja_rule():
    return {"p":"neurociencia_co_oja_rule","s":"ativo","t":datetime.utcnow().isoformat()}
@router_perceptron_neuro.get("")
async def i_perceptron_neuro():
    return {"p":"neurociencia_co_perceptron_neuro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_phase_precession.get("")
async def i_phase_precession():
    return {"p":"neurociencia_co_phase_precession","s":"ativo","t":datetime.utcnow().isoformat()}
@router_phase_transition_neu.get("")
async def i_phase_transition_neu():
    return {"p":"neurociencia_co_phase_transition_neu","s":"ativo","t":datetime.utcnow().isoformat()}
@router_place_cells.get("")
async def i_place_cells():
    return {"p":"neurociencia_co_place_cells","s":"ativo","t":datetime.utcnow().isoformat()}
@router_policy_gradient.get("")
async def i_policy_gradient():
    return {"p":"neurociencia_co_policy_gradient","s":"ativo","t":datetime.utcnow().isoformat()}
@router_population_coding.get("")
async def i_population_coding():
    return {"p":"neurociencia_co_population_coding","s":"ativo","t":datetime.utcnow().isoformat()}
@router_power_law_neuro.get("")
async def i_power_law_neuro():
    return {"p":"neurociencia_co_power_law_neuro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pragmatic_value.get("")
async def i_pragmatic_value():
    return {"p":"neurociencia_co_pragmatic_value","s":"ativo","t":datetime.utcnow().isoformat()}
@router_predictive_coding2.get("")
async def i_predictive_coding2():
    return {"p":"neurociencia_co_predictive_coding2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_prefrontal_model.get("")
async def i_prefrontal_model():
    return {"p":"neurociencia_co_prefrontal_model","s":"ativo","t":datetime.utcnow().isoformat()}
@router_proprioception_compu.get("")
async def i_proprioception_compu():
    return {"p":"neurociencia_co_proprioception_compu","s":"ativo","t":datetime.utcnow().isoformat()}
@router_q_learning.get("")
async def i_q_learning():
    return {"p":"neurociencia_co_q_learning","s":"ativo","t":datetime.utcnow().isoformat()}
@router_rate_coding.get("")
async def i_rate_coding():
    return {"p":"neurociencia_co_rate_coding","s":"ativo","t":datetime.utcnow().isoformat()}
@router_regulation_computati.get("")
async def i_regulation_computati():
    return {"p":"neurociencia_co_regulation_computati","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reinforcement_neuro.get("")
async def i_reinforcement_neuro():
    return {"p":"neurociencia_co_reinforcement_neuro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_self_evidencing.get("")
async def i_self_evidencing():
    return {"p":"neurociencia_co_self_evidencing","s":"ativo","t":datetime.utcnow().isoformat()}
@router_self_organized_criti.get("")
async def i_self_organized_criti():
    return {"p":"neurociencia_co_self_organized_criti","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sequence_replay.get("")
async def i_sequence_replay():
    return {"p":"neurociencia_co_sequence_replay","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sharp_wave_ripple.get("")
async def i_sharp_wave_ripple():
    return {"p":"neurociencia_co_sharp_wave_ripple","s":"ativo","t":datetime.utcnow().isoformat()}
@router_spike_timing.get("")
async def i_spike_timing():
    return {"p":"neurociencia_co_spike_timing","s":"ativo","t":datetime.utcnow().isoformat()}
@router_spiking_neural.get("")
async def i_spiking_neural():
    return {"p":"neurociencia_co_spiking_neural","s":"ativo","t":datetime.utcnow().isoformat()}
@router_stdp_learning.get("")
async def i_stdp_learning():
    return {"p":"neurociencia_co_stdp_learning","s":"ativo","t":datetime.utcnow().isoformat()}
@router_striatal_model.get("")
async def i_striatal_model():
    return {"p":"neurociencia_co_striatal_model","s":"ativo","t":datetime.utcnow().isoformat()}
@router_successor_representa.get("")
async def i_successor_representa():
    return {"p":"neurociencia_co_successor_representa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_synaptic_plasticity.get("")
async def i_synaptic_plasticity():
    return {"p":"neurociencia_co_synaptic_plasticity","s":"ativo","t":datetime.utcnow().isoformat()}
@router_temporal_difference2.get("")
async def i_temporal_difference2():
    return {"p":"neurociencia_co_temporal_difference2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_thalamic_model.get("")
async def i_thalamic_model():
    return {"p":"neurociencia_co_thalamic_model","s":"ativo","t":datetime.utcnow().isoformat()}
@router_theta_oscillation2.get("")
async def i_theta_oscillation2():
    return {"p":"neurociencia_co_theta_oscillation2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_theta_sequences.get("")
async def i_theta_sequences():
    return {"p":"neurociencia_co_theta_sequences","s":"ativo","t":datetime.utcnow().isoformat()}
@router_time_cells.get("")
async def i_time_cells():
    return {"p":"neurociencia_co_time_cells","s":"ativo","t":datetime.utcnow().isoformat()}
@router_variational_bayes.get("")
async def i_variational_bayes():
    return {"p":"neurociencia_co_variational_bayes","s":"ativo","t":datetime.utcnow().isoformat()}
@router_working_memory_model.get("")
async def i_working_memory_model():
    return {"p":"neurociencia_co_working_memory_model","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_neurociencia_computa(PluginBase):
    name = "consolidated_neurociencia_computacional"
    def setup(self, app):
        app.include_router(router_active_inference2)
        app.include_router(router_actor_critic)
        app.include_router(router_affordances_mental)
        app.include_router(router_allostasis_computati)
        app.include_router(router_amygdala_model)
        app.include_router(router_anti_hebbian)
        app.include_router(router_attractor_dynamics)
        app.include_router(router_avalanche_neuro)
        app.include_router(router_backpropagation)
        app.include_router(router_basal_ganglia_model)
        app.include_router(router_bayesian_brain2)
        app.include_router(router_bcm_rule)
        app.include_router(router_belief_propagation)
        app.include_router(router_bifurcation_neuro)
        app.include_router(router_bistability_neuro)
        app.include_router(router_boundary_cells)
        app.include_router(router_cerebellar_model)
        app.include_router(router_cognitive_map)
        app.include_router(router_criticality_neuro)
        app.include_router(router_cross_frequency2)
        app.include_router(router_e_i_balance)
        app.include_router(router_edge_criticality)
        app.include_router(router_epistemic_value)
        app.include_router(router_excitation_inhibitio)
        app.include_router(router_free_energy2)
        app.include_router(router_gamma_oscillation3)
        app.include_router(router_gradient_descent)
        app.include_router(router_grid_cells)
        app.include_router(router_head_direction)
        app.include_router(router_hebbian_learning)
        app.include_router(router_hippocampal_model)
        app.include_router(router_homeostasis_computat)
        app.include_router(router_interoception_comput)
        app.include_router(router_long_range_correlati)
        app.include_router(router_markov_blanket)
        app.include_router(router_mean_field)
        app.include_router(router_metastability)
        app.include_router(router_model_based2)
        app.include_router(router_model_free2)
        app.include_router(router_modelo_computacional)
        app.include_router(router_multistability)
        app.include_router(router_neocortex_model)
        app.include_router(router_neural_network_bio)
        app.include_router(router_oja_rule)
        app.include_router(router_perceptron_neuro)
        app.include_router(router_phase_precession)
        app.include_router(router_phase_transition_neu)
        app.include_router(router_place_cells)
        app.include_router(router_policy_gradient)
        app.include_router(router_population_coding)
        app.include_router(router_power_law_neuro)
        app.include_router(router_pragmatic_value)
        app.include_router(router_predictive_coding2)
        app.include_router(router_prefrontal_model)
        app.include_router(router_proprioception_compu)
        app.include_router(router_q_learning)
        app.include_router(router_rate_coding)
        app.include_router(router_regulation_computati)
        app.include_router(router_reinforcement_neuro)
        app.include_router(router_self_evidencing)
        app.include_router(router_self_organized_criti)
        app.include_router(router_sequence_replay)
        app.include_router(router_sharp_wave_ripple)
        app.include_router(router_spike_timing)
        app.include_router(router_spiking_neural)
        app.include_router(router_stdp_learning)
        app.include_router(router_striatal_model)
        app.include_router(router_successor_representa)
        app.include_router(router_synaptic_plasticity)
        app.include_router(router_temporal_difference2)
        app.include_router(router_thalamic_model)
        app.include_router(router_theta_oscillation2)
        app.include_router(router_theta_sequences)
        app.include_router(router_time_cells)
        app.include_router(router_variational_bayes)
        app.include_router(router_working_memory_model)


plugin = Plugin_neurociencia_computa()
