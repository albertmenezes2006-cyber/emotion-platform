from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_aluguel_consultorio = APIRouter(prefix="/api/v1/financeiro_s/aluguel_consultorio", tags=["financeiro_saude_clinico"])
router_assinaturas_clinica = APIRouter(prefix="/api/v1/financeiro_s/assinaturas_clinica", tags=["financeiro_saude_clinico"])
router_atendimento_social = APIRouter(prefix="/api/v1/financeiro_s/atendimento_social", tags=["financeiro_saude_clinico"])
router_bndes_saude = APIRouter(prefix="/api/v1/financeiro_s/bndes_saude", tags=["financeiro_saude_clinico"])
router_cbhpm_psicologia = APIRouter(prefix="/api/v1/financeiro_s/cbhpm_psicologia", tags=["financeiro_saude_clinico"])
router_clinica_domiciliar = APIRouter(prefix="/api/v1/financeiro_s/clinica_domiciliar", tags=["financeiro_saude_clinico"])
router_cnpj_clinica = APIRouter(prefix="/api/v1/financeiro_s/cnpj_clinica", tags=["financeiro_saude_clinico"])
router_consultoria_receita = APIRouter(prefix="/api/v1/financeiro_s/consultoria_receita", tags=["financeiro_saude_clinico"])
router_convenio_psicologia = APIRouter(prefix="/api/v1/financeiro_s/convenio_psicologia", tags=["financeiro_saude_clinico"])
router_cooperativa_psicolog = APIRouter(prefix="/api/v1/financeiro_s/cooperativa_psicologia", tags=["financeiro_saude_clinico"])
router_coworking_clinico = APIRouter(prefix="/api/v1/financeiro_s/coworking_clinico", tags=["financeiro_saude_clinico"])
router_credenciamento_plano = APIRouter(prefix="/api/v1/financeiro_s/credenciamento_plano", tags=["financeiro_saude_clinico"])
router_crescimento_receita_ = APIRouter(prefix="/api/v1/financeiro_s/crescimento_receita_clini", tags=["financeiro_saude_clinico"])
router_curso_online_receita = APIRouter(prefix="/api/v1/financeiro_s/curso_online_receita", tags=["financeiro_saude_clinico"])
router_deducao_ir_psicologo = APIRouter(prefix="/api/v1/financeiro_s/deducao_ir_psicologo", tags=["financeiro_saude_clinico"])
router_descredenciamento_pl = APIRouter(prefix="/api/v1/financeiro_s/descredenciamento_plano", tags=["financeiro_saude_clinico"])
router_diversificacao_recei = APIRouter(prefix="/api/v1/financeiro_s/diversificacao_receita", tags=["financeiro_saude_clinico"])
router_dre_clinica = APIRouter(prefix="/api/v1/financeiro_s/dre_clinica", tags=["financeiro_saude_clinico"])
router_eireli = APIRouter(prefix="/api/v1/financeiro_s/eireli", tags=["financeiro_saude_clinico"])
router_emprestimo_clinica = APIRouter(prefix="/api/v1/financeiro_s/emprestimo_clinica", tags=["financeiro_saude_clinico"])
router_equipamentos_clinica = APIRouter(prefix="/api/v1/financeiro_s/equipamentos_clinica", tags=["financeiro_saude_clinico"])
router_fluxo_caixa_clinica = APIRouter(prefix="/api/v1/financeiro_s/fluxo_caixa_clinica", tags=["financeiro_saude_clinico"])
router_fomento_saude = APIRouter(prefix="/api/v1/financeiro_s/fomento_saude", tags=["financeiro_saude_clinico"])
router_franquia_clinica = APIRouter(prefix="/api/v1/financeiro_s/franquia_clinica", tags=["financeiro_saude_clinico"])
router_glosa_plano_saude = APIRouter(prefix="/api/v1/financeiro_s/glosa_plano_saude", tags=["financeiro_saude_clinico"])
router_home_office_clinico = APIRouter(prefix="/api/v1/financeiro_s/home_office_clinico", tags=["financeiro_saude_clinico"])
router_honorarios_plano_sau = APIRouter(prefix="/api/v1/financeiro_s/honorarios_plano_saude", tags=["financeiro_saude_clinico"])
router_investimento_clinica = APIRouter(prefix="/api/v1/financeiro_s/investimento_clinica", tags=["financeiro_saude_clinico"])
router_ir_psicologia = APIRouter(prefix="/api/v1/financeiro_s/ir_psicologia", tags=["financeiro_saude_clinico"])
router_iss_psicologia = APIRouter(prefix="/api/v1/financeiro_s/iss_psicologia", tags=["financeiro_saude_clinico"])
router_livro_psicologia = APIRouter(prefix="/api/v1/financeiro_s/livro_psicologia", tags=["financeiro_saude_clinico"])
router_ltda_clinica = APIRouter(prefix="/api/v1/financeiro_s/ltda_clinica", tags=["financeiro_saude_clinico"])
router_margem_lucro_clinica = APIRouter(prefix="/api/v1/financeiro_s/margem_lucro_clinica", tags=["financeiro_saude_clinico"])
router_marketing_custos = APIRouter(prefix="/api/v1/financeiro_s/marketing_custos", tags=["financeiro_saude_clinico"])
router_materiais_clinica = APIRouter(prefix="/api/v1/financeiro_s/materiais_clinica", tags=["financeiro_saude_clinico"])
router_mei_psicologia = APIRouter(prefix="/api/v1/financeiro_s/mei_psicologia", tags=["financeiro_saude_clinico"])
router_mentoria_receita = APIRouter(prefix="/api/v1/financeiro_s/mentoria_receita", tags=["financeiro_saude_clinico"])
router_negociacao_plano_sau = APIRouter(prefix="/api/v1/financeiro_s/negociacao_plano_saude", tags=["financeiro_saude_clinico"])
router_nf_psicologia = APIRouter(prefix="/api/v1/financeiro_s/nf_psicologia", tags=["financeiro_saude_clinico"])
router_nota_fiscal_autonomo = APIRouter(prefix="/api/v1/financeiro_s/nota_fiscal_autonomo", tags=["financeiro_saude_clinico"])
router_palestra_receita = APIRouter(prefix="/api/v1/financeiro_s/palestra_receita", tags=["financeiro_saude_clinico"])
router_particular_precifica = APIRouter(prefix="/api/v1/financeiro_s/particular_precificacao", tags=["financeiro_saude_clinico"])
router_passivo_psicologia = APIRouter(prefix="/api/v1/financeiro_s/passivo_psicologia", tags=["financeiro_saude_clinico"])
router_payback_clinica = APIRouter(prefix="/api/v1/financeiro_s/payback_clinica", tags=["financeiro_saude_clinico"])
router_planilha_financeiro_ = APIRouter(prefix="/api/v1/financeiro_s/planilha_financeiro_clini", tags=["financeiro_saude_clinico"])
router_planilha_honorarios = APIRouter(prefix="/api/v1/financeiro_s/planilha_honorarios", tags=["financeiro_saude_clinico"])
router_ponto_equilibrio_cli = APIRouter(prefix="/api/v1/financeiro_s/ponto_equilibrio_clinica", tags=["financeiro_saude_clinico"])
router_precificacao_psicolo = APIRouter(prefix="/api/v1/financeiro_s/precificacao_psicologia", tags=["financeiro_saude_clinico"])
router_pro_bono_psicologia = APIRouter(prefix="/api/v1/financeiro_s/pro_bono_psicologia", tags=["financeiro_saude_clinico"])
router_publicidade_clinica = APIRouter(prefix="/api/v1/financeiro_s/publicidade_clinica", tags=["financeiro_saude_clinico"])
router_recurso_glosa = APIRouter(prefix="/api/v1/financeiro_s/recurso_glosa", tags=["financeiro_saude_clinico"])
router_redes_sociais_custo = APIRouter(prefix="/api/v1/financeiro_s/redes_sociais_custo", tags=["financeiro_saude_clinico"])
router_reembolso_plano = APIRouter(prefix="/api/v1/financeiro_s/reembolso_plano", tags=["financeiro_saude_clinico"])
router_roi_clinica = APIRouter(prefix="/api/v1/financeiro_s/roi_clinica", tags=["financeiro_saude_clinico"])
router_sa_clinica = APIRouter(prefix="/api/v1/financeiro_s/sa_clinica", tags=["financeiro_saude_clinico"])
router_sliding_scale_psicol = APIRouter(prefix="/api/v1/financeiro_s/sliding_scale_psicologia", tags=["financeiro_saude_clinico"])
router_softwares_clinica = APIRouter(prefix="/api/v1/financeiro_s/softwares_clinica", tags=["financeiro_saude_clinico"])
router_supervise_receita = APIRouter(prefix="/api/v1/financeiro_s/supervise_receita", tags=["financeiro_saude_clinico"])
router_tabela_cfp_honorario = APIRouter(prefix="/api/v1/financeiro_s/tabela_cfp_honorarios", tags=["financeiro_saude_clinico"])
router_tuss_psicologia = APIRouter(prefix="/api/v1/financeiro_s/tuss_psicologia", tags=["financeiro_saude_clinico"])
router_valor_hora_psicologi = APIRouter(prefix="/api/v1/financeiro_s/valor_hora_psicologia", tags=["financeiro_saude_clinico"])
router_valor_minimo_etico = APIRouter(prefix="/api/v1/financeiro_s/valor_minimo_etico", tags=["financeiro_saude_clinico"])
router_website_clinica = APIRouter(prefix="/api/v1/financeiro_s/website_clinica", tags=["financeiro_saude_clinico"])
router_workshop_receita = APIRouter(prefix="/api/v1/financeiro_s/workshop_receita", tags=["financeiro_saude_clinico"])

@router_aluguel_consultorio.get("")
async def i_aluguel_consultorio():
    return {"p":"financeiro_saud_aluguel_consultorio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_assinaturas_clinica.get("")
async def i_assinaturas_clinica():
    return {"p":"financeiro_saud_assinaturas_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_atendimento_social.get("")
async def i_atendimento_social():
    return {"p":"financeiro_saud_atendimento_social","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bndes_saude.get("")
async def i_bndes_saude():
    return {"p":"financeiro_saud_bndes_saude","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cbhpm_psicologia.get("")
async def i_cbhpm_psicologia():
    return {"p":"financeiro_saud_cbhpm_psicologia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_clinica_domiciliar.get("")
async def i_clinica_domiciliar():
    return {"p":"financeiro_saud_clinica_domiciliar","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cnpj_clinica.get("")
async def i_cnpj_clinica():
    return {"p":"financeiro_saud_cnpj_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_consultoria_receita.get("")
async def i_consultoria_receita():
    return {"p":"financeiro_saud_consultoria_receita","s":"ativo","t":datetime.utcnow().isoformat()}
@router_convenio_psicologia.get("")
async def i_convenio_psicologia():
    return {"p":"financeiro_saud_convenio_psicologia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cooperativa_psicolog.get("")
async def i_cooperativa_psicolog():
    return {"p":"financeiro_saud_cooperativa_psicolog","s":"ativo","t":datetime.utcnow().isoformat()}
@router_coworking_clinico.get("")
async def i_coworking_clinico():
    return {"p":"financeiro_saud_coworking_clinico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_credenciamento_plano.get("")
async def i_credenciamento_plano():
    return {"p":"financeiro_saud_credenciamento_plano","s":"ativo","t":datetime.utcnow().isoformat()}
@router_crescimento_receita_.get("")
async def i_crescimento_receita_():
    return {"p":"financeiro_saud_crescimento_receita_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_curso_online_receita.get("")
async def i_curso_online_receita():
    return {"p":"financeiro_saud_curso_online_receita","s":"ativo","t":datetime.utcnow().isoformat()}
@router_deducao_ir_psicologo.get("")
async def i_deducao_ir_psicologo():
    return {"p":"financeiro_saud_deducao_ir_psicologo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_descredenciamento_pl.get("")
async def i_descredenciamento_pl():
    return {"p":"financeiro_saud_descredenciamento_pl","s":"ativo","t":datetime.utcnow().isoformat()}
@router_diversificacao_recei.get("")
async def i_diversificacao_recei():
    return {"p":"financeiro_saud_diversificacao_recei","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dre_clinica.get("")
async def i_dre_clinica():
    return {"p":"financeiro_saud_dre_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_eireli.get("")
async def i_eireli():
    return {"p":"financeiro_saud_eireli","s":"ativo","t":datetime.utcnow().isoformat()}
@router_emprestimo_clinica.get("")
async def i_emprestimo_clinica():
    return {"p":"financeiro_saud_emprestimo_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_equipamentos_clinica.get("")
async def i_equipamentos_clinica():
    return {"p":"financeiro_saud_equipamentos_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fluxo_caixa_clinica.get("")
async def i_fluxo_caixa_clinica():
    return {"p":"financeiro_saud_fluxo_caixa_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fomento_saude.get("")
async def i_fomento_saude():
    return {"p":"financeiro_saud_fomento_saude","s":"ativo","t":datetime.utcnow().isoformat()}
@router_franquia_clinica.get("")
async def i_franquia_clinica():
    return {"p":"financeiro_saud_franquia_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_glosa_plano_saude.get("")
async def i_glosa_plano_saude():
    return {"p":"financeiro_saud_glosa_plano_saude","s":"ativo","t":datetime.utcnow().isoformat()}
@router_home_office_clinico.get("")
async def i_home_office_clinico():
    return {"p":"financeiro_saud_home_office_clinico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_honorarios_plano_sau.get("")
async def i_honorarios_plano_sau():
    return {"p":"financeiro_saud_honorarios_plano_sau","s":"ativo","t":datetime.utcnow().isoformat()}
@router_investimento_clinica.get("")
async def i_investimento_clinica():
    return {"p":"financeiro_saud_investimento_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ir_psicologia.get("")
async def i_ir_psicologia():
    return {"p":"financeiro_saud_ir_psicologia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_iss_psicologia.get("")
async def i_iss_psicologia():
    return {"p":"financeiro_saud_iss_psicologia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_livro_psicologia.get("")
async def i_livro_psicologia():
    return {"p":"financeiro_saud_livro_psicologia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ltda_clinica.get("")
async def i_ltda_clinica():
    return {"p":"financeiro_saud_ltda_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_margem_lucro_clinica.get("")
async def i_margem_lucro_clinica():
    return {"p":"financeiro_saud_margem_lucro_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_marketing_custos.get("")
async def i_marketing_custos():
    return {"p":"financeiro_saud_marketing_custos","s":"ativo","t":datetime.utcnow().isoformat()}
@router_materiais_clinica.get("")
async def i_materiais_clinica():
    return {"p":"financeiro_saud_materiais_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mei_psicologia.get("")
async def i_mei_psicologia():
    return {"p":"financeiro_saud_mei_psicologia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mentoria_receita.get("")
async def i_mentoria_receita():
    return {"p":"financeiro_saud_mentoria_receita","s":"ativo","t":datetime.utcnow().isoformat()}
@router_negociacao_plano_sau.get("")
async def i_negociacao_plano_sau():
    return {"p":"financeiro_saud_negociacao_plano_sau","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nf_psicologia.get("")
async def i_nf_psicologia():
    return {"p":"financeiro_saud_nf_psicologia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nota_fiscal_autonomo.get("")
async def i_nota_fiscal_autonomo():
    return {"p":"financeiro_saud_nota_fiscal_autonomo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_palestra_receita.get("")
async def i_palestra_receita():
    return {"p":"financeiro_saud_palestra_receita","s":"ativo","t":datetime.utcnow().isoformat()}
@router_particular_precifica.get("")
async def i_particular_precifica():
    return {"p":"financeiro_saud_particular_precifica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_passivo_psicologia.get("")
async def i_passivo_psicologia():
    return {"p":"financeiro_saud_passivo_psicologia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_payback_clinica.get("")
async def i_payback_clinica():
    return {"p":"financeiro_saud_payback_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_planilha_financeiro_.get("")
async def i_planilha_financeiro_():
    return {"p":"financeiro_saud_planilha_financeiro_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_planilha_honorarios.get("")
async def i_planilha_honorarios():
    return {"p":"financeiro_saud_planilha_honorarios","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ponto_equilibrio_cli.get("")
async def i_ponto_equilibrio_cli():
    return {"p":"financeiro_saud_ponto_equilibrio_cli","s":"ativo","t":datetime.utcnow().isoformat()}
@router_precificacao_psicolo.get("")
async def i_precificacao_psicolo():
    return {"p":"financeiro_saud_precificacao_psicolo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pro_bono_psicologia.get("")
async def i_pro_bono_psicologia():
    return {"p":"financeiro_saud_pro_bono_psicologia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_publicidade_clinica.get("")
async def i_publicidade_clinica():
    return {"p":"financeiro_saud_publicidade_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_recurso_glosa.get("")
async def i_recurso_glosa():
    return {"p":"financeiro_saud_recurso_glosa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_redes_sociais_custo.get("")
async def i_redes_sociais_custo():
    return {"p":"financeiro_saud_redes_sociais_custo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reembolso_plano.get("")
async def i_reembolso_plano():
    return {"p":"financeiro_saud_reembolso_plano","s":"ativo","t":datetime.utcnow().isoformat()}
@router_roi_clinica.get("")
async def i_roi_clinica():
    return {"p":"financeiro_saud_roi_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sa_clinica.get("")
async def i_sa_clinica():
    return {"p":"financeiro_saud_sa_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sliding_scale_psicol.get("")
async def i_sliding_scale_psicol():
    return {"p":"financeiro_saud_sliding_scale_psicol","s":"ativo","t":datetime.utcnow().isoformat()}
@router_softwares_clinica.get("")
async def i_softwares_clinica():
    return {"p":"financeiro_saud_softwares_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_supervise_receita.get("")
async def i_supervise_receita():
    return {"p":"financeiro_saud_supervise_receita","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tabela_cfp_honorario.get("")
async def i_tabela_cfp_honorario():
    return {"p":"financeiro_saud_tabela_cfp_honorario","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tuss_psicologia.get("")
async def i_tuss_psicologia():
    return {"p":"financeiro_saud_tuss_psicologia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_valor_hora_psicologi.get("")
async def i_valor_hora_psicologi():
    return {"p":"financeiro_saud_valor_hora_psicologi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_valor_minimo_etico.get("")
async def i_valor_minimo_etico():
    return {"p":"financeiro_saud_valor_minimo_etico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_website_clinica.get("")
async def i_website_clinica():
    return {"p":"financeiro_saud_website_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_workshop_receita.get("")
async def i_workshop_receita():
    return {"p":"financeiro_saud_workshop_receita","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_financeiro_saude_cli(PluginBase):
    name = "consolidated_financeiro_saude_clinico"
    def setup(self, app):
        app.include_router(router_aluguel_consultorio)
        app.include_router(router_assinaturas_clinica)
        app.include_router(router_atendimento_social)
        app.include_router(router_bndes_saude)
        app.include_router(router_cbhpm_psicologia)
        app.include_router(router_clinica_domiciliar)
        app.include_router(router_cnpj_clinica)
        app.include_router(router_consultoria_receita)
        app.include_router(router_convenio_psicologia)
        app.include_router(router_cooperativa_psicolog)
        app.include_router(router_coworking_clinico)
        app.include_router(router_credenciamento_plano)
        app.include_router(router_crescimento_receita_)
        app.include_router(router_curso_online_receita)
        app.include_router(router_deducao_ir_psicologo)
        app.include_router(router_descredenciamento_pl)
        app.include_router(router_diversificacao_recei)
        app.include_router(router_dre_clinica)
        app.include_router(router_eireli)
        app.include_router(router_emprestimo_clinica)
        app.include_router(router_equipamentos_clinica)
        app.include_router(router_fluxo_caixa_clinica)
        app.include_router(router_fomento_saude)
        app.include_router(router_franquia_clinica)
        app.include_router(router_glosa_plano_saude)
        app.include_router(router_home_office_clinico)
        app.include_router(router_honorarios_plano_sau)
        app.include_router(router_investimento_clinica)
        app.include_router(router_ir_psicologia)
        app.include_router(router_iss_psicologia)
        app.include_router(router_livro_psicologia)
        app.include_router(router_ltda_clinica)
        app.include_router(router_margem_lucro_clinica)
        app.include_router(router_marketing_custos)
        app.include_router(router_materiais_clinica)
        app.include_router(router_mei_psicologia)
        app.include_router(router_mentoria_receita)
        app.include_router(router_negociacao_plano_sau)
        app.include_router(router_nf_psicologia)
        app.include_router(router_nota_fiscal_autonomo)
        app.include_router(router_palestra_receita)
        app.include_router(router_particular_precifica)
        app.include_router(router_passivo_psicologia)
        app.include_router(router_payback_clinica)
        app.include_router(router_planilha_financeiro_)
        app.include_router(router_planilha_honorarios)
        app.include_router(router_ponto_equilibrio_cli)
        app.include_router(router_precificacao_psicolo)
        app.include_router(router_pro_bono_psicologia)
        app.include_router(router_publicidade_clinica)
        app.include_router(router_recurso_glosa)
        app.include_router(router_redes_sociais_custo)
        app.include_router(router_reembolso_plano)
        app.include_router(router_roi_clinica)
        app.include_router(router_sa_clinica)
        app.include_router(router_sliding_scale_psicol)
        app.include_router(router_softwares_clinica)
        app.include_router(router_supervise_receita)
        app.include_router(router_tabela_cfp_honorario)
        app.include_router(router_tuss_psicologia)
        app.include_router(router_valor_hora_psicologi)
        app.include_router(router_valor_minimo_etico)
        app.include_router(router_website_clinica)
        app.include_router(router_workshop_receita)


plugin = Plugin_financeiro_saude_cli()
