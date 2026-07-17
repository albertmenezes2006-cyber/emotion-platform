from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_abuso_narcisista = APIRouter(prefix="/api/v1/psicologia_c/abuso_narcisista", tags=["psicologia_clinica"])
router_adulto_saudavel_sche = APIRouter(prefix="/api/v1/psicologia_c/adulto_saudavel_schema", tags=["psicologia_clinica"])
router_antisocial_terapia = APIRouter(prefix="/api/v1/psicologia_c/antisocial_terapia", tags=["psicologia_clinica"])
router_apego_ansioso_adulto = APIRouter(prefix="/api/v1/psicologia_c/apego_ansioso_adulto", tags=["psicologia_clinica"])
router_apego_desorganizado_ = APIRouter(prefix="/api/v1/psicologia_c/apego_desorganizado_clini", tags=["psicologia_clinica"])
router_apego_evitativo_adul = APIRouter(prefix="/api/v1/psicologia_c/apego_evitativo_adulto", tags=["psicologia_clinica"])
router_apego_fearful_avoida = APIRouter(prefix="/api/v1/psicologia_c/apego_fearful_avoidant", tags=["psicologia_clinica"])
router_apego_seguro_adulto = APIRouter(prefix="/api/v1/psicologia_c/apego_seguro_adulto", tags=["psicologia_clinica"])
router_attachment_styles_qu = APIRouter(prefix="/api/v1/psicologia_c/attachment_styles_quiz", tags=["psicologia_clinica"])
router_borderline_terapia = APIRouter(prefix="/api/v1/psicologia_c/borderline_terapia", tags=["psicologia_clinica"])
router_carta_schema = APIRouter(prefix="/api/v1/psicologia_c/carta_schema", tags=["psicologia_clinica"])
router_chair_work_schema = APIRouter(prefix="/api/v1/psicologia_c/chair_work_schema", tags=["psicologia_clinica"])
router_codependencia_clinic = APIRouter(prefix="/api/v1/psicologia_c/codependencia_clinica", tags=["psicologia_clinica"])
router_coercao_controle = APIRouter(prefix="/api/v1/psicologia_c/coercao_controle", tags=["psicologia_clinica"])
router_crianca_raivosa = APIRouter(prefix="/api/v1/psicologia_c/crianca_raivosa", tags=["psicologia_clinica"])
router_crianca_vulneravel = APIRouter(prefix="/api/v1/psicologia_c/crianca_vulneravel", tags=["psicologia_clinica"])
router_dark_triad_clinico = APIRouter(prefix="/api/v1/psicologia_c/dark_triad_clinico", tags=["psicologia_clinica"])
router_dependente_clinico = APIRouter(prefix="/api/v1/psicologia_c/dependente_clinico", tags=["psicologia_clinica"])
router_diario_schema = APIRouter(prefix="/api/v1/psicologia_c/diario_schema", tags=["psicologia_clinica"])
router_eft_casal = APIRouter(prefix="/api/v1/psicologia_c/eft_casal", tags=["psicologia_clinica"])
router_enmeshment_clinico = APIRouter(prefix="/api/v1/psicologia_c/enmeshment_clinico", tags=["psicologia_clinica"])
router_esquemas_precoces = APIRouter(prefix="/api/v1/psicologia_c/esquemas_precoces", tags=["psicologia_clinica"])
router_esquizoide_clinico = APIRouter(prefix="/api/v1/psicologia_c/esquizoide_clinico", tags=["psicologia_clinica"])
router_esquizotipal = APIRouter(prefix="/api/v1/psicologia_c/esquizotipal", tags=["psicologia_clinica"])
router_evitativo_clinico = APIRouter(prefix="/api/v1/psicologia_c/evitativo_clinico", tags=["psicologia_clinica"])
router_flash_card_schema = APIRouter(prefix="/api/v1/psicologia_c/flash_card_schema", tags=["psicologia_clinica"])
router_fusao_identidade = APIRouter(prefix="/api/v1/psicologia_c/fusao_identidade", tags=["psicologia_clinica"])
router_gaslighting_clinico = APIRouter(prefix="/api/v1/psicologia_c/gaslighting_clinico", tags=["psicologia_clinica"])
router_histrionico = APIRouter(prefix="/api/v1/psicologia_c/histrionico", tags=["psicologia_clinica"])
router_imagery_rescripting = APIRouter(prefix="/api/v1/psicologia_c/imagery_rescripting", tags=["psicologia_clinica"])
router_internal_working_mod = APIRouter(prefix="/api/v1/psicologia_c/internal_working_models", tags=["psicologia_clinica"])
router_manipulacao_psico = APIRouter(prefix="/api/v1/psicologia_c/manipulacao_psico", tags=["psicologia_clinica"])
router_mode_work = APIRouter(prefix="/api/v1/psicologia_c/mode_work", tags=["psicologia_clinica"])
router_modelos_operantes_in = APIRouter(prefix="/api/v1/psicologia_c/modelos_operantes_interno", tags=["psicologia_clinica"])
router_modos_esquema = APIRouter(prefix="/api/v1/psicologia_c/modos_esquema", tags=["psicologia_clinica"])
router_narcisista_terapia = APIRouter(prefix="/api/v1/psicologia_c/narcisista_terapia", tags=["psicologia_clinica"])
router_obsessivo_compulsivo = APIRouter(prefix="/api/v1/psicologia_c/obsessivo_compulsivo_pers", tags=["psicologia_clinica"])
router_pai_punitivo = APIRouter(prefix="/api/v1/psicologia_c/pai_punitivo", tags=["psicologia_clinica"])
router_paranoia_clinica = APIRouter(prefix="/api/v1/psicologia_c/paranoia_clinica", tags=["psicologia_clinica"])
router_protetor_distante = APIRouter(prefix="/api/v1/psicologia_c/protetor_distante", tags=["psicologia_clinica"])
router_psicopatia_avaliacao = APIRouter(prefix="/api/v1/psicologia_c/psicopatia_avaliacao", tags=["psicologia_clinica"])
router_recuperacao_narcisis = APIRouter(prefix="/api/v1/psicologia_c/recuperacao_narcisismo", tags=["psicologia_clinica"])
router_reparo_apego = APIRouter(prefix="/api/v1/psicologia_c/reparo_apego", tags=["psicologia_clinica"])
router_representacoes_menta = APIRouter(prefix="/api/v1/psicologia_c/representacoes_mentais", tags=["psicologia_clinica"])
router_schema_casais = APIRouter(prefix="/api/v1/psicologia_c/schema_casais", tags=["psicologia_clinica"])
router_schema_familia = APIRouter(prefix="/api/v1/psicologia_c/schema_familia", tags=["psicologia_clinica"])
router_simbiose_psicologica = APIRouter(prefix="/api/v1/psicologia_c/simbiose_psicologica", tags=["psicologia_clinica"])
router_sociopatia_info = APIRouter(prefix="/api/v1/psicologia_c/sociopatia_info", tags=["psicologia_clinica"])
router_teoria_apego_adulto = APIRouter(prefix="/api/v1/psicologia_c/teoria_apego_adulto", tags=["psicologia_clinica"])
router_terapia_baseada_apeg = APIRouter(prefix="/api/v1/psicologia_c/terapia_baseada_apego", tags=["psicologia_clinica"])
router_terapia_schema_grupo = APIRouter(prefix="/api/v1/psicologia_c/terapia_schema_grupo", tags=["psicologia_clinica"])
router_transtorno_personali = APIRouter(prefix="/api/v1/psicologia_c/transtorno_personalidade_", tags=["psicologia_clinica"])
router_transtorno_personali = APIRouter(prefix="/api/v1/psicologia_c/transtorno_personalidade_", tags=["psicologia_clinica"])
router_transtorno_personali = APIRouter(prefix="/api/v1/psicologia_c/transtorno_personalidade_", tags=["psicologia_clinica"])
router_trauma_apego = APIRouter(prefix="/api/v1/psicologia_c/trauma_apego", tags=["psicologia_clinica"])
router_trauma_narcisista = APIRouter(prefix="/api/v1/psicologia_c/trauma_narcisista", tags=["psicologia_clinica"])
router_trilogia_escura = APIRouter(prefix="/api/v1/psicologia_c/trilogia_escura", tags=["psicologia_clinica"])

@router_abuso_narcisista.get("")
async def i_abuso_narcisista():
    return {"p":"psicologia_clin_abuso_narcisista","s":"ativo","t":datetime.utcnow().isoformat()}
@router_adulto_saudavel_sche.get("")
async def i_adulto_saudavel_sche():
    return {"p":"psicologia_clin_adulto_saudavel_sche","s":"ativo","t":datetime.utcnow().isoformat()}
@router_antisocial_terapia.get("")
async def i_antisocial_terapia():
    return {"p":"psicologia_clin_antisocial_terapia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_apego_ansioso_adulto.get("")
async def i_apego_ansioso_adulto():
    return {"p":"psicologia_clin_apego_ansioso_adulto","s":"ativo","t":datetime.utcnow().isoformat()}
@router_apego_desorganizado_.get("")
async def i_apego_desorganizado_():
    return {"p":"psicologia_clin_apego_desorganizado_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_apego_evitativo_adul.get("")
async def i_apego_evitativo_adul():
    return {"p":"psicologia_clin_apego_evitativo_adul","s":"ativo","t":datetime.utcnow().isoformat()}
@router_apego_fearful_avoida.get("")
async def i_apego_fearful_avoida():
    return {"p":"psicologia_clin_apego_fearful_avoida","s":"ativo","t":datetime.utcnow().isoformat()}
@router_apego_seguro_adulto.get("")
async def i_apego_seguro_adulto():
    return {"p":"psicologia_clin_apego_seguro_adulto","s":"ativo","t":datetime.utcnow().isoformat()}
@router_attachment_styles_qu.get("")
async def i_attachment_styles_qu():
    return {"p":"psicologia_clin_attachment_styles_qu","s":"ativo","t":datetime.utcnow().isoformat()}
@router_borderline_terapia.get("")
async def i_borderline_terapia():
    return {"p":"psicologia_clin_borderline_terapia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_carta_schema.get("")
async def i_carta_schema():
    return {"p":"psicologia_clin_carta_schema","s":"ativo","t":datetime.utcnow().isoformat()}
@router_chair_work_schema.get("")
async def i_chair_work_schema():
    return {"p":"psicologia_clin_chair_work_schema","s":"ativo","t":datetime.utcnow().isoformat()}
@router_codependencia_clinic.get("")
async def i_codependencia_clinic():
    return {"p":"psicologia_clin_codependencia_clinic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_coercao_controle.get("")
async def i_coercao_controle():
    return {"p":"psicologia_clin_coercao_controle","s":"ativo","t":datetime.utcnow().isoformat()}
@router_crianca_raivosa.get("")
async def i_crianca_raivosa():
    return {"p":"psicologia_clin_crianca_raivosa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_crianca_vulneravel.get("")
async def i_crianca_vulneravel():
    return {"p":"psicologia_clin_crianca_vulneravel","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dark_triad_clinico.get("")
async def i_dark_triad_clinico():
    return {"p":"psicologia_clin_dark_triad_clinico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dependente_clinico.get("")
async def i_dependente_clinico():
    return {"p":"psicologia_clin_dependente_clinico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_diario_schema.get("")
async def i_diario_schema():
    return {"p":"psicologia_clin_diario_schema","s":"ativo","t":datetime.utcnow().isoformat()}
@router_eft_casal.get("")
async def i_eft_casal():
    return {"p":"psicologia_clin_eft_casal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_enmeshment_clinico.get("")
async def i_enmeshment_clinico():
    return {"p":"psicologia_clin_enmeshment_clinico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_esquemas_precoces.get("")
async def i_esquemas_precoces():
    return {"p":"psicologia_clin_esquemas_precoces","s":"ativo","t":datetime.utcnow().isoformat()}
@router_esquizoide_clinico.get("")
async def i_esquizoide_clinico():
    return {"p":"psicologia_clin_esquizoide_clinico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_esquizotipal.get("")
async def i_esquizotipal():
    return {"p":"psicologia_clin_esquizotipal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_evitativo_clinico.get("")
async def i_evitativo_clinico():
    return {"p":"psicologia_clin_evitativo_clinico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_flash_card_schema.get("")
async def i_flash_card_schema():
    return {"p":"psicologia_clin_flash_card_schema","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fusao_identidade.get("")
async def i_fusao_identidade():
    return {"p":"psicologia_clin_fusao_identidade","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gaslighting_clinico.get("")
async def i_gaslighting_clinico():
    return {"p":"psicologia_clin_gaslighting_clinico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_histrionico.get("")
async def i_histrionico():
    return {"p":"psicologia_clin_histrionico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_imagery_rescripting.get("")
async def i_imagery_rescripting():
    return {"p":"psicologia_clin_imagery_rescripting","s":"ativo","t":datetime.utcnow().isoformat()}
@router_internal_working_mod.get("")
async def i_internal_working_mod():
    return {"p":"psicologia_clin_internal_working_mod","s":"ativo","t":datetime.utcnow().isoformat()}
@router_manipulacao_psico.get("")
async def i_manipulacao_psico():
    return {"p":"psicologia_clin_manipulacao_psico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mode_work.get("")
async def i_mode_work():
    return {"p":"psicologia_clin_mode_work","s":"ativo","t":datetime.utcnow().isoformat()}
@router_modelos_operantes_in.get("")
async def i_modelos_operantes_in():
    return {"p":"psicologia_clin_modelos_operantes_in","s":"ativo","t":datetime.utcnow().isoformat()}
@router_modos_esquema.get("")
async def i_modos_esquema():
    return {"p":"psicologia_clin_modos_esquema","s":"ativo","t":datetime.utcnow().isoformat()}
@router_narcisista_terapia.get("")
async def i_narcisista_terapia():
    return {"p":"psicologia_clin_narcisista_terapia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_obsessivo_compulsivo.get("")
async def i_obsessivo_compulsivo():
    return {"p":"psicologia_clin_obsessivo_compulsivo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pai_punitivo.get("")
async def i_pai_punitivo():
    return {"p":"psicologia_clin_pai_punitivo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_paranoia_clinica.get("")
async def i_paranoia_clinica():
    return {"p":"psicologia_clin_paranoia_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_protetor_distante.get("")
async def i_protetor_distante():
    return {"p":"psicologia_clin_protetor_distante","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicopatia_avaliacao.get("")
async def i_psicopatia_avaliacao():
    return {"p":"psicologia_clin_psicopatia_avaliacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_recuperacao_narcisis.get("")
async def i_recuperacao_narcisis():
    return {"p":"psicologia_clin_recuperacao_narcisis","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reparo_apego.get("")
async def i_reparo_apego():
    return {"p":"psicologia_clin_reparo_apego","s":"ativo","t":datetime.utcnow().isoformat()}
@router_representacoes_menta.get("")
async def i_representacoes_menta():
    return {"p":"psicologia_clin_representacoes_menta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_schema_casais.get("")
async def i_schema_casais():
    return {"p":"psicologia_clin_schema_casais","s":"ativo","t":datetime.utcnow().isoformat()}
@router_schema_familia.get("")
async def i_schema_familia():
    return {"p":"psicologia_clin_schema_familia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_simbiose_psicologica.get("")
async def i_simbiose_psicologica():
    return {"p":"psicologia_clin_simbiose_psicologica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sociopatia_info.get("")
async def i_sociopatia_info():
    return {"p":"psicologia_clin_sociopatia_info","s":"ativo","t":datetime.utcnow().isoformat()}
@router_teoria_apego_adulto.get("")
async def i_teoria_apego_adulto():
    return {"p":"psicologia_clin_teoria_apego_adulto","s":"ativo","t":datetime.utcnow().isoformat()}
@router_terapia_baseada_apeg.get("")
async def i_terapia_baseada_apeg():
    return {"p":"psicologia_clin_terapia_baseada_apeg","s":"ativo","t":datetime.utcnow().isoformat()}
@router_terapia_schema_grupo.get("")
async def i_terapia_schema_grupo():
    return {"p":"psicologia_clin_terapia_schema_grupo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_transtorno_personali.get("")
async def i_transtorno_personali():
    return {"p":"psicologia_clin_transtorno_personali","s":"ativo","t":datetime.utcnow().isoformat()}
@router_transtorno_personali.get("")
async def i_transtorno_personali():
    return {"p":"psicologia_clin_transtorno_personali","s":"ativo","t":datetime.utcnow().isoformat()}
@router_transtorno_personali.get("")
async def i_transtorno_personali():
    return {"p":"psicologia_clin_transtorno_personali","s":"ativo","t":datetime.utcnow().isoformat()}
@router_trauma_apego.get("")
async def i_trauma_apego():
    return {"p":"psicologia_clin_trauma_apego","s":"ativo","t":datetime.utcnow().isoformat()}
@router_trauma_narcisista.get("")
async def i_trauma_narcisista():
    return {"p":"psicologia_clin_trauma_narcisista","s":"ativo","t":datetime.utcnow().isoformat()}
@router_trilogia_escura.get("")
async def i_trilogia_escura():
    return {"p":"psicologia_clin_trilogia_escura","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_psicologia_clinica(PluginBase):
    name = "consolidated_psicologia_clinica"
    def setup(self, app):
        app.include_router(router_abuso_narcisista)
        app.include_router(router_adulto_saudavel_sche)
        app.include_router(router_antisocial_terapia)
        app.include_router(router_apego_ansioso_adulto)
        app.include_router(router_apego_desorganizado_)
        app.include_router(router_apego_evitativo_adul)
        app.include_router(router_apego_fearful_avoida)
        app.include_router(router_apego_seguro_adulto)
        app.include_router(router_attachment_styles_qu)
        app.include_router(router_borderline_terapia)
        app.include_router(router_carta_schema)
        app.include_router(router_chair_work_schema)
        app.include_router(router_codependencia_clinic)
        app.include_router(router_coercao_controle)
        app.include_router(router_crianca_raivosa)
        app.include_router(router_crianca_vulneravel)
        app.include_router(router_dark_triad_clinico)
        app.include_router(router_dependente_clinico)
        app.include_router(router_diario_schema)
        app.include_router(router_eft_casal)
        app.include_router(router_enmeshment_clinico)
        app.include_router(router_esquemas_precoces)
        app.include_router(router_esquizoide_clinico)
        app.include_router(router_esquizotipal)
        app.include_router(router_evitativo_clinico)
        app.include_router(router_flash_card_schema)
        app.include_router(router_fusao_identidade)
        app.include_router(router_gaslighting_clinico)
        app.include_router(router_histrionico)
        app.include_router(router_imagery_rescripting)
        app.include_router(router_internal_working_mod)
        app.include_router(router_manipulacao_psico)
        app.include_router(router_mode_work)
        app.include_router(router_modelos_operantes_in)
        app.include_router(router_modos_esquema)
        app.include_router(router_narcisista_terapia)
        app.include_router(router_obsessivo_compulsivo)
        app.include_router(router_pai_punitivo)
        app.include_router(router_paranoia_clinica)
        app.include_router(router_protetor_distante)
        app.include_router(router_psicopatia_avaliacao)
        app.include_router(router_recuperacao_narcisis)
        app.include_router(router_reparo_apego)
        app.include_router(router_representacoes_menta)
        app.include_router(router_schema_casais)
        app.include_router(router_schema_familia)
        app.include_router(router_simbiose_psicologica)
        app.include_router(router_sociopatia_info)
        app.include_router(router_teoria_apego_adulto)
        app.include_router(router_terapia_baseada_apeg)
        app.include_router(router_terapia_schema_grupo)
        app.include_router(router_transtorno_personali)
        app.include_router(router_transtorno_personali)
        app.include_router(router_transtorno_personali)
        app.include_router(router_trauma_apego)
        app.include_router(router_trauma_narcisista)
        app.include_router(router_trilogia_escura)


plugin = Plugin_psicologia_clinica()
