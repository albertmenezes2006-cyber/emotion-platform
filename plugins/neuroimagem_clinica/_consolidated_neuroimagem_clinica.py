from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_active_inference = APIRouter(prefix="/api/v1/neuroimagem_/active_inference", tags=["neuroimagem_clinica"])
router_allostasis_model = APIRouter(prefix="/api/v1/neuroimagem_/allostasis_model", tags=["neuroimagem_clinica"])
router_alpha_oscillation = APIRouter(prefix="/api/v1/neuroimagem_/alpha_oscillation", tags=["neuroimagem_clinica"])
router_alpha_theta_coupling = APIRouter(prefix="/api/v1/neuroimagem_/alpha_theta_coupling", tags=["neuroimagem_clinica"])
router_amyloid_pet = APIRouter(prefix="/api/v1/neuroimagem_/amyloid_pet", tags=["neuroimagem_clinica"])
router_bayesian_brain = APIRouter(prefix="/api/v1/neuroimagem_/bayesian_brain", tags=["neuroimagem_clinica"])
router_beta_oscillation2 = APIRouter(prefix="/api/v1/neuroimagem_/beta_oscillation2", tags=["neuroimagem_clinica"])
router_central_executive = APIRouter(prefix="/api/v1/neuroimagem_/central_executive", tags=["neuroimagem_clinica"])
router_cerebellar_network = APIRouter(prefix="/api/v1/neuroimagem_/cerebellar_network", tags=["neuroimagem_clinica"])
router_choline_spectroscopy = APIRouter(prefix="/api/v1/neuroimagem_/choline_spectroscopy", tags=["neuroimagem_clinica"])
router_clustering_coefficie = APIRouter(prefix="/api/v1/neuroimagem_/clustering_coefficient", tags=["neuroimagem_clinica"])
router_cnv = APIRouter(prefix="/api/v1/neuroimagem_/cnv", tags=["neuroimagem_clinica"])
router_computational_psychi = APIRouter(prefix="/api/v1/neuroimagem_/computational_psychiatry3", tags=["neuroimagem_clinica"])
router_contingent_negative_ = APIRouter(prefix="/api/v1/neuroimagem_/contingent_negative_varia", tags=["neuroimagem_clinica"])
router_cortical_thickness_m = APIRouter(prefix="/api/v1/neuroimagem_/cortical_thickness_mri", tags=["neuroimagem_clinica"])
router_creatine_spectroscop = APIRouter(prefix="/api/v1/neuroimagem_/creatine_spectroscopy", tags=["neuroimagem_clinica"])
router_cross_frequency_coup = APIRouter(prefix="/api/v1/neuroimagem_/cross_frequency_coupling", tags=["neuroimagem_clinica"])
router_default_mode_network = APIRouter(prefix="/api/v1/neuroimagem_/default_mode_network", tags=["neuroimagem_clinica"])
router_delta_oscillation2 = APIRouter(prefix="/api/v1/neuroimagem_/delta_oscillation2", tags=["neuroimagem_clinica"])
router_dics_beamformer = APIRouter(prefix="/api/v1/neuroimagem_/dics_beamformer", tags=["neuroimagem_clinica"])
router_dopamine_pet = APIRouter(prefix="/api/v1/neuroimagem_/dopamine_pet", tags=["neuroimagem_clinica"])
router_dopamine_transporter = APIRouter(prefix="/api/v1/neuroimagem_/dopamine_transporter", tags=["neuroimagem_clinica"])
router_dorsal_attention_net = APIRouter(prefix="/api/v1/neuroimagem_/dorsal_attention_network", tags=["neuroimagem_clinica"])
router_dti_tractography = APIRouter(prefix="/api/v1/neuroimagem_/dti_tractography", tags=["neuroimagem_clinica"])
router_eeg_clinical2 = APIRouter(prefix="/api/v1/neuroimagem_/eeg_clinical2", tags=["neuroimagem_clinica"])
router_erp_clinical = APIRouter(prefix="/api/v1/neuroimagem_/erp_clinical", tags=["neuroimagem_clinica"])
router_error_related_negati = APIRouter(prefix="/api/v1/neuroimagem_/error_related_negativity", tags=["neuroimagem_clinica"])
router_fdg_pet = APIRouter(prefix="/api/v1/neuroimagem_/fdg_pet", tags=["neuroimagem_clinica"])
router_feedback_related_neg = APIRouter(prefix="/api/v1/neuroimagem_/feedback_related_negativi", tags=["neuroimagem_clinica"])
router_fmri_clinical = APIRouter(prefix="/api/v1/neuroimagem_/fmri_clinical", tags=["neuroimagem_clinica"])
router_free_energy_principl = APIRouter(prefix="/api/v1/neuroimagem_/free_energy_principle", tags=["neuroimagem_clinica"])
router_frontal_asymmetry = APIRouter(prefix="/api/v1/neuroimagem_/frontal_asymmetry", tags=["neuroimagem_clinica"])
router_frontoparietal = APIRouter(prefix="/api/v1/neuroimagem_/frontoparietal", tags=["neuroimagem_clinica"])
router_functional_connectiv = APIRouter(prefix="/api/v1/neuroimagem_/functional_connectivity", tags=["neuroimagem_clinica"])
router_gaba_spectroscopy = APIRouter(prefix="/api/v1/neuroimagem_/gaba_spectroscopy", tags=["neuroimagem_clinica"])
router_gamma_oscillation2 = APIRouter(prefix="/api/v1/neuroimagem_/gamma_oscillation2", tags=["neuroimagem_clinica"])
router_generative_models = APIRouter(prefix="/api/v1/neuroimagem_/generative_models", tags=["neuroimagem_clinica"])
router_global_efficiency = APIRouter(prefix="/api/v1/neuroimagem_/global_efficiency", tags=["neuroimagem_clinica"])
router_glutamate_spectrosco = APIRouter(prefix="/api/v1/neuroimagem_/glutamate_spectroscopy", tags=["neuroimagem_clinica"])
router_graph_theory_brain = APIRouter(prefix="/api/v1/neuroimagem_/graph_theory_brain", tags=["neuroimagem_clinica"])
router_hierarchical_inferen = APIRouter(prefix="/api/v1/neuroimagem_/hierarchical_inference", tags=["neuroimagem_clinica"])
router_hub_nodes = APIRouter(prefix="/api/v1/neuroimagem_/hub_nodes", tags=["neuroimagem_clinica"])
router_ica_meg = APIRouter(prefix="/api/v1/neuroimagem_/ica_meg", tags=["neuroimagem_clinica"])
router_infra_slow_oscillati = APIRouter(prefix="/api/v1/neuroimagem_/infra_slow_oscillation", tags=["neuroimagem_clinica"])
router_interoceptive_predic = APIRouter(prefix="/api/v1/neuroimagem_/interoceptive_predictive", tags=["neuroimagem_clinica"])
router_lactate_spectroscopy = APIRouter(prefix="/api/v1/neuroimagem_/lactate_spectroscopy", tags=["neuroimagem_clinica"])
router_lateralized_readines = APIRouter(prefix="/api/v1/neuroimagem_/lateralized_readiness", tags=["neuroimagem_clinica"])
router_lcmv_beamforming = APIRouter(prefix="/api/v1/neuroimagem_/lcmv_beamforming", tags=["neuroimagem_clinica"])
router_limbic_network = APIRouter(prefix="/api/v1/neuroimagem_/limbic_network", tags=["neuroimagem_clinica"])
router_local_efficiency = APIRouter(prefix="/api/v1/neuroimagem_/local_efficiency", tags=["neuroimagem_clinica"])
router_meg_clinical2 = APIRouter(prefix="/api/v1/neuroimagem_/meg_clinical2", tags=["neuroimagem_clinica"])
router_mismatch_negativity = APIRouter(prefix="/api/v1/neuroimagem_/mismatch_negativity", tags=["neuroimagem_clinica"])
router_model_based_rl = APIRouter(prefix="/api/v1/neuroimagem_/model_based_rl", tags=["neuroimagem_clinica"])
router_model_free_rl = APIRouter(prefix="/api/v1/neuroimagem_/model_free_rl", tags=["neuroimagem_clinica"])
router_modularity = APIRouter(prefix="/api/v1/neuroimagem_/modularity", tags=["neuroimagem_clinica"])
router_motor_network = APIRouter(prefix="/api/v1/neuroimagem_/motor_network", tags=["neuroimagem_clinica"])
router_mri_spectroscopy = APIRouter(prefix="/api/v1/neuroimagem_/mri_spectroscopy", tags=["neuroimagem_clinica"])
router_myoinositol_spectros = APIRouter(prefix="/api/v1/neuroimagem_/myoinositol_spectroscopy", tags=["neuroimagem_clinica"])
router_n200_clinical = APIRouter(prefix="/api/v1/neuroimagem_/n200_clinical", tags=["neuroimagem_clinica"])
router_n400_clinical = APIRouter(prefix="/api/v1/neuroimagem_/n400_clinical", tags=["neuroimagem_clinica"])
router_naa_spectroscopy = APIRouter(prefix="/api/v1/neuroimagem_/naa_spectroscopy", tags=["neuroimagem_clinica"])
router_neuroinflammation_pe = APIRouter(prefix="/api/v1/neuroimagem_/neuroinflammation_pet", tags=["neuroimagem_clinica"])
router_p300_clinical = APIRouter(prefix="/api/v1/neuroimagem_/p300_clinical", tags=["neuroimagem_clinica"])
router_p600_clinical = APIRouter(prefix="/api/v1/neuroimagem_/p600_clinical", tags=["neuroimagem_clinica"])
router_path_length = APIRouter(prefix="/api/v1/neuroimagem_/path_length", tags=["neuroimagem_clinica"])
router_perfusion_spect = APIRouter(prefix="/api/v1/neuroimagem_/perfusion_spect", tags=["neuroimagem_clinica"])
router_pet_clinical = APIRouter(prefix="/api/v1/neuroimagem_/pet_clinical", tags=["neuroimagem_clinica"])
router_phase_amplitude_coup = APIRouter(prefix="/api/v1/neuroimagem_/phase_amplitude_coupling", tags=["neuroimagem_clinica"])
router_precision_weighting = APIRouter(prefix="/api/v1/neuroimagem_/precision_weighting", tags=["neuroimagem_clinica"])
router_predictive_coding = APIRouter(prefix="/api/v1/neuroimagem_/predictive_coding", tags=["neuroimagem_clinica"])
router_reinforcement_learni = APIRouter(prefix="/api/v1/neuroimagem_/reinforcement_learning_ne", tags=["neuroimagem_clinica"])
router_resting_state_fmri = APIRouter(prefix="/api/v1/neuroimagem_/resting_state_fmri", tags=["neuroimagem_clinica"])
router_reward_positivity = APIRouter(prefix="/api/v1/neuroimagem_/reward_positivity", tags=["neuroimagem_clinica"])
router_reward_prediction_er = APIRouter(prefix="/api/v1/neuroimagem_/reward_prediction_error", tags=["neuroimagem_clinica"])
router_rich_club = APIRouter(prefix="/api/v1/neuroimagem_/rich_club", tags=["neuroimagem_clinica"])
router_salience_network = APIRouter(prefix="/api/v1/neuroimagem_/salience_network", tags=["neuroimagem_clinica"])
router_serotonin_pet = APIRouter(prefix="/api/v1/neuroimagem_/serotonin_pet", tags=["neuroimagem_clinica"])
router_small_world_network = APIRouter(prefix="/api/v1/neuroimagem_/small_world_network", tags=["neuroimagem_clinica"])
router_social_bayesian = APIRouter(prefix="/api/v1/neuroimagem_/social_bayesian", tags=["neuroimagem_clinica"])
router_spect_clinical = APIRouter(prefix="/api/v1/neuroimagem_/spect_clinical", tags=["neuroimagem_clinica"])
router_ssp_meg = APIRouter(prefix="/api/v1/neuroimagem_/ssp_meg", tags=["neuroimagem_clinica"])
router_structural_mri = APIRouter(prefix="/api/v1/neuroimagem_/structural_mri", tags=["neuroimagem_clinica"])
router_subcortical_network = APIRouter(prefix="/api/v1/neuroimagem_/subcortical_network", tags=["neuroimagem_clinica"])
router_surface_based_morpho = APIRouter(prefix="/api/v1/neuroimagem_/surface_based_morphometry", tags=["neuroimagem_clinica"])
router_tau_pet = APIRouter(prefix="/api/v1/neuroimagem_/tau_pet", tags=["neuroimagem_clinica"])
router_temporal_difference = APIRouter(prefix="/api/v1/neuroimagem_/temporal_difference", tags=["neuroimagem_clinica"])
router_thalamic_network = APIRouter(prefix="/api/v1/neuroimagem_/thalamic_network", tags=["neuroimagem_clinica"])
router_theta_gamma_coupling = APIRouter(prefix="/api/v1/neuroimagem_/theta_gamma_coupling", tags=["neuroimagem_clinica"])
router_theta_oscillation = APIRouter(prefix="/api/v1/neuroimagem_/theta_oscillation", tags=["neuroimagem_clinica"])
router_ventral_attention = APIRouter(prefix="/api/v1/neuroimagem_/ventral_attention", tags=["neuroimagem_clinica"])
router_visual_network = APIRouter(prefix="/api/v1/neuroimagem_/visual_network", tags=["neuroimagem_clinica"])
router_volumetric_mri = APIRouter(prefix="/api/v1/neuroimagem_/volumetric_mri", tags=["neuroimagem_clinica"])
router_voxel_based_morphome = APIRouter(prefix="/api/v1/neuroimagem_/voxel_based_morphometry", tags=["neuroimagem_clinica"])
router_white_matter_mri = APIRouter(prefix="/api/v1/neuroimagem_/white_matter_mri", tags=["neuroimagem_clinica"])

@router_active_inference.get("")
async def i_active_inference():
    return {"p":"neuroimagem_cli_active_inference","s":"ativo","t":datetime.utcnow().isoformat()}
@router_allostasis_model.get("")
async def i_allostasis_model():
    return {"p":"neuroimagem_cli_allostasis_model","s":"ativo","t":datetime.utcnow().isoformat()}
@router_alpha_oscillation.get("")
async def i_alpha_oscillation():
    return {"p":"neuroimagem_cli_alpha_oscillation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_alpha_theta_coupling.get("")
async def i_alpha_theta_coupling():
    return {"p":"neuroimagem_cli_alpha_theta_coupling","s":"ativo","t":datetime.utcnow().isoformat()}
@router_amyloid_pet.get("")
async def i_amyloid_pet():
    return {"p":"neuroimagem_cli_amyloid_pet","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bayesian_brain.get("")
async def i_bayesian_brain():
    return {"p":"neuroimagem_cli_bayesian_brain","s":"ativo","t":datetime.utcnow().isoformat()}
@router_beta_oscillation2.get("")
async def i_beta_oscillation2():
    return {"p":"neuroimagem_cli_beta_oscillation2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_central_executive.get("")
async def i_central_executive():
    return {"p":"neuroimagem_cli_central_executive","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cerebellar_network.get("")
async def i_cerebellar_network():
    return {"p":"neuroimagem_cli_cerebellar_network","s":"ativo","t":datetime.utcnow().isoformat()}
@router_choline_spectroscopy.get("")
async def i_choline_spectroscopy():
    return {"p":"neuroimagem_cli_choline_spectroscopy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_clustering_coefficie.get("")
async def i_clustering_coefficie():
    return {"p":"neuroimagem_cli_clustering_coefficie","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cnv.get("")
async def i_cnv():
    return {"p":"neuroimagem_cli_cnv","s":"ativo","t":datetime.utcnow().isoformat()}
@router_computational_psychi.get("")
async def i_computational_psychi():
    return {"p":"neuroimagem_cli_computational_psychi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_contingent_negative_.get("")
async def i_contingent_negative_():
    return {"p":"neuroimagem_cli_contingent_negative_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cortical_thickness_m.get("")
async def i_cortical_thickness_m():
    return {"p":"neuroimagem_cli_cortical_thickness_m","s":"ativo","t":datetime.utcnow().isoformat()}
@router_creatine_spectroscop.get("")
async def i_creatine_spectroscop():
    return {"p":"neuroimagem_cli_creatine_spectroscop","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cross_frequency_coup.get("")
async def i_cross_frequency_coup():
    return {"p":"neuroimagem_cli_cross_frequency_coup","s":"ativo","t":datetime.utcnow().isoformat()}
@router_default_mode_network.get("")
async def i_default_mode_network():
    return {"p":"neuroimagem_cli_default_mode_network","s":"ativo","t":datetime.utcnow().isoformat()}
@router_delta_oscillation2.get("")
async def i_delta_oscillation2():
    return {"p":"neuroimagem_cli_delta_oscillation2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dics_beamformer.get("")
async def i_dics_beamformer():
    return {"p":"neuroimagem_cli_dics_beamformer","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dopamine_pet.get("")
async def i_dopamine_pet():
    return {"p":"neuroimagem_cli_dopamine_pet","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dopamine_transporter.get("")
async def i_dopamine_transporter():
    return {"p":"neuroimagem_cli_dopamine_transporter","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dorsal_attention_net.get("")
async def i_dorsal_attention_net():
    return {"p":"neuroimagem_cli_dorsal_attention_net","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dti_tractography.get("")
async def i_dti_tractography():
    return {"p":"neuroimagem_cli_dti_tractography","s":"ativo","t":datetime.utcnow().isoformat()}
@router_eeg_clinical2.get("")
async def i_eeg_clinical2():
    return {"p":"neuroimagem_cli_eeg_clinical2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_erp_clinical.get("")
async def i_erp_clinical():
    return {"p":"neuroimagem_cli_erp_clinical","s":"ativo","t":datetime.utcnow().isoformat()}
@router_error_related_negati.get("")
async def i_error_related_negati():
    return {"p":"neuroimagem_cli_error_related_negati","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fdg_pet.get("")
async def i_fdg_pet():
    return {"p":"neuroimagem_cli_fdg_pet","s":"ativo","t":datetime.utcnow().isoformat()}
@router_feedback_related_neg.get("")
async def i_feedback_related_neg():
    return {"p":"neuroimagem_cli_feedback_related_neg","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fmri_clinical.get("")
async def i_fmri_clinical():
    return {"p":"neuroimagem_cli_fmri_clinical","s":"ativo","t":datetime.utcnow().isoformat()}
@router_free_energy_principl.get("")
async def i_free_energy_principl():
    return {"p":"neuroimagem_cli_free_energy_principl","s":"ativo","t":datetime.utcnow().isoformat()}
@router_frontal_asymmetry.get("")
async def i_frontal_asymmetry():
    return {"p":"neuroimagem_cli_frontal_asymmetry","s":"ativo","t":datetime.utcnow().isoformat()}
@router_frontoparietal.get("")
async def i_frontoparietal():
    return {"p":"neuroimagem_cli_frontoparietal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_functional_connectiv.get("")
async def i_functional_connectiv():
    return {"p":"neuroimagem_cli_functional_connectiv","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gaba_spectroscopy.get("")
async def i_gaba_spectroscopy():
    return {"p":"neuroimagem_cli_gaba_spectroscopy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gamma_oscillation2.get("")
async def i_gamma_oscillation2():
    return {"p":"neuroimagem_cli_gamma_oscillation2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_generative_models.get("")
async def i_generative_models():
    return {"p":"neuroimagem_cli_generative_models","s":"ativo","t":datetime.utcnow().isoformat()}
@router_global_efficiency.get("")
async def i_global_efficiency():
    return {"p":"neuroimagem_cli_global_efficiency","s":"ativo","t":datetime.utcnow().isoformat()}
@router_glutamate_spectrosco.get("")
async def i_glutamate_spectrosco():
    return {"p":"neuroimagem_cli_glutamate_spectrosco","s":"ativo","t":datetime.utcnow().isoformat()}
@router_graph_theory_brain.get("")
async def i_graph_theory_brain():
    return {"p":"neuroimagem_cli_graph_theory_brain","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hierarchical_inferen.get("")
async def i_hierarchical_inferen():
    return {"p":"neuroimagem_cli_hierarchical_inferen","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hub_nodes.get("")
async def i_hub_nodes():
    return {"p":"neuroimagem_cli_hub_nodes","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ica_meg.get("")
async def i_ica_meg():
    return {"p":"neuroimagem_cli_ica_meg","s":"ativo","t":datetime.utcnow().isoformat()}
@router_infra_slow_oscillati.get("")
async def i_infra_slow_oscillati():
    return {"p":"neuroimagem_cli_infra_slow_oscillati","s":"ativo","t":datetime.utcnow().isoformat()}
@router_interoceptive_predic.get("")
async def i_interoceptive_predic():
    return {"p":"neuroimagem_cli_interoceptive_predic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lactate_spectroscopy.get("")
async def i_lactate_spectroscopy():
    return {"p":"neuroimagem_cli_lactate_spectroscopy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lateralized_readines.get("")
async def i_lateralized_readines():
    return {"p":"neuroimagem_cli_lateralized_readines","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lcmv_beamforming.get("")
async def i_lcmv_beamforming():
    return {"p":"neuroimagem_cli_lcmv_beamforming","s":"ativo","t":datetime.utcnow().isoformat()}
@router_limbic_network.get("")
async def i_limbic_network():
    return {"p":"neuroimagem_cli_limbic_network","s":"ativo","t":datetime.utcnow().isoformat()}
@router_local_efficiency.get("")
async def i_local_efficiency():
    return {"p":"neuroimagem_cli_local_efficiency","s":"ativo","t":datetime.utcnow().isoformat()}
@router_meg_clinical2.get("")
async def i_meg_clinical2():
    return {"p":"neuroimagem_cli_meg_clinical2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mismatch_negativity.get("")
async def i_mismatch_negativity():
    return {"p":"neuroimagem_cli_mismatch_negativity","s":"ativo","t":datetime.utcnow().isoformat()}
@router_model_based_rl.get("")
async def i_model_based_rl():
    return {"p":"neuroimagem_cli_model_based_rl","s":"ativo","t":datetime.utcnow().isoformat()}
@router_model_free_rl.get("")
async def i_model_free_rl():
    return {"p":"neuroimagem_cli_model_free_rl","s":"ativo","t":datetime.utcnow().isoformat()}
@router_modularity.get("")
async def i_modularity():
    return {"p":"neuroimagem_cli_modularity","s":"ativo","t":datetime.utcnow().isoformat()}
@router_motor_network.get("")
async def i_motor_network():
    return {"p":"neuroimagem_cli_motor_network","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mri_spectroscopy.get("")
async def i_mri_spectroscopy():
    return {"p":"neuroimagem_cli_mri_spectroscopy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_myoinositol_spectros.get("")
async def i_myoinositol_spectros():
    return {"p":"neuroimagem_cli_myoinositol_spectros","s":"ativo","t":datetime.utcnow().isoformat()}
@router_n200_clinical.get("")
async def i_n200_clinical():
    return {"p":"neuroimagem_cli_n200_clinical","s":"ativo","t":datetime.utcnow().isoformat()}
@router_n400_clinical.get("")
async def i_n400_clinical():
    return {"p":"neuroimagem_cli_n400_clinical","s":"ativo","t":datetime.utcnow().isoformat()}
@router_naa_spectroscopy.get("")
async def i_naa_spectroscopy():
    return {"p":"neuroimagem_cli_naa_spectroscopy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neuroinflammation_pe.get("")
async def i_neuroinflammation_pe():
    return {"p":"neuroimagem_cli_neuroinflammation_pe","s":"ativo","t":datetime.utcnow().isoformat()}
@router_p300_clinical.get("")
async def i_p300_clinical():
    return {"p":"neuroimagem_cli_p300_clinical","s":"ativo","t":datetime.utcnow().isoformat()}
@router_p600_clinical.get("")
async def i_p600_clinical():
    return {"p":"neuroimagem_cli_p600_clinical","s":"ativo","t":datetime.utcnow().isoformat()}
@router_path_length.get("")
async def i_path_length():
    return {"p":"neuroimagem_cli_path_length","s":"ativo","t":datetime.utcnow().isoformat()}
@router_perfusion_spect.get("")
async def i_perfusion_spect():
    return {"p":"neuroimagem_cli_perfusion_spect","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pet_clinical.get("")
async def i_pet_clinical():
    return {"p":"neuroimagem_cli_pet_clinical","s":"ativo","t":datetime.utcnow().isoformat()}
@router_phase_amplitude_coup.get("")
async def i_phase_amplitude_coup():
    return {"p":"neuroimagem_cli_phase_amplitude_coup","s":"ativo","t":datetime.utcnow().isoformat()}
@router_precision_weighting.get("")
async def i_precision_weighting():
    return {"p":"neuroimagem_cli_precision_weighting","s":"ativo","t":datetime.utcnow().isoformat()}
@router_predictive_coding.get("")
async def i_predictive_coding():
    return {"p":"neuroimagem_cli_predictive_coding","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reinforcement_learni.get("")
async def i_reinforcement_learni():
    return {"p":"neuroimagem_cli_reinforcement_learni","s":"ativo","t":datetime.utcnow().isoformat()}
@router_resting_state_fmri.get("")
async def i_resting_state_fmri():
    return {"p":"neuroimagem_cli_resting_state_fmri","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reward_positivity.get("")
async def i_reward_positivity():
    return {"p":"neuroimagem_cli_reward_positivity","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reward_prediction_er.get("")
async def i_reward_prediction_er():
    return {"p":"neuroimagem_cli_reward_prediction_er","s":"ativo","t":datetime.utcnow().isoformat()}
@router_rich_club.get("")
async def i_rich_club():
    return {"p":"neuroimagem_cli_rich_club","s":"ativo","t":datetime.utcnow().isoformat()}
@router_salience_network.get("")
async def i_salience_network():
    return {"p":"neuroimagem_cli_salience_network","s":"ativo","t":datetime.utcnow().isoformat()}
@router_serotonin_pet.get("")
async def i_serotonin_pet():
    return {"p":"neuroimagem_cli_serotonin_pet","s":"ativo","t":datetime.utcnow().isoformat()}
@router_small_world_network.get("")
async def i_small_world_network():
    return {"p":"neuroimagem_cli_small_world_network","s":"ativo","t":datetime.utcnow().isoformat()}
@router_social_bayesian.get("")
async def i_social_bayesian():
    return {"p":"neuroimagem_cli_social_bayesian","s":"ativo","t":datetime.utcnow().isoformat()}
@router_spect_clinical.get("")
async def i_spect_clinical():
    return {"p":"neuroimagem_cli_spect_clinical","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ssp_meg.get("")
async def i_ssp_meg():
    return {"p":"neuroimagem_cli_ssp_meg","s":"ativo","t":datetime.utcnow().isoformat()}
@router_structural_mri.get("")
async def i_structural_mri():
    return {"p":"neuroimagem_cli_structural_mri","s":"ativo","t":datetime.utcnow().isoformat()}
@router_subcortical_network.get("")
async def i_subcortical_network():
    return {"p":"neuroimagem_cli_subcortical_network","s":"ativo","t":datetime.utcnow().isoformat()}
@router_surface_based_morpho.get("")
async def i_surface_based_morpho():
    return {"p":"neuroimagem_cli_surface_based_morpho","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tau_pet.get("")
async def i_tau_pet():
    return {"p":"neuroimagem_cli_tau_pet","s":"ativo","t":datetime.utcnow().isoformat()}
@router_temporal_difference.get("")
async def i_temporal_difference():
    return {"p":"neuroimagem_cli_temporal_difference","s":"ativo","t":datetime.utcnow().isoformat()}
@router_thalamic_network.get("")
async def i_thalamic_network():
    return {"p":"neuroimagem_cli_thalamic_network","s":"ativo","t":datetime.utcnow().isoformat()}
@router_theta_gamma_coupling.get("")
async def i_theta_gamma_coupling():
    return {"p":"neuroimagem_cli_theta_gamma_coupling","s":"ativo","t":datetime.utcnow().isoformat()}
@router_theta_oscillation.get("")
async def i_theta_oscillation():
    return {"p":"neuroimagem_cli_theta_oscillation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ventral_attention.get("")
async def i_ventral_attention():
    return {"p":"neuroimagem_cli_ventral_attention","s":"ativo","t":datetime.utcnow().isoformat()}
@router_visual_network.get("")
async def i_visual_network():
    return {"p":"neuroimagem_cli_visual_network","s":"ativo","t":datetime.utcnow().isoformat()}
@router_volumetric_mri.get("")
async def i_volumetric_mri():
    return {"p":"neuroimagem_cli_volumetric_mri","s":"ativo","t":datetime.utcnow().isoformat()}
@router_voxel_based_morphome.get("")
async def i_voxel_based_morphome():
    return {"p":"neuroimagem_cli_voxel_based_morphome","s":"ativo","t":datetime.utcnow().isoformat()}
@router_white_matter_mri.get("")
async def i_white_matter_mri():
    return {"p":"neuroimagem_cli_white_matter_mri","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_neuroimagem_clinica(PluginBase):
    name = "consolidated_neuroimagem_clinica"
    def setup(self, app):
        app.include_router(router_active_inference)
        app.include_router(router_allostasis_model)
        app.include_router(router_alpha_oscillation)
        app.include_router(router_alpha_theta_coupling)
        app.include_router(router_amyloid_pet)
        app.include_router(router_bayesian_brain)
        app.include_router(router_beta_oscillation2)
        app.include_router(router_central_executive)
        app.include_router(router_cerebellar_network)
        app.include_router(router_choline_spectroscopy)
        app.include_router(router_clustering_coefficie)
        app.include_router(router_cnv)
        app.include_router(router_computational_psychi)
        app.include_router(router_contingent_negative_)
        app.include_router(router_cortical_thickness_m)
        app.include_router(router_creatine_spectroscop)
        app.include_router(router_cross_frequency_coup)
        app.include_router(router_default_mode_network)
        app.include_router(router_delta_oscillation2)
        app.include_router(router_dics_beamformer)
        app.include_router(router_dopamine_pet)
        app.include_router(router_dopamine_transporter)
        app.include_router(router_dorsal_attention_net)
        app.include_router(router_dti_tractography)
        app.include_router(router_eeg_clinical2)
        app.include_router(router_erp_clinical)
        app.include_router(router_error_related_negati)
        app.include_router(router_fdg_pet)
        app.include_router(router_feedback_related_neg)
        app.include_router(router_fmri_clinical)
        app.include_router(router_free_energy_principl)
        app.include_router(router_frontal_asymmetry)
        app.include_router(router_frontoparietal)
        app.include_router(router_functional_connectiv)
        app.include_router(router_gaba_spectroscopy)
        app.include_router(router_gamma_oscillation2)
        app.include_router(router_generative_models)
        app.include_router(router_global_efficiency)
        app.include_router(router_glutamate_spectrosco)
        app.include_router(router_graph_theory_brain)
        app.include_router(router_hierarchical_inferen)
        app.include_router(router_hub_nodes)
        app.include_router(router_ica_meg)
        app.include_router(router_infra_slow_oscillati)
        app.include_router(router_interoceptive_predic)
        app.include_router(router_lactate_spectroscopy)
        app.include_router(router_lateralized_readines)
        app.include_router(router_lcmv_beamforming)
        app.include_router(router_limbic_network)
        app.include_router(router_local_efficiency)
        app.include_router(router_meg_clinical2)
        app.include_router(router_mismatch_negativity)
        app.include_router(router_model_based_rl)
        app.include_router(router_model_free_rl)
        app.include_router(router_modularity)
        app.include_router(router_motor_network)
        app.include_router(router_mri_spectroscopy)
        app.include_router(router_myoinositol_spectros)
        app.include_router(router_n200_clinical)
        app.include_router(router_n400_clinical)
        app.include_router(router_naa_spectroscopy)
        app.include_router(router_neuroinflammation_pe)
        app.include_router(router_p300_clinical)
        app.include_router(router_p600_clinical)
        app.include_router(router_path_length)
        app.include_router(router_perfusion_spect)
        app.include_router(router_pet_clinical)
        app.include_router(router_phase_amplitude_coup)
        app.include_router(router_precision_weighting)
        app.include_router(router_predictive_coding)
        app.include_router(router_reinforcement_learni)
        app.include_router(router_resting_state_fmri)
        app.include_router(router_reward_positivity)
        app.include_router(router_reward_prediction_er)
        app.include_router(router_rich_club)
        app.include_router(router_salience_network)
        app.include_router(router_serotonin_pet)
        app.include_router(router_small_world_network)
        app.include_router(router_social_bayesian)
        app.include_router(router_spect_clinical)
        app.include_router(router_ssp_meg)
        app.include_router(router_structural_mri)
        app.include_router(router_subcortical_network)
        app.include_router(router_surface_based_morpho)
        app.include_router(router_tau_pet)
        app.include_router(router_temporal_difference)
        app.include_router(router_thalamic_network)
        app.include_router(router_theta_gamma_coupling)
        app.include_router(router_theta_oscillation)
        app.include_router(router_ventral_attention)
        app.include_router(router_visual_network)
        app.include_router(router_volumetric_mri)
        app.include_router(router_voxel_based_morphome)
        app.include_router(router_white_matter_mri)


plugin = Plugin_neuroimagem_clinica()
