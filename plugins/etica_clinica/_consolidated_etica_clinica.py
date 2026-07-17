from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_abuso_crianca_notifi = APIRouter(prefix="/api/v1/etica_clinic/abuso_crianca_notificacao", tags=["etica_clinica"])
router_alta_responsabilidad = APIRouter(prefix="/api/v1/etica_clinic/alta_responsabilidade", tags=["etica_clinica"])
router_amizade_cliente = APIRouter(prefix="/api/v1/etica_clinic/amizade_cliente", tags=["etica_clinica"])
router_assentimento_menor = APIRouter(prefix="/api/v1/etica_clinic/assentimento_menor", tags=["etica_clinica"])
router_autonomia2 = APIRouter(prefix="/api/v1/etica_clinic/autonomia2", tags=["etica_clinica"])
router_autonomia_suportada = APIRouter(prefix="/api/v1/etica_clinic/autonomia_suportada", tags=["etica_clinica"])
router_beneficencia2 = APIRouter(prefix="/api/v1/etica_clinic/beneficencia2", tags=["etica_clinica"])
router_capacidade_decisoria = APIRouter(prefix="/api/v1/etica_clinic/capacidade_decisoria", tags=["etica_clinica"])
router_consentimento_inform = APIRouter(prefix="/api/v1/etica_clinic/consentimento_informado2", tags=["etica_clinica"])
router_contratransferencia_ = APIRouter(prefix="/api/v1/etica_clinic/contratransferencia_etica", tags=["etica_clinica"])
router_cuidado_etica = APIRouter(prefix="/api/v1/etica_clinic/cuidado_etica", tags=["etica_clinica"])
router_cuidado_paliativo3 = APIRouter(prefix="/api/v1/etica_clinic/cuidado_paliativo3", tags=["etica_clinica"])
router_curatela_moderna = APIRouter(prefix="/api/v1/etica_clinic/curatela_moderna", tags=["etica_clinica"])
router_dever_alertar = APIRouter(prefix="/api/v1/etica_clinic/dever_alertar", tags=["etica_clinica"])
router_diretiva_antecipada3 = APIRouter(prefix="/api/v1/etica_clinic/diretiva_antecipada3", tags=["etica_clinica"])
router_distanasia_futilidad = APIRouter(prefix="/api/v1/etica_clinic/distanasia_futilidade", tags=["etica_clinica"])
router_doenca_infectocontag = APIRouter(prefix="/api/v1/etica_clinic/doenca_infectocontagiosa", tags=["etica_clinica"])
router_dupla_relacao2 = APIRouter(prefix="/api/v1/etica_clinic/dupla_relacao2", tags=["etica_clinica"])
router_eutanasia_passiva = APIRouter(prefix="/api/v1/etica_clinic/eutanasia_passiva", tags=["etica_clinica"])
router_ex_cliente_relacao = APIRouter(prefix="/api/v1/etica_clinic/ex_cliente_relacao", tags=["etica_clinica"])
router_hierarquia_terapeuti = APIRouter(prefix="/api/v1/etica_clinic/hierarquia_terapeutica", tags=["etica_clinica"])
router_internacao_compulsor = APIRouter(prefix="/api/v1/etica_clinic/internacao_compulsoria2", tags=["etica_clinica"])
router_internacao_involunta = APIRouter(prefix="/api/v1/etica_clinic/internacao_involuntaria2", tags=["etica_clinica"])
router_internacao_voluntari = APIRouter(prefix="/api/v1/etica_clinic/internacao_voluntaria", tags=["etica_clinica"])
router_jesum_recusa = APIRouter(prefix="/api/v1/etica_clinic/jesum_recusa", tags=["etica_clinica"])
router_justica2 = APIRouter(prefix="/api/v1/etica_clinic/justica2", tags=["etica_clinica"])
router_limitacao_esforco = APIRouter(prefix="/api/v1/etica_clinic/limitacao_esforco", tags=["etica_clinica"])
router_limites_profissionai = APIRouter(prefix="/api/v1/etica_clinic/limites_profissionais", tags=["etica_clinica"])
router_nao_maleficencia2 = APIRouter(prefix="/api/v1/etica_clinic/nao_maleficencia2", tags=["etica_clinica"])
router_notificacao_obrigato = APIRouter(prefix="/api/v1/etica_clinic/notificacao_obrigatoria", tags=["etica_clinica"])
router_obstinacao_terapeuti = APIRouter(prefix="/api/v1/etica_clinic/obstinacao_terapeutica", tags=["etica_clinica"])
router_ortotanasia = APIRouter(prefix="/api/v1/etica_clinic/ortotanasia", tags=["etica_clinica"])
router_periculosidade_psiqu = APIRouter(prefix="/api/v1/etica_clinic/periculosidade_psiquiatri", tags=["etica_clinica"])
router_presentes_clinico = APIRouter(prefix="/api/v1/etica_clinic/presentes_clinico", tags=["etica_clinica"])
router_principios_bioeticos = APIRouter(prefix="/api/v1/etica_clinic/principios_bioeticos2", tags=["etica_clinica"])
router_recusa_tratamento = APIRouter(prefix="/api/v1/etica_clinic/recusa_tratamento", tags=["etica_clinica"])
router_redes_sociais_client = APIRouter(prefix="/api/v1/etica_clinic/redes_sociais_cliente", tags=["etica_clinica"])
router_registro_profissiona = APIRouter(prefix="/api/v1/etica_clinic/registro_profissional", tags=["etica_clinica"])
router_relacao_poder = APIRouter(prefix="/api/v1/etica_clinic/relacao_poder", tags=["etica_clinica"])
router_relacao_sexual_clien = APIRouter(prefix="/api/v1/etica_clinic/relacao_sexual_cliente", tags=["etica_clinica"])
router_sedacao_paliativa = APIRouter(prefix="/api/v1/etica_clinic/sedacao_paliativa", tags=["etica_clinica"])
router_seguro_responsabilid = APIRouter(prefix="/api/v1/etica_clinic/seguro_responsabilidade", tags=["etica_clinica"])
router_sigilo_limite = APIRouter(prefix="/api/v1/etica_clinic/sigilo_limite", tags=["etica_clinica"])
router_supervisao_obrigator = APIRouter(prefix="/api/v1/etica_clinic/supervisao_obrigatoria", tags=["etica_clinica"])
router_tarasoff_brasil = APIRouter(prefix="/api/v1/etica_clinic/tarasoff_brasil", tags=["etica_clinica"])
router_terceiros_risco = APIRouter(prefix="/api/v1/etica_clinic/terceiros_risco", tags=["etica_clinica"])
router_testamento_vital3 = APIRouter(prefix="/api/v1/etica_clinic/testamento_vital3", tags=["etica_clinica"])
router_testemunha_jehova = APIRouter(prefix="/api/v1/etica_clinic/testemunha_jehova", tags=["etica_clinica"])
router_tomada_decisao_assis = APIRouter(prefix="/api/v1/etica_clinic/tomada_decisao_assistida", tags=["etica_clinica"])
router_toque_clinico = APIRouter(prefix="/api/v1/etica_clinic/toque_clinico", tags=["etica_clinica"])
router_transferencia_etica = APIRouter(prefix="/api/v1/etica_clinic/transferencia_etica", tags=["etica_clinica"])
router_transfusao_recusa = APIRouter(prefix="/api/v1/etica_clinic/transfusao_recusa", tags=["etica_clinica"])
router_violencia_domestica_ = APIRouter(prefix="/api/v1/etica_clinic/violencia_domestica_notif", tags=["etica_clinica"])
router_vulnerabilidade_etic = APIRouter(prefix="/api/v1/etica_clinic/vulnerabilidade_etica", tags=["etica_clinica"])

@router_abuso_crianca_notifi.get("")
async def i_abuso_crianca_notifi():
    return {"p":"etica_clinica_abuso_crianca_notifi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_alta_responsabilidad.get("")
async def i_alta_responsabilidad():
    return {"p":"etica_clinica_alta_responsabilidad","s":"ativo","t":datetime.utcnow().isoformat()}
@router_amizade_cliente.get("")
async def i_amizade_cliente():
    return {"p":"etica_clinica_amizade_cliente","s":"ativo","t":datetime.utcnow().isoformat()}
@router_assentimento_menor.get("")
async def i_assentimento_menor():
    return {"p":"etica_clinica_assentimento_menor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autonomia2.get("")
async def i_autonomia2():
    return {"p":"etica_clinica_autonomia2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autonomia_suportada.get("")
async def i_autonomia_suportada():
    return {"p":"etica_clinica_autonomia_suportada","s":"ativo","t":datetime.utcnow().isoformat()}
@router_beneficencia2.get("")
async def i_beneficencia2():
    return {"p":"etica_clinica_beneficencia2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_capacidade_decisoria.get("")
async def i_capacidade_decisoria():
    return {"p":"etica_clinica_capacidade_decisoria","s":"ativo","t":datetime.utcnow().isoformat()}
@router_consentimento_inform.get("")
async def i_consentimento_inform():
    return {"p":"etica_clinica_consentimento_inform","s":"ativo","t":datetime.utcnow().isoformat()}
@router_contratransferencia_.get("")
async def i_contratransferencia_():
    return {"p":"etica_clinica_contratransferencia_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cuidado_etica.get("")
async def i_cuidado_etica():
    return {"p":"etica_clinica_cuidado_etica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cuidado_paliativo3.get("")
async def i_cuidado_paliativo3():
    return {"p":"etica_clinica_cuidado_paliativo3","s":"ativo","t":datetime.utcnow().isoformat()}
@router_curatela_moderna.get("")
async def i_curatela_moderna():
    return {"p":"etica_clinica_curatela_moderna","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dever_alertar.get("")
async def i_dever_alertar():
    return {"p":"etica_clinica_dever_alertar","s":"ativo","t":datetime.utcnow().isoformat()}
@router_diretiva_antecipada3.get("")
async def i_diretiva_antecipada3():
    return {"p":"etica_clinica_diretiva_antecipada3","s":"ativo","t":datetime.utcnow().isoformat()}
@router_distanasia_futilidad.get("")
async def i_distanasia_futilidad():
    return {"p":"etica_clinica_distanasia_futilidad","s":"ativo","t":datetime.utcnow().isoformat()}
@router_doenca_infectocontag.get("")
async def i_doenca_infectocontag():
    return {"p":"etica_clinica_doenca_infectocontag","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dupla_relacao2.get("")
async def i_dupla_relacao2():
    return {"p":"etica_clinica_dupla_relacao2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_eutanasia_passiva.get("")
async def i_eutanasia_passiva():
    return {"p":"etica_clinica_eutanasia_passiva","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ex_cliente_relacao.get("")
async def i_ex_cliente_relacao():
    return {"p":"etica_clinica_ex_cliente_relacao","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hierarquia_terapeuti.get("")
async def i_hierarquia_terapeuti():
    return {"p":"etica_clinica_hierarquia_terapeuti","s":"ativo","t":datetime.utcnow().isoformat()}
@router_internacao_compulsor.get("")
async def i_internacao_compulsor():
    return {"p":"etica_clinica_internacao_compulsor","s":"ativo","t":datetime.utcnow().isoformat()}
@router_internacao_involunta.get("")
async def i_internacao_involunta():
    return {"p":"etica_clinica_internacao_involunta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_internacao_voluntari.get("")
async def i_internacao_voluntari():
    return {"p":"etica_clinica_internacao_voluntari","s":"ativo","t":datetime.utcnow().isoformat()}
@router_jesum_recusa.get("")
async def i_jesum_recusa():
    return {"p":"etica_clinica_jesum_recusa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_justica2.get("")
async def i_justica2():
    return {"p":"etica_clinica_justica2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_limitacao_esforco.get("")
async def i_limitacao_esforco():
    return {"p":"etica_clinica_limitacao_esforco","s":"ativo","t":datetime.utcnow().isoformat()}
@router_limites_profissionai.get("")
async def i_limites_profissionai():
    return {"p":"etica_clinica_limites_profissionai","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nao_maleficencia2.get("")
async def i_nao_maleficencia2():
    return {"p":"etica_clinica_nao_maleficencia2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_notificacao_obrigato.get("")
async def i_notificacao_obrigato():
    return {"p":"etica_clinica_notificacao_obrigato","s":"ativo","t":datetime.utcnow().isoformat()}
@router_obstinacao_terapeuti.get("")
async def i_obstinacao_terapeuti():
    return {"p":"etica_clinica_obstinacao_terapeuti","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ortotanasia.get("")
async def i_ortotanasia():
    return {"p":"etica_clinica_ortotanasia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_periculosidade_psiqu.get("")
async def i_periculosidade_psiqu():
    return {"p":"etica_clinica_periculosidade_psiqu","s":"ativo","t":datetime.utcnow().isoformat()}
@router_presentes_clinico.get("")
async def i_presentes_clinico():
    return {"p":"etica_clinica_presentes_clinico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_principios_bioeticos.get("")
async def i_principios_bioeticos():
    return {"p":"etica_clinica_principios_bioeticos","s":"ativo","t":datetime.utcnow().isoformat()}
@router_recusa_tratamento.get("")
async def i_recusa_tratamento():
    return {"p":"etica_clinica_recusa_tratamento","s":"ativo","t":datetime.utcnow().isoformat()}
@router_redes_sociais_client.get("")
async def i_redes_sociais_client():
    return {"p":"etica_clinica_redes_sociais_client","s":"ativo","t":datetime.utcnow().isoformat()}
@router_registro_profissiona.get("")
async def i_registro_profissiona():
    return {"p":"etica_clinica_registro_profissiona","s":"ativo","t":datetime.utcnow().isoformat()}
@router_relacao_poder.get("")
async def i_relacao_poder():
    return {"p":"etica_clinica_relacao_poder","s":"ativo","t":datetime.utcnow().isoformat()}
@router_relacao_sexual_clien.get("")
async def i_relacao_sexual_clien():
    return {"p":"etica_clinica_relacao_sexual_clien","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sedacao_paliativa.get("")
async def i_sedacao_paliativa():
    return {"p":"etica_clinica_sedacao_paliativa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_seguro_responsabilid.get("")
async def i_seguro_responsabilid():
    return {"p":"etica_clinica_seguro_responsabilid","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sigilo_limite.get("")
async def i_sigilo_limite():
    return {"p":"etica_clinica_sigilo_limite","s":"ativo","t":datetime.utcnow().isoformat()}
@router_supervisao_obrigator.get("")
async def i_supervisao_obrigator():
    return {"p":"etica_clinica_supervisao_obrigator","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tarasoff_brasil.get("")
async def i_tarasoff_brasil():
    return {"p":"etica_clinica_tarasoff_brasil","s":"ativo","t":datetime.utcnow().isoformat()}
@router_terceiros_risco.get("")
async def i_terceiros_risco():
    return {"p":"etica_clinica_terceiros_risco","s":"ativo","t":datetime.utcnow().isoformat()}
@router_testamento_vital3.get("")
async def i_testamento_vital3():
    return {"p":"etica_clinica_testamento_vital3","s":"ativo","t":datetime.utcnow().isoformat()}
@router_testemunha_jehova.get("")
async def i_testemunha_jehova():
    return {"p":"etica_clinica_testemunha_jehova","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tomada_decisao_assis.get("")
async def i_tomada_decisao_assis():
    return {"p":"etica_clinica_tomada_decisao_assis","s":"ativo","t":datetime.utcnow().isoformat()}
@router_toque_clinico.get("")
async def i_toque_clinico():
    return {"p":"etica_clinica_toque_clinico","s":"ativo","t":datetime.utcnow().isoformat()}
@router_transferencia_etica.get("")
async def i_transferencia_etica():
    return {"p":"etica_clinica_transferencia_etica","s":"ativo","t":datetime.utcnow().isoformat()}
@router_transfusao_recusa.get("")
async def i_transfusao_recusa():
    return {"p":"etica_clinica_transfusao_recusa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_violencia_domestica_.get("")
async def i_violencia_domestica_():
    return {"p":"etica_clinica_violencia_domestica_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_vulnerabilidade_etic.get("")
async def i_vulnerabilidade_etic():
    return {"p":"etica_clinica_vulnerabilidade_etic","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_etica_clinica(PluginBase):
    name = "consolidated_etica_clinica"
    def setup(self, app):
        app.include_router(router_abuso_crianca_notifi)
        app.include_router(router_alta_responsabilidad)
        app.include_router(router_amizade_cliente)
        app.include_router(router_assentimento_menor)
        app.include_router(router_autonomia2)
        app.include_router(router_autonomia_suportada)
        app.include_router(router_beneficencia2)
        app.include_router(router_capacidade_decisoria)
        app.include_router(router_consentimento_inform)
        app.include_router(router_contratransferencia_)
        app.include_router(router_cuidado_etica)
        app.include_router(router_cuidado_paliativo3)
        app.include_router(router_curatela_moderna)
        app.include_router(router_dever_alertar)
        app.include_router(router_diretiva_antecipada3)
        app.include_router(router_distanasia_futilidad)
        app.include_router(router_doenca_infectocontag)
        app.include_router(router_dupla_relacao2)
        app.include_router(router_eutanasia_passiva)
        app.include_router(router_ex_cliente_relacao)
        app.include_router(router_hierarquia_terapeuti)
        app.include_router(router_internacao_compulsor)
        app.include_router(router_internacao_involunta)
        app.include_router(router_internacao_voluntari)
        app.include_router(router_jesum_recusa)
        app.include_router(router_justica2)
        app.include_router(router_limitacao_esforco)
        app.include_router(router_limites_profissionai)
        app.include_router(router_nao_maleficencia2)
        app.include_router(router_notificacao_obrigato)
        app.include_router(router_obstinacao_terapeuti)
        app.include_router(router_ortotanasia)
        app.include_router(router_periculosidade_psiqu)
        app.include_router(router_presentes_clinico)
        app.include_router(router_principios_bioeticos)
        app.include_router(router_recusa_tratamento)
        app.include_router(router_redes_sociais_client)
        app.include_router(router_registro_profissiona)
        app.include_router(router_relacao_poder)
        app.include_router(router_relacao_sexual_clien)
        app.include_router(router_sedacao_paliativa)
        app.include_router(router_seguro_responsabilid)
        app.include_router(router_sigilo_limite)
        app.include_router(router_supervisao_obrigator)
        app.include_router(router_tarasoff_brasil)
        app.include_router(router_terceiros_risco)
        app.include_router(router_testamento_vital3)
        app.include_router(router_testemunha_jehova)
        app.include_router(router_tomada_decisao_assis)
        app.include_router(router_toque_clinico)
        app.include_router(router_transferencia_etica)
        app.include_router(router_transfusao_recusa)
        app.include_router(router_violencia_domestica_)
        app.include_router(router_vulnerabilidade_etic)


plugin = Plugin_etica_clinica()
