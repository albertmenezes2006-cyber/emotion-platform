from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_act_adolescente = APIRouter(prefix="/api/v1/psicoterapia/act_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_aculturacao_adolesce = APIRouter(prefix="/api/v1/psicoterapia/aculturacao_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_afirmacao_genero_ter = APIRouter(prefix="/api/v1/psicoterapia/afirmacao_genero_terapia", tags=["psicoterapia_adolescentes_tecnicas"])
router_alianca_adolescente = APIRouter(prefix="/api/v1/psicoterapia/alianca_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_ambivalencia_adolesc = APIRouter(prefix="/api/v1/psicoterapia/ambivalencia_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_arte_terapia_adolesc = APIRouter(prefix="/api/v1/psicoterapia/arte_terapia_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_autoestima_teen2 = APIRouter(prefix="/api/v1/psicoterapia/autoestima_teen2", tags=["psicoterapia_adolescentes_tecnicas"])
router_autolesao_intervenca = APIRouter(prefix="/api/v1/psicoterapia/autolesao_intervencao", tags=["psicoterapia_adolescentes_tecnicas"])
router_autonomia_adolescent = APIRouter(prefix="/api/v1/psicoterapia/autonomia_adolescente2", tags=["psicoterapia_adolescentes_tecnicas"])
router_aventura_adolescente = APIRouter(prefix="/api/v1/psicoterapia/aventura_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_bullying_intervenção = APIRouter(prefix="/api/v1/psicoterapia/bullying_intervenção", tags=["psicoterapia_adolescentes_tecnicas"])
router_cams_adolescente = APIRouter(prefix="/api/v1/psicoterapia/cams_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_cbt_adolescente = APIRouter(prefix="/api/v1/psicoterapia/cbt_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_cinema_adolescente = APIRouter(prefix="/api/v1/psicoterapia/cinema_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_coming_out_terapia = APIRouter(prefix="/api/v1/psicoterapia/coming_out_terapia", tags=["psicoterapia_adolescentes_tecnicas"])
router_confidencialidade_ad = APIRouter(prefix="/api/v1/psicoterapia/confidencialidade_adolesc", tags=["psicoterapia_adolescentes_tecnicas"])
router_contrato_adolescente = APIRouter(prefix="/api/v1/psicoterapia/contrato_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_criatividade_adolesc = APIRouter(prefix="/api/v1/psicoterapia/criatividade_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_crisis_teen = APIRouter(prefix="/api/v1/psicoterapia/crisis_teen", tags=["psicoterapia_adolescentes_tecnicas"])
router_cultura_adolescente_ = APIRouter(prefix="/api/v1/psicoterapia/cultura_adolescente_terap", tags=["psicoterapia_adolescentes_tecnicas"])
router_cyberbullying_interv = APIRouter(prefix="/api/v1/psicoterapia/cyberbullying_intervencao", tags=["psicoterapia_adolescentes_tecnicas"])
router_dbt_adolescente = APIRouter(prefix="/api/v1/psicoterapia/dbt_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_discriminacao_adoles = APIRouter(prefix="/api/v1/psicoterapia/discriminacao_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_divorcio_adolescente = APIRouter(prefix="/api/v1/psicoterapia/divorcio_adolescente_tera", tags=["psicoterapia_adolescentes_tecnicas"])
router_entrevista_motivacio = APIRouter(prefix="/api/v1/psicoterapia/entrevista_motivacional_t", tags=["psicoterapia_adolescentes_tecnicas"])
router_escrita_adolescente = APIRouter(prefix="/api/v1/psicoterapia/escrita_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_esporte_terapia_adol = APIRouter(prefix="/api/v1/psicoterapia/esporte_terapia_adolescen", tags=["psicoterapia_adolescentes_tecnicas"])
router_familia_adolescente_ = APIRouter(prefix="/api/v1/psicoterapia/familia_adolescente_terap", tags=["psicoterapia_adolescentes_tecnicas"])
router_fortalezas_adolescen = APIRouter(prefix="/api/v1/psicoterapia/fortalezas_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_grupo_adolescentes2 = APIRouter(prefix="/api/v1/psicoterapia/grupo_adolescentes2", tags=["psicoterapia_adolescentes_tecnicas"])
router_homofobia_adolescent = APIRouter(prefix="/api/v1/psicoterapia/homofobia_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_identidade_bicultura = APIRouter(prefix="/api/v1/psicoterapia/identidade_bicultural", tags=["psicoterapia_adolescentes_tecnicas"])
router_identidade_lgbtq_ter = APIRouter(prefix="/api/v1/psicoterapia/identidade_lgbtq_terapia", tags=["psicoterapia_adolescentes_tecnicas"])
router_identidade_terapia = APIRouter(prefix="/api/v1/psicoterapia/identidade_terapia", tags=["psicoterapia_adolescentes_tecnicas"])
router_imagem_corporal_tera = APIRouter(prefix="/api/v1/psicoterapia/imagem_corporal_terapia", tags=["psicoterapia_adolescentes_tecnicas"])
router_jogos_terapia_adoles = APIRouter(prefix="/api/v1/psicoterapia/jogos_terapia_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_limites_adolescente = APIRouter(prefix="/api/v1/psicoterapia/limites_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_mbct_adolescente = APIRouter(prefix="/api/v1/psicoterapia/mbct_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_midia_social_terapia = APIRouter(prefix="/api/v1/psicoterapia/midia_social_terapia", tags=["psicoterapia_adolescentes_tecnicas"])
router_migracao_adolescente = APIRouter(prefix="/api/v1/psicoterapia/migracao_adolescente_tera", tags=["psicoterapia_adolescentes_tecnicas"])
router_mindfulness_adolesce = APIRouter(prefix="/api/v1/psicoterapia/mindfulness_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_motivacao_adolescent = APIRouter(prefix="/api/v1/psicoterapia/motivacao_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_musica_adolescente = APIRouter(prefix="/api/v1/psicoterapia/musica_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_natureza_adolescente = APIRouter(prefix="/api/v1/psicoterapia/natureza_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_perdas_adolescente = APIRouter(prefix="/api/v1/psicoterapia/perdas_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_projetos_significado = APIRouter(prefix="/api/v1/psicoterapia/projetos_significado", tags=["psicoterapia_adolescentes_tecnicas"])
router_proposito_adolescent = APIRouter(prefix="/api/v1/psicoterapia/proposito_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_psicoeducacao_adoles = APIRouter(prefix="/api/v1/psicoterapia/psicoeducacao_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_psicoeducacao_pais = APIRouter(prefix="/api/v1/psicoterapia/psicoeducacao_pais", tags=["psicoterapia_adolescentes_tecnicas"])
router_racismo_adolescente = APIRouter(prefix="/api/v1/psicoterapia/racismo_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_relacionamentos_adol = APIRouter(prefix="/api/v1/psicoterapia/relacionamentos_adolescen", tags=["psicoterapia_adolescentes_tecnicas"])
router_religiao_espirituali = APIRouter(prefix="/api/v1/psicoterapia/religiao_espiritualidade_", tags=["psicoterapia_adolescentes_tecnicas"])
router_resistencia_adolesce = APIRouter(prefix="/api/v1/psicoterapia/resistencia_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_safety_planning_adol = APIRouter(prefix="/api/v1/psicoterapia/safety_planning_adolescen", tags=["psicoterapia_adolescentes_tecnicas"])
router_servico_comunitario = APIRouter(prefix="/api/v1/psicoterapia/servico_comunitario", tags=["psicoterapia_adolescentes_tecnicas"])
router_sessoes_familiares = APIRouter(prefix="/api/v1/psicoterapia/sessoes_familiares", tags=["psicoterapia_adolescentes_tecnicas"])
router_sessoes_individuais = APIRouter(prefix="/api/v1/psicoterapia/sessoes_individuais", tags=["psicoterapia_adolescentes_tecnicas"])
router_sexualidade_terapia = APIRouter(prefix="/api/v1/psicoterapia/sexualidade_terapia", tags=["psicoterapia_adolescentes_tecnicas"])
router_suicidio_adolescente = APIRouter(prefix="/api/v1/psicoterapia/suicidio_adolescente_inte", tags=["psicoterapia_adolescentes_tecnicas"])
router_tecnologia_terapia = APIRouter(prefix="/api/v1/psicoterapia/tecnologia_terapia", tags=["psicoterapia_adolescentes_tecnicas"])
router_trauma_adolescente = APIRouter(prefix="/api/v1/psicoterapia/trauma_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_trauma_focused_adole = APIRouter(prefix="/api/v1/psicoterapia/trauma_focused_adolescent", tags=["psicoterapia_adolescentes_tecnicas"])
router_valores_adolescente = APIRouter(prefix="/api/v1/psicoterapia/valores_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
router_voluntariado_terapia = APIRouter(prefix="/api/v1/psicoterapia/voluntariado_terapia", tags=["psicoterapia_adolescentes_tecnicas"])

@router_act_adolescente.get("")
async def i_act_adolescente():
    return {"p":"psicoterapia_ad_act_adolescente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_aculturacao_adolesce.get("")
async def i_aculturacao_adolesce():
    return {"p":"psicoterapia_ad_aculturacao_adolesce","s":"ativo","t":datetime.utcnow().isoformat()}
@router_afirmacao_genero_ter.get("")
async def i_afirmacao_genero_ter():
    return {"p":"psicoterapia_ad_afirmacao_genero_ter","s":"ativo","t":datetime.utcnow().isoformat()}
@router_alianca_adolescente.get("")
async def i_alianca_adolescente():
    return {"p":"psicoterapia_ad_alianca_adolescente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ambivalencia_adolesc.get("")
async def i_ambivalencia_adolesc():
    return {"p":"psicoterapia_ad_ambivalencia_adolesc","s":"ativo","t":datetime.utcnow().isoformat()}
@router_arte_terapia_adolesc.get("")
async def i_arte_terapia_adolesc():
    return {"p":"psicoterapia_ad_arte_terapia_adolesc","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autoestima_teen2.get("")
async def i_autoestima_teen2():
    return {"p":"psicoterapia_ad_autoestima_teen2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autolesao_intervenca.get("")
async def i_autolesao_intervenca():
    return {"p":"psicoterapia_ad_autolesao_intervenca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autonomia_adolescent.get("")
async def i_autonomia_adolescent():
    return {"p":"psicoterapia_ad_autonomia_adolescent","s":"ativo","t":datetime.utcnow().isoformat()}
@router_aventura_adolescente.get("")
async def i_aventura_adolescente():
    return {"p":"psicoterapia_ad_aventura_adolescente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bullying_intervenção.get("")
async def i_bullying_intervenção():
    return {"p":"psicoterapia_ad_bullying_intervenção","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cams_adolescente.get("")
async def i_cams_adolescente():
    return {"p":"psicoterapia_ad_cams_adolescente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cbt_adolescente.get("")
async def i_cbt_adolescente():
    return {"p":"psicoterapia_ad_cbt_adolescente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cinema_adolescente.get("")
async def i_cinema_adolescente():
    return {"p":"psicoterapia_ad_cinema_adolescente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_coming_out_terapia.get("")
async def i_coming_out_terapia():
    return {"p":"psicoterapia_ad_coming_out_terapia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_confidencialidade_ad.get("")
async def i_confidencialidade_ad():
    return {"p":"psicoterapia_ad_confidencialidade_ad","s":"ativo","t":datetime.utcnow().isoformat()}
@router_contrato_adolescente.get("")
async def i_contrato_adolescente():
    return {"p":"psicoterapia_ad_contrato_adolescente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_criatividade_adolesc.get("")
async def i_criatividade_adolesc():
    return {"p":"psicoterapia_ad_criatividade_adolesc","s":"ativo","t":datetime.utcnow().isoformat()}
@router_crisis_teen.get("")
async def i_crisis_teen():
    return {"p":"psicoterapia_ad_crisis_teen","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cultura_adolescente_.get("")
async def i_cultura_adolescente_():
    return {"p":"psicoterapia_ad_cultura_adolescente_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cyberbullying_interv.get("")
async def i_cyberbullying_interv():
    return {"p":"psicoterapia_ad_cyberbullying_interv","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dbt_adolescente.get("")
async def i_dbt_adolescente():
    return {"p":"psicoterapia_ad_dbt_adolescente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_discriminacao_adoles.get("")
async def i_discriminacao_adoles():
    return {"p":"psicoterapia_ad_discriminacao_adoles","s":"ativo","t":datetime.utcnow().isoformat()}
@router_divorcio_adolescente.get("")
async def i_divorcio_adolescente():
    return {"p":"psicoterapia_ad_divorcio_adolescente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_entrevista_motivacio.get("")
async def i_entrevista_motivacio():
    return {"p":"psicoterapia_ad_entrevista_motivacio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_escrita_adolescente.get("")
async def i_escrita_adolescente():
    return {"p":"psicoterapia_ad_escrita_adolescente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_esporte_terapia_adol.get("")
async def i_esporte_terapia_adol():
    return {"p":"psicoterapia_ad_esporte_terapia_adol","s":"ativo","t":datetime.utcnow().isoformat()}
@router_familia_adolescente_.get("")
async def i_familia_adolescente_():
    return {"p":"psicoterapia_ad_familia_adolescente_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fortalezas_adolescen.get("")
async def i_fortalezas_adolescen():
    return {"p":"psicoterapia_ad_fortalezas_adolescen","s":"ativo","t":datetime.utcnow().isoformat()}
@router_grupo_adolescentes2.get("")
async def i_grupo_adolescentes2():
    return {"p":"psicoterapia_ad_grupo_adolescentes2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_homofobia_adolescent.get("")
async def i_homofobia_adolescent():
    return {"p":"psicoterapia_ad_homofobia_adolescent","s":"ativo","t":datetime.utcnow().isoformat()}
@router_identidade_bicultura.get("")
async def i_identidade_bicultura():
    return {"p":"psicoterapia_ad_identidade_bicultura","s":"ativo","t":datetime.utcnow().isoformat()}
@router_identidade_lgbtq_ter.get("")
async def i_identidade_lgbtq_ter():
    return {"p":"psicoterapia_ad_identidade_lgbtq_ter","s":"ativo","t":datetime.utcnow().isoformat()}
@router_identidade_terapia.get("")
async def i_identidade_terapia():
    return {"p":"psicoterapia_ad_identidade_terapia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_imagem_corporal_tera.get("")
async def i_imagem_corporal_tera():
    return {"p":"psicoterapia_ad_imagem_corporal_tera","s":"ativo","t":datetime.utcnow().isoformat()}
@router_jogos_terapia_adoles.get("")
async def i_jogos_terapia_adoles():
    return {"p":"psicoterapia_ad_jogos_terapia_adoles","s":"ativo","t":datetime.utcnow().isoformat()}
@router_limites_adolescente.get("")
async def i_limites_adolescente():
    return {"p":"psicoterapia_ad_limites_adolescente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mbct_adolescente.get("")
async def i_mbct_adolescente():
    return {"p":"psicoterapia_ad_mbct_adolescente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_midia_social_terapia.get("")
async def i_midia_social_terapia():
    return {"p":"psicoterapia_ad_midia_social_terapia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_migracao_adolescente.get("")
async def i_migracao_adolescente():
    return {"p":"psicoterapia_ad_migracao_adolescente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mindfulness_adolesce.get("")
async def i_mindfulness_adolesce():
    return {"p":"psicoterapia_ad_mindfulness_adolesce","s":"ativo","t":datetime.utcnow().isoformat()}
@router_motivacao_adolescent.get("")
async def i_motivacao_adolescent():
    return {"p":"psicoterapia_ad_motivacao_adolescent","s":"ativo","t":datetime.utcnow().isoformat()}
@router_musica_adolescente.get("")
async def i_musica_adolescente():
    return {"p":"psicoterapia_ad_musica_adolescente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_natureza_adolescente.get("")
async def i_natureza_adolescente():
    return {"p":"psicoterapia_ad_natureza_adolescente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_perdas_adolescente.get("")
async def i_perdas_adolescente():
    return {"p":"psicoterapia_ad_perdas_adolescente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_projetos_significado.get("")
async def i_projetos_significado():
    return {"p":"psicoterapia_ad_projetos_significado","s":"ativo","t":datetime.utcnow().isoformat()}
@router_proposito_adolescent.get("")
async def i_proposito_adolescent():
    return {"p":"psicoterapia_ad_proposito_adolescent","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicoeducacao_adoles.get("")
async def i_psicoeducacao_adoles():
    return {"p":"psicoterapia_ad_psicoeducacao_adoles","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicoeducacao_pais.get("")
async def i_psicoeducacao_pais():
    return {"p":"psicoterapia_ad_psicoeducacao_pais","s":"ativo","t":datetime.utcnow().isoformat()}
@router_racismo_adolescente.get("")
async def i_racismo_adolescente():
    return {"p":"psicoterapia_ad_racismo_adolescente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_relacionamentos_adol.get("")
async def i_relacionamentos_adol():
    return {"p":"psicoterapia_ad_relacionamentos_adol","s":"ativo","t":datetime.utcnow().isoformat()}
@router_religiao_espirituali.get("")
async def i_religiao_espirituali():
    return {"p":"psicoterapia_ad_religiao_espirituali","s":"ativo","t":datetime.utcnow().isoformat()}
@router_resistencia_adolesce.get("")
async def i_resistencia_adolesce():
    return {"p":"psicoterapia_ad_resistencia_adolesce","s":"ativo","t":datetime.utcnow().isoformat()}
@router_safety_planning_adol.get("")
async def i_safety_planning_adol():
    return {"p":"psicoterapia_ad_safety_planning_adol","s":"ativo","t":datetime.utcnow().isoformat()}
@router_servico_comunitario.get("")
async def i_servico_comunitario():
    return {"p":"psicoterapia_ad_servico_comunitario","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sessoes_familiares.get("")
async def i_sessoes_familiares():
    return {"p":"psicoterapia_ad_sessoes_familiares","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sessoes_individuais.get("")
async def i_sessoes_individuais():
    return {"p":"psicoterapia_ad_sessoes_individuais","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sexualidade_terapia.get("")
async def i_sexualidade_terapia():
    return {"p":"psicoterapia_ad_sexualidade_terapia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_suicidio_adolescente.get("")
async def i_suicidio_adolescente():
    return {"p":"psicoterapia_ad_suicidio_adolescente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tecnologia_terapia.get("")
async def i_tecnologia_terapia():
    return {"p":"psicoterapia_ad_tecnologia_terapia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_trauma_adolescente.get("")
async def i_trauma_adolescente():
    return {"p":"psicoterapia_ad_trauma_adolescente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_trauma_focused_adole.get("")
async def i_trauma_focused_adole():
    return {"p":"psicoterapia_ad_trauma_focused_adole","s":"ativo","t":datetime.utcnow().isoformat()}
@router_valores_adolescente.get("")
async def i_valores_adolescente():
    return {"p":"psicoterapia_ad_valores_adolescente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_voluntariado_terapia.get("")
async def i_voluntariado_terapia():
    return {"p":"psicoterapia_ad_voluntariado_terapia","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_psicoterapia_adolesc(PluginBase):
    name = "consolidated_psicoterapia_adolescentes_tecn"
    def setup(self, app):
        app.include_router(router_act_adolescente)
        app.include_router(router_aculturacao_adolesce)
        app.include_router(router_afirmacao_genero_ter)
        app.include_router(router_alianca_adolescente)
        app.include_router(router_ambivalencia_adolesc)
        app.include_router(router_arte_terapia_adolesc)
        app.include_router(router_autoestima_teen2)
        app.include_router(router_autolesao_intervenca)
        app.include_router(router_autonomia_adolescent)
        app.include_router(router_aventura_adolescente)
        app.include_router(router_bullying_intervenção)
        app.include_router(router_cams_adolescente)
        app.include_router(router_cbt_adolescente)
        app.include_router(router_cinema_adolescente)
        app.include_router(router_coming_out_terapia)
        app.include_router(router_confidencialidade_ad)
        app.include_router(router_contrato_adolescente)
        app.include_router(router_criatividade_adolesc)
        app.include_router(router_crisis_teen)
        app.include_router(router_cultura_adolescente_)
        app.include_router(router_cyberbullying_interv)
        app.include_router(router_dbt_adolescente)
        app.include_router(router_discriminacao_adoles)
        app.include_router(router_divorcio_adolescente)
        app.include_router(router_entrevista_motivacio)
        app.include_router(router_escrita_adolescente)
        app.include_router(router_esporte_terapia_adol)
        app.include_router(router_familia_adolescente_)
        app.include_router(router_fortalezas_adolescen)
        app.include_router(router_grupo_adolescentes2)
        app.include_router(router_homofobia_adolescent)
        app.include_router(router_identidade_bicultura)
        app.include_router(router_identidade_lgbtq_ter)
        app.include_router(router_identidade_terapia)
        app.include_router(router_imagem_corporal_tera)
        app.include_router(router_jogos_terapia_adoles)
        app.include_router(router_limites_adolescente)
        app.include_router(router_mbct_adolescente)
        app.include_router(router_midia_social_terapia)
        app.include_router(router_migracao_adolescente)
        app.include_router(router_mindfulness_adolesce)
        app.include_router(router_motivacao_adolescent)
        app.include_router(router_musica_adolescente)
        app.include_router(router_natureza_adolescente)
        app.include_router(router_perdas_adolescente)
        app.include_router(router_projetos_significado)
        app.include_router(router_proposito_adolescent)
        app.include_router(router_psicoeducacao_adoles)
        app.include_router(router_psicoeducacao_pais)
        app.include_router(router_racismo_adolescente)
        app.include_router(router_relacionamentos_adol)
        app.include_router(router_religiao_espirituali)
        app.include_router(router_resistencia_adolesce)
        app.include_router(router_safety_planning_adol)
        app.include_router(router_servico_comunitario)
        app.include_router(router_sessoes_familiares)
        app.include_router(router_sessoes_individuais)
        app.include_router(router_sexualidade_terapia)
        app.include_router(router_suicidio_adolescente)
        app.include_router(router_tecnologia_terapia)
        app.include_router(router_trauma_adolescente)
        app.include_router(router_trauma_focused_adole)
        app.include_router(router_valores_adolescente)
        app.include_router(router_voluntariado_terapia)


plugin = Plugin_psicoterapia_adolesc()
