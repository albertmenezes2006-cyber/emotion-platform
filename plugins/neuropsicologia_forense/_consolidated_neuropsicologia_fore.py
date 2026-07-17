from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_admissibility = APIRouter(prefix="/api/v1/neuropsicolo/admissibility", tags=["neuropsicologia_forense"])
router_alzheimer_forense = APIRouter(prefix="/api/v1/neuropsicolo/alzheimer_forense", tags=["neuropsicologia_forense"])
router_amnesia_dissociativa = APIRouter(prefix="/api/v1/neuropsicolo/amnesia_dissociativa", tags=["neuropsicologia_forense"])
router_anterograde_amnesia = APIRouter(prefix="/api/v1/neuropsicolo/anterograde_amnesia", tags=["neuropsicologia_forense"])
router_auxiliar_justica = APIRouter(prefix="/api/v1/neuropsicolo/auxiliar_justica", tags=["neuropsicologia_forense"])
router_avaliacao_capacidade = APIRouter(prefix="/api/v1/neuropsicolo/avaliacao_capacidade", tags=["neuropsicologia_forense"])
router_avaliacao_forense_ne = APIRouter(prefix="/api/v1/neuropsicolo/avaliacao_forense_neuro", tags=["neuropsicologia_forense"])
router_biomarcadores_forens = APIRouter(prefix="/api/v1/neuropsicolo/biomarcadores_forense", tags=["neuropsicologia_forense"])
router_biomarker_tbi = APIRouter(prefix="/api/v1/neuropsicolo/biomarker_tbi", tags=["neuropsicologia_forense"])
router_biometria_forense = APIRouter(prefix="/api/v1/neuropsicolo/biometria_forense", tags=["neuropsicologia_forense"])
router_capacidade_contratua = APIRouter(prefix="/api/v1/neuropsicolo/capacidade_contratual", tags=["neuropsicologia_forense"])
router_capacidade_processua = APIRouter(prefix="/api/v1/neuropsicolo/capacidade_processual", tags=["neuropsicologia_forense"])
router_capacidade_testament = APIRouter(prefix="/api/v1/neuropsicolo/capacidade_testamentaria", tags=["neuropsicologia_forense"])
router_clinical_vs_forensic = APIRouter(prefix="/api/v1/neuropsicolo/clinical_vs_forensic", tags=["neuropsicologia_forense"])
router_cognicao_tbi = APIRouter(prefix="/api/v1/neuropsicolo/cognicao_tbi", tags=["neuropsicologia_forense"])
router_comportamento_tbi = APIRouter(prefix="/api/v1/neuropsicolo/comportamento_tbi", tags=["neuropsicologia_forense"])
router_confabulacao_forense = APIRouter(prefix="/api/v1/neuropsicolo/confabulacao_forense", tags=["neuropsicologia_forense"])
router_confidentiality_fore = APIRouter(prefix="/api/v1/neuropsicolo/confidentiality_forense", tags=["neuropsicologia_forense"])
router_cte_forense = APIRouter(prefix="/api/v1/neuropsicolo/cte_forense", tags=["neuropsicologia_forense"])
router_ctf_forense = APIRouter(prefix="/api/v1/neuropsicolo/ctf_forense", tags=["neuropsicologia_forense"])
router_daubert_standard = APIRouter(prefix="/api/v1/neuropsicolo/daubert_standard", tags=["neuropsicologia_forense"])
router_demencia_forense = APIRouter(prefix="/api/v1/neuropsicolo/demencia_forense", tags=["neuropsicologia_forense"])
router_dual_role = APIRouter(prefix="/api/v1/neuropsicolo/dual_role", tags=["neuropsicologia_forense"])
router_duty_protect = APIRouter(prefix="/api/v1/neuropsicolo/duty_protect", tags=["neuropsicologia_forense"])
router_duty_warn = APIRouter(prefix="/api/v1/neuropsicolo/duty_warn", tags=["neuropsicologia_forense"])
router_eeg_forense = APIRouter(prefix="/api/v1/neuropsicolo/eeg_forense", tags=["neuropsicologia_forense"])
router_emocao_tbi = APIRouter(prefix="/api/v1/neuropsicolo/emocao_tbi", tags=["neuropsicologia_forense"])
router_encefalopatia_forens = APIRouter(prefix="/api/v1/neuropsicolo/encefalopatia_forense", tags=["neuropsicologia_forense"])
router_epilepsia_forense = APIRouter(prefix="/api/v1/neuropsicolo/epilepsia_forense", tags=["neuropsicologia_forense"])
router_expert_witness = APIRouter(prefix="/api/v1/neuropsicolo/expert_witness", tags=["neuropsicologia_forense"])
router_eyewitness_adulto = APIRouter(prefix="/api/v1/neuropsicolo/eyewitness_adulto", tags=["neuropsicologia_forense"])
router_fmri_forense = APIRouter(prefix="/api/v1/neuropsicolo/fmri_forense", tags=["neuropsicologia_forense"])
router_frye_standard = APIRouter(prefix="/api/v1/neuropsicolo/frye_standard", tags=["neuropsicologia_forense"])
router_informed_consent_for = APIRouter(prefix="/api/v1/neuropsicolo/informed_consent_forense", tags=["neuropsicologia_forense"])
router_laudo_neuropsico = APIRouter(prefix="/api/v1/neuropsicolo/laudo_neuropsico", tags=["neuropsicologia_forense"])
router_limits_confidentiali = APIRouter(prefix="/api/v1/neuropsicolo/limits_confidentiality", tags=["neuropsicologia_forense"])
router_malingering_tbi = APIRouter(prefix="/api/v1/neuropsicolo/malingering_tbi", tags=["neuropsicologia_forense"])
router_mandatory_reporting2 = APIRouter(prefix="/api/v1/neuropsicolo/mandatory_reporting2", tags=["neuropsicologia_forense"])
router_memoria_forense = APIRouter(prefix="/api/v1/neuropsicolo/memoria_forense", tags=["neuropsicologia_forense"])
router_mri_forense = APIRouter(prefix="/api/v1/neuropsicolo/mri_forense", tags=["neuropsicologia_forense"])
router_neuroimagem_forense = APIRouter(prefix="/api/v1/neuropsicolo/neuroimagem_forense", tags=["neuropsicologia_forense"])
router_parkinson_forense = APIRouter(prefix="/api/v1/neuropsicolo/parkinson_forense", tags=["neuropsicologia_forense"])
router_pericia_neuropsico = APIRouter(prefix="/api/v1/neuropsicolo/pericia_neuropsico", tags=["neuropsicologia_forense"])
router_perito = APIRouter(prefix="/api/v1/neuropsicolo/perito", tags=["neuropsicologia_forense"])
router_personalidade_tbi = APIRouter(prefix="/api/v1/neuropsicolo/personalidade_tbi", tags=["neuropsicologia_forense"])
router_pet_forense = APIRouter(prefix="/api/v1/neuropsicolo/pet_forense", tags=["neuropsicologia_forense"])
router_privilege_forense = APIRouter(prefix="/api/v1/neuropsicolo/privilege_forense", tags=["neuropsicologia_forense"])
router_pseudo_memoria = APIRouter(prefix="/api/v1/neuropsicolo/pseudo_memoria", tags=["neuropsicologia_forense"])
router_reconhecimento_pesso = APIRouter(prefix="/api/v1/neuropsicolo/reconhecimento_pessoa", tags=["neuropsicologia_forense"])
router_reconhecimento_voz = APIRouter(prefix="/api/v1/neuropsicolo/reconhecimento_voz", tags=["neuropsicologia_forense"])
router_relatorio_forense = APIRouter(prefix="/api/v1/neuropsicolo/relatorio_forense", tags=["neuropsicologia_forense"])
router_reliability_evidence = APIRouter(prefix="/api/v1/neuropsicolo/reliability_evidence", tags=["neuropsicologia_forense"])
router_retrograde_amnesia = APIRouter(prefix="/api/v1/neuropsicolo/retrograde_amnesia", tags=["neuropsicologia_forense"])
router_sequelas_tbi = APIRouter(prefix="/api/v1/neuropsicolo/sequelas_tbi", tags=["neuropsicologia_forense"])
router_simulacao_tbi = APIRouter(prefix="/api/v1/neuropsicolo/simulacao_tbi", tags=["neuropsicologia_forense"])
router_spect_forense = APIRouter(prefix="/api/v1/neuropsicolo/spect_forense", tags=["neuropsicologia_forense"])
router_suggestibilidade_adu = APIRouter(prefix="/api/v1/neuropsicolo/suggestibilidade_adulto", tags=["neuropsicologia_forense"])
router_tarasoff2 = APIRouter(prefix="/api/v1/neuropsicolo/tarasoff2", tags=["neuropsicologia_forense"])
router_tbi_forense = APIRouter(prefix="/api/v1/neuropsicolo/tbi_forense", tags=["neuropsicologia_forense"])
router_tbi_mild = APIRouter(prefix="/api/v1/neuropsicolo/tbi_mild", tags=["neuropsicologia_forense"])
router_tbi_moderate = APIRouter(prefix="/api/v1/neuropsicolo/tbi_moderate", tags=["neuropsicologia_forense"])
router_tbi_severe = APIRouter(prefix="/api/v1/neuropsicolo/tbi_severe", tags=["neuropsicologia_forense"])
router_testemunho_especiali = APIRouter(prefix="/api/v1/neuropsicolo/testemunho_especialista", tags=["neuropsicologia_forense"])
router_therapeutic_jurispru = APIRouter(prefix="/api/v1/neuropsicolo/therapeutic_jurisprudence", tags=["neuropsicologia_forense"])
router_treatment_vs_evaluat = APIRouter(prefix="/api/v1/neuropsicolo/treatment_vs_evaluation", tags=["neuropsicologia_forense"])
router_validity_evidence = APIRouter(prefix="/api/v1/neuropsicolo/validity_evidence", tags=["neuropsicologia_forense"])

@router_admissibility.get("")
async def i_admissibility():
    return {"p":"neuropsicologia_admissibility","s":"ativo","t":datetime.utcnow().isoformat()}
@router_alzheimer_forense.get("")
async def i_alzheimer_forense():
    return {"p":"neuropsicologia_alzheimer_forense","s":"ativo","t":datetime.utcnow().isoformat()}
@router_amnesia_dissociativa.get("")
async def i_amnesia_dissociativa():
    return {"p":"neuropsicologia_amnesia_dissociativa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_anterograde_amnesia.get("")
async def i_anterograde_amnesia():
    return {"p":"neuropsicologia_anterograde_amnesia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_auxiliar_justica.get("")
async def i_auxiliar_justica():
    return {"p":"neuropsicologia_auxiliar_justica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_avaliacao_capacidade.get("")
async def i_avaliacao_capacidade():
    return {"p":"neuropsicologia_avaliacao_capacidade","s":"ativo","t":datetime.utcnow().isoformat()}
@router_avaliacao_forense_ne.get("")
async def i_avaliacao_forense_ne():
    return {"p":"neuropsicologia_avaliacao_forense_ne","s":"ativo","t":datetime.utcnow().isoformat()}
@router_biomarcadores_forens.get("")
async def i_biomarcadores_forens():
    return {"p":"neuropsicologia_biomarcadores_forens","s":"ativo","t":datetime.utcnow().isoformat()}
@router_biomarker_tbi.get("")
async def i_biomarker_tbi():
    return {"p":"neuropsicologia_biomarker_tbi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_biometria_forense.get("")
async def i_biometria_forense():
    return {"p":"neuropsicologia_biometria_forense","s":"ativo","t":datetime.utcnow().isoformat()}
@router_capacidade_contratua.get("")
async def i_capacidade_contratua():
    return {"p":"neuropsicologia_capacidade_contratua","s":"ativo","t":datetime.utcnow().isoformat()}
@router_capacidade_processua.get("")
async def i_capacidade_processua():
    return {"p":"neuropsicologia_capacidade_processua","s":"ativo","t":datetime.utcnow().isoformat()}
@router_capacidade_testament.get("")
async def i_capacidade_testament():
    return {"p":"neuropsicologia_capacidade_testament","s":"ativo","t":datetime.utcnow().isoformat()}
@router_clinical_vs_forensic.get("")
async def i_clinical_vs_forensic():
    return {"p":"neuropsicologia_clinical_vs_forensic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cognicao_tbi.get("")
async def i_cognicao_tbi():
    return {"p":"neuropsicologia_cognicao_tbi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_comportamento_tbi.get("")
async def i_comportamento_tbi():
    return {"p":"neuropsicologia_comportamento_tbi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_confabulacao_forense.get("")
async def i_confabulacao_forense():
    return {"p":"neuropsicologia_confabulacao_forense","s":"ativo","t":datetime.utcnow().isoformat()}
@router_confidentiality_fore.get("")
async def i_confidentiality_fore():
    return {"p":"neuropsicologia_confidentiality_fore","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cte_forense.get("")
async def i_cte_forense():
    return {"p":"neuropsicologia_cte_forense","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ctf_forense.get("")
async def i_ctf_forense():
    return {"p":"neuropsicologia_ctf_forense","s":"ativo","t":datetime.utcnow().isoformat()}
@router_daubert_standard.get("")
async def i_daubert_standard():
    return {"p":"neuropsicologia_daubert_standard","s":"ativo","t":datetime.utcnow().isoformat()}
@router_demencia_forense.get("")
async def i_demencia_forense():
    return {"p":"neuropsicologia_demencia_forense","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dual_role.get("")
async def i_dual_role():
    return {"p":"neuropsicologia_dual_role","s":"ativo","t":datetime.utcnow().isoformat()}
@router_duty_protect.get("")
async def i_duty_protect():
    return {"p":"neuropsicologia_duty_protect","s":"ativo","t":datetime.utcnow().isoformat()}
@router_duty_warn.get("")
async def i_duty_warn():
    return {"p":"neuropsicologia_duty_warn","s":"ativo","t":datetime.utcnow().isoformat()}
@router_eeg_forense.get("")
async def i_eeg_forense():
    return {"p":"neuropsicologia_eeg_forense","s":"ativo","t":datetime.utcnow().isoformat()}
@router_emocao_tbi.get("")
async def i_emocao_tbi():
    return {"p":"neuropsicologia_emocao_tbi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_encefalopatia_forens.get("")
async def i_encefalopatia_forens():
    return {"p":"neuropsicologia_encefalopatia_forens","s":"ativo","t":datetime.utcnow().isoformat()}
@router_epilepsia_forense.get("")
async def i_epilepsia_forense():
    return {"p":"neuropsicologia_epilepsia_forense","s":"ativo","t":datetime.utcnow().isoformat()}
@router_expert_witness.get("")
async def i_expert_witness():
    return {"p":"neuropsicologia_expert_witness","s":"ativo","t":datetime.utcnow().isoformat()}
@router_eyewitness_adulto.get("")
async def i_eyewitness_adulto():
    return {"p":"neuropsicologia_eyewitness_adulto","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fmri_forense.get("")
async def i_fmri_forense():
    return {"p":"neuropsicologia_fmri_forense","s":"ativo","t":datetime.utcnow().isoformat()}
@router_frye_standard.get("")
async def i_frye_standard():
    return {"p":"neuropsicologia_frye_standard","s":"ativo","t":datetime.utcnow().isoformat()}
@router_informed_consent_for.get("")
async def i_informed_consent_for():
    return {"p":"neuropsicologia_informed_consent_for","s":"ativo","t":datetime.utcnow().isoformat()}
@router_laudo_neuropsico.get("")
async def i_laudo_neuropsico():
    return {"p":"neuropsicologia_laudo_neuropsico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_limits_confidentiali.get("")
async def i_limits_confidentiali():
    return {"p":"neuropsicologia_limits_confidentiali","s":"ativo","t":datetime.utcnow().isoformat()}
@router_malingering_tbi.get("")
async def i_malingering_tbi():
    return {"p":"neuropsicologia_malingering_tbi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mandatory_reporting2.get("")
async def i_mandatory_reporting2():
    return {"p":"neuropsicologia_mandatory_reporting2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_memoria_forense.get("")
async def i_memoria_forense():
    return {"p":"neuropsicologia_memoria_forense","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mri_forense.get("")
async def i_mri_forense():
    return {"p":"neuropsicologia_mri_forense","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neuroimagem_forense.get("")
async def i_neuroimagem_forense():
    return {"p":"neuropsicologia_neuroimagem_forense","s":"ativo","t":datetime.utcnow().isoformat()}
@router_parkinson_forense.get("")
async def i_parkinson_forense():
    return {"p":"neuropsicologia_parkinson_forense","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pericia_neuropsico.get("")
async def i_pericia_neuropsico():
    return {"p":"neuropsicologia_pericia_neuropsico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_perito.get("")
async def i_perito():
    return {"p":"neuropsicologia_perito","s":"ativo","t":datetime.utcnow().isoformat()}
@router_personalidade_tbi.get("")
async def i_personalidade_tbi():
    return {"p":"neuropsicologia_personalidade_tbi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pet_forense.get("")
async def i_pet_forense():
    return {"p":"neuropsicologia_pet_forense","s":"ativo","t":datetime.utcnow().isoformat()}
@router_privilege_forense.get("")
async def i_privilege_forense():
    return {"p":"neuropsicologia_privilege_forense","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pseudo_memoria.get("")
async def i_pseudo_memoria():
    return {"p":"neuropsicologia_pseudo_memoria","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reconhecimento_pesso.get("")
async def i_reconhecimento_pesso():
    return {"p":"neuropsicologia_reconhecimento_pesso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reconhecimento_voz.get("")
async def i_reconhecimento_voz():
    return {"p":"neuropsicologia_reconhecimento_voz","s":"ativo","t":datetime.utcnow().isoformat()}
@router_relatorio_forense.get("")
async def i_relatorio_forense():
    return {"p":"neuropsicologia_relatorio_forense","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reliability_evidence.get("")
async def i_reliability_evidence():
    return {"p":"neuropsicologia_reliability_evidence","s":"ativo","t":datetime.utcnow().isoformat()}
@router_retrograde_amnesia.get("")
async def i_retrograde_amnesia():
    return {"p":"neuropsicologia_retrograde_amnesia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sequelas_tbi.get("")
async def i_sequelas_tbi():
    return {"p":"neuropsicologia_sequelas_tbi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_simulacao_tbi.get("")
async def i_simulacao_tbi():
    return {"p":"neuropsicologia_simulacao_tbi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_spect_forense.get("")
async def i_spect_forense():
    return {"p":"neuropsicologia_spect_forense","s":"ativo","t":datetime.utcnow().isoformat()}
@router_suggestibilidade_adu.get("")
async def i_suggestibilidade_adu():
    return {"p":"neuropsicologia_suggestibilidade_adu","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tarasoff2.get("")
async def i_tarasoff2():
    return {"p":"neuropsicologia_tarasoff2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tbi_forense.get("")
async def i_tbi_forense():
    return {"p":"neuropsicologia_tbi_forense","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tbi_mild.get("")
async def i_tbi_mild():
    return {"p":"neuropsicologia_tbi_mild","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tbi_moderate.get("")
async def i_tbi_moderate():
    return {"p":"neuropsicologia_tbi_moderate","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tbi_severe.get("")
async def i_tbi_severe():
    return {"p":"neuropsicologia_tbi_severe","s":"ativo","t":datetime.utcnow().isoformat()}
@router_testemunho_especiali.get("")
async def i_testemunho_especiali():
    return {"p":"neuropsicologia_testemunho_especiali","s":"ativo","t":datetime.utcnow().isoformat()}
@router_therapeutic_jurispru.get("")
async def i_therapeutic_jurispru():
    return {"p":"neuropsicologia_therapeutic_jurispru","s":"ativo","t":datetime.utcnow().isoformat()}
@router_treatment_vs_evaluat.get("")
async def i_treatment_vs_evaluat():
    return {"p":"neuropsicologia_treatment_vs_evaluat","s":"ativo","t":datetime.utcnow().isoformat()}
@router_validity_evidence.get("")
async def i_validity_evidence():
    return {"p":"neuropsicologia_validity_evidence","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_neuropsicologia_fore(PluginBase):
    name = "consolidated_neuropsicologia_forense"
    def setup(self, app):
        app.include_router(router_admissibility)
        app.include_router(router_alzheimer_forense)
        app.include_router(router_amnesia_dissociativa)
        app.include_router(router_anterograde_amnesia)
        app.include_router(router_auxiliar_justica)
        app.include_router(router_avaliacao_capacidade)
        app.include_router(router_avaliacao_forense_ne)
        app.include_router(router_biomarcadores_forens)
        app.include_router(router_biomarker_tbi)
        app.include_router(router_biometria_forense)
        app.include_router(router_capacidade_contratua)
        app.include_router(router_capacidade_processua)
        app.include_router(router_capacidade_testament)
        app.include_router(router_clinical_vs_forensic)
        app.include_router(router_cognicao_tbi)
        app.include_router(router_comportamento_tbi)
        app.include_router(router_confabulacao_forense)
        app.include_router(router_confidentiality_fore)
        app.include_router(router_cte_forense)
        app.include_router(router_ctf_forense)
        app.include_router(router_daubert_standard)
        app.include_router(router_demencia_forense)
        app.include_router(router_dual_role)
        app.include_router(router_duty_protect)
        app.include_router(router_duty_warn)
        app.include_router(router_eeg_forense)
        app.include_router(router_emocao_tbi)
        app.include_router(router_encefalopatia_forens)
        app.include_router(router_epilepsia_forense)
        app.include_router(router_expert_witness)
        app.include_router(router_eyewitness_adulto)
        app.include_router(router_fmri_forense)
        app.include_router(router_frye_standard)
        app.include_router(router_informed_consent_for)
        app.include_router(router_laudo_neuropsico)
        app.include_router(router_limits_confidentiali)
        app.include_router(router_malingering_tbi)
        app.include_router(router_mandatory_reporting2)
        app.include_router(router_memoria_forense)
        app.include_router(router_mri_forense)
        app.include_router(router_neuroimagem_forense)
        app.include_router(router_parkinson_forense)
        app.include_router(router_pericia_neuropsico)
        app.include_router(router_perito)
        app.include_router(router_personalidade_tbi)
        app.include_router(router_pet_forense)
        app.include_router(router_privilege_forense)
        app.include_router(router_pseudo_memoria)
        app.include_router(router_reconhecimento_pesso)
        app.include_router(router_reconhecimento_voz)
        app.include_router(router_relatorio_forense)
        app.include_router(router_reliability_evidence)
        app.include_router(router_retrograde_amnesia)
        app.include_router(router_sequelas_tbi)
        app.include_router(router_simulacao_tbi)
        app.include_router(router_spect_forense)
        app.include_router(router_suggestibilidade_adu)
        app.include_router(router_tarasoff2)
        app.include_router(router_tbi_forense)
        app.include_router(router_tbi_mild)
        app.include_router(router_tbi_moderate)
        app.include_router(router_tbi_severe)
        app.include_router(router_testemunho_especiali)
        app.include_router(router_therapeutic_jurispru)
        app.include_router(router_treatment_vs_evaluat)
        app.include_router(router_validity_evidence)


plugin = Plugin_neuropsicologia_fore()
