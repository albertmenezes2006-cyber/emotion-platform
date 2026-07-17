from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_allostatic_load = APIRouter(prefix="/api/v1/neurobiologi/allostatic_load", tags=["neurobiologia_transtornos"])
router_amygdala_anxiety = APIRouter(prefix="/api/v1/neurobiologi/amygdala_anxiety", tags=["neurobiologia_transtornos"])
router_amygdala_ptsd = APIRouter(prefix="/api/v1/neurobiologi/amygdala_ptsd", tags=["neurobiologia_transtornos"])
router_antipsychotic_mech = APIRouter(prefix="/api/v1/neurobiologi/antipsychotic_mech", tags=["neurobiologia_transtornos"])
router_bdnf_depression = APIRouter(prefix="/api/v1/neurobiologi/bdnf_depression", tags=["neurobiologia_transtornos"])
router_bnst_anxiety = APIRouter(prefix="/api/v1/neurobiologi/bnst_anxiety", tags=["neurobiologia_transtornos"])
router_caudate_ocd = APIRouter(prefix="/api/v1/neurobiologi/caudate_ocd", tags=["neurobiologia_transtornos"])
router_cingulate_anxiety = APIRouter(prefix="/api/v1/neurobiologi/cingulate_anxiety", tags=["neurobiologia_transtornos"])
router_circadian_bipolar = APIRouter(prefix="/api/v1/neurobiologi/circadian_bipolar", tags=["neurobiologia_transtornos"])
router_circadian_depression = APIRouter(prefix="/api/v1/neurobiologi/circadian_depression", tags=["neurobiologia_transtornos"])
router_connectivity = APIRouter(prefix="/api/v1/neurobiologi/connectivity", tags=["neurobiologia_transtornos"])
router_cortical_thinning = APIRouter(prefix="/api/v1/neurobiologi/cortical_thinning", tags=["neurobiologia_transtornos"])
router_corticostriatothalam = APIRouter(prefix="/api/v1/neurobiologi/corticostriatothalamocort", tags=["neurobiologia_transtornos"])
router_cortisol_ptsd = APIRouter(prefix="/api/v1/neurobiologi/cortisol_ptsd", tags=["neurobiologia_transtornos"])
router_craving_neural = APIRouter(prefix="/api/v1/neurobiologi/craving_neural", tags=["neurobiologia_transtornos"])
router_crf_anxiety = APIRouter(prefix="/api/v1/neurobiologi/crf_anxiety", tags=["neurobiologia_transtornos"])
router_decision_making_addi = APIRouter(prefix="/api/v1/neurobiologi/decision_making_addiction", tags=["neurobiologia_transtornos"])
router_default_mode_adhd = APIRouter(prefix="/api/v1/neurobiologi/default_mode_adhd", tags=["neurobiologia_transtornos"])
router_dopamine_adhd = APIRouter(prefix="/api/v1/neurobiologi/dopamine_adhd", tags=["neurobiologia_transtornos"])
router_dopamine_depression = APIRouter(prefix="/api/v1/neurobiologi/dopamine_depression", tags=["neurobiologia_transtornos"])
router_dopamine_hypothesis = APIRouter(prefix="/api/v1/neurobiologi/dopamine_hypothesis", tags=["neurobiologia_transtornos"])
router_dopamine_ocd = APIRouter(prefix="/api/v1/neurobiologi/dopamine_ocd", tags=["neurobiologia_transtornos"])
router_dopamine_reward = APIRouter(prefix="/api/v1/neurobiologi/dopamine_reward", tags=["neurobiologia_transtornos"])
router_endocannabinoid_addi = APIRouter(prefix="/api/v1/neurobiologi/endocannabinoid_addiction", tags=["neurobiologia_transtornos"])
router_endocannabinoid_ptsd = APIRouter(prefix="/api/v1/neurobiologi/endocannabinoid_ptsd", tags=["neurobiologia_transtornos"])
router_endocannabinoids_anx = APIRouter(prefix="/api/v1/neurobiologi/endocannabinoids_anxiety", tags=["neurobiologia_transtornos"])
router_epigenetics_ptsd = APIRouter(prefix="/api/v1/neurobiologi/epigenetics_ptsd", tags=["neurobiologia_transtornos"])
router_executive_function_a = APIRouter(prefix="/api/v1/neurobiologi/executive_function_adhd", tags=["neurobiologia_transtornos"])
router_gaba_addiction = APIRouter(prefix="/api/v1/neurobiologi/gaba_addiction", tags=["neurobiologia_transtornos"])
router_gaba_anxiety = APIRouter(prefix="/api/v1/neurobiologi/gaba_anxiety", tags=["neurobiologia_transtornos"])
router_gaba_depression = APIRouter(prefix="/api/v1/neurobiologi/gaba_depression", tags=["neurobiologia_transtornos"])
router_gaba_excitation_auti = APIRouter(prefix="/api/v1/neurobiologi/gaba_excitation_autism", tags=["neurobiologia_transtornos"])
router_gaba_ocd = APIRouter(prefix="/api/v1/neurobiologi/gaba_ocd", tags=["neurobiologia_transtornos"])
router_gaba_schizophrenia = APIRouter(prefix="/api/v1/neurobiologi/gaba_schizophrenia", tags=["neurobiologia_transtornos"])
router_glutamate_addiction = APIRouter(prefix="/api/v1/neurobiologi/glutamate_addiction", tags=["neurobiologia_transtornos"])
router_glutamate_depression = APIRouter(prefix="/api/v1/neurobiologi/glutamate_depression", tags=["neurobiologia_transtornos"])
router_glutamate_ocd = APIRouter(prefix="/api/v1/neurobiologi/glutamate_ocd", tags=["neurobiologia_transtornos"])
router_glutamate_schizophre = APIRouter(prefix="/api/v1/neurobiologi/glutamate_schizophrenia", tags=["neurobiologia_transtornos"])
router_habit_learning = APIRouter(prefix="/api/v1/neurobiologi/habit_learning", tags=["neurobiologia_transtornos"])
router_hippocampus_anxiety = APIRouter(prefix="/api/v1/neurobiologi/hippocampus_anxiety", tags=["neurobiologia_transtornos"])
router_hippocampus_ptsd = APIRouter(prefix="/api/v1/neurobiologi/hippocampus_ptsd", tags=["neurobiologia_transtornos"])
router_hpa_depression = APIRouter(prefix="/api/v1/neurobiologi/hpa_depression", tags=["neurobiologia_transtornos"])
router_hpa_ptsd = APIRouter(prefix="/api/v1/neurobiologi/hpa_ptsd", tags=["neurobiologia_transtornos"])
router_incentive_salience = APIRouter(prefix="/api/v1/neurobiologi/incentive_salience", tags=["neurobiologia_transtornos"])
router_inflammation_depress = APIRouter(prefix="/api/v1/neurobiologi/inflammation_depression", tags=["neurobiologia_transtornos"])
router_insula_anxiety = APIRouter(prefix="/api/v1/neurobiologi/insula_anxiety", tags=["neurobiologia_transtornos"])
router_kindling_bipolar = APIRouter(prefix="/api/v1/neurobiologi/kindling_bipolar", tags=["neurobiologia_transtornos"])
router_lamotrigine_mechanis = APIRouter(prefix="/api/v1/neurobiologi/lamotrigine_mechanism", tags=["neurobiologia_transtornos"])
router_lithium_mechanism = APIRouter(prefix="/api/v1/neurobiologi/lithium_mechanism", tags=["neurobiologia_transtornos"])
router_mesocortical_dopamin = APIRouter(prefix="/api/v1/neurobiologi/mesocortical_dopamine", tags=["neurobiologia_transtornos"])
router_mesolimbic_dopamine = APIRouter(prefix="/api/v1/neurobiologi/mesolimbic_dopamine", tags=["neurobiologia_transtornos"])
router_mirror_neuron_autism = APIRouter(prefix="/api/v1/neurobiologi/mirror_neuron_autism", tags=["neurobiologia_transtornos"])
router_neurobiologia_adicao = APIRouter(prefix="/api/v1/neurobiologi/neurobiologia_adicao", tags=["neurobiologia_transtornos"])
router_neurobiologia_ansied = APIRouter(prefix="/api/v1/neurobiologi/neurobiologia_ansiedade", tags=["neurobiologia_transtornos"])
router_neurobiologia_autism = APIRouter(prefix="/api/v1/neurobiologi/neurobiologia_autismo", tags=["neurobiologia_transtornos"])
router_neurobiologia_bipola = APIRouter(prefix="/api/v1/neurobiologi/neurobiologia_bipolar", tags=["neurobiologia_transtornos"])
router_neurobiologia_depres = APIRouter(prefix="/api/v1/neurobiologi/neurobiologia_depressao", tags=["neurobiologia_transtornos"])
router_neurobiologia_esquiz = APIRouter(prefix="/api/v1/neurobiologi/neurobiologia_esquizofren", tags=["neurobiologia_transtornos"])
router_neurobiologia_ptsd = APIRouter(prefix="/api/v1/neurobiologi/neurobiologia_ptsd", tags=["neurobiologia_transtornos"])
router_neurobiologia_tdah = APIRouter(prefix="/api/v1/neurobiologi/neurobiologia_tdah", tags=["neurobiologia_transtornos"])
router_neurobiologia_toc = APIRouter(prefix="/api/v1/neurobiologi/neurobiologia_toc", tags=["neurobiologia_transtornos"])
router_neurogenesis_depress = APIRouter(prefix="/api/v1/neurobiologi/neurogenesis_depression", tags=["neurobiologia_transtornos"])
router_neuroinflammation_sc = APIRouter(prefix="/api/v1/neurobiologi/neuroinflammation_schiz", tags=["neurobiologia_transtornos"])
router_neuropeptides = APIRouter(prefix="/api/v1/neurobiologi/neuropeptides", tags=["neurobiologia_transtornos"])
router_neuropeptides_ptsd = APIRouter(prefix="/api/v1/neurobiologi/neuropeptides_ptsd", tags=["neurobiologia_transtornos"])
router_nmda_hypothesis = APIRouter(prefix="/api/v1/neurobiologi/nmda_hypothesis", tags=["neurobiologia_transtornos"])
router_norepinephrine_adhd = APIRouter(prefix="/api/v1/neurobiologi/norepinephrine_adhd", tags=["neurobiologia_transtornos"])
router_norepinephrine_anxie = APIRouter(prefix="/api/v1/neurobiologi/norepinephrine_anxiety", tags=["neurobiologia_transtornos"])
router_norepinephrine_depre = APIRouter(prefix="/api/v1/neurobiologi/norepinephrine_depression", tags=["neurobiologia_transtornos"])
router_norepinephrine_ptsd = APIRouter(prefix="/api/v1/neurobiologi/norepinephrine_ptsd", tags=["neurobiologia_transtornos"])
router_npy_anxiety = APIRouter(prefix="/api/v1/neurobiologi/npy_anxiety", tags=["neurobiologia_transtornos"])
router_nucleus_accumbens = APIRouter(prefix="/api/v1/neurobiologi/nucleus_accumbens", tags=["neurobiologia_transtornos"])
router_opioid_addiction = APIRouter(prefix="/api/v1/neurobiologi/opioid_addiction", tags=["neurobiologia_transtornos"])
router_opioids_ocd = APIRouter(prefix="/api/v1/neurobiologi/opioids_ocd", tags=["neurobiologia_transtornos"])
router_orbitofrontal_ocd = APIRouter(prefix="/api/v1/neurobiologi/orbitofrontal_ocd", tags=["neurobiologia_transtornos"])
router_oxytocin_autism = APIRouter(prefix="/api/v1/neurobiologi/oxytocin_autism", tags=["neurobiologia_transtornos"])
router_prefrontal_adhd = APIRouter(prefix="/api/v1/neurobiologi/prefrontal_adhd", tags=["neurobiologia_transtornos"])
router_prefrontal_anxiety = APIRouter(prefix="/api/v1/neurobiologi/prefrontal_anxiety", tags=["neurobiologia_transtornos"])
router_prefrontal_ptsd = APIRouter(prefix="/api/v1/neurobiologi/prefrontal_ptsd", tags=["neurobiologia_transtornos"])
router_reward_circuit = APIRouter(prefix="/api/v1/neurobiologi/reward_circuit", tags=["neurobiologia_transtornos"])
router_reward_delay_adhd = APIRouter(prefix="/api/v1/neurobiologi/reward_delay_adhd", tags=["neurobiologia_transtornos"])
router_serotonin_anxiety = APIRouter(prefix="/api/v1/neurobiologi/serotonin_anxiety", tags=["neurobiologia_transtornos"])
router_serotonin_autism = APIRouter(prefix="/api/v1/neurobiologi/serotonin_autism", tags=["neurobiologia_transtornos"])
router_serotonin_hypothesis = APIRouter(prefix="/api/v1/neurobiologi/serotonin_hypothesis", tags=["neurobiologia_transtornos"])
router_serotonin_ocd = APIRouter(prefix="/api/v1/neurobiologi/serotonin_ocd", tags=["neurobiologia_transtornos"])
router_serotonin_ptsd = APIRouter(prefix="/api/v1/neurobiologi/serotonin_ptsd", tags=["neurobiologia_transtornos"])
router_serotonin_schizophre = APIRouter(prefix="/api/v1/neurobiologi/serotonin_schizophrenia", tags=["neurobiologia_transtornos"])
router_sleep_depression_neu = APIRouter(prefix="/api/v1/neurobiologi/sleep_depression_neuro", tags=["neurobiologia_transtornos"])
router_social_brain_autism = APIRouter(prefix="/api/v1/neurobiologi/social_brain_autism", tags=["neurobiologia_transtornos"])
router_thalamus_ocd = APIRouter(prefix="/api/v1/neurobiologi/thalamus_ocd", tags=["neurobiologia_transtornos"])
router_valproate_mechanism = APIRouter(prefix="/api/v1/neurobiologi/valproate_mechanism", tags=["neurobiologia_transtornos"])
router_ventricular_enlargem = APIRouter(prefix="/api/v1/neurobiologi/ventricular_enlargement", tags=["neurobiologia_transtornos"])
router_white_matter_schiz = APIRouter(prefix="/api/v1/neurobiologi/white_matter_schiz", tags=["neurobiologia_transtornos"])

@router_allostatic_load.get("")
async def i_allostatic_load():
    return {"p":"neurobiologia_t_allostatic_load","s":"ativo","t":datetime.utcnow().isoformat()}
@router_amygdala_anxiety.get("")
async def i_amygdala_anxiety():
    return {"p":"neurobiologia_t_amygdala_anxiety","s":"ativo","t":datetime.utcnow().isoformat()}
@router_amygdala_ptsd.get("")
async def i_amygdala_ptsd():
    return {"p":"neurobiologia_t_amygdala_ptsd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_antipsychotic_mech.get("")
async def i_antipsychotic_mech():
    return {"p":"neurobiologia_t_antipsychotic_mech","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bdnf_depression.get("")
async def i_bdnf_depression():
    return {"p":"neurobiologia_t_bdnf_depression","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bnst_anxiety.get("")
async def i_bnst_anxiety():
    return {"p":"neurobiologia_t_bnst_anxiety","s":"ativo","t":datetime.utcnow().isoformat()}
@router_caudate_ocd.get("")
async def i_caudate_ocd():
    return {"p":"neurobiologia_t_caudate_ocd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cingulate_anxiety.get("")
async def i_cingulate_anxiety():
    return {"p":"neurobiologia_t_cingulate_anxiety","s":"ativo","t":datetime.utcnow().isoformat()}
@router_circadian_bipolar.get("")
async def i_circadian_bipolar():
    return {"p":"neurobiologia_t_circadian_bipolar","s":"ativo","t":datetime.utcnow().isoformat()}
@router_circadian_depression.get("")
async def i_circadian_depression():
    return {"p":"neurobiologia_t_circadian_depression","s":"ativo","t":datetime.utcnow().isoformat()}
@router_connectivity.get("")
async def i_connectivity():
    return {"p":"neurobiologia_t_connectivity","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cortical_thinning.get("")
async def i_cortical_thinning():
    return {"p":"neurobiologia_t_cortical_thinning","s":"ativo","t":datetime.utcnow().isoformat()}
@router_corticostriatothalam.get("")
async def i_corticostriatothalam():
    return {"p":"neurobiologia_t_corticostriatothalam","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cortisol_ptsd.get("")
async def i_cortisol_ptsd():
    return {"p":"neurobiologia_t_cortisol_ptsd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_craving_neural.get("")
async def i_craving_neural():
    return {"p":"neurobiologia_t_craving_neural","s":"ativo","t":datetime.utcnow().isoformat()}
@router_crf_anxiety.get("")
async def i_crf_anxiety():
    return {"p":"neurobiologia_t_crf_anxiety","s":"ativo","t":datetime.utcnow().isoformat()}
@router_decision_making_addi.get("")
async def i_decision_making_addi():
    return {"p":"neurobiologia_t_decision_making_addi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_default_mode_adhd.get("")
async def i_default_mode_adhd():
    return {"p":"neurobiologia_t_default_mode_adhd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dopamine_adhd.get("")
async def i_dopamine_adhd():
    return {"p":"neurobiologia_t_dopamine_adhd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dopamine_depression.get("")
async def i_dopamine_depression():
    return {"p":"neurobiologia_t_dopamine_depression","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dopamine_hypothesis.get("")
async def i_dopamine_hypothesis():
    return {"p":"neurobiologia_t_dopamine_hypothesis","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dopamine_ocd.get("")
async def i_dopamine_ocd():
    return {"p":"neurobiologia_t_dopamine_ocd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dopamine_reward.get("")
async def i_dopamine_reward():
    return {"p":"neurobiologia_t_dopamine_reward","s":"ativo","t":datetime.utcnow().isoformat()}
@router_endocannabinoid_addi.get("")
async def i_endocannabinoid_addi():
    return {"p":"neurobiologia_t_endocannabinoid_addi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_endocannabinoid_ptsd.get("")
async def i_endocannabinoid_ptsd():
    return {"p":"neurobiologia_t_endocannabinoid_ptsd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_endocannabinoids_anx.get("")
async def i_endocannabinoids_anx():
    return {"p":"neurobiologia_t_endocannabinoids_anx","s":"ativo","t":datetime.utcnow().isoformat()}
@router_epigenetics_ptsd.get("")
async def i_epigenetics_ptsd():
    return {"p":"neurobiologia_t_epigenetics_ptsd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_executive_function_a.get("")
async def i_executive_function_a():
    return {"p":"neurobiologia_t_executive_function_a","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gaba_addiction.get("")
async def i_gaba_addiction():
    return {"p":"neurobiologia_t_gaba_addiction","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gaba_anxiety.get("")
async def i_gaba_anxiety():
    return {"p":"neurobiologia_t_gaba_anxiety","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gaba_depression.get("")
async def i_gaba_depression():
    return {"p":"neurobiologia_t_gaba_depression","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gaba_excitation_auti.get("")
async def i_gaba_excitation_auti():
    return {"p":"neurobiologia_t_gaba_excitation_auti","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gaba_ocd.get("")
async def i_gaba_ocd():
    return {"p":"neurobiologia_t_gaba_ocd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gaba_schizophrenia.get("")
async def i_gaba_schizophrenia():
    return {"p":"neurobiologia_t_gaba_schizophrenia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_glutamate_addiction.get("")
async def i_glutamate_addiction():
    return {"p":"neurobiologia_t_glutamate_addiction","s":"ativo","t":datetime.utcnow().isoformat()}
@router_glutamate_depression.get("")
async def i_glutamate_depression():
    return {"p":"neurobiologia_t_glutamate_depression","s":"ativo","t":datetime.utcnow().isoformat()}
@router_glutamate_ocd.get("")
async def i_glutamate_ocd():
    return {"p":"neurobiologia_t_glutamate_ocd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_glutamate_schizophre.get("")
async def i_glutamate_schizophre():
    return {"p":"neurobiologia_t_glutamate_schizophre","s":"ativo","t":datetime.utcnow().isoformat()}
@router_habit_learning.get("")
async def i_habit_learning():
    return {"p":"neurobiologia_t_habit_learning","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hippocampus_anxiety.get("")
async def i_hippocampus_anxiety():
    return {"p":"neurobiologia_t_hippocampus_anxiety","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hippocampus_ptsd.get("")
async def i_hippocampus_ptsd():
    return {"p":"neurobiologia_t_hippocampus_ptsd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hpa_depression.get("")
async def i_hpa_depression():
    return {"p":"neurobiologia_t_hpa_depression","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hpa_ptsd.get("")
async def i_hpa_ptsd():
    return {"p":"neurobiologia_t_hpa_ptsd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_incentive_salience.get("")
async def i_incentive_salience():
    return {"p":"neurobiologia_t_incentive_salience","s":"ativo","t":datetime.utcnow().isoformat()}
@router_inflammation_depress.get("")
async def i_inflammation_depress():
    return {"p":"neurobiologia_t_inflammation_depress","s":"ativo","t":datetime.utcnow().isoformat()}
@router_insula_anxiety.get("")
async def i_insula_anxiety():
    return {"p":"neurobiologia_t_insula_anxiety","s":"ativo","t":datetime.utcnow().isoformat()}
@router_kindling_bipolar.get("")
async def i_kindling_bipolar():
    return {"p":"neurobiologia_t_kindling_bipolar","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lamotrigine_mechanis.get("")
async def i_lamotrigine_mechanis():
    return {"p":"neurobiologia_t_lamotrigine_mechanis","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lithium_mechanism.get("")
async def i_lithium_mechanism():
    return {"p":"neurobiologia_t_lithium_mechanism","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mesocortical_dopamin.get("")
async def i_mesocortical_dopamin():
    return {"p":"neurobiologia_t_mesocortical_dopamin","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mesolimbic_dopamine.get("")
async def i_mesolimbic_dopamine():
    return {"p":"neurobiologia_t_mesolimbic_dopamine","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mirror_neuron_autism.get("")
async def i_mirror_neuron_autism():
    return {"p":"neurobiologia_t_mirror_neuron_autism","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neurobiologia_adicao.get("")
async def i_neurobiologia_adicao():
    return {"p":"neurobiologia_t_neurobiologia_adicao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neurobiologia_ansied.get("")
async def i_neurobiologia_ansied():
    return {"p":"neurobiologia_t_neurobiologia_ansied","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neurobiologia_autism.get("")
async def i_neurobiologia_autism():
    return {"p":"neurobiologia_t_neurobiologia_autism","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neurobiologia_bipola.get("")
async def i_neurobiologia_bipola():
    return {"p":"neurobiologia_t_neurobiologia_bipola","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neurobiologia_depres.get("")
async def i_neurobiologia_depres():
    return {"p":"neurobiologia_t_neurobiologia_depres","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neurobiologia_esquiz.get("")
async def i_neurobiologia_esquiz():
    return {"p":"neurobiologia_t_neurobiologia_esquiz","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neurobiologia_ptsd.get("")
async def i_neurobiologia_ptsd():
    return {"p":"neurobiologia_t_neurobiologia_ptsd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neurobiologia_tdah.get("")
async def i_neurobiologia_tdah():
    return {"p":"neurobiologia_t_neurobiologia_tdah","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neurobiologia_toc.get("")
async def i_neurobiologia_toc():
    return {"p":"neurobiologia_t_neurobiologia_toc","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neurogenesis_depress.get("")
async def i_neurogenesis_depress():
    return {"p":"neurobiologia_t_neurogenesis_depress","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neuroinflammation_sc.get("")
async def i_neuroinflammation_sc():
    return {"p":"neurobiologia_t_neuroinflammation_sc","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neuropeptides.get("")
async def i_neuropeptides():
    return {"p":"neurobiologia_t_neuropeptides","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neuropeptides_ptsd.get("")
async def i_neuropeptides_ptsd():
    return {"p":"neurobiologia_t_neuropeptides_ptsd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nmda_hypothesis.get("")
async def i_nmda_hypothesis():
    return {"p":"neurobiologia_t_nmda_hypothesis","s":"ativo","t":datetime.utcnow().isoformat()}
@router_norepinephrine_adhd.get("")
async def i_norepinephrine_adhd():
    return {"p":"neurobiologia_t_norepinephrine_adhd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_norepinephrine_anxie.get("")
async def i_norepinephrine_anxie():
    return {"p":"neurobiologia_t_norepinephrine_anxie","s":"ativo","t":datetime.utcnow().isoformat()}
@router_norepinephrine_depre.get("")
async def i_norepinephrine_depre():
    return {"p":"neurobiologia_t_norepinephrine_depre","s":"ativo","t":datetime.utcnow().isoformat()}
@router_norepinephrine_ptsd.get("")
async def i_norepinephrine_ptsd():
    return {"p":"neurobiologia_t_norepinephrine_ptsd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_npy_anxiety.get("")
async def i_npy_anxiety():
    return {"p":"neurobiologia_t_npy_anxiety","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nucleus_accumbens.get("")
async def i_nucleus_accumbens():
    return {"p":"neurobiologia_t_nucleus_accumbens","s":"ativo","t":datetime.utcnow().isoformat()}
@router_opioid_addiction.get("")
async def i_opioid_addiction():
    return {"p":"neurobiologia_t_opioid_addiction","s":"ativo","t":datetime.utcnow().isoformat()}
@router_opioids_ocd.get("")
async def i_opioids_ocd():
    return {"p":"neurobiologia_t_opioids_ocd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_orbitofrontal_ocd.get("")
async def i_orbitofrontal_ocd():
    return {"p":"neurobiologia_t_orbitofrontal_ocd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_oxytocin_autism.get("")
async def i_oxytocin_autism():
    return {"p":"neurobiologia_t_oxytocin_autism","s":"ativo","t":datetime.utcnow().isoformat()}
@router_prefrontal_adhd.get("")
async def i_prefrontal_adhd():
    return {"p":"neurobiologia_t_prefrontal_adhd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_prefrontal_anxiety.get("")
async def i_prefrontal_anxiety():
    return {"p":"neurobiologia_t_prefrontal_anxiety","s":"ativo","t":datetime.utcnow().isoformat()}
@router_prefrontal_ptsd.get("")
async def i_prefrontal_ptsd():
    return {"p":"neurobiologia_t_prefrontal_ptsd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reward_circuit.get("")
async def i_reward_circuit():
    return {"p":"neurobiologia_t_reward_circuit","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reward_delay_adhd.get("")
async def i_reward_delay_adhd():
    return {"p":"neurobiologia_t_reward_delay_adhd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_serotonin_anxiety.get("")
async def i_serotonin_anxiety():
    return {"p":"neurobiologia_t_serotonin_anxiety","s":"ativo","t":datetime.utcnow().isoformat()}
@router_serotonin_autism.get("")
async def i_serotonin_autism():
    return {"p":"neurobiologia_t_serotonin_autism","s":"ativo","t":datetime.utcnow().isoformat()}
@router_serotonin_hypothesis.get("")
async def i_serotonin_hypothesis():
    return {"p":"neurobiologia_t_serotonin_hypothesis","s":"ativo","t":datetime.utcnow().isoformat()}
@router_serotonin_ocd.get("")
async def i_serotonin_ocd():
    return {"p":"neurobiologia_t_serotonin_ocd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_serotonin_ptsd.get("")
async def i_serotonin_ptsd():
    return {"p":"neurobiologia_t_serotonin_ptsd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_serotonin_schizophre.get("")
async def i_serotonin_schizophre():
    return {"p":"neurobiologia_t_serotonin_schizophre","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sleep_depression_neu.get("")
async def i_sleep_depression_neu():
    return {"p":"neurobiologia_t_sleep_depression_neu","s":"ativo","t":datetime.utcnow().isoformat()}
@router_social_brain_autism.get("")
async def i_social_brain_autism():
    return {"p":"neurobiologia_t_social_brain_autism","s":"ativo","t":datetime.utcnow().isoformat()}
@router_thalamus_ocd.get("")
async def i_thalamus_ocd():
    return {"p":"neurobiologia_t_thalamus_ocd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_valproate_mechanism.get("")
async def i_valproate_mechanism():
    return {"p":"neurobiologia_t_valproate_mechanism","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ventricular_enlargem.get("")
async def i_ventricular_enlargem():
    return {"p":"neurobiologia_t_ventricular_enlargem","s":"ativo","t":datetime.utcnow().isoformat()}
@router_white_matter_schiz.get("")
async def i_white_matter_schiz():
    return {"p":"neurobiologia_t_white_matter_schiz","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_neurobiologia_transt(PluginBase):
    name = "consolidated_neurobiologia_transtornos"
    def setup(self, app):
        app.include_router(router_allostatic_load)
        app.include_router(router_amygdala_anxiety)
        app.include_router(router_amygdala_ptsd)
        app.include_router(router_antipsychotic_mech)
        app.include_router(router_bdnf_depression)
        app.include_router(router_bnst_anxiety)
        app.include_router(router_caudate_ocd)
        app.include_router(router_cingulate_anxiety)
        app.include_router(router_circadian_bipolar)
        app.include_router(router_circadian_depression)
        app.include_router(router_connectivity)
        app.include_router(router_cortical_thinning)
        app.include_router(router_corticostriatothalam)
        app.include_router(router_cortisol_ptsd)
        app.include_router(router_craving_neural)
        app.include_router(router_crf_anxiety)
        app.include_router(router_decision_making_addi)
        app.include_router(router_default_mode_adhd)
        app.include_router(router_dopamine_adhd)
        app.include_router(router_dopamine_depression)
        app.include_router(router_dopamine_hypothesis)
        app.include_router(router_dopamine_ocd)
        app.include_router(router_dopamine_reward)
        app.include_router(router_endocannabinoid_addi)
        app.include_router(router_endocannabinoid_ptsd)
        app.include_router(router_endocannabinoids_anx)
        app.include_router(router_epigenetics_ptsd)
        app.include_router(router_executive_function_a)
        app.include_router(router_gaba_addiction)
        app.include_router(router_gaba_anxiety)
        app.include_router(router_gaba_depression)
        app.include_router(router_gaba_excitation_auti)
        app.include_router(router_gaba_ocd)
        app.include_router(router_gaba_schizophrenia)
        app.include_router(router_glutamate_addiction)
        app.include_router(router_glutamate_depression)
        app.include_router(router_glutamate_ocd)
        app.include_router(router_glutamate_schizophre)
        app.include_router(router_habit_learning)
        app.include_router(router_hippocampus_anxiety)
        app.include_router(router_hippocampus_ptsd)
        app.include_router(router_hpa_depression)
        app.include_router(router_hpa_ptsd)
        app.include_router(router_incentive_salience)
        app.include_router(router_inflammation_depress)
        app.include_router(router_insula_anxiety)
        app.include_router(router_kindling_bipolar)
        app.include_router(router_lamotrigine_mechanis)
        app.include_router(router_lithium_mechanism)
        app.include_router(router_mesocortical_dopamin)
        app.include_router(router_mesolimbic_dopamine)
        app.include_router(router_mirror_neuron_autism)
        app.include_router(router_neurobiologia_adicao)
        app.include_router(router_neurobiologia_ansied)
        app.include_router(router_neurobiologia_autism)
        app.include_router(router_neurobiologia_bipola)
        app.include_router(router_neurobiologia_depres)
        app.include_router(router_neurobiologia_esquiz)
        app.include_router(router_neurobiologia_ptsd)
        app.include_router(router_neurobiologia_tdah)
        app.include_router(router_neurobiologia_toc)
        app.include_router(router_neurogenesis_depress)
        app.include_router(router_neuroinflammation_sc)
        app.include_router(router_neuropeptides)
        app.include_router(router_neuropeptides_ptsd)
        app.include_router(router_nmda_hypothesis)
        app.include_router(router_norepinephrine_adhd)
        app.include_router(router_norepinephrine_anxie)
        app.include_router(router_norepinephrine_depre)
        app.include_router(router_norepinephrine_ptsd)
        app.include_router(router_npy_anxiety)
        app.include_router(router_nucleus_accumbens)
        app.include_router(router_opioid_addiction)
        app.include_router(router_opioids_ocd)
        app.include_router(router_orbitofrontal_ocd)
        app.include_router(router_oxytocin_autism)
        app.include_router(router_prefrontal_adhd)
        app.include_router(router_prefrontal_anxiety)
        app.include_router(router_prefrontal_ptsd)
        app.include_router(router_reward_circuit)
        app.include_router(router_reward_delay_adhd)
        app.include_router(router_serotonin_anxiety)
        app.include_router(router_serotonin_autism)
        app.include_router(router_serotonin_hypothesis)
        app.include_router(router_serotonin_ocd)
        app.include_router(router_serotonin_ptsd)
        app.include_router(router_serotonin_schizophre)
        app.include_router(router_sleep_depression_neu)
        app.include_router(router_social_brain_autism)
        app.include_router(router_thalamus_ocd)
        app.include_router(router_valproate_mechanism)
        app.include_router(router_ventricular_enlargem)
        app.include_router(router_white_matter_schiz)


plugin = Plugin_neurobiologia_transt()
