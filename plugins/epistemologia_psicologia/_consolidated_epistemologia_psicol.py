from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_abduction = APIRouter(prefix="/api/v1/epistemologi/abduction", tags=["epistemologia_psicologia"])
router_abdutivismo = APIRouter(prefix="/api/v1/epistemologi/abdutivismo", tags=["epistemologia_psicologia"])
router_anomalia = APIRouter(prefix="/api/v1/epistemologi/anomalia", tags=["epistemologia_psicologia"])
router_anything_goes = APIRouter(prefix="/api/v1/epistemologi/anything_goes", tags=["epistemologia_psicologia"])
router_carneap_probabilidad = APIRouter(prefix="/api/v1/epistemologi/carneap_probabilidade", tags=["epistemologia_psicologia"])
router_ciencia_normal = APIRouter(prefix="/api/v1/epistemologi/ciencia_normal", tags=["epistemologia_psicologia"])
router_cinto_protetor = APIRouter(prefix="/api/v1/epistemologi/cinto_protetor", tags=["epistemologia_psicologia"])
router_construtivismo_epist = APIRouter(prefix="/api/v1/epistemologi/construtivismo_epistemico", tags=["epistemologia_psicologia"])
router_conteudo_empirico = APIRouter(prefix="/api/v1/epistemologi/conteudo_empirico", tags=["epistemologia_psicologia"])
router_controle_cientifico = APIRouter(prefix="/api/v1/epistemologi/controle_cientifico", tags=["epistemologia_psicologia"])
router_counterinduction = APIRouter(prefix="/api/v1/epistemologi/counterinduction", tags=["epistemologia_psicologia"])
router_crise_paradigmatica = APIRouter(prefix="/api/v1/epistemologi/crise_paradigmatica", tags=["epistemologia_psicologia"])
router_dedutivismo = APIRouter(prefix="/api/v1/epistemologi/dedutivismo", tags=["epistemologia_psicologia"])
router_demarcacao_ciencia = APIRouter(prefix="/api/v1/epistemologi/demarcacao_ciencia", tags=["epistemologia_psicologia"])
router_determinismo_linguis = APIRouter(prefix="/api/v1/epistemologi/determinismo_linguistico", tags=["epistemologia_psicologia"])
router_epistemologia_cienci = APIRouter(prefix="/api/v1/epistemologi/epistemologia_ciencia", tags=["epistemologia_psicologia"])
router_euristica_negativa = APIRouter(prefix="/api/v1/epistemologi/euristica_negativa", tags=["epistemologia_psicologia"])
router_euristica_positiva = APIRouter(prefix="/api/v1/epistemologi/euristica_positiva", tags=["epistemologia_psicologia"])
router_evidence_relation = APIRouter(prefix="/api/v1/epistemologi/evidence_relation", tags=["epistemologia_psicologia"])
router_experimento_ideal = APIRouter(prefix="/api/v1/epistemologi/experimento_ideal", tags=["epistemologia_psicologia"])
router_explicacao_cientific = APIRouter(prefix="/api/v1/epistemologi/explicacao_cientifica", tags=["epistemologia_psicologia"])
router_falsificacionismo = APIRouter(prefix="/api/v1/epistemologi/falsificacionismo", tags=["epistemologia_psicologia"])
router_feyerabend_anarquism = APIRouter(prefix="/api/v1/epistemologi/feyerabend_anarquismo", tags=["epistemologia_psicologia"])
router_filosofia_ciencia = APIRouter(prefix="/api/v1/epistemologi/filosofia_ciencia", tags=["epistemologia_psicologia"])
router_grau_corroboracao = APIRouter(prefix="/api/v1/epistemologi/grau_corroboracao", tags=["epistemologia_psicologia"])
router_hipotese_sapir_whorf = APIRouter(prefix="/api/v1/epistemologi/hipotese_sapir_whorf", tags=["epistemologia_psicologia"])
router_hipotetico_dedutivo = APIRouter(prefix="/api/v1/epistemologi/hipotetico_dedutivo", tags=["epistemologia_psicologia"])
router_historicismo = APIRouter(prefix="/api/v1/epistemologi/historicismo", tags=["epistemologia_psicologia"])
router_horizonte_empirico = APIRouter(prefix="/api/v1/epistemologi/horizonte_empirico", tags=["epistemologia_psicologia"])
router_iconicidade = APIRouter(prefix="/api/v1/epistemologi/iconicidade", tags=["epistemologia_psicologia"])
router_incomensurabilidade = APIRouter(prefix="/api/v1/epistemologi/incomensurabilidade", tags=["epistemologia_psicologia"])
router_indexicalidade = APIRouter(prefix="/api/v1/epistemologi/indexicalidade", tags=["epistemologia_psicologia"])
router_inductive_logic = APIRouter(prefix="/api/v1/epistemologi/inductive_logic", tags=["epistemologia_psicologia"])
router_indutivismo = APIRouter(prefix="/api/v1/epistemologi/indutivismo", tags=["epistemologia_psicologia"])
router_inference_best = APIRouter(prefix="/api/v1/epistemologi/inference_best", tags=["epistemologia_psicologia"])
router_instrumentalismo = APIRouter(prefix="/api/v1/epistemologi/instrumentalismo", tags=["epistemologia_psicologia"])
router_interpretante = APIRouter(prefix="/api/v1/epistemologi/interpretante", tags=["epistemologia_psicologia"])
router_kuhn_paradigma = APIRouter(prefix="/api/v1/epistemologi/kuhn_paradigma", tags=["epistemologia_psicologia"])
router_lakatos_programa = APIRouter(prefix="/api/v1/epistemologi/lakatos_programa", tags=["epistemologia_psicologia"])
router_linguagem_mente = APIRouter(prefix="/api/v1/epistemologi/linguagem_mente", tags=["epistemologia_psicologia"])
router_linguagem_pensamento = APIRouter(prefix="/api/v1/epistemologi/linguagem_pensamento", tags=["epistemologia_psicologia"])
router_linguagem_sem_pensam = APIRouter(prefix="/api/v1/epistemologi/linguagem_sem_pensamento", tags=["epistemologia_psicologia"])
router_logica_indutiva = APIRouter(prefix="/api/v1/epistemologi/logica_indutiva", tags=["epistemologia_psicologia"])
router_mentalese = APIRouter(prefix="/api/v1/epistemologi/mentalese", tags=["epistemologia_psicologia"])
router_modus_tollens = APIRouter(prefix="/api/v1/epistemologi/modus_tollens", tags=["epistemologia_psicologia"])
router_nucleo_duro = APIRouter(prefix="/api/v1/epistemologi/nucleo_duro", tags=["epistemologia_psicologia"])
router_peirce_semiotica = APIRouter(prefix="/api/v1/epistemologi/peirce_semiotica", tags=["epistemologia_psicologia"])
router_pensamento_abstrato = APIRouter(prefix="/api/v1/epistemologi/pensamento_abstrato", tags=["epistemologia_psicologia"])
router_pensamento_analitico = APIRouter(prefix="/api/v1/epistemologi/pensamento_analitico", tags=["epistemologia_psicologia"])
router_pensamento_concreto = APIRouter(prefix="/api/v1/epistemologi/pensamento_concreto", tags=["epistemologia_psicologia"])
router_pensamento_formal2 = APIRouter(prefix="/api/v1/epistemologi/pensamento_formal2", tags=["epistemologia_psicologia"])
router_pensamento_informal = APIRouter(prefix="/api/v1/epistemologi/pensamento_informal", tags=["epistemologia_psicologia"])
router_pensamento_sem_lingu = APIRouter(prefix="/api/v1/epistemologi/pensamento_sem_linguagem", tags=["epistemologia_psicologia"])
router_pensamento_sintetico = APIRouter(prefix="/api/v1/epistemologi/pensamento_sintetico", tags=["epistemologia_psicologia"])
router_popper_falsificabili = APIRouter(prefix="/api/v1/epistemologi/popper_falsificabilidade", tags=["epistemologia_psicologia"])
router_previsao_cientifica = APIRouter(prefix="/api/v1/epistemologi/previsao_cientifica", tags=["epistemologia_psicologia"])
router_probabilidade_bayesi = APIRouter(prefix="/api/v1/epistemologi/probabilidade_bayesiana", tags=["epistemologia_psicologia"])
router_probabilidade_freque = APIRouter(prefix="/api/v1/epistemologi/probabilidade_frequentist", tags=["epistemologia_psicologia"])
router_probabilidade_objeti = APIRouter(prefix="/api/v1/epistemologi/probabilidade_objetiva", tags=["epistemologia_psicologia"])
router_probabilidade_subjet = APIRouter(prefix="/api/v1/epistemologi/probabilidade_subjetiva", tags=["epistemologia_psicologia"])
router_proliferation_theori = APIRouter(prefix="/api/v1/epistemologi/proliferation_theories", tags=["epistemologia_psicologia"])
router_realismo_cientifico = APIRouter(prefix="/api/v1/epistemologi/realismo_cientifico", tags=["epistemologia_psicologia"])
router_relatividade_linguis = APIRouter(prefix="/api/v1/epistemologi/relatividade_linguistica", tags=["epistemologia_psicologia"])
router_relativismo_epistemi = APIRouter(prefix="/api/v1/epistemologi/relativismo_epistemico", tags=["epistemologia_psicologia"])
router_retroducao = APIRouter(prefix="/api/v1/epistemologi/retroducao", tags=["epistemologia_psicologia"])
router_revolucao_cientifica = APIRouter(prefix="/api/v1/epistemologi/revolucao_cientifica", tags=["epistemologia_psicologia"])
router_semiotica_psicologia = APIRouter(prefix="/api/v1/epistemologi/semiotica_psicologia", tags=["epistemologia_psicologia"])
router_signo_objeto = APIRouter(prefix="/api/v1/epistemologi/signo_objeto", tags=["epistemologia_psicologia"])
router_simbolicidade = APIRouter(prefix="/api/v1/epistemologi/simbolicidade", tags=["epistemologia_psicologia"])
router_tenacity = APIRouter(prefix="/api/v1/epistemologi/tenacity", tags=["epistemologia_psicologia"])
router_universalidade_lingu = APIRouter(prefix="/api/v1/epistemologi/universalidade_linguistic", tags=["epistemologia_psicologia"])
router_verificacionismo = APIRouter(prefix="/api/v1/epistemologi/verificacionismo", tags=["epistemologia_psicologia"])

@router_abduction.get("")
async def i_abduction():
    return {"p":"epistemologia_p_abduction","s":"ativo","t":datetime.utcnow().isoformat()}
@router_abdutivismo.get("")
async def i_abdutivismo():
    return {"p":"epistemologia_p_abdutivismo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_anomalia.get("")
async def i_anomalia():
    return {"p":"epistemologia_p_anomalia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_anything_goes.get("")
async def i_anything_goes():
    return {"p":"epistemologia_p_anything_goes","s":"ativo","t":datetime.utcnow().isoformat()}
@router_carneap_probabilidad.get("")
async def i_carneap_probabilidad():
    return {"p":"epistemologia_p_carneap_probabilidad","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ciencia_normal.get("")
async def i_ciencia_normal():
    return {"p":"epistemologia_p_ciencia_normal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cinto_protetor.get("")
async def i_cinto_protetor():
    return {"p":"epistemologia_p_cinto_protetor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_construtivismo_epist.get("")
async def i_construtivismo_epist():
    return {"p":"epistemologia_p_construtivismo_epist","s":"ativo","t":datetime.utcnow().isoformat()}
@router_conteudo_empirico.get("")
async def i_conteudo_empirico():
    return {"p":"epistemologia_p_conteudo_empirico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_controle_cientifico.get("")
async def i_controle_cientifico():
    return {"p":"epistemologia_p_controle_cientifico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_counterinduction.get("")
async def i_counterinduction():
    return {"p":"epistemologia_p_counterinduction","s":"ativo","t":datetime.utcnow().isoformat()}
@router_crise_paradigmatica.get("")
async def i_crise_paradigmatica():
    return {"p":"epistemologia_p_crise_paradigmatica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dedutivismo.get("")
async def i_dedutivismo():
    return {"p":"epistemologia_p_dedutivismo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_demarcacao_ciencia.get("")
async def i_demarcacao_ciencia():
    return {"p":"epistemologia_p_demarcacao_ciencia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_determinismo_linguis.get("")
async def i_determinismo_linguis():
    return {"p":"epistemologia_p_determinismo_linguis","s":"ativo","t":datetime.utcnow().isoformat()}
@router_epistemologia_cienci.get("")
async def i_epistemologia_cienci():
    return {"p":"epistemologia_p_epistemologia_cienci","s":"ativo","t":datetime.utcnow().isoformat()}
@router_euristica_negativa.get("")
async def i_euristica_negativa():
    return {"p":"epistemologia_p_euristica_negativa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_euristica_positiva.get("")
async def i_euristica_positiva():
    return {"p":"epistemologia_p_euristica_positiva","s":"ativo","t":datetime.utcnow().isoformat()}
@router_evidence_relation.get("")
async def i_evidence_relation():
    return {"p":"epistemologia_p_evidence_relation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_experimento_ideal.get("")
async def i_experimento_ideal():
    return {"p":"epistemologia_p_experimento_ideal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_explicacao_cientific.get("")
async def i_explicacao_cientific():
    return {"p":"epistemologia_p_explicacao_cientific","s":"ativo","t":datetime.utcnow().isoformat()}
@router_falsificacionismo.get("")
async def i_falsificacionismo():
    return {"p":"epistemologia_p_falsificacionismo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_feyerabend_anarquism.get("")
async def i_feyerabend_anarquism():
    return {"p":"epistemologia_p_feyerabend_anarquism","s":"ativo","t":datetime.utcnow().isoformat()}
@router_filosofia_ciencia.get("")
async def i_filosofia_ciencia():
    return {"p":"epistemologia_p_filosofia_ciencia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grau_corroboracao.get("")
async def i_grau_corroboracao():
    return {"p":"epistemologia_p_grau_corroboracao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hipotese_sapir_whorf.get("")
async def i_hipotese_sapir_whorf():
    return {"p":"epistemologia_p_hipotese_sapir_whorf","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hipotetico_dedutivo.get("")
async def i_hipotetico_dedutivo():
    return {"p":"epistemologia_p_hipotetico_dedutivo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_historicismo.get("")
async def i_historicismo():
    return {"p":"epistemologia_p_historicismo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_horizonte_empirico.get("")
async def i_horizonte_empirico():
    return {"p":"epistemologia_p_horizonte_empirico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_iconicidade.get("")
async def i_iconicidade():
    return {"p":"epistemologia_p_iconicidade","s":"ativo","t":datetime.utcnow().isoformat()}
@router_incomensurabilidade.get("")
async def i_incomensurabilidade():
    return {"p":"epistemologia_p_incomensurabilidade","s":"ativo","t":datetime.utcnow().isoformat()}
@router_indexicalidade.get("")
async def i_indexicalidade():
    return {"p":"epistemologia_p_indexicalidade","s":"ativo","t":datetime.utcnow().isoformat()}
@router_inductive_logic.get("")
async def i_inductive_logic():
    return {"p":"epistemologia_p_inductive_logic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_indutivismo.get("")
async def i_indutivismo():
    return {"p":"epistemologia_p_indutivismo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_inference_best.get("")
async def i_inference_best():
    return {"p":"epistemologia_p_inference_best","s":"ativo","t":datetime.utcnow().isoformat()}
@router_instrumentalismo.get("")
async def i_instrumentalismo():
    return {"p":"epistemologia_p_instrumentalismo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_interpretante.get("")
async def i_interpretante():
    return {"p":"epistemologia_p_interpretante","s":"ativo","t":datetime.utcnow().isoformat()}
@router_kuhn_paradigma.get("")
async def i_kuhn_paradigma():
    return {"p":"epistemologia_p_kuhn_paradigma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lakatos_programa.get("")
async def i_lakatos_programa():
    return {"p":"epistemologia_p_lakatos_programa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_linguagem_mente.get("")
async def i_linguagem_mente():
    return {"p":"epistemologia_p_linguagem_mente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_linguagem_pensamento.get("")
async def i_linguagem_pensamento():
    return {"p":"epistemologia_p_linguagem_pensamento","s":"ativo","t":datetime.utcnow().isoformat()}
@router_linguagem_sem_pensam.get("")
async def i_linguagem_sem_pensam():
    return {"p":"epistemologia_p_linguagem_sem_pensam","s":"ativo","t":datetime.utcnow().isoformat()}
@router_logica_indutiva.get("")
async def i_logica_indutiva():
    return {"p":"epistemologia_p_logica_indutiva","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mentalese.get("")
async def i_mentalese():
    return {"p":"epistemologia_p_mentalese","s":"ativo","t":datetime.utcnow().isoformat()}
@router_modus_tollens.get("")
async def i_modus_tollens():
    return {"p":"epistemologia_p_modus_tollens","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nucleo_duro.get("")
async def i_nucleo_duro():
    return {"p":"epistemologia_p_nucleo_duro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_peirce_semiotica.get("")
async def i_peirce_semiotica():
    return {"p":"epistemologia_p_peirce_semiotica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pensamento_abstrato.get("")
async def i_pensamento_abstrato():
    return {"p":"epistemologia_p_pensamento_abstrato","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pensamento_analitico.get("")
async def i_pensamento_analitico():
    return {"p":"epistemologia_p_pensamento_analitico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pensamento_concreto.get("")
async def i_pensamento_concreto():
    return {"p":"epistemologia_p_pensamento_concreto","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pensamento_formal2.get("")
async def i_pensamento_formal2():
    return {"p":"epistemologia_p_pensamento_formal2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pensamento_informal.get("")
async def i_pensamento_informal():
    return {"p":"epistemologia_p_pensamento_informal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pensamento_sem_lingu.get("")
async def i_pensamento_sem_lingu():
    return {"p":"epistemologia_p_pensamento_sem_lingu","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pensamento_sintetico.get("")
async def i_pensamento_sintetico():
    return {"p":"epistemologia_p_pensamento_sintetico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_popper_falsificabili.get("")
async def i_popper_falsificabili():
    return {"p":"epistemologia_p_popper_falsificabili","s":"ativo","t":datetime.utcnow().isoformat()}
@router_previsao_cientifica.get("")
async def i_previsao_cientifica():
    return {"p":"epistemologia_p_previsao_cientifica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_probabilidade_bayesi.get("")
async def i_probabilidade_bayesi():
    return {"p":"epistemologia_p_probabilidade_bayesi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_probabilidade_freque.get("")
async def i_probabilidade_freque():
    return {"p":"epistemologia_p_probabilidade_freque","s":"ativo","t":datetime.utcnow().isoformat()}
@router_probabilidade_objeti.get("")
async def i_probabilidade_objeti():
    return {"p":"epistemologia_p_probabilidade_objeti","s":"ativo","t":datetime.utcnow().isoformat()}
@router_probabilidade_subjet.get("")
async def i_probabilidade_subjet():
    return {"p":"epistemologia_p_probabilidade_subjet","s":"ativo","t":datetime.utcnow().isoformat()}
@router_proliferation_theori.get("")
async def i_proliferation_theori():
    return {"p":"epistemologia_p_proliferation_theori","s":"ativo","t":datetime.utcnow().isoformat()}
@router_realismo_cientifico.get("")
async def i_realismo_cientifico():
    return {"p":"epistemologia_p_realismo_cientifico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_relatividade_linguis.get("")
async def i_relatividade_linguis():
    return {"p":"epistemologia_p_relatividade_linguis","s":"ativo","t":datetime.utcnow().isoformat()}
@router_relativismo_epistemi.get("")
async def i_relativismo_epistemi():
    return {"p":"epistemologia_p_relativismo_epistemi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_retroducao.get("")
async def i_retroducao():
    return {"p":"epistemologia_p_retroducao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_revolucao_cientifica.get("")
async def i_revolucao_cientifica():
    return {"p":"epistemologia_p_revolucao_cientifica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_semiotica_psicologia.get("")
async def i_semiotica_psicologia():
    return {"p":"epistemologia_p_semiotica_psicologia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_signo_objeto.get("")
async def i_signo_objeto():
    return {"p":"epistemologia_p_signo_objeto","s":"ativo","t":datetime.utcnow().isoformat()}
@router_simbolicidade.get("")
async def i_simbolicidade():
    return {"p":"epistemologia_p_simbolicidade","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tenacity.get("")
async def i_tenacity():
    return {"p":"epistemologia_p_tenacity","s":"ativo","t":datetime.utcnow().isoformat()}
@router_universalidade_lingu.get("")
async def i_universalidade_lingu():
    return {"p":"epistemologia_p_universalidade_lingu","s":"ativo","t":datetime.utcnow().isoformat()}
@router_verificacionismo.get("")
async def i_verificacionismo():
    return {"p":"epistemologia_p_verificacionismo","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_epistemologia_psicol(PluginBase):
    name = "consolidated_epistemologia_psicologia"
    def setup(self, app):
        app.include_router(router_abduction)
        app.include_router(router_abdutivismo)
        app.include_router(router_anomalia)
        app.include_router(router_anything_goes)
        app.include_router(router_carneap_probabilidad)
        app.include_router(router_ciencia_normal)
        app.include_router(router_cinto_protetor)
        app.include_router(router_construtivismo_epist)
        app.include_router(router_conteudo_empirico)
        app.include_router(router_controle_cientifico)
        app.include_router(router_counterinduction)
        app.include_router(router_crise_paradigmatica)
        app.include_router(router_dedutivismo)
        app.include_router(router_demarcacao_ciencia)
        app.include_router(router_determinismo_linguis)
        app.include_router(router_epistemologia_cienci)
        app.include_router(router_euristica_negativa)
        app.include_router(router_euristica_positiva)
        app.include_router(router_evidence_relation)
        app.include_router(router_experimento_ideal)
        app.include_router(router_explicacao_cientific)
        app.include_router(router_falsificacionismo)
        app.include_router(router_feyerabend_anarquism)
        app.include_router(router_filosofia_ciencia)
        app.include_router(router_grau_corroboracao)
        app.include_router(router_hipotese_sapir_whorf)
        app.include_router(router_hipotetico_dedutivo)
        app.include_router(router_historicismo)
        app.include_router(router_horizonte_empirico)
        app.include_router(router_iconicidade)
        app.include_router(router_incomensurabilidade)
        app.include_router(router_indexicalidade)
        app.include_router(router_inductive_logic)
        app.include_router(router_indutivismo)
        app.include_router(router_inference_best)
        app.include_router(router_instrumentalismo)
        app.include_router(router_interpretante)
        app.include_router(router_kuhn_paradigma)
        app.include_router(router_lakatos_programa)
        app.include_router(router_linguagem_mente)
        app.include_router(router_linguagem_pensamento)
        app.include_router(router_linguagem_sem_pensam)
        app.include_router(router_logica_indutiva)
        app.include_router(router_mentalese)
        app.include_router(router_modus_tollens)
        app.include_router(router_nucleo_duro)
        app.include_router(router_peirce_semiotica)
        app.include_router(router_pensamento_abstrato)
        app.include_router(router_pensamento_analitico)
        app.include_router(router_pensamento_concreto)
        app.include_router(router_pensamento_formal2)
        app.include_router(router_pensamento_informal)
        app.include_router(router_pensamento_sem_lingu)
        app.include_router(router_pensamento_sintetico)
        app.include_router(router_popper_falsificabili)
        app.include_router(router_previsao_cientifica)
        app.include_router(router_probabilidade_bayesi)
        app.include_router(router_probabilidade_freque)
        app.include_router(router_probabilidade_objeti)
        app.include_router(router_probabilidade_subjet)
        app.include_router(router_proliferation_theori)
        app.include_router(router_realismo_cientifico)
        app.include_router(router_relatividade_linguis)
        app.include_router(router_relativismo_epistemi)
        app.include_router(router_retroducao)
        app.include_router(router_revolucao_cientifica)
        app.include_router(router_semiotica_psicologia)
        app.include_router(router_signo_objeto)
        app.include_router(router_simbolicidade)
        app.include_router(router_tenacity)
        app.include_router(router_universalidade_lingu)
        app.include_router(router_verificacionismo)


plugin = Plugin_epistemologia_psicol()
