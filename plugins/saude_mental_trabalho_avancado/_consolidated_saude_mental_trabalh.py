from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_adicao_trabalho = APIRouter(prefix="/api/v1/saude_mental/adicao_trabalho", tags=["saude_mental_trabalho_avancado"])
router_agressao_trabalho = APIRouter(prefix="/api/v1/saude_mental/agressao_trabalho", tags=["saude_mental_trabalho_avancado"])
router_aprendizagem_organiz = APIRouter(prefix="/api/v1/saude_mental/aprendizagem_organizacion", tags=["saude_mental_trabalho_avancado"])
router_assedio_moral2 = APIRouter(prefix="/api/v1/saude_mental/assedio_moral2", tags=["saude_mental_trabalho_avancado"])
router_assedio_sexual_traba = APIRouter(prefix="/api/v1/saude_mental/assedio_sexual_trabalho2", tags=["saude_mental_trabalho_avancado"])
router_atencao_trabalho = APIRouter(prefix="/api/v1/saude_mental/atencao_trabalho", tags=["saude_mental_trabalho_avancado"])
router_autoeficacia_trabalh = APIRouter(prefix="/api/v1/saude_mental/autoeficacia_trabalho", tags=["saude_mental_trabalho_avancado"])
router_boundary_work = APIRouter(prefix="/api/v1/saude_mental/boundary_work", tags=["saude_mental_trabalho_avancado"])
router_bullying_trabalho = APIRouter(prefix="/api/v1/saude_mental/bullying_trabalho", tags=["saude_mental_trabalho_avancado"])
router_burnout_assistencia_ = APIRouter(prefix="/api/v1/saude_mental/burnout_assistencia_socia", tags=["saude_mental_trabalho_avancado"])
router_burnout_atletas = APIRouter(prefix="/api/v1/saude_mental/burnout_atletas", tags=["saude_mental_trabalho_avancado"])
router_burnout_bat2 = APIRouter(prefix="/api/v1/saude_mental/burnout_bat2", tags=["saude_mental_trabalho_avancado"])
router_burnout_bombeiro = APIRouter(prefix="/api/v1/saude_mental/burnout_bombeiro", tags=["saude_mental_trabalho_avancado"])
router_burnout_cbi = APIRouter(prefix="/api/v1/saude_mental/burnout_cbi", tags=["saude_mental_trabalho_avancado"])
router_burnout_direito = APIRouter(prefix="/api/v1/saude_mental/burnout_direito", tags=["saude_mental_trabalho_avancado"])
router_burnout_educacao = APIRouter(prefix="/api/v1/saude_mental/burnout_educacao", tags=["saude_mental_trabalho_avancado"])
router_burnout_fases = APIRouter(prefix="/api/v1/saude_mental/burnout_fases", tags=["saude_mental_trabalho_avancado"])
router_burnout_maslach2 = APIRouter(prefix="/api/v1/saude_mental/burnout_maslach2", tags=["saude_mental_trabalho_avancado"])
router_burnout_militar = APIRouter(prefix="/api/v1/saude_mental/burnout_militar", tags=["saude_mental_trabalho_avancado"])
router_burnout_olbi = APIRouter(prefix="/api/v1/saude_mental/burnout_olbi", tags=["saude_mental_trabalho_avancado"])
router_burnout_perfis = APIRouter(prefix="/api/v1/saude_mental/burnout_perfis", tags=["saude_mental_trabalho_avancado"])
router_burnout_policia = APIRouter(prefix="/api/v1/saude_mental/burnout_policia", tags=["saude_mental_trabalho_avancado"])
router_burnout_profissoes = APIRouter(prefix="/api/v1/saude_mental/burnout_profissoes", tags=["saude_mental_trabalho_avancado"])
router_burnout_saude = APIRouter(prefix="/api/v1/saude_mental/burnout_saude", tags=["saude_mental_trabalho_avancado"])
router_burnout_sindrome_esg = APIRouter(prefix="/api/v1/saude_mental/burnout_sindrome_esgotame", tags=["saude_mental_trabalho_avancado"])
router_capital_humano = APIRouter(prefix="/api/v1/saude_mental/capital_humano", tags=["saude_mental_trabalho_avancado"])
router_capital_intelectual = APIRouter(prefix="/api/v1/saude_mental/capital_intelectual", tags=["saude_mental_trabalho_avancado"])
router_capital_psicologico_ = APIRouter(prefix="/api/v1/saude_mental/capital_psicologico_organ", tags=["saude_mental_trabalho_avancado"])
router_capital_social_traba = APIRouter(prefix="/api/v1/saude_mental/capital_social_trabalho", tags=["saude_mental_trabalho_avancado"])
router_carga_cognitiva_trab = APIRouter(prefix="/api/v1/saude_mental/carga_cognitiva_trabalho", tags=["saude_mental_trabalho_avancado"])
router_conflito_trabalho_fa = APIRouter(prefix="/api/v1/saude_mental/conflito_trabalho_familia", tags=["saude_mental_trabalho_avancado"])
router_criatividade_organiz = APIRouter(prefix="/api/v1/saude_mental/criatividade_organizacion", tags=["saude_mental_trabalho_avancado"])
router_crossover_trabalho_f = APIRouter(prefix="/api/v1/saude_mental/crossover_trabalho_famili", tags=["saude_mental_trabalho_avancado"])
router_desigualdade_trabalh = APIRouter(prefix="/api/v1/saude_mental/desigualdade_trabalho", tags=["saude_mental_trabalho_avancado"])
router_despersonalizacao = APIRouter(prefix="/api/v1/saude_mental/despersonalizacao", tags=["saude_mental_trabalho_avancado"])
router_discriminacao_trabal = APIRouter(prefix="/api/v1/saude_mental/discriminacao_trabalho2", tags=["saude_mental_trabalho_avancado"])
router_engagement_trabalho2 = APIRouter(prefix="/api/v1/saude_mental/engagement_trabalho2", tags=["saude_mental_trabalho_avancado"])
router_enriquecimento_traba = APIRouter(prefix="/api/v1/saude_mental/enriquecimento_trabalho", tags=["saude_mental_trabalho_avancado"])
router_ergonomia_cognitiva = APIRouter(prefix="/api/v1/saude_mental/ergonomia_cognitiva", tags=["saude_mental_trabalho_avancado"])
router_esperanca_trabalho = APIRouter(prefix="/api/v1/saude_mental/esperanca_trabalho", tags=["saude_mental_trabalho_avancado"])
router_exaustao_emocional = APIRouter(prefix="/api/v1/saude_mental/exaustao_emocional", tags=["saude_mental_trabalho_avancado"])
router_gestao_conhecimento = APIRouter(prefix="/api/v1/saude_mental/gestao_conhecimento", tags=["saude_mental_trabalho_avancado"])
router_inovacao_trabalho = APIRouter(prefix="/api/v1/saude_mental/inovacao_trabalho", tags=["saude_mental_trabalho_avancado"])
router_integracao_trabalho_ = APIRouter(prefix="/api/v1/saude_mental/integracao_trabalho_famil", tags=["saude_mental_trabalho_avancado"])
router_interferencia_famili = APIRouter(prefix="/api/v1/saude_mental/interferencia_familia_tra", tags=["saude_mental_trabalho_avancado"])
router_jornada_dupla = APIRouter(prefix="/api/v1/saude_mental/jornada_dupla", tags=["saude_mental_trabalho_avancado"])
router_memoria_trabalho_org = APIRouter(prefix="/api/v1/saude_mental/memoria_trabalho_organiza", tags=["saude_mental_trabalho_avancado"])
router_mobbing = APIRouter(prefix="/api/v1/saude_mental/mobbing", tags=["saude_mental_trabalho_avancado"])
router_otimismo_trabalho = APIRouter(prefix="/api/v1/saude_mental/otimismo_trabalho", tags=["saude_mental_trabalho_avancado"])
router_piso_pegajoso = APIRouter(prefix="/api/v1/saude_mental/piso_pegajoso", tags=["saude_mental_trabalho_avancado"])
router_psycap_organizaciona = APIRouter(prefix="/api/v1/saude_mental/psycap_organizacional", tags=["saude_mental_trabalho_avancado"])
router_realizacao_pessoal_t = APIRouter(prefix="/api/v1/saude_mental/realizacao_pessoal_trabal", tags=["saude_mental_trabalho_avancado"])
router_resiliencia_trabalho = APIRouter(prefix="/api/v1/saude_mental/resiliencia_trabalho", tags=["saude_mental_trabalho_avancado"])
router_resolucao_problema_t = APIRouter(prefix="/api/v1/saude_mental/resolucao_problema_trabal", tags=["saude_mental_trabalho_avancado"])
router_segmentacao_trabalho = APIRouter(prefix="/api/v1/saude_mental/segmentacao_trabalho", tags=["saude_mental_trabalho_avancado"])
router_spillover_trabalho_f = APIRouter(prefix="/api/v1/saude_mental/spillover_trabalho_famili", tags=["saude_mental_trabalho_avancado"])
router_teto_vidro = APIRouter(prefix="/api/v1/saude_mental/teto_vidro", tags=["saude_mental_trabalho_avancado"])
router_tomada_decisao_traba = APIRouter(prefix="/api/v1/saude_mental/tomada_decisao_trabalho", tags=["saude_mental_trabalho_avancado"])
router_vigor_dedicacao_abso = APIRouter(prefix="/api/v1/saude_mental/vigor_dedicacao_absorcao", tags=["saude_mental_trabalho_avancado"])
router_violencia_trabalho = APIRouter(prefix="/api/v1/saude_mental/violencia_trabalho", tags=["saude_mental_trabalho_avancado"])
router_work_life_balance2 = APIRouter(prefix="/api/v1/saude_mental/work_life_balance2", tags=["saude_mental_trabalho_avancado"])
router_workaholic_tipos = APIRouter(prefix="/api/v1/saude_mental/workaholic_tipos", tags=["saude_mental_trabalho_avancado"])
router_workaholism2 = APIRouter(prefix="/api/v1/saude_mental/workaholism2", tags=["saude_mental_trabalho_avancado"])

@router_adicao_trabalho.get("")
async def i_adicao_trabalho():
    return {"p":"saude_mental_tr_adicao_trabalho","s":"ativo","t":datetime.utcnow().isoformat()}
@router_agressao_trabalho.get("")
async def i_agressao_trabalho():
    return {"p":"saude_mental_tr_agressao_trabalho","s":"ativo","t":datetime.utcnow().isoformat()}
@router_aprendizagem_organiz.get("")
async def i_aprendizagem_organiz():
    return {"p":"saude_mental_tr_aprendizagem_organiz","s":"ativo","t":datetime.utcnow().isoformat()}
@router_assedio_moral2.get("")
async def i_assedio_moral2():
    return {"p":"saude_mental_tr_assedio_moral2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_assedio_sexual_traba.get("")
async def i_assedio_sexual_traba():
    return {"p":"saude_mental_tr_assedio_sexual_traba","s":"ativo","t":datetime.utcnow().isoformat()}
@router_atencao_trabalho.get("")
async def i_atencao_trabalho():
    return {"p":"saude_mental_tr_atencao_trabalho","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autoeficacia_trabalh.get("")
async def i_autoeficacia_trabalh():
    return {"p":"saude_mental_tr_autoeficacia_trabalh","s":"ativo","t":datetime.utcnow().isoformat()}
@router_boundary_work.get("")
async def i_boundary_work():
    return {"p":"saude_mental_tr_boundary_work","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bullying_trabalho.get("")
async def i_bullying_trabalho():
    return {"p":"saude_mental_tr_bullying_trabalho","s":"ativo","t":datetime.utcnow().isoformat()}
@router_burnout_assistencia_.get("")
async def i_burnout_assistencia_():
    return {"p":"saude_mental_tr_burnout_assistencia_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_burnout_atletas.get("")
async def i_burnout_atletas():
    return {"p":"saude_mental_tr_burnout_atletas","s":"ativo","t":datetime.utcnow().isoformat()}
@router_burnout_bat2.get("")
async def i_burnout_bat2():
    return {"p":"saude_mental_tr_burnout_bat2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_burnout_bombeiro.get("")
async def i_burnout_bombeiro():
    return {"p":"saude_mental_tr_burnout_bombeiro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_burnout_cbi.get("")
async def i_burnout_cbi():
    return {"p":"saude_mental_tr_burnout_cbi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_burnout_direito.get("")
async def i_burnout_direito():
    return {"p":"saude_mental_tr_burnout_direito","s":"ativo","t":datetime.utcnow().isoformat()}
@router_burnout_educacao.get("")
async def i_burnout_educacao():
    return {"p":"saude_mental_tr_burnout_educacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_burnout_fases.get("")
async def i_burnout_fases():
    return {"p":"saude_mental_tr_burnout_fases","s":"ativo","t":datetime.utcnow().isoformat()}
@router_burnout_maslach2.get("")
async def i_burnout_maslach2():
    return {"p":"saude_mental_tr_burnout_maslach2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_burnout_militar.get("")
async def i_burnout_militar():
    return {"p":"saude_mental_tr_burnout_militar","s":"ativo","t":datetime.utcnow().isoformat()}
@router_burnout_olbi.get("")
async def i_burnout_olbi():
    return {"p":"saude_mental_tr_burnout_olbi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_burnout_perfis.get("")
async def i_burnout_perfis():
    return {"p":"saude_mental_tr_burnout_perfis","s":"ativo","t":datetime.utcnow().isoformat()}
@router_burnout_policia.get("")
async def i_burnout_policia():
    return {"p":"saude_mental_tr_burnout_policia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_burnout_profissoes.get("")
async def i_burnout_profissoes():
    return {"p":"saude_mental_tr_burnout_profissoes","s":"ativo","t":datetime.utcnow().isoformat()}
@router_burnout_saude.get("")
async def i_burnout_saude():
    return {"p":"saude_mental_tr_burnout_saude","s":"ativo","t":datetime.utcnow().isoformat()}
@router_burnout_sindrome_esg.get("")
async def i_burnout_sindrome_esg():
    return {"p":"saude_mental_tr_burnout_sindrome_esg","s":"ativo","t":datetime.utcnow().isoformat()}
@router_capital_humano.get("")
async def i_capital_humano():
    return {"p":"saude_mental_tr_capital_humano","s":"ativo","t":datetime.utcnow().isoformat()}
@router_capital_intelectual.get("")
async def i_capital_intelectual():
    return {"p":"saude_mental_tr_capital_intelectual","s":"ativo","t":datetime.utcnow().isoformat()}
@router_capital_psicologico_.get("")
async def i_capital_psicologico_():
    return {"p":"saude_mental_tr_capital_psicologico_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_capital_social_traba.get("")
async def i_capital_social_traba():
    return {"p":"saude_mental_tr_capital_social_traba","s":"ativo","t":datetime.utcnow().isoformat()}
@router_carga_cognitiva_trab.get("")
async def i_carga_cognitiva_trab():
    return {"p":"saude_mental_tr_carga_cognitiva_trab","s":"ativo","t":datetime.utcnow().isoformat()}
@router_conflito_trabalho_fa.get("")
async def i_conflito_trabalho_fa():
    return {"p":"saude_mental_tr_conflito_trabalho_fa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_criatividade_organiz.get("")
async def i_criatividade_organiz():
    return {"p":"saude_mental_tr_criatividade_organiz","s":"ativo","t":datetime.utcnow().isoformat()}
@router_crossover_trabalho_f.get("")
async def i_crossover_trabalho_f():
    return {"p":"saude_mental_tr_crossover_trabalho_f","s":"ativo","t":datetime.utcnow().isoformat()}
@router_desigualdade_trabalh.get("")
async def i_desigualdade_trabalh():
    return {"p":"saude_mental_tr_desigualdade_trabalh","s":"ativo","t":datetime.utcnow().isoformat()}
@router_despersonalizacao.get("")
async def i_despersonalizacao():
    return {"p":"saude_mental_tr_despersonalizacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_discriminacao_trabal.get("")
async def i_discriminacao_trabal():
    return {"p":"saude_mental_tr_discriminacao_trabal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_engagement_trabalho2.get("")
async def i_engagement_trabalho2():
    return {"p":"saude_mental_tr_engagement_trabalho2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_enriquecimento_traba.get("")
async def i_enriquecimento_traba():
    return {"p":"saude_mental_tr_enriquecimento_traba","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ergonomia_cognitiva.get("")
async def i_ergonomia_cognitiva():
    return {"p":"saude_mental_tr_ergonomia_cognitiva","s":"ativo","t":datetime.utcnow().isoformat()}
@router_esperanca_trabalho.get("")
async def i_esperanca_trabalho():
    return {"p":"saude_mental_tr_esperanca_trabalho","s":"ativo","t":datetime.utcnow().isoformat()}
@router_exaustao_emocional.get("")
async def i_exaustao_emocional():
    return {"p":"saude_mental_tr_exaustao_emocional","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gestao_conhecimento.get("")
async def i_gestao_conhecimento():
    return {"p":"saude_mental_tr_gestao_conhecimento","s":"ativo","t":datetime.utcnow().isoformat()}
@router_inovacao_trabalho.get("")
async def i_inovacao_trabalho():
    return {"p":"saude_mental_tr_inovacao_trabalho","s":"ativo","t":datetime.utcnow().isoformat()}
@router_integracao_trabalho_.get("")
async def i_integracao_trabalho_():
    return {"p":"saude_mental_tr_integracao_trabalho_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_interferencia_famili.get("")
async def i_interferencia_famili():
    return {"p":"saude_mental_tr_interferencia_famili","s":"ativo","t":datetime.utcnow().isoformat()}
@router_jornada_dupla.get("")
async def i_jornada_dupla():
    return {"p":"saude_mental_tr_jornada_dupla","s":"ativo","t":datetime.utcnow().isoformat()}
@router_memoria_trabalho_org.get("")
async def i_memoria_trabalho_org():
    return {"p":"saude_mental_tr_memoria_trabalho_org","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mobbing.get("")
async def i_mobbing():
    return {"p":"saude_mental_tr_mobbing","s":"ativo","t":datetime.utcnow().isoformat()}
@router_otimismo_trabalho.get("")
async def i_otimismo_trabalho():
    return {"p":"saude_mental_tr_otimismo_trabalho","s":"ativo","t":datetime.utcnow().isoformat()}
@router_piso_pegajoso.get("")
async def i_piso_pegajoso():
    return {"p":"saude_mental_tr_piso_pegajoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psycap_organizaciona.get("")
async def i_psycap_organizaciona():
    return {"p":"saude_mental_tr_psycap_organizaciona","s":"ativo","t":datetime.utcnow().isoformat()}
@router_realizacao_pessoal_t.get("")
async def i_realizacao_pessoal_t():
    return {"p":"saude_mental_tr_realizacao_pessoal_t","s":"ativo","t":datetime.utcnow().isoformat()}
@router_resiliencia_trabalho.get("")
async def i_resiliencia_trabalho():
    return {"p":"saude_mental_tr_resiliencia_trabalho","s":"ativo","t":datetime.utcnow().isoformat()}
@router_resolucao_problema_t.get("")
async def i_resolucao_problema_t():
    return {"p":"saude_mental_tr_resolucao_problema_t","s":"ativo","t":datetime.utcnow().isoformat()}
@router_segmentacao_trabalho.get("")
async def i_segmentacao_trabalho():
    return {"p":"saude_mental_tr_segmentacao_trabalho","s":"ativo","t":datetime.utcnow().isoformat()}
@router_spillover_trabalho_f.get("")
async def i_spillover_trabalho_f():
    return {"p":"saude_mental_tr_spillover_trabalho_f","s":"ativo","t":datetime.utcnow().isoformat()}
@router_teto_vidro.get("")
async def i_teto_vidro():
    return {"p":"saude_mental_tr_teto_vidro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tomada_decisao_traba.get("")
async def i_tomada_decisao_traba():
    return {"p":"saude_mental_tr_tomada_decisao_traba","s":"ativo","t":datetime.utcnow().isoformat()}
@router_vigor_dedicacao_abso.get("")
async def i_vigor_dedicacao_abso():
    return {"p":"saude_mental_tr_vigor_dedicacao_abso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_violencia_trabalho.get("")
async def i_violencia_trabalho():
    return {"p":"saude_mental_tr_violencia_trabalho","s":"ativo","t":datetime.utcnow().isoformat()}
@router_work_life_balance2.get("")
async def i_work_life_balance2():
    return {"p":"saude_mental_tr_work_life_balance2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_workaholic_tipos.get("")
async def i_workaholic_tipos():
    return {"p":"saude_mental_tr_workaholic_tipos","s":"ativo","t":datetime.utcnow().isoformat()}
@router_workaholism2.get("")
async def i_workaholism2():
    return {"p":"saude_mental_tr_workaholism2","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_saude_mental_trabalh(PluginBase):
    name = "consolidated_saude_mental_trabalho_avancado"
    def setup(self, app):
        app.include_router(router_adicao_trabalho)
        app.include_router(router_agressao_trabalho)
        app.include_router(router_aprendizagem_organiz)
        app.include_router(router_assedio_moral2)
        app.include_router(router_assedio_sexual_traba)
        app.include_router(router_atencao_trabalho)
        app.include_router(router_autoeficacia_trabalh)
        app.include_router(router_boundary_work)
        app.include_router(router_bullying_trabalho)
        app.include_router(router_burnout_assistencia_)
        app.include_router(router_burnout_atletas)
        app.include_router(router_burnout_bat2)
        app.include_router(router_burnout_bombeiro)
        app.include_router(router_burnout_cbi)
        app.include_router(router_burnout_direito)
        app.include_router(router_burnout_educacao)
        app.include_router(router_burnout_fases)
        app.include_router(router_burnout_maslach2)
        app.include_router(router_burnout_militar)
        app.include_router(router_burnout_olbi)
        app.include_router(router_burnout_perfis)
        app.include_router(router_burnout_policia)
        app.include_router(router_burnout_profissoes)
        app.include_router(router_burnout_saude)
        app.include_router(router_burnout_sindrome_esg)
        app.include_router(router_capital_humano)
        app.include_router(router_capital_intelectual)
        app.include_router(router_capital_psicologico_)
        app.include_router(router_capital_social_traba)
        app.include_router(router_carga_cognitiva_trab)
        app.include_router(router_conflito_trabalho_fa)
        app.include_router(router_criatividade_organiz)
        app.include_router(router_crossover_trabalho_f)
        app.include_router(router_desigualdade_trabalh)
        app.include_router(router_despersonalizacao)
        app.include_router(router_discriminacao_trabal)
        app.include_router(router_engagement_trabalho2)
        app.include_router(router_enriquecimento_traba)
        app.include_router(router_ergonomia_cognitiva)
        app.include_router(router_esperanca_trabalho)
        app.include_router(router_exaustao_emocional)
        app.include_router(router_gestao_conhecimento)
        app.include_router(router_inovacao_trabalho)
        app.include_router(router_integracao_trabalho_)
        app.include_router(router_interferencia_famili)
        app.include_router(router_jornada_dupla)
        app.include_router(router_memoria_trabalho_org)
        app.include_router(router_mobbing)
        app.include_router(router_otimismo_trabalho)
        app.include_router(router_piso_pegajoso)
        app.include_router(router_psycap_organizaciona)
        app.include_router(router_realizacao_pessoal_t)
        app.include_router(router_resiliencia_trabalho)
        app.include_router(router_resolucao_problema_t)
        app.include_router(router_segmentacao_trabalho)
        app.include_router(router_spillover_trabalho_f)
        app.include_router(router_teto_vidro)
        app.include_router(router_tomada_decisao_traba)
        app.include_router(router_vigor_dedicacao_abso)
        app.include_router(router_violencia_trabalho)
        app.include_router(router_work_life_balance2)
        app.include_router(router_workaholic_tipos)
        app.include_router(router_workaholism2)


plugin = Plugin_saude_mental_trabalh()
