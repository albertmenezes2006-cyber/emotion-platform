from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_saude_mental_acampam = APIRouter(prefix="/api/v1/saude_mental/saude_mental_acampamento", tags=["saude_mental_contextos"])
router_saude_mental_aldeia = APIRouter(prefix="/api/v1/saude_mental/saude_mental_aldeia", tags=["saude_mental_contextos"])
router_saude_mental_ambulat = APIRouter(prefix="/api/v1/saude_mental/saude_mental_ambulatorio", tags=["saude_mental_contextos"])
router_saude_mental_assenta = APIRouter(prefix="/api/v1/saude_mental/saude_mental_assentamento", tags=["saude_mental_contextos"])
router_saude_mental_berçari = APIRouter(prefix="/api/v1/saude_mental/saude_mental_berçario", tags=["saude_mental_contextos"])
router_saude_mental_cardiol = APIRouter(prefix="/api/v1/saude_mental/saude_mental_cardiologia2", tags=["saude_mental_contextos"])
router_saude_mental_cirurgi = APIRouter(prefix="/api/v1/saude_mental/saude_mental_cirurgia2", tags=["saude_mental_contextos"])
router_saude_mental_comerci = APIRouter(prefix="/api/v1/saude_mental/saude_mental_comercial", tags=["saude_mental_contextos"])
router_saude_mental_comunid = APIRouter(prefix="/api/v1/saude_mental/saude_mental_comunidade", tags=["saude_mental_contextos"])
router_saude_mental_concurs = APIRouter(prefix="/api/v1/saude_mental/saude_mental_concursos", tags=["saude_mental_contextos"])
router_saude_mental_coorden = APIRouter(prefix="/api/v1/saude_mental/saude_mental_coordenadore", tags=["saude_mental_contextos"])
router_saude_mental_creche = APIRouter(prefix="/api/v1/saude_mental/saude_mental_creche", tags=["saude_mental_contextos"])
router_saude_mental_diretor = APIRouter(prefix="/api/v1/saude_mental/saude_mental_diretores", tags=["saude_mental_contextos"])
router_saude_mental_enferma = APIRouter(prefix="/api/v1/saude_mental/saude_mental_enfermagem", tags=["saude_mental_contextos"])
router_saude_mental_enferma = APIRouter(prefix="/api/v1/saude_mental/saude_mental_enfermaria", tags=["saude_mental_contextos"])
router_saude_mental_farmaci = APIRouter(prefix="/api/v1/saude_mental/saude_mental_farmacia", tags=["saude_mental_contextos"])
router_saude_mental_favela = APIRouter(prefix="/api/v1/saude_mental/saude_mental_favela", tags=["saude_mental_contextos"])
router_saude_mental_fisiote = APIRouter(prefix="/api/v1/saude_mental/saude_mental_fisioterapia", tags=["saude_mental_contextos"])
router_saude_mental_fonoaud = APIRouter(prefix="/api/v1/saude_mental/saude_mental_fonoaudiolog", tags=["saude_mental_contextos"])
router_saude_mental_fundame = APIRouter(prefix="/api/v1/saude_mental/saude_mental_fundamental", tags=["saude_mental_contextos"])
router_saude_mental_geriatr = APIRouter(prefix="/api/v1/saude_mental/saude_mental_geriatria2", tags=["saude_mental_contextos"])
router_saude_mental_industr = APIRouter(prefix="/api/v1/saude_mental/saude_mental_industrial", tags=["saude_mental_contextos"])
router_saude_mental_infanti = APIRouter(prefix="/api/v1/saude_mental/saude_mental_infantil_esc", tags=["saude_mental_contextos"])
router_saude_mental_interna = APIRouter(prefix="/api/v1/saude_mental/saude_mental_internacao", tags=["saude_mental_contextos"])
router_saude_mental_interna = APIRouter(prefix="/api/v1/saude_mental/saude_mental_internato", tags=["saude_mental_contextos"])
router_saude_mental_materni = APIRouter(prefix="/api/v1/saude_mental/saude_mental_maternidade", tags=["saude_mental_contextos"])
router_saude_mental_medicin = APIRouter(prefix="/api/v1/saude_mental/saude_mental_medicina", tags=["saude_mental_contextos"])
router_saude_mental_neurolo = APIRouter(prefix="/api/v1/saude_mental/saude_mental_neurologia2", tags=["saude_mental_contextos"])
router_saude_mental_nutrica = APIRouter(prefix="/api/v1/saude_mental/saude_mental_nutricao", tags=["saude_mental_contextos"])
router_saude_mental_odontol = APIRouter(prefix="/api/v1/saude_mental/saude_mental_odontologia", tags=["saude_mental_contextos"])
router_saude_mental_oncolog = APIRouter(prefix="/api/v1/saude_mental/saude_mental_oncologia2", tags=["saude_mental_contextos"])
router_saude_mental_ortoped = APIRouter(prefix="/api/v1/saude_mental/saude_mental_ortopedia", tags=["saude_mental_contextos"])
router_saude_mental_pediatr = APIRouter(prefix="/api/v1/saude_mental/saude_mental_pediatria2", tags=["saude_mental_contextos"])
router_saude_mental_perifer = APIRouter(prefix="/api/v1/saude_mental/saude_mental_periferia", tags=["saude_mental_contextos"])
router_saude_mental_pesquis = APIRouter(prefix="/api/v1/saude_mental/saude_mental_pesquisadore", tags=["saude_mental_contextos"])
router_saude_mental_pos_gra = APIRouter(prefix="/api/v1/saude_mental/saude_mental_pos_graduaca", tags=["saude_mental_contextos"])
router_saude_mental_profess = APIRouter(prefix="/api/v1/saude_mental/saude_mental_professores2", tags=["saude_mental_contextos"])
router_saude_mental_pronto_ = APIRouter(prefix="/api/v1/saude_mental/saude_mental_pronto_socor", tags=["saude_mental_contextos"])
router_saude_mental_quilomb = APIRouter(prefix="/api/v1/saude_mental/saude_mental_quilombo", tags=["saude_mental_contextos"])
router_saude_mental_reabili = APIRouter(prefix="/api/v1/saude_mental/saude_mental_reabilitacao", tags=["saude_mental_contextos"])
router_saude_mental_reitore = APIRouter(prefix="/api/v1/saude_mental/saude_mental_reitores", tags=["saude_mental_contextos"])
router_saude_mental_residen = APIRouter(prefix="/api/v1/saude_mental/saude_mental_residencia_m", tags=["saude_mental_contextos"])
router_saude_mental_rural2 = APIRouter(prefix="/api/v1/saude_mental/saude_mental_rural2", tags=["saude_mental_contextos"])
router_saude_mental_tecnico = APIRouter(prefix="/api/v1/saude_mental/saude_mental_tecnico", tags=["saude_mental_contextos"])
router_saude_mental_terapia = APIRouter(prefix="/api/v1/saude_mental/saude_mental_terapia_ocup", tags=["saude_mental_contextos"])
router_saude_mental_univers = APIRouter(prefix="/api/v1/saude_mental/saude_mental_universitari", tags=["saude_mental_contextos"])
router_saude_mental_urbano = APIRouter(prefix="/api/v1/saude_mental/saude_mental_urbano", tags=["saude_mental_contextos"])
router_saude_mental_uti2 = APIRouter(prefix="/api/v1/saude_mental/saude_mental_uti2", tags=["saude_mental_contextos"])
router_saude_mental_vestibu = APIRouter(prefix="/api/v1/saude_mental/saude_mental_vestibular", tags=["saude_mental_contextos"])
router_saude_mental_zona_po = APIRouter(prefix="/api/v1/saude_mental/saude_mental_zona_portuar", tags=["saude_mental_contextos"])

@router_saude_mental_acampam.get("")
async def i_saude_mental_acampam():
    return {"p":"saude_mental_co_saude_mental_acampam","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_aldeia.get("")
async def i_saude_mental_aldeia():
    return {"p":"saude_mental_co_saude_mental_aldeia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_ambulat.get("")
async def i_saude_mental_ambulat():
    return {"p":"saude_mental_co_saude_mental_ambulat","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_assenta.get("")
async def i_saude_mental_assenta():
    return {"p":"saude_mental_co_saude_mental_assenta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_berçari.get("")
async def i_saude_mental_berçari():
    return {"p":"saude_mental_co_saude_mental_berçari","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_cardiol.get("")
async def i_saude_mental_cardiol():
    return {"p":"saude_mental_co_saude_mental_cardiol","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_cirurgi.get("")
async def i_saude_mental_cirurgi():
    return {"p":"saude_mental_co_saude_mental_cirurgi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_comerci.get("")
async def i_saude_mental_comerci():
    return {"p":"saude_mental_co_saude_mental_comerci","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_comunid.get("")
async def i_saude_mental_comunid():
    return {"p":"saude_mental_co_saude_mental_comunid","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_concurs.get("")
async def i_saude_mental_concurs():
    return {"p":"saude_mental_co_saude_mental_concurs","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_coorden.get("")
async def i_saude_mental_coorden():
    return {"p":"saude_mental_co_saude_mental_coorden","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_creche.get("")
async def i_saude_mental_creche():
    return {"p":"saude_mental_co_saude_mental_creche","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_diretor.get("")
async def i_saude_mental_diretor():
    return {"p":"saude_mental_co_saude_mental_diretor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_enferma.get("")
async def i_saude_mental_enferma():
    return {"p":"saude_mental_co_saude_mental_enferma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_enferma.get("")
async def i_saude_mental_enferma():
    return {"p":"saude_mental_co_saude_mental_enferma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_farmaci.get("")
async def i_saude_mental_farmaci():
    return {"p":"saude_mental_co_saude_mental_farmaci","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_favela.get("")
async def i_saude_mental_favela():
    return {"p":"saude_mental_co_saude_mental_favela","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_fisiote.get("")
async def i_saude_mental_fisiote():
    return {"p":"saude_mental_co_saude_mental_fisiote","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_fonoaud.get("")
async def i_saude_mental_fonoaud():
    return {"p":"saude_mental_co_saude_mental_fonoaud","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_fundame.get("")
async def i_saude_mental_fundame():
    return {"p":"saude_mental_co_saude_mental_fundame","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_geriatr.get("")
async def i_saude_mental_geriatr():
    return {"p":"saude_mental_co_saude_mental_geriatr","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_industr.get("")
async def i_saude_mental_industr():
    return {"p":"saude_mental_co_saude_mental_industr","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_infanti.get("")
async def i_saude_mental_infanti():
    return {"p":"saude_mental_co_saude_mental_infanti","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_interna.get("")
async def i_saude_mental_interna():
    return {"p":"saude_mental_co_saude_mental_interna","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_interna.get("")
async def i_saude_mental_interna():
    return {"p":"saude_mental_co_saude_mental_interna","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_materni.get("")
async def i_saude_mental_materni():
    return {"p":"saude_mental_co_saude_mental_materni","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_medicin.get("")
async def i_saude_mental_medicin():
    return {"p":"saude_mental_co_saude_mental_medicin","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_neurolo.get("")
async def i_saude_mental_neurolo():
    return {"p":"saude_mental_co_saude_mental_neurolo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_nutrica.get("")
async def i_saude_mental_nutrica():
    return {"p":"saude_mental_co_saude_mental_nutrica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_odontol.get("")
async def i_saude_mental_odontol():
    return {"p":"saude_mental_co_saude_mental_odontol","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_oncolog.get("")
async def i_saude_mental_oncolog():
    return {"p":"saude_mental_co_saude_mental_oncolog","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_ortoped.get("")
async def i_saude_mental_ortoped():
    return {"p":"saude_mental_co_saude_mental_ortoped","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_pediatr.get("")
async def i_saude_mental_pediatr():
    return {"p":"saude_mental_co_saude_mental_pediatr","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_perifer.get("")
async def i_saude_mental_perifer():
    return {"p":"saude_mental_co_saude_mental_perifer","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_pesquis.get("")
async def i_saude_mental_pesquis():
    return {"p":"saude_mental_co_saude_mental_pesquis","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_pos_gra.get("")
async def i_saude_mental_pos_gra():
    return {"p":"saude_mental_co_saude_mental_pos_gra","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_profess.get("")
async def i_saude_mental_profess():
    return {"p":"saude_mental_co_saude_mental_profess","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_pronto_.get("")
async def i_saude_mental_pronto_():
    return {"p":"saude_mental_co_saude_mental_pronto_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_quilomb.get("")
async def i_saude_mental_quilomb():
    return {"p":"saude_mental_co_saude_mental_quilomb","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_reabili.get("")
async def i_saude_mental_reabili():
    return {"p":"saude_mental_co_saude_mental_reabili","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_reitore.get("")
async def i_saude_mental_reitore():
    return {"p":"saude_mental_co_saude_mental_reitore","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_residen.get("")
async def i_saude_mental_residen():
    return {"p":"saude_mental_co_saude_mental_residen","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_rural2.get("")
async def i_saude_mental_rural2():
    return {"p":"saude_mental_co_saude_mental_rural2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_tecnico.get("")
async def i_saude_mental_tecnico():
    return {"p":"saude_mental_co_saude_mental_tecnico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_terapia.get("")
async def i_saude_mental_terapia():
    return {"p":"saude_mental_co_saude_mental_terapia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_univers.get("")
async def i_saude_mental_univers():
    return {"p":"saude_mental_co_saude_mental_univers","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_urbano.get("")
async def i_saude_mental_urbano():
    return {"p":"saude_mental_co_saude_mental_urbano","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_uti2.get("")
async def i_saude_mental_uti2():
    return {"p":"saude_mental_co_saude_mental_uti2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_vestibu.get("")
async def i_saude_mental_vestibu():
    return {"p":"saude_mental_co_saude_mental_vestibu","s":"ativo","t":datetime.utcnow().isoformat()}
@router_saude_mental_zona_po.get("")
async def i_saude_mental_zona_po():
    return {"p":"saude_mental_co_saude_mental_zona_po","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_saude_mental_context(PluginBase):
    name = "consolidated_saude_mental_contextos"
    def setup(self, app):
        app.include_router(router_saude_mental_acampam)
        app.include_router(router_saude_mental_aldeia)
        app.include_router(router_saude_mental_ambulat)
        app.include_router(router_saude_mental_assenta)
        app.include_router(router_saude_mental_berçari)
        app.include_router(router_saude_mental_cardiol)
        app.include_router(router_saude_mental_cirurgi)
        app.include_router(router_saude_mental_comerci)
        app.include_router(router_saude_mental_comunid)
        app.include_router(router_saude_mental_concurs)
        app.include_router(router_saude_mental_coorden)
        app.include_router(router_saude_mental_creche)
        app.include_router(router_saude_mental_diretor)
        app.include_router(router_saude_mental_enferma)
        app.include_router(router_saude_mental_enferma)
        app.include_router(router_saude_mental_farmaci)
        app.include_router(router_saude_mental_favela)
        app.include_router(router_saude_mental_fisiote)
        app.include_router(router_saude_mental_fonoaud)
        app.include_router(router_saude_mental_fundame)
        app.include_router(router_saude_mental_geriatr)
        app.include_router(router_saude_mental_industr)
        app.include_router(router_saude_mental_infanti)
        app.include_router(router_saude_mental_interna)
        app.include_router(router_saude_mental_interna)
        app.include_router(router_saude_mental_materni)
        app.include_router(router_saude_mental_medicin)
        app.include_router(router_saude_mental_neurolo)
        app.include_router(router_saude_mental_nutrica)
        app.include_router(router_saude_mental_odontol)
        app.include_router(router_saude_mental_oncolog)
        app.include_router(router_saude_mental_ortoped)
        app.include_router(router_saude_mental_pediatr)
        app.include_router(router_saude_mental_perifer)
        app.include_router(router_saude_mental_pesquis)
        app.include_router(router_saude_mental_pos_gra)
        app.include_router(router_saude_mental_profess)
        app.include_router(router_saude_mental_pronto_)
        app.include_router(router_saude_mental_quilomb)
        app.include_router(router_saude_mental_reabili)
        app.include_router(router_saude_mental_reitore)
        app.include_router(router_saude_mental_residen)
        app.include_router(router_saude_mental_rural2)
        app.include_router(router_saude_mental_tecnico)
        app.include_router(router_saude_mental_terapia)
        app.include_router(router_saude_mental_univers)
        app.include_router(router_saude_mental_urbano)
        app.include_router(router_saude_mental_uti2)
        app.include_router(router_saude_mental_vestibu)
        app.include_router(router_saude_mental_zona_po)


plugin = Plugin_saude_mental_context()
