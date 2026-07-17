from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_aftercare_suicidio = APIRouter(prefix="/api/v1/intervencao_/aftercare_suicidio", tags=["intervencao_crise_avancada"])
router_ala_psiquiatrica = APIRouter(prefix="/api/v1/intervencao_/ala_psiquiatrica", tags=["intervencao_crise_avancada"])
router_alerta_precoce = APIRouter(prefix="/api/v1/intervencao_/alerta_precoce", tags=["intervencao_crise_avancada"])
router_app_emergencia = APIRouter(prefix="/api/v1/intervencao_/app_emergencia", tags=["intervencao_crise_avancada"])
router_ask_suicide = APIRouter(prefix="/api/v1/intervencao_/ask_suicide", tags=["intervencao_crise_avancada"])
router_beck_scale_ideation = APIRouter(prefix="/api/v1/intervencao_/beck_scale_ideation", tags=["intervencao_crise_avancada"])
router_caps_24h = APIRouter(prefix="/api/v1/intervencao_/caps_24h", tags=["intervencao_crise_avancada"])
router_cerimonia_despedida_ = APIRouter(prefix="/api/v1/intervencao_/cerimonia_despedida_suici", tags=["intervencao_crise_avancada"])
router_chat_emergencia = APIRouter(prefix="/api/v1/intervencao_/chat_emergencia", tags=["intervencao_crise_avancada"])
router_cluster_suicidio = APIRouter(prefix="/api/v1/intervencao_/cluster_suicidio", tags=["intervencao_crise_avancada"])
router_columbia_c_ssrs2 = APIRouter(prefix="/api/v1/intervencao_/columbia_c_ssrs2", tags=["intervencao_crise_avancada"])
router_complicated_grief_su = APIRouter(prefix="/api/v1/intervencao_/complicated_grief_suicide", tags=["intervencao_crise_avancada"])
router_comunicacao_suicidio = APIRouter(prefix="/api/v1/intervencao_/comunicacao_suicidio_midi", tags=["intervencao_crise_avancada"])
router_contagio_suicidio = APIRouter(prefix="/api/v1/intervencao_/contagio_suicidio", tags=["intervencao_crise_avancada"])
router_crise_equipe_mobile = APIRouter(prefix="/api/v1/intervencao_/crise_equipe_mobile", tags=["intervencao_crise_avancada"])
router_efeito_papageno = APIRouter(prefix="/api/v1/intervencao_/efeito_papageno", tags=["intervencao_crise_avancada"])
router_efeito_werther = APIRouter(prefix="/api/v1/intervencao_/efeito_werther", tags=["intervencao_crise_avancada"])
router_estigma_suicidio = APIRouter(prefix="/api/v1/intervencao_/estigma_suicidio", tags=["intervencao_crise_avancada"])
router_follow_up_crise = APIRouter(prefix="/api/v1/intervencao_/follow_up_crise", tags=["intervencao_crise_avancada"])
router_gate_keepers2 = APIRouter(prefix="/api/v1/intervencao_/gate_keepers2", tags=["intervencao_crise_avancada"])
router_gps_emergencia = APIRouter(prefix="/api/v1/intervencao_/gps_emergencia", tags=["intervencao_crise_avancada"])
router_hospitalização_volun = APIRouter(prefix="/api/v1/intervencao_/hospitalização_voluntaria", tags=["intervencao_crise_avancada"])
router_hotlines_emergencia = APIRouter(prefix="/api/v1/intervencao_/hotlines_emergencia", tags=["intervencao_crise_avancada"])
router_ia_predicao_crise = APIRouter(prefix="/api/v1/intervencao_/ia_predicao_crise", tags=["intervencao_crise_avancada"])
router_internacao_emergenci = APIRouter(prefix="/api/v1/intervencao_/internacao_emergencia", tags=["intervencao_crise_avancada"])
router_intervencao_precoce_ = APIRouter(prefix="/api/v1/intervencao_/intervencao_precoce_crise", tags=["intervencao_crise_avancada"])
router_lethal_means_counsel = APIRouter(prefix="/api/v1/intervencao_/lethal_means_counseling", tags=["intervencao_crise_avancada"])
router_manejo_ideacao_ativa = APIRouter(prefix="/api/v1/intervencao_/manejo_ideacao_ativa", tags=["intervencao_crise_avancada"])
router_manejo_ideacao_passi = APIRouter(prefix="/api/v1/intervencao_/manejo_ideacao_passiva", tags=["intervencao_crise_avancada"])
router_memorial_suicidio = APIRouter(prefix="/api/v1/intervencao_/memorial_suicidio", tags=["intervencao_crise_avancada"])
router_patterson_suicidio = APIRouter(prefix="/api/v1/intervencao_/patterson_suicidio", tags=["intervencao_crise_avancada"])
router_plano_seguranca2 = APIRouter(prefix="/api/v1/intervencao_/plano_seguranca2", tags=["intervencao_crise_avancada"])
router_pontes_suicidio = APIRouter(prefix="/api/v1/intervencao_/pontes_suicidio", tags=["intervencao_crise_avancada"])
router_postvention_suicidio = APIRouter(prefix="/api/v1/intervencao_/postvention_suicidio", tags=["intervencao_crise_avancada"])
router_prevencao_meios = APIRouter(prefix="/api/v1/intervencao_/prevencao_meios", tags=["intervencao_crise_avancada"])
router_recuperacao_pos_cris = APIRouter(prefix="/api/v1/intervencao_/recuperacao_pos_crise", tags=["intervencao_crise_avancada"])
router_redes_suicidio = APIRouter(prefix="/api/v1/intervencao_/redes_suicidio", tags=["intervencao_crise_avancada"])
router_reportagem_responsav = APIRouter(prefix="/api/v1/intervencao_/reportagem_responsavel2", tags=["intervencao_crise_avancada"])
router_restricao_armas = APIRouter(prefix="/api/v1/intervencao_/restricao_armas", tags=["intervencao_crise_avancada"])
router_restricao_medicament = APIRouter(prefix="/api/v1/intervencao_/restricao_medicamentos", tags=["intervencao_crise_avancada"])
router_restricao_meios = APIRouter(prefix="/api/v1/intervencao_/restricao_meios", tags=["intervencao_crise_avancada"])
router_restricao_pesticidas = APIRouter(prefix="/api/v1/intervencao_/restricao_pesticidas", tags=["intervencao_crise_avancada"])
router_sad_persons2 = APIRouter(prefix="/api/v1/intervencao_/sad_persons2", tags=["intervencao_crise_avancada"])
router_safe_t_protocol = APIRouter(prefix="/api/v1/intervencao_/safe_t_protocol", tags=["intervencao_crise_avancada"])
router_samu_mental2 = APIRouter(prefix="/api/v1/intervencao_/samu_mental2", tags=["intervencao_crise_avancada"])
router_sms_emergencia = APIRouter(prefix="/api/v1/intervencao_/sms_emergencia", tags=["intervencao_crise_avancada"])
router_ssrs_completo = APIRouter(prefix="/api/v1/intervencao_/ssrs_completo", tags=["intervencao_crise_avancada"])
router_survivors_suicide = APIRouter(prefix="/api/v1/intervencao_/survivors_suicide", tags=["intervencao_crise_avancada"])
router_triagem_suicidio = APIRouter(prefix="/api/v1/intervencao_/triagem_suicidio", tags=["intervencao_crise_avancada"])
router_upa_psiquiatrica = APIRouter(prefix="/api/v1/intervencao_/upa_psiquiatrica", tags=["intervencao_crise_avancada"])
router_wearable_crise = APIRouter(prefix="/api/v1/intervencao_/wearable_crise", tags=["intervencao_crise_avancada"])

@router_aftercare_suicidio.get("")
async def i_aftercare_suicidio():
    return {"p":"intervencao_cri_aftercare_suicidio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ala_psiquiatrica.get("")
async def i_ala_psiquiatrica():
    return {"p":"intervencao_cri_ala_psiquiatrica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_alerta_precoce.get("")
async def i_alerta_precoce():
    return {"p":"intervencao_cri_alerta_precoce","s":"ativo","t":datetime.utcnow().isoformat()}
@router_app_emergencia.get("")
async def i_app_emergencia():
    return {"p":"intervencao_cri_app_emergencia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ask_suicide.get("")
async def i_ask_suicide():
    return {"p":"intervencao_cri_ask_suicide","s":"ativo","t":datetime.utcnow().isoformat()}
@router_beck_scale_ideation.get("")
async def i_beck_scale_ideation():
    return {"p":"intervencao_cri_beck_scale_ideation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_caps_24h.get("")
async def i_caps_24h():
    return {"p":"intervencao_cri_caps_24h","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cerimonia_despedida_.get("")
async def i_cerimonia_despedida_():
    return {"p":"intervencao_cri_cerimonia_despedida_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_chat_emergencia.get("")
async def i_chat_emergencia():
    return {"p":"intervencao_cri_chat_emergencia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cluster_suicidio.get("")
async def i_cluster_suicidio():
    return {"p":"intervencao_cri_cluster_suicidio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_columbia_c_ssrs2.get("")
async def i_columbia_c_ssrs2():
    return {"p":"intervencao_cri_columbia_c_ssrs2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_complicated_grief_su.get("")
async def i_complicated_grief_su():
    return {"p":"intervencao_cri_complicated_grief_su","s":"ativo","t":datetime.utcnow().isoformat()}
@router_comunicacao_suicidio.get("")
async def i_comunicacao_suicidio():
    return {"p":"intervencao_cri_comunicacao_suicidio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_contagio_suicidio.get("")
async def i_contagio_suicidio():
    return {"p":"intervencao_cri_contagio_suicidio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_crise_equipe_mobile.get("")
async def i_crise_equipe_mobile():
    return {"p":"intervencao_cri_crise_equipe_mobile","s":"ativo","t":datetime.utcnow().isoformat()}
@router_efeito_papageno.get("")
async def i_efeito_papageno():
    return {"p":"intervencao_cri_efeito_papageno","s":"ativo","t":datetime.utcnow().isoformat()}
@router_efeito_werther.get("")
async def i_efeito_werther():
    return {"p":"intervencao_cri_efeito_werther","s":"ativo","t":datetime.utcnow().isoformat()}
@router_estigma_suicidio.get("")
async def i_estigma_suicidio():
    return {"p":"intervencao_cri_estigma_suicidio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_follow_up_crise.get("")
async def i_follow_up_crise():
    return {"p":"intervencao_cri_follow_up_crise","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gate_keepers2.get("")
async def i_gate_keepers2():
    return {"p":"intervencao_cri_gate_keepers2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gps_emergencia.get("")
async def i_gps_emergencia():
    return {"p":"intervencao_cri_gps_emergencia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hospitalização_volun.get("")
async def i_hospitalização_volun():
    return {"p":"intervencao_cri_hospitalização_volun","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hotlines_emergencia.get("")
async def i_hotlines_emergencia():
    return {"p":"intervencao_cri_hotlines_emergencia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ia_predicao_crise.get("")
async def i_ia_predicao_crise():
    return {"p":"intervencao_cri_ia_predicao_crise","s":"ativo","t":datetime.utcnow().isoformat()}
@router_internacao_emergenci.get("")
async def i_internacao_emergenci():
    return {"p":"intervencao_cri_internacao_emergenci","s":"ativo","t":datetime.utcnow().isoformat()}
@router_intervencao_precoce_.get("")
async def i_intervencao_precoce_():
    return {"p":"intervencao_cri_intervencao_precoce_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lethal_means_counsel.get("")
async def i_lethal_means_counsel():
    return {"p":"intervencao_cri_lethal_means_counsel","s":"ativo","t":datetime.utcnow().isoformat()}
@router_manejo_ideacao_ativa.get("")
async def i_manejo_ideacao_ativa():
    return {"p":"intervencao_cri_manejo_ideacao_ativa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_manejo_ideacao_passi.get("")
async def i_manejo_ideacao_passi():
    return {"p":"intervencao_cri_manejo_ideacao_passi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_memorial_suicidio.get("")
async def i_memorial_suicidio():
    return {"p":"intervencao_cri_memorial_suicidio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_patterson_suicidio.get("")
async def i_patterson_suicidio():
    return {"p":"intervencao_cri_patterson_suicidio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_plano_seguranca2.get("")
async def i_plano_seguranca2():
    return {"p":"intervencao_cri_plano_seguranca2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pontes_suicidio.get("")
async def i_pontes_suicidio():
    return {"p":"intervencao_cri_pontes_suicidio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_postvention_suicidio.get("")
async def i_postvention_suicidio():
    return {"p":"intervencao_cri_postvention_suicidio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_prevencao_meios.get("")
async def i_prevencao_meios():
    return {"p":"intervencao_cri_prevencao_meios","s":"ativo","t":datetime.utcnow().isoformat()}
@router_recuperacao_pos_cris.get("")
async def i_recuperacao_pos_cris():
    return {"p":"intervencao_cri_recuperacao_pos_cris","s":"ativo","t":datetime.utcnow().isoformat()}
@router_redes_suicidio.get("")
async def i_redes_suicidio():
    return {"p":"intervencao_cri_redes_suicidio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reportagem_responsav.get("")
async def i_reportagem_responsav():
    return {"p":"intervencao_cri_reportagem_responsav","s":"ativo","t":datetime.utcnow().isoformat()}
@router_restricao_armas.get("")
async def i_restricao_armas():
    return {"p":"intervencao_cri_restricao_armas","s":"ativo","t":datetime.utcnow().isoformat()}
@router_restricao_medicament.get("")
async def i_restricao_medicament():
    return {"p":"intervencao_cri_restricao_medicament","s":"ativo","t":datetime.utcnow().isoformat()}
@router_restricao_meios.get("")
async def i_restricao_meios():
    return {"p":"intervencao_cri_restricao_meios","s":"ativo","t":datetime.utcnow().isoformat()}
@router_restricao_pesticidas.get("")
async def i_restricao_pesticidas():
    return {"p":"intervencao_cri_restricao_pesticidas","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sad_persons2.get("")
async def i_sad_persons2():
    return {"p":"intervencao_cri_sad_persons2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_safe_t_protocol.get("")
async def i_safe_t_protocol():
    return {"p":"intervencao_cri_safe_t_protocol","s":"ativo","t":datetime.utcnow().isoformat()}
@router_samu_mental2.get("")
async def i_samu_mental2():
    return {"p":"intervencao_cri_samu_mental2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sms_emergencia.get("")
async def i_sms_emergencia():
    return {"p":"intervencao_cri_sms_emergencia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ssrs_completo.get("")
async def i_ssrs_completo():
    return {"p":"intervencao_cri_ssrs_completo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_survivors_suicide.get("")
async def i_survivors_suicide():
    return {"p":"intervencao_cri_survivors_suicide","s":"ativo","t":datetime.utcnow().isoformat()}
@router_triagem_suicidio.get("")
async def i_triagem_suicidio():
    return {"p":"intervencao_cri_triagem_suicidio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_upa_psiquiatrica.get("")
async def i_upa_psiquiatrica():
    return {"p":"intervencao_cri_upa_psiquiatrica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_wearable_crise.get("")
async def i_wearable_crise():
    return {"p":"intervencao_cri_wearable_crise","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_intervencao_crise_av(PluginBase):
    name = "consolidated_intervencao_crise_avancada"
    def setup(self, app):
        app.include_router(router_aftercare_suicidio)
        app.include_router(router_ala_psiquiatrica)
        app.include_router(router_alerta_precoce)
        app.include_router(router_app_emergencia)
        app.include_router(router_ask_suicide)
        app.include_router(router_beck_scale_ideation)
        app.include_router(router_caps_24h)
        app.include_router(router_cerimonia_despedida_)
        app.include_router(router_chat_emergencia)
        app.include_router(router_cluster_suicidio)
        app.include_router(router_columbia_c_ssrs2)
        app.include_router(router_complicated_grief_su)
        app.include_router(router_comunicacao_suicidio)
        app.include_router(router_contagio_suicidio)
        app.include_router(router_crise_equipe_mobile)
        app.include_router(router_efeito_papageno)
        app.include_router(router_efeito_werther)
        app.include_router(router_estigma_suicidio)
        app.include_router(router_follow_up_crise)
        app.include_router(router_gate_keepers2)
        app.include_router(router_gps_emergencia)
        app.include_router(router_hospitalização_volun)
        app.include_router(router_hotlines_emergencia)
        app.include_router(router_ia_predicao_crise)
        app.include_router(router_internacao_emergenci)
        app.include_router(router_intervencao_precoce_)
        app.include_router(router_lethal_means_counsel)
        app.include_router(router_manejo_ideacao_ativa)
        app.include_router(router_manejo_ideacao_passi)
        app.include_router(router_memorial_suicidio)
        app.include_router(router_patterson_suicidio)
        app.include_router(router_plano_seguranca2)
        app.include_router(router_pontes_suicidio)
        app.include_router(router_postvention_suicidio)
        app.include_router(router_prevencao_meios)
        app.include_router(router_recuperacao_pos_cris)
        app.include_router(router_redes_suicidio)
        app.include_router(router_reportagem_responsav)
        app.include_router(router_restricao_armas)
        app.include_router(router_restricao_medicament)
        app.include_router(router_restricao_meios)
        app.include_router(router_restricao_pesticidas)
        app.include_router(router_sad_persons2)
        app.include_router(router_safe_t_protocol)
        app.include_router(router_samu_mental2)
        app.include_router(router_sms_emergencia)
        app.include_router(router_ssrs_completo)
        app.include_router(router_survivors_suicide)
        app.include_router(router_triagem_suicidio)
        app.include_router(router_upa_psiquiatrica)
        app.include_router(router_wearable_crise)


plugin = Plugin_intervencao_crise_av()
