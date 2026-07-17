from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_abstinencia_versus_r = APIRouter(prefix="/api/v1/saude_coleti/abstinencia_versus_reduca", tags=["saude_coletiva_mental"])
router_aceitabilidade_servi = APIRouter(prefix="/api/v1/saude_coleti/aceitabilidade_servico", tags=["saude_coletiva_mental"])
router_acessibilidade_servi = APIRouter(prefix="/api/v1/saude_coleti/acessibilidade_servico", tags=["saude_coletiva_mental"])
router_acesso_saude_mental = APIRouter(prefix="/api/v1/saude_coleti/acesso_saude_mental", tags=["saude_coletiva_mental"])
router_advocacy_saude_menta = APIRouter(prefix="/api/v1/saude_coleti/advocacy_saude_mental2", tags=["saude_coletiva_mental"])
router_advocacy_usuario = APIRouter(prefix="/api/v1/saude_coleti/advocacy_usuario", tags=["saude_coletiva_mental"])
router_agentes_comunitarios = APIRouter(prefix="/api/v1/saude_coleti/agentes_comunitarios", tags=["saude_coletiva_mental"])
router_anos_vida_perdidos = APIRouter(prefix="/api/v1/saude_coleti/anos_vida_perdidos", tags=["saude_coletiva_mental"])
router_barreira_acesso = APIRouter(prefix="/api/v1/saude_coleti/barreira_acesso", tags=["saude_coletiva_mental"])
router_carga_doenca_mental = APIRouter(prefix="/api/v1/saude_coleti/carga_doenca_mental", tags=["saude_coletiva_mental"])
router_cobertura_servico = APIRouter(prefix="/api/v1/saude_coleti/cobertura_servico", tags=["saude_coletiva_mental"])
router_comorbidade_mental = APIRouter(prefix="/api/v1/saude_coleti/comorbidade_mental", tags=["saude_coletiva_mental"])
router_cultural_barreira = APIRouter(prefix="/api/v1/saude_coleti/cultural_barreira", tags=["saude_coletiva_mental"])
router_daly_mental = APIRouter(prefix="/api/v1/saude_coleti/daly_mental", tags=["saude_coletiva_mental"])
router_deserto_mental = APIRouter(prefix="/api/v1/saude_coleti/deserto_mental", tags=["saude_coletiva_mental"])
router_determinante_social = APIRouter(prefix="/api/v1/saude_coleti/determinante_social", tags=["saude_coletiva_mental"])
router_disponibilidade_serv = APIRouter(prefix="/api/v1/saude_coleti/disponibilidade_servico", tags=["saude_coletiva_mental"])
router_distribuicao_profiss = APIRouter(prefix="/api/v1/saude_coleti/distribuicao_profissional", tags=["saude_coletiva_mental"])
router_efetividade_servico = APIRouter(prefix="/api/v1/saude_coleti/efetividade_servico", tags=["saude_coletiva_mental"])
router_eficiencia_servico = APIRouter(prefix="/api/v1/saude_coleti/eficiencia_servico", tags=["saude_coletiva_mental"])
router_epidemiologia_mental = APIRouter(prefix="/api/v1/saude_coleti/epidemiologia_mental", tags=["saude_coletiva_mental"])
router_estigma_barreira = APIRouter(prefix="/api/v1/saude_coleti/estigma_barreira", tags=["saude_coletiva_mental"])
router_fator_protecao_menta = APIRouter(prefix="/api/v1/saude_coleti/fator_protecao_mental", tags=["saude_coletiva_mental"])
router_fator_risco_mental = APIRouter(prefix="/api/v1/saude_coleti/fator_risco_mental", tags=["saude_coletiva_mental"])
router_financeiro_barreira = APIRouter(prefix="/api/v1/saude_coleti/financeiro_barreira", tags=["saude_coletiva_mental"])
router_financiamento_mental = APIRouter(prefix="/api/v1/saude_coleti/financiamento_mental", tags=["saude_coletiva_mental"])
router_formacao_profissiona = APIRouter(prefix="/api/v1/saude_coleti/formacao_profissional_men", tags=["saude_coletiva_mental"])
router_gap_tratamento = APIRouter(prefix="/api/v1/saude_coleti/gap_tratamento", tags=["saude_coletiva_mental"])
router_geografico_barreira = APIRouter(prefix="/api/v1/saude_coleti/geografico_barreira", tags=["saude_coletiva_mental"])
router_gradiente_social = APIRouter(prefix="/api/v1/saude_coleti/gradiente_social", tags=["saude_coletiva_mental"])
router_harm_reduction = APIRouter(prefix="/api/v1/saude_coleti/harm_reduction", tags=["saude_coletiva_mental"])
router_incidencia_transtorn = APIRouter(prefix="/api/v1/saude_coleti/incidencia_transtornos", tags=["saude_coletiva_mental"])
router_inequidade_saude = APIRouter(prefix="/api/v1/saude_coleti/inequidade_saude", tags=["saude_coletiva_mental"])
router_intervencao_gap = APIRouter(prefix="/api/v1/saude_coleti/intervencao_gap", tags=["saude_coletiva_mental"])
router_investimento_mental = APIRouter(prefix="/api/v1/saude_coleti/investimento_mental", tags=["saude_coletiva_mental"])
router_legislacao_mental = APIRouter(prefix="/api/v1/saude_coleti/legislacao_mental", tags=["saude_coletiva_mental"])
router_linguistico_barreira = APIRouter(prefix="/api/v1/saude_coleti/linguistico_barreira", tags=["saude_coletiva_mental"])
router_literacia_barreira = APIRouter(prefix="/api/v1/saude_coleti/literacia_barreira", tags=["saude_coletiva_mental"])
router_morbidade_mental = APIRouter(prefix="/api/v1/saude_coleti/morbidade_mental", tags=["saude_coletiva_mental"])
router_mortalidade_mental = APIRouter(prefix="/api/v1/saude_coleti/mortalidade_mental", tags=["saude_coletiva_mental"])
router_necessidade_nao_aten = APIRouter(prefix="/api/v1/saude_coleti/necessidade_nao_atendida", tags=["saude_coletiva_mental"])
router_orcamento_mental = APIRouter(prefix="/api/v1/saude_coleti/orcamento_mental", tags=["saude_coletiva_mental"])
router_participacao_social_ = APIRouter(prefix="/api/v1/saude_coleti/participacao_social_saude", tags=["saude_coletiva_mental"])
router_peer_support_paid = APIRouter(prefix="/api/v1/saude_coleti/peer_support_paid", tags=["saude_coletiva_mental"])
router_politica_publica_men = APIRouter(prefix="/api/v1/saude_coleti/politica_publica_mental", tags=["saude_coletiva_mental"])
router_prevalencia_transtor = APIRouter(prefix="/api/v1/saude_coleti/prevalencia_transtornos", tags=["saude_coletiva_mental"])
router_prevention_gap = APIRouter(prefix="/api/v1/saude_coleti/prevention_gap", tags=["saude_coletiva_mental"])
router_qualidade_servico = APIRouter(prefix="/api/v1/saude_coleti/qualidade_servico", tags=["saude_coletiva_mental"])
router_recovery_movement = APIRouter(prefix="/api/v1/saude_coleti/recovery_movement", tags=["saude_coletiva_mental"])
router_recuperacao_orientad = APIRouter(prefix="/api/v1/saude_coleti/recuperacao_orientada", tags=["saude_coletiva_mental"])
router_recursos_humanos_men = APIRouter(prefix="/api/v1/saude_coleti/recursos_humanos_mental", tags=["saude_coletiva_mental"])
router_reducao_danos_mental = APIRouter(prefix="/api/v1/saude_coleti/reducao_danos_mental", tags=["saude_coletiva_mental"])
router_regiao_sem_psicologo = APIRouter(prefix="/api/v1/saude_coleti/regiao_sem_psicologo", tags=["saude_coletiva_mental"])
router_task_shifting_mental = APIRouter(prefix="/api/v1/saude_coleti/task_shifting_mental", tags=["saude_coletiva_mental"])
router_telepsicologia_acess = APIRouter(prefix="/api/v1/saude_coleti/telepsicologia_acesso", tags=["saude_coletiva_mental"])
router_treatment_gap = APIRouter(prefix="/api/v1/saude_coleti/treatment_gap", tags=["saude_coletiva_mental"])
router_usuario_protagonista = APIRouter(prefix="/api/v1/saude_coleti/usuario_protagonista", tags=["saude_coletiva_mental"])
router_utilizacao_servico = APIRouter(prefix="/api/v1/saude_coleti/utilizacao_servico", tags=["saude_coletiva_mental"])
router_yld_mental = APIRouter(prefix="/api/v1/saude_coleti/yld_mental", tags=["saude_coletiva_mental"])
router_yll_mental = APIRouter(prefix="/api/v1/saude_coleti/yll_mental", tags=["saude_coletiva_mental"])

@router_abstinencia_versus_r.get("")
async def i_abstinencia_versus_r():
    return {"p":"saude_coletiva__abstinencia_versus_r","s":"ativo","t":datetime.utcnow().isoformat()}
@router_aceitabilidade_servi.get("")
async def i_aceitabilidade_servi():
    return {"p":"saude_coletiva__aceitabilidade_servi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_acessibilidade_servi.get("")
async def i_acessibilidade_servi():
    return {"p":"saude_coletiva__acessibilidade_servi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_acesso_saude_mental.get("")
async def i_acesso_saude_mental():
    return {"p":"saude_coletiva__acesso_saude_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_advocacy_saude_menta.get("")
async def i_advocacy_saude_menta():
    return {"p":"saude_coletiva__advocacy_saude_menta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_advocacy_usuario.get("")
async def i_advocacy_usuario():
    return {"p":"saude_coletiva__advocacy_usuario","s":"ativo","t":datetime.utcnow().isoformat()}
@router_agentes_comunitarios.get("")
async def i_agentes_comunitarios():
    return {"p":"saude_coletiva__agentes_comunitarios","s":"ativo","t":datetime.utcnow().isoformat()}
@router_anos_vida_perdidos.get("")
async def i_anos_vida_perdidos():
    return {"p":"saude_coletiva__anos_vida_perdidos","s":"ativo","t":datetime.utcnow().isoformat()}
@router_barreira_acesso.get("")
async def i_barreira_acesso():
    return {"p":"saude_coletiva__barreira_acesso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_carga_doenca_mental.get("")
async def i_carga_doenca_mental():
    return {"p":"saude_coletiva__carga_doenca_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cobertura_servico.get("")
async def i_cobertura_servico():
    return {"p":"saude_coletiva__cobertura_servico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_comorbidade_mental.get("")
async def i_comorbidade_mental():
    return {"p":"saude_coletiva__comorbidade_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cultural_barreira.get("")
async def i_cultural_barreira():
    return {"p":"saude_coletiva__cultural_barreira","s":"ativo","t":datetime.utcnow().isoformat()}
@router_daly_mental.get("")
async def i_daly_mental():
    return {"p":"saude_coletiva__daly_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_deserto_mental.get("")
async def i_deserto_mental():
    return {"p":"saude_coletiva__deserto_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_determinante_social.get("")
async def i_determinante_social():
    return {"p":"saude_coletiva__determinante_social","s":"ativo","t":datetime.utcnow().isoformat()}
@router_disponibilidade_serv.get("")
async def i_disponibilidade_serv():
    return {"p":"saude_coletiva__disponibilidade_serv","s":"ativo","t":datetime.utcnow().isoformat()}
@router_distribuicao_profiss.get("")
async def i_distribuicao_profiss():
    return {"p":"saude_coletiva__distribuicao_profiss","s":"ativo","t":datetime.utcnow().isoformat()}
@router_efetividade_servico.get("")
async def i_efetividade_servico():
    return {"p":"saude_coletiva__efetividade_servico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_eficiencia_servico.get("")
async def i_eficiencia_servico():
    return {"p":"saude_coletiva__eficiencia_servico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_epidemiologia_mental.get("")
async def i_epidemiologia_mental():
    return {"p":"saude_coletiva__epidemiologia_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_estigma_barreira.get("")
async def i_estigma_barreira():
    return {"p":"saude_coletiva__estigma_barreira","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fator_protecao_menta.get("")
async def i_fator_protecao_menta():
    return {"p":"saude_coletiva__fator_protecao_menta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fator_risco_mental.get("")
async def i_fator_risco_mental():
    return {"p":"saude_coletiva__fator_risco_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_financeiro_barreira.get("")
async def i_financeiro_barreira():
    return {"p":"saude_coletiva__financeiro_barreira","s":"ativo","t":datetime.utcnow().isoformat()}
@router_financiamento_mental.get("")
async def i_financiamento_mental():
    return {"p":"saude_coletiva__financiamento_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_formacao_profissiona.get("")
async def i_formacao_profissiona():
    return {"p":"saude_coletiva__formacao_profissiona","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gap_tratamento.get("")
async def i_gap_tratamento():
    return {"p":"saude_coletiva__gap_tratamento","s":"ativo","t":datetime.utcnow().isoformat()}
@router_geografico_barreira.get("")
async def i_geografico_barreira():
    return {"p":"saude_coletiva__geografico_barreira","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gradiente_social.get("")
async def i_gradiente_social():
    return {"p":"saude_coletiva__gradiente_social","s":"ativo","t":datetime.utcnow().isoformat()}
@router_harm_reduction.get("")
async def i_harm_reduction():
    return {"p":"saude_coletiva__harm_reduction","s":"ativo","t":datetime.utcnow().isoformat()}
@router_incidencia_transtorn.get("")
async def i_incidencia_transtorn():
    return {"p":"saude_coletiva__incidencia_transtorn","s":"ativo","t":datetime.utcnow().isoformat()}
@router_inequidade_saude.get("")
async def i_inequidade_saude():
    return {"p":"saude_coletiva__inequidade_saude","s":"ativo","t":datetime.utcnow().isoformat()}
@router_intervencao_gap.get("")
async def i_intervencao_gap():
    return {"p":"saude_coletiva__intervencao_gap","s":"ativo","t":datetime.utcnow().isoformat()}
@router_investimento_mental.get("")
async def i_investimento_mental():
    return {"p":"saude_coletiva__investimento_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_legislacao_mental.get("")
async def i_legislacao_mental():
    return {"p":"saude_coletiva__legislacao_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_linguistico_barreira.get("")
async def i_linguistico_barreira():
    return {"p":"saude_coletiva__linguistico_barreira","s":"ativo","t":datetime.utcnow().isoformat()}
@router_literacia_barreira.get("")
async def i_literacia_barreira():
    return {"p":"saude_coletiva__literacia_barreira","s":"ativo","t":datetime.utcnow().isoformat()}
@router_morbidade_mental.get("")
async def i_morbidade_mental():
    return {"p":"saude_coletiva__morbidade_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mortalidade_mental.get("")
async def i_mortalidade_mental():
    return {"p":"saude_coletiva__mortalidade_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_necessidade_nao_aten.get("")
async def i_necessidade_nao_aten():
    return {"p":"saude_coletiva__necessidade_nao_aten","s":"ativo","t":datetime.utcnow().isoformat()}
@router_orcamento_mental.get("")
async def i_orcamento_mental():
    return {"p":"saude_coletiva__orcamento_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_participacao_social_.get("")
async def i_participacao_social_():
    return {"p":"saude_coletiva__participacao_social_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_peer_support_paid.get("")
async def i_peer_support_paid():
    return {"p":"saude_coletiva__peer_support_paid","s":"ativo","t":datetime.utcnow().isoformat()}
@router_politica_publica_men.get("")
async def i_politica_publica_men():
    return {"p":"saude_coletiva__politica_publica_men","s":"ativo","t":datetime.utcnow().isoformat()}
@router_prevalencia_transtor.get("")
async def i_prevalencia_transtor():
    return {"p":"saude_coletiva__prevalencia_transtor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_prevention_gap.get("")
async def i_prevention_gap():
    return {"p":"saude_coletiva__prevention_gap","s":"ativo","t":datetime.utcnow().isoformat()}
@router_qualidade_servico.get("")
async def i_qualidade_servico():
    return {"p":"saude_coletiva__qualidade_servico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_recovery_movement.get("")
async def i_recovery_movement():
    return {"p":"saude_coletiva__recovery_movement","s":"ativo","t":datetime.utcnow().isoformat()}
@router_recuperacao_orientad.get("")
async def i_recuperacao_orientad():
    return {"p":"saude_coletiva__recuperacao_orientad","s":"ativo","t":datetime.utcnow().isoformat()}
@router_recursos_humanos_men.get("")
async def i_recursos_humanos_men():
    return {"p":"saude_coletiva__recursos_humanos_men","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reducao_danos_mental.get("")
async def i_reducao_danos_mental():
    return {"p":"saude_coletiva__reducao_danos_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_regiao_sem_psicologo.get("")
async def i_regiao_sem_psicologo():
    return {"p":"saude_coletiva__regiao_sem_psicologo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_task_shifting_mental.get("")
async def i_task_shifting_mental():
    return {"p":"saude_coletiva__task_shifting_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_telepsicologia_acess.get("")
async def i_telepsicologia_acess():
    return {"p":"saude_coletiva__telepsicologia_acess","s":"ativo","t":datetime.utcnow().isoformat()}
@router_treatment_gap.get("")
async def i_treatment_gap():
    return {"p":"saude_coletiva__treatment_gap","s":"ativo","t":datetime.utcnow().isoformat()}
@router_usuario_protagonista.get("")
async def i_usuario_protagonista():
    return {"p":"saude_coletiva__usuario_protagonista","s":"ativo","t":datetime.utcnow().isoformat()}
@router_utilizacao_servico.get("")
async def i_utilizacao_servico():
    return {"p":"saude_coletiva__utilizacao_servico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_yld_mental.get("")
async def i_yld_mental():
    return {"p":"saude_coletiva__yld_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_yll_mental.get("")
async def i_yll_mental():
    return {"p":"saude_coletiva__yll_mental","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_saude_coletiva_menta(PluginBase):
    name = "consolidated_saude_coletiva_mental"
    def setup(self, app):
        app.include_router(router_abstinencia_versus_r)
        app.include_router(router_aceitabilidade_servi)
        app.include_router(router_acessibilidade_servi)
        app.include_router(router_acesso_saude_mental)
        app.include_router(router_advocacy_saude_menta)
        app.include_router(router_advocacy_usuario)
        app.include_router(router_agentes_comunitarios)
        app.include_router(router_anos_vida_perdidos)
        app.include_router(router_barreira_acesso)
        app.include_router(router_carga_doenca_mental)
        app.include_router(router_cobertura_servico)
        app.include_router(router_comorbidade_mental)
        app.include_router(router_cultural_barreira)
        app.include_router(router_daly_mental)
        app.include_router(router_deserto_mental)
        app.include_router(router_determinante_social)
        app.include_router(router_disponibilidade_serv)
        app.include_router(router_distribuicao_profiss)
        app.include_router(router_efetividade_servico)
        app.include_router(router_eficiencia_servico)
        app.include_router(router_epidemiologia_mental)
        app.include_router(router_estigma_barreira)
        app.include_router(router_fator_protecao_menta)
        app.include_router(router_fator_risco_mental)
        app.include_router(router_financeiro_barreira)
        app.include_router(router_financiamento_mental)
        app.include_router(router_formacao_profissiona)
        app.include_router(router_gap_tratamento)
        app.include_router(router_geografico_barreira)
        app.include_router(router_gradiente_social)
        app.include_router(router_harm_reduction)
        app.include_router(router_incidencia_transtorn)
        app.include_router(router_inequidade_saude)
        app.include_router(router_intervencao_gap)
        app.include_router(router_investimento_mental)
        app.include_router(router_legislacao_mental)
        app.include_router(router_linguistico_barreira)
        app.include_router(router_literacia_barreira)
        app.include_router(router_morbidade_mental)
        app.include_router(router_mortalidade_mental)
        app.include_router(router_necessidade_nao_aten)
        app.include_router(router_orcamento_mental)
        app.include_router(router_participacao_social_)
        app.include_router(router_peer_support_paid)
        app.include_router(router_politica_publica_men)
        app.include_router(router_prevalencia_transtor)
        app.include_router(router_prevention_gap)
        app.include_router(router_qualidade_servico)
        app.include_router(router_recovery_movement)
        app.include_router(router_recuperacao_orientad)
        app.include_router(router_recursos_humanos_men)
        app.include_router(router_reducao_danos_mental)
        app.include_router(router_regiao_sem_psicologo)
        app.include_router(router_task_shifting_mental)
        app.include_router(router_telepsicologia_acess)
        app.include_router(router_treatment_gap)
        app.include_router(router_usuario_protagonista)
        app.include_router(router_utilizacao_servico)
        app.include_router(router_yld_mental)
        app.include_router(router_yll_mental)


plugin = Plugin_saude_coletiva_menta()
