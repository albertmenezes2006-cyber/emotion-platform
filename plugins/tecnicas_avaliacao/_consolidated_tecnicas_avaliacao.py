from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_analise_abc = APIRouter(prefix="/api/v1/tecnicas_ava/analise_abc", tags=["tecnicas_avaliacao"])
router_analise_funcional_co = APIRouter(prefix="/api/v1/tecnicas_ava/analise_funcional_comport", tags=["tecnicas_avaliacao"])
router_antecedente_conseque = APIRouter(prefix="/api/v1/tecnicas_ava/antecedente_consequente", tags=["tecnicas_avaliacao"])
router_auto_monitoramento = APIRouter(prefix="/api/v1/tecnicas_ava/auto_monitoramento", tags=["tecnicas_avaliacao"])
router_autoregistro_clinico = APIRouter(prefix="/api/v1/tecnicas_ava/autoregistro_clinico", tags=["tecnicas_avaliacao"])
router_cadeia_comportamenta = APIRouter(prefix="/api/v1/tecnicas_ava/cadeia_comportamental", tags=["tecnicas_avaliacao"])
router_checklist_comportame = APIRouter(prefix="/api/v1/tecnicas_ava/checklist_comportamental", tags=["tecnicas_avaliacao"])
router_clinician_report = APIRouter(prefix="/api/v1/tecnicas_ava/clinician_report", tags=["tecnicas_avaliacao"])
router_clinimetria_clinica = APIRouter(prefix="/api/v1/tecnicas_ava/clinimetria_clinica", tags=["tecnicas_avaliacao"])
router_convergent_validity = APIRouter(prefix="/api/v1/tecnicas_ava/convergent_validity", tags=["tecnicas_avaliacao"])
router_cutoff_clinico = APIRouter(prefix="/api/v1/tecnicas_ava/cutoff_clinico", tags=["tecnicas_avaliacao"])
router_diagrama_formulacao = APIRouter(prefix="/api/v1/tecnicas_ava/diagrama_formulacao", tags=["tecnicas_avaliacao"])
router_diario_comportamento = APIRouter(prefix="/api/v1/tecnicas_ava/diario_comportamento", tags=["tecnicas_avaliacao"])
router_discriminant_validit = APIRouter(prefix="/api/v1/tecnicas_ava/discriminant_validity", tags=["tecnicas_avaliacao"])
router_ecomapa2 = APIRouter(prefix="/api/v1/tecnicas_ava/ecomapa2", tags=["tecnicas_avaliacao"])
router_entrevista_adolescen = APIRouter(prefix="/api/v1/tecnicas_ava/entrevista_adolescente", tags=["tecnicas_avaliacao"])
router_entrevista_casal = APIRouter(prefix="/api/v1/tecnicas_ava/entrevista_casal", tags=["tecnicas_avaliacao"])
router_entrevista_clinica_e = APIRouter(prefix="/api/v1/tecnicas_ava/entrevista_clinica_estrut", tags=["tecnicas_avaliacao"])
router_entrevista_crianca = APIRouter(prefix="/api/v1/tecnicas_ava/entrevista_crianca", tags=["tecnicas_avaliacao"])
router_entrevista_diagnosti = APIRouter(prefix="/api/v1/tecnicas_ava/entrevista_diagnostica", tags=["tecnicas_avaliacao"])
router_entrevista_familiar = APIRouter(prefix="/api/v1/tecnicas_ava/entrevista_familiar", tags=["tecnicas_avaliacao"])
router_entrevista_historico = APIRouter(prefix="/api/v1/tecnicas_ava/entrevista_historico_clin", tags=["tecnicas_avaliacao"])
router_entrevista_idoso = APIRouter(prefix="/api/v1/tecnicas_ava/entrevista_idoso", tags=["tecnicas_avaliacao"])
router_entrevista_motivacio = APIRouter(prefix="/api/v1/tecnicas_ava/entrevista_motivacional2", tags=["tecnicas_avaliacao"])
router_entrevista_nao_estru = APIRouter(prefix="/api/v1/tecnicas_ava/entrevista_nao_estruturad", tags=["tecnicas_avaliacao"])
router_entrevista_semiestru = APIRouter(prefix="/api/v1/tecnicas_ava/entrevista_semiestruturad", tags=["tecnicas_avaliacao"])
router_escala_grafica = APIRouter(prefix="/api/v1/tecnicas_ava/escala_grafica", tags=["tecnicas_avaliacao"])
router_escala_likert = APIRouter(prefix="/api/v1/tecnicas_ava/escala_likert", tags=["tecnicas_avaliacao"])
router_escala_numerica = APIRouter(prefix="/api/v1/tecnicas_ava/escala_numerica", tags=["tecnicas_avaliacao"])
router_escala_subjetiva_dis = APIRouter(prefix="/api/v1/tecnicas_ava/escala_subjetiva_distress", tags=["tecnicas_avaliacao"])
router_escala_visual_analog = APIRouter(prefix="/api/v1/tecnicas_ava/escala_visual_analogica", tags=["tecnicas_avaliacao"])
router_escalas_clinimetria = APIRouter(prefix="/api/v1/tecnicas_ava/escalas_clinimetria", tags=["tecnicas_avaliacao"])
router_fear_thermometer2 = APIRouter(prefix="/api/v1/tecnicas_ava/fear_thermometer2", tags=["tecnicas_avaliacao"])
router_funcao_comportamento = APIRouter(prefix="/api/v1/tecnicas_ava/funcao_comportamento", tags=["tecnicas_avaliacao"])
router_genograma2 = APIRouter(prefix="/api/v1/tecnicas_ava/genograma2", tags=["tecnicas_avaliacao"])
router_informant_report = APIRouter(prefix="/api/v1/tecnicas_ava/informant_report", tags=["tecnicas_avaliacao"])
router_inventario_cognitivo = APIRouter(prefix="/api/v1/tecnicas_ava/inventario_cognitivo", tags=["tecnicas_avaliacao"])
router_mapa_conceptual = APIRouter(prefix="/api/v1/tecnicas_ava/mapa_conceptual", tags=["tecnicas_avaliacao"])
router_mapa_recursos = APIRouter(prefix="/api/v1/tecnicas_ava/mapa_recursos", tags=["tecnicas_avaliacao"])
router_mapa_rede_social = APIRouter(prefix="/api/v1/tecnicas_ava/mapa_rede_social", tags=["tecnicas_avaliacao"])
router_multi_informant = APIRouter(prefix="/api/v1/tecnicas_ava/multi_informant", tags=["tecnicas_avaliacao"])
router_multi_metodo = APIRouter(prefix="/api/v1/tecnicas_ava/multi_metodo", tags=["tecnicas_avaliacao"])
router_multi_trait_multi_me = APIRouter(prefix="/api/v1/tecnicas_ava/multi_trait_multi_method", tags=["tecnicas_avaliacao"])
router_observacao_clinica = APIRouter(prefix="/api/v1/tecnicas_ava/observacao_clinica", tags=["tecnicas_avaliacao"])
router_observacao_sistemati = APIRouter(prefix="/api/v1/tecnicas_ava/observacao_sistematica", tags=["tecnicas_avaliacao"])
router_outcome_measurement = APIRouter(prefix="/api/v1/tecnicas_ava/outcome_measurement", tags=["tecnicas_avaliacao"])
router_patient_reported_out = APIRouter(prefix="/api/v1/tecnicas_ava/patient_reported_outcomes", tags=["tecnicas_avaliacao"])
router_predictive_validity = APIRouter(prefix="/api/v1/tecnicas_ava/predictive_validity", tags=["tecnicas_avaliacao"])
router_progress_monitoring = APIRouter(prefix="/api/v1/tecnicas_ava/progress_monitoring", tags=["tecnicas_avaliacao"])
router_proxy_report = APIRouter(prefix="/api/v1/tecnicas_ava/proxy_report", tags=["tecnicas_avaliacao"])
router_registro_pensamento_ = APIRouter(prefix="/api/v1/tecnicas_ava/registro_pensamento_auto", tags=["tecnicas_avaliacao"])
router_roc_curve_clinica = APIRouter(prefix="/api/v1/tecnicas_ava/roc_curve_clinica", tags=["tecnicas_avaliacao"])
router_roda_emocoes_clinica = APIRouter(prefix="/api/v1/tecnicas_ava/roda_emocoes_clinica", tags=["tecnicas_avaliacao"])
router_rom2 = APIRouter(prefix="/api/v1/tecnicas_ava/rom2", tags=["tecnicas_avaliacao"])
router_roteiro_entrevista = APIRouter(prefix="/api/v1/tecnicas_ava/roteiro_entrevista", tags=["tecnicas_avaliacao"])
router_sensitivity_specific = APIRouter(prefix="/api/v1/tecnicas_ava/sensitivity_specificity", tags=["tecnicas_avaliacao"])
router_sentimento_lista = APIRouter(prefix="/api/v1/tecnicas_ava/sentimento_lista", tags=["tecnicas_avaliacao"])
router_suds2 = APIRouter(prefix="/api/v1/tecnicas_ava/suds2", tags=["tecnicas_avaliacao"])
router_task_analysis = APIRouter(prefix="/api/v1/tecnicas_ava/task_analysis", tags=["tecnicas_avaliacao"])
router_termometro_emocional = APIRouter(prefix="/api/v1/tecnicas_ava/termometro_emocional", tags=["tecnicas_avaliacao"])
router_timeline_clinica = APIRouter(prefix="/api/v1/tecnicas_ava/timeline_clinica", tags=["tecnicas_avaliacao"])

@router_analise_abc.get("")
async def i_analise_abc():
    return {"p":"tecnicas_avalia_analise_abc","s":"ativo","t":datetime.utcnow().isoformat()}
@router_analise_funcional_co.get("")
async def i_analise_funcional_co():
    return {"p":"tecnicas_avalia_analise_funcional_co","s":"ativo","t":datetime.utcnow().isoformat()}
@router_antecedente_conseque.get("")
async def i_antecedente_conseque():
    return {"p":"tecnicas_avalia_antecedente_conseque","s":"ativo","t":datetime.utcnow().isoformat()}
@router_auto_monitoramento.get("")
async def i_auto_monitoramento():
    return {"p":"tecnicas_avalia_auto_monitoramento","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autoregistro_clinico.get("")
async def i_autoregistro_clinico():
    return {"p":"tecnicas_avalia_autoregistro_clinico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cadeia_comportamenta.get("")
async def i_cadeia_comportamenta():
    return {"p":"tecnicas_avalia_cadeia_comportamenta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_checklist_comportame.get("")
async def i_checklist_comportame():
    return {"p":"tecnicas_avalia_checklist_comportame","s":"ativo","t":datetime.utcnow().isoformat()}
@router_clinician_report.get("")
async def i_clinician_report():
    return {"p":"tecnicas_avalia_clinician_report","s":"ativo","t":datetime.utcnow().isoformat()}
@router_clinimetria_clinica.get("")
async def i_clinimetria_clinica():
    return {"p":"tecnicas_avalia_clinimetria_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_convergent_validity.get("")
async def i_convergent_validity():
    return {"p":"tecnicas_avalia_convergent_validity","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cutoff_clinico.get("")
async def i_cutoff_clinico():
    return {"p":"tecnicas_avalia_cutoff_clinico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_diagrama_formulacao.get("")
async def i_diagrama_formulacao():
    return {"p":"tecnicas_avalia_diagrama_formulacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_diario_comportamento.get("")
async def i_diario_comportamento():
    return {"p":"tecnicas_avalia_diario_comportamento","s":"ativo","t":datetime.utcnow().isoformat()}
@router_discriminant_validit.get("")
async def i_discriminant_validit():
    return {"p":"tecnicas_avalia_discriminant_validit","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ecomapa2.get("")
async def i_ecomapa2():
    return {"p":"tecnicas_avalia_ecomapa2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_entrevista_adolescen.get("")
async def i_entrevista_adolescen():
    return {"p":"tecnicas_avalia_entrevista_adolescen","s":"ativo","t":datetime.utcnow().isoformat()}
@router_entrevista_casal.get("")
async def i_entrevista_casal():
    return {"p":"tecnicas_avalia_entrevista_casal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_entrevista_clinica_e.get("")
async def i_entrevista_clinica_e():
    return {"p":"tecnicas_avalia_entrevista_clinica_e","s":"ativo","t":datetime.utcnow().isoformat()}
@router_entrevista_crianca.get("")
async def i_entrevista_crianca():
    return {"p":"tecnicas_avalia_entrevista_crianca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_entrevista_diagnosti.get("")
async def i_entrevista_diagnosti():
    return {"p":"tecnicas_avalia_entrevista_diagnosti","s":"ativo","t":datetime.utcnow().isoformat()}
@router_entrevista_familiar.get("")
async def i_entrevista_familiar():
    return {"p":"tecnicas_avalia_entrevista_familiar","s":"ativo","t":datetime.utcnow().isoformat()}
@router_entrevista_historico.get("")
async def i_entrevista_historico():
    return {"p":"tecnicas_avalia_entrevista_historico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_entrevista_idoso.get("")
async def i_entrevista_idoso():
    return {"p":"tecnicas_avalia_entrevista_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_entrevista_motivacio.get("")
async def i_entrevista_motivacio():
    return {"p":"tecnicas_avalia_entrevista_motivacio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_entrevista_nao_estru.get("")
async def i_entrevista_nao_estru():
    return {"p":"tecnicas_avalia_entrevista_nao_estru","s":"ativo","t":datetime.utcnow().isoformat()}
@router_entrevista_semiestru.get("")
async def i_entrevista_semiestru():
    return {"p":"tecnicas_avalia_entrevista_semiestru","s":"ativo","t":datetime.utcnow().isoformat()}
@router_escala_grafica.get("")
async def i_escala_grafica():
    return {"p":"tecnicas_avalia_escala_grafica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_escala_likert.get("")
async def i_escala_likert():
    return {"p":"tecnicas_avalia_escala_likert","s":"ativo","t":datetime.utcnow().isoformat()}
@router_escala_numerica.get("")
async def i_escala_numerica():
    return {"p":"tecnicas_avalia_escala_numerica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_escala_subjetiva_dis.get("")
async def i_escala_subjetiva_dis():
    return {"p":"tecnicas_avalia_escala_subjetiva_dis","s":"ativo","t":datetime.utcnow().isoformat()}
@router_escala_visual_analog.get("")
async def i_escala_visual_analog():
    return {"p":"tecnicas_avalia_escala_visual_analog","s":"ativo","t":datetime.utcnow().isoformat()}
@router_escalas_clinimetria.get("")
async def i_escalas_clinimetria():
    return {"p":"tecnicas_avalia_escalas_clinimetria","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fear_thermometer2.get("")
async def i_fear_thermometer2():
    return {"p":"tecnicas_avalia_fear_thermometer2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_funcao_comportamento.get("")
async def i_funcao_comportamento():
    return {"p":"tecnicas_avalia_funcao_comportamento","s":"ativo","t":datetime.utcnow().isoformat()}
@router_genograma2.get("")
async def i_genograma2():
    return {"p":"tecnicas_avalia_genograma2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_informant_report.get("")
async def i_informant_report():
    return {"p":"tecnicas_avalia_informant_report","s":"ativo","t":datetime.utcnow().isoformat()}
@router_inventario_cognitivo.get("")
async def i_inventario_cognitivo():
    return {"p":"tecnicas_avalia_inventario_cognitivo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mapa_conceptual.get("")
async def i_mapa_conceptual():
    return {"p":"tecnicas_avalia_mapa_conceptual","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mapa_recursos.get("")
async def i_mapa_recursos():
    return {"p":"tecnicas_avalia_mapa_recursos","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mapa_rede_social.get("")
async def i_mapa_rede_social():
    return {"p":"tecnicas_avalia_mapa_rede_social","s":"ativo","t":datetime.utcnow().isoformat()}
@router_multi_informant.get("")
async def i_multi_informant():
    return {"p":"tecnicas_avalia_multi_informant","s":"ativo","t":datetime.utcnow().isoformat()}
@router_multi_metodo.get("")
async def i_multi_metodo():
    return {"p":"tecnicas_avalia_multi_metodo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_multi_trait_multi_me.get("")
async def i_multi_trait_multi_me():
    return {"p":"tecnicas_avalia_multi_trait_multi_me","s":"ativo","t":datetime.utcnow().isoformat()}
@router_observacao_clinica.get("")
async def i_observacao_clinica():
    return {"p":"tecnicas_avalia_observacao_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_observacao_sistemati.get("")
async def i_observacao_sistemati():
    return {"p":"tecnicas_avalia_observacao_sistemati","s":"ativo","t":datetime.utcnow().isoformat()}
@router_outcome_measurement.get("")
async def i_outcome_measurement():
    return {"p":"tecnicas_avalia_outcome_measurement","s":"ativo","t":datetime.utcnow().isoformat()}
@router_patient_reported_out.get("")
async def i_patient_reported_out():
    return {"p":"tecnicas_avalia_patient_reported_out","s":"ativo","t":datetime.utcnow().isoformat()}
@router_predictive_validity.get("")
async def i_predictive_validity():
    return {"p":"tecnicas_avalia_predictive_validity","s":"ativo","t":datetime.utcnow().isoformat()}
@router_progress_monitoring.get("")
async def i_progress_monitoring():
    return {"p":"tecnicas_avalia_progress_monitoring","s":"ativo","t":datetime.utcnow().isoformat()}
@router_proxy_report.get("")
async def i_proxy_report():
    return {"p":"tecnicas_avalia_proxy_report","s":"ativo","t":datetime.utcnow().isoformat()}
@router_registro_pensamento_.get("")
async def i_registro_pensamento_():
    return {"p":"tecnicas_avalia_registro_pensamento_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_roc_curve_clinica.get("")
async def i_roc_curve_clinica():
    return {"p":"tecnicas_avalia_roc_curve_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_roda_emocoes_clinica.get("")
async def i_roda_emocoes_clinica():
    return {"p":"tecnicas_avalia_roda_emocoes_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_rom2.get("")
async def i_rom2():
    return {"p":"tecnicas_avalia_rom2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_roteiro_entrevista.get("")
async def i_roteiro_entrevista():
    return {"p":"tecnicas_avalia_roteiro_entrevista","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sensitivity_specific.get("")
async def i_sensitivity_specific():
    return {"p":"tecnicas_avalia_sensitivity_specific","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sentimento_lista.get("")
async def i_sentimento_lista():
    return {"p":"tecnicas_avalia_sentimento_lista","s":"ativo","t":datetime.utcnow().isoformat()}
@router_suds2.get("")
async def i_suds2():
    return {"p":"tecnicas_avalia_suds2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_task_analysis.get("")
async def i_task_analysis():
    return {"p":"tecnicas_avalia_task_analysis","s":"ativo","t":datetime.utcnow().isoformat()}
@router_termometro_emocional.get("")
async def i_termometro_emocional():
    return {"p":"tecnicas_avalia_termometro_emocional","s":"ativo","t":datetime.utcnow().isoformat()}
@router_timeline_clinica.get("")
async def i_timeline_clinica():
    return {"p":"tecnicas_avalia_timeline_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_tecnicas_avaliacao(PluginBase):
    name = "consolidated_tecnicas_avaliacao"
    def setup(self, app):
        app.include_router(router_analise_abc)
        app.include_router(router_analise_funcional_co)
        app.include_router(router_antecedente_conseque)
        app.include_router(router_auto_monitoramento)
        app.include_router(router_autoregistro_clinico)
        app.include_router(router_cadeia_comportamenta)
        app.include_router(router_checklist_comportame)
        app.include_router(router_clinician_report)
        app.include_router(router_clinimetria_clinica)
        app.include_router(router_convergent_validity)
        app.include_router(router_cutoff_clinico)
        app.include_router(router_diagrama_formulacao)
        app.include_router(router_diario_comportamento)
        app.include_router(router_discriminant_validit)
        app.include_router(router_ecomapa2)
        app.include_router(router_entrevista_adolescen)
        app.include_router(router_entrevista_casal)
        app.include_router(router_entrevista_clinica_e)
        app.include_router(router_entrevista_crianca)
        app.include_router(router_entrevista_diagnosti)
        app.include_router(router_entrevista_familiar)
        app.include_router(router_entrevista_historico)
        app.include_router(router_entrevista_idoso)
        app.include_router(router_entrevista_motivacio)
        app.include_router(router_entrevista_nao_estru)
        app.include_router(router_entrevista_semiestru)
        app.include_router(router_escala_grafica)
        app.include_router(router_escala_likert)
        app.include_router(router_escala_numerica)
        app.include_router(router_escala_subjetiva_dis)
        app.include_router(router_escala_visual_analog)
        app.include_router(router_escalas_clinimetria)
        app.include_router(router_fear_thermometer2)
        app.include_router(router_funcao_comportamento)
        app.include_router(router_genograma2)
        app.include_router(router_informant_report)
        app.include_router(router_inventario_cognitivo)
        app.include_router(router_mapa_conceptual)
        app.include_router(router_mapa_recursos)
        app.include_router(router_mapa_rede_social)
        app.include_router(router_multi_informant)
        app.include_router(router_multi_metodo)
        app.include_router(router_multi_trait_multi_me)
        app.include_router(router_observacao_clinica)
        app.include_router(router_observacao_sistemati)
        app.include_router(router_outcome_measurement)
        app.include_router(router_patient_reported_out)
        app.include_router(router_predictive_validity)
        app.include_router(router_progress_monitoring)
        app.include_router(router_proxy_report)
        app.include_router(router_registro_pensamento_)
        app.include_router(router_roc_curve_clinica)
        app.include_router(router_roda_emocoes_clinica)
        app.include_router(router_rom2)
        app.include_router(router_roteiro_entrevista)
        app.include_router(router_sensitivity_specific)
        app.include_router(router_sentimento_lista)
        app.include_router(router_suds2)
        app.include_router(router_task_analysis)
        app.include_router(router_termometro_emocional)
        app.include_router(router_timeline_clinica)


plugin = Plugin_tecnicas_avaliacao()
