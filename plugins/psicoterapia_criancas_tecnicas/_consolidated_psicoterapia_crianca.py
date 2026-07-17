from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_argila_crianca = APIRouter(prefix="/api/v1/psicoterapia/argila_crianca", tags=["psicoterapia_criancas_tecnicas"])
router_bibliotherapy_crianc = APIRouter(prefix="/api/v1/psicoterapia/bibliotherapy_crianca", tags=["psicoterapia_criancas_tecnicas"])
router_biofeedback_crianca = APIRouter(prefix="/api/v1/psicoterapia/biofeedback_crianca", tags=["psicoterapia_criancas_tecnicas"])
router_blocos_terapia = APIRouter(prefix="/api/v1/psicoterapia/blocos_terapia", tags=["psicoterapia_criancas_tecnicas"])
router_bonecos_terapeuticos = APIRouter(prefix="/api/v1/psicoterapia/bonecos_terapeuticos", tags=["psicoterapia_criancas_tecnicas"])
router_brinquedoteca = APIRouter(prefix="/api/v1/psicoterapia/brinquedoteca", tags=["psicoterapia_criancas_tecnicas"])
router_caixa_areia = APIRouter(prefix="/api/v1/psicoterapia/caixa_areia", tags=["psicoterapia_criancas_tecnicas"])
router_colagem_crianca = APIRouter(prefix="/api/v1/psicoterapia/colagem_crianca", tags=["psicoterapia_criancas_tecnicas"])
router_construcao_brinquedo = APIRouter(prefix="/api/v1/psicoterapia/construcao_brinquedo", tags=["psicoterapia_criancas_tecnicas"])
router_contos_fadas_terapia = APIRouter(prefix="/api/v1/psicoterapia/contos_fadas_terapia", tags=["psicoterapia_criancas_tecnicas"])
router_danca_crianca = APIRouter(prefix="/api/v1/psicoterapia/danca_crianca", tags=["psicoterapia_criancas_tecnicas"])
router_desenho_terapia = APIRouter(prefix="/api/v1/psicoterapia/desenho_terapia", tags=["psicoterapia_criancas_tecnicas"])
router_dramatizacao_crianca = APIRouter(prefix="/api/v1/psicoterapia/dramatizacao_crianca", tags=["psicoterapia_criancas_tecnicas"])
router_ensaio_comportamenta = APIRouter(prefix="/api/v1/psicoterapia/ensaio_comportamental_cri", tags=["psicoterapia_criancas_tecnicas"])
router_espelho_terapia = APIRouter(prefix="/api/v1/psicoterapia/espelho_terapia", tags=["psicoterapia_criancas_tecnicas"])
router_expressao_emocional_ = APIRouter(prefix="/api/v1/psicoterapia/expressao_emocional_crian", tags=["psicoterapia_criancas_tecnicas"])
router_fantasia_crianca2 = APIRouter(prefix="/api/v1/psicoterapia/fantasia_crianca2", tags=["psicoterapia_criancas_tecnicas"])
router_fantoches_terapia = APIRouter(prefix="/api/v1/psicoterapia/fantoches_terapia", tags=["psicoterapia_criancas_tecnicas"])
router_habilidades_sociais_ = APIRouter(prefix="/api/v1/psicoterapia/habilidades_sociais_crian", tags=["psicoterapia_criancas_tecnicas"])
router_heroi_jornada_crianc = APIRouter(prefix="/api/v1/psicoterapia/heroi_jornada_crianca", tags=["psicoterapia_criancas_tecnicas"])
router_hipnose_crianca2 = APIRouter(prefix="/api/v1/psicoterapia/hipnose_crianca2", tags=["psicoterapia_criancas_tecnicas"])
router_historia_brinquedo = APIRouter(prefix="/api/v1/psicoterapia/historia_brinquedo", tags=["psicoterapia_criancas_tecnicas"])
router_historia_terapeutica = APIRouter(prefix="/api/v1/psicoterapia/historia_terapeutica", tags=["psicoterapia_criancas_tecnicas"])
router_identificacao_emocoe = APIRouter(prefix="/api/v1/psicoterapia/identificacao_emocoes_cri", tags=["psicoterapia_criancas_tecnicas"])
router_imaginacao_crianca = APIRouter(prefix="/api/v1/psicoterapia/imaginacao_crianca", tags=["psicoterapia_criancas_tecnicas"])
router_imitacao_terapeutica = APIRouter(prefix="/api/v1/psicoterapia/imitacao_terapeutica", tags=["psicoterapia_criancas_tecnicas"])
router_jogo_dramatico_clini = APIRouter(prefix="/api/v1/psicoterapia/jogo_dramatico_clinico", tags=["psicoterapia_criancas_tecnicas"])
router_jogo_simbolico_clini = APIRouter(prefix="/api/v1/psicoterapia/jogo_simbolico_clinico", tags=["psicoterapia_criancas_tecnicas"])
router_lego_terapia = APIRouter(prefix="/api/v1/psicoterapia/lego_terapia", tags=["psicoterapia_criancas_tecnicas"])
router_livros_terapeuticos = APIRouter(prefix="/api/v1/psicoterapia/livros_terapeuticos", tags=["psicoterapia_criancas_tecnicas"])
router_ludoterapia_analitic = APIRouter(prefix="/api/v1/psicoterapia/ludoterapia_analitica", tags=["psicoterapia_criancas_tecnicas"])
router_ludoterapia_diretiva = APIRouter(prefix="/api/v1/psicoterapia/ludoterapia_diretiva", tags=["psicoterapia_criancas_tecnicas"])
router_ludoterapia_nao_dire = APIRouter(prefix="/api/v1/psicoterapia/ludoterapia_nao_diretiva", tags=["psicoterapia_criancas_tecnicas"])
router_marionetes = APIRouter(prefix="/api/v1/psicoterapia/marionetes", tags=["psicoterapia_criancas_tecnicas"])
router_massa_modelar = APIRouter(prefix="/api/v1/psicoterapia/massa_modelar", tags=["psicoterapia_criancas_tecnicas"])
router_metaforas_crianca = APIRouter(prefix="/api/v1/psicoterapia/metaforas_crianca", tags=["psicoterapia_criancas_tecnicas"])
router_metaforas_hipnoticas = APIRouter(prefix="/api/v1/psicoterapia/metaforas_hipnoticas_cria", tags=["psicoterapia_criancas_tecnicas"])
router_miniaturas_terapeuti = APIRouter(prefix="/api/v1/psicoterapia/miniaturas_terapeuticas", tags=["psicoterapia_criancas_tecnicas"])
router_mitos_crianca = APIRouter(prefix="/api/v1/psicoterapia/mitos_crianca", tags=["psicoterapia_criancas_tecnicas"])
router_modelagem_crianca = APIRouter(prefix="/api/v1/psicoterapia/modelagem_crianca", tags=["psicoterapia_criancas_tecnicas"])
router_modelagem_crianca2 = APIRouter(prefix="/api/v1/psicoterapia/modelagem_crianca2", tags=["psicoterapia_criancas_tecnicas"])
router_movimento_crianca = APIRouter(prefix="/api/v1/psicoterapia/movimento_crianca", tags=["psicoterapia_criancas_tecnicas"])
router_mundo_em_miniatura = APIRouter(prefix="/api/v1/psicoterapia/mundo_em_miniatura", tags=["psicoterapia_criancas_tecnicas"])
router_musica_crianca = APIRouter(prefix="/api/v1/psicoterapia/musica_crianca", tags=["psicoterapia_criancas_tecnicas"])
router_narrativa_brinquedo = APIRouter(prefix="/api/v1/psicoterapia/narrativa_brinquedo", tags=["psicoterapia_criancas_tecnicas"])
router_origami_terapia_cria = APIRouter(prefix="/api/v1/psicoterapia/origami_terapia_crianca", tags=["psicoterapia_criancas_tecnicas"])
router_personagens_terapia = APIRouter(prefix="/api/v1/psicoterapia/personagens_terapia", tags=["psicoterapia_criancas_tecnicas"])
router_pintura_crianca = APIRouter(prefix="/api/v1/psicoterapia/pintura_crianca", tags=["psicoterapia_criancas_tecnicas"])
router_reforco_positivo_cri = APIRouter(prefix="/api/v1/psicoterapia/reforco_positivo_crianca", tags=["psicoterapia_criancas_tecnicas"])
router_regulacao_emocional_ = APIRouter(prefix="/api/v1/psicoterapia/regulacao_emocional_crian", tags=["psicoterapia_criancas_tecnicas"])
router_relaxamento_crianca = APIRouter(prefix="/api/v1/psicoterapia/relaxamento_crianca", tags=["psicoterapia_criancas_tecnicas"])
router_resilencia_narrativa = APIRouter(prefix="/api/v1/psicoterapia/resilencia_narrativa", tags=["psicoterapia_criancas_tecnicas"])
router_resolucao_problema_c = APIRouter(prefix="/api/v1/psicoterapia/resolucao_problema_crianc", tags=["psicoterapia_criancas_tecnicas"])
router_ritmo_crianca = APIRouter(prefix="/api/v1/psicoterapia/ritmo_crianca", tags=["psicoterapia_criancas_tecnicas"])
router_roleplay_crianca = APIRouter(prefix="/api/v1/psicoterapia/roleplay_crianca", tags=["psicoterapia_criancas_tecnicas"])
router_sandplay_terapia = APIRouter(prefix="/api/v1/psicoterapia/sandplay_terapia", tags=["psicoterapia_criancas_tecnicas"])
router_simbolismo_brinquedo = APIRouter(prefix="/api/v1/psicoterapia/simbolismo_brinquedo", tags=["psicoterapia_criancas_tecnicas"])
router_superacao_narrativa = APIRouter(prefix="/api/v1/psicoterapia/superacao_narrativa", tags=["psicoterapia_criancas_tecnicas"])
router_teatro_crianca = APIRouter(prefix="/api/v1/psicoterapia/teatro_crianca", tags=["psicoterapia_criancas_tecnicas"])
router_terapia_cognitiva_cr = APIRouter(prefix="/api/v1/psicoterapia/terapia_cognitiva_crianca", tags=["psicoterapia_criancas_tecnicas"])
router_terapia_comportament = APIRouter(prefix="/api/v1/psicoterapia/terapia_comportamental_cr", tags=["psicoterapia_criancas_tecnicas"])
router_terapia_jogo_cogniti = APIRouter(prefix="/api/v1/psicoterapia/terapia_jogo_cognitivo", tags=["psicoterapia_criancas_tecnicas"])
router_tolerancia_frustacao = APIRouter(prefix="/api/v1/psicoterapia/tolerancia_frustacao", tags=["psicoterapia_criancas_tecnicas"])
router_treinamento_assertiv = APIRouter(prefix="/api/v1/psicoterapia/treinamento_assertividade", tags=["psicoterapia_criancas_tecnicas"])
router_video_feedback_crian = APIRouter(prefix="/api/v1/psicoterapia/video_feedback_crianca", tags=["psicoterapia_criancas_tecnicas"])
router_visualizacao_crianca = APIRouter(prefix="/api/v1/psicoterapia/visualizacao_crianca", tags=["psicoterapia_criancas_tecnicas"])

@router_argila_crianca.get("")
async def i_argila_crianca():
    return {"p":"psicoterapia_cr_argila_crianca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bibliotherapy_crianc.get("")
async def i_bibliotherapy_crianc():
    return {"p":"psicoterapia_cr_bibliotherapy_crianc","s":"ativo","t":datetime.utcnow().isoformat()}
@router_biofeedback_crianca.get("")
async def i_biofeedback_crianca():
    return {"p":"psicoterapia_cr_biofeedback_crianca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_blocos_terapia.get("")
async def i_blocos_terapia():
    return {"p":"psicoterapia_cr_blocos_terapia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bonecos_terapeuticos.get("")
async def i_bonecos_terapeuticos():
    return {"p":"psicoterapia_cr_bonecos_terapeuticos","s":"ativo","t":datetime.utcnow().isoformat()}
@router_brinquedoteca.get("")
async def i_brinquedoteca():
    return {"p":"psicoterapia_cr_brinquedoteca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_caixa_areia.get("")
async def i_caixa_areia():
    return {"p":"psicoterapia_cr_caixa_areia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_colagem_crianca.get("")
async def i_colagem_crianca():
    return {"p":"psicoterapia_cr_colagem_crianca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_construcao_brinquedo.get("")
async def i_construcao_brinquedo():
    return {"p":"psicoterapia_cr_construcao_brinquedo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_contos_fadas_terapia.get("")
async def i_contos_fadas_terapia():
    return {"p":"psicoterapia_cr_contos_fadas_terapia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_danca_crianca.get("")
async def i_danca_crianca():
    return {"p":"psicoterapia_cr_danca_crianca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_desenho_terapia.get("")
async def i_desenho_terapia():
    return {"p":"psicoterapia_cr_desenho_terapia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dramatizacao_crianca.get("")
async def i_dramatizacao_crianca():
    return {"p":"psicoterapia_cr_dramatizacao_crianca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ensaio_comportamenta.get("")
async def i_ensaio_comportamenta():
    return {"p":"psicoterapia_cr_ensaio_comportamenta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_espelho_terapia.get("")
async def i_espelho_terapia():
    return {"p":"psicoterapia_cr_espelho_terapia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_expressao_emocional_.get("")
async def i_expressao_emocional_():
    return {"p":"psicoterapia_cr_expressao_emocional_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fantasia_crianca2.get("")
async def i_fantasia_crianca2():
    return {"p":"psicoterapia_cr_fantasia_crianca2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fantoches_terapia.get("")
async def i_fantoches_terapia():
    return {"p":"psicoterapia_cr_fantoches_terapia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_habilidades_sociais_.get("")
async def i_habilidades_sociais_():
    return {"p":"psicoterapia_cr_habilidades_sociais_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_heroi_jornada_crianc.get("")
async def i_heroi_jornada_crianc():
    return {"p":"psicoterapia_cr_heroi_jornada_crianc","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hipnose_crianca2.get("")
async def i_hipnose_crianca2():
    return {"p":"psicoterapia_cr_hipnose_crianca2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_historia_brinquedo.get("")
async def i_historia_brinquedo():
    return {"p":"psicoterapia_cr_historia_brinquedo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_historia_terapeutica.get("")
async def i_historia_terapeutica():
    return {"p":"psicoterapia_cr_historia_terapeutica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_identificacao_emocoe.get("")
async def i_identificacao_emocoe():
    return {"p":"psicoterapia_cr_identificacao_emocoe","s":"ativo","t":datetime.utcnow().isoformat()}
@router_imaginacao_crianca.get("")
async def i_imaginacao_crianca():
    return {"p":"psicoterapia_cr_imaginacao_crianca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_imitacao_terapeutica.get("")
async def i_imitacao_terapeutica():
    return {"p":"psicoterapia_cr_imitacao_terapeutica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_jogo_dramatico_clini.get("")
async def i_jogo_dramatico_clini():
    return {"p":"psicoterapia_cr_jogo_dramatico_clini","s":"ativo","t":datetime.utcnow().isoformat()}
@router_jogo_simbolico_clini.get("")
async def i_jogo_simbolico_clini():
    return {"p":"psicoterapia_cr_jogo_simbolico_clini","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lego_terapia.get("")
async def i_lego_terapia():
    return {"p":"psicoterapia_cr_lego_terapia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_livros_terapeuticos.get("")
async def i_livros_terapeuticos():
    return {"p":"psicoterapia_cr_livros_terapeuticos","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ludoterapia_analitic.get("")
async def i_ludoterapia_analitic():
    return {"p":"psicoterapia_cr_ludoterapia_analitic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ludoterapia_diretiva.get("")
async def i_ludoterapia_diretiva():
    return {"p":"psicoterapia_cr_ludoterapia_diretiva","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ludoterapia_nao_dire.get("")
async def i_ludoterapia_nao_dire():
    return {"p":"psicoterapia_cr_ludoterapia_nao_dire","s":"ativo","t":datetime.utcnow().isoformat()}
@router_marionetes.get("")
async def i_marionetes():
    return {"p":"psicoterapia_cr_marionetes","s":"ativo","t":datetime.utcnow().isoformat()}
@router_massa_modelar.get("")
async def i_massa_modelar():
    return {"p":"psicoterapia_cr_massa_modelar","s":"ativo","t":datetime.utcnow().isoformat()}
@router_metaforas_crianca.get("")
async def i_metaforas_crianca():
    return {"p":"psicoterapia_cr_metaforas_crianca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_metaforas_hipnoticas.get("")
async def i_metaforas_hipnoticas():
    return {"p":"psicoterapia_cr_metaforas_hipnoticas","s":"ativo","t":datetime.utcnow().isoformat()}
@router_miniaturas_terapeuti.get("")
async def i_miniaturas_terapeuti():
    return {"p":"psicoterapia_cr_miniaturas_terapeuti","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mitos_crianca.get("")
async def i_mitos_crianca():
    return {"p":"psicoterapia_cr_mitos_crianca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_modelagem_crianca.get("")
async def i_modelagem_crianca():
    return {"p":"psicoterapia_cr_modelagem_crianca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_modelagem_crianca2.get("")
async def i_modelagem_crianca2():
    return {"p":"psicoterapia_cr_modelagem_crianca2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_movimento_crianca.get("")
async def i_movimento_crianca():
    return {"p":"psicoterapia_cr_movimento_crianca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mundo_em_miniatura.get("")
async def i_mundo_em_miniatura():
    return {"p":"psicoterapia_cr_mundo_em_miniatura","s":"ativo","t":datetime.utcnow().isoformat()}
@router_musica_crianca.get("")
async def i_musica_crianca():
    return {"p":"psicoterapia_cr_musica_crianca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_narrativa_brinquedo.get("")
async def i_narrativa_brinquedo():
    return {"p":"psicoterapia_cr_narrativa_brinquedo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_origami_terapia_cria.get("")
async def i_origami_terapia_cria():
    return {"p":"psicoterapia_cr_origami_terapia_cria","s":"ativo","t":datetime.utcnow().isoformat()}
@router_personagens_terapia.get("")
async def i_personagens_terapia():
    return {"p":"psicoterapia_cr_personagens_terapia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pintura_crianca.get("")
async def i_pintura_crianca():
    return {"p":"psicoterapia_cr_pintura_crianca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reforco_positivo_cri.get("")
async def i_reforco_positivo_cri():
    return {"p":"psicoterapia_cr_reforco_positivo_cri","s":"ativo","t":datetime.utcnow().isoformat()}
@router_regulacao_emocional_.get("")
async def i_regulacao_emocional_():
    return {"p":"psicoterapia_cr_regulacao_emocional_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_relaxamento_crianca.get("")
async def i_relaxamento_crianca():
    return {"p":"psicoterapia_cr_relaxamento_crianca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_resilencia_narrativa.get("")
async def i_resilencia_narrativa():
    return {"p":"psicoterapia_cr_resilencia_narrativa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_resolucao_problema_c.get("")
async def i_resolucao_problema_c():
    return {"p":"psicoterapia_cr_resolucao_problema_c","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ritmo_crianca.get("")
async def i_ritmo_crianca():
    return {"p":"psicoterapia_cr_ritmo_crianca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_roleplay_crianca.get("")
async def i_roleplay_crianca():
    return {"p":"psicoterapia_cr_roleplay_crianca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sandplay_terapia.get("")
async def i_sandplay_terapia():
    return {"p":"psicoterapia_cr_sandplay_terapia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_simbolismo_brinquedo.get("")
async def i_simbolismo_brinquedo():
    return {"p":"psicoterapia_cr_simbolismo_brinquedo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_superacao_narrativa.get("")
async def i_superacao_narrativa():
    return {"p":"psicoterapia_cr_superacao_narrativa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_teatro_crianca.get("")
async def i_teatro_crianca():
    return {"p":"psicoterapia_cr_teatro_crianca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_terapia_cognitiva_cr.get("")
async def i_terapia_cognitiva_cr():
    return {"p":"psicoterapia_cr_terapia_cognitiva_cr","s":"ativo","t":datetime.utcnow().isoformat()}
@router_terapia_comportament.get("")
async def i_terapia_comportament():
    return {"p":"psicoterapia_cr_terapia_comportament","s":"ativo","t":datetime.utcnow().isoformat()}
@router_terapia_jogo_cogniti.get("")
async def i_terapia_jogo_cogniti():
    return {"p":"psicoterapia_cr_terapia_jogo_cogniti","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tolerancia_frustacao.get("")
async def i_tolerancia_frustacao():
    return {"p":"psicoterapia_cr_tolerancia_frustacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_treinamento_assertiv.get("")
async def i_treinamento_assertiv():
    return {"p":"psicoterapia_cr_treinamento_assertiv","s":"ativo","t":datetime.utcnow().isoformat()}
@router_video_feedback_crian.get("")
async def i_video_feedback_crian():
    return {"p":"psicoterapia_cr_video_feedback_crian","s":"ativo","t":datetime.utcnow().isoformat()}
@router_visualizacao_crianca.get("")
async def i_visualizacao_crianca():
    return {"p":"psicoterapia_cr_visualizacao_crianca","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_psicoterapia_crianca(PluginBase):
    name = "consolidated_psicoterapia_criancas_tecnicas"
    def setup(self, app):
        app.include_router(router_argila_crianca)
        app.include_router(router_bibliotherapy_crianc)
        app.include_router(router_biofeedback_crianca)
        app.include_router(router_blocos_terapia)
        app.include_router(router_bonecos_terapeuticos)
        app.include_router(router_brinquedoteca)
        app.include_router(router_caixa_areia)
        app.include_router(router_colagem_crianca)
        app.include_router(router_construcao_brinquedo)
        app.include_router(router_contos_fadas_terapia)
        app.include_router(router_danca_crianca)
        app.include_router(router_desenho_terapia)
        app.include_router(router_dramatizacao_crianca)
        app.include_router(router_ensaio_comportamenta)
        app.include_router(router_espelho_terapia)
        app.include_router(router_expressao_emocional_)
        app.include_router(router_fantasia_crianca2)
        app.include_router(router_fantoches_terapia)
        app.include_router(router_habilidades_sociais_)
        app.include_router(router_heroi_jornada_crianc)
        app.include_router(router_hipnose_crianca2)
        app.include_router(router_historia_brinquedo)
        app.include_router(router_historia_terapeutica)
        app.include_router(router_identificacao_emocoe)
        app.include_router(router_imaginacao_crianca)
        app.include_router(router_imitacao_terapeutica)
        app.include_router(router_jogo_dramatico_clini)
        app.include_router(router_jogo_simbolico_clini)
        app.include_router(router_lego_terapia)
        app.include_router(router_livros_terapeuticos)
        app.include_router(router_ludoterapia_analitic)
        app.include_router(router_ludoterapia_diretiva)
        app.include_router(router_ludoterapia_nao_dire)
        app.include_router(router_marionetes)
        app.include_router(router_massa_modelar)
        app.include_router(router_metaforas_crianca)
        app.include_router(router_metaforas_hipnoticas)
        app.include_router(router_miniaturas_terapeuti)
        app.include_router(router_mitos_crianca)
        app.include_router(router_modelagem_crianca)
        app.include_router(router_modelagem_crianca2)
        app.include_router(router_movimento_crianca)
        app.include_router(router_mundo_em_miniatura)
        app.include_router(router_musica_crianca)
        app.include_router(router_narrativa_brinquedo)
        app.include_router(router_origami_terapia_cria)
        app.include_router(router_personagens_terapia)
        app.include_router(router_pintura_crianca)
        app.include_router(router_reforco_positivo_cri)
        app.include_router(router_regulacao_emocional_)
        app.include_router(router_relaxamento_crianca)
        app.include_router(router_resilencia_narrativa)
        app.include_router(router_resolucao_problema_c)
        app.include_router(router_ritmo_crianca)
        app.include_router(router_roleplay_crianca)
        app.include_router(router_sandplay_terapia)
        app.include_router(router_simbolismo_brinquedo)
        app.include_router(router_superacao_narrativa)
        app.include_router(router_teatro_crianca)
        app.include_router(router_terapia_cognitiva_cr)
        app.include_router(router_terapia_comportament)
        app.include_router(router_terapia_jogo_cogniti)
        app.include_router(router_tolerancia_frustacao)
        app.include_router(router_treinamento_assertiv)
        app.include_router(router_video_feedback_crian)
        app.include_router(router_visualizacao_crianca)


plugin = Plugin_psicoterapia_crianca()
