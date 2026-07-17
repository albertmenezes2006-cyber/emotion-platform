from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_saude_mental_africa_ = APIRouter(prefix="/api/v1/saude_mental/saude_mental_africa_sul", tags=["saude_mental_internacional"])
router_saude_mental_alemanh = APIRouter(prefix="/api/v1/saude_mental/saude_mental_alemanha", tags=["saude_mental_internacional"])
router_saude_mental_arabia_ = APIRouter(prefix="/api/v1/saude_mental/saude_mental_arabia_saudi", tags=["saude_mental_internacional"])
router_saude_mental_argenti = APIRouter(prefix="/api/v1/saude_mental/saude_mental_argentina", tags=["saude_mental_internacional"])
router_saude_mental_austral = APIRouter(prefix="/api/v1/saude_mental/saude_mental_australia", tags=["saude_mental_internacional"])
router_saude_mental_austria = APIRouter(prefix="/api/v1/saude_mental/saude_mental_austria", tags=["saude_mental_internacional"])
router_saude_mental_banglad = APIRouter(prefix="/api/v1/saude_mental/saude_mental_bangladesh", tags=["saude_mental_internacional"])
router_saude_mental_belgica = APIRouter(prefix="/api/v1/saude_mental/saude_mental_belgica", tags=["saude_mental_internacional"])
router_saude_mental_bolivia = APIRouter(prefix="/api/v1/saude_mental/saude_mental_bolivia", tags=["saude_mental_internacional"])
router_saude_mental_canada = APIRouter(prefix="/api/v1/saude_mental/saude_mental_canada", tags=["saude_mental_internacional"])
router_saude_mental_chile = APIRouter(prefix="/api/v1/saude_mental/saude_mental_chile", tags=["saude_mental_internacional"])
router_saude_mental_china = APIRouter(prefix="/api/v1/saude_mental/saude_mental_china", tags=["saude_mental_internacional"])
router_saude_mental_colombi = APIRouter(prefix="/api/v1/saude_mental/saude_mental_colombia", tags=["saude_mental_internacional"])
router_saude_mental_coreia = APIRouter(prefix="/api/v1/saude_mental/saude_mental_coreia", tags=["saude_mental_internacional"])
router_saude_mental_cuba = APIRouter(prefix="/api/v1/saude_mental/saude_mental_cuba", tags=["saude_mental_internacional"])
router_saude_mental_dinamar = APIRouter(prefix="/api/v1/saude_mental/saude_mental_dinamarca", tags=["saude_mental_internacional"])
router_saude_mental_ecuador = APIRouter(prefix="/api/v1/saude_mental/saude_mental_ecuador", tags=["saude_mental_internacional"])
router_saude_mental_egipto = APIRouter(prefix="/api/v1/saude_mental/saude_mental_egipto", tags=["saude_mental_internacional"])
router_saude_mental_emirado = APIRouter(prefix="/api/v1/saude_mental/saude_mental_emirados", tags=["saude_mental_internacional"])
router_saude_mental_espanha = APIRouter(prefix="/api/v1/saude_mental/saude_mental_espanha", tags=["saude_mental_internacional"])
router_saude_mental_etiopia = APIRouter(prefix="/api/v1/saude_mental/saude_mental_etiopia", tags=["saude_mental_internacional"])
router_saude_mental_eua = APIRouter(prefix="/api/v1/saude_mental/saude_mental_eua", tags=["saude_mental_internacional"])
router_saude_mental_filipin = APIRouter(prefix="/api/v1/saude_mental/saude_mental_filipinas", tags=["saude_mental_internacional"])
router_saude_mental_finland = APIRouter(prefix="/api/v1/saude_mental/saude_mental_finlandia", tags=["saude_mental_internacional"])
router_saude_mental_franca = APIRouter(prefix="/api/v1/saude_mental/saude_mental_franca", tags=["saude_mental_internacional"])
router_saude_mental_ghana = APIRouter(prefix="/api/v1/saude_mental/saude_mental_ghana", tags=["saude_mental_internacional"])
router_saude_mental_haiti = APIRouter(prefix="/api/v1/saude_mental/saude_mental_haiti", tags=["saude_mental_internacional"])
router_saude_mental_holanda = APIRouter(prefix="/api/v1/saude_mental/saude_mental_holanda", tags=["saude_mental_internacional"])
router_saude_mental_india = APIRouter(prefix="/api/v1/saude_mental/saude_mental_india", tags=["saude_mental_internacional"])
router_saude_mental_indones = APIRouter(prefix="/api/v1/saude_mental/saude_mental_indonesia", tags=["saude_mental_internacional"])
router_saude_mental_iran = APIRouter(prefix="/api/v1/saude_mental/saude_mental_iran", tags=["saude_mental_internacional"])
router_saude_mental_irlanda = APIRouter(prefix="/api/v1/saude_mental/saude_mental_irlanda", tags=["saude_mental_internacional"])
router_saude_mental_israel = APIRouter(prefix="/api/v1/saude_mental/saude_mental_israel", tags=["saude_mental_internacional"])
router_saude_mental_italia = APIRouter(prefix="/api/v1/saude_mental/saude_mental_italia", tags=["saude_mental_internacional"])
router_saude_mental_japao = APIRouter(prefix="/api/v1/saude_mental/saude_mental_japao", tags=["saude_mental_internacional"])
router_saude_mental_kenya = APIRouter(prefix="/api/v1/saude_mental/saude_mental_kenya", tags=["saude_mental_internacional"])
router_saude_mental_malaysi = APIRouter(prefix="/api/v1/saude_mental/saude_mental_malaysia", tags=["saude_mental_internacional"])
router_saude_mental_marroco = APIRouter(prefix="/api/v1/saude_mental/saude_mental_marrocos", tags=["saude_mental_internacional"])
router_saude_mental_mexico = APIRouter(prefix="/api/v1/saude_mental/saude_mental_mexico", tags=["saude_mental_internacional"])
router_saude_mental_nigeria = APIRouter(prefix="/api/v1/saude_mental/saude_mental_nigeria", tags=["saude_mental_internacional"])
router_saude_mental_noruega = APIRouter(prefix="/api/v1/saude_mental/saude_mental_noruega", tags=["saude_mental_internacional"])
router_saude_mental_nova_ze = APIRouter(prefix="/api/v1/saude_mental/saude_mental_nova_zelandi", tags=["saude_mental_internacional"])
router_saude_mental_paquist = APIRouter(prefix="/api/v1/saude_mental/saude_mental_paquistao", tags=["saude_mental_internacional"])
router_saude_mental_paragua = APIRouter(prefix="/api/v1/saude_mental/saude_mental_paraguai", tags=["saude_mental_internacional"])
router_saude_mental_peru = APIRouter(prefix="/api/v1/saude_mental/saude_mental_peru", tags=["saude_mental_internacional"])
router_saude_mental_polônia = APIRouter(prefix="/api/v1/saude_mental/saude_mental_polônia", tags=["saude_mental_internacional"])
router_saude_mental_portuga = APIRouter(prefix="/api/v1/saude_mental/saude_mental_portugal", tags=["saude_mental_internacional"])
router_saude_mental_qatar = APIRouter(prefix="/api/v1/saude_mental/saude_mental_qatar", tags=["saude_mental_internacional"])
router_saude_mental_russia = APIRouter(prefix="/api/v1/saude_mental/saude_mental_russia", tags=["saude_mental_internacional"])
router_saude_mental_singapu = APIRouter(prefix="/api/v1/saude_mental/saude_mental_singapura", tags=["saude_mental_internacional"])
router_saude_mental_suecia = APIRouter(prefix="/api/v1/saude_mental/saude_mental_suecia", tags=["saude_mental_internacional"])
router_saude_mental_suica = APIRouter(prefix="/api/v1/saude_mental/saude_mental_suica", tags=["saude_mental_internacional"])
router_saude_mental_tailand = APIRouter(prefix="/api/v1/saude_mental/saude_mental_tailandia", tags=["saude_mental_internacional"])
router_saude_mental_tanzani = APIRouter(prefix="/api/v1/saude_mental/saude_mental_tanzania", tags=["saude_mental_internacional"])
router_saude_mental_tunisia = APIRouter(prefix="/api/v1/saude_mental/saude_mental_tunisia", tags=["saude_mental_internacional"])
router_saude_mental_turquia = APIRouter(prefix="/api/v1/saude_mental/saude_mental_turquia", tags=["saude_mental_internacional"])
router_saude_mental_uganda = APIRouter(prefix="/api/v1/saude_mental/saude_mental_uganda", tags=["saude_mental_internacional"])
router_saude_mental_uk = APIRouter(prefix="/api/v1/saude_mental/saude_mental_uk", tags=["saude_mental_internacional"])
router_saude_mental_uruguai = APIRouter(prefix="/api/v1/saude_mental/saude_mental_uruguai", tags=["saude_mental_internacional"])
router_saude_mental_venezue = APIRouter(prefix="/api/v1/saude_mental/saude_mental_venezuela", tags=["saude_mental_internacional"])
router_saude_mental_vietnam = APIRouter(prefix="/api/v1/saude_mental/saude_mental_vietnam", tags=["saude_mental_internacional"])
router_saude_mental_zambia = APIRouter(prefix="/api/v1/saude_mental/saude_mental_zambia", tags=["saude_mental_internacional"])
router_saude_mental_zimbabw = APIRouter(prefix="/api/v1/saude_mental/saude_mental_zimbabwe", tags=["saude_mental_internacional"])

@router_saude_mental_africa_.get("")
async def i_saude_mental_africa_():
    return {"p":"saude_mental_in_saude_mental_africa_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_alemanh.get("")
async def i_saude_mental_alemanh():
    return {"p":"saude_mental_in_saude_mental_alemanh","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_arabia_.get("")
async def i_saude_mental_arabia_():
    return {"p":"saude_mental_in_saude_mental_arabia_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_argenti.get("")
async def i_saude_mental_argenti():
    return {"p":"saude_mental_in_saude_mental_argenti","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_austral.get("")
async def i_saude_mental_austral():
    return {"p":"saude_mental_in_saude_mental_austral","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_austria.get("")
async def i_saude_mental_austria():
    return {"p":"saude_mental_in_saude_mental_austria","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_banglad.get("")
async def i_saude_mental_banglad():
    return {"p":"saude_mental_in_saude_mental_banglad","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_belgica.get("")
async def i_saude_mental_belgica():
    return {"p":"saude_mental_in_saude_mental_belgica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_bolivia.get("")
async def i_saude_mental_bolivia():
    return {"p":"saude_mental_in_saude_mental_bolivia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_canada.get("")
async def i_saude_mental_canada():
    return {"p":"saude_mental_in_saude_mental_canada","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_chile.get("")
async def i_saude_mental_chile():
    return {"p":"saude_mental_in_saude_mental_chile","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_china.get("")
async def i_saude_mental_china():
    return {"p":"saude_mental_in_saude_mental_china","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_colombi.get("")
async def i_saude_mental_colombi():
    return {"p":"saude_mental_in_saude_mental_colombi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_coreia.get("")
async def i_saude_mental_coreia():
    return {"p":"saude_mental_in_saude_mental_coreia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_cuba.get("")
async def i_saude_mental_cuba():
    return {"p":"saude_mental_in_saude_mental_cuba","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_dinamar.get("")
async def i_saude_mental_dinamar():
    return {"p":"saude_mental_in_saude_mental_dinamar","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_ecuador.get("")
async def i_saude_mental_ecuador():
    return {"p":"saude_mental_in_saude_mental_ecuador","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_egipto.get("")
async def i_saude_mental_egipto():
    return {"p":"saude_mental_in_saude_mental_egipto","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_emirado.get("")
async def i_saude_mental_emirado():
    return {"p":"saude_mental_in_saude_mental_emirado","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_espanha.get("")
async def i_saude_mental_espanha():
    return {"p":"saude_mental_in_saude_mental_espanha","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_etiopia.get("")
async def i_saude_mental_etiopia():
    return {"p":"saude_mental_in_saude_mental_etiopia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_eua.get("")
async def i_saude_mental_eua():
    return {"p":"saude_mental_in_saude_mental_eua","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_filipin.get("")
async def i_saude_mental_filipin():
    return {"p":"saude_mental_in_saude_mental_filipin","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_finland.get("")
async def i_saude_mental_finland():
    return {"p":"saude_mental_in_saude_mental_finland","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_franca.get("")
async def i_saude_mental_franca():
    return {"p":"saude_mental_in_saude_mental_franca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_ghana.get("")
async def i_saude_mental_ghana():
    return {"p":"saude_mental_in_saude_mental_ghana","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_haiti.get("")
async def i_saude_mental_haiti():
    return {"p":"saude_mental_in_saude_mental_haiti","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_holanda.get("")
async def i_saude_mental_holanda():
    return {"p":"saude_mental_in_saude_mental_holanda","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_india.get("")
async def i_saude_mental_india():
    return {"p":"saude_mental_in_saude_mental_india","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_indones.get("")
async def i_saude_mental_indones():
    return {"p":"saude_mental_in_saude_mental_indones","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_iran.get("")
async def i_saude_mental_iran():
    return {"p":"saude_mental_in_saude_mental_iran","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_irlanda.get("")
async def i_saude_mental_irlanda():
    return {"p":"saude_mental_in_saude_mental_irlanda","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_israel.get("")
async def i_saude_mental_israel():
    return {"p":"saude_mental_in_saude_mental_israel","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_italia.get("")
async def i_saude_mental_italia():
    return {"p":"saude_mental_in_saude_mental_italia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_japao.get("")
async def i_saude_mental_japao():
    return {"p":"saude_mental_in_saude_mental_japao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_kenya.get("")
async def i_saude_mental_kenya():
    return {"p":"saude_mental_in_saude_mental_kenya","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_malaysi.get("")
async def i_saude_mental_malaysi():
    return {"p":"saude_mental_in_saude_mental_malaysi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_marroco.get("")
async def i_saude_mental_marroco():
    return {"p":"saude_mental_in_saude_mental_marroco","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_mexico.get("")
async def i_saude_mental_mexico():
    return {"p":"saude_mental_in_saude_mental_mexico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_nigeria.get("")
async def i_saude_mental_nigeria():
    return {"p":"saude_mental_in_saude_mental_nigeria","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_noruega.get("")
async def i_saude_mental_noruega():
    return {"p":"saude_mental_in_saude_mental_noruega","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_nova_ze.get("")
async def i_saude_mental_nova_ze():
    return {"p":"saude_mental_in_saude_mental_nova_ze","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_paquist.get("")
async def i_saude_mental_paquist():
    return {"p":"saude_mental_in_saude_mental_paquist","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_paragua.get("")
async def i_saude_mental_paragua():
    return {"p":"saude_mental_in_saude_mental_paragua","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_peru.get("")
async def i_saude_mental_peru():
    return {"p":"saude_mental_in_saude_mental_peru","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_polônia.get("")
async def i_saude_mental_polônia():
    return {"p":"saude_mental_in_saude_mental_polônia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_portuga.get("")
async def i_saude_mental_portuga():
    return {"p":"saude_mental_in_saude_mental_portuga","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_qatar.get("")
async def i_saude_mental_qatar():
    return {"p":"saude_mental_in_saude_mental_qatar","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_russia.get("")
async def i_saude_mental_russia():
    return {"p":"saude_mental_in_saude_mental_russia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_singapu.get("")
async def i_saude_mental_singapu():
    return {"p":"saude_mental_in_saude_mental_singapu","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_suecia.get("")
async def i_saude_mental_suecia():
    return {"p":"saude_mental_in_saude_mental_suecia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_suica.get("")
async def i_saude_mental_suica():
    return {"p":"saude_mental_in_saude_mental_suica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_tailand.get("")
async def i_saude_mental_tailand():
    return {"p":"saude_mental_in_saude_mental_tailand","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_tanzani.get("")
async def i_saude_mental_tanzani():
    return {"p":"saude_mental_in_saude_mental_tanzani","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_tunisia.get("")
async def i_saude_mental_tunisia():
    return {"p":"saude_mental_in_saude_mental_tunisia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_turquia.get("")
async def i_saude_mental_turquia():
    return {"p":"saude_mental_in_saude_mental_turquia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_uganda.get("")
async def i_saude_mental_uganda():
    return {"p":"saude_mental_in_saude_mental_uganda","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_uk.get("")
async def i_saude_mental_uk():
    return {"p":"saude_mental_in_saude_mental_uk","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_uruguai.get("")
async def i_saude_mental_uruguai():
    return {"p":"saude_mental_in_saude_mental_uruguai","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_venezue.get("")
async def i_saude_mental_venezue():
    return {"p":"saude_mental_in_saude_mental_venezue","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_vietnam.get("")
async def i_saude_mental_vietnam():
    return {"p":"saude_mental_in_saude_mental_vietnam","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_zambia.get("")
async def i_saude_mental_zambia():
    return {"p":"saude_mental_in_saude_mental_zambia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_zimbabw.get("")
async def i_saude_mental_zimbabw():
    return {"p":"saude_mental_in_saude_mental_zimbabw","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_saude_mental_interna(PluginBase):
    name = "consolidated_saude_mental_internacional"
    def setup(self, app):
        app.include_router(router_saude_mental_africa_)
        app.include_router(router_saude_mental_alemanh)
        app.include_router(router_saude_mental_arabia_)
        app.include_router(router_saude_mental_argenti)
        app.include_router(router_saude_mental_austral)
        app.include_router(router_saude_mental_austria)
        app.include_router(router_saude_mental_banglad)
        app.include_router(router_saude_mental_belgica)
        app.include_router(router_saude_mental_bolivia)
        app.include_router(router_saude_mental_canada)
        app.include_router(router_saude_mental_chile)
        app.include_router(router_saude_mental_china)
        app.include_router(router_saude_mental_colombi)
        app.include_router(router_saude_mental_coreia)
        app.include_router(router_saude_mental_cuba)
        app.include_router(router_saude_mental_dinamar)
        app.include_router(router_saude_mental_ecuador)
        app.include_router(router_saude_mental_egipto)
        app.include_router(router_saude_mental_emirado)
        app.include_router(router_saude_mental_espanha)
        app.include_router(router_saude_mental_etiopia)
        app.include_router(router_saude_mental_eua)
        app.include_router(router_saude_mental_filipin)
        app.include_router(router_saude_mental_finland)
        app.include_router(router_saude_mental_franca)
        app.include_router(router_saude_mental_ghana)
        app.include_router(router_saude_mental_haiti)
        app.include_router(router_saude_mental_holanda)
        app.include_router(router_saude_mental_india)
        app.include_router(router_saude_mental_indones)
        app.include_router(router_saude_mental_iran)
        app.include_router(router_saude_mental_irlanda)
        app.include_router(router_saude_mental_israel)
        app.include_router(router_saude_mental_italia)
        app.include_router(router_saude_mental_japao)
        app.include_router(router_saude_mental_kenya)
        app.include_router(router_saude_mental_malaysi)
        app.include_router(router_saude_mental_marroco)
        app.include_router(router_saude_mental_mexico)
        app.include_router(router_saude_mental_nigeria)
        app.include_router(router_saude_mental_noruega)
        app.include_router(router_saude_mental_nova_ze)
        app.include_router(router_saude_mental_paquist)
        app.include_router(router_saude_mental_paragua)
        app.include_router(router_saude_mental_peru)
        app.include_router(router_saude_mental_polônia)
        app.include_router(router_saude_mental_portuga)
        app.include_router(router_saude_mental_qatar)
        app.include_router(router_saude_mental_russia)
        app.include_router(router_saude_mental_singapu)
        app.include_router(router_saude_mental_suecia)
        app.include_router(router_saude_mental_suica)
        app.include_router(router_saude_mental_tailand)
        app.include_router(router_saude_mental_tanzani)
        app.include_router(router_saude_mental_tunisia)
        app.include_router(router_saude_mental_turquia)
        app.include_router(router_saude_mental_uganda)
        app.include_router(router_saude_mental_uk)
        app.include_router(router_saude_mental_uruguai)
        app.include_router(router_saude_mental_venezue)
        app.include_router(router_saude_mental_vietnam)
        app.include_router(router_saude_mental_zambia)
        app.include_router(router_saude_mental_zimbabw)


plugin = Plugin_saude_mental_interna()
