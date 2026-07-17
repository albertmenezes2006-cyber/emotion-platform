from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_anosodiaforia = APIRouter(prefix="/api/v1/psicopatolog/anosodiaforia", tags=["psicopatologia_avancada"])
router_anosognosia = APIRouter(prefix="/api/v1/psicopatolog/anosognosia", tags=["psicopatologia_avancada"])
router_autopercepao_alterad = APIRouter(prefix="/api/v1/psicopatolog/autopercepao_alterada", tags=["psicopatologia_avancada"])
router_autoscopia = APIRouter(prefix="/api/v1/psicopatolog/autoscopia", tags=["psicopatologia_avancada"])
router_burden_disease = APIRouter(prefix="/api/v1/psicopatolog/burden_disease", tags=["psicopatologia_avancada"])
router_ciclico = APIRouter(prefix="/api/v1/psicopatolog/ciclico", tags=["psicopatologia_avancada"])
router_comorbidade2 = APIRouter(prefix="/api/v1/psicopatolog/comorbidade2", tags=["psicopatologia_avancada"])
router_consciencia_doenca = APIRouter(prefix="/api/v1/psicopatolog/consciencia_doenca", tags=["psicopatologia_avancada"])
router_critica_patologica = APIRouter(prefix="/api/v1/psicopatolog/critica_patologica", tags=["psicopatologia_avancada"])
router_cronicidade = APIRouter(prefix="/api/v1/psicopatolog/cronicidade", tags=["psicopatologia_avancada"])
router_curso_temporal = APIRouter(prefix="/api/v1/psicopatolog/curso_temporal", tags=["psicopatologia_avancada"])
router_desduplamento = APIRouter(prefix="/api/v1/psicopatolog/desduplamento", tags=["psicopatologia_avancada"])
router_deteriorante = APIRouter(prefix="/api/v1/psicopatolog/deteriorante", tags=["psicopatologia_avancada"])
router_doenca_mental = APIRouter(prefix="/api/v1/psicopatolog/doenca_mental", tags=["psicopatologia_avancada"])
router_episodico = APIRouter(prefix="/api/v1/psicopatolog/episodico", tags=["psicopatologia_avancada"])
router_episodio = APIRouter(prefix="/api/v1/psicopatolog/episodio", tags=["psicopatologia_avancada"])
router_estavel = APIRouter(prefix="/api/v1/psicopatolog/estavel", tags=["psicopatologia_avancada"])
router_flutuante = APIRouter(prefix="/api/v1/psicopatolog/flutuante", tags=["psicopatologia_avancada"])
router_funcionamento_global = APIRouter(prefix="/api/v1/psicopatolog/funcionamento_global", tags=["psicopatologia_avancada"])
router_heautoscopia = APIRouter(prefix="/api/v1/psicopatolog/heautoscopia", tags=["psicopatologia_avancada"])
router_heterogeneidade = APIRouter(prefix="/api/v1/psicopatolog/heterogeneidade", tags=["psicopatologia_avancada"])
router_homogeneidade = APIRouter(prefix="/api/v1/psicopatolog/homogeneidade", tags=["psicopatologia_avancada"])
router_insight_clinico = APIRouter(prefix="/api/v1/psicopatolog/insight_clinico", tags=["psicopatologia_avancada"])
router_julgamento_clinico = APIRouter(prefix="/api/v1/psicopatolog/julgamento_clinico", tags=["psicopatologia_avancada"])
router_multimorbidade = APIRouter(prefix="/api/v1/psicopatolog/multimorbidade", tags=["psicopatologia_avancada"])
router_onset_agudo = APIRouter(prefix="/api/v1/psicopatolog/onset_agudo", tags=["psicopatologia_avancada"])
router_onset_gradual = APIRouter(prefix="/api/v1/psicopatolog/onset_gradual", tags=["psicopatologia_avancada"])
router_onset_insidioso = APIRouter(prefix="/api/v1/psicopatolog/onset_insidioso", tags=["psicopatologia_avancada"])
router_polimorbidade = APIRouter(prefix="/api/v1/psicopatolog/polimorbidade", tags=["psicopatologia_avancada"])
router_problem_behavior = APIRouter(prefix="/api/v1/psicopatolog/problem_behavior", tags=["psicopatologia_avancada"])
router_prodromo = APIRouter(prefix="/api/v1/psicopatolog/prodromo", tags=["psicopatologia_avancada"])
router_progressivo = APIRouter(prefix="/api/v1/psicopatolog/progressivo", tags=["psicopatologia_avancada"])
router_psicopatologia_biolo = APIRouter(prefix="/api/v1/psicopatolog/psicopatologia_biologica", tags=["psicopatologia_avancada"])
router_psicopatologia_categ = APIRouter(prefix="/api/v1/psicopatolog/psicopatologia_categorial", tags=["psicopatologia_avancada"])
router_psicopatologia_cogni = APIRouter(prefix="/api/v1/psicopatolog/psicopatologia_cognitiva", tags=["psicopatologia_avancada"])
router_psicopatologia_cultu = APIRouter(prefix="/api/v1/psicopatolog/psicopatologia_cultural", tags=["psicopatologia_avancada"])
router_psicopatologia_descr = APIRouter(prefix="/api/v1/psicopatolog/psicopatologia_descritiva", tags=["psicopatologia_avancada"])
router_psicopatologia_desen = APIRouter(prefix="/api/v1/psicopatolog/psicopatologia_desenvolvi", tags=["psicopatologia_avancada"])
router_psicopatologia_dimen = APIRouter(prefix="/api/v1/psicopatolog/psicopatologia_dimensiona", tags=["psicopatologia_avancada"])
router_psicopatologia_evolu = APIRouter(prefix="/api/v1/psicopatolog/psicopatologia_evoluciona", tags=["psicopatologia_avancada"])
router_psicopatologia_exist = APIRouter(prefix="/api/v1/psicopatolog/psicopatologia_existencia", tags=["psicopatologia_avancada"])
router_psicopatologia_exper = APIRouter(prefix="/api/v1/psicopatolog/psicopatologia_experiment", tags=["psicopatologia_avancada"])
router_psicopatologia_expli = APIRouter(prefix="/api/v1/psicopatolog/psicopatologia_explicativ", tags=["psicopatologia_avancada"])
router_psicopatologia_fenom = APIRouter(prefix="/api/v1/psicopatolog/psicopatologia_fenomenolo", tags=["psicopatologia_avancada"])
router_psicopatologia_human = APIRouter(prefix="/api/v1/psicopatolog/psicopatologia_humanista", tags=["psicopatologia_avancada"])
router_psicopatologia_integ = APIRouter(prefix="/api/v1/psicopatolog/psicopatologia_integrativ", tags=["psicopatologia_avancada"])
router_psicopatologia_proce = APIRouter(prefix="/api/v1/psicopatolog/psicopatologia_processual", tags=["psicopatologia_avancada"])
router_psicopatologia_psico = APIRouter(prefix="/api/v1/psicopatolog/psicopatologia_psicodinam", tags=["psicopatologia_avancada"])
router_psicopatologia_socia = APIRouter(prefix="/api/v1/psicopatolog/psicopatologia_social", tags=["psicopatologia_avancada"])
router_psicopatologia_trans = APIRouter(prefix="/api/v1/psicopatolog/psicopatologia_transdiagn", tags=["psicopatologia_avancada"])
router_qualidade_vida_psico = APIRouter(prefix="/api/v1/psicopatolog/qualidade_vida_psico", tags=["psicopatologia_avancada"])
router_recaida = APIRouter(prefix="/api/v1/psicopatolog/recaida", tags=["psicopatologia_avancada"])
router_recorrencia = APIRouter(prefix="/api/v1/psicopatolog/recorrencia", tags=["psicopatologia_avancada"])
router_recuperacao = APIRouter(prefix="/api/v1/psicopatolog/recuperacao", tags=["psicopatologia_avancada"])
router_remissao = APIRouter(prefix="/api/v1/psicopatolog/remissao", tags=["psicopatologia_avancada"])
router_sazonal = APIRouter(prefix="/api/v1/psicopatolog/sazonal", tags=["psicopatologia_avancada"])
router_sinal_clinico = APIRouter(prefix="/api/v1/psicopatolog/sinal_clinico", tags=["psicopatologia_avancada"])
router_sindrome_clinica = APIRouter(prefix="/api/v1/psicopatolog/sindrome_clinica", tags=["psicopatologia_avancada"])
router_sintoma_primario = APIRouter(prefix="/api/v1/psicopatolog/sintoma_primario", tags=["psicopatologia_avancada"])
router_sintoma_secundario = APIRouter(prefix="/api/v1/psicopatolog/sintoma_secundario", tags=["psicopatologia_avancada"])
router_sintoma_terciario = APIRouter(prefix="/api/v1/psicopatolog/sintoma_terciario", tags=["psicopatologia_avancada"])
router_somatognosia = APIRouter(prefix="/api/v1/psicopatolog/somatognosia", tags=["psicopatologia_avancada"])
router_subagudo = APIRouter(prefix="/api/v1/psicopatolog/subagudo", tags=["psicopatologia_avancada"])
router_transtorno_mental = APIRouter(prefix="/api/v1/psicopatolog/transtorno_mental", tags=["psicopatologia_avancada"])
router_variabilidade = APIRouter(prefix="/api/v1/psicopatolog/variabilidade", tags=["psicopatologia_avancada"])

@router_anosodiaforia.get("")
async def i_anosodiaforia():
    return {"p":"psicopatologia__anosodiaforia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_anosognosia.get("")
async def i_anosognosia():
    return {"p":"psicopatologia__anosognosia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autopercepao_alterad.get("")
async def i_autopercepao_alterad():
    return {"p":"psicopatologia__autopercepao_alterad","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autoscopia.get("")
async def i_autoscopia():
    return {"p":"psicopatologia__autoscopia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_burden_disease.get("")
async def i_burden_disease():
    return {"p":"psicopatologia__burden_disease","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ciclico.get("")
async def i_ciclico():
    return {"p":"psicopatologia__ciclico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_comorbidade2.get("")
async def i_comorbidade2():
    return {"p":"psicopatologia__comorbidade2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_consciencia_doenca.get("")
async def i_consciencia_doenca():
    return {"p":"psicopatologia__consciencia_doenca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_critica_patologica.get("")
async def i_critica_patologica():
    return {"p":"psicopatologia__critica_patologica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cronicidade.get("")
async def i_cronicidade():
    return {"p":"psicopatologia__cronicidade","s":"ativo","t":datetime.utcnow().isoformat()}
@router_curso_temporal.get("")
async def i_curso_temporal():
    return {"p":"psicopatologia__curso_temporal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_desduplamento.get("")
async def i_desduplamento():
    return {"p":"psicopatologia__desduplamento","s":"ativo","t":datetime.utcnow().isoformat()}
@router_deteriorante.get("")
async def i_deteriorante():
    return {"p":"psicopatologia__deteriorante","s":"ativo","t":datetime.utcnow().isoformat()}
@router_doenca_mental.get("")
async def i_doenca_mental():
    return {"p":"psicopatologia__doenca_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_episodico.get("")
async def i_episodico():
    return {"p":"psicopatologia__episodico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_episodio.get("")
async def i_episodio():
    return {"p":"psicopatologia__episodio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_estavel.get("")
async def i_estavel():
    return {"p":"psicopatologia__estavel","s":"ativo","t":datetime.utcnow().isoformat()}
@router_flutuante.get("")
async def i_flutuante():
    return {"p":"psicopatologia__flutuante","s":"ativo","t":datetime.utcnow().isoformat()}
@router_funcionamento_global.get("")
async def i_funcionamento_global():
    return {"p":"psicopatologia__funcionamento_global","s":"ativo","t":datetime.utcnow().isoformat()}
@router_heautoscopia.get("")
async def i_heautoscopia():
    return {"p":"psicopatologia__heautoscopia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_heterogeneidade.get("")
async def i_heterogeneidade():
    return {"p":"psicopatologia__heterogeneidade","s":"ativo","t":datetime.utcnow().isoformat()}
@router_homogeneidade.get("")
async def i_homogeneidade():
    return {"p":"psicopatologia__homogeneidade","s":"ativo","t":datetime.utcnow().isoformat()}
@router_insight_clinico.get("")
async def i_insight_clinico():
    return {"p":"psicopatologia__insight_clinico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_julgamento_clinico.get("")
async def i_julgamento_clinico():
    return {"p":"psicopatologia__julgamento_clinico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_multimorbidade.get("")
async def i_multimorbidade():
    return {"p":"psicopatologia__multimorbidade","s":"ativo","t":datetime.utcnow().isoformat()}
@router_onset_agudo.get("")
async def i_onset_agudo():
    return {"p":"psicopatologia__onset_agudo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_onset_gradual.get("")
async def i_onset_gradual():
    return {"p":"psicopatologia__onset_gradual","s":"ativo","t":datetime.utcnow().isoformat()}
@router_onset_insidioso.get("")
async def i_onset_insidioso():
    return {"p":"psicopatologia__onset_insidioso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_polimorbidade.get("")
async def i_polimorbidade():
    return {"p":"psicopatologia__polimorbidade","s":"ativo","t":datetime.utcnow().isoformat()}
@router_problem_behavior.get("")
async def i_problem_behavior():
    return {"p":"psicopatologia__problem_behavior","s":"ativo","t":datetime.utcnow().isoformat()}
@router_prodromo.get("")
async def i_prodromo():
    return {"p":"psicopatologia__prodromo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_progressivo.get("")
async def i_progressivo():
    return {"p":"psicopatologia__progressivo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicopatologia_biolo.get("")
async def i_psicopatologia_biolo():
    return {"p":"psicopatologia__psicopatologia_biolo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicopatologia_categ.get("")
async def i_psicopatologia_categ():
    return {"p":"psicopatologia__psicopatologia_categ","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicopatologia_cogni.get("")
async def i_psicopatologia_cogni():
    return {"p":"psicopatologia__psicopatologia_cogni","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicopatologia_cultu.get("")
async def i_psicopatologia_cultu():
    return {"p":"psicopatologia__psicopatologia_cultu","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicopatologia_descr.get("")
async def i_psicopatologia_descr():
    return {"p":"psicopatologia__psicopatologia_descr","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicopatologia_desen.get("")
async def i_psicopatologia_desen():
    return {"p":"psicopatologia__psicopatologia_desen","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicopatologia_dimen.get("")
async def i_psicopatologia_dimen():
    return {"p":"psicopatologia__psicopatologia_dimen","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicopatologia_evolu.get("")
async def i_psicopatologia_evolu():
    return {"p":"psicopatologia__psicopatologia_evolu","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicopatologia_exist.get("")
async def i_psicopatologia_exist():
    return {"p":"psicopatologia__psicopatologia_exist","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicopatologia_exper.get("")
async def i_psicopatologia_exper():
    return {"p":"psicopatologia__psicopatologia_exper","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicopatologia_expli.get("")
async def i_psicopatologia_expli():
    return {"p":"psicopatologia__psicopatologia_expli","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicopatologia_fenom.get("")
async def i_psicopatologia_fenom():
    return {"p":"psicopatologia__psicopatologia_fenom","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicopatologia_human.get("")
async def i_psicopatologia_human():
    return {"p":"psicopatologia__psicopatologia_human","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicopatologia_integ.get("")
async def i_psicopatologia_integ():
    return {"p":"psicopatologia__psicopatologia_integ","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicopatologia_proce.get("")
async def i_psicopatologia_proce():
    return {"p":"psicopatologia__psicopatologia_proce","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicopatologia_psico.get("")
async def i_psicopatologia_psico():
    return {"p":"psicopatologia__psicopatologia_psico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicopatologia_socia.get("")
async def i_psicopatologia_socia():
    return {"p":"psicopatologia__psicopatologia_socia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicopatologia_trans.get("")
async def i_psicopatologia_trans():
    return {"p":"psicopatologia__psicopatologia_trans","s":"ativo","t":datetime.utcnow().isoformat()}
@router_qualidade_vida_psico.get("")
async def i_qualidade_vida_psico():
    return {"p":"psicopatologia__qualidade_vida_psico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_recaida.get("")
async def i_recaida():
    return {"p":"psicopatologia__recaida","s":"ativo","t":datetime.utcnow().isoformat()}
@router_recorrencia.get("")
async def i_recorrencia():
    return {"p":"psicopatologia__recorrencia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_recuperacao.get("")
async def i_recuperacao():
    return {"p":"psicopatologia__recuperacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_remissao.get("")
async def i_remissao():
    return {"p":"psicopatologia__remissao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sazonal.get("")
async def i_sazonal():
    return {"p":"psicopatologia__sazonal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sinal_clinico.get("")
async def i_sinal_clinico():
    return {"p":"psicopatologia__sinal_clinico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sindrome_clinica.get("")
async def i_sindrome_clinica():
    return {"p":"psicopatologia__sindrome_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sintoma_primario.get("")
async def i_sintoma_primario():
    return {"p":"psicopatologia__sintoma_primario","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sintoma_secundario.get("")
async def i_sintoma_secundario():
    return {"p":"psicopatologia__sintoma_secundario","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sintoma_terciario.get("")
async def i_sintoma_terciario():
    return {"p":"psicopatologia__sintoma_terciario","s":"ativo","t":datetime.utcnow().isoformat()}
@router_somatognosia.get("")
async def i_somatognosia():
    return {"p":"psicopatologia__somatognosia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_subagudo.get("")
async def i_subagudo():
    return {"p":"psicopatologia__subagudo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_transtorno_mental.get("")
async def i_transtorno_mental():
    return {"p":"psicopatologia__transtorno_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_variabilidade.get("")
async def i_variabilidade():
    return {"p":"psicopatologia__variabilidade","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_psicopatologia_avanc(PluginBase):
    name = "consolidated_psicopatologia_avancada"
    def setup(self, app):
        app.include_router(router_anosodiaforia)
        app.include_router(router_anosognosia)
        app.include_router(router_autopercepao_alterad)
        app.include_router(router_autoscopia)
        app.include_router(router_burden_disease)
        app.include_router(router_ciclico)
        app.include_router(router_comorbidade2)
        app.include_router(router_consciencia_doenca)
        app.include_router(router_critica_patologica)
        app.include_router(router_cronicidade)
        app.include_router(router_curso_temporal)
        app.include_router(router_desduplamento)
        app.include_router(router_deteriorante)
        app.include_router(router_doenca_mental)
        app.include_router(router_episodico)
        app.include_router(router_episodio)
        app.include_router(router_estavel)
        app.include_router(router_flutuante)
        app.include_router(router_funcionamento_global)
        app.include_router(router_heautoscopia)
        app.include_router(router_heterogeneidade)
        app.include_router(router_homogeneidade)
        app.include_router(router_insight_clinico)
        app.include_router(router_julgamento_clinico)
        app.include_router(router_multimorbidade)
        app.include_router(router_onset_agudo)
        app.include_router(router_onset_gradual)
        app.include_router(router_onset_insidioso)
        app.include_router(router_polimorbidade)
        app.include_router(router_problem_behavior)
        app.include_router(router_prodromo)
        app.include_router(router_progressivo)
        app.include_router(router_psicopatologia_biolo)
        app.include_router(router_psicopatologia_categ)
        app.include_router(router_psicopatologia_cogni)
        app.include_router(router_psicopatologia_cultu)
        app.include_router(router_psicopatologia_descr)
        app.include_router(router_psicopatologia_desen)
        app.include_router(router_psicopatologia_dimen)
        app.include_router(router_psicopatologia_evolu)
        app.include_router(router_psicopatologia_exist)
        app.include_router(router_psicopatologia_exper)
        app.include_router(router_psicopatologia_expli)
        app.include_router(router_psicopatologia_fenom)
        app.include_router(router_psicopatologia_human)
        app.include_router(router_psicopatologia_integ)
        app.include_router(router_psicopatologia_proce)
        app.include_router(router_psicopatologia_psico)
        app.include_router(router_psicopatologia_socia)
        app.include_router(router_psicopatologia_trans)
        app.include_router(router_qualidade_vida_psico)
        app.include_router(router_recaida)
        app.include_router(router_recorrencia)
        app.include_router(router_recuperacao)
        app.include_router(router_remissao)
        app.include_router(router_sazonal)
        app.include_router(router_sinal_clinico)
        app.include_router(router_sindrome_clinica)
        app.include_router(router_sintoma_primario)
        app.include_router(router_sintoma_secundario)
        app.include_router(router_sintoma_terciario)
        app.include_router(router_somatognosia)
        app.include_router(router_subagudo)
        app.include_router(router_transtorno_mental)
        app.include_router(router_variabilidade)


plugin = Plugin_psicopatologia_avanc()
