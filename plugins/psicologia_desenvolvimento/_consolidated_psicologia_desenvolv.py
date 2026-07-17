from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_afeto_vitalidade = APIRouter(prefix="/api/v1/psicologia_d/afeto_vitalidade", tags=["psicologia_desenvolvimento"])
router_agressao_desenvolvim = APIRouter(prefix="/api/v1/psicologia_d/agressao_desenvolvimento", tags=["psicologia_desenvolvimento"])
router_ainsworth_estranha = APIRouter(prefix="/api/v1/psicologia_d/ainsworth_estranha", tags=["psicologia_desenvolvimento"])
router_altruismo_desenvolvi = APIRouter(prefix="/api/v1/psicologia_d/altruismo_desenvolvimento", tags=["psicologia_desenvolvimento"])
router_apego_ansioso_resist = APIRouter(prefix="/api/v1/psicologia_d/apego_ansioso_resistente", tags=["psicologia_desenvolvimento"])
router_apego_desorganizado_ = APIRouter(prefix="/api/v1/psicologia_d/apego_desorganizado_infan", tags=["psicologia_desenvolvimento"])
router_apego_evitativo_infa = APIRouter(prefix="/api/v1/psicologia_d/apego_evitativo_infantil", tags=["psicologia_desenvolvimento"])
router_apego_seguro_infanti = APIRouter(prefix="/api/v1/psicologia_d/apego_seguro_infantil", tags=["psicologia_desenvolvimento"])
router_autonomia_vergonha = APIRouter(prefix="/api/v1/psicologia_d/autonomia_vergonha", tags=["psicologia_desenvolvimento"])
router_base_segura = APIRouter(prefix="/api/v1/psicologia_d/base_segura", tags=["psicologia_desenvolvimento"])
router_bioecologico = APIRouter(prefix="/api/v1/psicologia_d/bioecologico", tags=["psicologia_desenvolvimento"])
router_bullying_desenvolvim = APIRouter(prefix="/api/v1/psicologia_d/bullying_desenvolvimento", tags=["psicologia_desenvolvimento"])
router_comportamento_apego = APIRouter(prefix="/api/v1/psicologia_d/comportamento_apego", tags=["psicologia_desenvolvimento"])
router_confianca_desconfian = APIRouter(prefix="/api/v1/psicologia_d/confianca_desconfianca", tags=["psicologia_desenvolvimento"])
router_consolidacao_individ = APIRouter(prefix="/api/v1/psicologia_d/consolidacao_individualid", tags=["psicologia_desenvolvimento"])
router_contingencia = APIRouter(prefix="/api/v1/psicologia_d/contingencia", tags=["psicologia_desenvolvimento"])
router_convencional_moral = APIRouter(prefix="/api/v1/psicologia_d/convencional_moral", tags=["psicologia_desenvolvimento"])
router_criacao_sentido = APIRouter(prefix="/api/v1/psicologia_d/criacao_sentido", tags=["psicologia_desenvolvimento"])
router_cronosistema = APIRouter(prefix="/api/v1/psicologia_d/cronosistema", tags=["psicologia_desenvolvimento"])
router_culpa_desenvolviment = APIRouter(prefix="/api/v1/psicologia_d/culpa_desenvolvimento", tags=["psicologia_desenvolvimento"])
router_desenvolvimento_mora = APIRouter(prefix="/api/v1/psicologia_d/desenvolvimento_moral", tags=["psicologia_desenvolvimento"])
router_desenvolvimento_soci = APIRouter(prefix="/api/v1/psicologia_d/desenvolvimento_sociocult", tags=["psicologia_desenvolvimento"])
router_dialogo_intersubjeti = APIRouter(prefix="/api/v1/psicologia_d/dialogo_intersubjetivo", tags=["psicologia_desenvolvimento"])
router_diferenciacao = APIRouter(prefix="/api/v1/psicologia_d/diferenciacao", tags=["psicologia_desenvolvimento"])
router_ecologia_desenvolvim = APIRouter(prefix="/api/v1/psicologia_d/ecologia_desenvolvimento", tags=["psicologia_desenvolvimento"])
router_empatia_cognitiva = APIRouter(prefix="/api/v1/psicologia_d/empatia_cognitiva", tags=["psicologia_desenvolvimento"])
router_empatia_desenvolvime = APIRouter(prefix="/api/v1/psicologia_d/empatia_desenvolvimento", tags=["psicologia_desenvolvimento"])
router_empatia_emocional = APIRouter(prefix="/api/v1/psicologia_d/empatia_emocional", tags=["psicologia_desenvolvimento"])
router_estadios_kohlberg = APIRouter(prefix="/api/v1/psicologia_d/estadios_kohlberg", tags=["psicologia_desenvolvimento"])
router_estágios_erikson = APIRouter(prefix="/api/v1/psicologia_d/estágios_erikson", tags=["psicologia_desenvolvimento"])
router_etica_cuidado = APIRouter(prefix="/api/v1/psicologia_d/etica_cuidado", tags=["psicologia_desenvolvimento"])
router_exosistema = APIRouter(prefix="/api/v1/psicologia_d/exosistema", tags=["psicologia_desenvolvimento"])
router_experiencia_interaca = APIRouter(prefix="/api/v1/psicologia_d/experiencia_interacao", tags=["psicologia_desenvolvimento"])
router_exploracao_apego = APIRouter(prefix="/api/v1/psicologia_d/exploracao_apego", tags=["psicologia_desenvolvimento"])
router_falsa_crenca = APIRouter(prefix="/api/v1/psicologia_d/falsa_crenca", tags=["psicologia_desenvolvimento"])
router_fase_simbiotica = APIRouter(prefix="/api/v1/psicologia_d/fase_simbiotica", tags=["psicologia_desenvolvimento"])
router_figura_apego = APIRouter(prefix="/api/v1/psicologia_d/figura_apego", tags=["psicologia_desenvolvimento"])
router_funcao_reflexiva = APIRouter(prefix="/api/v1/psicologia_d/funcao_reflexiva", tags=["psicologia_desenvolvimento"])
router_geratividade_estagna = APIRouter(prefix="/api/v1/psicologia_d/geratividade_estagnacao", tags=["psicologia_desenvolvimento"])
router_identidade_confusao = APIRouter(prefix="/api/v1/psicologia_d/identidade_confusao", tags=["psicologia_desenvolvimento"])
router_industria_inferiorid = APIRouter(prefix="/api/v1/psicologia_d/industria_inferioridade", tags=["psicologia_desenvolvimento"])
router_iniciativa_culpa = APIRouter(prefix="/api/v1/psicologia_d/iniciativa_culpa", tags=["psicologia_desenvolvimento"])
router_integridade_desesper = APIRouter(prefix="/api/v1/psicologia_d/integridade_desespero", tags=["psicologia_desenvolvimento"])
router_intimidade_isolament = APIRouter(prefix="/api/v1/psicologia_d/intimidade_isolamento", tags=["psicologia_desenvolvimento"])
router_joint_attention = APIRouter(prefix="/api/v1/psicologia_d/joint_attention", tags=["psicologia_desenvolvimento"])
router_juizo_moral = APIRouter(prefix="/api/v1/psicologia_d/juizo_moral", tags=["psicologia_desenvolvimento"])
router_luto_apego = APIRouter(prefix="/api/v1/psicologia_d/luto_apego", tags=["psicologia_desenvolvimento"])
router_macrosistema = APIRouter(prefix="/api/v1/psicologia_d/macrosistema", tags=["psicologia_desenvolvimento"])
router_marcacao = APIRouter(prefix="/api/v1/psicologia_d/marcacao", tags=["psicologia_desenvolvimento"])
router_mentalizacao_parenta = APIRouter(prefix="/api/v1/psicologia_d/mentalizacao_parental", tags=["psicologia_desenvolvimento"])
router_mente_reflexiva = APIRouter(prefix="/api/v1/psicologia_d/mente_reflexiva", tags=["psicologia_desenvolvimento"])
router_mesosistema = APIRouter(prefix="/api/v1/psicologia_d/mesosistema", tags=["psicologia_desenvolvimento"])
router_microsistema = APIRouter(prefix="/api/v1/psicologia_d/microsistema", tags=["psicologia_desenvolvimento"])
router_moral_emotion = APIRouter(prefix="/api/v1/psicologia_d/moral_emotion", tags=["psicologia_desenvolvimento"])
router_narrativo_si = APIRouter(prefix="/api/v1/psicologia_d/narrativo_si", tags=["psicologia_desenvolvimento"])
router_nucleo_si = APIRouter(prefix="/api/v1/psicologia_d/nucleo_si", tags=["psicologia_desenvolvimento"])
router_operatorio_concreto = APIRouter(prefix="/api/v1/psicologia_d/operatorio_concreto", tags=["psicologia_desenvolvimento"])
router_operatorio_formal = APIRouter(prefix="/api/v1/psicologia_d/operatorio_formal", tags=["psicologia_desenvolvimento"])
router_pensamento_linguagem = APIRouter(prefix="/api/v1/psicologia_d/pensamento_linguagem", tags=["psicologia_desenvolvimento"])
router_perda_apego = APIRouter(prefix="/api/v1/psicologia_d/perda_apego", tags=["psicologia_desenvolvimento"])
router_perspectiva_feminist = APIRouter(prefix="/api/v1/psicologia_d/perspectiva_feminista_mor", tags=["psicologia_desenvolvimento"])
router_perspectiva_taking = APIRouter(prefix="/api/v1/psicologia_d/perspectiva_taking", tags=["psicologia_desenvolvimento"])
router_porto_seguro = APIRouter(prefix="/api/v1/psicologia_d/porto_seguro", tags=["psicologia_desenvolvimento"])
router_posconvencional = APIRouter(prefix="/api/v1/psicologia_d/posconvencional", tags=["psicologia_desenvolvimento"])
router_praticando = APIRouter(prefix="/api/v1/psicologia_d/praticando", tags=["psicologia_desenvolvimento"])
router_preconvencional_mora = APIRouter(prefix="/api/v1/psicologia_d/preconvencional_moral", tags=["psicologia_desenvolvimento"])
router_preoperatorio_piaget = APIRouter(prefix="/api/v1/psicologia_d/preoperatorio_piaget", tags=["psicologia_desenvolvimento"])
router_prosocial_desenvolvi = APIRouter(prefix="/api/v1/psicologia_d/prosocial_desenvolvimento", tags=["psicologia_desenvolvimento"])
router_protoconversacao = APIRouter(prefix="/api/v1/psicologia_d/protoconversacao", tags=["psicologia_desenvolvimento"])
router_raciocinio_moral = APIRouter(prefix="/api/v1/psicologia_d/raciocinio_moral", tags=["psicologia_desenvolvimento"])
router_reaproximacao = APIRouter(prefix="/api/v1/psicologia_d/reaproximacao", tags=["psicologia_desenvolvimento"])
router_regulacao_emocional_ = APIRouter(prefix="/api/v1/psicologia_d/regulacao_emocional_desen", tags=["psicologia_desenvolvimento"])
router_reuniao_apego = APIRouter(prefix="/api/v1/psicologia_d/reuniao_apego", tags=["psicologia_desenvolvimento"])
router_scaffolding_vygotsky = APIRouter(prefix="/api/v1/psicologia_d/scaffolding_vygotsky", tags=["psicologia_desenvolvimento"])
router_sensoriomotor_piaget = APIRouter(prefix="/api/v1/psicologia_d/sensoriomotor_piaget", tags=["psicologia_desenvolvimento"])
router_sentido_si_emergente = APIRouter(prefix="/api/v1/psicologia_d/sentido_si_emergente", tags=["psicologia_desenvolvimento"])
router_separacao_apego = APIRouter(prefix="/api/v1/psicologia_d/separacao_apego", tags=["psicologia_desenvolvimento"])
router_separacao_individuac = APIRouter(prefix="/api/v1/psicologia_d/separacao_individuacao", tags=["psicologia_desenvolvimento"])
router_sincronia = APIRouter(prefix="/api/v1/psicologia_d/sincronia", tags=["psicologia_desenvolvimento"])
router_sistema_apego = APIRouter(prefix="/api/v1/psicologia_d/sistema_apego", tags=["psicologia_desenvolvimento"])
router_situacao_estranha = APIRouter(prefix="/api/v1/psicologia_d/situacao_estranha", tags=["psicologia_desenvolvimento"])
router_subjetivo_si = APIRouter(prefix="/api/v1/psicologia_d/subjetivo_si", tags=["psicologia_desenvolvimento"])
router_temperamento_dif = APIRouter(prefix="/api/v1/psicologia_d/temperamento_dif", tags=["psicologia_desenvolvimento"])
router_teoria_bowlby = APIRouter(prefix="/api/v1/psicologia_d/teoria_bowlby", tags=["psicologia_desenvolvimento"])
router_teoria_bronfenbrenne = APIRouter(prefix="/api/v1/psicologia_d/teoria_bronfenbrenner", tags=["psicologia_desenvolvimento"])
router_teoria_erikson = APIRouter(prefix="/api/v1/psicologia_d/teoria_erikson", tags=["psicologia_desenvolvimento"])
router_teoria_gilligan = APIRouter(prefix="/api/v1/psicologia_d/teoria_gilligan", tags=["psicologia_desenvolvimento"])
router_teoria_kohlberg = APIRouter(prefix="/api/v1/psicologia_d/teoria_kohlberg", tags=["psicologia_desenvolvimento"])
router_teoria_mahler = APIRouter(prefix="/api/v1/psicologia_d/teoria_mahler", tags=["psicologia_desenvolvimento"])
router_teoria_mente = APIRouter(prefix="/api/v1/psicologia_d/teoria_mente", tags=["psicologia_desenvolvimento"])
router_teoria_piaget = APIRouter(prefix="/api/v1/psicologia_d/teoria_piaget", tags=["psicologia_desenvolvimento"])
router_teoria_stern = APIRouter(prefix="/api/v1/psicologia_d/teoria_stern", tags=["psicologia_desenvolvimento"])
router_teoria_vygotsky = APIRouter(prefix="/api/v1/psicologia_d/teoria_vygotsky", tags=["psicologia_desenvolvimento"])
router_transmissao_apego = APIRouter(prefix="/api/v1/psicologia_d/transmissao_apego", tags=["psicologia_desenvolvimento"])
router_verbal_si = APIRouter(prefix="/api/v1/psicologia_d/verbal_si", tags=["psicologia_desenvolvimento"])
router_vergonha_desenvolvim = APIRouter(prefix="/api/v1/psicologia_d/vergonha_desenvolvimento", tags=["psicologia_desenvolvimento"])
router_zona_desenvolvimento = APIRouter(prefix="/api/v1/psicologia_d/zona_desenvolvimento_prox", tags=["psicologia_desenvolvimento"])

@router_afeto_vitalidade.get("")
async def i_afeto_vitalidade():
    return {"p":"psicologia_dese_afeto_vitalidade","s":"ativo","t":datetime.utcnow().isoformat()}
@router_agressao_desenvolvim.get("")
async def i_agressao_desenvolvim():
    return {"p":"psicologia_dese_agressao_desenvolvim","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ainsworth_estranha.get("")
async def i_ainsworth_estranha():
    return {"p":"psicologia_dese_ainsworth_estranha","s":"ativo","t":datetime.utcnow().isoformat()}
@router_altruismo_desenvolvi.get("")
async def i_altruismo_desenvolvi():
    return {"p":"psicologia_dese_altruismo_desenvolvi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_apego_ansioso_resist.get("")
async def i_apego_ansioso_resist():
    return {"p":"psicologia_dese_apego_ansioso_resist","s":"ativo","t":datetime.utcnow().isoformat()}
@router_apego_desorganizado_.get("")
async def i_apego_desorganizado_():
    return {"p":"psicologia_dese_apego_desorganizado_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_apego_evitativo_infa.get("")
async def i_apego_evitativo_infa():
    return {"p":"psicologia_dese_apego_evitativo_infa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_apego_seguro_infanti.get("")
async def i_apego_seguro_infanti():
    return {"p":"psicologia_dese_apego_seguro_infanti","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autonomia_vergonha.get("")
async def i_autonomia_vergonha():
    return {"p":"psicologia_dese_autonomia_vergonha","s":"ativo","t":datetime.utcnow().isoformat()}
@router_base_segura.get("")
async def i_base_segura():
    return {"p":"psicologia_dese_base_segura","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bioecologico.get("")
async def i_bioecologico():
    return {"p":"psicologia_dese_bioecologico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bullying_desenvolvim.get("")
async def i_bullying_desenvolvim():
    return {"p":"psicologia_dese_bullying_desenvolvim","s":"ativo","t":datetime.utcnow().isoformat()}
@router_comportamento_apego.get("")
async def i_comportamento_apego():
    return {"p":"psicologia_dese_comportamento_apego","s":"ativo","t":datetime.utcnow().isoformat()}
@router_confianca_desconfian.get("")
async def i_confianca_desconfian():
    return {"p":"psicologia_dese_confianca_desconfian","s":"ativo","t":datetime.utcnow().isoformat()}
@router_consolidacao_individ.get("")
async def i_consolidacao_individ():
    return {"p":"psicologia_dese_consolidacao_individ","s":"ativo","t":datetime.utcnow().isoformat()}
@router_contingencia.get("")
async def i_contingencia():
    return {"p":"psicologia_dese_contingencia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_convencional_moral.get("")
async def i_convencional_moral():
    return {"p":"psicologia_dese_convencional_moral","s":"ativo","t":datetime.utcnow().isoformat()}
@router_criacao_sentido.get("")
async def i_criacao_sentido():
    return {"p":"psicologia_dese_criacao_sentido","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cronosistema.get("")
async def i_cronosistema():
    return {"p":"psicologia_dese_cronosistema","s":"ativo","t":datetime.utcnow().isoformat()}
@router_culpa_desenvolviment.get("")
async def i_culpa_desenvolviment():
    return {"p":"psicologia_dese_culpa_desenvolviment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_desenvolvimento_mora.get("")
async def i_desenvolvimento_mora():
    return {"p":"psicologia_dese_desenvolvimento_mora","s":"ativo","t":datetime.utcnow().isoformat()}
@router_desenvolvimento_soci.get("")
async def i_desenvolvimento_soci():
    return {"p":"psicologia_dese_desenvolvimento_soci","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dialogo_intersubjeti.get("")
async def i_dialogo_intersubjeti():
    return {"p":"psicologia_dese_dialogo_intersubjeti","s":"ativo","t":datetime.utcnow().isoformat()}
@router_diferenciacao.get("")
async def i_diferenciacao():
    return {"p":"psicologia_dese_diferenciacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ecologia_desenvolvim.get("")
async def i_ecologia_desenvolvim():
    return {"p":"psicologia_dese_ecologia_desenvolvim","s":"ativo","t":datetime.utcnow().isoformat()}
@router_empatia_cognitiva.get("")
async def i_empatia_cognitiva():
    return {"p":"psicologia_dese_empatia_cognitiva","s":"ativo","t":datetime.utcnow().isoformat()}
@router_empatia_desenvolvime.get("")
async def i_empatia_desenvolvime():
    return {"p":"psicologia_dese_empatia_desenvolvime","s":"ativo","t":datetime.utcnow().isoformat()}
@router_empatia_emocional.get("")
async def i_empatia_emocional():
    return {"p":"psicologia_dese_empatia_emocional","s":"ativo","t":datetime.utcnow().isoformat()}
@router_estadios_kohlberg.get("")
async def i_estadios_kohlberg():
    return {"p":"psicologia_dese_estadios_kohlberg","s":"ativo","t":datetime.utcnow().isoformat()}
@router_estágios_erikson.get("")
async def i_estágios_erikson():
    return {"p":"psicologia_dese_estágios_erikson","s":"ativo","t":datetime.utcnow().isoformat()}
@router_etica_cuidado.get("")
async def i_etica_cuidado():
    return {"p":"psicologia_dese_etica_cuidado","s":"ativo","t":datetime.utcnow().isoformat()}
@router_exosistema.get("")
async def i_exosistema():
    return {"p":"psicologia_dese_exosistema","s":"ativo","t":datetime.utcnow().isoformat()}
@router_experiencia_interaca.get("")
async def i_experiencia_interaca():
    return {"p":"psicologia_dese_experiencia_interaca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_exploracao_apego.get("")
async def i_exploracao_apego():
    return {"p":"psicologia_dese_exploracao_apego","s":"ativo","t":datetime.utcnow().isoformat()}
@router_falsa_crenca.get("")
async def i_falsa_crenca():
    return {"p":"psicologia_dese_falsa_crenca","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fase_simbiotica.get("")
async def i_fase_simbiotica():
    return {"p":"psicologia_dese_fase_simbiotica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_figura_apego.get("")
async def i_figura_apego():
    return {"p":"psicologia_dese_figura_apego","s":"ativo","t":datetime.utcnow().isoformat()}
@router_funcao_reflexiva.get("")
async def i_funcao_reflexiva():
    return {"p":"psicologia_dese_funcao_reflexiva","s":"ativo","t":datetime.utcnow().isoformat()}
@router_geratividade_estagna.get("")
async def i_geratividade_estagna():
    return {"p":"psicologia_dese_geratividade_estagna","s":"ativo","t":datetime.utcnow().isoformat()}
@router_identidade_confusao.get("")
async def i_identidade_confusao():
    return {"p":"psicologia_dese_identidade_confusao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_industria_inferiorid.get("")
async def i_industria_inferiorid():
    return {"p":"psicologia_dese_industria_inferiorid","s":"ativo","t":datetime.utcnow().isoformat()}
@router_iniciativa_culpa.get("")
async def i_iniciativa_culpa():
    return {"p":"psicologia_dese_iniciativa_culpa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_integridade_desesper.get("")
async def i_integridade_desesper():
    return {"p":"psicologia_dese_integridade_desesper","s":"ativo","t":datetime.utcnow().isoformat()}
@router_intimidade_isolament.get("")
async def i_intimidade_isolament():
    return {"p":"psicologia_dese_intimidade_isolament","s":"ativo","t":datetime.utcnow().isoformat()}
@router_joint_attention.get("")
async def i_joint_attention():
    return {"p":"psicologia_dese_joint_attention","s":"ativo","t":datetime.utcnow().isoformat()}
@router_juizo_moral.get("")
async def i_juizo_moral():
    return {"p":"psicologia_dese_juizo_moral","s":"ativo","t":datetime.utcnow().isoformat()}
@router_luto_apego.get("")
async def i_luto_apego():
    return {"p":"psicologia_dese_luto_apego","s":"ativo","t":datetime.utcnow().isoformat()}
@router_macrosistema.get("")
async def i_macrosistema():
    return {"p":"psicologia_dese_macrosistema","s":"ativo","t":datetime.utcnow().isoformat()}
@router_marcacao.get("")
async def i_marcacao():
    return {"p":"psicologia_dese_marcacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mentalizacao_parenta.get("")
async def i_mentalizacao_parenta():
    return {"p":"psicologia_dese_mentalizacao_parenta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mente_reflexiva.get("")
async def i_mente_reflexiva():
    return {"p":"psicologia_dese_mente_reflexiva","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mesosistema.get("")
async def i_mesosistema():
    return {"p":"psicologia_dese_mesosistema","s":"ativo","t":datetime.utcnow().isoformat()}
@router_microsistema.get("")
async def i_microsistema():
    return {"p":"psicologia_dese_microsistema","s":"ativo","t":datetime.utcnow().isoformat()}
@router_moral_emotion.get("")
async def i_moral_emotion():
    return {"p":"psicologia_dese_moral_emotion","s":"ativo","t":datetime.utcnow().isoformat()}
@router_narrativo_si.get("")
async def i_narrativo_si():
    return {"p":"psicologia_dese_narrativo_si","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nucleo_si.get("")
async def i_nucleo_si():
    return {"p":"psicologia_dese_nucleo_si","s":"ativo","t":datetime.utcnow().isoformat()}
@router_operatorio_concreto.get("")
async def i_operatorio_concreto():
    return {"p":"psicologia_dese_operatorio_concreto","s":"ativo","t":datetime.utcnow().isoformat()}
@router_operatorio_formal.get("")
async def i_operatorio_formal():
    return {"p":"psicologia_dese_operatorio_formal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pensamento_linguagem.get("")
async def i_pensamento_linguagem():
    return {"p":"psicologia_dese_pensamento_linguagem","s":"ativo","t":datetime.utcnow().isoformat()}
@router_perda_apego.get("")
async def i_perda_apego():
    return {"p":"psicologia_dese_perda_apego","s":"ativo","t":datetime.utcnow().isoformat()}
@router_perspectiva_feminist.get("")
async def i_perspectiva_feminist():
    return {"p":"psicologia_dese_perspectiva_feminist","s":"ativo","t":datetime.utcnow().isoformat()}
@router_perspectiva_taking.get("")
async def i_perspectiva_taking():
    return {"p":"psicologia_dese_perspectiva_taking","s":"ativo","t":datetime.utcnow().isoformat()}
@router_porto_seguro.get("")
async def i_porto_seguro():
    return {"p":"psicologia_dese_porto_seguro","s":"ativo","t":datetime.utcnow().isoformat()}
@router_posconvencional.get("")
async def i_posconvencional():
    return {"p":"psicologia_dese_posconvencional","s":"ativo","t":datetime.utcnow().isoformat()}
@router_praticando.get("")
async def i_praticando():
    return {"p":"psicologia_dese_praticando","s":"ativo","t":datetime.utcnow().isoformat()}
@router_preconvencional_mora.get("")
async def i_preconvencional_mora():
    return {"p":"psicologia_dese_preconvencional_mora","s":"ativo","t":datetime.utcnow().isoformat()}
@router_preoperatorio_piaget.get("")
async def i_preoperatorio_piaget():
    return {"p":"psicologia_dese_preoperatorio_piaget","s":"ativo","t":datetime.utcnow().isoformat()}
@router_prosocial_desenvolvi.get("")
async def i_prosocial_desenvolvi():
    return {"p":"psicologia_dese_prosocial_desenvolvi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_protoconversacao.get("")
async def i_protoconversacao():
    return {"p":"psicologia_dese_protoconversacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_raciocinio_moral.get("")
async def i_raciocinio_moral():
    return {"p":"psicologia_dese_raciocinio_moral","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reaproximacao.get("")
async def i_reaproximacao():
    return {"p":"psicologia_dese_reaproximacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_regulacao_emocional_.get("")
async def i_regulacao_emocional_():
    return {"p":"psicologia_dese_regulacao_emocional_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reuniao_apego.get("")
async def i_reuniao_apego():
    return {"p":"psicologia_dese_reuniao_apego","s":"ativo","t":datetime.utcnow().isoformat()}
@router_scaffolding_vygotsky.get("")
async def i_scaffolding_vygotsky():
    return {"p":"psicologia_dese_scaffolding_vygotsky","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sensoriomotor_piaget.get("")
async def i_sensoriomotor_piaget():
    return {"p":"psicologia_dese_sensoriomotor_piaget","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sentido_si_emergente.get("")
async def i_sentido_si_emergente():
    return {"p":"psicologia_dese_sentido_si_emergente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_separacao_apego.get("")
async def i_separacao_apego():
    return {"p":"psicologia_dese_separacao_apego","s":"ativo","t":datetime.utcnow().isoformat()}
@router_separacao_individuac.get("")
async def i_separacao_individuac():
    return {"p":"psicologia_dese_separacao_individuac","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sincronia.get("")
async def i_sincronia():
    return {"p":"psicologia_dese_sincronia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sistema_apego.get("")
async def i_sistema_apego():
    return {"p":"psicologia_dese_sistema_apego","s":"ativo","t":datetime.utcnow().isoformat()}
@router_situacao_estranha.get("")
async def i_situacao_estranha():
    return {"p":"psicologia_dese_situacao_estranha","s":"ativo","t":datetime.utcnow().isoformat()}
@router_subjetivo_si.get("")
async def i_subjetivo_si():
    return {"p":"psicologia_dese_subjetivo_si","s":"ativo","t":datetime.utcnow().isoformat()}
@router_temperamento_dif.get("")
async def i_temperamento_dif():
    return {"p":"psicologia_dese_temperamento_dif","s":"ativo","t":datetime.utcnow().isoformat()}
@router_teoria_bowlby.get("")
async def i_teoria_bowlby():
    return {"p":"psicologia_dese_teoria_bowlby","s":"ativo","t":datetime.utcnow().isoformat()}
@router_teoria_bronfenbrenne.get("")
async def i_teoria_bronfenbrenne():
    return {"p":"psicologia_dese_teoria_bronfenbrenne","s":"ativo","t":datetime.utcnow().isoformat()}
@router_teoria_erikson.get("")
async def i_teoria_erikson():
    return {"p":"psicologia_dese_teoria_erikson","s":"ativo","t":datetime.utcnow().isoformat()}
@router_teoria_gilligan.get("")
async def i_teoria_gilligan():
    return {"p":"psicologia_dese_teoria_gilligan","s":"ativo","t":datetime.utcnow().isoformat()}
@router_teoria_kohlberg.get("")
async def i_teoria_kohlberg():
    return {"p":"psicologia_dese_teoria_kohlberg","s":"ativo","t":datetime.utcnow().isoformat()}
@router_teoria_mahler.get("")
async def i_teoria_mahler():
    return {"p":"psicologia_dese_teoria_mahler","s":"ativo","t":datetime.utcnow().isoformat()}
@router_teoria_mente.get("")
async def i_teoria_mente():
    return {"p":"psicologia_dese_teoria_mente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_teoria_piaget.get("")
async def i_teoria_piaget():
    return {"p":"psicologia_dese_teoria_piaget","s":"ativo","t":datetime.utcnow().isoformat()}
@router_teoria_stern.get("")
async def i_teoria_stern():
    return {"p":"psicologia_dese_teoria_stern","s":"ativo","t":datetime.utcnow().isoformat()}
@router_teoria_vygotsky.get("")
async def i_teoria_vygotsky():
    return {"p":"psicologia_dese_teoria_vygotsky","s":"ativo","t":datetime.utcnow().isoformat()}
@router_transmissao_apego.get("")
async def i_transmissao_apego():
    return {"p":"psicologia_dese_transmissao_apego","s":"ativo","t":datetime.utcnow().isoformat()}
@router_verbal_si.get("")
async def i_verbal_si():
    return {"p":"psicologia_dese_verbal_si","s":"ativo","t":datetime.utcnow().isoformat()}
@router_vergonha_desenvolvim.get("")
async def i_vergonha_desenvolvim():
    return {"p":"psicologia_dese_vergonha_desenvolvim","s":"ativo","t":datetime.utcnow().isoformat()}
@router_zona_desenvolvimento.get("")
async def i_zona_desenvolvimento():
    return {"p":"psicologia_dese_zona_desenvolvimento","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_psicologia_desenvolv(PluginBase):
    name = "consolidated_psicologia_desenvolvimento"
    def setup(self, app):
        app.include_router(router_afeto_vitalidade)
        app.include_router(router_agressao_desenvolvim)
        app.include_router(router_ainsworth_estranha)
        app.include_router(router_altruismo_desenvolvi)
        app.include_router(router_apego_ansioso_resist)
        app.include_router(router_apego_desorganizado_)
        app.include_router(router_apego_evitativo_infa)
        app.include_router(router_apego_seguro_infanti)
        app.include_router(router_autonomia_vergonha)
        app.include_router(router_base_segura)
        app.include_router(router_bioecologico)
        app.include_router(router_bullying_desenvolvim)
        app.include_router(router_comportamento_apego)
        app.include_router(router_confianca_desconfian)
        app.include_router(router_consolidacao_individ)
        app.include_router(router_contingencia)
        app.include_router(router_convencional_moral)
        app.include_router(router_criacao_sentido)
        app.include_router(router_cronosistema)
        app.include_router(router_culpa_desenvolviment)
        app.include_router(router_desenvolvimento_mora)
        app.include_router(router_desenvolvimento_soci)
        app.include_router(router_dialogo_intersubjeti)
        app.include_router(router_diferenciacao)
        app.include_router(router_ecologia_desenvolvim)
        app.include_router(router_empatia_cognitiva)
        app.include_router(router_empatia_desenvolvime)
        app.include_router(router_empatia_emocional)
        app.include_router(router_estadios_kohlberg)
        app.include_router(router_estágios_erikson)
        app.include_router(router_etica_cuidado)
        app.include_router(router_exosistema)
        app.include_router(router_experiencia_interaca)
        app.include_router(router_exploracao_apego)
        app.include_router(router_falsa_crenca)
        app.include_router(router_fase_simbiotica)
        app.include_router(router_figura_apego)
        app.include_router(router_funcao_reflexiva)
        app.include_router(router_geratividade_estagna)
        app.include_router(router_identidade_confusao)
        app.include_router(router_industria_inferiorid)
        app.include_router(router_iniciativa_culpa)
        app.include_router(router_integridade_desesper)
        app.include_router(router_intimidade_isolament)
        app.include_router(router_joint_attention)
        app.include_router(router_juizo_moral)
        app.include_router(router_luto_apego)
        app.include_router(router_macrosistema)
        app.include_router(router_marcacao)
        app.include_router(router_mentalizacao_parenta)
        app.include_router(router_mente_reflexiva)
        app.include_router(router_mesosistema)
        app.include_router(router_microsistema)
        app.include_router(router_moral_emotion)
        app.include_router(router_narrativo_si)
        app.include_router(router_nucleo_si)
        app.include_router(router_operatorio_concreto)
        app.include_router(router_operatorio_formal)
        app.include_router(router_pensamento_linguagem)
        app.include_router(router_perda_apego)
        app.include_router(router_perspectiva_feminist)
        app.include_router(router_perspectiva_taking)
        app.include_router(router_porto_seguro)
        app.include_router(router_posconvencional)
        app.include_router(router_praticando)
        app.include_router(router_preconvencional_mora)
        app.include_router(router_preoperatorio_piaget)
        app.include_router(router_prosocial_desenvolvi)
        app.include_router(router_protoconversacao)
        app.include_router(router_raciocinio_moral)
        app.include_router(router_reaproximacao)
        app.include_router(router_regulacao_emocional_)
        app.include_router(router_reuniao_apego)
        app.include_router(router_scaffolding_vygotsky)
        app.include_router(router_sensoriomotor_piaget)
        app.include_router(router_sentido_si_emergente)
        app.include_router(router_separacao_apego)
        app.include_router(router_separacao_individuac)
        app.include_router(router_sincronia)
        app.include_router(router_sistema_apego)
        app.include_router(router_situacao_estranha)
        app.include_router(router_subjetivo_si)
        app.include_router(router_temperamento_dif)
        app.include_router(router_teoria_bowlby)
        app.include_router(router_teoria_bronfenbrenne)
        app.include_router(router_teoria_erikson)
        app.include_router(router_teoria_gilligan)
        app.include_router(router_teoria_kohlberg)
        app.include_router(router_teoria_mahler)
        app.include_router(router_teoria_mente)
        app.include_router(router_teoria_piaget)
        app.include_router(router_teoria_stern)
        app.include_router(router_teoria_vygotsky)
        app.include_router(router_transmissao_apego)
        app.include_router(router_verbal_si)
        app.include_router(router_vergonha_desenvolvim)
        app.include_router(router_zona_desenvolvimento)


plugin = Plugin_psicologia_desenvolv()
