from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_accountability_saude = APIRouter(prefix="/api/v1/saude_mental/accountability_saude", tags=["saude_mental_politicas_avancadas"])
router_acesso_judicial = APIRouter(prefix="/api/v1/saude_mental/acesso_judicial", tags=["saude_mental_politicas_avancadas"])
router_acesso_saude_mental2 = APIRouter(prefix="/api/v1/saude_mental/acesso_saude_mental2", tags=["saude_mental_politicas_avancadas"])
router_anti_manicomial2 = APIRouter(prefix="/api/v1/saude_mental/anti_manicomial2", tags=["saude_mental_politicas_avancadas"])
router_apoio_matricial = APIRouter(prefix="/api/v1/saude_mental/apoio_matricial", tags=["saude_mental_politicas_avancadas"])
router_atenção_primaria_men = APIRouter(prefix="/api/v1/saude_mental/atenção_primaria_mental", tags=["saude_mental_politicas_avancadas"])
router_auditoria_sus = APIRouter(prefix="/api/v1/saude_mental/auditoria_sus", tags=["saude_mental_politicas_avancadas"])
router_avaliacao_tecnologia = APIRouter(prefix="/api/v1/saude_mental/avaliacao_tecnologia_saud", tags=["saude_mental_politicas_avancadas"])
router_caps_avaliacao = APIRouter(prefix="/api/v1/saude_mental/caps_avaliacao", tags=["saude_mental_politicas_avancadas"])
router_conectesus2 = APIRouter(prefix="/api/v1/saude_mental/conectesus2", tags=["saude_mental_politicas_avancadas"])
router_conferencia_saude_me = APIRouter(prefix="/api/v1/saude_mental/conferencia_saude_mental", tags=["saude_mental_politicas_avancadas"])
router_conselho_saude_menta = APIRouter(prefix="/api/v1/saude_mental/conselho_saude_mental", tags=["saude_mental_politicas_avancadas"])
router_controle_social_saud = APIRouter(prefix="/api/v1/saude_mental/controle_social_saude", tags=["saude_mental_politicas_avancadas"])
router_corrupcao_saude = APIRouter(prefix="/api/v1/saude_mental/corrupcao_saude", tags=["saude_mental_politicas_avancadas"])
router_custeio_mental = APIRouter(prefix="/api/v1/saude_mental/custeio_mental", tags=["saude_mental_politicas_avancadas"])
router_desinstitucionalizaç = APIRouter(prefix="/api/v1/saude_mental/desinstitucionalização", tags=["saude_mental_politicas_avancadas"])
router_desvio_verbas_saude = APIRouter(prefix="/api/v1/saude_mental/desvio_verbas_saude", tags=["saude_mental_politicas_avancadas"])
router_direito_saude = APIRouter(prefix="/api/v1/saude_mental/direito_saude", tags=["saude_mental_politicas_avancadas"])
router_diretriz_terapeutica = APIRouter(prefix="/api/v1/saude_mental/diretriz_terapeutica", tags=["saude_mental_politicas_avancadas"])
router_e_sus = APIRouter(prefix="/api/v1/saude_mental/e_sus", tags=["saude_mental_politicas_avancadas"])
router_emenda_saude_mental = APIRouter(prefix="/api/v1/saude_mental/emenda_saude_mental", tags=["saude_mental_politicas_avancadas"])
router_equidade_saude_menta = APIRouter(prefix="/api/v1/saude_mental/equidade_saude_mental", tags=["saude_mental_politicas_avancadas"])
router_financiamento_saude_ = APIRouter(prefix="/api/v1/saude_mental/financiamento_saude_menta", tags=["saude_mental_politicas_avancadas"])
router_fiscalizacao_saude = APIRouter(prefix="/api/v1/saude_mental/fiscalizacao_saude", tags=["saude_mental_politicas_avancadas"])
router_fluxo_atencao = APIRouter(prefix="/api/v1/saude_mental/fluxo_atencao", tags=["saude_mental_politicas_avancadas"])
router_fornecimento_medicam = APIRouter(prefix="/api/v1/saude_mental/fornecimento_medicamentos", tags=["saude_mental_politicas_avancadas"])
router_fundo_saude_mental = APIRouter(prefix="/api/v1/saude_mental/fundo_saude_mental", tags=["saude_mental_politicas_avancadas"])
router_hta_mental = APIRouter(prefix="/api/v1/saude_mental/hta_mental", tags=["saude_mental_politicas_avancadas"])
router_improbidade_saude = APIRouter(prefix="/api/v1/saude_mental/improbidade_saude", tags=["saude_mental_politicas_avancadas"])
router_integralidade_mental = APIRouter(prefix="/api/v1/saude_mental/integralidade_mental", tags=["saude_mental_politicas_avancadas"])
router_internacao_judicial = APIRouter(prefix="/api/v1/saude_mental/internacao_judicial", tags=["saude_mental_politicas_avancadas"])
router_iv_conferencia = APIRouter(prefix="/api/v1/saude_mental/iv_conferencia", tags=["saude_mental_politicas_avancadas"])
router_judicializacao_saude = APIRouter(prefix="/api/v1/saude_mental/judicializacao_saude", tags=["saude_mental_politicas_avancadas"])
router_legislacao_saude_men = APIRouter(prefix="/api/v1/saude_mental/legislacao_saude_mental", tags=["saude_mental_politicas_avancadas"])
router_lei_10216_analise = APIRouter(prefix="/api/v1/saude_mental/lei_10216_analise", tags=["saude_mental_politicas_avancadas"])
router_linha_cuidado_mental = APIRouter(prefix="/api/v1/saude_mental/linha_cuidado_mental", tags=["saude_mental_politicas_avancadas"])
router_luta_antimanicomial = APIRouter(prefix="/api/v1/saude_mental/luta_antimanicomial", tags=["saude_mental_politicas_avancadas"])
router_manicomioje = APIRouter(prefix="/api/v1/saude_mental/manicomioje", tags=["saude_mental_politicas_avancadas"])
router_matriciamento2 = APIRouter(prefix="/api/v1/saude_mental/matriciamento2", tags=["saude_mental_politicas_avancadas"])
router_matriciamento_saude2 = APIRouter(prefix="/api/v1/saude_mental/matriciamento_saude2", tags=["saude_mental_politicas_avancadas"])
router_movimento_sanitarist = APIRouter(prefix="/api/v1/saude_mental/movimento_sanitarista", tags=["saude_mental_politicas_avancadas"])
router_nasf_avaliacao = APIRouter(prefix="/api/v1/saude_mental/nasf_avaliacao", tags=["saude_mental_politicas_avancadas"])
router_orçamento_saude = APIRouter(prefix="/api/v1/saude_mental/orçamento_saude", tags=["saude_mental_politicas_avancadas"])
router_participacao_control = APIRouter(prefix="/api/v1/saude_mental/participacao_controle_soc", tags=["saude_mental_politicas_avancadas"])
router_pcdt_mental = APIRouter(prefix="/api/v1/saude_mental/pcdt_mental", tags=["saude_mental_politicas_avancadas"])
router_plano_nacional_saude = APIRouter(prefix="/api/v1/saude_mental/plano_nacional_saude_ment", tags=["saude_mental_politicas_avancadas"])
router_politica_nacional_sa = APIRouter(prefix="/api/v1/saude_mental/politica_nacional_saude_m", tags=["saude_mental_politicas_avancadas"])
router_politica_saude_menta = APIRouter(prefix="/api/v1/saude_mental/politica_saude_mental2", tags=["saude_mental_politicas_avancadas"])
router_pontos_atencao = APIRouter(prefix="/api/v1/saude_mental/pontos_atencao", tags=["saude_mental_politicas_avancadas"])
router_programa_nacional_sa = APIRouter(prefix="/api/v1/saude_mental/programa_nacional_saude_m", tags=["saude_mental_politicas_avancadas"])
router_prontuario_eletronic = APIRouter(prefix="/api/v1/saude_mental/prontuario_eletronico_sus", tags=["saude_mental_politicas_avancadas"])
router_protocolo_atencao = APIRouter(prefix="/api/v1/saude_mental/protocolo_atencao", tags=["saude_mental_politicas_avancadas"])
router_protocolo_clinico = APIRouter(prefix="/api/v1/saude_mental/protocolo_clinico", tags=["saude_mental_politicas_avancadas"])
router_psicologia_sus = APIRouter(prefix="/api/v1/saude_mental/psicologia_sus", tags=["saude_mental_politicas_avancadas"])
router_psicologo_sus = APIRouter(prefix="/api/v1/saude_mental/psicologo_sus", tags=["saude_mental_politicas_avancadas"])
router_raps_avaliacao = APIRouter(prefix="/api/v1/saude_mental/raps_avaliacao", tags=["saude_mental_politicas_avancadas"])
router_rede_atencao_psicoss = APIRouter(prefix="/api/v1/saude_mental/rede_atencao_psicossocial", tags=["saude_mental_politicas_avancadas"])
router_rede_saude_mental = APIRouter(prefix="/api/v1/saude_mental/rede_saude_mental", tags=["saude_mental_politicas_avancadas"])
router_referencia_contrarre = APIRouter(prefix="/api/v1/saude_mental/referencia_contrarreferen", tags=["saude_mental_politicas_avancadas"])
router_reforma_psiquiatrica = APIRouter(prefix="/api/v1/saude_mental/reforma_psiquiatrica_aval", tags=["saude_mental_politicas_avancadas"])
router_reforma_sanitaria = APIRouter(prefix="/api/v1/saude_mental/reforma_sanitaria", tags=["saude_mental_politicas_avancadas"])
router_regulacao_saude_ment = APIRouter(prefix="/api/v1/saude_mental/regulacao_saude_mental", tags=["saude_mental_politicas_avancadas"])
router_rename_mental = APIRouter(prefix="/api/v1/saude_mental/rename_mental", tags=["saude_mental_politicas_avancadas"])
router_renases_mental = APIRouter(prefix="/api/v1/saude_mental/renases_mental", tags=["saude_mental_politicas_avancadas"])
router_resolutividade_sus = APIRouter(prefix="/api/v1/saude_mental/resolutividade_sus", tags=["saude_mental_politicas_avancadas"])
router_rnds_saude = APIRouter(prefix="/api/v1/saude_mental/rnds_saude", tags=["saude_mental_politicas_avancadas"])
router_saude_digital_sus = APIRouter(prefix="/api/v1/saude_mental/saude_digital_sus", tags=["saude_mental_politicas_avancadas"])
router_saude_digital_sus2 = APIRouter(prefix="/api/v1/saude_mental/saude_digital_sus2", tags=["saude_mental_politicas_avancadas"])
router_sus_avaliacao = APIRouter(prefix="/api/v1/saude_mental/sus_avaliacao", tags=["saude_mental_politicas_avancadas"])
router_tabela_sus_mental = APIRouter(prefix="/api/v1/saude_mental/tabela_sus_mental", tags=["saude_mental_politicas_avancadas"])
router_telepsiquiatria_sus2 = APIRouter(prefix="/api/v1/saude_mental/telepsiquiatria_sus2", tags=["saude_mental_politicas_avancadas"])
router_telessaude_mental = APIRouter(prefix="/api/v1/saude_mental/telessaude_mental", tags=["saude_mental_politicas_avancadas"])
router_transparencia_saude = APIRouter(prefix="/api/v1/saude_mental/transparencia_saude", tags=["saude_mental_politicas_avancadas"])
router_tratamento_compulsor = APIRouter(prefix="/api/v1/saude_mental/tratamento_compulsorio_ju", tags=["saude_mental_politicas_avancadas"])
router_universalidade_menta = APIRouter(prefix="/api/v1/saude_mental/universalidade_mental", tags=["saude_mental_politicas_avancadas"])
router_v_conferencia = APIRouter(prefix="/api/v1/saude_mental/v_conferencia", tags=["saude_mental_politicas_avancadas"])
router_vi_conferencia = APIRouter(prefix="/api/v1/saude_mental/vi_conferencia", tags=["saude_mental_politicas_avancadas"])

@router_accountability_saude.get("")
async def i_accountability_saude():
    return {"p":"saude_mental_po_accountability_saude","s":"ativo","t":datetime.utcnow().isoformat()}
@router_acesso_judicial.get("")
async def i_acesso_judicial():
    return {"p":"saude_mental_po_acesso_judicial","s":"ativo","t":datetime.utcnow().isoformat()}
@router_acesso_saude_mental2.get("")
async def i_acesso_saude_mental2():
    return {"p":"saude_mental_po_acesso_saude_mental2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_anti_manicomial2.get("")
async def i_anti_manicomial2():
    return {"p":"saude_mental_po_anti_manicomial2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_apoio_matricial.get("")
async def i_apoio_matricial():
    return {"p":"saude_mental_po_apoio_matricial","s":"ativo","t":datetime.utcnow().isoformat()}
@router_atenção_primaria_men.get("")
async def i_atenção_primaria_men():
    return {"p":"saude_mental_po_atenção_primaria_men","s":"ativo","t":datetime.utcnow().isoformat()}
@router_auditoria_sus.get("")
async def i_auditoria_sus():
    return {"p":"saude_mental_po_auditoria_sus","s":"ativo","t":datetime.utcnow().isoformat()}
@router_avaliacao_tecnologia.get("")
async def i_avaliacao_tecnologia():
    return {"p":"saude_mental_po_avaliacao_tecnologia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_caps_avaliacao.get("")
async def i_caps_avaliacao():
    return {"p":"saude_mental_po_caps_avaliacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_conectesus2.get("")
async def i_conectesus2():
    return {"p":"saude_mental_po_conectesus2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_conferencia_saude_me.get("")
async def i_conferencia_saude_me():
    return {"p":"saude_mental_po_conferencia_saude_me","s":"ativo","t":datetime.utcnow().isoformat()}
@router_conselho_saude_menta.get("")
async def i_conselho_saude_menta():
    return {"p":"saude_mental_po_conselho_saude_menta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_controle_social_saud.get("")
async def i_controle_social_saud():
    return {"p":"saude_mental_po_controle_social_saud","s":"ativo","t":datetime.utcnow().isoformat()}
@router_corrupcao_saude.get("")
async def i_corrupcao_saude():
    return {"p":"saude_mental_po_corrupcao_saude","s":"ativo","t":datetime.utcnow().isoformat()}
@router_custeio_mental.get("")
async def i_custeio_mental():
    return {"p":"saude_mental_po_custeio_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_desinstitucionalizaç.get("")
async def i_desinstitucionalizaç():
    return {"p":"saude_mental_po_desinstitucionalizaç","s":"ativo","t":datetime.utcnow().isoformat()}
@router_desvio_verbas_saude.get("")
async def i_desvio_verbas_saude():
    return {"p":"saude_mental_po_desvio_verbas_saude","s":"ativo","t":datetime.utcnow().isoformat()}
@router_direito_saude.get("")
async def i_direito_saude():
    return {"p":"saude_mental_po_direito_saude","s":"ativo","t":datetime.utcnow().isoformat()}
@router_diretriz_terapeutica.get("")
async def i_diretriz_terapeutica():
    return {"p":"saude_mental_po_diretriz_terapeutica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_e_sus.get("")
async def i_e_sus():
    return {"p":"saude_mental_po_e_sus","s":"ativo","t":datetime.utcnow().isoformat()}
@router_emenda_saude_mental.get("")
async def i_emenda_saude_mental():
    return {"p":"saude_mental_po_emenda_saude_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_equidade_saude_menta.get("")
async def i_equidade_saude_menta():
    return {"p":"saude_mental_po_equidade_saude_menta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_financiamento_saude_.get("")
async def i_financiamento_saude_():
    return {"p":"saude_mental_po_financiamento_saude_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fiscalizacao_saude.get("")
async def i_fiscalizacao_saude():
    return {"p":"saude_mental_po_fiscalizacao_saude","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fluxo_atencao.get("")
async def i_fluxo_atencao():
    return {"p":"saude_mental_po_fluxo_atencao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fornecimento_medicam.get("")
async def i_fornecimento_medicam():
    return {"p":"saude_mental_po_fornecimento_medicam","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fundo_saude_mental.get("")
async def i_fundo_saude_mental():
    return {"p":"saude_mental_po_fundo_saude_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hta_mental.get("")
async def i_hta_mental():
    return {"p":"saude_mental_po_hta_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_improbidade_saude.get("")
async def i_improbidade_saude():
    return {"p":"saude_mental_po_improbidade_saude","s":"ativo","t":datetime.utcnow().isoformat()}
@router_integralidade_mental.get("")
async def i_integralidade_mental():
    return {"p":"saude_mental_po_integralidade_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_internacao_judicial.get("")
async def i_internacao_judicial():
    return {"p":"saude_mental_po_internacao_judicial","s":"ativo","t":datetime.utcnow().isoformat()}
@router_iv_conferencia.get("")
async def i_iv_conferencia():
    return {"p":"saude_mental_po_iv_conferencia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_judicializacao_saude.get("")
async def i_judicializacao_saude():
    return {"p":"saude_mental_po_judicializacao_saude","s":"ativo","t":datetime.utcnow().isoformat()}
@router_legislacao_saude_men.get("")
async def i_legislacao_saude_men():
    return {"p":"saude_mental_po_legislacao_saude_men","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lei_10216_analise.get("")
async def i_lei_10216_analise():
    return {"p":"saude_mental_po_lei_10216_analise","s":"ativo","t":datetime.utcnow().isoformat()}
@router_linha_cuidado_mental.get("")
async def i_linha_cuidado_mental():
    return {"p":"saude_mental_po_linha_cuidado_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_luta_antimanicomial.get("")
async def i_luta_antimanicomial():
    return {"p":"saude_mental_po_luta_antimanicomial","s":"ativo","t":datetime.utcnow().isoformat()}
@router_manicomioje.get("")
async def i_manicomioje():
    return {"p":"saude_mental_po_manicomioje","s":"ativo","t":datetime.utcnow().isoformat()}
@router_matriciamento2.get("")
async def i_matriciamento2():
    return {"p":"saude_mental_po_matriciamento2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_matriciamento_saude2.get("")
async def i_matriciamento_saude2():
    return {"p":"saude_mental_po_matriciamento_saude2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_movimento_sanitarist.get("")
async def i_movimento_sanitarist():
    return {"p":"saude_mental_po_movimento_sanitarist","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nasf_avaliacao.get("")
async def i_nasf_avaliacao():
    return {"p":"saude_mental_po_nasf_avaliacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_orçamento_saude.get("")
async def i_orçamento_saude():
    return {"p":"saude_mental_po_orçamento_saude","s":"ativo","t":datetime.utcnow().isoformat()}
@router_participacao_control.get("")
async def i_participacao_control():
    return {"p":"saude_mental_po_participacao_control","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pcdt_mental.get("")
async def i_pcdt_mental():
    return {"p":"saude_mental_po_pcdt_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_plano_nacional_saude.get("")
async def i_plano_nacional_saude():
    return {"p":"saude_mental_po_plano_nacional_saude","s":"ativo","t":datetime.utcnow().isoformat()}
@router_politica_nacional_sa.get("")
async def i_politica_nacional_sa():
    return {"p":"saude_mental_po_politica_nacional_sa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_politica_saude_menta.get("")
async def i_politica_saude_menta():
    return {"p":"saude_mental_po_politica_saude_menta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pontos_atencao.get("")
async def i_pontos_atencao():
    return {"p":"saude_mental_po_pontos_atencao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_programa_nacional_sa.get("")
async def i_programa_nacional_sa():
    return {"p":"saude_mental_po_programa_nacional_sa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_prontuario_eletronic.get("")
async def i_prontuario_eletronic():
    return {"p":"saude_mental_po_prontuario_eletronic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_protocolo_atencao.get("")
async def i_protocolo_atencao():
    return {"p":"saude_mental_po_protocolo_atencao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_protocolo_clinico.get("")
async def i_protocolo_clinico():
    return {"p":"saude_mental_po_protocolo_clinico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicologia_sus.get("")
async def i_psicologia_sus():
    return {"p":"saude_mental_po_psicologia_sus","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicologo_sus.get("")
async def i_psicologo_sus():
    return {"p":"saude_mental_po_psicologo_sus","s":"ativo","t":datetime.utcnow().isoformat()}
@router_raps_avaliacao.get("")
async def i_raps_avaliacao():
    return {"p":"saude_mental_po_raps_avaliacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_rede_atencao_psicoss.get("")
async def i_rede_atencao_psicoss():
    return {"p":"saude_mental_po_rede_atencao_psicoss","s":"ativo","t":datetime.utcnow().isoformat()}
@router_rede_saude_mental.get("")
async def i_rede_saude_mental():
    return {"p":"saude_mental_po_rede_saude_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_referencia_contrarre.get("")
async def i_referencia_contrarre():
    return {"p":"saude_mental_po_referencia_contrarre","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reforma_psiquiatrica.get("")
async def i_reforma_psiquiatrica():
    return {"p":"saude_mental_po_reforma_psiquiatrica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reforma_sanitaria.get("")
async def i_reforma_sanitaria():
    return {"p":"saude_mental_po_reforma_sanitaria","s":"ativo","t":datetime.utcnow().isoformat()}
@router_regulacao_saude_ment.get("")
async def i_regulacao_saude_ment():
    return {"p":"saude_mental_po_regulacao_saude_ment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_rename_mental.get("")
async def i_rename_mental():
    return {"p":"saude_mental_po_rename_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_renases_mental.get("")
async def i_renases_mental():
    return {"p":"saude_mental_po_renases_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_resolutividade_sus.get("")
async def i_resolutividade_sus():
    return {"p":"saude_mental_po_resolutividade_sus","s":"ativo","t":datetime.utcnow().isoformat()}
@router_rnds_saude.get("")
async def i_rnds_saude():
    return {"p":"saude_mental_po_rnds_saude","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_digital_sus.get("")
async def i_saude_digital_sus():
    return {"p":"saude_mental_po_saude_digital_sus","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_digital_sus2.get("")
async def i_saude_digital_sus2():
    return {"p":"saude_mental_po_saude_digital_sus2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sus_avaliacao.get("")
async def i_sus_avaliacao():
    return {"p":"saude_mental_po_sus_avaliacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tabela_sus_mental.get("")
async def i_tabela_sus_mental():
    return {"p":"saude_mental_po_tabela_sus_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_telepsiquiatria_sus2.get("")
async def i_telepsiquiatria_sus2():
    return {"p":"saude_mental_po_telepsiquiatria_sus2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_telessaude_mental.get("")
async def i_telessaude_mental():
    return {"p":"saude_mental_po_telessaude_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_transparencia_saude.get("")
async def i_transparencia_saude():
    return {"p":"saude_mental_po_transparencia_saude","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tratamento_compulsor.get("")
async def i_tratamento_compulsor():
    return {"p":"saude_mental_po_tratamento_compulsor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_universalidade_menta.get("")
async def i_universalidade_menta():
    return {"p":"saude_mental_po_universalidade_menta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_v_conferencia.get("")
async def i_v_conferencia():
    return {"p":"saude_mental_po_v_conferencia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_vi_conferencia.get("")
async def i_vi_conferencia():
    return {"p":"saude_mental_po_vi_conferencia","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_saude_mental_politic(PluginBase):
    name = "consolidated_saude_mental_politicas_avancad"
    def setup(self, app):
        app.include_router(router_accountability_saude)
        app.include_router(router_acesso_judicial)
        app.include_router(router_acesso_saude_mental2)
        app.include_router(router_anti_manicomial2)
        app.include_router(router_apoio_matricial)
        app.include_router(router_atenção_primaria_men)
        app.include_router(router_auditoria_sus)
        app.include_router(router_avaliacao_tecnologia)
        app.include_router(router_caps_avaliacao)
        app.include_router(router_conectesus2)
        app.include_router(router_conferencia_saude_me)
        app.include_router(router_conselho_saude_menta)
        app.include_router(router_controle_social_saud)
        app.include_router(router_corrupcao_saude)
        app.include_router(router_custeio_mental)
        app.include_router(router_desinstitucionalizaç)
        app.include_router(router_desvio_verbas_saude)
        app.include_router(router_direito_saude)
        app.include_router(router_diretriz_terapeutica)
        app.include_router(router_e_sus)
        app.include_router(router_emenda_saude_mental)
        app.include_router(router_equidade_saude_menta)
        app.include_router(router_financiamento_saude_)
        app.include_router(router_fiscalizacao_saude)
        app.include_router(router_fluxo_atencao)
        app.include_router(router_fornecimento_medicam)
        app.include_router(router_fundo_saude_mental)
        app.include_router(router_hta_mental)
        app.include_router(router_improbidade_saude)
        app.include_router(router_integralidade_mental)
        app.include_router(router_internacao_judicial)
        app.include_router(router_iv_conferencia)
        app.include_router(router_judicializacao_saude)
        app.include_router(router_legislacao_saude_men)
        app.include_router(router_lei_10216_analise)
        app.include_router(router_linha_cuidado_mental)
        app.include_router(router_luta_antimanicomial)
        app.include_router(router_manicomioje)
        app.include_router(router_matriciamento2)
        app.include_router(router_matriciamento_saude2)
        app.include_router(router_movimento_sanitarist)
        app.include_router(router_nasf_avaliacao)
        app.include_router(router_orçamento_saude)
        app.include_router(router_participacao_control)
        app.include_router(router_pcdt_mental)
        app.include_router(router_plano_nacional_saude)
        app.include_router(router_politica_nacional_sa)
        app.include_router(router_politica_saude_menta)
        app.include_router(router_pontos_atencao)
        app.include_router(router_programa_nacional_sa)
        app.include_router(router_prontuario_eletronic)
        app.include_router(router_protocolo_atencao)
        app.include_router(router_protocolo_clinico)
        app.include_router(router_psicologia_sus)
        app.include_router(router_psicologo_sus)
        app.include_router(router_raps_avaliacao)
        app.include_router(router_rede_atencao_psicoss)
        app.include_router(router_rede_saude_mental)
        app.include_router(router_referencia_contrarre)
        app.include_router(router_reforma_psiquiatrica)
        app.include_router(router_reforma_sanitaria)
        app.include_router(router_regulacao_saude_ment)
        app.include_router(router_rename_mental)
        app.include_router(router_renases_mental)
        app.include_router(router_resolutividade_sus)
        app.include_router(router_rnds_saude)
        app.include_router(router_saude_digital_sus)
        app.include_router(router_saude_digital_sus2)
        app.include_router(router_sus_avaliacao)
        app.include_router(router_tabela_sus_mental)
        app.include_router(router_telepsiquiatria_sus2)
        app.include_router(router_telessaude_mental)
        app.include_router(router_transparencia_saude)
        app.include_router(router_tratamento_compulsor)
        app.include_router(router_universalidade_menta)
        app.include_router(router_v_conferencia)
        app.include_router(router_vi_conferencia)


plugin = Plugin_saude_mental_politic()
