from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_acetilcisteina = APIRouter(prefix="/api/v1/farmacologia/acetilcisteina", tags=["farmacologia_psiquiatrica_avancada"])
router_adiponectina_mental = APIRouter(prefix="/api/v1/farmacologia/adiponectina_mental", tags=["farmacologia_psiquiatrica_avancada"])
router_agonista_inverso = APIRouter(prefix="/api/v1/farmacologia/agonista_inverso", tags=["farmacologia_psiquiatrica_avancada"])
router_agonista_parcial = APIRouter(prefix="/api/v1/farmacologia/agonista_parcial", tags=["farmacologia_psiquiatrica_avancada"])
router_agonista_receptor = APIRouter(prefix="/api/v1/farmacologia/agonista_receptor", tags=["farmacologia_psiquiatrica_avancada"])
router_alfa_cetoglutarato = APIRouter(prefix="/api/v1/farmacologia/alfa_cetoglutarato", tags=["farmacologia_psiquiatrica_avancada"])
router_allosteric_modulator = APIRouter(prefix="/api/v1/farmacologia/allosteric_modulator", tags=["farmacologia_psiquiatrica_avancada"])
router_antagonista_receptor = APIRouter(prefix="/api/v1/farmacologia/antagonista_receptor", tags=["farmacologia_psiquiatrica_avancada"])
router_antioxidante_endogen = APIRouter(prefix="/api/v1/farmacologia/antioxidante_endogeno", tags=["farmacologia_psiquiatrica_avancada"])
router_antocianina = APIRouter(prefix="/api/v1/farmacologia/antocianina", tags=["farmacologia_psiquiatrica_avancada"])
router_atp_producao = APIRouter(prefix="/api/v1/farmacologia/atp_producao", tags=["farmacologia_psiquiatrica_avancada"])
router_bdnf_trkb = APIRouter(prefix="/api/v1/farmacologia/bdnf_trkb", tags=["farmacologia_psiquiatrica_avancada"])
router_camp_pathway = APIRouter(prefix="/api/v1/farmacologia/camp_pathway", tags=["farmacologia_psiquiatrica_avancada"])
router_catalase_cerebro = APIRouter(prefix="/api/v1/farmacologia/catalase_cerebro", tags=["farmacologia_psiquiatrica_avancada"])
router_cetose_cerebro = APIRouter(prefix="/api/v1/farmacologia/cetose_cerebro", tags=["farmacologia_psiquiatrica_avancada"])
router_ciclo_krebs_cerebro = APIRouter(prefix="/api/v1/farmacologia/ciclo_krebs_cerebro", tags=["farmacologia_psiquiatrica_avancada"])
router_cpeptide_mental = APIRouter(prefix="/api/v1/farmacologia/cpeptide_mental", tags=["farmacologia_psiquiatrica_avancada"])
router_curcumina2 = APIRouter(prefix="/api/v1/farmacologia/curcumina2", tags=["farmacologia_psiquiatrica_avancada"])
router_daidzeina = APIRouter(prefix="/api/v1/farmacologia/daidzeina", tags=["farmacologia_psiquiatrica_avancada"])
router_disfuncao_mitocondri = APIRouter(prefix="/api/v1/farmacologia/disfuncao_mitocondrial", tags=["farmacologia_psiquiatrica_avancada"])
router_dpp4_mental = APIRouter(prefix="/api/v1/farmacologia/dpp4_mental", tags=["farmacologia_psiquiatrica_avancada"])
router_equol_mental = APIRouter(prefix="/api/v1/farmacologia/equol_mental", tags=["farmacologia_psiquiatrica_avancada"])
router_estresse_oxidativo2 = APIRouter(prefix="/api/v1/farmacologia/estresse_oxidativo2", tags=["farmacologia_psiquiatrica_avancada"])
router_fisetin_mental = APIRouter(prefix="/api/v1/farmacologia/fisetin_mental", tags=["farmacologia_psiquiatrica_avancada"])
router_flavonoide_mental = APIRouter(prefix="/api/v1/farmacologia/flavonoide_mental", tags=["farmacologia_psiquiatrica_avancada"])
router_fosforilacao_oxidati = APIRouter(prefix="/api/v1/farmacologia/fosforilacao_oxidativa", tags=["farmacologia_psiquiatrica_avancada"])
router_fumarato = APIRouter(prefix="/api/v1/farmacologia/fumarato", tags=["farmacologia_psiquiatrica_avancada"])
router_gdnf_gfralpha = APIRouter(prefix="/api/v1/farmacologia/gdnf_gfralpha", tags=["farmacologia_psiquiatrica_avancada"])
router_genisteina = APIRouter(prefix="/api/v1/farmacologia/genisteina", tags=["farmacologia_psiquiatrica_avancada"])
router_ghrelin_mental = APIRouter(prefix="/api/v1/farmacologia/ghrelin_mental", tags=["farmacologia_psiquiatrica_avancada"])
router_glp1_mental = APIRouter(prefix="/api/v1/farmacologia/glp1_mental", tags=["farmacologia_psiquiatrica_avancada"])
router_glucagon_mental = APIRouter(prefix="/api/v1/farmacologia/glucagon_mental", tags=["farmacologia_psiquiatrica_avancada"])
router_glutationa_cerebro = APIRouter(prefix="/api/v1/farmacologia/glutationa_cerebro", tags=["farmacologia_psiquiatrica_avancada"])
router_gsh_mental = APIRouter(prefix="/api/v1/farmacologia/gsh_mental", tags=["farmacologia_psiquiatrica_avancada"])
router_hba1c_mental = APIRouter(prefix="/api/v1/farmacologia/hba1c_mental", tags=["farmacologia_psiquiatrica_avancada"])
router_hesperidina = APIRouter(prefix="/api/v1/farmacologia/hesperidina", tags=["farmacologia_psiquiatrica_avancada"])
router_igf1_signaling = APIRouter(prefix="/api/v1/farmacologia/igf1_signaling", tags=["farmacologia_psiquiatrica_avancada"])
router_insulin_brain = APIRouter(prefix="/api/v1/farmacologia/insulin_brain", tags=["farmacologia_psiquiatrica_avancada"])
router_ip3_pathway = APIRouter(prefix="/api/v1/farmacologia/ip3_pathway", tags=["farmacologia_psiquiatrica_avancada"])
router_jak_stat = APIRouter(prefix="/api/v1/farmacologia/jak_stat", tags=["farmacologia_psiquiatrica_avancada"])
router_kaempferol = APIRouter(prefix="/api/v1/farmacologia/kaempferol", tags=["farmacologia_psiquiatrica_avancada"])
router_lactato_cerebro = APIRouter(prefix="/api/v1/farmacologia/lactato_cerebro", tags=["farmacologia_psiquiatrica_avancada"])
router_leptin_mental = APIRouter(prefix="/api/v1/farmacologia/leptin_mental", tags=["farmacologia_psiquiatrica_avancada"])
router_malato_cerebro = APIRouter(prefix="/api/v1/farmacologia/malato_cerebro", tags=["farmacologia_psiquiatrica_avancada"])
router_mapk_pathway = APIRouter(prefix="/api/v1/farmacologia/mapk_pathway", tags=["farmacologia_psiquiatrica_avancada"])
router_melatonina2 = APIRouter(prefix="/api/v1/farmacologia/melatonina2", tags=["farmacologia_psiquiatrica_avancada"])
router_metabolismo_glicose_ = APIRouter(prefix="/api/v1/farmacologia/metabolismo_glicose_cereb", tags=["farmacologia_psiquiatrica_avancada"])
router_mitocondria_mental = APIRouter(prefix="/api/v1/farmacologia/mitocondria_mental", tags=["farmacologia_psiquiatrica_avancada"])
router_modulador_alosterico = APIRouter(prefix="/api/v1/farmacologia/modulador_alosterico", tags=["farmacologia_psiquiatrica_avancada"])
router_modulador_receptor = APIRouter(prefix="/api/v1/farmacologia/modulador_receptor", tags=["farmacologia_psiquiatrica_avancada"])
router_mtor_pathway = APIRouter(prefix="/api/v1/farmacologia/mtor_pathway", tags=["farmacologia_psiquiatrica_avancada"])
router_nac_mental = APIRouter(prefix="/api/v1/farmacologia/nac_mental", tags=["farmacologia_psiquiatrica_avancada"])
router_nam_modulator = APIRouter(prefix="/api/v1/farmacologia/nam_modulator", tags=["farmacologia_psiquiatrica_avancada"])
router_naringenina = APIRouter(prefix="/api/v1/farmacologia/naringenina", tags=["farmacologia_psiquiatrica_avancada"])
router_negative_allosteric = APIRouter(prefix="/api/v1/farmacologia/negative_allosteric", tags=["farmacologia_psiquiatrica_avancada"])
router_neurotrophin_signali = APIRouter(prefix="/api/v1/farmacologia/neurotrophin_signaling", tags=["farmacologia_psiquiatrica_avancada"])
router_ngf_trka = APIRouter(prefix="/api/v1/farmacologia/ngf_trka", tags=["farmacologia_psiquiatrica_avancada"])
router_nt3_trkc = APIRouter(prefix="/api/v1/farmacologia/nt3_trkc", tags=["farmacologia_psiquiatrica_avancada"])
router_oxaloacetato = APIRouter(prefix="/api/v1/farmacologia/oxaloacetato", tags=["farmacologia_psiquiatrica_avancada"])
router_pam_modulator = APIRouter(prefix="/api/v1/farmacologia/pam_modulator", tags=["farmacologia_psiquiatrica_avancada"])
router_peroxiredoxina = APIRouter(prefix="/api/v1/farmacologia/peroxiredoxina", tags=["farmacologia_psiquiatrica_avancada"])
router_pi3k_akt = APIRouter(prefix="/api/v1/farmacologia/pi3k_akt", tags=["farmacologia_psiquiatrica_avancada"])
router_piruvato_cerebro = APIRouter(prefix="/api/v1/farmacologia/piruvato_cerebro", tags=["farmacologia_psiquiatrica_avancada"])
router_polifenol_mental = APIRouter(prefix="/api/v1/farmacologia/polifenol_mental", tags=["farmacologia_psiquiatrica_avancada"])
router_positive_allosteric = APIRouter(prefix="/api/v1/farmacologia/positive_allosteric", tags=["farmacologia_psiquiatrica_avancada"])
router_pterostilbene = APIRouter(prefix="/api/v1/farmacologia/pterostilbene", tags=["farmacologia_psiquiatrica_avancada"])
router_quercetina_mental = APIRouter(prefix="/api/v1/farmacologia/quercetina_mental", tags=["farmacologia_psiquiatrica_avancada"])
router_radicais_livres = APIRouter(prefix="/api/v1/farmacologia/radicais_livres", tags=["farmacologia_psiquiatrica_avancada"])
router_receptor_coupling = APIRouter(prefix="/api/v1/farmacologia/receptor_coupling", tags=["farmacologia_psiquiatrica_avancada"])
router_resistina_mental = APIRouter(prefix="/api/v1/farmacologia/resistina_mental", tags=["farmacologia_psiquiatrica_avancada"])
router_resveratrol_mental = APIRouter(prefix="/api/v1/farmacologia/resveratrol_mental", tags=["farmacologia_psiquiatrica_avancada"])
router_rutina_mental = APIRouter(prefix="/api/v1/farmacologia/rutina_mental", tags=["farmacologia_psiquiatrica_avancada"])
router_second_messenger = APIRouter(prefix="/api/v1/farmacologia/second_messenger", tags=["farmacologia_psiquiatrica_avancada"])
router_sglt2_mental = APIRouter(prefix="/api/v1/farmacologia/sglt2_mental", tags=["farmacologia_psiquiatrica_avancada"])
router_signal_transduction = APIRouter(prefix="/api/v1/farmacologia/signal_transduction", tags=["farmacologia_psiquiatrica_avancada"])
router_silent_allosteric = APIRouter(prefix="/api/v1/farmacologia/silent_allosteric", tags=["farmacologia_psiquiatrica_avancada"])
router_sod_cerebro = APIRouter(prefix="/api/v1/farmacologia/sod_cerebro", tags=["farmacologia_psiquiatrica_avancada"])
router_succinato_cerebro = APIRouter(prefix="/api/v1/farmacologia/succinato_cerebro", tags=["farmacologia_psiquiatrica_avancada"])
router_tioredoxina = APIRouter(prefix="/api/v1/farmacologia/tioredoxina", tags=["farmacologia_psiquiatrica_avancada"])
router_vegf_mental = APIRouter(prefix="/api/v1/farmacologia/vegf_mental", tags=["farmacologia_psiquiatrica_avancada"])

@router_acetilcisteina.get("")
async def i_acetilcisteina():
    return {"p":"farmacologia_ps_acetilcisteina","s":"ativo","t":datetime.utcnow().isoformat()}
@router_adiponectina_mental.get("")
async def i_adiponectina_mental():
    return {"p":"farmacologia_ps_adiponectina_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_agonista_inverso.get("")
async def i_agonista_inverso():
    return {"p":"farmacologia_ps_agonista_inverso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_agonista_parcial.get("")
async def i_agonista_parcial():
    return {"p":"farmacologia_ps_agonista_parcial","s":"ativo","t":datetime.utcnow().isoformat()}
@router_agonista_receptor.get("")
async def i_agonista_receptor():
    return {"p":"farmacologia_ps_agonista_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_alfa_cetoglutarato.get("")
async def i_alfa_cetoglutarato():
    return {"p":"farmacologia_ps_alfa_cetoglutarato","s":"ativo","t":datetime.utcnow().isoformat()}
@router_allosteric_modulator.get("")
async def i_allosteric_modulator():
    return {"p":"farmacologia_ps_allosteric_modulator","s":"ativo","t":datetime.utcnow().isoformat()}
@router_antagonista_receptor.get("")
async def i_antagonista_receptor():
    return {"p":"farmacologia_ps_antagonista_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_antioxidante_endogen.get("")
async def i_antioxidante_endogen():
    return {"p":"farmacologia_ps_antioxidante_endogen","s":"ativo","t":datetime.utcnow().isoformat()}
@router_antocianina.get("")
async def i_antocianina():
    return {"p":"farmacologia_ps_antocianina","s":"ativo","t":datetime.utcnow().isoformat()}
@router_atp_producao.get("")
async def i_atp_producao():
    return {"p":"farmacologia_ps_atp_producao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bdnf_trkb.get("")
async def i_bdnf_trkb():
    return {"p":"farmacologia_ps_bdnf_trkb","s":"ativo","t":datetime.utcnow().isoformat()}
@router_camp_pathway.get("")
async def i_camp_pathway():
    return {"p":"farmacologia_ps_camp_pathway","s":"ativo","t":datetime.utcnow().isoformat()}
@router_catalase_cerebro.get("")
async def i_catalase_cerebro():
    return {"p":"farmacologia_ps_catalase_cerebro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cetose_cerebro.get("")
async def i_cetose_cerebro():
    return {"p":"farmacologia_ps_cetose_cerebro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ciclo_krebs_cerebro.get("")
async def i_ciclo_krebs_cerebro():
    return {"p":"farmacologia_ps_ciclo_krebs_cerebro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cpeptide_mental.get("")
async def i_cpeptide_mental():
    return {"p":"farmacologia_ps_cpeptide_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_curcumina2.get("")
async def i_curcumina2():
    return {"p":"farmacologia_ps_curcumina2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_daidzeina.get("")
async def i_daidzeina():
    return {"p":"farmacologia_ps_daidzeina","s":"ativo","t":datetime.utcnow().isoformat()}
@router_disfuncao_mitocondri.get("")
async def i_disfuncao_mitocondri():
    return {"p":"farmacologia_ps_disfuncao_mitocondri","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dpp4_mental.get("")
async def i_dpp4_mental():
    return {"p":"farmacologia_ps_dpp4_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_equol_mental.get("")
async def i_equol_mental():
    return {"p":"farmacologia_ps_equol_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_estresse_oxidativo2.get("")
async def i_estresse_oxidativo2():
    return {"p":"farmacologia_ps_estresse_oxidativo2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fisetin_mental.get("")
async def i_fisetin_mental():
    return {"p":"farmacologia_ps_fisetin_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_flavonoide_mental.get("")
async def i_flavonoide_mental():
    return {"p":"farmacologia_ps_flavonoide_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fosforilacao_oxidati.get("")
async def i_fosforilacao_oxidati():
    return {"p":"farmacologia_ps_fosforilacao_oxidati","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fumarato.get("")
async def i_fumarato():
    return {"p":"farmacologia_ps_fumarato","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gdnf_gfralpha.get("")
async def i_gdnf_gfralpha():
    return {"p":"farmacologia_ps_gdnf_gfralpha","s":"ativo","t":datetime.utcnow().isoformat()}
@router_genisteina.get("")
async def i_genisteina():
    return {"p":"farmacologia_ps_genisteina","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ghrelin_mental.get("")
async def i_ghrelin_mental():
    return {"p":"farmacologia_ps_ghrelin_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_glp1_mental.get("")
async def i_glp1_mental():
    return {"p":"farmacologia_ps_glp1_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_glucagon_mental.get("")
async def i_glucagon_mental():
    return {"p":"farmacologia_ps_glucagon_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_glutationa_cerebro.get("")
async def i_glutationa_cerebro():
    return {"p":"farmacologia_ps_glutationa_cerebro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gsh_mental.get("")
async def i_gsh_mental():
    return {"p":"farmacologia_ps_gsh_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hba1c_mental.get("")
async def i_hba1c_mental():
    return {"p":"farmacologia_ps_hba1c_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hesperidina.get("")
async def i_hesperidina():
    return {"p":"farmacologia_ps_hesperidina","s":"ativo","t":datetime.utcnow().isoformat()}
@router_igf1_signaling.get("")
async def i_igf1_signaling():
    return {"p":"farmacologia_ps_igf1_signaling","s":"ativo","t":datetime.utcnow().isoformat()}
@router_insulin_brain.get("")
async def i_insulin_brain():
    return {"p":"farmacologia_ps_insulin_brain","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ip3_pathway.get("")
async def i_ip3_pathway():
    return {"p":"farmacologia_ps_ip3_pathway","s":"ativo","t":datetime.utcnow().isoformat()}
@router_jak_stat.get("")
async def i_jak_stat():
    return {"p":"farmacologia_ps_jak_stat","s":"ativo","t":datetime.utcnow().isoformat()}
@router_kaempferol.get("")
async def i_kaempferol():
    return {"p":"farmacologia_ps_kaempferol","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lactato_cerebro.get("")
async def i_lactato_cerebro():
    return {"p":"farmacologia_ps_lactato_cerebro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_leptin_mental.get("")
async def i_leptin_mental():
    return {"p":"farmacologia_ps_leptin_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_malato_cerebro.get("")
async def i_malato_cerebro():
    return {"p":"farmacologia_ps_malato_cerebro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mapk_pathway.get("")
async def i_mapk_pathway():
    return {"p":"farmacologia_ps_mapk_pathway","s":"ativo","t":datetime.utcnow().isoformat()}
@router_melatonina2.get("")
async def i_melatonina2():
    return {"p":"farmacologia_ps_melatonina2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_metabolismo_glicose_.get("")
async def i_metabolismo_glicose_():
    return {"p":"farmacologia_ps_metabolismo_glicose_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mitocondria_mental.get("")
async def i_mitocondria_mental():
    return {"p":"farmacologia_ps_mitocondria_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_modulador_alosterico.get("")
async def i_modulador_alosterico():
    return {"p":"farmacologia_ps_modulador_alosterico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_modulador_receptor.get("")
async def i_modulador_receptor():
    return {"p":"farmacologia_ps_modulador_receptor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mtor_pathway.get("")
async def i_mtor_pathway():
    return {"p":"farmacologia_ps_mtor_pathway","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nac_mental.get("")
async def i_nac_mental():
    return {"p":"farmacologia_ps_nac_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nam_modulator.get("")
async def i_nam_modulator():
    return {"p":"farmacologia_ps_nam_modulator","s":"ativo","t":datetime.utcnow().isoformat()}
@router_naringenina.get("")
async def i_naringenina():
    return {"p":"farmacologia_ps_naringenina","s":"ativo","t":datetime.utcnow().isoformat()}
@router_negative_allosteric.get("")
async def i_negative_allosteric():
    return {"p":"farmacologia_ps_negative_allosteric","s":"ativo","t":datetime.utcnow().isoformat()}
@router_neurotrophin_signali.get("")
async def i_neurotrophin_signali():
    return {"p":"farmacologia_ps_neurotrophin_signali","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ngf_trka.get("")
async def i_ngf_trka():
    return {"p":"farmacologia_ps_ngf_trka","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nt3_trkc.get("")
async def i_nt3_trkc():
    return {"p":"farmacologia_ps_nt3_trkc","s":"ativo","t":datetime.utcnow().isoformat()}
@router_oxaloacetato.get("")
async def i_oxaloacetato():
    return {"p":"farmacologia_ps_oxaloacetato","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pam_modulator.get("")
async def i_pam_modulator():
    return {"p":"farmacologia_ps_pam_modulator","s":"ativo","t":datetime.utcnow().isoformat()}
@router_peroxiredoxina.get("")
async def i_peroxiredoxina():
    return {"p":"farmacologia_ps_peroxiredoxina","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pi3k_akt.get("")
async def i_pi3k_akt():
    return {"p":"farmacologia_ps_pi3k_akt","s":"ativo","t":datetime.utcnow().isoformat()}
@router_piruvato_cerebro.get("")
async def i_piruvato_cerebro():
    return {"p":"farmacologia_ps_piruvato_cerebro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_polifenol_mental.get("")
async def i_polifenol_mental():
    return {"p":"farmacologia_ps_polifenol_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_positive_allosteric.get("")
async def i_positive_allosteric():
    return {"p":"farmacologia_ps_positive_allosteric","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pterostilbene.get("")
async def i_pterostilbene():
    return {"p":"farmacologia_ps_pterostilbene","s":"ativo","t":datetime.utcnow().isoformat()}
@router_quercetina_mental.get("")
async def i_quercetina_mental():
    return {"p":"farmacologia_ps_quercetina_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_radicais_livres.get("")
async def i_radicais_livres():
    return {"p":"farmacologia_ps_radicais_livres","s":"ativo","t":datetime.utcnow().isoformat()}
@router_receptor_coupling.get("")
async def i_receptor_coupling():
    return {"p":"farmacologia_ps_receptor_coupling","s":"ativo","t":datetime.utcnow().isoformat()}
@router_resistina_mental.get("")
async def i_resistina_mental():
    return {"p":"farmacologia_ps_resistina_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_resveratrol_mental.get("")
async def i_resveratrol_mental():
    return {"p":"farmacologia_ps_resveratrol_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_rutina_mental.get("")
async def i_rutina_mental():
    return {"p":"farmacologia_ps_rutina_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_second_messenger.get("")
async def i_second_messenger():
    return {"p":"farmacologia_ps_second_messenger","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sglt2_mental.get("")
async def i_sglt2_mental():
    return {"p":"farmacologia_ps_sglt2_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_signal_transduction.get("")
async def i_signal_transduction():
    return {"p":"farmacologia_ps_signal_transduction","s":"ativo","t":datetime.utcnow().isoformat()}
@router_silent_allosteric.get("")
async def i_silent_allosteric():
    return {"p":"farmacologia_ps_silent_allosteric","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sod_cerebro.get("")
async def i_sod_cerebro():
    return {"p":"farmacologia_ps_sod_cerebro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_succinato_cerebro.get("")
async def i_succinato_cerebro():
    return {"p":"farmacologia_ps_succinato_cerebro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tioredoxina.get("")
async def i_tioredoxina():
    return {"p":"farmacologia_ps_tioredoxina","s":"ativo","t":datetime.utcnow().isoformat()}
@router_vegf_mental.get("")
async def i_vegf_mental():
    return {"p":"farmacologia_ps_vegf_mental","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_farmacologia_psiquia(PluginBase):
    name = "consolidated_farmacologia_psiquiatrica_avan"
    def setup(self, app):
        app.include_router(router_acetilcisteina)
        app.include_router(router_adiponectina_mental)
        app.include_router(router_agonista_inverso)
        app.include_router(router_agonista_parcial)
        app.include_router(router_agonista_receptor)
        app.include_router(router_alfa_cetoglutarato)
        app.include_router(router_allosteric_modulator)
        app.include_router(router_antagonista_receptor)
        app.include_router(router_antioxidante_endogen)
        app.include_router(router_antocianina)
        app.include_router(router_atp_producao)
        app.include_router(router_bdnf_trkb)
        app.include_router(router_camp_pathway)
        app.include_router(router_catalase_cerebro)
        app.include_router(router_cetose_cerebro)
        app.include_router(router_ciclo_krebs_cerebro)
        app.include_router(router_cpeptide_mental)
        app.include_router(router_curcumina2)
        app.include_router(router_daidzeina)
        app.include_router(router_disfuncao_mitocondri)
        app.include_router(router_dpp4_mental)
        app.include_router(router_equol_mental)
        app.include_router(router_estresse_oxidativo2)
        app.include_router(router_fisetin_mental)
        app.include_router(router_flavonoide_mental)
        app.include_router(router_fosforilacao_oxidati)
        app.include_router(router_fumarato)
        app.include_router(router_gdnf_gfralpha)
        app.include_router(router_genisteina)
        app.include_router(router_ghrelin_mental)
        app.include_router(router_glp1_mental)
        app.include_router(router_glucagon_mental)
        app.include_router(router_glutationa_cerebro)
        app.include_router(router_gsh_mental)
        app.include_router(router_hba1c_mental)
        app.include_router(router_hesperidina)
        app.include_router(router_igf1_signaling)
        app.include_router(router_insulin_brain)
        app.include_router(router_ip3_pathway)
        app.include_router(router_jak_stat)
        app.include_router(router_kaempferol)
        app.include_router(router_lactato_cerebro)
        app.include_router(router_leptin_mental)
        app.include_router(router_malato_cerebro)
        app.include_router(router_mapk_pathway)
        app.include_router(router_melatonina2)
        app.include_router(router_metabolismo_glicose_)
        app.include_router(router_mitocondria_mental)
        app.include_router(router_modulador_alosterico)
        app.include_router(router_modulador_receptor)
        app.include_router(router_mtor_pathway)
        app.include_router(router_nac_mental)
        app.include_router(router_nam_modulator)
        app.include_router(router_naringenina)
        app.include_router(router_negative_allosteric)
        app.include_router(router_neurotrophin_signali)
        app.include_router(router_ngf_trka)
        app.include_router(router_nt3_trkc)
        app.include_router(router_oxaloacetato)
        app.include_router(router_pam_modulator)
        app.include_router(router_peroxiredoxina)
        app.include_router(router_pi3k_akt)
        app.include_router(router_piruvato_cerebro)
        app.include_router(router_polifenol_mental)
        app.include_router(router_positive_allosteric)
        app.include_router(router_pterostilbene)
        app.include_router(router_quercetina_mental)
        app.include_router(router_radicais_livres)
        app.include_router(router_receptor_coupling)
        app.include_router(router_resistina_mental)
        app.include_router(router_resveratrol_mental)
        app.include_router(router_rutina_mental)
        app.include_router(router_second_messenger)
        app.include_router(router_sglt2_mental)
        app.include_router(router_signal_transduction)
        app.include_router(router_silent_allosteric)
        app.include_router(router_sod_cerebro)
        app.include_router(router_succinato_cerebro)
        app.include_router(router_tioredoxina)
        app.include_router(router_vegf_mental)


plugin = Plugin_farmacologia_psiquia()
