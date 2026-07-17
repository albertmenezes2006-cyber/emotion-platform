from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_anulacao = APIRouter(prefix="/api/v1/abordagens_t/anulacao", tags=["abordagens_terapeuticas_especificas"])
router_aprofundamento_hipno = APIRouter(prefix="/api/v1/abordagens_t/aprofundamento_hipnotico", tags=["abordagens_terapeuticas_especificas"])
router_autohipnose = APIRouter(prefix="/api/v1/abordagens_t/autohipnose", tags=["abordagens_terapeuticas_especificas"])
router_auxiliar = APIRouter(prefix="/api/v1/abordagens_t/auxiliar", tags=["abordagens_terapeuticas_especificas"])
router_awareness = APIRouter(prefix="/api/v1/abordagens_t/awareness", tags=["abordagens_terapeuticas_especificas"])
router_axiodrama = APIRouter(prefix="/api/v1/abordagens_t/axiodrama", tags=["abordagens_terapeuticas_especificas"])
router_bibliodrama = APIRouter(prefix="/api/v1/abordagens_t/bibliodrama", tags=["abordagens_terapeuticas_especificas"])
router_bion_clinico = APIRouter(prefix="/api/v1/abordagens_t/bion_clinico", tags=["abordagens_terapeuticas_especificas"])
router_catarse_psicodrama = APIRouter(prefix="/api/v1/abordagens_t/catarse_psicodrama", tags=["abordagens_terapeuticas_especificas"])
router_cisão = APIRouter(prefix="/api/v1/abordagens_t/cisão", tags=["abordagens_terapeuticas_especificas"])
router_confluencia_gestalt = APIRouter(prefix="/api/v1/abordagens_t/confluencia_gestalt", tags=["abordagens_terapeuticas_especificas"])
router_contato_gestalt = APIRouter(prefix="/api/v1/abordagens_t/contato_gestalt", tags=["abordagens_terapeuticas_especificas"])
router_conversao_clinica = APIRouter(prefix="/api/v1/abordagens_t/conversao_clinica", tags=["abordagens_terapeuticas_especificas"])
router_defflexao = APIRouter(prefix="/api/v1/abordagens_t/defflexao", tags=["abordagens_terapeuticas_especificas"])
router_deslocamento = APIRouter(prefix="/api/v1/abordagens_t/deslocamento", tags=["abordagens_terapeuticas_especificas"])
router_diretor_psicodrama = APIRouter(prefix="/api/v1/abordagens_t/diretor_psicodrama", tags=["abordagens_terapeuticas_especificas"])
router_dissociacao_defesa = APIRouter(prefix="/api/v1/abordagens_t/dissociacao_defesa", tags=["abordagens_terapeuticas_especificas"])
router_ego_defenses_avancad = APIRouter(prefix="/api/v1/abordagens_t/ego_defenses_avancado", tags=["abordagens_terapeuticas_especificas"])
router_ego_psychology = APIRouter(prefix="/api/v1/abordagens_t/ego_psychology", tags=["abordagens_terapeuticas_especificas"])
router_egotismo_gestalt = APIRouter(prefix="/api/v1/abordagens_t/egotismo_gestalt", tags=["abordagens_terapeuticas_especificas"])
router_experimento_gestalt = APIRouter(prefix="/api/v1/abordagens_t/experimento_gestalt", tags=["abordagens_terapeuticas_especificas"])
router_field_theory = APIRouter(prefix="/api/v1/abordagens_t/field_theory", tags=["abordagens_terapeuticas_especificas"])
router_figura_fundo2 = APIRouter(prefix="/api/v1/abordagens_t/figura_fundo2", tags=["abordagens_terapeuticas_especificas"])
router_forcluisao = APIRouter(prefix="/api/v1/abordagens_t/forcluisao", tags=["abordagens_terapeuticas_especificas"])
router_formacao_reativa = APIRouter(prefix="/api/v1/abordagens_t/formacao_reativa", tags=["abordagens_terapeuticas_especificas"])
router_fronteira_contato = APIRouter(prefix="/api/v1/abordagens_t/fronteira_contato", tags=["abordagens_terapeuticas_especificas"])
router_gestalt_terapia2 = APIRouter(prefix="/api/v1/abordagens_t/gestalt_terapia2", tags=["abordagens_terapeuticas_especificas"])
router_heinz_hartmann = APIRouter(prefix="/api/v1/abordagens_t/heinz_hartmann", tags=["abordagens_terapeuticas_especificas"])
router_hipnose_ansiedade = APIRouter(prefix="/api/v1/abordagens_t/hipnose_ansiedade", tags=["abordagens_terapeuticas_especificas"])
router_hipnose_clinica2 = APIRouter(prefix="/api/v1/abordagens_t/hipnose_clinica2", tags=["abordagens_terapeuticas_especificas"])
router_hipnose_crianca = APIRouter(prefix="/api/v1/abordagens_t/hipnose_crianca", tags=["abordagens_terapeuticas_especificas"])
router_hipnose_dor = APIRouter(prefix="/api/v1/abordagens_t/hipnose_dor", tags=["abordagens_terapeuticas_especificas"])
router_hipnose_ericksoniana = APIRouter(prefix="/api/v1/abordagens_t/hipnose_ericksoniana", tags=["abordagens_terapeuticas_especificas"])
router_hipnose_esportiva = APIRouter(prefix="/api/v1/abordagens_t/hipnose_esportiva", tags=["abordagens_terapeuticas_especificas"])
router_hipnose_grupo = APIRouter(prefix="/api/v1/abordagens_t/hipnose_grupo", tags=["abordagens_terapeuticas_especificas"])
router_hipnose_habitos = APIRouter(prefix="/api/v1/abordagens_t/hipnose_habitos", tags=["abordagens_terapeuticas_especificas"])
router_hipnose_medica = APIRouter(prefix="/api/v1/abordagens_t/hipnose_medica", tags=["abordagens_terapeuticas_especificas"])
router_hipnoterapia2 = APIRouter(prefix="/api/v1/abordagens_t/hipnoterapia2", tags=["abordagens_terapeuticas_especificas"])
router_identificacao_projet = APIRouter(prefix="/api/v1/abordagens_t/identificacao_projetiva", tags=["abordagens_terapeuticas_especificas"])
router_inducao_hipnotica = APIRouter(prefix="/api/v1/abordagens_t/inducao_hipnotica", tags=["abordagens_terapeuticas_especificas"])
router_insight_psicodrama = APIRouter(prefix="/api/v1/abordagens_t/insight_psicodrama", tags=["abordagens_terapeuticas_especificas"])
router_integracao_psicodram = APIRouter(prefix="/api/v1/abordagens_t/integracao_psicodrama", tags=["abordagens_terapeuticas_especificas"])
router_intelectualizacao = APIRouter(prefix="/api/v1/abordagens_t/intelectualizacao", tags=["abordagens_terapeuticas_especificas"])
router_introjeto = APIRouter(prefix="/api/v1/abordagens_t/introjeto", tags=["abordagens_terapeuticas_especificas"])
router_introprojecao = APIRouter(prefix="/api/v1/abordagens_t/introprojecao", tags=["abordagens_terapeuticas_especificas"])
router_kohut_self = APIRouter(prefix="/api/v1/abordagens_t/kohut_self", tags=["abordagens_terapeuticas_especificas"])
router_mecanismos_defesa2 = APIRouter(prefix="/api/v1/abordagens_t/mecanismos_defesa2", tags=["abordagens_terapeuticas_especificas"])
router_metafora_hipnotica = APIRouter(prefix="/api/v1/abordagens_t/metafora_hipnotica", tags=["abordagens_terapeuticas_especificas"])
router_moreniano = APIRouter(prefix="/api/v1/abordagens_t/moreniano", tags=["abordagens_terapeuticas_especificas"])
router_negacao = APIRouter(prefix="/api/v1/abordagens_t/negacao", tags=["abordagens_terapeuticas_especificas"])
router_objeto_relacional = APIRouter(prefix="/api/v1/abordagens_t/objeto_relacional", tags=["abordagens_terapeuticas_especificas"])
router_playback_theatre = APIRouter(prefix="/api/v1/abordagens_t/playback_theatre", tags=["abordagens_terapeuticas_especificas"])
router_pos_hipnotica = APIRouter(prefix="/api/v1/abordagens_t/pos_hipnotica", tags=["abordagens_terapeuticas_especificas"])
router_proflexao = APIRouter(prefix="/api/v1/abordagens_t/proflexao", tags=["abordagens_terapeuticas_especificas"])
router_projecao_clinica = APIRouter(prefix="/api/v1/abordagens_t/projecao_clinica", tags=["abordagens_terapeuticas_especificas"])
router_protagonista = APIRouter(prefix="/api/v1/abordagens_t/protagonista", tags=["abordagens_terapeuticas_especificas"])
router_psicoanalise_freudia = APIRouter(prefix="/api/v1/abordagens_t/psicoanalise_freudiana", tags=["abordagens_terapeuticas_especificas"])
router_psicoanalise_kleinia = APIRouter(prefix="/api/v1/abordagens_t/psicoanalise_kleiniana", tags=["abordagens_terapeuticas_especificas"])
router_psicoanalise_lacania = APIRouter(prefix="/api/v1/abordagens_t/psicoanalise_lacaniana", tags=["abordagens_terapeuticas_especificas"])
router_psicodrama = APIRouter(prefix="/api/v1/abordagens_t/psicodrama", tags=["abordagens_terapeuticas_especificas"])
router_psicodrama_grupais = APIRouter(prefix="/api/v1/abordagens_t/psicodrama_grupais", tags=["abordagens_terapeuticas_especificas"])
router_psicologia_analitica = APIRouter(prefix="/api/v1/abordagens_t/psicologia_analitica2", tags=["abordagens_terapeuticas_especificas"])
router_psicologia_individua = APIRouter(prefix="/api/v1/abordagens_t/psicologia_individual_adl", tags=["abordagens_terapeuticas_especificas"])
router_psicologia_self = APIRouter(prefix="/api/v1/abordagens_t/psicologia_self", tags=["abordagens_terapeuticas_especificas"])
router_racionalizacao = APIRouter(prefix="/api/v1/abordagens_t/racionalizacao", tags=["abordagens_terapeuticas_especificas"])
router_regressao_clinica = APIRouter(prefix="/api/v1/abordagens_t/regressao_clinica", tags=["abordagens_terapeuticas_especificas"])
router_regressao_vida_passa = APIRouter(prefix="/api/v1/abordagens_t/regressao_vida_passada_in", tags=["abordagens_terapeuticas_especificas"])
router_repressao = APIRouter(prefix="/api/v1/abordagens_t/repressao", tags=["abordagens_terapeuticas_especificas"])
router_retroflexao = APIRouter(prefix="/api/v1/abordagens_t/retroflexao", tags=["abordagens_terapeuticas_especificas"])
router_role_playing2 = APIRouter(prefix="/api/v1/abordagens_t/role_playing2", tags=["abordagens_terapeuticas_especificas"])
router_sociodrama = APIRouter(prefix="/api/v1/abordagens_t/sociodrama", tags=["abordagens_terapeuticas_especificas"])
router_sociometria = APIRouter(prefix="/api/v1/abordagens_t/sociometria", tags=["abordagens_terapeuticas_especificas"])
router_somatizacao_defesa = APIRouter(prefix="/api/v1/abordagens_t/somatizacao_defesa", tags=["abordagens_terapeuticas_especificas"])
router_sublimacao = APIRouter(prefix="/api/v1/abordagens_t/sublimacao", tags=["abordagens_terapeuticas_especificas"])
router_sugestao_hipnotica = APIRouter(prefix="/api/v1/abordagens_t/sugestao_hipnotica", tags=["abordagens_terapeuticas_especificas"])
router_supressao = APIRouter(prefix="/api/v1/abordagens_t/supressao", tags=["abordagens_terapeuticas_especificas"])
router_tele_sociodrama = APIRouter(prefix="/api/v1/abordagens_t/tele_sociodrama", tags=["abordagens_terapeuticas_especificas"])
router_teoria_objeto = APIRouter(prefix="/api/v1/abordagens_t/teoria_objeto", tags=["abordagens_terapeuticas_especificas"])
router_theatre_oppressed = APIRouter(prefix="/api/v1/abordagens_t/theatre_oppressed", tags=["abordagens_terapeuticas_especificas"])
router_trabalho_sonhos_gest = APIRouter(prefix="/api/v1/abordagens_t/trabalho_sonhos_gestalt", tags=["abordagens_terapeuticas_especificas"])
router_transe_terapeutico = APIRouter(prefix="/api/v1/abordagens_t/transe_terapeutico", tags=["abordagens_terapeuticas_especificas"])
router_winnicott_clinico = APIRouter(prefix="/api/v1/abordagens_t/winnicott_clinico", tags=["abordagens_terapeuticas_especificas"])

@router_anulacao.get("")
async def i_anulacao():
    return {"p":"abordagens_tera_anulacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_aprofundamento_hipno.get("")
async def i_aprofundamento_hipno():
    return {"p":"abordagens_tera_aprofundamento_hipno","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autohipnose.get("")
async def i_autohipnose():
    return {"p":"abordagens_tera_autohipnose","s":"ativo","t":datetime.utcnow().isoformat()}
@router_auxiliar.get("")
async def i_auxiliar():
    return {"p":"abordagens_tera_auxiliar","s":"ativo","t":datetime.utcnow().isoformat()}
@router_awareness.get("")
async def i_awareness():
    return {"p":"abordagens_tera_awareness","s":"ativo","t":datetime.utcnow().isoformat()}
@router_axiodrama.get("")
async def i_axiodrama():
    return {"p":"abordagens_tera_axiodrama","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bibliodrama.get("")
async def i_bibliodrama():
    return {"p":"abordagens_tera_bibliodrama","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bion_clinico.get("")
async def i_bion_clinico():
    return {"p":"abordagens_tera_bion_clinico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_catarse_psicodrama.get("")
async def i_catarse_psicodrama():
    return {"p":"abordagens_tera_catarse_psicodrama","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cisão.get("")
async def i_cisão():
    return {"p":"abordagens_tera_cisão","s":"ativo","t":datetime.utcnow().isoformat()}
@router_confluencia_gestalt.get("")
async def i_confluencia_gestalt():
    return {"p":"abordagens_tera_confluencia_gestalt","s":"ativo","t":datetime.utcnow().isoformat()}
@router_contato_gestalt.get("")
async def i_contato_gestalt():
    return {"p":"abordagens_tera_contato_gestalt","s":"ativo","t":datetime.utcnow().isoformat()}
@router_conversao_clinica.get("")
async def i_conversao_clinica():
    return {"p":"abordagens_tera_conversao_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_defflexao.get("")
async def i_defflexao():
    return {"p":"abordagens_tera_defflexao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_deslocamento.get("")
async def i_deslocamento():
    return {"p":"abordagens_tera_deslocamento","s":"ativo","t":datetime.utcnow().isoformat()}
@router_diretor_psicodrama.get("")
async def i_diretor_psicodrama():
    return {"p":"abordagens_tera_diretor_psicodrama","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dissociacao_defesa.get("")
async def i_dissociacao_defesa():
    return {"p":"abordagens_tera_dissociacao_defesa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ego_defenses_avancad.get("")
async def i_ego_defenses_avancad():
    return {"p":"abordagens_tera_ego_defenses_avancad","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ego_psychology.get("")
async def i_ego_psychology():
    return {"p":"abordagens_tera_ego_psychology","s":"ativo","t":datetime.utcnow().isoformat()}
@router_egotismo_gestalt.get("")
async def i_egotismo_gestalt():
    return {"p":"abordagens_tera_egotismo_gestalt","s":"ativo","t":datetime.utcnow().isoformat()}
@router_experimento_gestalt.get("")
async def i_experimento_gestalt():
    return {"p":"abordagens_tera_experimento_gestalt","s":"ativo","t":datetime.utcnow().isoformat()}
@router_field_theory.get("")
async def i_field_theory():
    return {"p":"abordagens_tera_field_theory","s":"ativo","t":datetime.utcnow().isoformat()}
@router_figura_fundo2.get("")
async def i_figura_fundo2():
    return {"p":"abordagens_tera_figura_fundo2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_forcluisao.get("")
async def i_forcluisao():
    return {"p":"abordagens_tera_forcluisao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_formacao_reativa.get("")
async def i_formacao_reativa():
    return {"p":"abordagens_tera_formacao_reativa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fronteira_contato.get("")
async def i_fronteira_contato():
    return {"p":"abordagens_tera_fronteira_contato","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gestalt_terapia2.get("")
async def i_gestalt_terapia2():
    return {"p":"abordagens_tera_gestalt_terapia2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_heinz_hartmann.get("")
async def i_heinz_hartmann():
    return {"p":"abordagens_tera_heinz_hartmann","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hipnose_ansiedade.get("")
async def i_hipnose_ansiedade():
    return {"p":"abordagens_tera_hipnose_ansiedade","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hipnose_clinica2.get("")
async def i_hipnose_clinica2():
    return {"p":"abordagens_tera_hipnose_clinica2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hipnose_crianca.get("")
async def i_hipnose_crianca():
    return {"p":"abordagens_tera_hipnose_crianca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hipnose_dor.get("")
async def i_hipnose_dor():
    return {"p":"abordagens_tera_hipnose_dor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hipnose_ericksoniana.get("")
async def i_hipnose_ericksoniana():
    return {"p":"abordagens_tera_hipnose_ericksoniana","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hipnose_esportiva.get("")
async def i_hipnose_esportiva():
    return {"p":"abordagens_tera_hipnose_esportiva","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hipnose_grupo.get("")
async def i_hipnose_grupo():
    return {"p":"abordagens_tera_hipnose_grupo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hipnose_habitos.get("")
async def i_hipnose_habitos():
    return {"p":"abordagens_tera_hipnose_habitos","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hipnose_medica.get("")
async def i_hipnose_medica():
    return {"p":"abordagens_tera_hipnose_medica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hipnoterapia2.get("")
async def i_hipnoterapia2():
    return {"p":"abordagens_tera_hipnoterapia2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_identificacao_projet.get("")
async def i_identificacao_projet():
    return {"p":"abordagens_tera_identificacao_projet","s":"ativo","t":datetime.utcnow().isoformat()}
@router_inducao_hipnotica.get("")
async def i_inducao_hipnotica():
    return {"p":"abordagens_tera_inducao_hipnotica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_insight_psicodrama.get("")
async def i_insight_psicodrama():
    return {"p":"abordagens_tera_insight_psicodrama","s":"ativo","t":datetime.utcnow().isoformat()}
@router_integracao_psicodram.get("")
async def i_integracao_psicodram():
    return {"p":"abordagens_tera_integracao_psicodram","s":"ativo","t":datetime.utcnow().isoformat()}
@router_intelectualizacao.get("")
async def i_intelectualizacao():
    return {"p":"abordagens_tera_intelectualizacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_introjeto.get("")
async def i_introjeto():
    return {"p":"abordagens_tera_introjeto","s":"ativo","t":datetime.utcnow().isoformat()}
@router_introprojecao.get("")
async def i_introprojecao():
    return {"p":"abordagens_tera_introprojecao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_kohut_self.get("")
async def i_kohut_self():
    return {"p":"abordagens_tera_kohut_self","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mecanismos_defesa2.get("")
async def i_mecanismos_defesa2():
    return {"p":"abordagens_tera_mecanismos_defesa2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_metafora_hipnotica.get("")
async def i_metafora_hipnotica():
    return {"p":"abordagens_tera_metafora_hipnotica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_moreniano.get("")
async def i_moreniano():
    return {"p":"abordagens_tera_moreniano","s":"ativo","t":datetime.utcnow().isoformat()}
@router_negacao.get("")
async def i_negacao():
    return {"p":"abordagens_tera_negacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_objeto_relacional.get("")
async def i_objeto_relacional():
    return {"p":"abordagens_tera_objeto_relacional","s":"ativo","t":datetime.utcnow().isoformat()}
@router_playback_theatre.get("")
async def i_playback_theatre():
    return {"p":"abordagens_tera_playback_theatre","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pos_hipnotica.get("")
async def i_pos_hipnotica():
    return {"p":"abordagens_tera_pos_hipnotica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_proflexao.get("")
async def i_proflexao():
    return {"p":"abordagens_tera_proflexao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_projecao_clinica.get("")
async def i_projecao_clinica():
    return {"p":"abordagens_tera_projecao_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_protagonista.get("")
async def i_protagonista():
    return {"p":"abordagens_tera_protagonista","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicoanalise_freudia.get("")
async def i_psicoanalise_freudia():
    return {"p":"abordagens_tera_psicoanalise_freudia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicoanalise_kleinia.get("")
async def i_psicoanalise_kleinia():
    return {"p":"abordagens_tera_psicoanalise_kleinia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicoanalise_lacania.get("")
async def i_psicoanalise_lacania():
    return {"p":"abordagens_tera_psicoanalise_lacania","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicodrama.get("")
async def i_psicodrama():
    return {"p":"abordagens_tera_psicodrama","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicodrama_grupais.get("")
async def i_psicodrama_grupais():
    return {"p":"abordagens_tera_psicodrama_grupais","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicologia_analitica.get("")
async def i_psicologia_analitica():
    return {"p":"abordagens_tera_psicologia_analitica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicologia_individua.get("")
async def i_psicologia_individua():
    return {"p":"abordagens_tera_psicologia_individua","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psicologia_self.get("")
async def i_psicologia_self():
    return {"p":"abordagens_tera_psicologia_self","s":"ativo","t":datetime.utcnow().isoformat()}
@router_racionalizacao.get("")
async def i_racionalizacao():
    return {"p":"abordagens_tera_racionalizacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_regressao_clinica.get("")
async def i_regressao_clinica():
    return {"p":"abordagens_tera_regressao_clinica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_regressao_vida_passa.get("")
async def i_regressao_vida_passa():
    return {"p":"abordagens_tera_regressao_vida_passa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_repressao.get("")
async def i_repressao():
    return {"p":"abordagens_tera_repressao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_retroflexao.get("")
async def i_retroflexao():
    return {"p":"abordagens_tera_retroflexao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_role_playing2.get("")
async def i_role_playing2():
    return {"p":"abordagens_tera_role_playing2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sociodrama.get("")
async def i_sociodrama():
    return {"p":"abordagens_tera_sociodrama","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sociometria.get("")
async def i_sociometria():
    return {"p":"abordagens_tera_sociometria","s":"ativo","t":datetime.utcnow().isoformat()}
@router_somatizacao_defesa.get("")
async def i_somatizacao_defesa():
    return {"p":"abordagens_tera_somatizacao_defesa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sublimacao.get("")
async def i_sublimacao():
    return {"p":"abordagens_tera_sublimacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sugestao_hipnotica.get("")
async def i_sugestao_hipnotica():
    return {"p":"abordagens_tera_sugestao_hipnotica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_supressao.get("")
async def i_supressao():
    return {"p":"abordagens_tera_supressao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tele_sociodrama.get("")
async def i_tele_sociodrama():
    return {"p":"abordagens_tera_tele_sociodrama","s":"ativo","t":datetime.utcnow().isoformat()}
@router_teoria_objeto.get("")
async def i_teoria_objeto():
    return {"p":"abordagens_tera_teoria_objeto","s":"ativo","t":datetime.utcnow().isoformat()}
@router_theatre_oppressed.get("")
async def i_theatre_oppressed():
    return {"p":"abordagens_tera_theatre_oppressed","s":"ativo","t":datetime.utcnow().isoformat()}
@router_trabalho_sonhos_gest.get("")
async def i_trabalho_sonhos_gest():
    return {"p":"abordagens_tera_trabalho_sonhos_gest","s":"ativo","t":datetime.utcnow().isoformat()}
@router_transe_terapeutico.get("")
async def i_transe_terapeutico():
    return {"p":"abordagens_tera_transe_terapeutico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_winnicott_clinico.get("")
async def i_winnicott_clinico():
    return {"p":"abordagens_tera_winnicott_clinico","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_abordagens_terapeuti(PluginBase):
    name = "consolidated_abordagens_terapeuticas_especi"
    def setup(self, app):
        app.include_router(router_anulacao)
        app.include_router(router_aprofundamento_hipno)
        app.include_router(router_autohipnose)
        app.include_router(router_auxiliar)
        app.include_router(router_awareness)
        app.include_router(router_axiodrama)
        app.include_router(router_bibliodrama)
        app.include_router(router_bion_clinico)
        app.include_router(router_catarse_psicodrama)
        app.include_router(router_cisão)
        app.include_router(router_confluencia_gestalt)
        app.include_router(router_contato_gestalt)
        app.include_router(router_conversao_clinica)
        app.include_router(router_defflexao)
        app.include_router(router_deslocamento)
        app.include_router(router_diretor_psicodrama)
        app.include_router(router_dissociacao_defesa)
        app.include_router(router_ego_defenses_avancad)
        app.include_router(router_ego_psychology)
        app.include_router(router_egotismo_gestalt)
        app.include_router(router_experimento_gestalt)
        app.include_router(router_field_theory)
        app.include_router(router_figura_fundo2)
        app.include_router(router_forcluisao)
        app.include_router(router_formacao_reativa)
        app.include_router(router_fronteira_contato)
        app.include_router(router_gestalt_terapia2)
        app.include_router(router_heinz_hartmann)
        app.include_router(router_hipnose_ansiedade)
        app.include_router(router_hipnose_clinica2)
        app.include_router(router_hipnose_crianca)
        app.include_router(router_hipnose_dor)
        app.include_router(router_hipnose_ericksoniana)
        app.include_router(router_hipnose_esportiva)
        app.include_router(router_hipnose_grupo)
        app.include_router(router_hipnose_habitos)
        app.include_router(router_hipnose_medica)
        app.include_router(router_hipnoterapia2)
        app.include_router(router_identificacao_projet)
        app.include_router(router_inducao_hipnotica)
        app.include_router(router_insight_psicodrama)
        app.include_router(router_integracao_psicodram)
        app.include_router(router_intelectualizacao)
        app.include_router(router_introjeto)
        app.include_router(router_introprojecao)
        app.include_router(router_kohut_self)
        app.include_router(router_mecanismos_defesa2)
        app.include_router(router_metafora_hipnotica)
        app.include_router(router_moreniano)
        app.include_router(router_negacao)
        app.include_router(router_objeto_relacional)
        app.include_router(router_playback_theatre)
        app.include_router(router_pos_hipnotica)
        app.include_router(router_proflexao)
        app.include_router(router_projecao_clinica)
        app.include_router(router_protagonista)
        app.include_router(router_psicoanalise_freudia)
        app.include_router(router_psicoanalise_kleinia)
        app.include_router(router_psicoanalise_lacania)
        app.include_router(router_psicodrama)
        app.include_router(router_psicodrama_grupais)
        app.include_router(router_psicologia_analitica)
        app.include_router(router_psicologia_individua)
        app.include_router(router_psicologia_self)
        app.include_router(router_racionalizacao)
        app.include_router(router_regressao_clinica)
        app.include_router(router_regressao_vida_passa)
        app.include_router(router_repressao)
        app.include_router(router_retroflexao)
        app.include_router(router_role_playing2)
        app.include_router(router_sociodrama)
        app.include_router(router_sociometria)
        app.include_router(router_somatizacao_defesa)
        app.include_router(router_sublimacao)
        app.include_router(router_sugestao_hipnotica)
        app.include_router(router_supressao)
        app.include_router(router_tele_sociodrama)
        app.include_router(router_teoria_objeto)
        app.include_router(router_theatre_oppressed)
        app.include_router(router_trabalho_sonhos_gest)
        app.include_router(router_transe_terapeutico)
        app.include_router(router_winnicott_clinico)


plugin = Plugin_abordagens_terapeuti()
