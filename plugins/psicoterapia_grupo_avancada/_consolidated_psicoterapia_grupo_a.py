from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_altruismo_grupo = APIRouter(prefix="/api/v1/psicoterapia/altruismo_grupo", tags=["psicoterapia_grupo_avancada"])
router_ancestralidade_siste = APIRouter(prefix="/api/v1/psicoterapia/ancestralidade_sistemica", tags=["psicoterapia_grupo_avancada"])
router_aprendizado_imitativ = APIRouter(prefix="/api/v1/psicoterapia/aprendizado_imitativo", tags=["psicoterapia_grupo_avancada"])
router_aqui_agora_grupo = APIRouter(prefix="/api/v1/psicoterapia/aqui_agora_grupo", tags=["psicoterapia_grupo_avancada"])
router_bert_hellinger = APIRouter(prefix="/api/v1/psicoterapia/bert_hellinger", tags=["psicoterapia_grupo_avancada"])
router_bode_expiatorio_grup = APIRouter(prefix="/api/v1/psicoterapia/bode_expiatorio_grupo", tags=["psicoterapia_grupo_avancada"])
router_campo_morfogenetico = APIRouter(prefix="/api/v1/psicoterapia/campo_morfogenetico", tags=["psicoterapia_grupo_avancada"])
router_catarse_grupo = APIRouter(prefix="/api/v1/psicoterapia/catarse_grupo", tags=["psicoterapia_grupo_avancada"])
router_coesao_grupo = APIRouter(prefix="/api/v1/psicoterapia/coesao_grupo", tags=["psicoterapia_grupo_avancada"])
router_confidencialidade_gr = APIRouter(prefix="/api/v1/psicoterapia/confidencialidade_grupo", tags=["psicoterapia_grupo_avancada"])
router_conflito_grupo = APIRouter(prefix="/api/v1/psicoterapia/conflito_grupo", tags=["psicoterapia_grupo_avancada"])
router_constelacoes_familia = APIRouter(prefix="/api/v1/psicoterapia/constelacoes_familiares", tags=["psicoterapia_grupo_avancada"])
router_contrato_grupo = APIRouter(prefix="/api/v1/psicoterapia/contrato_grupo", tags=["psicoterapia_grupo_avancada"])
router_dissolucao_grupo = APIRouter(prefix="/api/v1/psicoterapia/dissolucao_grupo", tags=["psicoterapia_grupo_avancada"])
router_divisoes_grupo = APIRouter(prefix="/api/v1/psicoterapia/divisoes_grupo", tags=["psicoterapia_grupo_avancada"])
router_emaranhamentos = APIRouter(prefix="/api/v1/psicoterapia/emaranhamentos", tags=["psicoterapia_grupo_avancada"])
router_exclusao_membros = APIRouter(prefix="/api/v1/psicoterapia/exclusao_membros", tags=["psicoterapia_grupo_avancada"])
router_exclusoes = APIRouter(prefix="/api/v1/psicoterapia/exclusoes", tags=["psicoterapia_grupo_avancada"])
router_fases_grupo = APIRouter(prefix="/api/v1/psicoterapia/fases_grupo", tags=["psicoterapia_grupo_avancada"])
router_fatores_curativos = APIRouter(prefix="/api/v1/psicoterapia/fatores_curativos", tags=["psicoterapia_grupo_avancada"])
router_fatores_existenciais = APIRouter(prefix="/api/v1/psicoterapia/fatores_existenciais", tags=["psicoterapia_grupo_avancada"])
router_fenomenologia_sistem = APIRouter(prefix="/api/v1/psicoterapia/fenomenologia_sistemica", tags=["psicoterapia_grupo_avancada"])
router_formacao_grupo = APIRouter(prefix="/api/v1/psicoterapia/formacao_grupo", tags=["psicoterapia_grupo_avancada"])
router_grupo_aberto = APIRouter(prefix="/api/v1/psicoterapia/grupo_aberto", tags=["psicoterapia_grupo_avancada"])
router_grupo_encontro = APIRouter(prefix="/api/v1/psicoterapia/grupo_encontro", tags=["psicoterapia_grupo_avancada"])
router_grupo_fechado = APIRouter(prefix="/api/v1/psicoterapia/grupo_fechado", tags=["psicoterapia_grupo_avancada"])
router_grupo_heterogeneo = APIRouter(prefix="/api/v1/psicoterapia/grupo_heterogeneo", tags=["psicoterapia_grupo_avancada"])
router_grupo_hibrido = APIRouter(prefix="/api/v1/psicoterapia/grupo_hibrido", tags=["psicoterapia_grupo_avancada"])
router_grupo_homogeneo = APIRouter(prefix="/api/v1/psicoterapia/grupo_homogeneo", tags=["psicoterapia_grupo_avancada"])
router_grupo_online2 = APIRouter(prefix="/api/v1/psicoterapia/grupo_online2", tags=["psicoterapia_grupo_avancada"])
router_grupo_psicoeducativo = APIRouter(prefix="/api/v1/psicoterapia/grupo_psicoeducativo", tags=["psicoterapia_grupo_avancada"])
router_grupo_self_help = APIRouter(prefix="/api/v1/psicoterapia/grupo_self_help", tags=["psicoterapia_grupo_avancada"])
router_grupo_semi_aberto = APIRouter(prefix="/api/v1/psicoterapia/grupo_semi_aberto", tags=["psicoterapia_grupo_avancada"])
router_grupo_suporte = APIRouter(prefix="/api/v1/psicoterapia/grupo_suporte", tags=["psicoterapia_grupo_avancada"])
router_grupo_tarefa = APIRouter(prefix="/api/v1/psicoterapia/grupo_tarefa", tags=["psicoterapia_grupo_avancada"])
router_grupo_teleconferenci = APIRouter(prefix="/api/v1/psicoterapia/grupo_teleconferencia", tags=["psicoterapia_grupo_avancada"])
router_grupo_terapeutico = APIRouter(prefix="/api/v1/psicoterapia/grupo_terapeutico", tags=["psicoterapia_grupo_avancada"])
router_grupo_treinamento = APIRouter(prefix="/api/v1/psicoterapia/grupo_treinamento", tags=["psicoterapia_grupo_avancada"])
router_identificacoes_siste = APIRouter(prefix="/api/v1/psicoterapia/identificacoes_sistemicas", tags=["psicoterapia_grupo_avancada"])
router_informacao_grupo = APIRouter(prefix="/api/v1/psicoterapia/informacao_grupo", tags=["psicoterapia_grupo_avancada"])
router_instilacao_esperanca = APIRouter(prefix="/api/v1/psicoterapia/instilacao_esperanca", tags=["psicoterapia_grupo_avancada"])
router_lideranca_grupo = APIRouter(prefix="/api/v1/psicoterapia/lideranca_grupo", tags=["psicoterapia_grupo_avancada"])
router_lideres_co = APIRouter(prefix="/api/v1/psicoterapia/lideres_co", tags=["psicoterapia_grupo_avancada"])
router_limites_grupo = APIRouter(prefix="/api/v1/psicoterapia/limites_grupo", tags=["psicoterapia_grupo_avancada"])
router_lugares_sistemicos = APIRouter(prefix="/api/v1/psicoterapia/lugares_sistemicos", tags=["psicoterapia_grupo_avancada"])
router_membro_dependente = APIRouter(prefix="/api/v1/psicoterapia/membro_dependente", tags=["psicoterapia_grupo_avancada"])
router_membro_desafiador = APIRouter(prefix="/api/v1/psicoterapia/membro_desafiador", tags=["psicoterapia_grupo_avancada"])
router_membro_sedutor = APIRouter(prefix="/api/v1/psicoterapia/membro_sedutor", tags=["psicoterapia_grupo_avancada"])
router_membro_silencioso = APIRouter(prefix="/api/v1/psicoterapia/membro_silencioso", tags=["psicoterapia_grupo_avancada"])
router_monopolizador = APIRouter(prefix="/api/v1/psicoterapia/monopolizador", tags=["psicoterapia_grupo_avancada"])
router_movimentos_campo = APIRouter(prefix="/api/v1/psicoterapia/movimentos_campo", tags=["psicoterapia_grupo_avancada"])
router_movimentos_sistemico = APIRouter(prefix="/api/v1/psicoterapia/movimentos_sistemicos", tags=["psicoterapia_grupo_avancada"])
router_normatividade_grupo = APIRouter(prefix="/api/v1/psicoterapia/normatividade_grupo", tags=["psicoterapia_grupo_avancada"])
router_ordens_amor = APIRouter(prefix="/api/v1/psicoterapia/ordens_amor", tags=["psicoterapia_grupo_avancada"])
router_papeis_sistemicos = APIRouter(prefix="/api/v1/psicoterapia/papeis_sistemicos", tags=["psicoterapia_grupo_avancada"])
router_performance_grupo = APIRouter(prefix="/api/v1/psicoterapia/performance_grupo", tags=["psicoterapia_grupo_avancada"])
router_perspectiva_multiger = APIRouter(prefix="/api/v1/psicoterapia/perspectiva_multigeracion", tags=["psicoterapia_grupo_avancada"])
router_processo_grupo_conte = APIRouter(prefix="/api/v1/psicoterapia/processo_grupo_conteudo", tags=["psicoterapia_grupo_avancada"])
router_recapitulacao_famili = APIRouter(prefix="/api/v1/psicoterapia/recapitulacao_familiar", tags=["psicoterapia_grupo_avancada"])
router_regras_grupo = APIRouter(prefix="/api/v1/psicoterapia/regras_grupo", tags=["psicoterapia_grupo_avancada"])
router_representantes = APIRouter(prefix="/api/v1/psicoterapia/representantes", tags=["psicoterapia_grupo_avancada"])
router_ruptura_grupal = APIRouter(prefix="/api/v1/psicoterapia/ruptura_grupal", tags=["psicoterapia_grupo_avancada"])
router_selecao_membros = APIRouter(prefix="/api/v1/psicoterapia/selecao_membros", tags=["psicoterapia_grupo_avancada"])
router_sigilidade_grupo = APIRouter(prefix="/api/v1/psicoterapia/sigilidade_grupo", tags=["psicoterapia_grupo_avancada"])
router_subgrupos = APIRouter(prefix="/api/v1/psicoterapia/subgrupos", tags=["psicoterapia_grupo_avancada"])
router_tecnicas_socializaca = APIRouter(prefix="/api/v1/psicoterapia/tecnicas_socializacao", tags=["psicoterapia_grupo_avancada"])
router_tempestade_grupo = APIRouter(prefix="/api/v1/psicoterapia/tempestade_grupo", tags=["psicoterapia_grupo_avancada"])
router_triangulacao_grupo = APIRouter(prefix="/api/v1/psicoterapia/triangulacao_grupo", tags=["psicoterapia_grupo_avancada"])
router_tuckman_modelo = APIRouter(prefix="/api/v1/psicoterapia/tuckman_modelo", tags=["psicoterapia_grupo_avancada"])
router_universalidade = APIRouter(prefix="/api/v1/psicoterapia/universalidade", tags=["psicoterapia_grupo_avancada"])
router_yalom_terapia_grupo = APIRouter(prefix="/api/v1/psicoterapia/yalom_terapia_grupo", tags=["psicoterapia_grupo_avancada"])

@router_altruismo_grupo.get("")
async def i_altruismo_grupo():
    return {"p":"psicoterapia_gr_altruismo_grupo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ancestralidade_siste.get("")
async def i_ancestralidade_siste():
    return {"p":"psicoterapia_gr_ancestralidade_siste","s":"ativo","t":datetime.utcnow().isoformat()}
@router_aprendizado_imitativ.get("")
async def i_aprendizado_imitativ():
    return {"p":"psicoterapia_gr_aprendizado_imitativ","s":"ativo","t":datetime.utcnow().isoformat()}
@router_aqui_agora_grupo.get("")
async def i_aqui_agora_grupo():
    return {"p":"psicoterapia_gr_aqui_agora_grupo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bert_hellinger.get("")
async def i_bert_hellinger():
    return {"p":"psicoterapia_gr_bert_hellinger","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bode_expiatorio_grup.get("")
async def i_bode_expiatorio_grup():
    return {"p":"psicoterapia_gr_bode_expiatorio_grup","s":"ativo","t":datetime.utcnow().isoformat()}
@router_campo_morfogenetico.get("")
async def i_campo_morfogenetico():
    return {"p":"psicoterapia_gr_campo_morfogenetico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_catarse_grupo.get("")
async def i_catarse_grupo():
    return {"p":"psicoterapia_gr_catarse_grupo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_coesao_grupo.get("")
async def i_coesao_grupo():
    return {"p":"psicoterapia_gr_coesao_grupo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_confidencialidade_gr.get("")
async def i_confidencialidade_gr():
    return {"p":"psicoterapia_gr_confidencialidade_gr","s":"ativo","t":datetime.utcnow().isoformat()}
@router_conflito_grupo.get("")
async def i_conflito_grupo():
    return {"p":"psicoterapia_gr_conflito_grupo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_constelacoes_familia.get("")
async def i_constelacoes_familia():
    return {"p":"psicoterapia_gr_constelacoes_familia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_contrato_grupo.get("")
async def i_contrato_grupo():
    return {"p":"psicoterapia_gr_contrato_grupo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dissolucao_grupo.get("")
async def i_dissolucao_grupo():
    return {"p":"psicoterapia_gr_dissolucao_grupo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_divisoes_grupo.get("")
async def i_divisoes_grupo():
    return {"p":"psicoterapia_gr_divisoes_grupo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_emaranhamentos.get("")
async def i_emaranhamentos():
    return {"p":"psicoterapia_gr_emaranhamentos","s":"ativo","t":datetime.utcnow().isoformat()}
@router_exclusao_membros.get("")
async def i_exclusao_membros():
    return {"p":"psicoterapia_gr_exclusao_membros","s":"ativo","t":datetime.utcnow().isoformat()}
@router_exclusoes.get("")
async def i_exclusoes():
    return {"p":"psicoterapia_gr_exclusoes","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fases_grupo.get("")
async def i_fases_grupo():
    return {"p":"psicoterapia_gr_fases_grupo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fatores_curativos.get("")
async def i_fatores_curativos():
    return {"p":"psicoterapia_gr_fatores_curativos","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fatores_existenciais.get("")
async def i_fatores_existenciais():
    return {"p":"psicoterapia_gr_fatores_existenciais","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fenomenologia_sistem.get("")
async def i_fenomenologia_sistem():
    return {"p":"psicoterapia_gr_fenomenologia_sistem","s":"ativo","t":datetime.utcnow().isoformat()}
@router_formacao_grupo.get("")
async def i_formacao_grupo():
    return {"p":"psicoterapia_gr_formacao_grupo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grupo_aberto.get("")
async def i_grupo_aberto():
    return {"p":"psicoterapia_gr_grupo_aberto","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grupo_encontro.get("")
async def i_grupo_encontro():
    return {"p":"psicoterapia_gr_grupo_encontro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grupo_fechado.get("")
async def i_grupo_fechado():
    return {"p":"psicoterapia_gr_grupo_fechado","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grupo_heterogeneo.get("")
async def i_grupo_heterogeneo():
    return {"p":"psicoterapia_gr_grupo_heterogeneo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grupo_hibrido.get("")
async def i_grupo_hibrido():
    return {"p":"psicoterapia_gr_grupo_hibrido","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grupo_homogeneo.get("")
async def i_grupo_homogeneo():
    return {"p":"psicoterapia_gr_grupo_homogeneo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grupo_online2.get("")
async def i_grupo_online2():
    return {"p":"psicoterapia_gr_grupo_online2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grupo_psicoeducativo.get("")
async def i_grupo_psicoeducativo():
    return {"p":"psicoterapia_gr_grupo_psicoeducativo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grupo_self_help.get("")
async def i_grupo_self_help():
    return {"p":"psicoterapia_gr_grupo_self_help","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grupo_semi_aberto.get("")
async def i_grupo_semi_aberto():
    return {"p":"psicoterapia_gr_grupo_semi_aberto","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grupo_suporte.get("")
async def i_grupo_suporte():
    return {"p":"psicoterapia_gr_grupo_suporte","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grupo_tarefa.get("")
async def i_grupo_tarefa():
    return {"p":"psicoterapia_gr_grupo_tarefa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grupo_teleconferenci.get("")
async def i_grupo_teleconferenci():
    return {"p":"psicoterapia_gr_grupo_teleconferenci","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grupo_terapeutico.get("")
async def i_grupo_terapeutico():
    return {"p":"psicoterapia_gr_grupo_terapeutico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grupo_treinamento.get("")
async def i_grupo_treinamento():
    return {"p":"psicoterapia_gr_grupo_treinamento","s":"ativo","t":datetime.utcnow().isoformat()}
@router_identificacoes_siste.get("")
async def i_identificacoes_siste():
    return {"p":"psicoterapia_gr_identificacoes_siste","s":"ativo","t":datetime.utcnow().isoformat()}
@router_informacao_grupo.get("")
async def i_informacao_grupo():
    return {"p":"psicoterapia_gr_informacao_grupo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_instilacao_esperanca.get("")
async def i_instilacao_esperanca():
    return {"p":"psicoterapia_gr_instilacao_esperanca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lideranca_grupo.get("")
async def i_lideranca_grupo():
    return {"p":"psicoterapia_gr_lideranca_grupo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lideres_co.get("")
async def i_lideres_co():
    return {"p":"psicoterapia_gr_lideres_co","s":"ativo","t":datetime.utcnow().isoformat()}
@router_limites_grupo.get("")
async def i_limites_grupo():
    return {"p":"psicoterapia_gr_limites_grupo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lugares_sistemicos.get("")
async def i_lugares_sistemicos():
    return {"p":"psicoterapia_gr_lugares_sistemicos","s":"ativo","t":datetime.utcnow().isoformat()}
@router_membro_dependente.get("")
async def i_membro_dependente():
    return {"p":"psicoterapia_gr_membro_dependente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_membro_desafiador.get("")
async def i_membro_desafiador():
    return {"p":"psicoterapia_gr_membro_desafiador","s":"ativo","t":datetime.utcnow().isoformat()}
@router_membro_sedutor.get("")
async def i_membro_sedutor():
    return {"p":"psicoterapia_gr_membro_sedutor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_membro_silencioso.get("")
async def i_membro_silencioso():
    return {"p":"psicoterapia_gr_membro_silencioso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_monopolizador.get("")
async def i_monopolizador():
    return {"p":"psicoterapia_gr_monopolizador","s":"ativo","t":datetime.utcnow().isoformat()}
@router_movimentos_campo.get("")
async def i_movimentos_campo():
    return {"p":"psicoterapia_gr_movimentos_campo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_movimentos_sistemico.get("")
async def i_movimentos_sistemico():
    return {"p":"psicoterapia_gr_movimentos_sistemico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_normatividade_grupo.get("")
async def i_normatividade_grupo():
    return {"p":"psicoterapia_gr_normatividade_grupo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ordens_amor.get("")
async def i_ordens_amor():
    return {"p":"psicoterapia_gr_ordens_amor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_papeis_sistemicos.get("")
async def i_papeis_sistemicos():
    return {"p":"psicoterapia_gr_papeis_sistemicos","s":"ativo","t":datetime.utcnow().isoformat()}
@router_performance_grupo.get("")
async def i_performance_grupo():
    return {"p":"psicoterapia_gr_performance_grupo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_perspectiva_multiger.get("")
async def i_perspectiva_multiger():
    return {"p":"psicoterapia_gr_perspectiva_multiger","s":"ativo","t":datetime.utcnow().isoformat()}
@router_processo_grupo_conte.get("")
async def i_processo_grupo_conte():
    return {"p":"psicoterapia_gr_processo_grupo_conte","s":"ativo","t":datetime.utcnow().isoformat()}
@router_recapitulacao_famili.get("")
async def i_recapitulacao_famili():
    return {"p":"psicoterapia_gr_recapitulacao_famili","s":"ativo","t":datetime.utcnow().isoformat()}
@router_regras_grupo.get("")
async def i_regras_grupo():
    return {"p":"psicoterapia_gr_regras_grupo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_representantes.get("")
async def i_representantes():
    return {"p":"psicoterapia_gr_representantes","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ruptura_grupal.get("")
async def i_ruptura_grupal():
    return {"p":"psicoterapia_gr_ruptura_grupal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_selecao_membros.get("")
async def i_selecao_membros():
    return {"p":"psicoterapia_gr_selecao_membros","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sigilidade_grupo.get("")
async def i_sigilidade_grupo():
    return {"p":"psicoterapia_gr_sigilidade_grupo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_subgrupos.get("")
async def i_subgrupos():
    return {"p":"psicoterapia_gr_subgrupos","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tecnicas_socializaca.get("")
async def i_tecnicas_socializaca():
    return {"p":"psicoterapia_gr_tecnicas_socializaca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tempestade_grupo.get("")
async def i_tempestade_grupo():
    return {"p":"psicoterapia_gr_tempestade_grupo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_triangulacao_grupo.get("")
async def i_triangulacao_grupo():
    return {"p":"psicoterapia_gr_triangulacao_grupo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tuckman_modelo.get("")
async def i_tuckman_modelo():
    return {"p":"psicoterapia_gr_tuckman_modelo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_universalidade.get("")
async def i_universalidade():
    return {"p":"psicoterapia_gr_universalidade","s":"ativo","t":datetime.utcnow().isoformat()}
@router_yalom_terapia_grupo.get("")
async def i_yalom_terapia_grupo():
    return {"p":"psicoterapia_gr_yalom_terapia_grupo","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_psicoterapia_grupo_a(PluginBase):
    name = "consolidated_psicoterapia_grupo_avancada"
    def setup(self, app):
        app.include_router(router_altruismo_grupo)
        app.include_router(router_ancestralidade_siste)
        app.include_router(router_aprendizado_imitativ)
        app.include_router(router_aqui_agora_grupo)
        app.include_router(router_bert_hellinger)
        app.include_router(router_bode_expiatorio_grup)
        app.include_router(router_campo_morfogenetico)
        app.include_router(router_catarse_grupo)
        app.include_router(router_coesao_grupo)
        app.include_router(router_confidencialidade_gr)
        app.include_router(router_conflito_grupo)
        app.include_router(router_constelacoes_familia)
        app.include_router(router_contrato_grupo)
        app.include_router(router_dissolucao_grupo)
        app.include_router(router_divisoes_grupo)
        app.include_router(router_emaranhamentos)
        app.include_router(router_exclusao_membros)
        app.include_router(router_exclusoes)
        app.include_router(router_fases_grupo)
        app.include_router(router_fatores_curativos)
        app.include_router(router_fatores_existenciais)
        app.include_router(router_fenomenologia_sistem)
        app.include_router(router_formacao_grupo)
        app.include_router(router_grupo_aberto)
        app.include_router(router_grupo_encontro)
        app.include_router(router_grupo_fechado)
        app.include_router(router_grupo_heterogeneo)
        app.include_router(router_grupo_hibrido)
        app.include_router(router_grupo_homogeneo)
        app.include_router(router_grupo_online2)
        app.include_router(router_grupo_psicoeducativo)
        app.include_router(router_grupo_self_help)
        app.include_router(router_grupo_semi_aberto)
        app.include_router(router_grupo_suporte)
        app.include_router(router_grupo_tarefa)
        app.include_router(router_grupo_teleconferenci)
        app.include_router(router_grupo_terapeutico)
        app.include_router(router_grupo_treinamento)
        app.include_router(router_identificacoes_siste)
        app.include_router(router_informacao_grupo)
        app.include_router(router_instilacao_esperanca)
        app.include_router(router_lideranca_grupo)
        app.include_router(router_lideres_co)
        app.include_router(router_limites_grupo)
        app.include_router(router_lugares_sistemicos)
        app.include_router(router_membro_dependente)
        app.include_router(router_membro_desafiador)
        app.include_router(router_membro_sedutor)
        app.include_router(router_membro_silencioso)
        app.include_router(router_monopolizador)
        app.include_router(router_movimentos_campo)
        app.include_router(router_movimentos_sistemico)
        app.include_router(router_normatividade_grupo)
        app.include_router(router_ordens_amor)
        app.include_router(router_papeis_sistemicos)
        app.include_router(router_performance_grupo)
        app.include_router(router_perspectiva_multiger)
        app.include_router(router_processo_grupo_conte)
        app.include_router(router_recapitulacao_famili)
        app.include_router(router_regras_grupo)
        app.include_router(router_representantes)
        app.include_router(router_ruptura_grupal)
        app.include_router(router_selecao_membros)
        app.include_router(router_sigilidade_grupo)
        app.include_router(router_subgrupos)
        app.include_router(router_tecnicas_socializaca)
        app.include_router(router_tempestade_grupo)
        app.include_router(router_triangulacao_grupo)
        app.include_router(router_tuckman_modelo)
        app.include_router(router_universalidade)
        app.include_router(router_yalom_terapia_grupo)


plugin = Plugin_psicoterapia_grupo_a()
