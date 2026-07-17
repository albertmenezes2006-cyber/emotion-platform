from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_alianca_idoso = APIRouter(prefix="/api/v1/psicoterapia/alianca_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_animais_idoso = APIRouter(prefix="/api/v1/psicoterapia/animais_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_arte_idoso = APIRouter(prefix="/api/v1/psicoterapia/arte_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_atividade_fisica_ido = APIRouter(prefix="/api/v1/psicoterapia/atividade_fisica_idoso3", tags=["psicoterapia_idosos_tecnicas"])
router_autobiografia_terape = APIRouter(prefix="/api/v1/psicoterapia/autobiografia_terapeutica", tags=["psicoterapia_idosos_tecnicas"])
router_autocuidado_idoso = APIRouter(prefix="/api/v1/psicoterapia/autocuidado_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_autonomia_idoso2 = APIRouter(prefix="/api/v1/psicoterapia/autonomia_idoso2", tags=["psicoterapia_idosos_tecnicas"])
router_bordado_idoso = APIRouter(prefix="/api/v1/psicoterapia/bordado_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_caminhada_idoso = APIRouter(prefix="/api/v1/psicoterapia/caminhada_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_cartas_terapia_idoso = APIRouter(prefix="/api/v1/psicoterapia/cartas_terapia_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_compliance_medicacao = APIRouter(prefix="/api/v1/psicoterapia/compliance_medicacao", tags=["psicoterapia_idosos_tecnicas"])
router_computador_idoso = APIRouter(prefix="/api/v1/psicoterapia/computador_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_contemplacao_idoso = APIRouter(prefix="/api/v1/psicoterapia/contemplacao_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_culinaria_idoso = APIRouter(prefix="/api/v1/psicoterapia/culinaria_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_curso_novo_idoso = APIRouter(prefix="/api/v1/psicoterapia/curso_novo_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_danca_idoso = APIRouter(prefix="/api/v1/psicoterapia/danca_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_dignidade_idoso = APIRouter(prefix="/api/v1/psicoterapia/dignidade_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_direitos_idoso = APIRouter(prefix="/api/v1/psicoterapia/direitos_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_dor_cronica_idoso2 = APIRouter(prefix="/api/v1/psicoterapia/dor_cronica_idoso2", tags=["psicoterapia_idosos_tecnicas"])
router_engajamento_social_i = APIRouter(prefix="/api/v1/psicoterapia/engajamento_social_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_escrita_criativa_ido = APIRouter(prefix="/api/v1/psicoterapia/escrita_criativa_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_espiritualidade_idos = APIRouter(prefix="/api/v1/psicoterapia/espiritualidade_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_estimulacao_cognitiv = APIRouter(prefix="/api/v1/psicoterapia/estimulacao_cognitiva2", tags=["psicoterapia_idosos_tecnicas"])
router_exercicio_cognitivo = APIRouter(prefix="/api/v1/psicoterapia/exercicio_cognitivo", tags=["psicoterapia_idosos_tecnicas"])
router_fotos_terapia = APIRouter(prefix="/api/v1/psicoterapia/fotos_terapia", tags=["psicoterapia_idosos_tecnicas"])
router_hidratacao_idoso = APIRouter(prefix="/api/v1/psicoterapia/hidratacao_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_historia_vida = APIRouter(prefix="/api/v1/psicoterapia/historia_vida", tags=["psicoterapia_idosos_tecnicas"])
router_horta_idoso = APIRouter(prefix="/api/v1/psicoterapia/horta_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_idioma_novo_idoso = APIRouter(prefix="/api/v1/psicoterapia/idioma_novo_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_independencia_funcio = APIRouter(prefix="/api/v1/psicoterapia/independencia_funcional", tags=["psicoterapia_idosos_tecnicas"])
router_intergeracional_ativ = APIRouter(prefix="/api/v1/psicoterapia/intergeracional_atividade", tags=["psicoterapia_idosos_tecnicas"])
router_jardinagem_idoso2 = APIRouter(prefix="/api/v1/psicoterapia/jardinagem_idoso2", tags=["psicoterapia_idosos_tecnicas"])
router_jogos_cognitivos = APIRouter(prefix="/api/v1/psicoterapia/jogos_cognitivos", tags=["psicoterapia_idosos_tecnicas"])
router_legado_idoso3 = APIRouter(prefix="/api/v1/psicoterapia/legado_idoso3", tags=["psicoterapia_idosos_tecnicas"])
router_leitura_idoso = APIRouter(prefix="/api/v1/psicoterapia/leitura_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_linhas_tempo_idoso = APIRouter(prefix="/api/v1/psicoterapia/linhas_tempo_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_medicacao_gerenciame = APIRouter(prefix="/api/v1/psicoterapia/medicacao_gerenciamento", tags=["psicoterapia_idosos_tecnicas"])
router_meditacao_idoso2 = APIRouter(prefix="/api/v1/psicoterapia/meditacao_idoso2", tags=["psicoterapia_idosos_tecnicas"])
router_mentorado_idoso = APIRouter(prefix="/api/v1/psicoterapia/mentorado_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_mobilidade_idoso = APIRouter(prefix="/api/v1/psicoterapia/mobilidade_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_musica_aprendizado_i = APIRouter(prefix="/api/v1/psicoterapia/musica_aprendizado_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_musica_idoso = APIRouter(prefix="/api/v1/psicoterapia/musica_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_musica_memoria = APIRouter(prefix="/api/v1/psicoterapia/musica_memoria", tags=["psicoterapia_idosos_tecnicas"])
router_narrativa_idoso = APIRouter(prefix="/api/v1/psicoterapia/narrativa_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_natacao_idoso = APIRouter(prefix="/api/v1/psicoterapia/natacao_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_natureza_idoso = APIRouter(prefix="/api/v1/psicoterapia/natureza_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_nutricao_idoso = APIRouter(prefix="/api/v1/psicoterapia/nutricao_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_objetos_significativ = APIRouter(prefix="/api/v1/psicoterapia/objetos_significativos", tags=["psicoterapia_idosos_tecnicas"])
router_palavras_cruzadas = APIRouter(prefix="/api/v1/psicoterapia/palavras_cruzadas", tags=["psicoterapia_idosos_tecnicas"])
router_pet_therapy_idoso = APIRouter(prefix="/api/v1/psicoterapia/pet_therapy_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_pilates_idoso = APIRouter(prefix="/api/v1/psicoterapia/pilates_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_polifarmacia_manejo = APIRouter(prefix="/api/v1/psicoterapia/polifarmacia_manejo", tags=["psicoterapia_idosos_tecnicas"])
router_projeto_significativ = APIRouter(prefix="/api/v1/psicoterapia/projeto_significativo", tags=["psicoterapia_idosos_tecnicas"])
router_religiao_idoso = APIRouter(prefix="/api/v1/psicoterapia/religiao_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_reminiscencia2 = APIRouter(prefix="/api/v1/psicoterapia/reminiscencia2", tags=["psicoterapia_idosos_tecnicas"])
router_revisao_vida2 = APIRouter(prefix="/api/v1/psicoterapia/revisao_vida2", tags=["psicoterapia_idosos_tecnicas"])
router_sabedoria_transmissa = APIRouter(prefix="/api/v1/psicoterapia/sabedoria_transmissao", tags=["psicoterapia_idosos_tecnicas"])
router_social_media_idoso = APIRouter(prefix="/api/v1/psicoterapia/social_media_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_sono_higiene_idoso = APIRouter(prefix="/api/v1/psicoterapia/sono_higiene_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_sudoku_mental = APIRouter(prefix="/api/v1/psicoterapia/sudoku_mental", tags=["psicoterapia_idosos_tecnicas"])
router_tai_chi_idoso = APIRouter(prefix="/api/v1/psicoterapia/tai_chi_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_tecnologia_idoso2 = APIRouter(prefix="/api/v1/psicoterapia/tecnologia_idoso2", tags=["psicoterapia_idosos_tecnicas"])
router_terapia_retro = APIRouter(prefix="/api/v1/psicoterapia/terapia_retro", tags=["psicoterapia_idosos_tecnicas"])
router_treino_memoria_idoso = APIRouter(prefix="/api/v1/psicoterapia/treino_memoria_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_turismo_terapeutico = APIRouter(prefix="/api/v1/psicoterapia/turismo_terapeutico", tags=["psicoterapia_idosos_tecnicas"])
router_viagem_idoso = APIRouter(prefix="/api/v1/psicoterapia/viagem_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_videochamada_idoso = APIRouter(prefix="/api/v1/psicoterapia/videochamada_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_voluntariado_idoso = APIRouter(prefix="/api/v1/psicoterapia/voluntariado_idoso", tags=["psicoterapia_idosos_tecnicas"])
router_xadrez_mental = APIRouter(prefix="/api/v1/psicoterapia/xadrez_mental", tags=["psicoterapia_idosos_tecnicas"])
router_yoga_idoso = APIRouter(prefix="/api/v1/psicoterapia/yoga_idoso", tags=["psicoterapia_idosos_tecnicas"])

@router_alianca_idoso.get("")
async def i_alianca_idoso():
    return {"p":"psicoterapia_id_alianca_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_animais_idoso.get("")
async def i_animais_idoso():
    return {"p":"psicoterapia_id_animais_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_arte_idoso.get("")
async def i_arte_idoso():
    return {"p":"psicoterapia_id_arte_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_atividade_fisica_ido.get("")
async def i_atividade_fisica_ido():
    return {"p":"psicoterapia_id_atividade_fisica_ido","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autobiografia_terape.get("")
async def i_autobiografia_terape():
    return {"p":"psicoterapia_id_autobiografia_terape","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autocuidado_idoso.get("")
async def i_autocuidado_idoso():
    return {"p":"psicoterapia_id_autocuidado_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autonomia_idoso2.get("")
async def i_autonomia_idoso2():
    return {"p":"psicoterapia_id_autonomia_idoso2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bordado_idoso.get("")
async def i_bordado_idoso():
    return {"p":"psicoterapia_id_bordado_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_caminhada_idoso.get("")
async def i_caminhada_idoso():
    return {"p":"psicoterapia_id_caminhada_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cartas_terapia_idoso.get("")
async def i_cartas_terapia_idoso():
    return {"p":"psicoterapia_id_cartas_terapia_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_compliance_medicacao.get("")
async def i_compliance_medicacao():
    return {"p":"psicoterapia_id_compliance_medicacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_computador_idoso.get("")
async def i_computador_idoso():
    return {"p":"psicoterapia_id_computador_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_contemplacao_idoso.get("")
async def i_contemplacao_idoso():
    return {"p":"psicoterapia_id_contemplacao_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_culinaria_idoso.get("")
async def i_culinaria_idoso():
    return {"p":"psicoterapia_id_culinaria_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_curso_novo_idoso.get("")
async def i_curso_novo_idoso():
    return {"p":"psicoterapia_id_curso_novo_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_danca_idoso.get("")
async def i_danca_idoso():
    return {"p":"psicoterapia_id_danca_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dignidade_idoso.get("")
async def i_dignidade_idoso():
    return {"p":"psicoterapia_id_dignidade_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_direitos_idoso.get("")
async def i_direitos_idoso():
    return {"p":"psicoterapia_id_direitos_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dor_cronica_idoso2.get("")
async def i_dor_cronica_idoso2():
    return {"p":"psicoterapia_id_dor_cronica_idoso2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_engajamento_social_i.get("")
async def i_engajamento_social_i():
    return {"p":"psicoterapia_id_engajamento_social_i","s":"ativo","t":datetime.utcnow().isoformat()}
@router_escrita_criativa_ido.get("")
async def i_escrita_criativa_ido():
    return {"p":"psicoterapia_id_escrita_criativa_ido","s":"ativo","t":datetime.utcnow().isoformat()}
@router_espiritualidade_idos.get("")
async def i_espiritualidade_idos():
    return {"p":"psicoterapia_id_espiritualidade_idos","s":"ativo","t":datetime.utcnow().isoformat()}
@router_estimulacao_cognitiv.get("")
async def i_estimulacao_cognitiv():
    return {"p":"psicoterapia_id_estimulacao_cognitiv","s":"ativo","t":datetime.utcnow().isoformat()}
@router_exercicio_cognitivo.get("")
async def i_exercicio_cognitivo():
    return {"p":"psicoterapia_id_exercicio_cognitivo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fotos_terapia.get("")
async def i_fotos_terapia():
    return {"p":"psicoterapia_id_fotos_terapia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hidratacao_idoso.get("")
async def i_hidratacao_idoso():
    return {"p":"psicoterapia_id_hidratacao_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_historia_vida.get("")
async def i_historia_vida():
    return {"p":"psicoterapia_id_historia_vida","s":"ativo","t":datetime.utcnow().isoformat()}
@router_horta_idoso.get("")
async def i_horta_idoso():
    return {"p":"psicoterapia_id_horta_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_idioma_novo_idoso.get("")
async def i_idioma_novo_idoso():
    return {"p":"psicoterapia_id_idioma_novo_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_independencia_funcio.get("")
async def i_independencia_funcio():
    return {"p":"psicoterapia_id_independencia_funcio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_intergeracional_ativ.get("")
async def i_intergeracional_ativ():
    return {"p":"psicoterapia_id_intergeracional_ativ","s":"ativo","t":datetime.utcnow().isoformat()}
@router_jardinagem_idoso2.get("")
async def i_jardinagem_idoso2():
    return {"p":"psicoterapia_id_jardinagem_idoso2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_jogos_cognitivos.get("")
async def i_jogos_cognitivos():
    return {"p":"psicoterapia_id_jogos_cognitivos","s":"ativo","t":datetime.utcnow().isoformat()}
@router_legado_idoso3.get("")
async def i_legado_idoso3():
    return {"p":"psicoterapia_id_legado_idoso3","s":"ativo","t":datetime.utcnow().isoformat()}
@router_leitura_idoso.get("")
async def i_leitura_idoso():
    return {"p":"psicoterapia_id_leitura_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_linhas_tempo_idoso.get("")
async def i_linhas_tempo_idoso():
    return {"p":"psicoterapia_id_linhas_tempo_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_medicacao_gerenciame.get("")
async def i_medicacao_gerenciame():
    return {"p":"psicoterapia_id_medicacao_gerenciame","s":"ativo","t":datetime.utcnow().isoformat()}
@router_meditacao_idoso2.get("")
async def i_meditacao_idoso2():
    return {"p":"psicoterapia_id_meditacao_idoso2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mentorado_idoso.get("")
async def i_mentorado_idoso():
    return {"p":"psicoterapia_id_mentorado_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mobilidade_idoso.get("")
async def i_mobilidade_idoso():
    return {"p":"psicoterapia_id_mobilidade_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_musica_aprendizado_i.get("")
async def i_musica_aprendizado_i():
    return {"p":"psicoterapia_id_musica_aprendizado_i","s":"ativo","t":datetime.utcnow().isoformat()}
@router_musica_idoso.get("")
async def i_musica_idoso():
    return {"p":"psicoterapia_id_musica_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_musica_memoria.get("")
async def i_musica_memoria():
    return {"p":"psicoterapia_id_musica_memoria","s":"ativo","t":datetime.utcnow().isoformat()}
@router_narrativa_idoso.get("")
async def i_narrativa_idoso():
    return {"p":"psicoterapia_id_narrativa_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_natacao_idoso.get("")
async def i_natacao_idoso():
    return {"p":"psicoterapia_id_natacao_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_natureza_idoso.get("")
async def i_natureza_idoso():
    return {"p":"psicoterapia_id_natureza_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nutricao_idoso.get("")
async def i_nutricao_idoso():
    return {"p":"psicoterapia_id_nutricao_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_objetos_significativ.get("")
async def i_objetos_significativ():
    return {"p":"psicoterapia_id_objetos_significativ","s":"ativo","t":datetime.utcnow().isoformat()}
@router_palavras_cruzadas.get("")
async def i_palavras_cruzadas():
    return {"p":"psicoterapia_id_palavras_cruzadas","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pet_therapy_idoso.get("")
async def i_pet_therapy_idoso():
    return {"p":"psicoterapia_id_pet_therapy_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pilates_idoso.get("")
async def i_pilates_idoso():
    return {"p":"psicoterapia_id_pilates_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_polifarmacia_manejo.get("")
async def i_polifarmacia_manejo():
    return {"p":"psicoterapia_id_polifarmacia_manejo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_projeto_significativ.get("")
async def i_projeto_significativ():
    return {"p":"psicoterapia_id_projeto_significativ","s":"ativo","t":datetime.utcnow().isoformat()}
@router_religiao_idoso.get("")
async def i_religiao_idoso():
    return {"p":"psicoterapia_id_religiao_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reminiscencia2.get("")
async def i_reminiscencia2():
    return {"p":"psicoterapia_id_reminiscencia2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_revisao_vida2.get("")
async def i_revisao_vida2():
    return {"p":"psicoterapia_id_revisao_vida2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sabedoria_transmissa.get("")
async def i_sabedoria_transmissa():
    return {"p":"psicoterapia_id_sabedoria_transmissa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_social_media_idoso.get("")
async def i_social_media_idoso():
    return {"p":"psicoterapia_id_social_media_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sono_higiene_idoso.get("")
async def i_sono_higiene_idoso():
    return {"p":"psicoterapia_id_sono_higiene_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sudoku_mental.get("")
async def i_sudoku_mental():
    return {"p":"psicoterapia_id_sudoku_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tai_chi_idoso.get("")
async def i_tai_chi_idoso():
    return {"p":"psicoterapia_id_tai_chi_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tecnologia_idoso2.get("")
async def i_tecnologia_idoso2():
    return {"p":"psicoterapia_id_tecnologia_idoso2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_terapia_retro.get("")
async def i_terapia_retro():
    return {"p":"psicoterapia_id_terapia_retro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_treino_memoria_idoso.get("")
async def i_treino_memoria_idoso():
    return {"p":"psicoterapia_id_treino_memoria_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_turismo_terapeutico.get("")
async def i_turismo_terapeutico():
    return {"p":"psicoterapia_id_turismo_terapeutico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_viagem_idoso.get("")
async def i_viagem_idoso():
    return {"p":"psicoterapia_id_viagem_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_videochamada_idoso.get("")
async def i_videochamada_idoso():
    return {"p":"psicoterapia_id_videochamada_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_voluntariado_idoso.get("")
async def i_voluntariado_idoso():
    return {"p":"psicoterapia_id_voluntariado_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_xadrez_mental.get("")
async def i_xadrez_mental():
    return {"p":"psicoterapia_id_xadrez_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_yoga_idoso.get("")
async def i_yoga_idoso():
    return {"p":"psicoterapia_id_yoga_idoso","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_psicoterapia_idosos_(PluginBase):
    name = "consolidated_psicoterapia_idosos_tecnicas"
    def setup(self, app):
        app.include_router(router_alianca_idoso)
        app.include_router(router_animais_idoso)
        app.include_router(router_arte_idoso)
        app.include_router(router_atividade_fisica_ido)
        app.include_router(router_autobiografia_terape)
        app.include_router(router_autocuidado_idoso)
        app.include_router(router_autonomia_idoso2)
        app.include_router(router_bordado_idoso)
        app.include_router(router_caminhada_idoso)
        app.include_router(router_cartas_terapia_idoso)
        app.include_router(router_compliance_medicacao)
        app.include_router(router_computador_idoso)
        app.include_router(router_contemplacao_idoso)
        app.include_router(router_culinaria_idoso)
        app.include_router(router_curso_novo_idoso)
        app.include_router(router_danca_idoso)
        app.include_router(router_dignidade_idoso)
        app.include_router(router_direitos_idoso)
        app.include_router(router_dor_cronica_idoso2)
        app.include_router(router_engajamento_social_i)
        app.include_router(router_escrita_criativa_ido)
        app.include_router(router_espiritualidade_idos)
        app.include_router(router_estimulacao_cognitiv)
        app.include_router(router_exercicio_cognitivo)
        app.include_router(router_fotos_terapia)
        app.include_router(router_hidratacao_idoso)
        app.include_router(router_historia_vida)
        app.include_router(router_horta_idoso)
        app.include_router(router_idioma_novo_idoso)
        app.include_router(router_independencia_funcio)
        app.include_router(router_intergeracional_ativ)
        app.include_router(router_jardinagem_idoso2)
        app.include_router(router_jogos_cognitivos)
        app.include_router(router_legado_idoso3)
        app.include_router(router_leitura_idoso)
        app.include_router(router_linhas_tempo_idoso)
        app.include_router(router_medicacao_gerenciame)
        app.include_router(router_meditacao_idoso2)
        app.include_router(router_mentorado_idoso)
        app.include_router(router_mobilidade_idoso)
        app.include_router(router_musica_aprendizado_i)
        app.include_router(router_musica_idoso)
        app.include_router(router_musica_memoria)
        app.include_router(router_narrativa_idoso)
        app.include_router(router_natacao_idoso)
        app.include_router(router_natureza_idoso)
        app.include_router(router_nutricao_idoso)
        app.include_router(router_objetos_significativ)
        app.include_router(router_palavras_cruzadas)
        app.include_router(router_pet_therapy_idoso)
        app.include_router(router_pilates_idoso)
        app.include_router(router_polifarmacia_manejo)
        app.include_router(router_projeto_significativ)
        app.include_router(router_religiao_idoso)
        app.include_router(router_reminiscencia2)
        app.include_router(router_revisao_vida2)
        app.include_router(router_sabedoria_transmissa)
        app.include_router(router_social_media_idoso)
        app.include_router(router_sono_higiene_idoso)
        app.include_router(router_sudoku_mental)
        app.include_router(router_tai_chi_idoso)
        app.include_router(router_tecnologia_idoso2)
        app.include_router(router_terapia_retro)
        app.include_router(router_treino_memoria_idoso)
        app.include_router(router_turismo_terapeutico)
        app.include_router(router_viagem_idoso)
        app.include_router(router_videochamada_idoso)
        app.include_router(router_voluntariado_idoso)
        app.include_router(router_xadrez_mental)
        app.include_router(router_yoga_idoso)


plugin = Plugin_psicoterapia_idosos_()
