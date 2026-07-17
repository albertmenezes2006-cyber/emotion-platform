from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_adamts_mental = APIRouter(prefix="/api/v1/neurogenomic/adamts_mental", tags=["neurogenomica_mental"])
router_calpain_mental = APIRouter(prefix="/api/v1/neurogenomic/calpain_mental", tags=["neurogenomica_mental"])
router_caspase_mental = APIRouter(prefix="/api/v1/neurogenomic/caspase_mental", tags=["neurogenomica_mental"])
router_cathepsin_mental = APIRouter(prefix="/api/v1/neurogenomic/cathepsin_mental", tags=["neurogenomica_mental"])
router_chromatin_accessibil = APIRouter(prefix="/api/v1/neurogenomic/chromatin_accessibility", tags=["neurogenomica_mental"])
router_clathrin = APIRouter(prefix="/api/v1/neurogenomic/clathrin", tags=["neurogenomica_mental"])
router_complexin = APIRouter(prefix="/api/v1/neurogenomic/complexin", tags=["neurogenomica_mental"])
router_copy_number_variatio = APIRouter(prefix="/api/v1/neurogenomic/copy_number_variation", tags=["neurogenomica_mental"])
router_cryo_electron = APIRouter(prefix="/api/v1/neurogenomic/cryo_electron", tags=["neurogenomica_mental"])
router_cullin_ring = APIRouter(prefix="/api/v1/neurogenomic/cullin_ring", tags=["neurogenomica_mental"])
router_deubiquitinase = APIRouter(prefix="/api/v1/neurogenomic/deubiquitinase", tags=["neurogenomica_mental"])
router_dynamin = APIRouter(prefix="/api/v1/neurogenomic/dynamin", tags=["neurogenomica_mental"])
router_elisa_mental = APIRouter(prefix="/api/v1/neurogenomic/elisa_mental", tags=["neurogenomica_mental"])
router_endocytosis_synaptic = APIRouter(prefix="/api/v1/neurogenomic/endocytosis_synaptic", tags=["neurogenomica_mental"])
router_endosome_mental = APIRouter(prefix="/api/v1/neurogenomic/endosome_mental", tags=["neurogenomica_mental"])
router_exocytosis_synaptic = APIRouter(prefix="/api/v1/neurogenomic/exocytosis_synaptic", tags=["neurogenomica_mental"])
router_expansion_microscopy = APIRouter(prefix="/api/v1/neurogenomic/expansion_microscopy", tags=["neurogenomica_mental"])
router_expression_quantitat = APIRouter(prefix="/api/v1/neurogenomic/expression_quantitative", tags=["neurogenomica_mental"])
router_fish_mental = APIRouter(prefix="/api/v1/neurogenomic/fish_mental", tags=["neurogenomica_mental"])
router_furin_mental = APIRouter(prefix="/api/v1/neurogenomic/furin_mental", tags=["neurogenomica_mental"])
router_genetic_risk_factor = APIRouter(prefix="/api/v1/neurogenomic/genetic_risk_factor", tags=["neurogenomica_mental"])
router_genome_wide_associat = APIRouter(prefix="/api/v1/neurogenomic/genome_wide_association", tags=["neurogenomica_mental"])
router_glycomics = APIRouter(prefix="/api/v1/neurogenomic/glycomics", tags=["neurogenomica_mental"])
router_glycoproteomics = APIRouter(prefix="/api/v1/neurogenomic/glycoproteomics", tags=["neurogenomica_mental"])
router_imaging_mass = APIRouter(prefix="/api/v1/neurogenomic/imaging_mass", tags=["neurogenomica_mental"])
router_immunofluorescence = APIRouter(prefix="/api/v1/neurogenomic/immunofluorescence", tags=["neurogenomica_mental"])
router_immunohistochemistry = APIRouter(prefix="/api/v1/neurogenomic/immunohistochemistry", tags=["neurogenomica_mental"])
router_in_situ_hybridizatio = APIRouter(prefix="/api/v1/neurogenomic/in_situ_hybridization", tags=["neurogenomica_mental"])
router_interactomics = APIRouter(prefix="/api/v1/neurogenomic/interactomics", tags=["neurogenomica_mental"])
router_kinomics = APIRouter(prefix="/api/v1/neurogenomic/kinomics", tags=["neurogenomica_mental"])
router_lipidomics = APIRouter(prefix="/api/v1/neurogenomic/lipidomics", tags=["neurogenomica_mental"])
router_lysosome_mental = APIRouter(prefix="/api/v1/neurogenomic/lysosome_mental", tags=["neurogenomica_mental"])
router_mass_cytometry = APIRouter(prefix="/api/v1/neurogenomic/mass_cytometry", tags=["neurogenomica_mental"])
router_mass_spectrometry_me = APIRouter(prefix="/api/v1/neurogenomic/mass_spectrometry_mental", tags=["neurogenomica_mental"])
router_matrix_metalloprotea = APIRouter(prefix="/api/v1/neurogenomic/matrix_metalloprotease", tags=["neurogenomica_mental"])
router_membrane_proteomics = APIRouter(prefix="/api/v1/neurogenomic/membrane_proteomics", tags=["neurogenomica_mental"])
router_metabolomics2 = APIRouter(prefix="/api/v1/neurogenomic/metabolomics2", tags=["neurogenomica_mental"])
router_methylation_quantita = APIRouter(prefix="/api/v1/neurogenomic/methylation_quantitative", tags=["neurogenomica_mental"])
router_microsatellite = APIRouter(prefix="/api/v1/neurogenomic/microsatellite", tags=["neurogenomica_mental"])
router_mitochondrial_proteo = APIRouter(prefix="/api/v1/neurogenomic/mitochondrial_proteomics", tags=["neurogenomica_mental"])
router_munc18 = APIRouter(prefix="/api/v1/neurogenomic/munc18", tags=["neurogenomica_mental"])
router_nedd8_mental = APIRouter(prefix="/api/v1/neurogenomic/nedd8_mental", tags=["neurogenomica_mental"])
router_neurotransmitter_rel = APIRouter(prefix="/api/v1/neurogenomic/neurotransmitter_release", tags=["neurogenomica_mental"])
router_nuclear_proteomics = APIRouter(prefix="/api/v1/neurogenomic/nuclear_proteomics", tags=["neurogenomica_mental"])
router_patch_seq = APIRouter(prefix="/api/v1/neurogenomic/patch_seq", tags=["neurogenomica_mental"])
router_phosphoproteomics = APIRouter(prefix="/api/v1/neurogenomic/phosphoproteomics", tags=["neurogenomica_mental"])
router_plasminogen = APIRouter(prefix="/api/v1/neurogenomic/plasminogen", tags=["neurogenomica_mental"])
router_polygenic_risk_score = APIRouter(prefix="/api/v1/neurogenomic/polygenic_risk_score", tags=["neurogenomica_mental"])
router_postsynaptic_density = APIRouter(prefix="/api/v1/neurogenomic/postsynaptic_density", tags=["neurogenomica_mental"])
router_presynaptic_proteome = APIRouter(prefix="/api/v1/neurogenomic/presynaptic_proteome", tags=["neurogenomica_mental"])
router_protease_mental = APIRouter(prefix="/api/v1/neurogenomic/protease_mental", tags=["neurogenomica_mental"])
router_proteasome_synaptic = APIRouter(prefix="/api/v1/neurogenomic/proteasome_synaptic", tags=["neurogenomica_mental"])
router_protein_quantitative = APIRouter(prefix="/api/v1/neurogenomic/protein_quantitative", tags=["neurogenomica_mental"])
router_rab_proteins = APIRouter(prefix="/api/v1/neurogenomic/rab_proteins", tags=["neurogenomica_mental"])
router_rare_variant_associa = APIRouter(prefix="/api/v1/neurogenomic/rare_variant_association", tags=["neurogenomica_mental"])
router_redox_proteomics = APIRouter(prefix="/api/v1/neurogenomic/redox_proteomics", tags=["neurogenomica_mental"])
router_secretomics = APIRouter(prefix="/api/v1/neurogenomic/secretomics", tags=["neurogenomica_mental"])
router_sentrin = APIRouter(prefix="/api/v1/neurogenomic/sentrin", tags=["neurogenomica_mental"])
router_single_cell_atac = APIRouter(prefix="/api/v1/neurogenomic/single_cell_atac", tags=["neurogenomica_mental"])
router_single_cell_multiome = APIRouter(prefix="/api/v1/neurogenomic/single_cell_multiome", tags=["neurogenomica_mental"])
router_single_cell_rna = APIRouter(prefix="/api/v1/neurogenomic/single_cell_rna", tags=["neurogenomica_mental"])
router_snare_complex = APIRouter(prefix="/api/v1/neurogenomic/snare_complex", tags=["neurogenomica_mental"])
router_snp_functional = APIRouter(prefix="/api/v1/neurogenomic/snp_functional", tags=["neurogenomica_mental"])
router_spatial_proteomics = APIRouter(prefix="/api/v1/neurogenomic/spatial_proteomics", tags=["neurogenomica_mental"])
router_spatial_transcriptom = APIRouter(prefix="/api/v1/neurogenomic/spatial_transcriptomics", tags=["neurogenomica_mental"])
router_splicing_quantitativ = APIRouter(prefix="/api/v1/neurogenomic/splicing_quantitative", tags=["neurogenomica_mental"])
router_structural_proteomic = APIRouter(prefix="/api/v1/neurogenomic/structural_proteomics", tags=["neurogenomica_mental"])
router_structural_variation = APIRouter(prefix="/api/v1/neurogenomic/structural_variation", tags=["neurogenomica_mental"])
router_sumo_mental = APIRouter(prefix="/api/v1/neurogenomic/sumo_mental", tags=["neurogenomica_mental"])
router_super_resolution = APIRouter(prefix="/api/v1/neurogenomic/super_resolution", tags=["neurogenomica_mental"])
router_synaptosomal = APIRouter(prefix="/api/v1/neurogenomic/synaptosomal", tags=["neurogenomica_mental"])
router_synaptotagmin = APIRouter(prefix="/api/v1/neurogenomic/synaptotagmin", tags=["neurogenomica_mental"])
router_tandem_repeat = APIRouter(prefix="/api/v1/neurogenomic/tandem_repeat", tags=["neurogenomica_mental"])
router_tissue_plasminogen = APIRouter(prefix="/api/v1/neurogenomic/tissue_plasminogen", tags=["neurogenomica_mental"])
router_ubiquitin_synaptic = APIRouter(prefix="/api/v1/neurogenomic/ubiquitin_synaptic", tags=["neurogenomica_mental"])
router_ubiquitinomics = APIRouter(prefix="/api/v1/neurogenomic/ubiquitinomics", tags=["neurogenomica_mental"])
router_vesicle_biogenesis = APIRouter(prefix="/api/v1/neurogenomic/vesicle_biogenesis", tags=["neurogenomica_mental"])
router_western_blot = APIRouter(prefix="/api/v1/neurogenomic/western_blot", tags=["neurogenomica_mental"])

@router_adamts_mental.get("")
async def i_adamts_mental():
    return {"p":"neurogenomica_m_adamts_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_calpain_mental.get("")
async def i_calpain_mental():
    return {"p":"neurogenomica_m_calpain_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_caspase_mental.get("")
async def i_caspase_mental():
    return {"p":"neurogenomica_m_caspase_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cathepsin_mental.get("")
async def i_cathepsin_mental():
    return {"p":"neurogenomica_m_cathepsin_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_chromatin_accessibil.get("")
async def i_chromatin_accessibil():
    return {"p":"neurogenomica_m_chromatin_accessibil","s":"ativo","t":datetime.utcnow().isoformat()}
@router_clathrin.get("")
async def i_clathrin():
    return {"p":"neurogenomica_m_clathrin","s":"ativo","t":datetime.utcnow().isoformat()}
@router_complexin.get("")
async def i_complexin():
    return {"p":"neurogenomica_m_complexin","s":"ativo","t":datetime.utcnow().isoformat()}
@router_copy_number_variatio.get("")
async def i_copy_number_variatio():
    return {"p":"neurogenomica_m_copy_number_variatio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cryo_electron.get("")
async def i_cryo_electron():
    return {"p":"neurogenomica_m_cryo_electron","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cullin_ring.get("")
async def i_cullin_ring():
    return {"p":"neurogenomica_m_cullin_ring","s":"ativo","t":datetime.utcnow().isoformat()}
@router_deubiquitinase.get("")
async def i_deubiquitinase():
    return {"p":"neurogenomica_m_deubiquitinase","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dynamin.get("")
async def i_dynamin():
    return {"p":"neurogenomica_m_dynamin","s":"ativo","t":datetime.utcnow().isoformat()}
@router_elisa_mental.get("")
async def i_elisa_mental():
    return {"p":"neurogenomica_m_elisa_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_endocytosis_synaptic.get("")
async def i_endocytosis_synaptic():
    return {"p":"neurogenomica_m_endocytosis_synaptic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_endosome_mental.get("")
async def i_endosome_mental():
    return {"p":"neurogenomica_m_endosome_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_exocytosis_synaptic.get("")
async def i_exocytosis_synaptic():
    return {"p":"neurogenomica_m_exocytosis_synaptic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_expansion_microscopy.get("")
async def i_expansion_microscopy():
    return {"p":"neurogenomica_m_expansion_microscopy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_expression_quantitat.get("")
async def i_expression_quantitat():
    return {"p":"neurogenomica_m_expression_quantitat","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fish_mental.get("")
async def i_fish_mental():
    return {"p":"neurogenomica_m_fish_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_furin_mental.get("")
async def i_furin_mental():
    return {"p":"neurogenomica_m_furin_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_genetic_risk_factor.get("")
async def i_genetic_risk_factor():
    return {"p":"neurogenomica_m_genetic_risk_factor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_genome_wide_associat.get("")
async def i_genome_wide_associat():
    return {"p":"neurogenomica_m_genome_wide_associat","s":"ativo","t":datetime.utcnow().isoformat()}
@router_glycomics.get("")
async def i_glycomics():
    return {"p":"neurogenomica_m_glycomics","s":"ativo","t":datetime.utcnow().isoformat()}
@router_glycoproteomics.get("")
async def i_glycoproteomics():
    return {"p":"neurogenomica_m_glycoproteomics","s":"ativo","t":datetime.utcnow().isoformat()}
@router_imaging_mass.get("")
async def i_imaging_mass():
    return {"p":"neurogenomica_m_imaging_mass","s":"ativo","t":datetime.utcnow().isoformat()}
@router_immunofluorescence.get("")
async def i_immunofluorescence():
    return {"p":"neurogenomica_m_immunofluorescence","s":"ativo","t":datetime.utcnow().isoformat()}
@router_immunohistochemistry.get("")
async def i_immunohistochemistry():
    return {"p":"neurogenomica_m_immunohistochemistry","s":"ativo","t":datetime.utcnow().isoformat()}
@router_in_situ_hybridizatio.get("")
async def i_in_situ_hybridizatio():
    return {"p":"neurogenomica_m_in_situ_hybridizatio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_interactomics.get("")
async def i_interactomics():
    return {"p":"neurogenomica_m_interactomics","s":"ativo","t":datetime.utcnow().isoformat()}
@router_kinomics.get("")
async def i_kinomics():
    return {"p":"neurogenomica_m_kinomics","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lipidomics.get("")
async def i_lipidomics():
    return {"p":"neurogenomica_m_lipidomics","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lysosome_mental.get("")
async def i_lysosome_mental():
    return {"p":"neurogenomica_m_lysosome_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mass_cytometry.get("")
async def i_mass_cytometry():
    return {"p":"neurogenomica_m_mass_cytometry","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mass_spectrometry_me.get("")
async def i_mass_spectrometry_me():
    return {"p":"neurogenomica_m_mass_spectrometry_me","s":"ativo","t":datetime.utcnow().isoformat()}
@router_matrix_metalloprotea.get("")
async def i_matrix_metalloprotea():
    return {"p":"neurogenomica_m_matrix_metalloprotea","s":"ativo","t":datetime.utcnow().isoformat()}
@router_membrane_proteomics.get("")
async def i_membrane_proteomics():
    return {"p":"neurogenomica_m_membrane_proteomics","s":"ativo","t":datetime.utcnow().isoformat()}
@router_metabolomics2.get("")
async def i_metabolomics2():
    return {"p":"neurogenomica_m_metabolomics2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_methylation_quantita.get("")
async def i_methylation_quantita():
    return {"p":"neurogenomica_m_methylation_quantita","s":"ativo","t":datetime.utcnow().isoformat()}
@router_microsatellite.get("")
async def i_microsatellite():
    return {"p":"neurogenomica_m_microsatellite","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mitochondrial_proteo.get("")
async def i_mitochondrial_proteo():
    return {"p":"neurogenomica_m_mitochondrial_proteo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_munc18.get("")
async def i_munc18():
    return {"p":"neurogenomica_m_munc18","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nedd8_mental.get("")
async def i_nedd8_mental():
    return {"p":"neurogenomica_m_nedd8_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neurotransmitter_rel.get("")
async def i_neurotransmitter_rel():
    return {"p":"neurogenomica_m_neurotransmitter_rel","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nuclear_proteomics.get("")
async def i_nuclear_proteomics():
    return {"p":"neurogenomica_m_nuclear_proteomics","s":"ativo","t":datetime.utcnow().isoformat()}
@router_patch_seq.get("")
async def i_patch_seq():
    return {"p":"neurogenomica_m_patch_seq","s":"ativo","t":datetime.utcnow().isoformat()}
@router_phosphoproteomics.get("")
async def i_phosphoproteomics():
    return {"p":"neurogenomica_m_phosphoproteomics","s":"ativo","t":datetime.utcnow().isoformat()}
@router_plasminogen.get("")
async def i_plasminogen():
    return {"p":"neurogenomica_m_plasminogen","s":"ativo","t":datetime.utcnow().isoformat()}
@router_polygenic_risk_score.get("")
async def i_polygenic_risk_score():
    return {"p":"neurogenomica_m_polygenic_risk_score","s":"ativo","t":datetime.utcnow().isoformat()}
@router_postsynaptic_density.get("")
async def i_postsynaptic_density():
    return {"p":"neurogenomica_m_postsynaptic_density","s":"ativo","t":datetime.utcnow().isoformat()}
@router_presynaptic_proteome.get("")
async def i_presynaptic_proteome():
    return {"p":"neurogenomica_m_presynaptic_proteome","s":"ativo","t":datetime.utcnow().isoformat()}
@router_protease_mental.get("")
async def i_protease_mental():
    return {"p":"neurogenomica_m_protease_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_proteasome_synaptic.get("")
async def i_proteasome_synaptic():
    return {"p":"neurogenomica_m_proteasome_synaptic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_protein_quantitative.get("")
async def i_protein_quantitative():
    return {"p":"neurogenomica_m_protein_quantitative","s":"ativo","t":datetime.utcnow().isoformat()}
@router_rab_proteins.get("")
async def i_rab_proteins():
    return {"p":"neurogenomica_m_rab_proteins","s":"ativo","t":datetime.utcnow().isoformat()}
@router_rare_variant_associa.get("")
async def i_rare_variant_associa():
    return {"p":"neurogenomica_m_rare_variant_associa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_redox_proteomics.get("")
async def i_redox_proteomics():
    return {"p":"neurogenomica_m_redox_proteomics","s":"ativo","t":datetime.utcnow().isoformat()}
@router_secretomics.get("")
async def i_secretomics():
    return {"p":"neurogenomica_m_secretomics","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sentrin.get("")
async def i_sentrin():
    return {"p":"neurogenomica_m_sentrin","s":"ativo","t":datetime.utcnow().isoformat()}
@router_single_cell_atac.get("")
async def i_single_cell_atac():
    return {"p":"neurogenomica_m_single_cell_atac","s":"ativo","t":datetime.utcnow().isoformat()}
@router_single_cell_multiome.get("")
async def i_single_cell_multiome():
    return {"p":"neurogenomica_m_single_cell_multiome","s":"ativo","t":datetime.utcnow().isoformat()}
@router_single_cell_rna.get("")
async def i_single_cell_rna():
    return {"p":"neurogenomica_m_single_cell_rna","s":"ativo","t":datetime.utcnow().isoformat()}
@router_snare_complex.get("")
async def i_snare_complex():
    return {"p":"neurogenomica_m_snare_complex","s":"ativo","t":datetime.utcnow().isoformat()}
@router_snp_functional.get("")
async def i_snp_functional():
    return {"p":"neurogenomica_m_snp_functional","s":"ativo","t":datetime.utcnow().isoformat()}
@router_spatial_proteomics.get("")
async def i_spatial_proteomics():
    return {"p":"neurogenomica_m_spatial_proteomics","s":"ativo","t":datetime.utcnow().isoformat()}
@router_spatial_transcriptom.get("")
async def i_spatial_transcriptom():
    return {"p":"neurogenomica_m_spatial_transcriptom","s":"ativo","t":datetime.utcnow().isoformat()}
@router_splicing_quantitativ.get("")
async def i_splicing_quantitativ():
    return {"p":"neurogenomica_m_splicing_quantitativ","s":"ativo","t":datetime.utcnow().isoformat()}
@router_structural_proteomic.get("")
async def i_structural_proteomic():
    return {"p":"neurogenomica_m_structural_proteomic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_structural_variation.get("")
async def i_structural_variation():
    return {"p":"neurogenomica_m_structural_variation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sumo_mental.get("")
async def i_sumo_mental():
    return {"p":"neurogenomica_m_sumo_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_super_resolution.get("")
async def i_super_resolution():
    return {"p":"neurogenomica_m_super_resolution","s":"ativo","t":datetime.utcnow().isoformat()}
@router_synaptosomal.get("")
async def i_synaptosomal():
    return {"p":"neurogenomica_m_synaptosomal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_synaptotagmin.get("")
async def i_synaptotagmin():
    return {"p":"neurogenomica_m_synaptotagmin","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tandem_repeat.get("")
async def i_tandem_repeat():
    return {"p":"neurogenomica_m_tandem_repeat","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tissue_plasminogen.get("")
async def i_tissue_plasminogen():
    return {"p":"neurogenomica_m_tissue_plasminogen","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ubiquitin_synaptic.get("")
async def i_ubiquitin_synaptic():
    return {"p":"neurogenomica_m_ubiquitin_synaptic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ubiquitinomics.get("")
async def i_ubiquitinomics():
    return {"p":"neurogenomica_m_ubiquitinomics","s":"ativo","t":datetime.utcnow().isoformat()}
@router_vesicle_biogenesis.get("")
async def i_vesicle_biogenesis():
    return {"p":"neurogenomica_m_vesicle_biogenesis","s":"ativo","t":datetime.utcnow().isoformat()}
@router_western_blot.get("")
async def i_western_blot():
    return {"p":"neurogenomica_m_western_blot","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_neurogenomica_mental(PluginBase):
    name = "consolidated_neurogenomica_mental"
    def setup(self, app):
        app.include_router(router_adamts_mental)
        app.include_router(router_calpain_mental)
        app.include_router(router_caspase_mental)
        app.include_router(router_cathepsin_mental)
        app.include_router(router_chromatin_accessibil)
        app.include_router(router_clathrin)
        app.include_router(router_complexin)
        app.include_router(router_copy_number_variatio)
        app.include_router(router_cryo_electron)
        app.include_router(router_cullin_ring)
        app.include_router(router_deubiquitinase)
        app.include_router(router_dynamin)
        app.include_router(router_elisa_mental)
        app.include_router(router_endocytosis_synaptic)
        app.include_router(router_endosome_mental)
        app.include_router(router_exocytosis_synaptic)
        app.include_router(router_expansion_microscopy)
        app.include_router(router_expression_quantitat)
        app.include_router(router_fish_mental)
        app.include_router(router_furin_mental)
        app.include_router(router_genetic_risk_factor)
        app.include_router(router_genome_wide_associat)
        app.include_router(router_glycomics)
        app.include_router(router_glycoproteomics)
        app.include_router(router_imaging_mass)
        app.include_router(router_immunofluorescence)
        app.include_router(router_immunohistochemistry)
        app.include_router(router_in_situ_hybridizatio)
        app.include_router(router_interactomics)
        app.include_router(router_kinomics)
        app.include_router(router_lipidomics)
        app.include_router(router_lysosome_mental)
        app.include_router(router_mass_cytometry)
        app.include_router(router_mass_spectrometry_me)
        app.include_router(router_matrix_metalloprotea)
        app.include_router(router_membrane_proteomics)
        app.include_router(router_metabolomics2)
        app.include_router(router_methylation_quantita)
        app.include_router(router_microsatellite)
        app.include_router(router_mitochondrial_proteo)
        app.include_router(router_munc18)
        app.include_router(router_nedd8_mental)
        app.include_router(router_neurotransmitter_rel)
        app.include_router(router_nuclear_proteomics)
        app.include_router(router_patch_seq)
        app.include_router(router_phosphoproteomics)
        app.include_router(router_plasminogen)
        app.include_router(router_polygenic_risk_score)
        app.include_router(router_postsynaptic_density)
        app.include_router(router_presynaptic_proteome)
        app.include_router(router_protease_mental)
        app.include_router(router_proteasome_synaptic)
        app.include_router(router_protein_quantitative)
        app.include_router(router_rab_proteins)
        app.include_router(router_rare_variant_associa)
        app.include_router(router_redox_proteomics)
        app.include_router(router_secretomics)
        app.include_router(router_sentrin)
        app.include_router(router_single_cell_atac)
        app.include_router(router_single_cell_multiome)
        app.include_router(router_single_cell_rna)
        app.include_router(router_snare_complex)
        app.include_router(router_snp_functional)
        app.include_router(router_spatial_proteomics)
        app.include_router(router_spatial_transcriptom)
        app.include_router(router_splicing_quantitativ)
        app.include_router(router_structural_proteomic)
        app.include_router(router_structural_variation)
        app.include_router(router_sumo_mental)
        app.include_router(router_super_resolution)
        app.include_router(router_synaptosomal)
        app.include_router(router_synaptotagmin)
        app.include_router(router_tandem_repeat)
        app.include_router(router_tissue_plasminogen)
        app.include_router(router_ubiquitin_synaptic)
        app.include_router(router_ubiquitinomics)
        app.include_router(router_vesicle_biogenesis)
        app.include_router(router_western_blot)


plugin = Plugin_neurogenomica_mental()
