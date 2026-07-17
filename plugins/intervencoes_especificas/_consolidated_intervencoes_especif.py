from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_aceitacao_dor = APIRouter(prefix="/api/v1/intervencoes/aceitacao_dor", tags=["intervencoes_especificas"])
router_ativacao_depressao = APIRouter(prefix="/api/v1/intervencoes/ativacao_depressao", tags=["intervencoes_especificas"])
router_avoidance_dor = APIRouter(prefix="/api/v1/intervencoes/avoidance_dor", tags=["intervencoes_especificas"])
router_catastrophizing_dor = APIRouter(prefix="/api/v1/intervencoes/catastrophizing_dor", tags=["intervencoes_especificas"])
router_cbt_binge = APIRouter(prefix="/api/v1/intervencoes/cbt_binge", tags=["intervencoes_especificas"])
router_cbt_e_anorexia = APIRouter(prefix="/api/v1/intervencoes/cbt_e_anorexia", tags=["intervencoes_especificas"])
router_cbt_e_bulimia = APIRouter(prefix="/api/v1/intervencoes/cbt_e_bulimia", tags=["intervencoes_especificas"])
router_cbte_transdiag = APIRouter(prefix="/api/v1/intervencoes/cbte_transdiag", tags=["intervencoes_especificas"])
router_cognicoes_toc = APIRouter(prefix="/api/v1/intervencoes/cognicoes_toc", tags=["intervencoes_especificas"])
router_community_reinforcem = APIRouter(prefix="/api/v1/intervencoes/community_reinforcement", tags=["intervencoes_especificas"])
router_comprometimento_dor = APIRouter(prefix="/api/v1/intervencoes/comprometimento_dor", tags=["intervencoes_especificas"])
router_contingency_manageme = APIRouter(prefix="/api/v1/intervencoes/contingency_management", tags=["intervencoes_especificas"])
router_controle_estimulo_so = APIRouter(prefix="/api/v1/intervencoes/controle_estimulo_sono", tags=["intervencoes_especificas"])
router_coping_psicose = APIRouter(prefix="/api/v1/intervencoes/coping_psicose", tags=["intervencoes_especificas"])
router_cpt_completo = APIRouter(prefix="/api/v1/intervencoes/cpt_completo", tags=["intervencoes_especificas"])
router_cra_plus_vouchers = APIRouter(prefix="/api/v1/intervencoes/cra_plus_vouchers", tags=["intervencoes_especificas"])
router_dbt_tca = APIRouter(prefix="/api/v1/intervencoes/dbt_tca", tags=["intervencoes_especificas"])
router_erp_toc = APIRouter(prefix="/api/v1/intervencoes/erp_toc", tags=["intervencoes_especificas"])
router_exposicao_fobia = APIRouter(prefix="/api/v1/intervencoes/exposicao_fobia", tags=["intervencoes_especificas"])
router_family_based_treatme = APIRouter(prefix="/api/v1/intervencoes/family_based_treatment", tags=["intervencoes_especificas"])
router_family_focused_bipol = APIRouter(prefix="/api/v1/intervencoes/family_focused_bipolar", tags=["intervencoes_especificas"])
router_funcionalidade_dor = APIRouter(prefix="/api/v1/intervencoes/funcionalidade_dor", tags=["intervencoes_especificas"])
router_higiene_sono2 = APIRouter(prefix="/api/v1/intervencoes/higiene_sono2", tags=["intervencoes_especificas"])
router_inferencia_toc = APIRouter(prefix="/api/v1/intervencoes/inferencia_toc", tags=["intervencoes_especificas"])
router_intenção_paradoxal_s = APIRouter(prefix="/api/v1/intervencoes/intenção_paradoxal_sono", tags=["intervencoes_especificas"])
router_interoceptiva_panico = APIRouter(prefix="/api/v1/intervencoes/interoceptiva_panico", tags=["intervencoes_especificas"])
router_kinesiofobia = APIRouter(prefix="/api/v1/intervencoes/kinesiofobia", tags=["intervencoes_especificas"])
router_matrix_intensive_out = APIRouter(prefix="/api/v1/intervencoes/matrix_intensive_outpatie", tags=["intervencoes_especificas"])
router_matrix_model = APIRouter(prefix="/api/v1/intervencoes/matrix_model", tags=["intervencoes_especificas"])
router_maudsley_anorexia = APIRouter(prefix="/api/v1/intervencoes/maudsley_anorexia", tags=["intervencoes_especificas"])
router_mindfulness_insonia = APIRouter(prefix="/api/v1/intervencoes/mindfulness_insonia", tags=["intervencoes_especificas"])
router_narrative_exposure2 = APIRouter(prefix="/api/v1/intervencoes/narrative_exposure2", tags=["intervencoes_especificas"])
router_normalizacao_psicose = APIRouter(prefix="/api/v1/intervencoes/normalizacao_psicose", tags=["intervencoes_especificas"])
router_prevencao_resposta_t = APIRouter(prefix="/api/v1/intervencoes/prevencao_resposta_toc", tags=["intervencoes_especificas"])
router_prolonged_exposure2 = APIRouter(prefix="/api/v1/intervencoes/prolonged_exposure2", tags=["intervencoes_especificas"])
router_protocolo_erp = APIRouter(prefix="/api/v1/intervencoes/protocolo_erp", tags=["intervencoes_especificas"])
router_protocolo_fobia_soci = APIRouter(prefix="/api/v1/intervencoes/protocolo_fobia_social", tags=["intervencoes_especificas"])
router_protocolo_panico = APIRouter(prefix="/api/v1/intervencoes/protocolo_panico", tags=["intervencoes_especificas"])
router_psicoeducacao_bipola = APIRouter(prefix="/api/v1/intervencoes/psicoeducacao_bipolar2", tags=["intervencoes_especificas"])
router_relapse_prevention2 = APIRouter(prefix="/api/v1/intervencoes/relapse_prevention2", tags=["intervencoes_especificas"])
router_restricao_sono2 = APIRouter(prefix="/api/v1/intervencoes/restricao_sono2", tags=["intervencoes_especificas"])
router_ritmo_social_bipolar = APIRouter(prefix="/api/v1/intervencoes/ritmo_social_bipolar", tags=["intervencoes_especificas"])
router_rumination_focused = APIRouter(prefix="/api/v1/intervencoes/rumination_focused", tags=["intervencoes_especificas"])
router_situacional_panico = APIRouter(prefix="/api/v1/intervencoes/situacional_panico", tags=["intervencoes_especificas"])
router_social_recovery_psic = APIRouter(prefix="/api/v1/intervencoes/social_recovery_psicose", tags=["intervencoes_especificas"])
router_tcc_abuso_substancia = APIRouter(prefix="/api/v1/intervencoes/tcc_abuso_substancia", tags=["intervencoes_especificas"])
router_tcc_adicao_exercicio = APIRouter(prefix="/api/v1/intervencoes/tcc_adicao_exercicio", tags=["intervencoes_especificas"])
router_tcc_adicao_sexual = APIRouter(prefix="/api/v1/intervencoes/tcc_adicao_sexual", tags=["intervencoes_especificas"])
router_tcc_adicao_trabalho = APIRouter(prefix="/api/v1/intervencoes/tcc_adicao_trabalho", tags=["intervencoes_especificas"])
router_tcc_agorafobia = APIRouter(prefix="/api/v1/intervencoes/tcc_agorafobia", tags=["intervencoes_especificas"])
router_tcc_alcool = APIRouter(prefix="/api/v1/intervencoes/tcc_alcool", tags=["intervencoes_especificas"])
router_tcc_bipolar = APIRouter(prefix="/api/v1/intervencoes/tcc_bipolar", tags=["intervencoes_especificas"])
router_tcc_compulsao_compra = APIRouter(prefix="/api/v1/intervencoes/tcc_compulsao_compras", tags=["intervencoes_especificas"])
router_tcc_delirios = APIRouter(prefix="/api/v1/intervencoes/tcc_delirios", tags=["intervencoes_especificas"])
router_tcc_depressao_grave = APIRouter(prefix="/api/v1/intervencoes/tcc_depressao_grave", tags=["intervencoes_especificas"])
router_tcc_dor_cronica = APIRouter(prefix="/api/v1/intervencoes/tcc_dor_cronica", tags=["intervencoes_especificas"])
router_tcc_drogas = APIRouter(prefix="/api/v1/intervencoes/tcc_drogas", tags=["intervencoes_especificas"])
router_tcc_fobia_social = APIRouter(prefix="/api/v1/intervencoes/tcc_fobia_social", tags=["intervencoes_especificas"])
router_tcc_insonia2 = APIRouter(prefix="/api/v1/intervencoes/tcc_insonia2", tags=["intervencoes_especificas"])
router_tcc_jogo_patologico = APIRouter(prefix="/api/v1/intervencoes/tcc_jogo_patologico", tags=["intervencoes_especificas"])
router_tcc_psicose = APIRouter(prefix="/api/v1/intervencoes/tcc_psicose", tags=["intervencoes_especificas"])
router_tcc_ptsd_completo = APIRouter(prefix="/api/v1/intervencoes/tcc_ptsd_completo", tags=["intervencoes_especificas"])
router_tcc_pânico = APIRouter(prefix="/api/v1/intervencoes/tcc_pânico", tags=["intervencoes_especificas"])
router_tcc_tca = APIRouter(prefix="/api/v1/intervencoes/tcc_tca", tags=["intervencoes_especificas"])
router_tcc_toc = APIRouter(prefix="/api/v1/intervencoes/tcc_toc", tags=["intervencoes_especificas"])
router_tcc_vicio_internet = APIRouter(prefix="/api/v1/intervencoes/tcc_vicio_internet", tags=["intervencoes_especificas"])
router_tcc_vozes = APIRouter(prefix="/api/v1/intervencoes/tcc_vozes", tags=["intervencoes_especificas"])
router_valores_dor = APIRouter(prefix="/api/v1/intervencoes/valores_dor", tags=["intervencoes_especificas"])
router_voucher_based = APIRouter(prefix="/api/v1/intervencoes/voucher_based", tags=["intervencoes_especificas"])

@router_aceitacao_dor.get("")
async def i_aceitacao_dor():
    return {"p":"intervencoes_es_aceitacao_dor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ativacao_depressao.get("")
async def i_ativacao_depressao():
    return {"p":"intervencoes_es_ativacao_depressao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_avoidance_dor.get("")
async def i_avoidance_dor():
    return {"p":"intervencoes_es_avoidance_dor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_catastrophizing_dor.get("")
async def i_catastrophizing_dor():
    return {"p":"intervencoes_es_catastrophizing_dor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cbt_binge.get("")
async def i_cbt_binge():
    return {"p":"intervencoes_es_cbt_binge","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cbt_e_anorexia.get("")
async def i_cbt_e_anorexia():
    return {"p":"intervencoes_es_cbt_e_anorexia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cbt_e_bulimia.get("")
async def i_cbt_e_bulimia():
    return {"p":"intervencoes_es_cbt_e_bulimia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cbte_transdiag.get("")
async def i_cbte_transdiag():
    return {"p":"intervencoes_es_cbte_transdiag","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cognicoes_toc.get("")
async def i_cognicoes_toc():
    return {"p":"intervencoes_es_cognicoes_toc","s":"ativo","t":datetime.utcnow().isoformat()}
@router_community_reinforcem.get("")
async def i_community_reinforcem():
    return {"p":"intervencoes_es_community_reinforcem","s":"ativo","t":datetime.utcnow().isoformat()}
@router_comprometimento_dor.get("")
async def i_comprometimento_dor():
    return {"p":"intervencoes_es_comprometimento_dor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_contingency_manageme.get("")
async def i_contingency_manageme():
    return {"p":"intervencoes_es_contingency_manageme","s":"ativo","t":datetime.utcnow().isoformat()}
@router_controle_estimulo_so.get("")
async def i_controle_estimulo_so():
    return {"p":"intervencoes_es_controle_estimulo_so","s":"ativo","t":datetime.utcnow().isoformat()}
@router_coping_psicose.get("")
async def i_coping_psicose():
    return {"p":"intervencoes_es_coping_psicose","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cpt_completo.get("")
async def i_cpt_completo():
    return {"p":"intervencoes_es_cpt_completo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cra_plus_vouchers.get("")
async def i_cra_plus_vouchers():
    return {"p":"intervencoes_es_cra_plus_vouchers","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dbt_tca.get("")
async def i_dbt_tca():
    return {"p":"intervencoes_es_dbt_tca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_erp_toc.get("")
async def i_erp_toc():
    return {"p":"intervencoes_es_erp_toc","s":"ativo","t":datetime.utcnow().isoformat()}
@router_exposicao_fobia.get("")
async def i_exposicao_fobia():
    return {"p":"intervencoes_es_exposicao_fobia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_family_based_treatme.get("")
async def i_family_based_treatme():
    return {"p":"intervencoes_es_family_based_treatme","s":"ativo","t":datetime.utcnow().isoformat()}
@router_family_focused_bipol.get("")
async def i_family_focused_bipol():
    return {"p":"intervencoes_es_family_focused_bipol","s":"ativo","t":datetime.utcnow().isoformat()}
@router_funcionalidade_dor.get("")
async def i_funcionalidade_dor():
    return {"p":"intervencoes_es_funcionalidade_dor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_higiene_sono2.get("")
async def i_higiene_sono2():
    return {"p":"intervencoes_es_higiene_sono2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_inferencia_toc.get("")
async def i_inferencia_toc():
    return {"p":"intervencoes_es_inferencia_toc","s":"ativo","t":datetime.utcnow().isoformat()}
@router_intenção_paradoxal_s.get("")
async def i_intenção_paradoxal_s():
    return {"p":"intervencoes_es_intenção_paradoxal_s","s":"ativo","t":datetime.utcnow().isoformat()}
@router_interoceptiva_panico.get("")
async def i_interoceptiva_panico():
    return {"p":"intervencoes_es_interoceptiva_panico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_kinesiofobia.get("")
async def i_kinesiofobia():
    return {"p":"intervencoes_es_kinesiofobia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_matrix_intensive_out.get("")
async def i_matrix_intensive_out():
    return {"p":"intervencoes_es_matrix_intensive_out","s":"ativo","t":datetime.utcnow().isoformat()}
@router_matrix_model.get("")
async def i_matrix_model():
    return {"p":"intervencoes_es_matrix_model","s":"ativo","t":datetime.utcnow().isoformat()}
@router_maudsley_anorexia.get("")
async def i_maudsley_anorexia():
    return {"p":"intervencoes_es_maudsley_anorexia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindfulness_insonia.get("")
async def i_mindfulness_insonia():
    return {"p":"intervencoes_es_mindfulness_insonia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_narrative_exposure2.get("")
async def i_narrative_exposure2():
    return {"p":"intervencoes_es_narrative_exposure2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_normalizacao_psicose.get("")
async def i_normalizacao_psicose():
    return {"p":"intervencoes_es_normalizacao_psicose","s":"ativo","t":datetime.utcnow().isoformat()}
@router_prevencao_resposta_t.get("")
async def i_prevencao_resposta_t():
    return {"p":"intervencoes_es_prevencao_resposta_t","s":"ativo","t":datetime.utcnow().isoformat()}
@router_prolonged_exposure2.get("")
async def i_prolonged_exposure2():
    return {"p":"intervencoes_es_prolonged_exposure2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_protocolo_erp.get("")
async def i_protocolo_erp():
    return {"p":"intervencoes_es_protocolo_erp","s":"ativo","t":datetime.utcnow().isoformat()}
@router_protocolo_fobia_soci.get("")
async def i_protocolo_fobia_soci():
    return {"p":"intervencoes_es_protocolo_fobia_soci","s":"ativo","t":datetime.utcnow().isoformat()}
@router_protocolo_panico.get("")
async def i_protocolo_panico():
    return {"p":"intervencoes_es_protocolo_panico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicoeducacao_bipola.get("")
async def i_psicoeducacao_bipola():
    return {"p":"intervencoes_es_psicoeducacao_bipola","s":"ativo","t":datetime.utcnow().isoformat()}
@router_relapse_prevention2.get("")
async def i_relapse_prevention2():
    return {"p":"intervencoes_es_relapse_prevention2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_restricao_sono2.get("")
async def i_restricao_sono2():
    return {"p":"intervencoes_es_restricao_sono2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ritmo_social_bipolar.get("")
async def i_ritmo_social_bipolar():
    return {"p":"intervencoes_es_ritmo_social_bipolar","s":"ativo","t":datetime.utcnow().isoformat()}
@router_rumination_focused.get("")
async def i_rumination_focused():
    return {"p":"intervencoes_es_rumination_focused","s":"ativo","t":datetime.utcnow().isoformat()}
@router_situacional_panico.get("")
async def i_situacional_panico():
    return {"p":"intervencoes_es_situacional_panico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_social_recovery_psic.get("")
async def i_social_recovery_psic():
    return {"p":"intervencoes_es_social_recovery_psic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tcc_abuso_substancia.get("")
async def i_tcc_abuso_substancia():
    return {"p":"intervencoes_es_tcc_abuso_substancia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tcc_adicao_exercicio.get("")
async def i_tcc_adicao_exercicio():
    return {"p":"intervencoes_es_tcc_adicao_exercicio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tcc_adicao_sexual.get("")
async def i_tcc_adicao_sexual():
    return {"p":"intervencoes_es_tcc_adicao_sexual","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tcc_adicao_trabalho.get("")
async def i_tcc_adicao_trabalho():
    return {"p":"intervencoes_es_tcc_adicao_trabalho","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tcc_agorafobia.get("")
async def i_tcc_agorafobia():
    return {"p":"intervencoes_es_tcc_agorafobia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tcc_alcool.get("")
async def i_tcc_alcool():
    return {"p":"intervencoes_es_tcc_alcool","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tcc_bipolar.get("")
async def i_tcc_bipolar():
    return {"p":"intervencoes_es_tcc_bipolar","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tcc_compulsao_compra.get("")
async def i_tcc_compulsao_compra():
    return {"p":"intervencoes_es_tcc_compulsao_compra","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tcc_delirios.get("")
async def i_tcc_delirios():
    return {"p":"intervencoes_es_tcc_delirios","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tcc_depressao_grave.get("")
async def i_tcc_depressao_grave():
    return {"p":"intervencoes_es_tcc_depressao_grave","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tcc_dor_cronica.get("")
async def i_tcc_dor_cronica():
    return {"p":"intervencoes_es_tcc_dor_cronica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tcc_drogas.get("")
async def i_tcc_drogas():
    return {"p":"intervencoes_es_tcc_drogas","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tcc_fobia_social.get("")
async def i_tcc_fobia_social():
    return {"p":"intervencoes_es_tcc_fobia_social","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tcc_insonia2.get("")
async def i_tcc_insonia2():
    return {"p":"intervencoes_es_tcc_insonia2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tcc_jogo_patologico.get("")
async def i_tcc_jogo_patologico():
    return {"p":"intervencoes_es_tcc_jogo_patologico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tcc_psicose.get("")
async def i_tcc_psicose():
    return {"p":"intervencoes_es_tcc_psicose","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tcc_ptsd_completo.get("")
async def i_tcc_ptsd_completo():
    return {"p":"intervencoes_es_tcc_ptsd_completo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tcc_pânico.get("")
async def i_tcc_pânico():
    return {"p":"intervencoes_es_tcc_pânico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tcc_tca.get("")
async def i_tcc_tca():
    return {"p":"intervencoes_es_tcc_tca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tcc_toc.get("")
async def i_tcc_toc():
    return {"p":"intervencoes_es_tcc_toc","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tcc_vicio_internet.get("")
async def i_tcc_vicio_internet():
    return {"p":"intervencoes_es_tcc_vicio_internet","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tcc_vozes.get("")
async def i_tcc_vozes():
    return {"p":"intervencoes_es_tcc_vozes","s":"ativo","t":datetime.utcnow().isoformat()}
@router_valores_dor.get("")
async def i_valores_dor():
    return {"p":"intervencoes_es_valores_dor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_voucher_based.get("")
async def i_voucher_based():
    return {"p":"intervencoes_es_voucher_based","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_intervencoes_especif(PluginBase):
    name = "consolidated_intervencoes_especificas"
    def setup(self, app):
        app.include_router(router_aceitacao_dor)
        app.include_router(router_ativacao_depressao)
        app.include_router(router_avoidance_dor)
        app.include_router(router_catastrophizing_dor)
        app.include_router(router_cbt_binge)
        app.include_router(router_cbt_e_anorexia)
        app.include_router(router_cbt_e_bulimia)
        app.include_router(router_cbte_transdiag)
        app.include_router(router_cognicoes_toc)
        app.include_router(router_community_reinforcem)
        app.include_router(router_comprometimento_dor)
        app.include_router(router_contingency_manageme)
        app.include_router(router_controle_estimulo_so)
        app.include_router(router_coping_psicose)
        app.include_router(router_cpt_completo)
        app.include_router(router_cra_plus_vouchers)
        app.include_router(router_dbt_tca)
        app.include_router(router_erp_toc)
        app.include_router(router_exposicao_fobia)
        app.include_router(router_family_based_treatme)
        app.include_router(router_family_focused_bipol)
        app.include_router(router_funcionalidade_dor)
        app.include_router(router_higiene_sono2)
        app.include_router(router_inferencia_toc)
        app.include_router(router_intenção_paradoxal_s)
        app.include_router(router_interoceptiva_panico)
        app.include_router(router_kinesiofobia)
        app.include_router(router_matrix_intensive_out)
        app.include_router(router_matrix_model)
        app.include_router(router_maudsley_anorexia)
        app.include_router(router_mindfulness_insonia)
        app.include_router(router_narrative_exposure2)
        app.include_router(router_normalizacao_psicose)
        app.include_router(router_prevencao_resposta_t)
        app.include_router(router_prolonged_exposure2)
        app.include_router(router_protocolo_erp)
        app.include_router(router_protocolo_fobia_soci)
        app.include_router(router_protocolo_panico)
        app.include_router(router_psicoeducacao_bipola)
        app.include_router(router_relapse_prevention2)
        app.include_router(router_restricao_sono2)
        app.include_router(router_ritmo_social_bipolar)
        app.include_router(router_rumination_focused)
        app.include_router(router_situacional_panico)
        app.include_router(router_social_recovery_psic)
        app.include_router(router_tcc_abuso_substancia)
        app.include_router(router_tcc_adicao_exercicio)
        app.include_router(router_tcc_adicao_sexual)
        app.include_router(router_tcc_adicao_trabalho)
        app.include_router(router_tcc_agorafobia)
        app.include_router(router_tcc_alcool)
        app.include_router(router_tcc_bipolar)
        app.include_router(router_tcc_compulsao_compra)
        app.include_router(router_tcc_delirios)
        app.include_router(router_tcc_depressao_grave)
        app.include_router(router_tcc_dor_cronica)
        app.include_router(router_tcc_drogas)
        app.include_router(router_tcc_fobia_social)
        app.include_router(router_tcc_insonia2)
        app.include_router(router_tcc_jogo_patologico)
        app.include_router(router_tcc_psicose)
        app.include_router(router_tcc_ptsd_completo)
        app.include_router(router_tcc_pânico)
        app.include_router(router_tcc_tca)
        app.include_router(router_tcc_toc)
        app.include_router(router_tcc_vicio_internet)
        app.include_router(router_tcc_vozes)
        app.include_router(router_valores_dor)
        app.include_router(router_voucher_based)


plugin = Plugin_intervencoes_especif()
