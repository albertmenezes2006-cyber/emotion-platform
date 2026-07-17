from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_abertura = APIRouter(prefix="/api/v1/fenomenologi/abertura", tags=["fenomenologia_psicologica"])
router_afeccao_fenomenologi = APIRouter(prefix="/api/v1/fenomenologi/afeccao_fenomenologica", tags=["fenomenologia_psicologica"])
router_afeto_fenomenologico = APIRouter(prefix="/api/v1/fenomenologi/afeto_fenomenologico", tags=["fenomenologia_psicologica"])
router_ambiguidade_dasein = APIRouter(prefix="/api/v1/fenomenologi/ambiguidade_dasein", tags=["fenomenologia_psicologica"])
router_angst_heidegger = APIRouter(prefix="/api/v1/fenomenologi/angst_heidegger", tags=["fenomenologia_psicologica"])
router_angustia_heidegger = APIRouter(prefix="/api/v1/fenomenologi/angustia_heidegger", tags=["fenomenologia_psicologica"])
router_associacao_fenomenol = APIRouter(prefix="/api/v1/fenomenologi/associacao_fenomenologica", tags=["fenomenologia_psicologica"])
router_carncia_ryzanek = APIRouter(prefix="/api/v1/fenomenologi/carncia_ryzanek", tags=["fenomenologia_psicologica"])
router_clamor_consciencia = APIRouter(prefix="/api/v1/fenomenologi/clamor_consciencia", tags=["fenomenologia_psicologica"])
router_consciencia_heidegge = APIRouter(prefix="/api/v1/fenomenologi/consciencia_heidegger", tags=["fenomenologia_psicologica"])
router_consciencia_interna = APIRouter(prefix="/api/v1/fenomenologi/consciencia_interna", tags=["fenomenologia_psicologica"])
router_consciencia_temporal = APIRouter(prefix="/api/v1/fenomenologi/consciencia_temporal", tags=["fenomenologia_psicologica"])
router_constituicao_transce = APIRouter(prefix="/api/v1/fenomenologi/constituicao_transcendent", tags=["fenomenologia_psicologica"])
router_corpo_objetivo = APIRouter(prefix="/api/v1/fenomenologi/corpo_objetivo", tags=["fenomenologia_psicologica"])
router_corpo_proprio = APIRouter(prefix="/api/v1/fenomenologi/corpo_proprio", tags=["fenomenologia_psicologica"])
router_corpo_vivido = APIRouter(prefix="/api/v1/fenomenologi/corpo_vivido", tags=["fenomenologia_psicologica"])
router_corporalidade_fenome = APIRouter(prefix="/api/v1/fenomenologi/corporalidade_fenomenolog", tags=["fenomenologia_psicologica"])
router_corps_vecu = APIRouter(prefix="/api/v1/fenomenologi/corps_vecu", tags=["fenomenologia_psicologica"])
router_cuidado_heidegger = APIRouter(prefix="/api/v1/fenomenologi/cuidado_heidegger", tags=["fenomenologia_psicologica"])
router_culpa_heidegger = APIRouter(prefix="/api/v1/fenomenologi/culpa_heidegger", tags=["fenomenologia_psicologica"])
router_curiosidade_heidegge = APIRouter(prefix="/api/v1/fenomenologi/curiosidade_heidegger", tags=["fenomenologia_psicologica"])
router_dasein = APIRouter(prefix="/api/v1/fenomenologi/dasein", tags=["fenomenologia_psicologica"])
router_desocultamento = APIRouter(prefix="/api/v1/fenomenologi/desocultamento", tags=["fenomenologia_psicologica"])
router_dis_closure = APIRouter(prefix="/api/v1/fenomenologi/dis_closure", tags=["fenomenologia_psicologica"])
router_ego_transcendental = APIRouter(prefix="/api/v1/fenomenologi/ego_transcendental", tags=["fenomenologia_psicologica"])
router_eigentlichkeit = APIRouter(prefix="/api/v1/fenomenologi/eigentlichkeit", tags=["fenomenologia_psicologica"])
router_embodiment_fenomenol = APIRouter(prefix="/api/v1/fenomenologi/embodiment_fenomenologico", tags=["fenomenologia_psicologica"])
router_empatia_fenomenologi = APIRouter(prefix="/api/v1/fenomenologi/empatia_fenomenologica", tags=["fenomenologia_psicologica"])
router_epoché_fenomenologic = APIRouter(prefix="/api/v1/fenomenologi/epoché_fenomenologica", tags=["fenomenologia_psicologica"])
router_espacialidade_dasein = APIRouter(prefix="/api/v1/fenomenologi/espacialidade_dasein", tags=["fenomenologia_psicologica"])
router_espaco_vivido = APIRouter(prefix="/api/v1/fenomenologi/espaco_vivido", tags=["fenomenologia_psicologica"])
router_essencia_fenomenolog = APIRouter(prefix="/api/v1/fenomenologi/essencia_fenomenologica", tags=["fenomenologia_psicologica"])
router_existencial_heidegge = APIRouter(prefix="/api/v1/fenomenologi/existencial_heidegger", tags=["fenomenologia_psicologica"])
router_existenciario = APIRouter(prefix="/api/v1/fenomenologi/existenciario", tags=["fenomenologia_psicologica"])
router_factidade = APIRouter(prefix="/api/v1/fenomenologi/factidade", tags=["fenomenologia_psicologica"])
router_falatório = APIRouter(prefix="/api/v1/fenomenologi/falatório", tags=["fenomenologia_psicologica"])
router_fenomenologia_husser = APIRouter(prefix="/api/v1/fenomenologi/fenomenologia_husserliana", tags=["fenomenologia_psicologica"])
router_fluxo_temporal = APIRouter(prefix="/api/v1/fenomenologi/fluxo_temporal", tags=["fenomenologia_psicologica"])
router_gesto_expressivo = APIRouter(prefix="/api/v1/fenomenologi/gesto_expressivo", tags=["fenomenologia_psicologica"])
router_habito_corporal = APIRouter(prefix="/api/v1/fenomenologi/habito_corporal", tags=["fenomenologia_psicologica"])
router_historicidade = APIRouter(prefix="/api/v1/fenomenologi/historicidade", tags=["fenomenologia_psicologica"])
router_horizonte_externo = APIRouter(prefix="/api/v1/fenomenologi/horizonte_externo", tags=["fenomenologia_psicologica"])
router_horizonte_interno = APIRouter(prefix="/api/v1/fenomenologi/horizonte_interno", tags=["fenomenologia_psicologica"])
router_humor_fenomenologico = APIRouter(prefix="/api/v1/fenomenologi/humor_fenomenologico", tags=["fenomenologia_psicologica"])
router_impressao_originaria = APIRouter(prefix="/api/v1/fenomenologi/impressao_originaria", tags=["fenomenologia_psicologica"])
router_incarnation = APIRouter(prefix="/api/v1/fenomenologi/incarnation", tags=["fenomenologia_psicologica"])
router_intencionalidade = APIRouter(prefix="/api/v1/fenomenologi/intencionalidade", tags=["fenomenologia_psicologica"])
router_intencionalidade_de_ = APIRouter(prefix="/api/v1/fenomenologi/intencionalidade_de_ato", tags=["fenomenologia_psicologica"])
router_intencionalidade_ope = APIRouter(prefix="/api/v1/fenomenologi/intencionalidade_operativ", tags=["fenomenologia_psicologica"])
router_intersubjetividade_f = APIRouter(prefix="/api/v1/fenomenologi/intersubjetividade_fenome", tags=["fenomenologia_psicologica"])
router_invariantes_estrutur = APIRouter(prefix="/api/v1/fenomenologi/invariantes_estruturais", tags=["fenomenologia_psicologica"])
router_memoria_muscular = APIRouter(prefix="/api/v1/fenomenologi/memoria_muscular", tags=["fenomenologia_psicologica"])
router_mimica_fenomenologic = APIRouter(prefix="/api/v1/fenomenologi/mimica_fenomenologica", tags=["fenomenologia_psicologica"])
router_motricidade_intencio = APIRouter(prefix="/api/v1/fenomenologi/motricidade_intencional", tags=["fenomenologia_psicologica"])
router_mundanidade = APIRouter(prefix="/api/v1/fenomenologi/mundanidade", tags=["fenomenologia_psicologica"])
router_mundo_vida_lebenswel = APIRouter(prefix="/api/v1/fenomenologi/mundo_vida_lebenswelt", tags=["fenomenologia_psicologica"])
router_presente_vivo = APIRouter(prefix="/api/v1/fenomenologi/presente_vivo", tags=["fenomenologia_psicologica"])
router_projecao_heidegger = APIRouter(prefix="/api/v1/fenomenologi/projecao_heidegger", tags=["fenomenologia_psicologica"])
router_projecao_introjeto = APIRouter(prefix="/api/v1/fenomenologi/projecao_introjeto", tags=["fenomenologia_psicologica"])
router_protencao_tempo = APIRouter(prefix="/api/v1/fenomenologi/protencao_tempo", tags=["fenomenologia_psicologica"])
router_queda_heidegger = APIRouter(prefix="/api/v1/fenomenologi/queda_heidegger", tags=["fenomenologia_psicologica"])
router_reducao_eidetica = APIRouter(prefix="/api/v1/fenomenologi/reducao_eidetica", tags=["fenomenologia_psicologica"])
router_relacao_vivida = APIRouter(prefix="/api/v1/fenomenologi/relacao_vivida", tags=["fenomenologia_psicologica"])
router_resolucao_antecipado = APIRouter(prefix="/api/v1/fenomenologi/resolucao_antecipadora", tags=["fenomenologia_psicologica"])
router_retencao_tempo = APIRouter(prefix="/api/v1/fenomenologi/retencao_tempo", tags=["fenomenologia_psicologica"])
router_ser_no_mundo = APIRouter(prefix="/api/v1/fenomenologi/ser_no_mundo", tags=["fenomenologia_psicologica"])
router_sintese_ativa = APIRouter(prefix="/api/v1/fenomenologi/sintese_ativa", tags=["fenomenologia_psicologica"])
router_sintese_passiva = APIRouter(prefix="/api/v1/fenomenologi/sintese_passiva", tags=["fenomenologia_psicologica"])
router_soma_fenomenologico = APIRouter(prefix="/api/v1/fenomenologi/soma_fenomenologico", tags=["fenomenologia_psicologica"])
router_tempo_vivido = APIRouter(prefix="/api/v1/fenomenologi/tempo_vivido", tags=["fenomenologia_psicologica"])
router_temporalidade_dasein = APIRouter(prefix="/api/v1/fenomenologi/temporalidade_dasein", tags=["fenomenologia_psicologica"])
router_uneigentlichkeit = APIRouter(prefix="/api/v1/fenomenologi/uneigentlichkeit", tags=["fenomenologia_psicologica"])
router_unidades_significado = APIRouter(prefix="/api/v1/fenomenologi/unidades_significado", tags=["fenomenologia_psicologica"])
router_variacao_imaginativa = APIRouter(prefix="/api/v1/fenomenologi/variacao_imaginativa", tags=["fenomenologia_psicologica"])
router_verdade_aletheia = APIRouter(prefix="/api/v1/fenomenologi/verdade_aletheia", tags=["fenomenologia_psicologica"])
router_vorlaufen = APIRouter(prefix="/api/v1/fenomenologi/vorlaufen", tags=["fenomenologia_psicologica"])

@router_abertura.get("")
async def i_abertura():
    return {"p":"fenomenologia_p_abertura","s":"ativo","t":datetime.utcnow().isoformat()}
@router_afeccao_fenomenologi.get("")
async def i_afeccao_fenomenologi():
    return {"p":"fenomenologia_p_afeccao_fenomenologi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_afeto_fenomenologico.get("")
async def i_afeto_fenomenologico():
    return {"p":"fenomenologia_p_afeto_fenomenologico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ambiguidade_dasein.get("")
async def i_ambiguidade_dasein():
    return {"p":"fenomenologia_p_ambiguidade_dasein","s":"ativo","t":datetime.utcnow().isoformat()}
@router_angst_heidegger.get("")
async def i_angst_heidegger():
    return {"p":"fenomenologia_p_angst_heidegger","s":"ativo","t":datetime.utcnow().isoformat()}
@router_angustia_heidegger.get("")
async def i_angustia_heidegger():
    return {"p":"fenomenologia_p_angustia_heidegger","s":"ativo","t":datetime.utcnow().isoformat()}
@router_associacao_fenomenol.get("")
async def i_associacao_fenomenol():
    return {"p":"fenomenologia_p_associacao_fenomenol","s":"ativo","t":datetime.utcnow().isoformat()}
@router_carncia_ryzanek.get("")
async def i_carncia_ryzanek():
    return {"p":"fenomenologia_p_carncia_ryzanek","s":"ativo","t":datetime.utcnow().isoformat()}
@router_clamor_consciencia.get("")
async def i_clamor_consciencia():
    return {"p":"fenomenologia_p_clamor_consciencia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_consciencia_heidegge.get("")
async def i_consciencia_heidegge():
    return {"p":"fenomenologia_p_consciencia_heidegge","s":"ativo","t":datetime.utcnow().isoformat()}
@router_consciencia_interna.get("")
async def i_consciencia_interna():
    return {"p":"fenomenologia_p_consciencia_interna","s":"ativo","t":datetime.utcnow().isoformat()}
@router_consciencia_temporal.get("")
async def i_consciencia_temporal():
    return {"p":"fenomenologia_p_consciencia_temporal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_constituicao_transce.get("")
async def i_constituicao_transce():
    return {"p":"fenomenologia_p_constituicao_transce","s":"ativo","t":datetime.utcnow().isoformat()}
@router_corpo_objetivo.get("")
async def i_corpo_objetivo():
    return {"p":"fenomenologia_p_corpo_objetivo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_corpo_proprio.get("")
async def i_corpo_proprio():
    return {"p":"fenomenologia_p_corpo_proprio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_corpo_vivido.get("")
async def i_corpo_vivido():
    return {"p":"fenomenologia_p_corpo_vivido","s":"ativo","t":datetime.utcnow().isoformat()}
@router_corporalidade_fenome.get("")
async def i_corporalidade_fenome():
    return {"p":"fenomenologia_p_corporalidade_fenome","s":"ativo","t":datetime.utcnow().isoformat()}
@router_corps_vecu.get("")
async def i_corps_vecu():
    return {"p":"fenomenologia_p_corps_vecu","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cuidado_heidegger.get("")
async def i_cuidado_heidegger():
    return {"p":"fenomenologia_p_cuidado_heidegger","s":"ativo","t":datetime.utcnow().isoformat()}
@router_culpa_heidegger.get("")
async def i_culpa_heidegger():
    return {"p":"fenomenologia_p_culpa_heidegger","s":"ativo","t":datetime.utcnow().isoformat()}
@router_curiosidade_heidegge.get("")
async def i_curiosidade_heidegge():
    return {"p":"fenomenologia_p_curiosidade_heidegge","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dasein.get("")
async def i_dasein():
    return {"p":"fenomenologia_p_dasein","s":"ativo","t":datetime.utcnow().isoformat()}
@router_desocultamento.get("")
async def i_desocultamento():
    return {"p":"fenomenologia_p_desocultamento","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dis_closure.get("")
async def i_dis_closure():
    return {"p":"fenomenologia_p_dis_closure","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ego_transcendental.get("")
async def i_ego_transcendental():
    return {"p":"fenomenologia_p_ego_transcendental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_eigentlichkeit.get("")
async def i_eigentlichkeit():
    return {"p":"fenomenologia_p_eigentlichkeit","s":"ativo","t":datetime.utcnow().isoformat()}
@router_embodiment_fenomenol.get("")
async def i_embodiment_fenomenol():
    return {"p":"fenomenologia_p_embodiment_fenomenol","s":"ativo","t":datetime.utcnow().isoformat()}
@router_empatia_fenomenologi.get("")
async def i_empatia_fenomenologi():
    return {"p":"fenomenologia_p_empatia_fenomenologi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_epoché_fenomenologic.get("")
async def i_epoché_fenomenologic():
    return {"p":"fenomenologia_p_epoché_fenomenologic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_espacialidade_dasein.get("")
async def i_espacialidade_dasein():
    return {"p":"fenomenologia_p_espacialidade_dasein","s":"ativo","t":datetime.utcnow().isoformat()}
@router_espaco_vivido.get("")
async def i_espaco_vivido():
    return {"p":"fenomenologia_p_espaco_vivido","s":"ativo","t":datetime.utcnow().isoformat()}
@router_essencia_fenomenolog.get("")
async def i_essencia_fenomenolog():
    return {"p":"fenomenologia_p_essencia_fenomenolog","s":"ativo","t":datetime.utcnow().isoformat()}
@router_existencial_heidegge.get("")
async def i_existencial_heidegge():
    return {"p":"fenomenologia_p_existencial_heidegge","s":"ativo","t":datetime.utcnow().isoformat()}
@router_existenciario.get("")
async def i_existenciario():
    return {"p":"fenomenologia_p_existenciario","s":"ativo","t":datetime.utcnow().isoformat()}
@router_factidade.get("")
async def i_factidade():
    return {"p":"fenomenologia_p_factidade","s":"ativo","t":datetime.utcnow().isoformat()}
@router_falatório.get("")
async def i_falatório():
    return {"p":"fenomenologia_p_falatório","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fenomenologia_husser.get("")
async def i_fenomenologia_husser():
    return {"p":"fenomenologia_p_fenomenologia_husser","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fluxo_temporal.get("")
async def i_fluxo_temporal():
    return {"p":"fenomenologia_p_fluxo_temporal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gesto_expressivo.get("")
async def i_gesto_expressivo():
    return {"p":"fenomenologia_p_gesto_expressivo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_habito_corporal.get("")
async def i_habito_corporal():
    return {"p":"fenomenologia_p_habito_corporal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_historicidade.get("")
async def i_historicidade():
    return {"p":"fenomenologia_p_historicidade","s":"ativo","t":datetime.utcnow().isoformat()}
@router_horizonte_externo.get("")
async def i_horizonte_externo():
    return {"p":"fenomenologia_p_horizonte_externo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_horizonte_interno.get("")
async def i_horizonte_interno():
    return {"p":"fenomenologia_p_horizonte_interno","s":"ativo","t":datetime.utcnow().isoformat()}
@router_humor_fenomenologico.get("")
async def i_humor_fenomenologico():
    return {"p":"fenomenologia_p_humor_fenomenologico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_impressao_originaria.get("")
async def i_impressao_originaria():
    return {"p":"fenomenologia_p_impressao_originaria","s":"ativo","t":datetime.utcnow().isoformat()}
@router_incarnation.get("")
async def i_incarnation():
    return {"p":"fenomenologia_p_incarnation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_intencionalidade.get("")
async def i_intencionalidade():
    return {"p":"fenomenologia_p_intencionalidade","s":"ativo","t":datetime.utcnow().isoformat()}
@router_intencionalidade_de_.get("")
async def i_intencionalidade_de_():
    return {"p":"fenomenologia_p_intencionalidade_de_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_intencionalidade_ope.get("")
async def i_intencionalidade_ope():
    return {"p":"fenomenologia_p_intencionalidade_ope","s":"ativo","t":datetime.utcnow().isoformat()}
@router_intersubjetividade_f.get("")
async def i_intersubjetividade_f():
    return {"p":"fenomenologia_p_intersubjetividade_f","s":"ativo","t":datetime.utcnow().isoformat()}
@router_invariantes_estrutur.get("")
async def i_invariantes_estrutur():
    return {"p":"fenomenologia_p_invariantes_estrutur","s":"ativo","t":datetime.utcnow().isoformat()}
@router_memoria_muscular.get("")
async def i_memoria_muscular():
    return {"p":"fenomenologia_p_memoria_muscular","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mimica_fenomenologic.get("")
async def i_mimica_fenomenologic():
    return {"p":"fenomenologia_p_mimica_fenomenologic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_motricidade_intencio.get("")
async def i_motricidade_intencio():
    return {"p":"fenomenologia_p_motricidade_intencio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mundanidade.get("")
async def i_mundanidade():
    return {"p":"fenomenologia_p_mundanidade","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mundo_vida_lebenswel.get("")
async def i_mundo_vida_lebenswel():
    return {"p":"fenomenologia_p_mundo_vida_lebenswel","s":"ativo","t":datetime.utcnow().isoformat()}
@router_presente_vivo.get("")
async def i_presente_vivo():
    return {"p":"fenomenologia_p_presente_vivo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_projecao_heidegger.get("")
async def i_projecao_heidegger():
    return {"p":"fenomenologia_p_projecao_heidegger","s":"ativo","t":datetime.utcnow().isoformat()}
@router_projecao_introjeto.get("")
async def i_projecao_introjeto():
    return {"p":"fenomenologia_p_projecao_introjeto","s":"ativo","t":datetime.utcnow().isoformat()}
@router_protencao_tempo.get("")
async def i_protencao_tempo():
    return {"p":"fenomenologia_p_protencao_tempo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_queda_heidegger.get("")
async def i_queda_heidegger():
    return {"p":"fenomenologia_p_queda_heidegger","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reducao_eidetica.get("")
async def i_reducao_eidetica():
    return {"p":"fenomenologia_p_reducao_eidetica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_relacao_vivida.get("")
async def i_relacao_vivida():
    return {"p":"fenomenologia_p_relacao_vivida","s":"ativo","t":datetime.utcnow().isoformat()}
@router_resolucao_antecipado.get("")
async def i_resolucao_antecipado():
    return {"p":"fenomenologia_p_resolucao_antecipado","s":"ativo","t":datetime.utcnow().isoformat()}
@router_retencao_tempo.get("")
async def i_retencao_tempo():
    return {"p":"fenomenologia_p_retencao_tempo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ser_no_mundo.get("")
async def i_ser_no_mundo():
    return {"p":"fenomenologia_p_ser_no_mundo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sintese_ativa.get("")
async def i_sintese_ativa():
    return {"p":"fenomenologia_p_sintese_ativa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sintese_passiva.get("")
async def i_sintese_passiva():
    return {"p":"fenomenologia_p_sintese_passiva","s":"ativo","t":datetime.utcnow().isoformat()}
@router_soma_fenomenologico.get("")
async def i_soma_fenomenologico():
    return {"p":"fenomenologia_p_soma_fenomenologico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tempo_vivido.get("")
async def i_tempo_vivido():
    return {"p":"fenomenologia_p_tempo_vivido","s":"ativo","t":datetime.utcnow().isoformat()}
@router_temporalidade_dasein.get("")
async def i_temporalidade_dasein():
    return {"p":"fenomenologia_p_temporalidade_dasein","s":"ativo","t":datetime.utcnow().isoformat()}
@router_uneigentlichkeit.get("")
async def i_uneigentlichkeit():
    return {"p":"fenomenologia_p_uneigentlichkeit","s":"ativo","t":datetime.utcnow().isoformat()}
@router_unidades_significado.get("")
async def i_unidades_significado():
    return {"p":"fenomenologia_p_unidades_significado","s":"ativo","t":datetime.utcnow().isoformat()}
@router_variacao_imaginativa.get("")
async def i_variacao_imaginativa():
    return {"p":"fenomenologia_p_variacao_imaginativa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_verdade_aletheia.get("")
async def i_verdade_aletheia():
    return {"p":"fenomenologia_p_verdade_aletheia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_vorlaufen.get("")
async def i_vorlaufen():
    return {"p":"fenomenologia_p_vorlaufen","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_fenomenologia_psicol(PluginBase):
    name = "consolidated_fenomenologia_psicologica"
    def setup(self, app):
        app.include_router(router_abertura)
        app.include_router(router_afeccao_fenomenologi)
        app.include_router(router_afeto_fenomenologico)
        app.include_router(router_ambiguidade_dasein)
        app.include_router(router_angst_heidegger)
        app.include_router(router_angustia_heidegger)
        app.include_router(router_associacao_fenomenol)
        app.include_router(router_carncia_ryzanek)
        app.include_router(router_clamor_consciencia)
        app.include_router(router_consciencia_heidegge)
        app.include_router(router_consciencia_interna)
        app.include_router(router_consciencia_temporal)
        app.include_router(router_constituicao_transce)
        app.include_router(router_corpo_objetivo)
        app.include_router(router_corpo_proprio)
        app.include_router(router_corpo_vivido)
        app.include_router(router_corporalidade_fenome)
        app.include_router(router_corps_vecu)
        app.include_router(router_cuidado_heidegger)
        app.include_router(router_culpa_heidegger)
        app.include_router(router_curiosidade_heidegge)
        app.include_router(router_dasein)
        app.include_router(router_desocultamento)
        app.include_router(router_dis_closure)
        app.include_router(router_ego_transcendental)
        app.include_router(router_eigentlichkeit)
        app.include_router(router_embodiment_fenomenol)
        app.include_router(router_empatia_fenomenologi)
        app.include_router(router_epoché_fenomenologic)
        app.include_router(router_espacialidade_dasein)
        app.include_router(router_espaco_vivido)
        app.include_router(router_essencia_fenomenolog)
        app.include_router(router_existencial_heidegge)
        app.include_router(router_existenciario)
        app.include_router(router_factidade)
        app.include_router(router_falatório)
        app.include_router(router_fenomenologia_husser)
        app.include_router(router_fluxo_temporal)
        app.include_router(router_gesto_expressivo)
        app.include_router(router_habito_corporal)
        app.include_router(router_historicidade)
        app.include_router(router_horizonte_externo)
        app.include_router(router_horizonte_interno)
        app.include_router(router_humor_fenomenologico)
        app.include_router(router_impressao_originaria)
        app.include_router(router_incarnation)
        app.include_router(router_intencionalidade)
        app.include_router(router_intencionalidade_de_)
        app.include_router(router_intencionalidade_ope)
        app.include_router(router_intersubjetividade_f)
        app.include_router(router_invariantes_estrutur)
        app.include_router(router_memoria_muscular)
        app.include_router(router_mimica_fenomenologic)
        app.include_router(router_motricidade_intencio)
        app.include_router(router_mundanidade)
        app.include_router(router_mundo_vida_lebenswel)
        app.include_router(router_presente_vivo)
        app.include_router(router_projecao_heidegger)
        app.include_router(router_projecao_introjeto)
        app.include_router(router_protencao_tempo)
        app.include_router(router_queda_heidegger)
        app.include_router(router_reducao_eidetica)
        app.include_router(router_relacao_vivida)
        app.include_router(router_resolucao_antecipado)
        app.include_router(router_retencao_tempo)
        app.include_router(router_ser_no_mundo)
        app.include_router(router_sintese_ativa)
        app.include_router(router_sintese_passiva)
        app.include_router(router_soma_fenomenologico)
        app.include_router(router_tempo_vivido)
        app.include_router(router_temporalidade_dasein)
        app.include_router(router_uneigentlichkeit)
        app.include_router(router_unidades_significado)
        app.include_router(router_variacao_imaginativa)
        app.include_router(router_verdade_aletheia)
        app.include_router(router_vorlaufen)


plugin = Plugin_fenomenologia_psicol()
