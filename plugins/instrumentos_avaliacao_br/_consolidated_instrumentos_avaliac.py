from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_acq_br = APIRouter(prefix="/api/v1/instrumentos/acq_br", tags=["instrumentos_avaliacao_br"])
router_assist_br = APIRouter(prefix="/api/v1/instrumentos/assist_br", tags=["instrumentos_avaliacao_br"])
router_audit_br = APIRouter(prefix="/api/v1/instrumentos/audit_br", tags=["instrumentos_avaliacao_br"])
router_bai_br = APIRouter(prefix="/api/v1/instrumentos/bai_br", tags=["instrumentos_avaliacao_br"])
router_bandura_autoeficacia = APIRouter(prefix="/api/v1/instrumentos/bandura_autoeficacia", tags=["instrumentos_avaliacao_br"])
router_bdi_ii_br = APIRouter(prefix="/api/v1/instrumentos/bdi_ii_br", tags=["instrumentos_avaliacao_br"])
router_beck_hopelessness_br = APIRouter(prefix="/api/v1/instrumentos/beck_hopelessness_br", tags=["instrumentos_avaliacao_br"])
router_beck_scale_suicidal = APIRouter(prefix="/api/v1/instrumentos/beck_scale_suicidal", tags=["instrumentos_avaliacao_br"])
router_bfis_br = APIRouter(prefix="/api/v1/instrumentos/bfis_br", tags=["instrumentos_avaliacao_br"])
router_bfq_br = APIRouter(prefix="/api/v1/instrumentos/bfq_br", tags=["instrumentos_avaliacao_br"])
router_bmis_br = APIRouter(prefix="/api/v1/instrumentos/bmis_br", tags=["instrumentos_avaliacao_br"])
router_brief_cope = APIRouter(prefix="/api/v1/instrumentos/brief_cope", tags=["instrumentos_avaliacao_br"])
router_bsq_br = APIRouter(prefix="/api/v1/instrumentos/bsq_br", tags=["instrumentos_avaliacao_br"])
router_cage_br = APIRouter(prefix="/api/v1/instrumentos/cage_br", tags=["instrumentos_avaliacao_br"])
router_cap_br = APIRouter(prefix="/api/v1/instrumentos/cap_br", tags=["instrumentos_avaliacao_br"])
router_caps_5_br = APIRouter(prefix="/api/v1/instrumentos/caps_5_br", tags=["instrumentos_avaliacao_br"])
router_carver_cope = APIRouter(prefix="/api/v1/instrumentos/carver_cope", tags=["instrumentos_avaliacao_br"])
router_cdrisc_br = APIRouter(prefix="/api/v1/instrumentos/cdrisc_br", tags=["instrumentos_avaliacao_br"])
router_clinician_ptsd = APIRouter(prefix="/api/v1/instrumentos/clinician_ptsd", tags=["instrumentos_avaliacao_br"])
router_cope_full = APIRouter(prefix="/api/v1/instrumentos/cope_full", tags=["instrumentos_avaliacao_br"])
router_crafft_br = APIRouter(prefix="/api/v1/instrumentos/crafft_br", tags=["instrumentos_avaliacao_br"])
router_dass21_br = APIRouter(prefix="/api/v1/instrumentos/dass21_br", tags=["instrumentos_avaliacao_br"])
router_dast_br = APIRouter(prefix="/api/v1/instrumentos/dast_br", tags=["instrumentos_avaliacao_br"])
router_davidson_trauma_br = APIRouter(prefix="/api/v1/instrumentos/davidson_trauma_br", tags=["instrumentos_avaliacao_br"])
router_duke_social_support = APIRouter(prefix="/api/v1/instrumentos/duke_social_support", tags=["instrumentos_avaliacao_br"])
router_emotion_focused = APIRouter(prefix="/api/v1/instrumentos/emotion_focused", tags=["instrumentos_avaliacao_br"])
router_escala_autoconceito = APIRouter(prefix="/api/v1/instrumentos/escala_autoconceito", tags=["instrumentos_avaliacao_br"])
router_escala_autoeficacia_ = APIRouter(prefix="/api/v1/instrumentos/escala_autoeficacia_br", tags=["instrumentos_avaliacao_br"])
router_escala_autoestima_es = APIRouter(prefix="/api/v1/instrumentos/escala_autoestima_especif", tags=["instrumentos_avaliacao_br"])
router_escala_satisfacao_vi = APIRouter(prefix="/api/v1/instrumentos/escala_satisfacao_vida_br", tags=["instrumentos_avaliacao_br"])
router_folkman_lazarus = APIRouter(prefix="/api/v1/instrumentos/folkman_lazarus", tags=["instrumentos_avaliacao_br"])
router_gad2_br = APIRouter(prefix="/api/v1/instrumentos/gad2_br", tags=["instrumentos_avaliacao_br"])
router_gad7_normas_br = APIRouter(prefix="/api/v1/instrumentos/gad7_normas_br", tags=["instrumentos_avaliacao_br"])
router_gses_br = APIRouter(prefix="/api/v1/instrumentos/gses_br", tags=["instrumentos_avaliacao_br"])
router_hads_br = APIRouter(prefix="/api/v1/instrumentos/hads_br", tags=["instrumentos_avaliacao_br"])
router_ies_r_br = APIRouter(prefix="/api/v1/instrumentos/ies_r_br", tags=["instrumentos_avaliacao_br"])
router_k10_br = APIRouter(prefix="/api/v1/instrumentos/k10_br", tags=["instrumentos_avaliacao_br"])
router_k6_br = APIRouter(prefix="/api/v1/instrumentos/k6_br", tags=["instrumentos_avaliacao_br"])
router_lsas_br = APIRouter(prefix="/api/v1/instrumentos/lsas_br", tags=["instrumentos_avaliacao_br"])
router_meaning_focused = APIRouter(prefix="/api/v1/instrumentos/meaning_focused", tags=["instrumentos_avaliacao_br"])
router_mi_br = APIRouter(prefix="/api/v1/instrumentos/mi_br", tags=["instrumentos_avaliacao_br"])
router_mos_social_support = APIRouter(prefix="/api/v1/instrumentos/mos_social_support", tags=["instrumentos_avaliacao_br"])
router_mspss_br = APIRouter(prefix="/api/v1/instrumentos/mspss_br", tags=["instrumentos_avaliacao_br"])
router_neo_pi_r_br = APIRouter(prefix="/api/v1/instrumentos/neo_pi_r_br", tags=["instrumentos_avaliacao_br"])
router_oci_r_br = APIRouter(prefix="/api/v1/instrumentos/oci_r_br", tags=["instrumentos_avaliacao_br"])
router_panas_br = APIRouter(prefix="/api/v1/instrumentos/panas_br", tags=["instrumentos_avaliacao_br"])
router_panas_x_br = APIRouter(prefix="/api/v1/instrumentos/panas_x_br", tags=["instrumentos_avaliacao_br"])
router_pcl5_br = APIRouter(prefix="/api/v1/instrumentos/pcl5_br", tags=["instrumentos_avaliacao_br"])
router_pdss_br = APIRouter(prefix="/api/v1/instrumentos/pdss_br", tags=["instrumentos_avaliacao_br"])
router_phq2_br = APIRouter(prefix="/api/v1/instrumentos/phq2_br", tags=["instrumentos_avaliacao_br"])
router_phq4_br = APIRouter(prefix="/api/v1/instrumentos/phq4_br", tags=["instrumentos_avaliacao_br"])
router_phq9_normas_br = APIRouter(prefix="/api/v1/instrumentos/phq9_normas_br", tags=["instrumentos_avaliacao_br"])
router_phq_ptsd_br = APIRouter(prefix="/api/v1/instrumentos/phq_ptsd_br", tags=["instrumentos_avaliacao_br"])
router_pi_wsur_br = APIRouter(prefix="/api/v1/instrumentos/pi_wsur_br", tags=["instrumentos_avaliacao_br"])
router_poms_br = APIRouter(prefix="/api/v1/instrumentos/poms_br", tags=["instrumentos_avaliacao_br"])
router_problem_focused = APIRouter(prefix="/api/v1/instrumentos/problem_focused", tags=["instrumentos_avaliacao_br"])
router_rosenberg_br2 = APIRouter(prefix="/api/v1/instrumentos/rosenberg_br2", tags=["instrumentos_avaliacao_br"])
router_sense_coherence_br = APIRouter(prefix="/api/v1/instrumentos/sense_coherence_br", tags=["instrumentos_avaliacao_br"])
router_sf12_br = APIRouter(prefix="/api/v1/instrumentos/sf12_br", tags=["instrumentos_avaliacao_br"])
router_sf36_br = APIRouter(prefix="/api/v1/instrumentos/sf36_br", tags=["instrumentos_avaliacao_br"])
router_spin_br = APIRouter(prefix="/api/v1/instrumentos/spin_br", tags=["instrumentos_avaliacao_br"])
router_stai_state = APIRouter(prefix="/api/v1/instrumentos/stai_state", tags=["instrumentos_avaliacao_br"])
router_stai_trait = APIRouter(prefix="/api/v1/instrumentos/stai_trait", tags=["instrumentos_avaliacao_br"])
router_swls_br = APIRouter(prefix="/api/v1/instrumentos/swls_br", tags=["instrumentos_avaliacao_br"])
router_whoqol_100_br = APIRouter(prefix="/api/v1/instrumentos/whoqol_100_br", tags=["instrumentos_avaliacao_br"])
router_whoqol_bref_br = APIRouter(prefix="/api/v1/instrumentos/whoqol_bref_br", tags=["instrumentos_avaliacao_br"])
router_ybocs_br = APIRouter(prefix="/api/v1/instrumentos/ybocs_br", tags=["instrumentos_avaliacao_br"])

@router_acq_br.get("")
async def i_acq_br():
    return {"p":"instrumentos_av_acq_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_assist_br.get("")
async def i_assist_br():
    return {"p":"instrumentos_av_assist_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_audit_br.get("")
async def i_audit_br():
    return {"p":"instrumentos_av_audit_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bai_br.get("")
async def i_bai_br():
    return {"p":"instrumentos_av_bai_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bandura_autoeficacia.get("")
async def i_bandura_autoeficacia():
    return {"p":"instrumentos_av_bandura_autoeficacia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bdi_ii_br.get("")
async def i_bdi_ii_br():
    return {"p":"instrumentos_av_bdi_ii_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_beck_hopelessness_br.get("")
async def i_beck_hopelessness_br():
    return {"p":"instrumentos_av_beck_hopelessness_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_beck_scale_suicidal.get("")
async def i_beck_scale_suicidal():
    return {"p":"instrumentos_av_beck_scale_suicidal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bfis_br.get("")
async def i_bfis_br():
    return {"p":"instrumentos_av_bfis_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bfq_br.get("")
async def i_bfq_br():
    return {"p":"instrumentos_av_bfq_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bmis_br.get("")
async def i_bmis_br():
    return {"p":"instrumentos_av_bmis_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_brief_cope.get("")
async def i_brief_cope():
    return {"p":"instrumentos_av_brief_cope","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bsq_br.get("")
async def i_bsq_br():
    return {"p":"instrumentos_av_bsq_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cage_br.get("")
async def i_cage_br():
    return {"p":"instrumentos_av_cage_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cap_br.get("")
async def i_cap_br():
    return {"p":"instrumentos_av_cap_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_caps_5_br.get("")
async def i_caps_5_br():
    return {"p":"instrumentos_av_caps_5_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_carver_cope.get("")
async def i_carver_cope():
    return {"p":"instrumentos_av_carver_cope","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cdrisc_br.get("")
async def i_cdrisc_br():
    return {"p":"instrumentos_av_cdrisc_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_clinician_ptsd.get("")
async def i_clinician_ptsd():
    return {"p":"instrumentos_av_clinician_ptsd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cope_full.get("")
async def i_cope_full():
    return {"p":"instrumentos_av_cope_full","s":"ativo","t":datetime.utcnow().isoformat()}
@router_crafft_br.get("")
async def i_crafft_br():
    return {"p":"instrumentos_av_crafft_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dass21_br.get("")
async def i_dass21_br():
    return {"p":"instrumentos_av_dass21_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dast_br.get("")
async def i_dast_br():
    return {"p":"instrumentos_av_dast_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_davidson_trauma_br.get("")
async def i_davidson_trauma_br():
    return {"p":"instrumentos_av_davidson_trauma_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_duke_social_support.get("")
async def i_duke_social_support():
    return {"p":"instrumentos_av_duke_social_support","s":"ativo","t":datetime.utcnow().isoformat()}
@router_emotion_focused.get("")
async def i_emotion_focused():
    return {"p":"instrumentos_av_emotion_focused","s":"ativo","t":datetime.utcnow().isoformat()}
@router_escala_autoconceito.get("")
async def i_escala_autoconceito():
    return {"p":"instrumentos_av_escala_autoconceito","s":"ativo","t":datetime.utcnow().isoformat()}
@router_escala_autoeficacia_.get("")
async def i_escala_autoeficacia_():
    return {"p":"instrumentos_av_escala_autoeficacia_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_escala_autoestima_es.get("")
async def i_escala_autoestima_es():
    return {"p":"instrumentos_av_escala_autoestima_es","s":"ativo","t":datetime.utcnow().isoformat()}
@router_escala_satisfacao_vi.get("")
async def i_escala_satisfacao_vi():
    return {"p":"instrumentos_av_escala_satisfacao_vi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_folkman_lazarus.get("")
async def i_folkman_lazarus():
    return {"p":"instrumentos_av_folkman_lazarus","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gad2_br.get("")
async def i_gad2_br():
    return {"p":"instrumentos_av_gad2_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gad7_normas_br.get("")
async def i_gad7_normas_br():
    return {"p":"instrumentos_av_gad7_normas_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gses_br.get("")
async def i_gses_br():
    return {"p":"instrumentos_av_gses_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hads_br.get("")
async def i_hads_br():
    return {"p":"instrumentos_av_hads_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ies_r_br.get("")
async def i_ies_r_br():
    return {"p":"instrumentos_av_ies_r_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_k10_br.get("")
async def i_k10_br():
    return {"p":"instrumentos_av_k10_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_k6_br.get("")
async def i_k6_br():
    return {"p":"instrumentos_av_k6_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lsas_br.get("")
async def i_lsas_br():
    return {"p":"instrumentos_av_lsas_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_meaning_focused.get("")
async def i_meaning_focused():
    return {"p":"instrumentos_av_meaning_focused","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mi_br.get("")
async def i_mi_br():
    return {"p":"instrumentos_av_mi_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mos_social_support.get("")
async def i_mos_social_support():
    return {"p":"instrumentos_av_mos_social_support","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mspss_br.get("")
async def i_mspss_br():
    return {"p":"instrumentos_av_mspss_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neo_pi_r_br.get("")
async def i_neo_pi_r_br():
    return {"p":"instrumentos_av_neo_pi_r_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_oci_r_br.get("")
async def i_oci_r_br():
    return {"p":"instrumentos_av_oci_r_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_panas_br.get("")
async def i_panas_br():
    return {"p":"instrumentos_av_panas_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_panas_x_br.get("")
async def i_panas_x_br():
    return {"p":"instrumentos_av_panas_x_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pcl5_br.get("")
async def i_pcl5_br():
    return {"p":"instrumentos_av_pcl5_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pdss_br.get("")
async def i_pdss_br():
    return {"p":"instrumentos_av_pdss_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_phq2_br.get("")
async def i_phq2_br():
    return {"p":"instrumentos_av_phq2_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_phq4_br.get("")
async def i_phq4_br():
    return {"p":"instrumentos_av_phq4_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_phq9_normas_br.get("")
async def i_phq9_normas_br():
    return {"p":"instrumentos_av_phq9_normas_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_phq_ptsd_br.get("")
async def i_phq_ptsd_br():
    return {"p":"instrumentos_av_phq_ptsd_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pi_wsur_br.get("")
async def i_pi_wsur_br():
    return {"p":"instrumentos_av_pi_wsur_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_poms_br.get("")
async def i_poms_br():
    return {"p":"instrumentos_av_poms_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_problem_focused.get("")
async def i_problem_focused():
    return {"p":"instrumentos_av_problem_focused","s":"ativo","t":datetime.utcnow().isoformat()}
@router_rosenberg_br2.get("")
async def i_rosenberg_br2():
    return {"p":"instrumentos_av_rosenberg_br2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sense_coherence_br.get("")
async def i_sense_coherence_br():
    return {"p":"instrumentos_av_sense_coherence_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sf12_br.get("")
async def i_sf12_br():
    return {"p":"instrumentos_av_sf12_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sf36_br.get("")
async def i_sf36_br():
    return {"p":"instrumentos_av_sf36_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_spin_br.get("")
async def i_spin_br():
    return {"p":"instrumentos_av_spin_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_stai_state.get("")
async def i_stai_state():
    return {"p":"instrumentos_av_stai_state","s":"ativo","t":datetime.utcnow().isoformat()}
@router_stai_trait.get("")
async def i_stai_trait():
    return {"p":"instrumentos_av_stai_trait","s":"ativo","t":datetime.utcnow().isoformat()}
@router_swls_br.get("")
async def i_swls_br():
    return {"p":"instrumentos_av_swls_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_whoqol_100_br.get("")
async def i_whoqol_100_br():
    return {"p":"instrumentos_av_whoqol_100_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_whoqol_bref_br.get("")
async def i_whoqol_bref_br():
    return {"p":"instrumentos_av_whoqol_bref_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ybocs_br.get("")
async def i_ybocs_br():
    return {"p":"instrumentos_av_ybocs_br","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_instrumentos_avaliac(PluginBase):
    name = "consolidated_instrumentos_avaliacao_br"
    def setup(self, app):
        app.include_router(router_acq_br)
        app.include_router(router_assist_br)
        app.include_router(router_audit_br)
        app.include_router(router_bai_br)
        app.include_router(router_bandura_autoeficacia)
        app.include_router(router_bdi_ii_br)
        app.include_router(router_beck_hopelessness_br)
        app.include_router(router_beck_scale_suicidal)
        app.include_router(router_bfis_br)
        app.include_router(router_bfq_br)
        app.include_router(router_bmis_br)
        app.include_router(router_brief_cope)
        app.include_router(router_bsq_br)
        app.include_router(router_cage_br)
        app.include_router(router_cap_br)
        app.include_router(router_caps_5_br)
        app.include_router(router_carver_cope)
        app.include_router(router_cdrisc_br)
        app.include_router(router_clinician_ptsd)
        app.include_router(router_cope_full)
        app.include_router(router_crafft_br)
        app.include_router(router_dass21_br)
        app.include_router(router_dast_br)
        app.include_router(router_davidson_trauma_br)
        app.include_router(router_duke_social_support)
        app.include_router(router_emotion_focused)
        app.include_router(router_escala_autoconceito)
        app.include_router(router_escala_autoeficacia_)
        app.include_router(router_escala_autoestima_es)
        app.include_router(router_escala_satisfacao_vi)
        app.include_router(router_folkman_lazarus)
        app.include_router(router_gad2_br)
        app.include_router(router_gad7_normas_br)
        app.include_router(router_gses_br)
        app.include_router(router_hads_br)
        app.include_router(router_ies_r_br)
        app.include_router(router_k10_br)
        app.include_router(router_k6_br)
        app.include_router(router_lsas_br)
        app.include_router(router_meaning_focused)
        app.include_router(router_mi_br)
        app.include_router(router_mos_social_support)
        app.include_router(router_mspss_br)
        app.include_router(router_neo_pi_r_br)
        app.include_router(router_oci_r_br)
        app.include_router(router_panas_br)
        app.include_router(router_panas_x_br)
        app.include_router(router_pcl5_br)
        app.include_router(router_pdss_br)
        app.include_router(router_phq2_br)
        app.include_router(router_phq4_br)
        app.include_router(router_phq9_normas_br)
        app.include_router(router_phq_ptsd_br)
        app.include_router(router_pi_wsur_br)
        app.include_router(router_poms_br)
        app.include_router(router_problem_focused)
        app.include_router(router_rosenberg_br2)
        app.include_router(router_sense_coherence_br)
        app.include_router(router_sf12_br)
        app.include_router(router_sf36_br)
        app.include_router(router_spin_br)
        app.include_router(router_stai_state)
        app.include_router(router_stai_trait)
        app.include_router(router_swls_br)
        app.include_router(router_whoqol_100_br)
        app.include_router(router_whoqol_bref_br)
        app.include_router(router_ybocs_br)


plugin = Plugin_instrumentos_avaliac()
