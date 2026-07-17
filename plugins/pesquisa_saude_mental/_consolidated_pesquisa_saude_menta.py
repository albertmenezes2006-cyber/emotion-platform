from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_analise_conteudo = APIRouter(prefix="/api/v1/pesquisa_sau/analise_conteudo", tags=["pesquisa_saude_mental"])
router_analise_discurso = APIRouter(prefix="/api/v1/pesquisa_sau/analise_discurso", tags=["pesquisa_saude_mental"])
router_analise_narrativa_pe = APIRouter(prefix="/api/v1/pesquisa_sau/analise_narrativa_pesquis", tags=["pesquisa_saude_mental"])
router_analise_sentimento2 = APIRouter(prefix="/api/v1/pesquisa_sau/analise_sentimento2", tags=["pesquisa_saude_mental"])
router_autoetnografia = APIRouter(prefix="/api/v1/pesquisa_sau/autoetnografia", tags=["pesquisa_saude_mental"])
router_bayesiano_psicologia = APIRouter(prefix="/api/v1/pesquisa_sau/bayesiano_psicologia", tags=["pesquisa_saude_mental"])
router_big_data_mental = APIRouter(prefix="/api/v1/pesquisa_sau/big_data_mental", tags=["pesquisa_saude_mental"])
router_cid12_futuro = APIRouter(prefix="/api/v1/pesquisa_sau/cid12_futuro", tags=["pesquisa_saude_mental"])
router_ciencia_cidada = APIRouter(prefix="/api/v1/pesquisa_sau/ciencia_cidada", tags=["pesquisa_saude_mental"])
router_citizen_science_ment = APIRouter(prefix="/api/v1/pesquisa_sau/citizen_science_mental", tags=["pesquisa_saude_mental"])
router_classificacao_mental = APIRouter(prefix="/api/v1/pesquisa_sau/classificacao_mental", tags=["pesquisa_saude_mental"])
router_co_producao_conhecim = APIRouter(prefix="/api/v1/pesquisa_sau/co_producao_conhecimento", tags=["pesquisa_saude_mental"])
router_continuum_mental = APIRouter(prefix="/api/v1/pesquisa_sau/continuum_mental", tags=["pesquisa_saude_mental"])
router_course_outcome = APIRouter(prefix="/api/v1/pesquisa_sau/course_outcome", tags=["pesquisa_saude_mental"])
router_crise_replicacao = APIRouter(prefix="/api/v1/pesquisa_sau/crise_replicacao", tags=["pesquisa_saude_mental"])
router_deep_learning_psi = APIRouter(prefix="/api/v1/pesquisa_sau/deep_learning_psi", tags=["pesquisa_saude_mental"])
router_dimensoes_psicopatol = APIRouter(prefix="/api/v1/pesquisa_sau/dimensoes_psicopatologia", tags=["pesquisa_saude_mental"])
router_dsm6_futuro = APIRouter(prefix="/api/v1/pesquisa_sau/dsm6_futuro", tags=["pesquisa_saude_mental"])
router_espectros_mentais = APIRouter(prefix="/api/v1/pesquisa_sau/espectros_mentais", tags=["pesquisa_saude_mental"])
router_etnografia_mental = APIRouter(prefix="/api/v1/pesquisa_sau/etnografia_mental", tags=["pesquisa_saude_mental"])
router_fenomenologia_psi = APIRouter(prefix="/api/v1/pesquisa_sau/fenomenologia_psi", tags=["pesquisa_saude_mental"])
router_frequentista_psi = APIRouter(prefix="/api/v1/pesquisa_sau/frequentista_psi", tags=["pesquisa_saude_mental"])
router_grounded_theory = APIRouter(prefix="/api/v1/pesquisa_sau/grounded_theory", tags=["pesquisa_saude_mental"])
router_hermeneutica_psi = APIRouter(prefix="/api/v1/pesquisa_sau/hermeneutica_psi", tags=["pesquisa_saude_mental"])
router_hierarquia_mental = APIRouter(prefix="/api/v1/pesquisa_sau/hierarquia_mental", tags=["pesquisa_saude_mental"])
router_hipercorrecao = APIRouter(prefix="/api/v1/pesquisa_sau/hipercorrecao", tags=["pesquisa_saude_mental"])
router_ipa_analise = APIRouter(prefix="/api/v1/pesquisa_sau/ipa_analise", tags=["pesquisa_saude_mental"])
router_linked_data_mental = APIRouter(prefix="/api/v1/pesquisa_sau/linked_data_mental", tags=["pesquisa_saude_mental"])
router_machine_learning_psi = APIRouter(prefix="/api/v1/pesquisa_sau/machine_learning_psi", tags=["pesquisa_saude_mental"])
router_metodologia_qualitat = APIRouter(prefix="/api/v1/pesquisa_sau/metodologia_qualitativa_p", tags=["pesquisa_saude_mental"])
router_metodologia_quantita = APIRouter(prefix="/api/v1/pesquisa_sau/metodologia_quantitativa_", tags=["pesquisa_saude_mental"])
router_metodos_mistos_psi = APIRouter(prefix="/api/v1/pesquisa_sau/metodos_mistos_psi", tags=["pesquisa_saude_mental"])
router_ontologia_mental = APIRouter(prefix="/api/v1/pesquisa_sau/ontologia_mental", tags=["pesquisa_saude_mental"])
router_open_science2 = APIRouter(prefix="/api/v1/pesquisa_sau/open_science2", tags=["pesquisa_saude_mental"])
router_p_hacking = APIRouter(prefix="/api/v1/pesquisa_sau/p_hacking", tags=["pesquisa_saude_mental"])
router_pesquisa_acao = APIRouter(prefix="/api/v1/pesquisa_sau/pesquisa_acao", tags=["pesquisa_saude_mental"])
router_pesquisa_colaborativ = APIRouter(prefix="/api/v1/pesquisa_sau/pesquisa_colaborativa", tags=["pesquisa_saude_mental"])
router_pesquisa_participati = APIRouter(prefix="/api/v1/pesquisa_sau/pesquisa_participativa", tags=["pesquisa_saude_mental"])
router_poder_estatistico2 = APIRouter(prefix="/api/v1/pesquisa_sau/poder_estatistico2", tags=["pesquisa_saude_mental"])
router_preregistro_pesquisa = APIRouter(prefix="/api/v1/pesquisa_sau/preregistro_pesquisa", tags=["pesquisa_saude_mental"])
router_processamento_texto_ = APIRouter(prefix="/api/v1/pesquisa_sau/processamento_texto_psi", tags=["pesquisa_saude_mental"])
router_rdoc_criterios = APIRouter(prefix="/api/v1/pesquisa_sau/rdoc_criterios", tags=["pesquisa_saude_mental"])
router_rede_semantica = APIRouter(prefix="/api/v1/pesquisa_sau/rede_semantica", tags=["pesquisa_saude_mental"])
router_registered_reports2 = APIRouter(prefix="/api/v1/pesquisa_sau/registered_reports2", tags=["pesquisa_saude_mental"])
router_replicabilidade_psi = APIRouter(prefix="/api/v1/pesquisa_sau/replicabilidade_psi", tags=["pesquisa_saude_mental"])
router_sentiment_psi = APIRouter(prefix="/api/v1/pesquisa_sau/sentiment_psi", tags=["pesquisa_saude_mental"])
router_staging_mental = APIRouter(prefix="/api/v1/pesquisa_sau/staging_mental", tags=["pesquisa_saude_mental"])
router_tamanho_efeito2 = APIRouter(prefix="/api/v1/pesquisa_sau/tamanho_efeito2", tags=["pesquisa_saude_mental"])
router_taxonomia_mental = APIRouter(prefix="/api/v1/pesquisa_sau/taxonomia_mental", tags=["pesquisa_saude_mental"])
router_text_mining_psi = APIRouter(prefix="/api/v1/pesquisa_sau/text_mining_psi", tags=["pesquisa_saude_mental"])
router_topic_modeling = APIRouter(prefix="/api/v1/pesquisa_sau/topic_modeling", tags=["pesquisa_saude_mental"])
router_trajetoria_mental = APIRouter(prefix="/api/v1/pesquisa_sau/trajetoria_mental", tags=["pesquisa_saude_mental"])
router_transdiag2 = APIRouter(prefix="/api/v1/pesquisa_sau/transdiag2", tags=["pesquisa_saude_mental"])

@router_analise_conteudo.get("")
async def i_analise_conteudo():
    return {"p":"pesquisa_saude__analise_conteudo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_analise_discurso.get("")
async def i_analise_discurso():
    return {"p":"pesquisa_saude__analise_discurso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_analise_narrativa_pe.get("")
async def i_analise_narrativa_pe():
    return {"p":"pesquisa_saude__analise_narrativa_pe","s":"ativo","t":datetime.utcnow().isoformat()}
@router_analise_sentimento2.get("")
async def i_analise_sentimento2():
    return {"p":"pesquisa_saude__analise_sentimento2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autoetnografia.get("")
async def i_autoetnografia():
    return {"p":"pesquisa_saude__autoetnografia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bayesiano_psicologia.get("")
async def i_bayesiano_psicologia():
    return {"p":"pesquisa_saude__bayesiano_psicologia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_big_data_mental.get("")
async def i_big_data_mental():
    return {"p":"pesquisa_saude__big_data_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cid12_futuro.get("")
async def i_cid12_futuro():
    return {"p":"pesquisa_saude__cid12_futuro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ciencia_cidada.get("")
async def i_ciencia_cidada():
    return {"p":"pesquisa_saude__ciencia_cidada","s":"ativo","t":datetime.utcnow().isoformat()}
@router_citizen_science_ment.get("")
async def i_citizen_science_ment():
    return {"p":"pesquisa_saude__citizen_science_ment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_classificacao_mental.get("")
async def i_classificacao_mental():
    return {"p":"pesquisa_saude__classificacao_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_co_producao_conhecim.get("")
async def i_co_producao_conhecim():
    return {"p":"pesquisa_saude__co_producao_conhecim","s":"ativo","t":datetime.utcnow().isoformat()}
@router_continuum_mental.get("")
async def i_continuum_mental():
    return {"p":"pesquisa_saude__continuum_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_course_outcome.get("")
async def i_course_outcome():
    return {"p":"pesquisa_saude__course_outcome","s":"ativo","t":datetime.utcnow().isoformat()}
@router_crise_replicacao.get("")
async def i_crise_replicacao():
    return {"p":"pesquisa_saude__crise_replicacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_deep_learning_psi.get("")
async def i_deep_learning_psi():
    return {"p":"pesquisa_saude__deep_learning_psi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dimensoes_psicopatol.get("")
async def i_dimensoes_psicopatol():
    return {"p":"pesquisa_saude__dimensoes_psicopatol","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dsm6_futuro.get("")
async def i_dsm6_futuro():
    return {"p":"pesquisa_saude__dsm6_futuro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_espectros_mentais.get("")
async def i_espectros_mentais():
    return {"p":"pesquisa_saude__espectros_mentais","s":"ativo","t":datetime.utcnow().isoformat()}
@router_etnografia_mental.get("")
async def i_etnografia_mental():
    return {"p":"pesquisa_saude__etnografia_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fenomenologia_psi.get("")
async def i_fenomenologia_psi():
    return {"p":"pesquisa_saude__fenomenologia_psi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_frequentista_psi.get("")
async def i_frequentista_psi():
    return {"p":"pesquisa_saude__frequentista_psi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grounded_theory.get("")
async def i_grounded_theory():
    return {"p":"pesquisa_saude__grounded_theory","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hermeneutica_psi.get("")
async def i_hermeneutica_psi():
    return {"p":"pesquisa_saude__hermeneutica_psi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hierarquia_mental.get("")
async def i_hierarquia_mental():
    return {"p":"pesquisa_saude__hierarquia_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hipercorrecao.get("")
async def i_hipercorrecao():
    return {"p":"pesquisa_saude__hipercorrecao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ipa_analise.get("")
async def i_ipa_analise():
    return {"p":"pesquisa_saude__ipa_analise","s":"ativo","t":datetime.utcnow().isoformat()}
@router_linked_data_mental.get("")
async def i_linked_data_mental():
    return {"p":"pesquisa_saude__linked_data_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_machine_learning_psi.get("")
async def i_machine_learning_psi():
    return {"p":"pesquisa_saude__machine_learning_psi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_metodologia_qualitat.get("")
async def i_metodologia_qualitat():
    return {"p":"pesquisa_saude__metodologia_qualitat","s":"ativo","t":datetime.utcnow().isoformat()}
@router_metodologia_quantita.get("")
async def i_metodologia_quantita():
    return {"p":"pesquisa_saude__metodologia_quantita","s":"ativo","t":datetime.utcnow().isoformat()}
@router_metodos_mistos_psi.get("")
async def i_metodos_mistos_psi():
    return {"p":"pesquisa_saude__metodos_mistos_psi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ontologia_mental.get("")
async def i_ontologia_mental():
    return {"p":"pesquisa_saude__ontologia_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_open_science2.get("")
async def i_open_science2():
    return {"p":"pesquisa_saude__open_science2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_p_hacking.get("")
async def i_p_hacking():
    return {"p":"pesquisa_saude__p_hacking","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pesquisa_acao.get("")
async def i_pesquisa_acao():
    return {"p":"pesquisa_saude__pesquisa_acao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pesquisa_colaborativ.get("")
async def i_pesquisa_colaborativ():
    return {"p":"pesquisa_saude__pesquisa_colaborativ","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pesquisa_participati.get("")
async def i_pesquisa_participati():
    return {"p":"pesquisa_saude__pesquisa_participati","s":"ativo","t":datetime.utcnow().isoformat()}
@router_poder_estatistico2.get("")
async def i_poder_estatistico2():
    return {"p":"pesquisa_saude__poder_estatistico2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_preregistro_pesquisa.get("")
async def i_preregistro_pesquisa():
    return {"p":"pesquisa_saude__preregistro_pesquisa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_processamento_texto_.get("")
async def i_processamento_texto_():
    return {"p":"pesquisa_saude__processamento_texto_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_rdoc_criterios.get("")
async def i_rdoc_criterios():
    return {"p":"pesquisa_saude__rdoc_criterios","s":"ativo","t":datetime.utcnow().isoformat()}
@router_rede_semantica.get("")
async def i_rede_semantica():
    return {"p":"pesquisa_saude__rede_semantica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_registered_reports2.get("")
async def i_registered_reports2():
    return {"p":"pesquisa_saude__registered_reports2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_replicabilidade_psi.get("")
async def i_replicabilidade_psi():
    return {"p":"pesquisa_saude__replicabilidade_psi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sentiment_psi.get("")
async def i_sentiment_psi():
    return {"p":"pesquisa_saude__sentiment_psi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_staging_mental.get("")
async def i_staging_mental():
    return {"p":"pesquisa_saude__staging_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tamanho_efeito2.get("")
async def i_tamanho_efeito2():
    return {"p":"pesquisa_saude__tamanho_efeito2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_taxonomia_mental.get("")
async def i_taxonomia_mental():
    return {"p":"pesquisa_saude__taxonomia_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_text_mining_psi.get("")
async def i_text_mining_psi():
    return {"p":"pesquisa_saude__text_mining_psi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_topic_modeling.get("")
async def i_topic_modeling():
    return {"p":"pesquisa_saude__topic_modeling","s":"ativo","t":datetime.utcnow().isoformat()}
@router_trajetoria_mental.get("")
async def i_trajetoria_mental():
    return {"p":"pesquisa_saude__trajetoria_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_transdiag2.get("")
async def i_transdiag2():
    return {"p":"pesquisa_saude__transdiag2","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_pesquisa_saude_menta(PluginBase):
    name = "consolidated_pesquisa_saude_mental"
    def setup(self, app):
        app.include_router(router_analise_conteudo)
        app.include_router(router_analise_discurso)
        app.include_router(router_analise_narrativa_pe)
        app.include_router(router_analise_sentimento2)
        app.include_router(router_autoetnografia)
        app.include_router(router_bayesiano_psicologia)
        app.include_router(router_big_data_mental)
        app.include_router(router_cid12_futuro)
        app.include_router(router_ciencia_cidada)
        app.include_router(router_citizen_science_ment)
        app.include_router(router_classificacao_mental)
        app.include_router(router_co_producao_conhecim)
        app.include_router(router_continuum_mental)
        app.include_router(router_course_outcome)
        app.include_router(router_crise_replicacao)
        app.include_router(router_deep_learning_psi)
        app.include_router(router_dimensoes_psicopatol)
        app.include_router(router_dsm6_futuro)
        app.include_router(router_espectros_mentais)
        app.include_router(router_etnografia_mental)
        app.include_router(router_fenomenologia_psi)
        app.include_router(router_frequentista_psi)
        app.include_router(router_grounded_theory)
        app.include_router(router_hermeneutica_psi)
        app.include_router(router_hierarquia_mental)
        app.include_router(router_hipercorrecao)
        app.include_router(router_ipa_analise)
        app.include_router(router_linked_data_mental)
        app.include_router(router_machine_learning_psi)
        app.include_router(router_metodologia_qualitat)
        app.include_router(router_metodologia_quantita)
        app.include_router(router_metodos_mistos_psi)
        app.include_router(router_ontologia_mental)
        app.include_router(router_open_science2)
        app.include_router(router_p_hacking)
        app.include_router(router_pesquisa_acao)
        app.include_router(router_pesquisa_colaborativ)
        app.include_router(router_pesquisa_participati)
        app.include_router(router_poder_estatistico2)
        app.include_router(router_preregistro_pesquisa)
        app.include_router(router_processamento_texto_)
        app.include_router(router_rdoc_criterios)
        app.include_router(router_rede_semantica)
        app.include_router(router_registered_reports2)
        app.include_router(router_replicabilidade_psi)
        app.include_router(router_sentiment_psi)
        app.include_router(router_staging_mental)
        app.include_router(router_tamanho_efeito2)
        app.include_router(router_taxonomia_mental)
        app.include_router(router_text_mining_psi)
        app.include_router(router_topic_modeling)
        app.include_router(router_trajetoria_mental)
        app.include_router(router_transdiag2)


plugin = Plugin_pesquisa_saude_menta()
