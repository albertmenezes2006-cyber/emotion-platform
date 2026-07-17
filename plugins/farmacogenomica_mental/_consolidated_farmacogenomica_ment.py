from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_22q11_deletion = APIRouter(prefix="/api/v1/farmacogenom/22q11_deletion", tags=["farmacogenomica_mental"])
router_actionable_variants = APIRouter(prefix="/api/v1/farmacogenom/actionable_variants", tags=["farmacogenomica_mental"])
router_adoption_studies = APIRouter(prefix="/api/v1/farmacogenom/adoption_studies", tags=["farmacogenomica_mental"])
router_analgesic_genetics = APIRouter(prefix="/api/v1/farmacogenom/analgesic_genetics", tags=["farmacogenomica_mental"])
router_angelman_syndrome = APIRouter(prefix="/api/v1/farmacogenom/angelman_syndrome", tags=["farmacogenomica_mental"])
router_antipsychotic_geneti = APIRouter(prefix="/api/v1/farmacogenom/antipsychotic_genetics", tags=["farmacogenomica_mental"])
router_bdnf_val66met = APIRouter(prefix="/api/v1/farmacogenom/bdnf_val66met", tags=["farmacogenomica_mental"])
router_benzodiazepine_genet = APIRouter(prefix="/api/v1/farmacogenom/benzodiazepine_genetics", tags=["farmacogenomica_mental"])
router_biomarker_mental = APIRouter(prefix="/api/v1/farmacogenom/biomarker_mental", tags=["farmacogenomica_mental"])
router_chromatin_remodeling = APIRouter(prefix="/api/v1/farmacogenom/chromatin_remodeling", tags=["farmacogenomica_mental"])
router_cns_doseguide = APIRouter(prefix="/api/v1/farmacogenom/cns_doseguide", tags=["farmacogenomica_mental"])
router_cntnap2_autism = APIRouter(prefix="/api/v1/farmacogenom/cntnap2_autism", tags=["farmacogenomica_mental"])
router_comt_gene = APIRouter(prefix="/api/v1/farmacogenom/comt_gene", tags=["farmacogenomica_mental"])
router_copy_number_variant = APIRouter(prefix="/api/v1/farmacogenom/copy_number_variant", tags=["farmacogenomica_mental"])
router_cyp1a2_mental = APIRouter(prefix="/api/v1/farmacogenom/cyp1a2_mental", tags=["farmacogenomica_mental"])
router_cyp2c19_mental = APIRouter(prefix="/api/v1/farmacogenom/cyp2c19_mental", tags=["farmacogenomica_mental"])
router_cyp2d6_mental = APIRouter(prefix="/api/v1/farmacogenom/cyp2d6_mental", tags=["farmacogenomica_mental"])
router_cyp3a4_mental = APIRouter(prefix="/api/v1/farmacogenom/cyp3a4_mental", tags=["farmacogenomica_mental"])
router_cytochrome_p450 = APIRouter(prefix="/api/v1/farmacogenom/cytochrome_p450", tags=["farmacogenomica_mental"])
router_dat_gene = APIRouter(prefix="/api/v1/farmacogenom/dat_gene", tags=["farmacogenomica_mental"])
router_de_novo_mutation = APIRouter(prefix="/api/v1/farmacogenom/de_novo_mutation", tags=["farmacogenomica_mental"])
router_dimensional_genetics = APIRouter(prefix="/api/v1/farmacogenom/dimensional_genetics", tags=["farmacogenomica_mental"])
router_dna_methylation_ment = APIRouter(prefix="/api/v1/farmacogenom/dna_methylation_mental", tags=["farmacogenomica_mental"])
router_down_syndrome_mental = APIRouter(prefix="/api/v1/farmacogenom/down_syndrome_mental", tags=["farmacogenomica_mental"])
router_drd2_receptor = APIRouter(prefix="/api/v1/farmacogenom/drd2_receptor", tags=["farmacogenomica_mental"])
router_drd4_receptor = APIRouter(prefix="/api/v1/farmacogenom/drd4_receptor", tags=["farmacogenomica_mental"])
router_drug_drug_interactio = APIRouter(prefix="/api/v1/farmacogenom/drug_drug_interaction", tags=["farmacogenomica_mental"])
router_endophenotype = APIRouter(prefix="/api/v1/farmacogenom/endophenotype", tags=["farmacogenomica_mental"])
router_epigenomics_mental = APIRouter(prefix="/api/v1/farmacogenom/epigenomics_mental", tags=["farmacogenomica_mental"])
router_family_studies = APIRouter(prefix="/api/v1/farmacogenom/family_studies", tags=["farmacogenomica_mental"])
router_fmr1_fragile = APIRouter(prefix="/api/v1/farmacogenom/fmr1_fragile", tags=["farmacogenomica_mental"])
router_gabrb3_mental = APIRouter(prefix="/api/v1/farmacogenom/gabrb3_mental", tags=["farmacogenomica_mental"])
router_genesight_test = APIRouter(prefix="/api/v1/farmacogenom/genesight_test", tags=["farmacogenomica_mental"])
router_genomic_psychiatry = APIRouter(prefix="/api/v1/farmacogenom/genomic_psychiatry", tags=["farmacogenomica_mental"])
router_genomind_test = APIRouter(prefix="/api/v1/farmacogenom/genomind_test", tags=["farmacogenomica_mental"])
router_grik1_grik2 = APIRouter(prefix="/api/v1/farmacogenom/grik1_grik2", tags=["farmacogenomica_mental"])
router_grin2a_grin2b = APIRouter(prefix="/api/v1/farmacogenom/grin2a_grin2b", tags=["farmacogenomica_mental"])
router_gwas_mental = APIRouter(prefix="/api/v1/farmacogenom/gwas_mental", tags=["farmacogenomica_mental"])
router_half_life = APIRouter(prefix="/api/v1/farmacogenom/half_life", tags=["farmacogenomica_mental"])
router_heritability_mental = APIRouter(prefix="/api/v1/farmacogenom/heritability_mental", tags=["farmacogenomica_mental"])
router_histone_modification = APIRouter(prefix="/api/v1/farmacogenom/histone_modification", tags=["farmacogenomica_mental"])
router_htr2a_receptor = APIRouter(prefix="/api/v1/farmacogenom/htr2a_receptor", tags=["farmacogenomica_mental"])
router_imaging_genomics = APIRouter(prefix="/api/v1/farmacogenom/imaging_genomics", tags=["farmacogenomica_mental"])
router_inherited_variant = APIRouter(prefix="/api/v1/farmacogenom/inherited_variant", tags=["farmacogenomica_mental"])
router_intermediate_phenoty = APIRouter(prefix="/api/v1/farmacogenom/intermediate_phenotype", tags=["farmacogenomica_mental"])
router_interpretome_mental = APIRouter(prefix="/api/v1/farmacogenom/interpretome_mental", tags=["farmacogenomica_mental"])
router_liquid_biopsy_mental = APIRouter(prefix="/api/v1/farmacogenom/liquid_biopsy_mental", tags=["farmacogenomica_mental"])
router_lncRNA_mental = APIRouter(prefix="/api/v1/farmacogenom/lncRNA_mental", tags=["farmacogenomica_mental"])
router_loading_dose = APIRouter(prefix="/api/v1/farmacogenom/loading_dose", tags=["farmacogenomica_mental"])
router_maoa_maob = APIRouter(prefix="/api/v1/farmacogenom/maoa_maob", tags=["farmacogenomica_mental"])
router_mecp2_rett = APIRouter(prefix="/api/v1/farmacogenom/mecp2_rett", tags=["farmacogenomica_mental"])
router_metabolism_interacti = APIRouter(prefix="/api/v1/farmacogenom/metabolism_interactions", tags=["farmacogenomica_mental"])
router_metabolomics_mental = APIRouter(prefix="/api/v1/farmacogenom/metabolomics_mental", tags=["farmacogenomica_mental"])
router_microRNA_mental = APIRouter(prefix="/api/v1/farmacogenom/microRNA_mental", tags=["farmacogenomica_mental"])
router_mood_stabilizer_gene = APIRouter(prefix="/api/v1/farmacogenom/mood_stabilizer_genetics", tags=["farmacogenomica_mental"])
router_mthfr_mental = APIRouter(prefix="/api/v1/farmacogenom/mthfr_mental", tags=["farmacogenomica_mental"])
router_multi_omics_integrat = APIRouter(prefix="/api/v1/farmacogenom/multi_omics_integration", tags=["farmacogenomica_mental"])
router_net_gene = APIRouter(prefix="/api/v1/farmacogenom/net_gene", tags=["farmacogenomica_mental"])
router_neuroimaging_genetic = APIRouter(prefix="/api/v1/farmacogenom/neuroimaging_genetics", tags=["farmacogenomica_mental"])
router_non_coding_rna = APIRouter(prefix="/api/v1/farmacogenom/non_coding_rna", tags=["farmacogenomica_mental"])
router_nrxn1_autism = APIRouter(prefix="/api/v1/farmacogenom/nrxn1_autism", tags=["farmacogenomica_mental"])
router_pgp_transporter = APIRouter(prefix="/api/v1/farmacogenom/pgp_transporter", tags=["farmacogenomica_mental"])
router_pharmacogenomic_test = APIRouter(prefix="/api/v1/farmacogenom/pharmacogenomic_testing", tags=["farmacogenomica_mental"])
router_phelan_mcdermid = APIRouter(prefix="/api/v1/farmacogenom/phelan_mcdermid", tags=["farmacogenomica_mental"])
router_polygenic_risk = APIRouter(prefix="/api/v1/farmacogenom/polygenic_risk", tags=["farmacogenomica_mental"])
router_polypharmacy_genetic = APIRouter(prefix="/api/v1/farmacogenom/polypharmacy_genetics", tags=["farmacogenomica_mental"])
router_prader_willi = APIRouter(prefix="/api/v1/farmacogenom/prader_willi", tags=["farmacogenomica_mental"])
router_precision_medicine_m = APIRouter(prefix="/api/v1/farmacogenom/precision_medicine_mental", tags=["farmacogenomica_mental"])
router_promoter_5httlpr = APIRouter(prefix="/api/v1/farmacogenom/promoter_5httlpr", tags=["farmacogenomica_mental"])
router_protein_binding = APIRouter(prefix="/api/v1/farmacogenom/protein_binding", tags=["farmacogenomica_mental"])
router_proteomics_mental = APIRouter(prefix="/api/v1/farmacogenom/proteomics_mental", tags=["farmacogenomica_mental"])
router_rare_variant = APIRouter(prefix="/api/v1/farmacogenom/rare_variant", tags=["farmacogenomica_mental"])
router_rna_editing = APIRouter(prefix="/api/v1/farmacogenom/rna_editing", tags=["farmacogenomica_mental"])
router_serotonin_transporte = APIRouter(prefix="/api/v1/farmacogenom/serotonin_transporter_gen", tags=["farmacogenomica_mental"])
router_sert_gene = APIRouter(prefix="/api/v1/farmacogenom/sert_gene", tags=["farmacogenomica_mental"])
router_serum_levels = APIRouter(prefix="/api/v1/farmacogenom/serum_levels", tags=["farmacogenomica_mental"])
router_shank3_autism = APIRouter(prefix="/api/v1/farmacogenom/shank3_autism", tags=["farmacogenomica_mental"])
router_slc6a4_transporter = APIRouter(prefix="/api/v1/farmacogenom/slc6a4_transporter", tags=["farmacogenomica_mental"])
router_snp_mental = APIRouter(prefix="/api/v1/farmacogenom/snp_mental", tags=["farmacogenomica_mental"])
router_ssri_genetics = APIRouter(prefix="/api/v1/farmacogenom/ssri_genetics", tags=["farmacogenomica_mental"])
router_steady_state = APIRouter(prefix="/api/v1/farmacogenom/steady_state", tags=["farmacogenomica_mental"])
router_stimulant_genetics = APIRouter(prefix="/api/v1/farmacogenom/stimulant_genetics", tags=["farmacogenomica_mental"])
router_stxbp1_mental = APIRouter(prefix="/api/v1/farmacogenom/stxbp1_mental", tags=["farmacogenomica_mental"])
router_therapeutic_drug_mon = APIRouter(prefix="/api/v1/farmacogenom/therapeutic_drug_monitori", tags=["farmacogenomica_mental"])
router_tph1_tph2_serotonin = APIRouter(prefix="/api/v1/farmacogenom/tph1_tph2_serotonin", tags=["farmacogenomica_mental"])
router_transcriptomics_ment = APIRouter(prefix="/api/v1/farmacogenom/transcriptomics_mental", tags=["farmacogenomica_mental"])
router_tsc1_tsc2 = APIRouter(prefix="/api/v1/farmacogenom/tsc1_tsc2", tags=["farmacogenomica_mental"])
router_twin_studies_mental = APIRouter(prefix="/api/v1/farmacogenom/twin_studies_mental", tags=["farmacogenomica_mental"])
router_velocardiofacial = APIRouter(prefix="/api/v1/farmacogenom/velocardiofacial", tags=["farmacogenomica_mental"])
router_warfarin_genetics = APIRouter(prefix="/api/v1/farmacogenom/warfarin_genetics", tags=["farmacogenomica_mental"])
router_williams_syndrome = APIRouter(prefix="/api/v1/farmacogenom/williams_syndrome", tags=["farmacogenomica_mental"])

@router_22q11_deletion.get("")
async def i_22q11_deletion():
    return {"p":"farmacogenomica_22q11_deletion","s":"ativo","t":datetime.utcnow().isoformat()}
@router_actionable_variants.get("")
async def i_actionable_variants():
    return {"p":"farmacogenomica_actionable_variants","s":"ativo","t":datetime.utcnow().isoformat()}
@router_adoption_studies.get("")
async def i_adoption_studies():
    return {"p":"farmacogenomica_adoption_studies","s":"ativo","t":datetime.utcnow().isoformat()}
@router_analgesic_genetics.get("")
async def i_analgesic_genetics():
    return {"p":"farmacogenomica_analgesic_genetics","s":"ativo","t":datetime.utcnow().isoformat()}
@router_angelman_syndrome.get("")
async def i_angelman_syndrome():
    return {"p":"farmacogenomica_angelman_syndrome","s":"ativo","t":datetime.utcnow().isoformat()}
@router_antipsychotic_geneti.get("")
async def i_antipsychotic_geneti():
    return {"p":"farmacogenomica_antipsychotic_geneti","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bdnf_val66met.get("")
async def i_bdnf_val66met():
    return {"p":"farmacogenomica_bdnf_val66met","s":"ativo","t":datetime.utcnow().isoformat()}
@router_benzodiazepine_genet.get("")
async def i_benzodiazepine_genet():
    return {"p":"farmacogenomica_benzodiazepine_genet","s":"ativo","t":datetime.utcnow().isoformat()}
@router_biomarker_mental.get("")
async def i_biomarker_mental():
    return {"p":"farmacogenomica_biomarker_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_chromatin_remodeling.get("")
async def i_chromatin_remodeling():
    return {"p":"farmacogenomica_chromatin_remodeling","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cns_doseguide.get("")
async def i_cns_doseguide():
    return {"p":"farmacogenomica_cns_doseguide","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cntnap2_autism.get("")
async def i_cntnap2_autism():
    return {"p":"farmacogenomica_cntnap2_autism","s":"ativo","t":datetime.utcnow().isoformat()}
@router_comt_gene.get("")
async def i_comt_gene():
    return {"p":"farmacogenomica_comt_gene","s":"ativo","t":datetime.utcnow().isoformat()}
@router_copy_number_variant.get("")
async def i_copy_number_variant():
    return {"p":"farmacogenomica_copy_number_variant","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cyp1a2_mental.get("")
async def i_cyp1a2_mental():
    return {"p":"farmacogenomica_cyp1a2_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cyp2c19_mental.get("")
async def i_cyp2c19_mental():
    return {"p":"farmacogenomica_cyp2c19_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cyp2d6_mental.get("")
async def i_cyp2d6_mental():
    return {"p":"farmacogenomica_cyp2d6_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cyp3a4_mental.get("")
async def i_cyp3a4_mental():
    return {"p":"farmacogenomica_cyp3a4_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cytochrome_p450.get("")
async def i_cytochrome_p450():
    return {"p":"farmacogenomica_cytochrome_p450","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dat_gene.get("")
async def i_dat_gene():
    return {"p":"farmacogenomica_dat_gene","s":"ativo","t":datetime.utcnow().isoformat()}
@router_de_novo_mutation.get("")
async def i_de_novo_mutation():
    return {"p":"farmacogenomica_de_novo_mutation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dimensional_genetics.get("")
async def i_dimensional_genetics():
    return {"p":"farmacogenomica_dimensional_genetics","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dna_methylation_ment.get("")
async def i_dna_methylation_ment():
    return {"p":"farmacogenomica_dna_methylation_ment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_down_syndrome_mental.get("")
async def i_down_syndrome_mental():
    return {"p":"farmacogenomica_down_syndrome_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_drd2_receptor.get("")
async def i_drd2_receptor():
    return {"p":"farmacogenomica_drd2_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_drd4_receptor.get("")
async def i_drd4_receptor():
    return {"p":"farmacogenomica_drd4_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_drug_drug_interactio.get("")
async def i_drug_drug_interactio():
    return {"p":"farmacogenomica_drug_drug_interactio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_endophenotype.get("")
async def i_endophenotype():
    return {"p":"farmacogenomica_endophenotype","s":"ativo","t":datetime.utcnow().isoformat()}
@router_epigenomics_mental.get("")
async def i_epigenomics_mental():
    return {"p":"farmacogenomica_epigenomics_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_family_studies.get("")
async def i_family_studies():
    return {"p":"farmacogenomica_family_studies","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fmr1_fragile.get("")
async def i_fmr1_fragile():
    return {"p":"farmacogenomica_fmr1_fragile","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gabrb3_mental.get("")
async def i_gabrb3_mental():
    return {"p":"farmacogenomica_gabrb3_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_genesight_test.get("")
async def i_genesight_test():
    return {"p":"farmacogenomica_genesight_test","s":"ativo","t":datetime.utcnow().isoformat()}
@router_genomic_psychiatry.get("")
async def i_genomic_psychiatry():
    return {"p":"farmacogenomica_genomic_psychiatry","s":"ativo","t":datetime.utcnow().isoformat()}
@router_genomind_test.get("")
async def i_genomind_test():
    return {"p":"farmacogenomica_genomind_test","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grik1_grik2.get("")
async def i_grik1_grik2():
    return {"p":"farmacogenomica_grik1_grik2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grin2a_grin2b.get("")
async def i_grin2a_grin2b():
    return {"p":"farmacogenomica_grin2a_grin2b","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gwas_mental.get("")
async def i_gwas_mental():
    return {"p":"farmacogenomica_gwas_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_half_life.get("")
async def i_half_life():
    return {"p":"farmacogenomica_half_life","s":"ativo","t":datetime.utcnow().isoformat()}
@router_heritability_mental.get("")
async def i_heritability_mental():
    return {"p":"farmacogenomica_heritability_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_histone_modification.get("")
async def i_histone_modification():
    return {"p":"farmacogenomica_histone_modification","s":"ativo","t":datetime.utcnow().isoformat()}
@router_htr2a_receptor.get("")
async def i_htr2a_receptor():
    return {"p":"farmacogenomica_htr2a_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_imaging_genomics.get("")
async def i_imaging_genomics():
    return {"p":"farmacogenomica_imaging_genomics","s":"ativo","t":datetime.utcnow().isoformat()}
@router_inherited_variant.get("")
async def i_inherited_variant():
    return {"p":"farmacogenomica_inherited_variant","s":"ativo","t":datetime.utcnow().isoformat()}
@router_intermediate_phenoty.get("")
async def i_intermediate_phenoty():
    return {"p":"farmacogenomica_intermediate_phenoty","s":"ativo","t":datetime.utcnow().isoformat()}
@router_interpretome_mental.get("")
async def i_interpretome_mental():
    return {"p":"farmacogenomica_interpretome_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_liquid_biopsy_mental.get("")
async def i_liquid_biopsy_mental():
    return {"p":"farmacogenomica_liquid_biopsy_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lncRNA_mental.get("")
async def i_lncRNA_mental():
    return {"p":"farmacogenomica_lncRNA_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_loading_dose.get("")
async def i_loading_dose():
    return {"p":"farmacogenomica_loading_dose","s":"ativo","t":datetime.utcnow().isoformat()}
@router_maoa_maob.get("")
async def i_maoa_maob():
    return {"p":"farmacogenomica_maoa_maob","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mecp2_rett.get("")
async def i_mecp2_rett():
    return {"p":"farmacogenomica_mecp2_rett","s":"ativo","t":datetime.utcnow().isoformat()}
@router_metabolism_interacti.get("")
async def i_metabolism_interacti():
    return {"p":"farmacogenomica_metabolism_interacti","s":"ativo","t":datetime.utcnow().isoformat()}
@router_metabolomics_mental.get("")
async def i_metabolomics_mental():
    return {"p":"farmacogenomica_metabolomics_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_microRNA_mental.get("")
async def i_microRNA_mental():
    return {"p":"farmacogenomica_microRNA_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mood_stabilizer_gene.get("")
async def i_mood_stabilizer_gene():
    return {"p":"farmacogenomica_mood_stabilizer_gene","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mthfr_mental.get("")
async def i_mthfr_mental():
    return {"p":"farmacogenomica_mthfr_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_multi_omics_integrat.get("")
async def i_multi_omics_integrat():
    return {"p":"farmacogenomica_multi_omics_integrat","s":"ativo","t":datetime.utcnow().isoformat()}
@router_net_gene.get("")
async def i_net_gene():
    return {"p":"farmacogenomica_net_gene","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neuroimaging_genetic.get("")
async def i_neuroimaging_genetic():
    return {"p":"farmacogenomica_neuroimaging_genetic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_non_coding_rna.get("")
async def i_non_coding_rna():
    return {"p":"farmacogenomica_non_coding_rna","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nrxn1_autism.get("")
async def i_nrxn1_autism():
    return {"p":"farmacogenomica_nrxn1_autism","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pgp_transporter.get("")
async def i_pgp_transporter():
    return {"p":"farmacogenomica_pgp_transporter","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pharmacogenomic_test.get("")
async def i_pharmacogenomic_test():
    return {"p":"farmacogenomica_pharmacogenomic_test","s":"ativo","t":datetime.utcnow().isoformat()}
@router_phelan_mcdermid.get("")
async def i_phelan_mcdermid():
    return {"p":"farmacogenomica_phelan_mcdermid","s":"ativo","t":datetime.utcnow().isoformat()}
@router_polygenic_risk.get("")
async def i_polygenic_risk():
    return {"p":"farmacogenomica_polygenic_risk","s":"ativo","t":datetime.utcnow().isoformat()}
@router_polypharmacy_genetic.get("")
async def i_polypharmacy_genetic():
    return {"p":"farmacogenomica_polypharmacy_genetic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_prader_willi.get("")
async def i_prader_willi():
    return {"p":"farmacogenomica_prader_willi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_precision_medicine_m.get("")
async def i_precision_medicine_m():
    return {"p":"farmacogenomica_precision_medicine_m","s":"ativo","t":datetime.utcnow().isoformat()}
@router_promoter_5httlpr.get("")
async def i_promoter_5httlpr():
    return {"p":"farmacogenomica_promoter_5httlpr","s":"ativo","t":datetime.utcnow().isoformat()}
@router_protein_binding.get("")
async def i_protein_binding():
    return {"p":"farmacogenomica_protein_binding","s":"ativo","t":datetime.utcnow().isoformat()}
@router_proteomics_mental.get("")
async def i_proteomics_mental():
    return {"p":"farmacogenomica_proteomics_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_rare_variant.get("")
async def i_rare_variant():
    return {"p":"farmacogenomica_rare_variant","s":"ativo","t":datetime.utcnow().isoformat()}
@router_rna_editing.get("")
async def i_rna_editing():
    return {"p":"farmacogenomica_rna_editing","s":"ativo","t":datetime.utcnow().isoformat()}
@router_serotonin_transporte.get("")
async def i_serotonin_transporte():
    return {"p":"farmacogenomica_serotonin_transporte","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sert_gene.get("")
async def i_sert_gene():
    return {"p":"farmacogenomica_sert_gene","s":"ativo","t":datetime.utcnow().isoformat()}
@router_serum_levels.get("")
async def i_serum_levels():
    return {"p":"farmacogenomica_serum_levels","s":"ativo","t":datetime.utcnow().isoformat()}
@router_shank3_autism.get("")
async def i_shank3_autism():
    return {"p":"farmacogenomica_shank3_autism","s":"ativo","t":datetime.utcnow().isoformat()}
@router_slc6a4_transporter.get("")
async def i_slc6a4_transporter():
    return {"p":"farmacogenomica_slc6a4_transporter","s":"ativo","t":datetime.utcnow().isoformat()}
@router_snp_mental.get("")
async def i_snp_mental():
    return {"p":"farmacogenomica_snp_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ssri_genetics.get("")
async def i_ssri_genetics():
    return {"p":"farmacogenomica_ssri_genetics","s":"ativo","t":datetime.utcnow().isoformat()}
@router_steady_state.get("")
async def i_steady_state():
    return {"p":"farmacogenomica_steady_state","s":"ativo","t":datetime.utcnow().isoformat()}
@router_stimulant_genetics.get("")
async def i_stimulant_genetics():
    return {"p":"farmacogenomica_stimulant_genetics","s":"ativo","t":datetime.utcnow().isoformat()}
@router_stxbp1_mental.get("")
async def i_stxbp1_mental():
    return {"p":"farmacogenomica_stxbp1_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_therapeutic_drug_mon.get("")
async def i_therapeutic_drug_mon():
    return {"p":"farmacogenomica_therapeutic_drug_mon","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tph1_tph2_serotonin.get("")
async def i_tph1_tph2_serotonin():
    return {"p":"farmacogenomica_tph1_tph2_serotonin","s":"ativo","t":datetime.utcnow().isoformat()}
@router_transcriptomics_ment.get("")
async def i_transcriptomics_ment():
    return {"p":"farmacogenomica_transcriptomics_ment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tsc1_tsc2.get("")
async def i_tsc1_tsc2():
    return {"p":"farmacogenomica_tsc1_tsc2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_twin_studies_mental.get("")
async def i_twin_studies_mental():
    return {"p":"farmacogenomica_twin_studies_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_velocardiofacial.get("")
async def i_velocardiofacial():
    return {"p":"farmacogenomica_velocardiofacial","s":"ativo","t":datetime.utcnow().isoformat()}
@router_warfarin_genetics.get("")
async def i_warfarin_genetics():
    return {"p":"farmacogenomica_warfarin_genetics","s":"ativo","t":datetime.utcnow().isoformat()}
@router_williams_syndrome.get("")
async def i_williams_syndrome():
    return {"p":"farmacogenomica_williams_syndrome","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_farmacogenomica_ment(PluginBase):
    name = "consolidated_farmacogenomica_mental"
    def setup(self, app):
        app.include_router(router_22q11_deletion)
        app.include_router(router_actionable_variants)
        app.include_router(router_adoption_studies)
        app.include_router(router_analgesic_genetics)
        app.include_router(router_angelman_syndrome)
        app.include_router(router_antipsychotic_geneti)
        app.include_router(router_bdnf_val66met)
        app.include_router(router_benzodiazepine_genet)
        app.include_router(router_biomarker_mental)
        app.include_router(router_chromatin_remodeling)
        app.include_router(router_cns_doseguide)
        app.include_router(router_cntnap2_autism)
        app.include_router(router_comt_gene)
        app.include_router(router_copy_number_variant)
        app.include_router(router_cyp1a2_mental)
        app.include_router(router_cyp2c19_mental)
        app.include_router(router_cyp2d6_mental)
        app.include_router(router_cyp3a4_mental)
        app.include_router(router_cytochrome_p450)
        app.include_router(router_dat_gene)
        app.include_router(router_de_novo_mutation)
        app.include_router(router_dimensional_genetics)
        app.include_router(router_dna_methylation_ment)
        app.include_router(router_down_syndrome_mental)
        app.include_router(router_drd2_receptor)
        app.include_router(router_drd4_receptor)
        app.include_router(router_drug_drug_interactio)
        app.include_router(router_endophenotype)
        app.include_router(router_epigenomics_mental)
        app.include_router(router_family_studies)
        app.include_router(router_fmr1_fragile)
        app.include_router(router_gabrb3_mental)
        app.include_router(router_genesight_test)
        app.include_router(router_genomic_psychiatry)
        app.include_router(router_genomind_test)
        app.include_router(router_grik1_grik2)
        app.include_router(router_grin2a_grin2b)
        app.include_router(router_gwas_mental)
        app.include_router(router_half_life)
        app.include_router(router_heritability_mental)
        app.include_router(router_histone_modification)
        app.include_router(router_htr2a_receptor)
        app.include_router(router_imaging_genomics)
        app.include_router(router_inherited_variant)
        app.include_router(router_intermediate_phenoty)
        app.include_router(router_interpretome_mental)
        app.include_router(router_liquid_biopsy_mental)
        app.include_router(router_lncRNA_mental)
        app.include_router(router_loading_dose)
        app.include_router(router_maoa_maob)
        app.include_router(router_mecp2_rett)
        app.include_router(router_metabolism_interacti)
        app.include_router(router_metabolomics_mental)
        app.include_router(router_microRNA_mental)
        app.include_router(router_mood_stabilizer_gene)
        app.include_router(router_mthfr_mental)
        app.include_router(router_multi_omics_integrat)
        app.include_router(router_net_gene)
        app.include_router(router_neuroimaging_genetic)
        app.include_router(router_non_coding_rna)
        app.include_router(router_nrxn1_autism)
        app.include_router(router_pgp_transporter)
        app.include_router(router_pharmacogenomic_test)
        app.include_router(router_phelan_mcdermid)
        app.include_router(router_polygenic_risk)
        app.include_router(router_polypharmacy_genetic)
        app.include_router(router_prader_willi)
        app.include_router(router_precision_medicine_m)
        app.include_router(router_promoter_5httlpr)
        app.include_router(router_protein_binding)
        app.include_router(router_proteomics_mental)
        app.include_router(router_rare_variant)
        app.include_router(router_rna_editing)
        app.include_router(router_serotonin_transporte)
        app.include_router(router_sert_gene)
        app.include_router(router_serum_levels)
        app.include_router(router_shank3_autism)
        app.include_router(router_slc6a4_transporter)
        app.include_router(router_snp_mental)
        app.include_router(router_ssri_genetics)
        app.include_router(router_steady_state)
        app.include_router(router_stimulant_genetics)
        app.include_router(router_stxbp1_mental)
        app.include_router(router_therapeutic_drug_mon)
        app.include_router(router_tph1_tph2_serotonin)
        app.include_router(router_transcriptomics_ment)
        app.include_router(router_tsc1_tsc2)
        app.include_router(router_twin_studies_mental)
        app.include_router(router_velocardiofacial)
        app.include_router(router_warfarin_genetics)
        app.include_router(router_williams_syndrome)


plugin = Plugin_farmacogenomica_ment()
