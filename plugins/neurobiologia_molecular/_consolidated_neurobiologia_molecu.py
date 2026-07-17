from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_acetylation_reader = APIRouter(prefix="/api/v1/neurobiologi/acetylation_reader", tags=["neurobiologia_molecular"])
router_adenosine_receptor = APIRouter(prefix="/api/v1/neurobiologi/adenosine_receptor", tags=["neurobiologia_molecular"])
router_alpha_synuclein = APIRouter(prefix="/api/v1/neurobiologi/alpha_synuclein", tags=["neurobiologia_molecular"])
router_ampa_receptor = APIRouter(prefix="/api/v1/neurobiologi/ampa_receptor", tags=["neurobiologia_molecular"])
router_ampk_autophagy = APIRouter(prefix="/api/v1/neurobiologi/ampk_autophagy", tags=["neurobiologia_molecular"])
router_amyloid_precursor = APIRouter(prefix="/api/v1/neurobiologi/amyloid_precursor", tags=["neurobiologia_molecular"])
router_androgen_receptor = APIRouter(prefix="/api/v1/neurobiologi/androgen_receptor", tags=["neurobiologia_molecular"])
router_aryl_hydrocarbon = APIRouter(prefix="/api/v1/neurobiologi/aryl_hydrocarbon", tags=["neurobiologia_molecular"])
router_atf4_translation = APIRouter(prefix="/api/v1/neurobiologi/atf4_translation", tags=["neurobiologia_molecular"])
router_atf6_pathway = APIRouter(prefix="/api/v1/neurobiologi/atf6_pathway", tags=["neurobiologia_molecular"])
router_atg5_mental = APIRouter(prefix="/api/v1/neurobiologi/atg5_mental", tags=["neurobiologia_molecular"])
router_atg7_mental = APIRouter(prefix="/api/v1/neurobiologi/atg7_mental", tags=["neurobiologia_molecular"])
router_autophagy_mental = APIRouter(prefix="/api/v1/neurobiologi/autophagy_mental", tags=["neurobiologia_molecular"])
router_beclin1 = APIRouter(prefix="/api/v1/neurobiologi/beclin1", tags=["neurobiologia_molecular"])
router_calnexin = APIRouter(prefix="/api/v1/neurobiologi/calnexin", tags=["neurobiologia_molecular"])
router_calreticulin = APIRouter(prefix="/api/v1/neurobiologi/calreticulin", tags=["neurobiologia_molecular"])
router_canal_calcio = APIRouter(prefix="/api/v1/neurobiologi/canal_calcio", tags=["neurobiologia_molecular"])
router_canal_cloreto = APIRouter(prefix="/api/v1/neurobiologi/canal_cloreto", tags=["neurobiologia_molecular"])
router_canal_ionico = APIRouter(prefix="/api/v1/neurobiologi/canal_ionico", tags=["neurobiologia_molecular"])
router_canal_potassio = APIRouter(prefix="/api/v1/neurobiologi/canal_potassio", tags=["neurobiologia_molecular"])
router_canal_sodio = APIRouter(prefix="/api/v1/neurobiologi/canal_sodio", tags=["neurobiologia_molecular"])
router_cannabinoid_receptor = APIRouter(prefix="/api/v1/neurobiologi/cannabinoid_receptor", tags=["neurobiologia_molecular"])
router_chaperone = APIRouter(prefix="/api/v1/neurobiologi/chaperone", tags=["neurobiologia_molecular"])
router_chemokine_receptor = APIRouter(prefix="/api/v1/neurobiologi/chemokine_receptor", tags=["neurobiologia_molecular"])
router_chop_ddit3 = APIRouter(prefix="/api/v1/neurobiologi/chop_ddit3", tags=["neurobiologia_molecular"])
router_cytokine_receptor = APIRouter(prefix="/api/v1/neurobiologi/cytokine_receptor", tags=["neurobiologia_molecular"])
router_derlin = APIRouter(prefix="/api/v1/neurobiologi/derlin", tags=["neurobiologia_molecular"])
router_dnmt_mental = APIRouter(prefix="/api/v1/neurobiologi/dnmt_mental", tags=["neurobiologia_molecular"])
router_dopamine_receptor = APIRouter(prefix="/api/v1/neurobiologi/dopamine_receptor", tags=["neurobiologia_molecular"])
router_endoplasmic_reticulu = APIRouter(prefix="/api/v1/neurobiologi/endoplasmic_reticulum", tags=["neurobiologia_molecular"])
router_er_stress = APIRouter(prefix="/api/v1/neurobiologi/er_stress", tags=["neurobiologia_molecular"])
router_ero1_mental = APIRouter(prefix="/api/v1/neurobiologi/ero1_mental", tags=["neurobiologia_molecular"])
router_estrogen_receptor = APIRouter(prefix="/api/v1/neurobiologi/estrogen_receptor", tags=["neurobiologia_molecular"])
router_fus_mental = APIRouter(prefix="/api/v1/neurobiologi/fus_mental", tags=["neurobiologia_molecular"])
router_gabaa_receptor = APIRouter(prefix="/api/v1/neurobiologi/gabaa_receptor", tags=["neurobiologia_molecular"])
router_gabab_receptor = APIRouter(prefix="/api/v1/neurobiologi/gabab_receptor", tags=["neurobiologia_molecular"])
router_glucocorticoid_recep = APIRouter(prefix="/api/v1/neurobiologi/glucocorticoid_receptor", tags=["neurobiologia_molecular"])
router_glycine_receptor = APIRouter(prefix="/api/v1/neurobiologi/glycine_receptor", tags=["neurobiologia_molecular"])
router_growth_factor_recept = APIRouter(prefix="/api/v1/neurobiologi/growth_factor_receptor", tags=["neurobiologia_molecular"])
router_grp78_bip = APIRouter(prefix="/api/v1/neurobiologi/grp78_bip", tags=["neurobiologia_molecular"])
router_hat_mental = APIRouter(prefix="/api/v1/neurobiologi/hat_mental", tags=["neurobiologia_molecular"])
router_hdac_mental = APIRouter(prefix="/api/v1/neurobiologi/hdac_mental", tags=["neurobiologia_molecular"])
router_heat_shock_protein = APIRouter(prefix="/api/v1/neurobiologi/heat_shock_protein", tags=["neurobiologia_molecular"])
router_histamine_receptor = APIRouter(prefix="/api/v1/neurobiologi/histamine_receptor", tags=["neurobiologia_molecular"])
router_huntingtin = APIRouter(prefix="/api/v1/neurobiologi/huntingtin", tags=["neurobiologia_molecular"])
router_interferon_signaling = APIRouter(prefix="/api/v1/neurobiologi/interferon_signaling", tags=["neurobiologia_molecular"])
router_ire1_pathway = APIRouter(prefix="/api/v1/neurobiologi/ire1_pathway", tags=["neurobiologia_molecular"])
router_kainate_receptor = APIRouter(prefix="/api/v1/neurobiologi/kainate_receptor", tags=["neurobiologia_molecular"])
router_lc3_autophagy = APIRouter(prefix="/api/v1/neurobiologi/lc3_autophagy", tags=["neurobiologia_molecular"])
router_melatonin_receptor = APIRouter(prefix="/api/v1/neurobiologi/melatonin_receptor", tags=["neurobiologia_molecular"])
router_methylation_reader = APIRouter(prefix="/api/v1/neurobiologi/methylation_reader", tags=["neurobiologia_molecular"])
router_mineralocorticoid_re = APIRouter(prefix="/api/v1/neurobiologi/mineralocorticoid_recepto", tags=["neurobiologia_molecular"])
router_mitophagy = APIRouter(prefix="/api/v1/neurobiologi/mitophagy", tags=["neurobiologia_molecular"])
router_mtorc1_autophagy = APIRouter(prefix="/api/v1/neurobiologi/mtorc1_autophagy", tags=["neurobiologia_molecular"])
router_muscarinic_receptor = APIRouter(prefix="/api/v1/neurobiologi/muscarinic_receptor", tags=["neurobiologia_molecular"])
router_nfkb_pathway = APIRouter(prefix="/api/v1/neurobiologi/nfkb_pathway", tags=["neurobiologia_molecular"])
router_nicotinic_receptor = APIRouter(prefix="/api/v1/neurobiologi/nicotinic_receptor", tags=["neurobiologia_molecular"])
router_nlrp3_inflammasome = APIRouter(prefix="/api/v1/neurobiologi/nlrp3_inflammasome", tags=["neurobiologia_molecular"])
router_nmda_receptor = APIRouter(prefix="/api/v1/neurobiologi/nmda_receptor", tags=["neurobiologia_molecular"])
router_norepinephrine_recep = APIRouter(prefix="/api/v1/neurobiologi/norepinephrine_receptor", tags=["neurobiologia_molecular"])
router_opioid_receptor = APIRouter(prefix="/api/v1/neurobiologi/opioid_receptor", tags=["neurobiologia_molecular"])
router_p62_mental = APIRouter(prefix="/api/v1/neurobiologi/p62_mental", tags=["neurobiologia_molecular"])
router_p97_aaa = APIRouter(prefix="/api/v1/neurobiologi/p97_aaa", tags=["neurobiologia_molecular"])
router_pdi_mental = APIRouter(prefix="/api/v1/neurobiologi/pdi_mental", tags=["neurobiologia_molecular"])
router_perk_pathway = APIRouter(prefix="/api/v1/neurobiologi/perk_pathway", tags=["neurobiologia_molecular"])
router_phosphatase = APIRouter(prefix="/api/v1/neurobiologi/phosphatase", tags=["neurobiologia_molecular"])
router_phosphorylation_read = APIRouter(prefix="/api/v1/neurobiologi/phosphorylation_reader", tags=["neurobiologia_molecular"])
router_prion_mental = APIRouter(prefix="/api/v1/neurobiologi/prion_mental", tags=["neurobiologia_molecular"])
router_progesterone_recepto = APIRouter(prefix="/api/v1/neurobiologi/progesterone_receptor", tags=["neurobiologia_molecular"])
router_protein_disulfide = APIRouter(prefix="/api/v1/neurobiologi/protein_disulfide", tags=["neurobiologia_molecular"])
router_receptor_ionotropico = APIRouter(prefix="/api/v1/neurobiologi/receptor_ionotropico", tags=["neurobiologia_molecular"])
router_receptor_metabotropi = APIRouter(prefix="/api/v1/neurobiologi/receptor_metabotropico", tags=["neurobiologia_molecular"])
router_retinoic_acid_recept = APIRouter(prefix="/api/v1/neurobiologi/retinoic_acid_receptor", tags=["neurobiologia_molecular"])
router_sequestosome = APIRouter(prefix="/api/v1/neurobiologi/sequestosome", tags=["neurobiologia_molecular"])
router_serine_threonine_kin = APIRouter(prefix="/api/v1/neurobiologi/serine_threonine_kinase", tags=["neurobiologia_molecular"])
router_serotonin_receptor = APIRouter(prefix="/api/v1/neurobiologi/serotonin_receptor", tags=["neurobiologia_molecular"])
router_sigma_receptor = APIRouter(prefix="/api/v1/neurobiologi/sigma_receptor", tags=["neurobiologia_molecular"])
router_sirt1_mental = APIRouter(prefix="/api/v1/neurobiologi/sirt1_mental", tags=["neurobiologia_molecular"])
router_sirtuin_mental = APIRouter(prefix="/api/v1/neurobiologi/sirtuin_mental", tags=["neurobiologia_molecular"])
router_tau_phosphorylation = APIRouter(prefix="/api/v1/neurobiologi/tau_phosphorylation", tags=["neurobiologia_molecular"])
router_tdp43 = APIRouter(prefix="/api/v1/neurobiologi/tdp43", tags=["neurobiologia_molecular"])
router_tet_enzyme = APIRouter(prefix="/api/v1/neurobiologi/tet_enzyme", tags=["neurobiologia_molecular"])
router_thyroid_receptor = APIRouter(prefix="/api/v1/neurobiologi/thyroid_receptor", tags=["neurobiologia_molecular"])
router_toll_like_receptor = APIRouter(prefix="/api/v1/neurobiologi/toll_like_receptor", tags=["neurobiologia_molecular"])
router_tyrosine_kinase = APIRouter(prefix="/api/v1/neurobiologi/tyrosine_kinase", tags=["neurobiologia_molecular"])
router_ubiquilin = APIRouter(prefix="/api/v1/neurobiologi/ubiquilin", tags=["neurobiologia_molecular"])
router_ubiquitin_proteasome = APIRouter(prefix="/api/v1/neurobiologi/ubiquitin_proteasome", tags=["neurobiologia_molecular"])
router_ubiquitin_reader = APIRouter(prefix="/api/v1/neurobiologi/ubiquitin_reader", tags=["neurobiologia_molecular"])
router_ulk1_mental = APIRouter(prefix="/api/v1/neurobiologi/ulk1_mental", tags=["neurobiologia_molecular"])
router_unfolded_protein = APIRouter(prefix="/api/v1/neurobiologi/unfolded_protein", tags=["neurobiologia_molecular"])
router_valosin = APIRouter(prefix="/api/v1/neurobiologi/valosin", tags=["neurobiologia_molecular"])
router_vitamin_d_receptor = APIRouter(prefix="/api/v1/neurobiologi/vitamin_d_receptor", tags=["neurobiologia_molecular"])
router_xbp1_splicing = APIRouter(prefix="/api/v1/neurobiologi/xbp1_splicing", tags=["neurobiologia_molecular"])

@router_acetylation_reader.get("")
async def i_acetylation_reader():
    return {"p":"neurobiologia_m_acetylation_reader","s":"ativo","t":datetime.utcnow().isoformat()}
@router_adenosine_receptor.get("")
async def i_adenosine_receptor():
    return {"p":"neurobiologia_m_adenosine_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_alpha_synuclein.get("")
async def i_alpha_synuclein():
    return {"p":"neurobiologia_m_alpha_synuclein","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ampa_receptor.get("")
async def i_ampa_receptor():
    return {"p":"neurobiologia_m_ampa_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ampk_autophagy.get("")
async def i_ampk_autophagy():
    return {"p":"neurobiologia_m_ampk_autophagy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_amyloid_precursor.get("")
async def i_amyloid_precursor():
    return {"p":"neurobiologia_m_amyloid_precursor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_androgen_receptor.get("")
async def i_androgen_receptor():
    return {"p":"neurobiologia_m_androgen_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_aryl_hydrocarbon.get("")
async def i_aryl_hydrocarbon():
    return {"p":"neurobiologia_m_aryl_hydrocarbon","s":"ativo","t":datetime.utcnow().isoformat()}
@router_atf4_translation.get("")
async def i_atf4_translation():
    return {"p":"neurobiologia_m_atf4_translation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_atf6_pathway.get("")
async def i_atf6_pathway():
    return {"p":"neurobiologia_m_atf6_pathway","s":"ativo","t":datetime.utcnow().isoformat()}
@router_atg5_mental.get("")
async def i_atg5_mental():
    return {"p":"neurobiologia_m_atg5_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_atg7_mental.get("")
async def i_atg7_mental():
    return {"p":"neurobiologia_m_atg7_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autophagy_mental.get("")
async def i_autophagy_mental():
    return {"p":"neurobiologia_m_autophagy_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_beclin1.get("")
async def i_beclin1():
    return {"p":"neurobiologia_m_beclin1","s":"ativo","t":datetime.utcnow().isoformat()}
@router_calnexin.get("")
async def i_calnexin():
    return {"p":"neurobiologia_m_calnexin","s":"ativo","t":datetime.utcnow().isoformat()}
@router_calreticulin.get("")
async def i_calreticulin():
    return {"p":"neurobiologia_m_calreticulin","s":"ativo","t":datetime.utcnow().isoformat()}
@router_canal_calcio.get("")
async def i_canal_calcio():
    return {"p":"neurobiologia_m_canal_calcio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_canal_cloreto.get("")
async def i_canal_cloreto():
    return {"p":"neurobiologia_m_canal_cloreto","s":"ativo","t":datetime.utcnow().isoformat()}
@router_canal_ionico.get("")
async def i_canal_ionico():
    return {"p":"neurobiologia_m_canal_ionico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_canal_potassio.get("")
async def i_canal_potassio():
    return {"p":"neurobiologia_m_canal_potassio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_canal_sodio.get("")
async def i_canal_sodio():
    return {"p":"neurobiologia_m_canal_sodio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cannabinoid_receptor.get("")
async def i_cannabinoid_receptor():
    return {"p":"neurobiologia_m_cannabinoid_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_chaperone.get("")
async def i_chaperone():
    return {"p":"neurobiologia_m_chaperone","s":"ativo","t":datetime.utcnow().isoformat()}
@router_chemokine_receptor.get("")
async def i_chemokine_receptor():
    return {"p":"neurobiologia_m_chemokine_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_chop_ddit3.get("")
async def i_chop_ddit3():
    return {"p":"neurobiologia_m_chop_ddit3","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cytokine_receptor.get("")
async def i_cytokine_receptor():
    return {"p":"neurobiologia_m_cytokine_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_derlin.get("")
async def i_derlin():
    return {"p":"neurobiologia_m_derlin","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dnmt_mental.get("")
async def i_dnmt_mental():
    return {"p":"neurobiologia_m_dnmt_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dopamine_receptor.get("")
async def i_dopamine_receptor():
    return {"p":"neurobiologia_m_dopamine_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_endoplasmic_reticulu.get("")
async def i_endoplasmic_reticulu():
    return {"p":"neurobiologia_m_endoplasmic_reticulu","s":"ativo","t":datetime.utcnow().isoformat()}
@router_er_stress.get("")
async def i_er_stress():
    return {"p":"neurobiologia_m_er_stress","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ero1_mental.get("")
async def i_ero1_mental():
    return {"p":"neurobiologia_m_ero1_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_estrogen_receptor.get("")
async def i_estrogen_receptor():
    return {"p":"neurobiologia_m_estrogen_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fus_mental.get("")
async def i_fus_mental():
    return {"p":"neurobiologia_m_fus_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gabaa_receptor.get("")
async def i_gabaa_receptor():
    return {"p":"neurobiologia_m_gabaa_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gabab_receptor.get("")
async def i_gabab_receptor():
    return {"p":"neurobiologia_m_gabab_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_glucocorticoid_recep.get("")
async def i_glucocorticoid_recep():
    return {"p":"neurobiologia_m_glucocorticoid_recep","s":"ativo","t":datetime.utcnow().isoformat()}
@router_glycine_receptor.get("")
async def i_glycine_receptor():
    return {"p":"neurobiologia_m_glycine_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_growth_factor_recept.get("")
async def i_growth_factor_recept():
    return {"p":"neurobiologia_m_growth_factor_recept","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grp78_bip.get("")
async def i_grp78_bip():
    return {"p":"neurobiologia_m_grp78_bip","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hat_mental.get("")
async def i_hat_mental():
    return {"p":"neurobiologia_m_hat_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hdac_mental.get("")
async def i_hdac_mental():
    return {"p":"neurobiologia_m_hdac_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_heat_shock_protein.get("")
async def i_heat_shock_protein():
    return {"p":"neurobiologia_m_heat_shock_protein","s":"ativo","t":datetime.utcnow().isoformat()}
@router_histamine_receptor.get("")
async def i_histamine_receptor():
    return {"p":"neurobiologia_m_histamine_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_huntingtin.get("")
async def i_huntingtin():
    return {"p":"neurobiologia_m_huntingtin","s":"ativo","t":datetime.utcnow().isoformat()}
@router_interferon_signaling.get("")
async def i_interferon_signaling():
    return {"p":"neurobiologia_m_interferon_signaling","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ire1_pathway.get("")
async def i_ire1_pathway():
    return {"p":"neurobiologia_m_ire1_pathway","s":"ativo","t":datetime.utcnow().isoformat()}
@router_kainate_receptor.get("")
async def i_kainate_receptor():
    return {"p":"neurobiologia_m_kainate_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lc3_autophagy.get("")
async def i_lc3_autophagy():
    return {"p":"neurobiologia_m_lc3_autophagy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_melatonin_receptor.get("")
async def i_melatonin_receptor():
    return {"p":"neurobiologia_m_melatonin_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_methylation_reader.get("")
async def i_methylation_reader():
    return {"p":"neurobiologia_m_methylation_reader","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mineralocorticoid_re.get("")
async def i_mineralocorticoid_re():
    return {"p":"neurobiologia_m_mineralocorticoid_re","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mitophagy.get("")
async def i_mitophagy():
    return {"p":"neurobiologia_m_mitophagy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mtorc1_autophagy.get("")
async def i_mtorc1_autophagy():
    return {"p":"neurobiologia_m_mtorc1_autophagy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_muscarinic_receptor.get("")
async def i_muscarinic_receptor():
    return {"p":"neurobiologia_m_muscarinic_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nfkb_pathway.get("")
async def i_nfkb_pathway():
    return {"p":"neurobiologia_m_nfkb_pathway","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nicotinic_receptor.get("")
async def i_nicotinic_receptor():
    return {"p":"neurobiologia_m_nicotinic_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nlrp3_inflammasome.get("")
async def i_nlrp3_inflammasome():
    return {"p":"neurobiologia_m_nlrp3_inflammasome","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nmda_receptor.get("")
async def i_nmda_receptor():
    return {"p":"neurobiologia_m_nmda_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_norepinephrine_recep.get("")
async def i_norepinephrine_recep():
    return {"p":"neurobiologia_m_norepinephrine_recep","s":"ativo","t":datetime.utcnow().isoformat()}
@router_opioid_receptor.get("")
async def i_opioid_receptor():
    return {"p":"neurobiologia_m_opioid_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_p62_mental.get("")
async def i_p62_mental():
    return {"p":"neurobiologia_m_p62_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_p97_aaa.get("")
async def i_p97_aaa():
    return {"p":"neurobiologia_m_p97_aaa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pdi_mental.get("")
async def i_pdi_mental():
    return {"p":"neurobiologia_m_pdi_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_perk_pathway.get("")
async def i_perk_pathway():
    return {"p":"neurobiologia_m_perk_pathway","s":"ativo","t":datetime.utcnow().isoformat()}
@router_phosphatase.get("")
async def i_phosphatase():
    return {"p":"neurobiologia_m_phosphatase","s":"ativo","t":datetime.utcnow().isoformat()}
@router_phosphorylation_read.get("")
async def i_phosphorylation_read():
    return {"p":"neurobiologia_m_phosphorylation_read","s":"ativo","t":datetime.utcnow().isoformat()}
@router_prion_mental.get("")
async def i_prion_mental():
    return {"p":"neurobiologia_m_prion_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_progesterone_recepto.get("")
async def i_progesterone_recepto():
    return {"p":"neurobiologia_m_progesterone_recepto","s":"ativo","t":datetime.utcnow().isoformat()}
@router_protein_disulfide.get("")
async def i_protein_disulfide():
    return {"p":"neurobiologia_m_protein_disulfide","s":"ativo","t":datetime.utcnow().isoformat()}
@router_receptor_ionotropico.get("")
async def i_receptor_ionotropico():
    return {"p":"neurobiologia_m_receptor_ionotropico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_receptor_metabotropi.get("")
async def i_receptor_metabotropi():
    return {"p":"neurobiologia_m_receptor_metabotropi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_retinoic_acid_recept.get("")
async def i_retinoic_acid_recept():
    return {"p":"neurobiologia_m_retinoic_acid_recept","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sequestosome.get("")
async def i_sequestosome():
    return {"p":"neurobiologia_m_sequestosome","s":"ativo","t":datetime.utcnow().isoformat()}
@router_serine_threonine_kin.get("")
async def i_serine_threonine_kin():
    return {"p":"neurobiologia_m_serine_threonine_kin","s":"ativo","t":datetime.utcnow().isoformat()}
@router_serotonin_receptor.get("")
async def i_serotonin_receptor():
    return {"p":"neurobiologia_m_serotonin_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sigma_receptor.get("")
async def i_sigma_receptor():
    return {"p":"neurobiologia_m_sigma_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sirt1_mental.get("")
async def i_sirt1_mental():
    return {"p":"neurobiologia_m_sirt1_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sirtuin_mental.get("")
async def i_sirtuin_mental():
    return {"p":"neurobiologia_m_sirtuin_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tau_phosphorylation.get("")
async def i_tau_phosphorylation():
    return {"p":"neurobiologia_m_tau_phosphorylation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tdp43.get("")
async def i_tdp43():
    return {"p":"neurobiologia_m_tdp43","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tet_enzyme.get("")
async def i_tet_enzyme():
    return {"p":"neurobiologia_m_tet_enzyme","s":"ativo","t":datetime.utcnow().isoformat()}
@router_thyroid_receptor.get("")
async def i_thyroid_receptor():
    return {"p":"neurobiologia_m_thyroid_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_toll_like_receptor.get("")
async def i_toll_like_receptor():
    return {"p":"neurobiologia_m_toll_like_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tyrosine_kinase.get("")
async def i_tyrosine_kinase():
    return {"p":"neurobiologia_m_tyrosine_kinase","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ubiquilin.get("")
async def i_ubiquilin():
    return {"p":"neurobiologia_m_ubiquilin","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ubiquitin_proteasome.get("")
async def i_ubiquitin_proteasome():
    return {"p":"neurobiologia_m_ubiquitin_proteasome","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ubiquitin_reader.get("")
async def i_ubiquitin_reader():
    return {"p":"neurobiologia_m_ubiquitin_reader","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ulk1_mental.get("")
async def i_ulk1_mental():
    return {"p":"neurobiologia_m_ulk1_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_unfolded_protein.get("")
async def i_unfolded_protein():
    return {"p":"neurobiologia_m_unfolded_protein","s":"ativo","t":datetime.utcnow().isoformat()}
@router_valosin.get("")
async def i_valosin():
    return {"p":"neurobiologia_m_valosin","s":"ativo","t":datetime.utcnow().isoformat()}
@router_vitamin_d_receptor.get("")
async def i_vitamin_d_receptor():
    return {"p":"neurobiologia_m_vitamin_d_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_xbp1_splicing.get("")
async def i_xbp1_splicing():
    return {"p":"neurobiologia_m_xbp1_splicing","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_neurobiologia_molecu(PluginBase):
    name = "consolidated_neurobiologia_molecular"
    def setup(self, app):
        app.include_router(router_acetylation_reader)
        app.include_router(router_adenosine_receptor)
        app.include_router(router_alpha_synuclein)
        app.include_router(router_ampa_receptor)
        app.include_router(router_ampk_autophagy)
        app.include_router(router_amyloid_precursor)
        app.include_router(router_androgen_receptor)
        app.include_router(router_aryl_hydrocarbon)
        app.include_router(router_atf4_translation)
        app.include_router(router_atf6_pathway)
        app.include_router(router_atg5_mental)
        app.include_router(router_atg7_mental)
        app.include_router(router_autophagy_mental)
        app.include_router(router_beclin1)
        app.include_router(router_calnexin)
        app.include_router(router_calreticulin)
        app.include_router(router_canal_calcio)
        app.include_router(router_canal_cloreto)
        app.include_router(router_canal_ionico)
        app.include_router(router_canal_potassio)
        app.include_router(router_canal_sodio)
        app.include_router(router_cannabinoid_receptor)
        app.include_router(router_chaperone)
        app.include_router(router_chemokine_receptor)
        app.include_router(router_chop_ddit3)
        app.include_router(router_cytokine_receptor)
        app.include_router(router_derlin)
        app.include_router(router_dnmt_mental)
        app.include_router(router_dopamine_receptor)
        app.include_router(router_endoplasmic_reticulu)
        app.include_router(router_er_stress)
        app.include_router(router_ero1_mental)
        app.include_router(router_estrogen_receptor)
        app.include_router(router_fus_mental)
        app.include_router(router_gabaa_receptor)
        app.include_router(router_gabab_receptor)
        app.include_router(router_glucocorticoid_recep)
        app.include_router(router_glycine_receptor)
        app.include_router(router_growth_factor_recept)
        app.include_router(router_grp78_bip)
        app.include_router(router_hat_mental)
        app.include_router(router_hdac_mental)
        app.include_router(router_heat_shock_protein)
        app.include_router(router_histamine_receptor)
        app.include_router(router_huntingtin)
        app.include_router(router_interferon_signaling)
        app.include_router(router_ire1_pathway)
        app.include_router(router_kainate_receptor)
        app.include_router(router_lc3_autophagy)
        app.include_router(router_melatonin_receptor)
        app.include_router(router_methylation_reader)
        app.include_router(router_mineralocorticoid_re)
        app.include_router(router_mitophagy)
        app.include_router(router_mtorc1_autophagy)
        app.include_router(router_muscarinic_receptor)
        app.include_router(router_nfkb_pathway)
        app.include_router(router_nicotinic_receptor)
        app.include_router(router_nlrp3_inflammasome)
        app.include_router(router_nmda_receptor)
        app.include_router(router_norepinephrine_recep)
        app.include_router(router_opioid_receptor)
        app.include_router(router_p62_mental)
        app.include_router(router_p97_aaa)
        app.include_router(router_pdi_mental)
        app.include_router(router_perk_pathway)
        app.include_router(router_phosphatase)
        app.include_router(router_phosphorylation_read)
        app.include_router(router_prion_mental)
        app.include_router(router_progesterone_recepto)
        app.include_router(router_protein_disulfide)
        app.include_router(router_receptor_ionotropico)
        app.include_router(router_receptor_metabotropi)
        app.include_router(router_retinoic_acid_recept)
        app.include_router(router_sequestosome)
        app.include_router(router_serine_threonine_kin)
        app.include_router(router_serotonin_receptor)
        app.include_router(router_sigma_receptor)
        app.include_router(router_sirt1_mental)
        app.include_router(router_sirtuin_mental)
        app.include_router(router_tau_phosphorylation)
        app.include_router(router_tdp43)
        app.include_router(router_tet_enzyme)
        app.include_router(router_thyroid_receptor)
        app.include_router(router_toll_like_receptor)
        app.include_router(router_tyrosine_kinase)
        app.include_router(router_ubiquilin)
        app.include_router(router_ubiquitin_proteasome)
        app.include_router(router_ubiquitin_reader)
        app.include_router(router_ulk1_mental)
        app.include_router(router_unfolded_protein)
        app.include_router(router_valosin)
        app.include_router(router_vitamin_d_receptor)
        app.include_router(router_xbp1_splicing)


plugin = Plugin_neurobiologia_molecu()
