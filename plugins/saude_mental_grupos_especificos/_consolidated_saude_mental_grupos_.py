from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_afrocentricidade = APIRouter(prefix="/api/v1/saude_mental/afrocentricidade", tags=["saude_mental_grupos_especificos"])
router_agnosticismo_psico = APIRouter(prefix="/api/v1/saude_mental/agnosticismo_psico", tags=["saude_mental_grupos_especificos"])
router_agricultores_mental = APIRouter(prefix="/api/v1/saude_mental/agricultores_mental", tags=["saude_mental_grupos_especificos"])
router_ateismo_psico = APIRouter(prefix="/api/v1/saude_mental/ateismo_psico", tags=["saude_mental_grupos_especificos"])
router_budismo_psico2 = APIRouter(prefix="/api/v1/saude_mental/budismo_psico2", tags=["saude_mental_grupos_especificos"])
router_caminhoneiros_mental = APIRouter(prefix="/api/v1/saude_mental/caminhoneiros_mental", tags=["saude_mental_grupos_especificos"])
router_candomble_psicologia = APIRouter(prefix="/api/v1/saude_mental/candomble_psicologia", tags=["saude_mental_grupos_especificos"])
router_catadores_mental = APIRouter(prefix="/api/v1/saude_mental/catadores_mental", tags=["saude_mental_grupos_especificos"])
router_catolicismo_psico = APIRouter(prefix="/api/v1/saude_mental/catolicismo_psico", tags=["saude_mental_grupos_especificos"])
router_construcao_civil_men = APIRouter(prefix="/api/v1/saude_mental/construcao_civil_mental", tags=["saude_mental_grupos_especificos"])
router_cosmologia_indigena = APIRouter(prefix="/api/v1/saude_mental/cosmologia_indigena", tags=["saude_mental_grupos_especificos"])
router_costureiras_mental = APIRouter(prefix="/api/v1/saude_mental/costureiras_mental", tags=["saude_mental_grupos_especificos"])
router_cozinheiros_mental = APIRouter(prefix="/api/v1/saude_mental/cozinheiros_mental", tags=["saude_mental_grupos_especificos"])
router_empreendedores_menta = APIRouter(prefix="/api/v1/saude_mental/empreendedores_mental", tags=["saude_mental_grupos_especificos"])
router_espiritismo_psicolog = APIRouter(prefix="/api/v1/saude_mental/espiritismo_psicologia", tags=["saude_mental_grupos_especificos"])
router_espiritualidade_br = APIRouter(prefix="/api/v1/saude_mental/espiritualidade_br", tags=["saude_mental_grupos_especificos"])
router_espiritualidade_secu = APIRouter(prefix="/api/v1/saude_mental/espiritualidade_secular", tags=["saude_mental_grupos_especificos"])
router_estresse_minorias2 = APIRouter(prefix="/api/v1/saude_mental/estresse_minorias2", tags=["saude_mental_grupos_especificos"])
router_evangelicalismo_psic = APIRouter(prefix="/api/v1/saude_mental/evangelicalismo_psico", tags=["saude_mental_grupos_especificos"])
router_freelancers_mental = APIRouter(prefix="/api/v1/saude_mental/freelancers_mental", tags=["saude_mental_grupos_especificos"])
router_garcons_mental = APIRouter(prefix="/api/v1/saude_mental/garcons_mental", tags=["saude_mental_grupos_especificos"])
router_garimpo_mental = APIRouter(prefix="/api/v1/saude_mental/garimpo_mental", tags=["saude_mental_grupos_especificos"])
router_gig_workers_mental = APIRouter(prefix="/api/v1/saude_mental/gig_workers_mental", tags=["saude_mental_grupos_especificos"])
router_guias_mental = APIRouter(prefix="/api/v1/saude_mental/guias_mental", tags=["saude_mental_grupos_especificos"])
router_hinduismo_psico = APIRouter(prefix="/api/v1/saude_mental/hinduismo_psico", tags=["saude_mental_grupos_especificos"])
router_hotelaria_mental = APIRouter(prefix="/api/v1/saude_mental/hotelaria_mental", tags=["saude_mental_grupos_especificos"])
router_humanismo_secular = APIRouter(prefix="/api/v1/saude_mental/humanismo_secular", tags=["saude_mental_grupos_especificos"])
router_identidade_racial = APIRouter(prefix="/api/v1/saude_mental/identidade_racial", tags=["saude_mental_grupos_especificos"])
router_islamismo_psico = APIRouter(prefix="/api/v1/saude_mental/islamismo_psico", tags=["saude_mental_grupos_especificos"])
router_judaismo_psico = APIRouter(prefix="/api/v1/saude_mental/judaismo_psico", tags=["saude_mental_grupos_especificos"])
router_limpeza_urbana_menta = APIRouter(prefix="/api/v1/saude_mental/limpeza_urbana_mental", tags=["saude_mental_grupos_especificos"])
router_marinheiros_mental = APIRouter(prefix="/api/v1/saude_mental/marinheiros_mental", tags=["saude_mental_grupos_especificos"])
router_metalurgicos_mental = APIRouter(prefix="/api/v1/saude_mental/metalurgicos_mental", tags=["saude_mental_grupos_especificos"])
router_microagressao_racial = APIRouter(prefix="/api/v1/saude_mental/microagressao_racial2", tags=["saude_mental_grupos_especificos"])
router_mineiros_mental = APIRouter(prefix="/api/v1/saude_mental/mineiros_mental", tags=["saude_mental_grupos_especificos"])
router_mineracao_mental = APIRouter(prefix="/api/v1/saude_mental/mineracao_mental", tags=["saude_mental_grupos_especificos"])
router_motoboys_mental = APIRouter(prefix="/api/v1/saude_mental/motoboys_mental", tags=["saude_mental_grupos_especificos"])
router_motoristas_mental = APIRouter(prefix="/api/v1/saude_mental/motoristas_mental", tags=["saude_mental_grupos_especificos"])
router_orgulho_racial = APIRouter(prefix="/api/v1/saude_mental/orgulho_racial", tags=["saude_mental_grupos_especificos"])
router_pajé_psicologia = APIRouter(prefix="/api/v1/saude_mental/pajé_psicologia", tags=["saude_mental_grupos_especificos"])
router_pescadores_alto_mar = APIRouter(prefix="/api/v1/saude_mental/pescadores_alto_mar", tags=["saude_mental_grupos_especificos"])
router_pescadores_mental = APIRouter(prefix="/api/v1/saude_mental/pescadores_mental", tags=["saude_mental_grupos_especificos"])
router_petróleo_mental = APIRouter(prefix="/api/v1/saude_mental/petróleo_mental", tags=["saude_mental_grupos_especificos"])
router_pilotos_mental = APIRouter(prefix="/api/v1/saude_mental/pilotos_mental", tags=["saude_mental_grupos_especificos"])
router_protestantismo_psico = APIRouter(prefix="/api/v1/saude_mental/protestantismo_psico", tags=["saude_mental_grupos_especificos"])
router_psicologia_africana = APIRouter(prefix="/api/v1/saude_mental/psicologia_africana", tags=["saude_mental_grupos_especificos"])
router_psicologia_indigena_ = APIRouter(prefix="/api/v1/saude_mental/psicologia_indigena_br", tags=["saude_mental_grupos_especificos"])
router_racismo_interiorizad = APIRouter(prefix="/api/v1/saude_mental/racismo_interiorizado", tags=["saude_mental_grupos_especificos"])
router_reciclagem_mental = APIRouter(prefix="/api/v1/saude_mental/reciclagem_mental", tags=["saude_mental_grupos_especificos"])
router_ritualidade = APIRouter(prefix="/api/v1/saude_mental/ritualidade", tags=["saude_mental_grupos_especificos"])
router_sankofa_psico = APIRouter(prefix="/api/v1/saude_mental/sankofa_psico", tags=["saude_mental_grupos_especificos"])
router_santo_daime_psico = APIRouter(prefix="/api/v1/saude_mental/santo_daime_psico", tags=["saude_mental_grupos_especificos"])
router_sapateiros_mental = APIRouter(prefix="/api/v1/saude_mental/sapateiros_mental", tags=["saude_mental_grupos_especificos"])
router_saude_mental_branco_ = APIRouter(prefix="/api/v1/saude_mental/saude_mental_branco_privi", tags=["saude_mental_grupos_especificos"])
router_saude_mental_negro = APIRouter(prefix="/api/v1/saude_mental/saude_mental_negro", tags=["saude_mental_grupos_especificos"])
router_saude_mental_trabalh = APIRouter(prefix="/api/v1/saude_mental/saude_mental_trabalhadore", tags=["saude_mental_grupos_especificos"])
router_servicos_gerais_ment = APIRouter(prefix="/api/v1/saude_mental/servicos_gerais_mental", tags=["saude_mental_grupos_especificos"])
router_taxistas_mental = APIRouter(prefix="/api/v1/saude_mental/taxistas_mental", tags=["saude_mental_grupos_especificos"])
router_turismo_mental = APIRouter(prefix="/api/v1/saude_mental/turismo_mental", tags=["saude_mental_grupos_especificos"])
router_ubuntu_psicologia = APIRouter(prefix="/api/v1/saude_mental/ubuntu_psicologia", tags=["saude_mental_grupos_especificos"])
router_umbanda_psicologia = APIRouter(prefix="/api/v1/saude_mental/umbanda_psicologia", tags=["saude_mental_grupos_especificos"])
router_vale_amanhecer = APIRouter(prefix="/api/v1/saude_mental/vale_amanhecer", tags=["saude_mental_grupos_especificos"])
router_xamanismo_psico = APIRouter(prefix="/api/v1/saude_mental/xamanismo_psico", tags=["saude_mental_grupos_especificos"])

@router_afrocentricidade.get("")
async def i_afrocentricidade():
    return {"p":"saude_mental_gr_afrocentricidade","s":"ativo","t":datetime.utcnow().isoformat()}
@router_agnosticismo_psico.get("")
async def i_agnosticismo_psico():
    return {"p":"saude_mental_gr_agnosticismo_psico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_agricultores_mental.get("")
async def i_agricultores_mental():
    return {"p":"saude_mental_gr_agricultores_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ateismo_psico.get("")
async def i_ateismo_psico():
    return {"p":"saude_mental_gr_ateismo_psico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_budismo_psico2.get("")
async def i_budismo_psico2():
    return {"p":"saude_mental_gr_budismo_psico2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_caminhoneiros_mental.get("")
async def i_caminhoneiros_mental():
    return {"p":"saude_mental_gr_caminhoneiros_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_candomble_psicologia.get("")
async def i_candomble_psicologia():
    return {"p":"saude_mental_gr_candomble_psicologia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_catadores_mental.get("")
async def i_catadores_mental():
    return {"p":"saude_mental_gr_catadores_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_catolicismo_psico.get("")
async def i_catolicismo_psico():
    return {"p":"saude_mental_gr_catolicismo_psico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_construcao_civil_men.get("")
async def i_construcao_civil_men():
    return {"p":"saude_mental_gr_construcao_civil_men","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cosmologia_indigena.get("")
async def i_cosmologia_indigena():
    return {"p":"saude_mental_gr_cosmologia_indigena","s":"ativo","t":datetime.utcnow().isoformat()}
@router_costureiras_mental.get("")
async def i_costureiras_mental():
    return {"p":"saude_mental_gr_costureiras_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cozinheiros_mental.get("")
async def i_cozinheiros_mental():
    return {"p":"saude_mental_gr_cozinheiros_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_empreendedores_menta.get("")
async def i_empreendedores_menta():
    return {"p":"saude_mental_gr_empreendedores_menta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_espiritismo_psicolog.get("")
async def i_espiritismo_psicolog():
    return {"p":"saude_mental_gr_espiritismo_psicolog","s":"ativo","t":datetime.utcnow().isoformat()}
@router_espiritualidade_br.get("")
async def i_espiritualidade_br():
    return {"p":"saude_mental_gr_espiritualidade_br","s":"ativo","t":datetime.utcnow().isoformat()}
@router_espiritualidade_secu.get("")
async def i_espiritualidade_secu():
    return {"p":"saude_mental_gr_espiritualidade_secu","s":"ativo","t":datetime.utcnow().isoformat()}
@router_estresse_minorias2.get("")
async def i_estresse_minorias2():
    return {"p":"saude_mental_gr_estresse_minorias2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_evangelicalismo_psic.get("")
async def i_evangelicalismo_psic():
    return {"p":"saude_mental_gr_evangelicalismo_psic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_freelancers_mental.get("")
async def i_freelancers_mental():
    return {"p":"saude_mental_gr_freelancers_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_garcons_mental.get("")
async def i_garcons_mental():
    return {"p":"saude_mental_gr_garcons_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_garimpo_mental.get("")
async def i_garimpo_mental():
    return {"p":"saude_mental_gr_garimpo_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gig_workers_mental.get("")
async def i_gig_workers_mental():
    return {"p":"saude_mental_gr_gig_workers_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_guias_mental.get("")
async def i_guias_mental():
    return {"p":"saude_mental_gr_guias_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hinduismo_psico.get("")
async def i_hinduismo_psico():
    return {"p":"saude_mental_gr_hinduismo_psico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hotelaria_mental.get("")
async def i_hotelaria_mental():
    return {"p":"saude_mental_gr_hotelaria_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_humanismo_secular.get("")
async def i_humanismo_secular():
    return {"p":"saude_mental_gr_humanismo_secular","s":"ativo","t":datetime.utcnow().isoformat()}
@router_identidade_racial.get("")
async def i_identidade_racial():
    return {"p":"saude_mental_gr_identidade_racial","s":"ativo","t":datetime.utcnow().isoformat()}
@router_islamismo_psico.get("")
async def i_islamismo_psico():
    return {"p":"saude_mental_gr_islamismo_psico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_judaismo_psico.get("")
async def i_judaismo_psico():
    return {"p":"saude_mental_gr_judaismo_psico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_limpeza_urbana_menta.get("")
async def i_limpeza_urbana_menta():
    return {"p":"saude_mental_gr_limpeza_urbana_menta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_marinheiros_mental.get("")
async def i_marinheiros_mental():
    return {"p":"saude_mental_gr_marinheiros_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_metalurgicos_mental.get("")
async def i_metalurgicos_mental():
    return {"p":"saude_mental_gr_metalurgicos_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_microagressao_racial.get("")
async def i_microagressao_racial():
    return {"p":"saude_mental_gr_microagressao_racial","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mineiros_mental.get("")
async def i_mineiros_mental():
    return {"p":"saude_mental_gr_mineiros_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mineracao_mental.get("")
async def i_mineracao_mental():
    return {"p":"saude_mental_gr_mineracao_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_motoboys_mental.get("")
async def i_motoboys_mental():
    return {"p":"saude_mental_gr_motoboys_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_motoristas_mental.get("")
async def i_motoristas_mental():
    return {"p":"saude_mental_gr_motoristas_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_orgulho_racial.get("")
async def i_orgulho_racial():
    return {"p":"saude_mental_gr_orgulho_racial","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pajé_psicologia.get("")
async def i_pajé_psicologia():
    return {"p":"saude_mental_gr_pajé_psicologia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pescadores_alto_mar.get("")
async def i_pescadores_alto_mar():
    return {"p":"saude_mental_gr_pescadores_alto_mar","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pescadores_mental.get("")
async def i_pescadores_mental():
    return {"p":"saude_mental_gr_pescadores_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_petróleo_mental.get("")
async def i_petróleo_mental():
    return {"p":"saude_mental_gr_petróleo_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pilotos_mental.get("")
async def i_pilotos_mental():
    return {"p":"saude_mental_gr_pilotos_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_protestantismo_psico.get("")
async def i_protestantismo_psico():
    return {"p":"saude_mental_gr_protestantismo_psico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicologia_africana.get("")
async def i_psicologia_africana():
    return {"p":"saude_mental_gr_psicologia_africana","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicologia_indigena_.get("")
async def i_psicologia_indigena_():
    return {"p":"saude_mental_gr_psicologia_indigena_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_racismo_interiorizad.get("")
async def i_racismo_interiorizad():
    return {"p":"saude_mental_gr_racismo_interiorizad","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reciclagem_mental.get("")
async def i_reciclagem_mental():
    return {"p":"saude_mental_gr_reciclagem_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ritualidade.get("")
async def i_ritualidade():
    return {"p":"saude_mental_gr_ritualidade","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sankofa_psico.get("")
async def i_sankofa_psico():
    return {"p":"saude_mental_gr_sankofa_psico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_santo_daime_psico.get("")
async def i_santo_daime_psico():
    return {"p":"saude_mental_gr_santo_daime_psico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sapateiros_mental.get("")
async def i_sapateiros_mental():
    return {"p":"saude_mental_gr_sapateiros_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_branco_.get("")
async def i_saude_mental_branco_():
    return {"p":"saude_mental_gr_saude_mental_branco_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_negro.get("")
async def i_saude_mental_negro():
    return {"p":"saude_mental_gr_saude_mental_negro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_trabalh.get("")
async def i_saude_mental_trabalh():
    return {"p":"saude_mental_gr_saude_mental_trabalh","s":"ativo","t":datetime.utcnow().isoformat()}
@router_servicos_gerais_ment.get("")
async def i_servicos_gerais_ment():
    return {"p":"saude_mental_gr_servicos_gerais_ment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_taxistas_mental.get("")
async def i_taxistas_mental():
    return {"p":"saude_mental_gr_taxistas_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_turismo_mental.get("")
async def i_turismo_mental():
    return {"p":"saude_mental_gr_turismo_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ubuntu_psicologia.get("")
async def i_ubuntu_psicologia():
    return {"p":"saude_mental_gr_ubuntu_psicologia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_umbanda_psicologia.get("")
async def i_umbanda_psicologia():
    return {"p":"saude_mental_gr_umbanda_psicologia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_vale_amanhecer.get("")
async def i_vale_amanhecer():
    return {"p":"saude_mental_gr_vale_amanhecer","s":"ativo","t":datetime.utcnow().isoformat()}
@router_xamanismo_psico.get("")
async def i_xamanismo_psico():
    return {"p":"saude_mental_gr_xamanismo_psico","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_saude_mental_grupos_(PluginBase):
    name = "consolidated_saude_mental_grupos_especifico"
    def setup(self, app):
        app.include_router(router_afrocentricidade)
        app.include_router(router_agnosticismo_psico)
        app.include_router(router_agricultores_mental)
        app.include_router(router_ateismo_psico)
        app.include_router(router_budismo_psico2)
        app.include_router(router_caminhoneiros_mental)
        app.include_router(router_candomble_psicologia)
        app.include_router(router_catadores_mental)
        app.include_router(router_catolicismo_psico)
        app.include_router(router_construcao_civil_men)
        app.include_router(router_cosmologia_indigena)
        app.include_router(router_costureiras_mental)
        app.include_router(router_cozinheiros_mental)
        app.include_router(router_empreendedores_menta)
        app.include_router(router_espiritismo_psicolog)
        app.include_router(router_espiritualidade_br)
        app.include_router(router_espiritualidade_secu)
        app.include_router(router_estresse_minorias2)
        app.include_router(router_evangelicalismo_psic)
        app.include_router(router_freelancers_mental)
        app.include_router(router_garcons_mental)
        app.include_router(router_garimpo_mental)
        app.include_router(router_gig_workers_mental)
        app.include_router(router_guias_mental)
        app.include_router(router_hinduismo_psico)
        app.include_router(router_hotelaria_mental)
        app.include_router(router_humanismo_secular)
        app.include_router(router_identidade_racial)
        app.include_router(router_islamismo_psico)
        app.include_router(router_judaismo_psico)
        app.include_router(router_limpeza_urbana_menta)
        app.include_router(router_marinheiros_mental)
        app.include_router(router_metalurgicos_mental)
        app.include_router(router_microagressao_racial)
        app.include_router(router_mineiros_mental)
        app.include_router(router_mineracao_mental)
        app.include_router(router_motoboys_mental)
        app.include_router(router_motoristas_mental)
        app.include_router(router_orgulho_racial)
        app.include_router(router_pajé_psicologia)
        app.include_router(router_pescadores_alto_mar)
        app.include_router(router_pescadores_mental)
        app.include_router(router_petróleo_mental)
        app.include_router(router_pilotos_mental)
        app.include_router(router_protestantismo_psico)
        app.include_router(router_psicologia_africana)
        app.include_router(router_psicologia_indigena_)
        app.include_router(router_racismo_interiorizad)
        app.include_router(router_reciclagem_mental)
        app.include_router(router_ritualidade)
        app.include_router(router_sankofa_psico)
        app.include_router(router_santo_daime_psico)
        app.include_router(router_sapateiros_mental)
        app.include_router(router_saude_mental_branco_)
        app.include_router(router_saude_mental_negro)
        app.include_router(router_saude_mental_trabalh)
        app.include_router(router_servicos_gerais_ment)
        app.include_router(router_taxistas_mental)
        app.include_router(router_turismo_mental)
        app.include_router(router_ubuntu_psicologia)
        app.include_router(router_umbanda_psicologia)
        app.include_router(router_vale_amanhecer)
        app.include_router(router_xamanismo_psico)


plugin = Plugin_saude_mental_grupos_()
