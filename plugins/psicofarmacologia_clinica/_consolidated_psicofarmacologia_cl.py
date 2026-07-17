from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_agomelatina = APIRouter(prefix="/api/v1/psicofarmaco/agomelatina", tags=["psicofarmacologia_clinica"])
router_anfetamina_clinica = APIRouter(prefix="/api/v1/psicofarmaco/anfetamina_clinica", tags=["psicofarmacologia_clinica"])
router_ansiolisticos_benzod = APIRouter(prefix="/api/v1/psicofarmaco/ansiolisticos_benzodiazep", tags=["psicofarmacologia_clinica"])
router_antidepressivos_irsn = APIRouter(prefix="/api/v1/psicofarmaco/antidepressivos_irsn", tags=["psicofarmacologia_clinica"])
router_antidepressivos_iss = APIRouter(prefix="/api/v1/psicofarmaco/antidepressivos_iss", tags=["psicofarmacologia_clinica"])
router_antidepressivos_tric = APIRouter(prefix="/api/v1/psicofarmaco/antidepressivos_triciclic", tags=["psicofarmacologia_clinica"])
router_antipsicóticos_atipi = APIRouter(prefix="/api/v1/psicofarmaco/antipsicóticos_atipicos", tags=["psicofarmacologia_clinica"])
router_antipsicóticos_tipic = APIRouter(prefix="/api/v1/psicofarmaco/antipsicóticos_tipicos", tags=["psicofarmacologia_clinica"])
router_aripiprazol_clinica = APIRouter(prefix="/api/v1/psicofarmaco/aripiprazol_clinica", tags=["psicofarmacologia_clinica"])
router_armodafinil_cognicao = APIRouter(prefix="/api/v1/psicofarmaco/armodafinil_cognicao", tags=["psicofarmacologia_clinica"])
router_atomoxetina_tdah = APIRouter(prefix="/api/v1/psicofarmaco/atomoxetina_tdah", tags=["psicofarmacologia_clinica"])
router_bupropiona_clinica = APIRouter(prefix="/api/v1/psicofarmaco/bupropiona_clinica", tags=["psicofarmacologia_clinica"])
router_buspirona_clinica2 = APIRouter(prefix="/api/v1/psicofarmaco/buspirona_clinica2", tags=["psicofarmacologia_clinica"])
router_cannabis_bipolar = APIRouter(prefix="/api/v1/psicofarmaco/cannabis_bipolar", tags=["psicofarmacologia_clinica"])
router_carbamazepina_humor = APIRouter(prefix="/api/v1/psicofarmaco/carbamazepina_humor", tags=["psicofarmacologia_clinica"])
router_cbd_ansiedade = APIRouter(prefix="/api/v1/psicofarmaco/cbd_ansiedade", tags=["psicofarmacologia_clinica"])
router_clonidina_ansiedade = APIRouter(prefix="/api/v1/psicofarmaco/clonidina_ansiedade", tags=["psicofarmacologia_clinica"])
router_clonidina_tdah = APIRouter(prefix="/api/v1/psicofarmaco/clonidina_tdah", tags=["psicofarmacologia_clinica"])
router_clozapina_refrataria = APIRouter(prefix="/api/v1/psicofarmaco/clozapina_refrataria", tags=["psicofarmacologia_clinica"])
router_doxilamina_sono = APIRouter(prefix="/api/v1/psicofarmaco/doxilamina_sono", tags=["psicofarmacologia_clinica"])
router_esketamina_nasal = APIRouter(prefix="/api/v1/psicofarmaco/esketamina_nasal", tags=["psicofarmacologia_clinica"])
router_estabilizadores_carb = APIRouter(prefix="/api/v1/psicofarmaco/estabilizadores_carbonato", tags=["psicofarmacologia_clinica"])
router_eszopiclona = APIRouter(prefix="/api/v1/psicofarmaco/eszopiclona", tags=["psicofarmacologia_clinica"])
router_gabapentina_ansiedad = APIRouter(prefix="/api/v1/psicofarmaco/gabapentina_ansiedade", tags=["psicofarmacologia_clinica"])
router_gabapentina_humor = APIRouter(prefix="/api/v1/psicofarmaco/gabapentina_humor", tags=["psicofarmacologia_clinica"])
router_guanfacina_tdah = APIRouter(prefix="/api/v1/psicofarmaco/guanfacina_tdah", tags=["psicofarmacologia_clinica"])
router_hidroxizina_clinica = APIRouter(prefix="/api/v1/psicofarmaco/hidroxizina_clinica", tags=["psicofarmacologia_clinica"])
router_hipnoticos_z = APIRouter(prefix="/api/v1/psicofarmaco/hipnoticos_z", tags=["psicofarmacologia_clinica"])
router_imao_antidepressivos = APIRouter(prefix="/api/v1/psicofarmaco/imao_antidepressivos", tags=["psicofarmacologia_clinica"])
router_ketamina_iv = APIRouter(prefix="/api/v1/psicofarmaco/ketamina_iv", tags=["psicofarmacologia_clinica"])
router_lamotrigina_humor = APIRouter(prefix="/api/v1/psicofarmaco/lamotrigina_humor", tags=["psicofarmacologia_clinica"])
router_lisdexanfetamina = APIRouter(prefix="/api/v1/psicofarmaco/lisdexanfetamina", tags=["psicofarmacologia_clinica"])
router_litio_clinico = APIRouter(prefix="/api/v1/psicofarmaco/litio_clinico", tags=["psicofarmacologia_clinica"])
router_lurasidona_clinica = APIRouter(prefix="/api/v1/psicofarmaco/lurasidona_clinica", tags=["psicofarmacologia_clinica"])
router_melatonina_suplement = APIRouter(prefix="/api/v1/psicofarmaco/melatonina_suplemento", tags=["psicofarmacologia_clinica"])
router_metilfenidato_adulto = APIRouter(prefix="/api/v1/psicofarmaco/metilfenidato_adulto", tags=["psicofarmacologia_clinica"])
router_metilfenidato_clinic = APIRouter(prefix="/api/v1/psicofarmaco/metilfenidato_clinico", tags=["psicofarmacologia_clinica"])
router_mirtazapina_clinica = APIRouter(prefix="/api/v1/psicofarmaco/mirtazapina_clinica", tags=["psicofarmacologia_clinica"])
router_modafinil_sonolencia = APIRouter(prefix="/api/v1/psicofarmaco/modafinil_sonolencia", tags=["psicofarmacologia_clinica"])
router_olanzapina_clinica = APIRouter(prefix="/api/v1/psicofarmaco/olanzapina_clinica", tags=["psicofarmacologia_clinica"])
router_oxcarbazepina_humor = APIRouter(prefix="/api/v1/psicofarmaco/oxcarbazepina_humor", tags=["psicofarmacologia_clinica"])
router_pregabalina_ansiedad = APIRouter(prefix="/api/v1/psicofarmaco/pregabalina_ansiedade", tags=["psicofarmacologia_clinica"])
router_propranolol_ansiedad = APIRouter(prefix="/api/v1/psicofarmaco/propranolol_ansiedade", tags=["psicofarmacologia_clinica"])
router_psicoestimulantes_td = APIRouter(prefix="/api/v1/psicofarmaco/psicoestimulantes_tdah", tags=["psicofarmacologia_clinica"])
router_quetiapina_clinica = APIRouter(prefix="/api/v1/psicofarmaco/quetiapina_clinica", tags=["psicofarmacologia_clinica"])
router_ramelteon_melatonina = APIRouter(prefix="/api/v1/psicofarmaco/ramelteon_melatonina", tags=["psicofarmacologia_clinica"])
router_risperidona_clinica = APIRouter(prefix="/api/v1/psicofarmaco/risperidona_clinica", tags=["psicofarmacologia_clinica"])
router_suvorexant_orexina = APIRouter(prefix="/api/v1/psicofarmaco/suvorexant_orexina", tags=["psicofarmacologia_clinica"])
router_thc_psicose = APIRouter(prefix="/api/v1/psicofarmaco/thc_psicose", tags=["psicofarmacologia_clinica"])
router_topiramato_psico = APIRouter(prefix="/api/v1/psicofarmaco/topiramato_psico", tags=["psicofarmacologia_clinica"])
router_valproato_humor = APIRouter(prefix="/api/v1/psicofarmaco/valproato_humor", tags=["psicofarmacologia_clinica"])
router_vortioxetina = APIRouter(prefix="/api/v1/psicofarmaco/vortioxetina", tags=["psicofarmacologia_clinica"])
router_zolpidem_sono = APIRouter(prefix="/api/v1/psicofarmaco/zolpidem_sono", tags=["psicofarmacologia_clinica"])
router_zopiclona_sono = APIRouter(prefix="/api/v1/psicofarmaco/zopiclona_sono", tags=["psicofarmacologia_clinica"])

@router_agomelatina.get("")
async def i_agomelatina():
    return {"p":"psicofarmacolog_agomelatina","s":"ativo","t":datetime.utcnow().isoformat()}
@router_anfetamina_clinica.get("")
async def i_anfetamina_clinica():
    return {"p":"psicofarmacolog_anfetamina_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ansiolisticos_benzod.get("")
async def i_ansiolisticos_benzod():
    return {"p":"psicofarmacolog_ansiolisticos_benzod","s":"ativo","t":datetime.utcnow().isoformat()}
@router_antidepressivos_irsn.get("")
async def i_antidepressivos_irsn():
    return {"p":"psicofarmacolog_antidepressivos_irsn","s":"ativo","t":datetime.utcnow().isoformat()}
@router_antidepressivos_iss.get("")
async def i_antidepressivos_iss():
    return {"p":"psicofarmacolog_antidepressivos_iss","s":"ativo","t":datetime.utcnow().isoformat()}
@router_antidepressivos_tric.get("")
async def i_antidepressivos_tric():
    return {"p":"psicofarmacolog_antidepressivos_tric","s":"ativo","t":datetime.utcnow().isoformat()}
@router_antipsicóticos_atipi.get("")
async def i_antipsicóticos_atipi():
    return {"p":"psicofarmacolog_antipsicóticos_atipi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_antipsicóticos_tipic.get("")
async def i_antipsicóticos_tipic():
    return {"p":"psicofarmacolog_antipsicóticos_tipic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_aripiprazol_clinica.get("")
async def i_aripiprazol_clinica():
    return {"p":"psicofarmacolog_aripiprazol_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_armodafinil_cognicao.get("")
async def i_armodafinil_cognicao():
    return {"p":"psicofarmacolog_armodafinil_cognicao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_atomoxetina_tdah.get("")
async def i_atomoxetina_tdah():
    return {"p":"psicofarmacolog_atomoxetina_tdah","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bupropiona_clinica.get("")
async def i_bupropiona_clinica():
    return {"p":"psicofarmacolog_bupropiona_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_buspirona_clinica2.get("")
async def i_buspirona_clinica2():
    return {"p":"psicofarmacolog_buspirona_clinica2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cannabis_bipolar.get("")
async def i_cannabis_bipolar():
    return {"p":"psicofarmacolog_cannabis_bipolar","s":"ativo","t":datetime.utcnow().isoformat()}
@router_carbamazepina_humor.get("")
async def i_carbamazepina_humor():
    return {"p":"psicofarmacolog_carbamazepina_humor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cbd_ansiedade.get("")
async def i_cbd_ansiedade():
    return {"p":"psicofarmacolog_cbd_ansiedade","s":"ativo","t":datetime.utcnow().isoformat()}
@router_clonidina_ansiedade.get("")
async def i_clonidina_ansiedade():
    return {"p":"psicofarmacolog_clonidina_ansiedade","s":"ativo","t":datetime.utcnow().isoformat()}
@router_clonidina_tdah.get("")
async def i_clonidina_tdah():
    return {"p":"psicofarmacolog_clonidina_tdah","s":"ativo","t":datetime.utcnow().isoformat()}
@router_clozapina_refrataria.get("")
async def i_clozapina_refrataria():
    return {"p":"psicofarmacolog_clozapina_refrataria","s":"ativo","t":datetime.utcnow().isoformat()}
@router_doxilamina_sono.get("")
async def i_doxilamina_sono():
    return {"p":"psicofarmacolog_doxilamina_sono","s":"ativo","t":datetime.utcnow().isoformat()}
@router_esketamina_nasal.get("")
async def i_esketamina_nasal():
    return {"p":"psicofarmacolog_esketamina_nasal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_estabilizadores_carb.get("")
async def i_estabilizadores_carb():
    return {"p":"psicofarmacolog_estabilizadores_carb","s":"ativo","t":datetime.utcnow().isoformat()}
@router_eszopiclona.get("")
async def i_eszopiclona():
    return {"p":"psicofarmacolog_eszopiclona","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gabapentina_ansiedad.get("")
async def i_gabapentina_ansiedad():
    return {"p":"psicofarmacolog_gabapentina_ansiedad","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gabapentina_humor.get("")
async def i_gabapentina_humor():
    return {"p":"psicofarmacolog_gabapentina_humor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_guanfacina_tdah.get("")
async def i_guanfacina_tdah():
    return {"p":"psicofarmacolog_guanfacina_tdah","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hidroxizina_clinica.get("")
async def i_hidroxizina_clinica():
    return {"p":"psicofarmacolog_hidroxizina_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hipnoticos_z.get("")
async def i_hipnoticos_z():
    return {"p":"psicofarmacolog_hipnoticos_z","s":"ativo","t":datetime.utcnow().isoformat()}
@router_imao_antidepressivos.get("")
async def i_imao_antidepressivos():
    return {"p":"psicofarmacolog_imao_antidepressivos","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ketamina_iv.get("")
async def i_ketamina_iv():
    return {"p":"psicofarmacolog_ketamina_iv","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lamotrigina_humor.get("")
async def i_lamotrigina_humor():
    return {"p":"psicofarmacolog_lamotrigina_humor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lisdexanfetamina.get("")
async def i_lisdexanfetamina():
    return {"p":"psicofarmacolog_lisdexanfetamina","s":"ativo","t":datetime.utcnow().isoformat()}
@router_litio_clinico.get("")
async def i_litio_clinico():
    return {"p":"psicofarmacolog_litio_clinico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lurasidona_clinica.get("")
async def i_lurasidona_clinica():
    return {"p":"psicofarmacolog_lurasidona_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_melatonina_suplement.get("")
async def i_melatonina_suplement():
    return {"p":"psicofarmacolog_melatonina_suplement","s":"ativo","t":datetime.utcnow().isoformat()}
@router_metilfenidato_adulto.get("")
async def i_metilfenidato_adulto():
    return {"p":"psicofarmacolog_metilfenidato_adulto","s":"ativo","t":datetime.utcnow().isoformat()}
@router_metilfenidato_clinic.get("")
async def i_metilfenidato_clinic():
    return {"p":"psicofarmacolog_metilfenidato_clinic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mirtazapina_clinica.get("")
async def i_mirtazapina_clinica():
    return {"p":"psicofarmacolog_mirtazapina_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_modafinil_sonolencia.get("")
async def i_modafinil_sonolencia():
    return {"p":"psicofarmacolog_modafinil_sonolencia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_olanzapina_clinica.get("")
async def i_olanzapina_clinica():
    return {"p":"psicofarmacolog_olanzapina_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_oxcarbazepina_humor.get("")
async def i_oxcarbazepina_humor():
    return {"p":"psicofarmacolog_oxcarbazepina_humor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pregabalina_ansiedad.get("")
async def i_pregabalina_ansiedad():
    return {"p":"psicofarmacolog_pregabalina_ansiedad","s":"ativo","t":datetime.utcnow().isoformat()}
@router_propranolol_ansiedad.get("")
async def i_propranolol_ansiedad():
    return {"p":"psicofarmacolog_propranolol_ansiedad","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicoestimulantes_td.get("")
async def i_psicoestimulantes_td():
    return {"p":"psicofarmacolog_psicoestimulantes_td","s":"ativo","t":datetime.utcnow().isoformat()}
@router_quetiapina_clinica.get("")
async def i_quetiapina_clinica():
    return {"p":"psicofarmacolog_quetiapina_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ramelteon_melatonina.get("")
async def i_ramelteon_melatonina():
    return {"p":"psicofarmacolog_ramelteon_melatonina","s":"ativo","t":datetime.utcnow().isoformat()}
@router_risperidona_clinica.get("")
async def i_risperidona_clinica():
    return {"p":"psicofarmacolog_risperidona_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_suvorexant_orexina.get("")
async def i_suvorexant_orexina():
    return {"p":"psicofarmacolog_suvorexant_orexina","s":"ativo","t":datetime.utcnow().isoformat()}
@router_thc_psicose.get("")
async def i_thc_psicose():
    return {"p":"psicofarmacolog_thc_psicose","s":"ativo","t":datetime.utcnow().isoformat()}
@router_topiramato_psico.get("")
async def i_topiramato_psico():
    return {"p":"psicofarmacolog_topiramato_psico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_valproato_humor.get("")
async def i_valproato_humor():
    return {"p":"psicofarmacolog_valproato_humor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_vortioxetina.get("")
async def i_vortioxetina():
    return {"p":"psicofarmacolog_vortioxetina","s":"ativo","t":datetime.utcnow().isoformat()}
@router_zolpidem_sono.get("")
async def i_zolpidem_sono():
    return {"p":"psicofarmacolog_zolpidem_sono","s":"ativo","t":datetime.utcnow().isoformat()}
@router_zopiclona_sono.get("")
async def i_zopiclona_sono():
    return {"p":"psicofarmacolog_zopiclona_sono","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_psicofarmacologia_cl(PluginBase):
    name = "consolidated_psicofarmacologia_clinica"
    def setup(self, app):
        app.include_router(router_agomelatina)
        app.include_router(router_anfetamina_clinica)
        app.include_router(router_ansiolisticos_benzod)
        app.include_router(router_antidepressivos_irsn)
        app.include_router(router_antidepressivos_iss)
        app.include_router(router_antidepressivos_tric)
        app.include_router(router_antipsicóticos_atipi)
        app.include_router(router_antipsicóticos_tipic)
        app.include_router(router_aripiprazol_clinica)
        app.include_router(router_armodafinil_cognicao)
        app.include_router(router_atomoxetina_tdah)
        app.include_router(router_bupropiona_clinica)
        app.include_router(router_buspirona_clinica2)
        app.include_router(router_cannabis_bipolar)
        app.include_router(router_carbamazepina_humor)
        app.include_router(router_cbd_ansiedade)
        app.include_router(router_clonidina_ansiedade)
        app.include_router(router_clonidina_tdah)
        app.include_router(router_clozapina_refrataria)
        app.include_router(router_doxilamina_sono)
        app.include_router(router_esketamina_nasal)
        app.include_router(router_estabilizadores_carb)
        app.include_router(router_eszopiclona)
        app.include_router(router_gabapentina_ansiedad)
        app.include_router(router_gabapentina_humor)
        app.include_router(router_guanfacina_tdah)
        app.include_router(router_hidroxizina_clinica)
        app.include_router(router_hipnoticos_z)
        app.include_router(router_imao_antidepressivos)
        app.include_router(router_ketamina_iv)
        app.include_router(router_lamotrigina_humor)
        app.include_router(router_lisdexanfetamina)
        app.include_router(router_litio_clinico)
        app.include_router(router_lurasidona_clinica)
        app.include_router(router_melatonina_suplement)
        app.include_router(router_metilfenidato_adulto)
        app.include_router(router_metilfenidato_clinic)
        app.include_router(router_mirtazapina_clinica)
        app.include_router(router_modafinil_sonolencia)
        app.include_router(router_olanzapina_clinica)
        app.include_router(router_oxcarbazepina_humor)
        app.include_router(router_pregabalina_ansiedad)
        app.include_router(router_propranolol_ansiedad)
        app.include_router(router_psicoestimulantes_td)
        app.include_router(router_quetiapina_clinica)
        app.include_router(router_ramelteon_melatonina)
        app.include_router(router_risperidona_clinica)
        app.include_router(router_suvorexant_orexina)
        app.include_router(router_thc_psicose)
        app.include_router(router_topiramato_psico)
        app.include_router(router_valproato_humor)
        app.include_router(router_vortioxetina)
        app.include_router(router_zolpidem_sono)
        app.include_router(router_zopiclona_sono)


plugin = Plugin_psicofarmacologia_cl()
