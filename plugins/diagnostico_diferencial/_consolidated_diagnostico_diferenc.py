from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_adhd_vs_anxiety = APIRouter(prefix="/api/v1/diagnostico_/adhd_vs_anxiety", tags=["diagnostico_diferencial"])
router_adhd_vs_autism = APIRouter(prefix="/api/v1/diagnostico_/adhd_vs_autism", tags=["diagnostico_diferencial"])
router_adhd_vs_bipolar = APIRouter(prefix="/api/v1/diagnostico_/adhd_vs_bipolar", tags=["diagnostico_diferencial"])
router_adhd_vs_learning = APIRouter(prefix="/api/v1/diagnostico_/adhd_vs_learning", tags=["diagnostico_diferencial"])
router_alzheimer_vs_dlb = APIRouter(prefix="/api/v1/diagnostico_/alzheimer_vs_dlb", tags=["diagnostico_diferencial"])
router_alzheimer_vs_ftd = APIRouter(prefix="/api/v1/diagnostico_/alzheimer_vs_ftd", tags=["diagnostico_diferencial"])
router_alzheimer_vs_vascula = APIRouter(prefix="/api/v1/diagnostico_/alzheimer_vs_vascular", tags=["diagnostico_diferencial"])
router_anorexia_vs_bulimia = APIRouter(prefix="/api/v1/diagnostico_/anorexia_vs_bulimia", tags=["diagnostico_diferencial"])
router_antisocial_vs_psycho = APIRouter(prefix="/api/v1/diagnostico_/antisocial_vs_psychopathy", tags=["diagnostico_diferencial"])
router_anxiety_vs_adhd = APIRouter(prefix="/api/v1/diagnostico_/anxiety_vs_adhd", tags=["diagnostico_diferencial"])
router_anxiety_vs_autism = APIRouter(prefix="/api/v1/diagnostico_/anxiety_vs_autism", tags=["diagnostico_diferencial"])
router_anxiety_vs_depressio = APIRouter(prefix="/api/v1/diagnostico_/anxiety_vs_depression", tags=["diagnostico_diferencial"])
router_attachment_vs_ptsd = APIRouter(prefix="/api/v1/diagnostico_/attachment_vs_ptsd", tags=["diagnostico_diferencial"])
router_autism_spectrum = APIRouter(prefix="/api/v1/diagnostico_/autism_spectrum", tags=["diagnostico_diferencial"])
router_autism_vs_adhd2 = APIRouter(prefix="/api/v1/diagnostico_/autism_vs_adhd2", tags=["diagnostico_diferencial"])
router_autism_vs_schizoid = APIRouter(prefix="/api/v1/diagnostico_/autism_vs_schizoid", tags=["diagnostico_diferencial"])
router_autism_vs_social_anx = APIRouter(prefix="/api/v1/diagnostico_/autism_vs_social_anxiety", tags=["diagnostico_diferencial"])
router_avoidant_vs_social_a = APIRouter(prefix="/api/v1/diagnostico_/avoidant_vs_social_anxiet", tags=["diagnostico_diferencial"])
router_binge_vs_bulimia = APIRouter(prefix="/api/v1/diagnostico_/binge_vs_bulimia", tags=["diagnostico_diferencial"])
router_bpd_vs_adhd = APIRouter(prefix="/api/v1/diagnostico_/bpd_vs_adhd", tags=["diagnostico_diferencial"])
router_bpd_vs_bipolar = APIRouter(prefix="/api/v1/diagnostico_/bpd_vs_bipolar", tags=["diagnostico_diferencial"])
router_bpd_vs_narcissistic = APIRouter(prefix="/api/v1/diagnostico_/bpd_vs_narcissistic", tags=["diagnostico_diferencial"])
router_bpd_vs_ptsd = APIRouter(prefix="/api/v1/diagnostico_/bpd_vs_ptsd", tags=["diagnostico_diferencial"])
router_complex_ptsd_vs_ptsd = APIRouter(prefix="/api/v1/diagnostico_/complex_ptsd_vs_ptsd", tags=["diagnostico_diferencial"])
router_conversion_vs_maling = APIRouter(prefix="/api/v1/diagnostico_/conversion_vs_malingering", tags=["diagnostico_diferencial"])
router_delirium_vs_dementia = APIRouter(prefix="/api/v1/diagnostico_/delirium_vs_dementia", tags=["diagnostico_diferencial"])
router_delirium_vs_depressi = APIRouter(prefix="/api/v1/diagnostico_/delirium_vs_depression", tags=["diagnostico_diferencial"])
router_dementia_vs_depressi = APIRouter(prefix="/api/v1/diagnostico_/dementia_vs_depression", tags=["diagnostico_diferencial"])
router_dependent_vs_bpd = APIRouter(prefix="/api/v1/diagnostico_/dependent_vs_bpd", tags=["diagnostico_diferencial"])
router_depression_vs_bipola = APIRouter(prefix="/api/v1/diagnostico_/depression_vs_bipolar", tags=["diagnostico_diferencial"])
router_depression_vs_cyclot = APIRouter(prefix="/api/v1/diagnostico_/depression_vs_cyclothymia", tags=["diagnostico_diferencial"])
router_depression_vs_dysthy = APIRouter(prefix="/api/v1/diagnostico_/depression_vs_dysthymia", tags=["diagnostico_diferencial"])
router_depression_vs_grief = APIRouter(prefix="/api/v1/diagnostico_/depression_vs_grief", tags=["diagnostico_diferencial"])
router_drug_induced_psychos = APIRouter(prefix="/api/v1/diagnostico_/drug_induced_psychosis", tags=["diagnostico_diferencial"])
router_eating_disorders_dif = APIRouter(prefix="/api/v1/diagnostico_/eating_disorders_differen", tags=["diagnostico_diferencial"])
router_factitious_vs_somati = APIRouter(prefix="/api/v1/diagnostico_/factitious_vs_somatic", tags=["diagnostico_diferencial"])
router_first_episode_psycho = APIRouter(prefix="/api/v1/diagnostico_/first_episode_psychosis", tags=["diagnostico_diferencial"])
router_ftd_vs_als = APIRouter(prefix="/api/v1/diagnostico_/ftd_vs_als", tags=["diagnostico_diferencial"])
router_histrionic_vs_bpd = APIRouter(prefix="/api/v1/diagnostico_/histrionic_vs_bpd", tags=["diagnostico_diferencial"])
router_hypochondria_vs_soma = APIRouter(prefix="/api/v1/diagnostico_/hypochondria_vs_somatic", tags=["diagnostico_diferencial"])
router_intoxication_vs_psyc = APIRouter(prefix="/api/v1/diagnostico_/intoxication_vs_psychosis", tags=["diagnostico_diferencial"])
router_mania_vs_hypomania = APIRouter(prefix="/api/v1/diagnostico_/mania_vs_hypomania", tags=["diagnostico_diferencial"])
router_medical_psychosis = APIRouter(prefix="/api/v1/diagnostico_/medical_psychosis", tags=["diagnostico_diferencial"])
router_mild_cognitive_vs_de = APIRouter(prefix="/api/v1/diagnostico_/mild_cognitive_vs_dementi", tags=["diagnostico_diferencial"])
router_munchausen_vs_somati = APIRouter(prefix="/api/v1/diagnostico_/munchausen_vs_somatic", tags=["diagnostico_diferencial"])
router_night_eating_vs_bing = APIRouter(prefix="/api/v1/diagnostico_/night_eating_vs_binge", tags=["diagnostico_diferencial"])
router_npd_vs_antisocial = APIRouter(prefix="/api/v1/diagnostico_/npd_vs_antisocial", tags=["diagnostico_diferencial"])
router_ocd_personality_vs_o = APIRouter(prefix="/api/v1/diagnostico_/ocd_personality_vs_ocd", tags=["diagnostico_diferencial"])
router_ocd_vs_anxiety = APIRouter(prefix="/api/v1/diagnostico_/ocd_vs_anxiety", tags=["diagnostico_diferencial"])
router_ocd_vs_body_dysmorph = APIRouter(prefix="/api/v1/diagnostico_/ocd_vs_body_dysmorphic", tags=["diagnostico_diferencial"])
router_ocd_vs_ptsd = APIRouter(prefix="/api/v1/diagnostico_/ocd_vs_ptsd", tags=["diagnostico_diferencial"])
router_ocd_vs_schizophrenia = APIRouter(prefix="/api/v1/diagnostico_/ocd_vs_schizophrenia", tags=["diagnostico_diferencial"])
router_ocd_vs_tic_disorder = APIRouter(prefix="/api/v1/diagnostico_/ocd_vs_tic_disorder", tags=["diagnostico_diferencial"])
router_orthorexia_vs_anorex = APIRouter(prefix="/api/v1/diagnostico_/orthorexia_vs_anorexia", tags=["diagnostico_diferencial"])
router_parkinson_dementia = APIRouter(prefix="/api/v1/diagnostico_/parkinson_dementia", tags=["diagnostico_diferencial"])
router_psychosis_vs_mania = APIRouter(prefix="/api/v1/diagnostico_/psychosis_vs_mania", tags=["diagnostico_diferencial"])
router_ptsd_vs_anxiety = APIRouter(prefix="/api/v1/diagnostico_/ptsd_vs_anxiety", tags=["diagnostico_diferencial"])
router_ptsd_vs_bipolar = APIRouter(prefix="/api/v1/diagnostico_/ptsd_vs_bipolar", tags=["diagnostico_diferencial"])
router_ptsd_vs_borderline = APIRouter(prefix="/api/v1/diagnostico_/ptsd_vs_borderline", tags=["diagnostico_diferencial"])
router_ptsd_vs_depression = APIRouter(prefix="/api/v1/diagnostico_/ptsd_vs_depression", tags=["diagnostico_diferencial"])
router_ptsd_vs_dissociation = APIRouter(prefix="/api/v1/diagnostico_/ptsd_vs_dissociation", tags=["diagnostico_diferencial"])
router_restrictive_avoidant = APIRouter(prefix="/api/v1/diagnostico_/restrictive_avoidant_vs_a", tags=["diagnostico_diferencial"])
router_schizophrenia_vs_aut = APIRouter(prefix="/api/v1/diagnostico_/schizophrenia_vs_autism", tags=["diagnostico_diferencial"])
router_schizophrenia_vs_bip = APIRouter(prefix="/api/v1/diagnostico_/schizophrenia_vs_bipolar", tags=["diagnostico_diferencial"])
router_schizophrenia_vs_dep = APIRouter(prefix="/api/v1/diagnostico_/schizophrenia_vs_depressi", tags=["diagnostico_diferencial"])
router_somatic_vs_anxiety = APIRouter(prefix="/api/v1/diagnostico_/somatic_vs_anxiety", tags=["diagnostico_diferencial"])
router_somatic_vs_depressio = APIRouter(prefix="/api/v1/diagnostico_/somatic_vs_depression", tags=["diagnostico_diferencial"])
router_substance_induced_vs = APIRouter(prefix="/api/v1/diagnostico_/substance_induced_vs_prim", tags=["diagnostico_diferencial"])
router_unipolar_vs_bipolar = APIRouter(prefix="/api/v1/diagnostico_/unipolar_vs_bipolar", tags=["diagnostico_diferencial"])
router_withdrawal_vs_anxiet = APIRouter(prefix="/api/v1/diagnostico_/withdrawal_vs_anxiety", tags=["diagnostico_diferencial"])

@router_adhd_vs_anxiety.get("")
async def i_adhd_vs_anxiety():
    return {"p":"diagnostico_dif_adhd_vs_anxiety","s":"ativo","t":datetime.utcnow().isoformat()}
@router_adhd_vs_autism.get("")
async def i_adhd_vs_autism():
    return {"p":"diagnostico_dif_adhd_vs_autism","s":"ativo","t":datetime.utcnow().isoformat()}
@router_adhd_vs_bipolar.get("")
async def i_adhd_vs_bipolar():
    return {"p":"diagnostico_dif_adhd_vs_bipolar","s":"ativo","t":datetime.utcnow().isoformat()}
@router_adhd_vs_learning.get("")
async def i_adhd_vs_learning():
    return {"p":"diagnostico_dif_adhd_vs_learning","s":"ativo","t":datetime.utcnow().isoformat()}
@router_alzheimer_vs_dlb.get("")
async def i_alzheimer_vs_dlb():
    return {"p":"diagnostico_dif_alzheimer_vs_dlb","s":"ativo","t":datetime.utcnow().isoformat()}
@router_alzheimer_vs_ftd.get("")
async def i_alzheimer_vs_ftd():
    return {"p":"diagnostico_dif_alzheimer_vs_ftd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_alzheimer_vs_vascula.get("")
async def i_alzheimer_vs_vascula():
    return {"p":"diagnostico_dif_alzheimer_vs_vascula","s":"ativo","t":datetime.utcnow().isoformat()}
@router_anorexia_vs_bulimia.get("")
async def i_anorexia_vs_bulimia():
    return {"p":"diagnostico_dif_anorexia_vs_bulimia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_antisocial_vs_psycho.get("")
async def i_antisocial_vs_psycho():
    return {"p":"diagnostico_dif_antisocial_vs_psycho","s":"ativo","t":datetime.utcnow().isoformat()}
@router_anxiety_vs_adhd.get("")
async def i_anxiety_vs_adhd():
    return {"p":"diagnostico_dif_anxiety_vs_adhd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_anxiety_vs_autism.get("")
async def i_anxiety_vs_autism():
    return {"p":"diagnostico_dif_anxiety_vs_autism","s":"ativo","t":datetime.utcnow().isoformat()}
@router_anxiety_vs_depressio.get("")
async def i_anxiety_vs_depressio():
    return {"p":"diagnostico_dif_anxiety_vs_depressio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_attachment_vs_ptsd.get("")
async def i_attachment_vs_ptsd():
    return {"p":"diagnostico_dif_attachment_vs_ptsd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autism_spectrum.get("")
async def i_autism_spectrum():
    return {"p":"diagnostico_dif_autism_spectrum","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autism_vs_adhd2.get("")
async def i_autism_vs_adhd2():
    return {"p":"diagnostico_dif_autism_vs_adhd2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autism_vs_schizoid.get("")
async def i_autism_vs_schizoid():
    return {"p":"diagnostico_dif_autism_vs_schizoid","s":"ativo","t":datetime.utcnow().isoformat()}
@router_autism_vs_social_anx.get("")
async def i_autism_vs_social_anx():
    return {"p":"diagnostico_dif_autism_vs_social_anx","s":"ativo","t":datetime.utcnow().isoformat()}
@router_avoidant_vs_social_a.get("")
async def i_avoidant_vs_social_a():
    return {"p":"diagnostico_dif_avoidant_vs_social_a","s":"ativo","t":datetime.utcnow().isoformat()}
@router_binge_vs_bulimia.get("")
async def i_binge_vs_bulimia():
    return {"p":"diagnostico_dif_binge_vs_bulimia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bpd_vs_adhd.get("")
async def i_bpd_vs_adhd():
    return {"p":"diagnostico_dif_bpd_vs_adhd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bpd_vs_bipolar.get("")
async def i_bpd_vs_bipolar():
    return {"p":"diagnostico_dif_bpd_vs_bipolar","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bpd_vs_narcissistic.get("")
async def i_bpd_vs_narcissistic():
    return {"p":"diagnostico_dif_bpd_vs_narcissistic","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bpd_vs_ptsd.get("")
async def i_bpd_vs_ptsd():
    return {"p":"diagnostico_dif_bpd_vs_ptsd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_complex_ptsd_vs_ptsd.get("")
async def i_complex_ptsd_vs_ptsd():
    return {"p":"diagnostico_dif_complex_ptsd_vs_ptsd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_conversion_vs_maling.get("")
async def i_conversion_vs_maling():
    return {"p":"diagnostico_dif_conversion_vs_maling","s":"ativo","t":datetime.utcnow().isoformat()}
@router_delirium_vs_dementia.get("")
async def i_delirium_vs_dementia():
    return {"p":"diagnostico_dif_delirium_vs_dementia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_delirium_vs_depressi.get("")
async def i_delirium_vs_depressi():
    return {"p":"diagnostico_dif_delirium_vs_depressi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dementia_vs_depressi.get("")
async def i_dementia_vs_depressi():
    return {"p":"diagnostico_dif_dementia_vs_depressi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dependent_vs_bpd.get("")
async def i_dependent_vs_bpd():
    return {"p":"diagnostico_dif_dependent_vs_bpd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_depression_vs_bipola.get("")
async def i_depression_vs_bipola():
    return {"p":"diagnostico_dif_depression_vs_bipola","s":"ativo","t":datetime.utcnow().isoformat()}
@router_depression_vs_cyclot.get("")
async def i_depression_vs_cyclot():
    return {"p":"diagnostico_dif_depression_vs_cyclot","s":"ativo","t":datetime.utcnow().isoformat()}
@router_depression_vs_dysthy.get("")
async def i_depression_vs_dysthy():
    return {"p":"diagnostico_dif_depression_vs_dysthy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_depression_vs_grief.get("")
async def i_depression_vs_grief():
    return {"p":"diagnostico_dif_depression_vs_grief","s":"ativo","t":datetime.utcnow().isoformat()}
@router_drug_induced_psychos.get("")
async def i_drug_induced_psychos():
    return {"p":"diagnostico_dif_drug_induced_psychos","s":"ativo","t":datetime.utcnow().isoformat()}
@router_eating_disorders_dif.get("")
async def i_eating_disorders_dif():
    return {"p":"diagnostico_dif_eating_disorders_dif","s":"ativo","t":datetime.utcnow().isoformat()}
@router_factitious_vs_somati.get("")
async def i_factitious_vs_somati():
    return {"p":"diagnostico_dif_factitious_vs_somati","s":"ativo","t":datetime.utcnow().isoformat()}
@router_first_episode_psycho.get("")
async def i_first_episode_psycho():
    return {"p":"diagnostico_dif_first_episode_psycho","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ftd_vs_als.get("")
async def i_ftd_vs_als():
    return {"p":"diagnostico_dif_ftd_vs_als","s":"ativo","t":datetime.utcnow().isoformat()}
@router_histrionic_vs_bpd.get("")
async def i_histrionic_vs_bpd():
    return {"p":"diagnostico_dif_histrionic_vs_bpd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hypochondria_vs_soma.get("")
async def i_hypochondria_vs_soma():
    return {"p":"diagnostico_dif_hypochondria_vs_soma","s":"ativo","t":datetime.utcnow().isoformat()}
@router_intoxication_vs_psyc.get("")
async def i_intoxication_vs_psyc():
    return {"p":"diagnostico_dif_intoxication_vs_psyc","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mania_vs_hypomania.get("")
async def i_mania_vs_hypomania():
    return {"p":"diagnostico_dif_mania_vs_hypomania","s":"ativo","t":datetime.utcnow().isoformat()}
@router_medical_psychosis.get("")
async def i_medical_psychosis():
    return {"p":"diagnostico_dif_medical_psychosis","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mild_cognitive_vs_de.get("")
async def i_mild_cognitive_vs_de():
    return {"p":"diagnostico_dif_mild_cognitive_vs_de","s":"ativo","t":datetime.utcnow().isoformat()}
@router_munchausen_vs_somati.get("")
async def i_munchausen_vs_somati():
    return {"p":"diagnostico_dif_munchausen_vs_somati","s":"ativo","t":datetime.utcnow().isoformat()}
@router_night_eating_vs_bing.get("")
async def i_night_eating_vs_bing():
    return {"p":"diagnostico_dif_night_eating_vs_bing","s":"ativo","t":datetime.utcnow().isoformat()}
@router_npd_vs_antisocial.get("")
async def i_npd_vs_antisocial():
    return {"p":"diagnostico_dif_npd_vs_antisocial","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ocd_personality_vs_o.get("")
async def i_ocd_personality_vs_o():
    return {"p":"diagnostico_dif_ocd_personality_vs_o","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ocd_vs_anxiety.get("")
async def i_ocd_vs_anxiety():
    return {"p":"diagnostico_dif_ocd_vs_anxiety","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ocd_vs_body_dysmorph.get("")
async def i_ocd_vs_body_dysmorph():
    return {"p":"diagnostico_dif_ocd_vs_body_dysmorph","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ocd_vs_ptsd.get("")
async def i_ocd_vs_ptsd():
    return {"p":"diagnostico_dif_ocd_vs_ptsd","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ocd_vs_schizophrenia.get("")
async def i_ocd_vs_schizophrenia():
    return {"p":"diagnostico_dif_ocd_vs_schizophrenia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ocd_vs_tic_disorder.get("")
async def i_ocd_vs_tic_disorder():
    return {"p":"diagnostico_dif_ocd_vs_tic_disorder","s":"ativo","t":datetime.utcnow().isoformat()}
@router_orthorexia_vs_anorex.get("")
async def i_orthorexia_vs_anorex():
    return {"p":"diagnostico_dif_orthorexia_vs_anorex","s":"ativo","t":datetime.utcnow().isoformat()}
@router_parkinson_dementia.get("")
async def i_parkinson_dementia():
    return {"p":"diagnostico_dif_parkinson_dementia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_psychosis_vs_mania.get("")
async def i_psychosis_vs_mania():
    return {"p":"diagnostico_dif_psychosis_vs_mania","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ptsd_vs_anxiety.get("")
async def i_ptsd_vs_anxiety():
    return {"p":"diagnostico_dif_ptsd_vs_anxiety","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ptsd_vs_bipolar.get("")
async def i_ptsd_vs_bipolar():
    return {"p":"diagnostico_dif_ptsd_vs_bipolar","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ptsd_vs_borderline.get("")
async def i_ptsd_vs_borderline():
    return {"p":"diagnostico_dif_ptsd_vs_borderline","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ptsd_vs_depression.get("")
async def i_ptsd_vs_depression():
    return {"p":"diagnostico_dif_ptsd_vs_depression","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ptsd_vs_dissociation.get("")
async def i_ptsd_vs_dissociation():
    return {"p":"diagnostico_dif_ptsd_vs_dissociation","s":"ativo","t":datetime.utcnow().isoformat()}
@router_restrictive_avoidant.get("")
async def i_restrictive_avoidant():
    return {"p":"diagnostico_dif_restrictive_avoidant","s":"ativo","t":datetime.utcnow().isoformat()}
@router_schizophrenia_vs_aut.get("")
async def i_schizophrenia_vs_aut():
    return {"p":"diagnostico_dif_schizophrenia_vs_aut","s":"ativo","t":datetime.utcnow().isoformat()}
@router_schizophrenia_vs_bip.get("")
async def i_schizophrenia_vs_bip():
    return {"p":"diagnostico_dif_schizophrenia_vs_bip","s":"ativo","t":datetime.utcnow().isoformat()}
@router_schizophrenia_vs_dep.get("")
async def i_schizophrenia_vs_dep():
    return {"p":"diagnostico_dif_schizophrenia_vs_dep","s":"ativo","t":datetime.utcnow().isoformat()}
@router_somatic_vs_anxiety.get("")
async def i_somatic_vs_anxiety():
    return {"p":"diagnostico_dif_somatic_vs_anxiety","s":"ativo","t":datetime.utcnow().isoformat()}
@router_somatic_vs_depressio.get("")
async def i_somatic_vs_depressio():
    return {"p":"diagnostico_dif_somatic_vs_depressio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_substance_induced_vs.get("")
async def i_substance_induced_vs():
    return {"p":"diagnostico_dif_substance_induced_vs","s":"ativo","t":datetime.utcnow().isoformat()}
@router_unipolar_vs_bipolar.get("")
async def i_unipolar_vs_bipolar():
    return {"p":"diagnostico_dif_unipolar_vs_bipolar","s":"ativo","t":datetime.utcnow().isoformat()}
@router_withdrawal_vs_anxiet.get("")
async def i_withdrawal_vs_anxiet():
    return {"p":"diagnostico_dif_withdrawal_vs_anxiet","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_diagnostico_diferenc(PluginBase):
    name = "consolidated_diagnostico_diferencial"
    def setup(self, app):
        app.include_router(router_adhd_vs_anxiety)
        app.include_router(router_adhd_vs_autism)
        app.include_router(router_adhd_vs_bipolar)
        app.include_router(router_adhd_vs_learning)
        app.include_router(router_alzheimer_vs_dlb)
        app.include_router(router_alzheimer_vs_ftd)
        app.include_router(router_alzheimer_vs_vascula)
        app.include_router(router_anorexia_vs_bulimia)
        app.include_router(router_antisocial_vs_psycho)
        app.include_router(router_anxiety_vs_adhd)
        app.include_router(router_anxiety_vs_autism)
        app.include_router(router_anxiety_vs_depressio)
        app.include_router(router_attachment_vs_ptsd)
        app.include_router(router_autism_spectrum)
        app.include_router(router_autism_vs_adhd2)
        app.include_router(router_autism_vs_schizoid)
        app.include_router(router_autism_vs_social_anx)
        app.include_router(router_avoidant_vs_social_a)
        app.include_router(router_binge_vs_bulimia)
        app.include_router(router_bpd_vs_adhd)
        app.include_router(router_bpd_vs_bipolar)
        app.include_router(router_bpd_vs_narcissistic)
        app.include_router(router_bpd_vs_ptsd)
        app.include_router(router_complex_ptsd_vs_ptsd)
        app.include_router(router_conversion_vs_maling)
        app.include_router(router_delirium_vs_dementia)
        app.include_router(router_delirium_vs_depressi)
        app.include_router(router_dementia_vs_depressi)
        app.include_router(router_dependent_vs_bpd)
        app.include_router(router_depression_vs_bipola)
        app.include_router(router_depression_vs_cyclot)
        app.include_router(router_depression_vs_dysthy)
        app.include_router(router_depression_vs_grief)
        app.include_router(router_drug_induced_psychos)
        app.include_router(router_eating_disorders_dif)
        app.include_router(router_factitious_vs_somati)
        app.include_router(router_first_episode_psycho)
        app.include_router(router_ftd_vs_als)
        app.include_router(router_histrionic_vs_bpd)
        app.include_router(router_hypochondria_vs_soma)
        app.include_router(router_intoxication_vs_psyc)
        app.include_router(router_mania_vs_hypomania)
        app.include_router(router_medical_psychosis)
        app.include_router(router_mild_cognitive_vs_de)
        app.include_router(router_munchausen_vs_somati)
        app.include_router(router_night_eating_vs_bing)
        app.include_router(router_npd_vs_antisocial)
        app.include_router(router_ocd_personality_vs_o)
        app.include_router(router_ocd_vs_anxiety)
        app.include_router(router_ocd_vs_body_dysmorph)
        app.include_router(router_ocd_vs_ptsd)
        app.include_router(router_ocd_vs_schizophrenia)
        app.include_router(router_ocd_vs_tic_disorder)
        app.include_router(router_orthorexia_vs_anorex)
        app.include_router(router_parkinson_dementia)
        app.include_router(router_psychosis_vs_mania)
        app.include_router(router_ptsd_vs_anxiety)
        app.include_router(router_ptsd_vs_bipolar)
        app.include_router(router_ptsd_vs_borderline)
        app.include_router(router_ptsd_vs_depression)
        app.include_router(router_ptsd_vs_dissociation)
        app.include_router(router_restrictive_avoidant)
        app.include_router(router_schizophrenia_vs_aut)
        app.include_router(router_schizophrenia_vs_bip)
        app.include_router(router_schizophrenia_vs_dep)
        app.include_router(router_somatic_vs_anxiety)
        app.include_router(router_somatic_vs_depressio)
        app.include_router(router_substance_induced_vs)
        app.include_router(router_unipolar_vs_bipolar)
        app.include_router(router_withdrawal_vs_anxiet)


plugin = Plugin_diagnostico_diferenc()
