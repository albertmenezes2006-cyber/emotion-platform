from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_abp_participacao = APIRouter(prefix="/api/v1/autodesenvol/abp_participacao", tags=["autodesenvolvimento_profissional"])
router_abpmc_participacao = APIRouter(prefix="/api/v1/autodesenvol/abpmc_participacao", tags=["autodesenvolvimento_profissional"])
router_abpp_participacao = APIRouter(prefix="/api/v1/autodesenvol/abpp_participacao", tags=["autodesenvolvimento_profissional"])
router_analise_pessoal = APIRouter(prefix="/api/v1/autodesenvol/analise_pessoal", tags=["autodesenvolvimento_profissional"])
router_aprendizado_continuo = APIRouter(prefix="/api/v1/autodesenvol/aprendizado_continuo", tags=["autodesenvolvimento_profissional"])
router_artigos_cientificos_ = APIRouter(prefix="/api/v1/autodesenvol/artigos_cientificos_leitu", tags=["autodesenvolvimento_profissional"])
router_associacoes_profissi = APIRouter(prefix="/api/v1/autodesenvol/associacoes_profissionais", tags=["autodesenvolvimento_profissional"])
router_atualizacao_etica = APIRouter(prefix="/api/v1/autodesenvol/atualizacao_etica", tags=["autodesenvolvimento_profissional"])
router_autocuidado_psicolog = APIRouter(prefix="/api/v1/autodesenvol/autocuidado_psicologo", tags=["autodesenvolvimento_profissional"])
router_blog_profissional = APIRouter(prefix="/api/v1/autodesenvol/blog_profissional", tags=["autodesenvolvimento_profissional"])
router_burnout_prevencao_ps = APIRouter(prefix="/api/v1/autodesenvol/burnout_prevencao_psi", tags=["autodesenvolvimento_profissional"])
router_casos_eticos_cfp = APIRouter(prefix="/api/v1/autodesenvol/casos_eticos_cfp", tags=["autodesenvolvimento_profissional"])
router_cfp_participacao = APIRouter(prefix="/api/v1/autodesenvol/cfp_participacao", tags=["autodesenvolvimento_profissional"])
router_chamado_psicologia = APIRouter(prefix="/api/v1/autodesenvol/chamado_psicologia", tags=["autodesenvolvimento_profissional"])
router_coaching_profissiona = APIRouter(prefix="/api/v1/autodesenvol/coaching_profissional", tags=["autodesenvolvimento_profissional"])
router_codigo_etica_cfp2 = APIRouter(prefix="/api/v1/autodesenvol/codigo_etica_cfp2", tags=["autodesenvolvimento_profissional"])
router_comunidades_pratica = APIRouter(prefix="/api/v1/autodesenvol/comunidades_pratica", tags=["autodesenvolvimento_profissional"])
router_conciliacao_etica = APIRouter(prefix="/api/v1/autodesenvol/conciliacao_etica", tags=["autodesenvolvimento_profissional"])
router_congressos_participa = APIRouter(prefix="/api/v1/autodesenvol/congressos_participacao", tags=["autodesenvolvimento_profissional"])
router_consultoria_etica = APIRouter(prefix="/api/v1/autodesenvol/consultoria_etica", tags=["autodesenvolvimento_profissional"])
router_crp_participacao = APIRouter(prefix="/api/v1/autodesenvol/crp_participacao", tags=["autodesenvolvimento_profissional"])
router_cursos_pos_graduacao = APIRouter(prefix="/api/v1/autodesenvol/cursos_pos_graduacao", tags=["autodesenvolvimento_profissional"])
router_defesa_etica = APIRouter(prefix="/api/v1/autodesenvol/defesa_etica", tags=["autodesenvolvimento_profissional"])
router_denuncia_etica = APIRouter(prefix="/api/v1/autodesenvol/denuncia_etica", tags=["autodesenvolvimento_profissional"])
router_desenvolvimento_pess = APIRouter(prefix="/api/v1/autodesenvol/desenvolvimento_pessoal_p", tags=["autodesenvolvimento_profissional"])
router_dilemas_eticos_prati = APIRouter(prefix="/api/v1/autodesenvol/dilemas_eticos_pratica", tags=["autodesenvolvimento_profissional"])
router_doutorado_profission = APIRouter(prefix="/api/v1/autodesenvol/doutorado_profissional", tags=["autodesenvolvimento_profissional"])
router_educacao_permanente = APIRouter(prefix="/api/v1/autodesenvol/educacao_permanente", tags=["autodesenvolvimento_profissional"])
router_engagement_profissio = APIRouter(prefix="/api/v1/autodesenvol/engagement_profissional", tags=["autodesenvolvimento_profissional"])
router_especializacoes_psic = APIRouter(prefix="/api/v1/autodesenvol/especializacoes_psicologi", tags=["autodesenvolvimento_profissional"])
router_formacao_continua = APIRouter(prefix="/api/v1/autodesenvol/formacao_continua", tags=["autodesenvolvimento_profissional"])
router_formacao_etica = APIRouter(prefix="/api/v1/autodesenvol/formacao_etica", tags=["autodesenvolvimento_profissional"])
router_grupos_balint = APIRouter(prefix="/api/v1/autodesenvol/grupos_balint", tags=["autodesenvolvimento_profissional"])
router_grupos_estudo = APIRouter(prefix="/api/v1/autodesenvol/grupos_estudo", tags=["autodesenvolvimento_profissional"])
router_grupos_intervisao = APIRouter(prefix="/api/v1/autodesenvol/grupos_intervisao", tags=["autodesenvolvimento_profissional"])
router_grupos_reflexivos = APIRouter(prefix="/api/v1/autodesenvol/grupos_reflexivos", tags=["autodesenvolvimento_profissional"])
router_higiene_emocional_ps = APIRouter(prefix="/api/v1/autodesenvol/higiene_emocional_psicolo", tags=["autodesenvolvimento_profissional"])
router_identidade_profissio = APIRouter(prefix="/api/v1/autodesenvol/identidade_profissional_p", tags=["autodesenvolvimento_profissional"])
router_ifpe_participacao = APIRouter(prefix="/api/v1/autodesenvol/ifpe_participacao", tags=["autodesenvolvimento_profissional"])
router_instagram_profission = APIRouter(prefix="/api/v1/autodesenvol/instagram_profissional", tags=["autodesenvolvimento_profissional"])
router_jurisprudencia_psico = APIRouter(prefix="/api/v1/autodesenvol/jurisprudencia_psicologia", tags=["autodesenvolvimento_profissional"])
router_leitura_profissional = APIRouter(prefix="/api/v1/autodesenvol/leitura_profissional", tags=["autodesenvolvimento_profissional"])
router_linkedin_psicologo = APIRouter(prefix="/api/v1/autodesenvol/linkedin_psicologo", tags=["autodesenvolvimento_profissional"])
router_mentoria_profissiona = APIRouter(prefix="/api/v1/autodesenvol/mentoria_profissional", tags=["autodesenvolvimento_profissional"])
router_mestrado_profissiona = APIRouter(prefix="/api/v1/autodesenvol/mestrado_profissional", tags=["autodesenvolvimento_profissional"])
router_missao_visao_valores = APIRouter(prefix="/api/v1/autodesenvol/missao_visao_valores_psi", tags=["autodesenvolvimento_profissional"])
router_pesquisa_clinica_pro = APIRouter(prefix="/api/v1/autodesenvol/pesquisa_clinica_propria", tags=["autodesenvolvimento_profissional"])
router_podcast_profissional = APIRouter(prefix="/api/v1/autodesenvol/podcast_profissional2", tags=["autodesenvolvimento_profissional"])
router_processos_eticos = APIRouter(prefix="/api/v1/autodesenvol/processos_eticos", tags=["autodesenvolvimento_profissional"])
router_proposito_psicologia = APIRouter(prefix="/api/v1/autodesenvol/proposito_psicologia", tags=["autodesenvolvimento_profissional"])
router_publicacao_profissio = APIRouter(prefix="/api/v1/autodesenvol/publicacao_profissional", tags=["autodesenvolvimento_profissional"])
router_punicao_etica = APIRouter(prefix="/api/v1/autodesenvol/punicao_etica", tags=["autodesenvolvimento_profissional"])
router_redes_colaborativas = APIRouter(prefix="/api/v1/autodesenvol/redes_colaborativas", tags=["autodesenvolvimento_profissional"])
router_redes_profissionais_ = APIRouter(prefix="/api/v1/autodesenvol/redes_profissionais_psi", tags=["autodesenvolvimento_profissional"])
router_resolucoes_cfp_atual = APIRouter(prefix="/api/v1/autodesenvol/resolucoes_cfp_atualizaca", tags=["autodesenvolvimento_profissional"])
router_satisfacao_profissio = APIRouter(prefix="/api/v1/autodesenvol/satisfacao_profissional_p", tags=["autodesenvolvimento_profissional"])
router_sbcp_participacao = APIRouter(prefix="/api/v1/autodesenvol/sbcp_participacao", tags=["autodesenvolvimento_profissional"])
router_sentido_trabalho_psi = APIRouter(prefix="/api/v1/autodesenvol/sentido_trabalho_psi", tags=["autodesenvolvimento_profissional"])
router_supervisao_profissio = APIRouter(prefix="/api/v1/autodesenvol/supervisao_profissional", tags=["autodesenvolvimento_profissional"])
router_supervisao_propria = APIRouter(prefix="/api/v1/autodesenvol/supervisao_propria", tags=["autodesenvolvimento_profissional"])
router_terapia_propria_psic = APIRouter(prefix="/api/v1/autodesenvol/terapia_propria_psicologo", tags=["autodesenvolvimento_profissional"])
router_vocacao_psicologia = APIRouter(prefix="/api/v1/autodesenvol/vocacao_psicologia", tags=["autodesenvolvimento_profissional"])
router_youtube_profissional = APIRouter(prefix="/api/v1/autodesenvol/youtube_profissional", tags=["autodesenvolvimento_profissional"])

@router_abp_participacao.get("")
async def i_abp_participacao():
    return {"p":"autodesenvolvim_abp_participacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_abpmc_participacao.get("")
async def i_abpmc_participacao():
    return {"p":"autodesenvolvim_abpmc_participacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_abpp_participacao.get("")
async def i_abpp_participacao():
    return {"p":"autodesenvolvim_abpp_participacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_analise_pessoal.get("")
async def i_analise_pessoal():
    return {"p":"autodesenvolvim_analise_pessoal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_aprendizado_continuo.get("")
async def i_aprendizado_continuo():
    return {"p":"autodesenvolvim_aprendizado_continuo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_artigos_cientificos_.get("")
async def i_artigos_cientificos_():
    return {"p":"autodesenvolvim_artigos_cientificos_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_associacoes_profissi.get("")
async def i_associacoes_profissi():
    return {"p":"autodesenvolvim_associacoes_profissi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_atualizacao_etica.get("")
async def i_atualizacao_etica():
    return {"p":"autodesenvolvim_atualizacao_etica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autocuidado_psicolog.get("")
async def i_autocuidado_psicolog():
    return {"p":"autodesenvolvim_autocuidado_psicolog","s":"ativo","t":datetime.utcnow().isoformat()}
@router_blog_profissional.get("")
async def i_blog_profissional():
    return {"p":"autodesenvolvim_blog_profissional","s":"ativo","t":datetime.utcnow().isoformat()}
@router_burnout_prevencao_ps.get("")
async def i_burnout_prevencao_ps():
    return {"p":"autodesenvolvim_burnout_prevencao_ps","s":"ativo","t":datetime.utcnow().isoformat()}
@router_casos_eticos_cfp.get("")
async def i_casos_eticos_cfp():
    return {"p":"autodesenvolvim_casos_eticos_cfp","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cfp_participacao.get("")
async def i_cfp_participacao():
    return {"p":"autodesenvolvim_cfp_participacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_chamado_psicologia.get("")
async def i_chamado_psicologia():
    return {"p":"autodesenvolvim_chamado_psicologia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_coaching_profissiona.get("")
async def i_coaching_profissiona():
    return {"p":"autodesenvolvim_coaching_profissiona","s":"ativo","t":datetime.utcnow().isoformat()}
@router_codigo_etica_cfp2.get("")
async def i_codigo_etica_cfp2():
    return {"p":"autodesenvolvim_codigo_etica_cfp2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_comunidades_pratica.get("")
async def i_comunidades_pratica():
    return {"p":"autodesenvolvim_comunidades_pratica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_conciliacao_etica.get("")
async def i_conciliacao_etica():
    return {"p":"autodesenvolvim_conciliacao_etica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_congressos_participa.get("")
async def i_congressos_participa():
    return {"p":"autodesenvolvim_congressos_participa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_consultoria_etica.get("")
async def i_consultoria_etica():
    return {"p":"autodesenvolvim_consultoria_etica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_crp_participacao.get("")
async def i_crp_participacao():
    return {"p":"autodesenvolvim_crp_participacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cursos_pos_graduacao.get("")
async def i_cursos_pos_graduacao():
    return {"p":"autodesenvolvim_cursos_pos_graduacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_defesa_etica.get("")
async def i_defesa_etica():
    return {"p":"autodesenvolvim_defesa_etica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_denuncia_etica.get("")
async def i_denuncia_etica():
    return {"p":"autodesenvolvim_denuncia_etica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_desenvolvimento_pess.get("")
async def i_desenvolvimento_pess():
    return {"p":"autodesenvolvim_desenvolvimento_pess","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dilemas_eticos_prati.get("")
async def i_dilemas_eticos_prati():
    return {"p":"autodesenvolvim_dilemas_eticos_prati","s":"ativo","t":datetime.utcnow().isoformat()}
@router_doutorado_profission.get("")
async def i_doutorado_profission():
    return {"p":"autodesenvolvim_doutorado_profission","s":"ativo","t":datetime.utcnow().isoformat()}
@router_educacao_permanente.get("")
async def i_educacao_permanente():
    return {"p":"autodesenvolvim_educacao_permanente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_engagement_profissio.get("")
async def i_engagement_profissio():
    return {"p":"autodesenvolvim_engagement_profissio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_especializacoes_psic.get("")
async def i_especializacoes_psic():
    return {"p":"autodesenvolvim_especializacoes_psic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_formacao_continua.get("")
async def i_formacao_continua():
    return {"p":"autodesenvolvim_formacao_continua","s":"ativo","t":datetime.utcnow().isoformat()}
@router_formacao_etica.get("")
async def i_formacao_etica():
    return {"p":"autodesenvolvim_formacao_etica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grupos_balint.get("")
async def i_grupos_balint():
    return {"p":"autodesenvolvim_grupos_balint","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grupos_estudo.get("")
async def i_grupos_estudo():
    return {"p":"autodesenvolvim_grupos_estudo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grupos_intervisao.get("")
async def i_grupos_intervisao():
    return {"p":"autodesenvolvim_grupos_intervisao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grupos_reflexivos.get("")
async def i_grupos_reflexivos():
    return {"p":"autodesenvolvim_grupos_reflexivos","s":"ativo","t":datetime.utcnow().isoformat()}
@router_higiene_emocional_ps.get("")
async def i_higiene_emocional_ps():
    return {"p":"autodesenvolvim_higiene_emocional_ps","s":"ativo","t":datetime.utcnow().isoformat()}
@router_identidade_profissio.get("")
async def i_identidade_profissio():
    return {"p":"autodesenvolvim_identidade_profissio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ifpe_participacao.get("")
async def i_ifpe_participacao():
    return {"p":"autodesenvolvim_ifpe_participacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_instagram_profission.get("")
async def i_instagram_profission():
    return {"p":"autodesenvolvim_instagram_profission","s":"ativo","t":datetime.utcnow().isoformat()}
@router_jurisprudencia_psico.get("")
async def i_jurisprudencia_psico():
    return {"p":"autodesenvolvim_jurisprudencia_psico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_leitura_profissional.get("")
async def i_leitura_profissional():
    return {"p":"autodesenvolvim_leitura_profissional","s":"ativo","t":datetime.utcnow().isoformat()}
@router_linkedin_psicologo.get("")
async def i_linkedin_psicologo():
    return {"p":"autodesenvolvim_linkedin_psicologo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mentoria_profissiona.get("")
async def i_mentoria_profissiona():
    return {"p":"autodesenvolvim_mentoria_profissiona","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mestrado_profissiona.get("")
async def i_mestrado_profissiona():
    return {"p":"autodesenvolvim_mestrado_profissiona","s":"ativo","t":datetime.utcnow().isoformat()}
@router_missao_visao_valores.get("")
async def i_missao_visao_valores():
    return {"p":"autodesenvolvim_missao_visao_valores","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pesquisa_clinica_pro.get("")
async def i_pesquisa_clinica_pro():
    return {"p":"autodesenvolvim_pesquisa_clinica_pro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_podcast_profissional.get("")
async def i_podcast_profissional():
    return {"p":"autodesenvolvim_podcast_profissional","s":"ativo","t":datetime.utcnow().isoformat()}
@router_processos_eticos.get("")
async def i_processos_eticos():
    return {"p":"autodesenvolvim_processos_eticos","s":"ativo","t":datetime.utcnow().isoformat()}
@router_proposito_psicologia.get("")
async def i_proposito_psicologia():
    return {"p":"autodesenvolvim_proposito_psicologia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_publicacao_profissio.get("")
async def i_publicacao_profissio():
    return {"p":"autodesenvolvim_publicacao_profissio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_punicao_etica.get("")
async def i_punicao_etica():
    return {"p":"autodesenvolvim_punicao_etica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_redes_colaborativas.get("")
async def i_redes_colaborativas():
    return {"p":"autodesenvolvim_redes_colaborativas","s":"ativo","t":datetime.utcnow().isoformat()}
@router_redes_profissionais_.get("")
async def i_redes_profissionais_():
    return {"p":"autodesenvolvim_redes_profissionais_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_resolucoes_cfp_atual.get("")
async def i_resolucoes_cfp_atual():
    return {"p":"autodesenvolvim_resolucoes_cfp_atual","s":"ativo","t":datetime.utcnow().isoformat()}
@router_satisfacao_profissio.get("")
async def i_satisfacao_profissio():
    return {"p":"autodesenvolvim_satisfacao_profissio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sbcp_participacao.get("")
async def i_sbcp_participacao():
    return {"p":"autodesenvolvim_sbcp_participacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sentido_trabalho_psi.get("")
async def i_sentido_trabalho_psi():
    return {"p":"autodesenvolvim_sentido_trabalho_psi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_supervisao_profissio.get("")
async def i_supervisao_profissio():
    return {"p":"autodesenvolvim_supervisao_profissio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_supervisao_propria.get("")
async def i_supervisao_propria():
    return {"p":"autodesenvolvim_supervisao_propria","s":"ativo","t":datetime.utcnow().isoformat()}
@router_terapia_propria_psic.get("")
async def i_terapia_propria_psic():
    return {"p":"autodesenvolvim_terapia_propria_psic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_vocacao_psicologia.get("")
async def i_vocacao_psicologia():
    return {"p":"autodesenvolvim_vocacao_psicologia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_youtube_profissional.get("")
async def i_youtube_profissional():
    return {"p":"autodesenvolvim_youtube_profissional","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_autodesenvolvimento_(PluginBase):
    name = "consolidated_autodesenvolvimento_profission"
    def setup(self, app):
        app.include_router(router_abp_participacao)
        app.include_router(router_abpmc_participacao)
        app.include_router(router_abpp_participacao)
        app.include_router(router_analise_pessoal)
        app.include_router(router_aprendizado_continuo)
        app.include_router(router_artigos_cientificos_)
        app.include_router(router_associacoes_profissi)
        app.include_router(router_atualizacao_etica)
        app.include_router(router_autocuidado_psicolog)
        app.include_router(router_blog_profissional)
        app.include_router(router_burnout_prevencao_ps)
        app.include_router(router_casos_eticos_cfp)
        app.include_router(router_cfp_participacao)
        app.include_router(router_chamado_psicologia)
        app.include_router(router_coaching_profissiona)
        app.include_router(router_codigo_etica_cfp2)
        app.include_router(router_comunidades_pratica)
        app.include_router(router_conciliacao_etica)
        app.include_router(router_congressos_participa)
        app.include_router(router_consultoria_etica)
        app.include_router(router_crp_participacao)
        app.include_router(router_cursos_pos_graduacao)
        app.include_router(router_defesa_etica)
        app.include_router(router_denuncia_etica)
        app.include_router(router_desenvolvimento_pess)
        app.include_router(router_dilemas_eticos_prati)
        app.include_router(router_doutorado_profission)
        app.include_router(router_educacao_permanente)
        app.include_router(router_engagement_profissio)
        app.include_router(router_especializacoes_psic)
        app.include_router(router_formacao_continua)
        app.include_router(router_formacao_etica)
        app.include_router(router_grupos_balint)
        app.include_router(router_grupos_estudo)
        app.include_router(router_grupos_intervisao)
        app.include_router(router_grupos_reflexivos)
        app.include_router(router_higiene_emocional_ps)
        app.include_router(router_identidade_profissio)
        app.include_router(router_ifpe_participacao)
        app.include_router(router_instagram_profission)
        app.include_router(router_jurisprudencia_psico)
        app.include_router(router_leitura_profissional)
        app.include_router(router_linkedin_psicologo)
        app.include_router(router_mentoria_profissiona)
        app.include_router(router_mestrado_profissiona)
        app.include_router(router_missao_visao_valores)
        app.include_router(router_pesquisa_clinica_pro)
        app.include_router(router_podcast_profissional)
        app.include_router(router_processos_eticos)
        app.include_router(router_proposito_psicologia)
        app.include_router(router_publicacao_profissio)
        app.include_router(router_punicao_etica)
        app.include_router(router_redes_colaborativas)
        app.include_router(router_redes_profissionais_)
        app.include_router(router_resolucoes_cfp_atual)
        app.include_router(router_satisfacao_profissio)
        app.include_router(router_sbcp_participacao)
        app.include_router(router_sentido_trabalho_psi)
        app.include_router(router_supervisao_profissio)
        app.include_router(router_supervisao_propria)
        app.include_router(router_terapia_propria_psic)
        app.include_router(router_vocacao_psicologia)
        app.include_router(router_youtube_profissional)


plugin = Plugin_autodesenvolvimento_()
