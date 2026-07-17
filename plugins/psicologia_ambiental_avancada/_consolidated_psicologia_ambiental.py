from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_air_pollution_mental = APIRouter(prefix="/api/v1/psicologia_a/air_pollution_mental2", tags=["psicologia_ambiental_avancada"])
router_animal_assisted_gree = APIRouter(prefix="/api/v1/psicologia_a/animal_assisted_green", tags=["psicologia_ambiental_avancada"])
router_attention_restoratio = APIRouter(prefix="/api/v1/psicologia_a/attention_restoration", tags=["psicologia_ambiental_avancada"])
router_beaches_mental = APIRouter(prefix="/api/v1/psicologia_a/beaches_mental", tags=["psicologia_ambiental_avancada"])
router_biophilia_hypothesis = APIRouter(prefix="/api/v1/psicologia_a/biophilia_hypothesis", tags=["psicologia_ambiental_avancada"])
router_biophilic_design2 = APIRouter(prefix="/api/v1/psicologia_a/biophilic_design2", tags=["psicologia_ambiental_avancada"])
router_blue_mind2 = APIRouter(prefix="/api/v1/psicologia_a/blue_mind2", tags=["psicologia_ambiental_avancada"])
router_childhood_nature = APIRouter(prefix="/api/v1/psicologia_a/childhood_nature", tags=["psicologia_ambiental_avancada"])
router_climate_change_adapt = APIRouter(prefix="/api/v1/psicologia_a/climate_change_adaptation", tags=["psicologia_ambiental_avancada"])
router_climate_distress = APIRouter(prefix="/api/v1/psicologia_a/climate_distress", tags=["psicologia_ambiental_avancada"])
router_climate_emotions = APIRouter(prefix="/api/v1/psicologia_a/climate_emotions", tags=["psicologia_ambiental_avancada"])
router_climbing_therapy = APIRouter(prefix="/api/v1/psicologia_a/climbing_therapy", tags=["psicologia_ambiental_avancada"])
router_conservation_psychol = APIRouter(prefix="/api/v1/psicologia_a/conservation_psychology", tags=["psicologia_ambiental_avancada"])
router_control_environment = APIRouter(prefix="/api/v1/psicologia_a/control_environment", tags=["psicologia_ambiental_avancada"])
router_crowding_mental = APIRouter(prefix="/api/v1/psicologia_a/crowding_mental", tags=["psicologia_ambiental_avancada"])
router_deep_ecology = APIRouter(prefix="/api/v1/psicologia_a/deep_ecology", tags=["psicologia_ambiental_avancada"])
router_directed_attention = APIRouter(prefix="/api/v1/psicologia_a/directed_attention", tags=["psicologia_ambiental_avancada"])
router_dolphin_therapy = APIRouter(prefix="/api/v1/psicologia_a/dolphin_therapy", tags=["psicologia_ambiental_avancada"])
router_eco_anxiety2 = APIRouter(prefix="/api/v1/psicologia_a/eco_anxiety2", tags=["psicologia_ambiental_avancada"])
router_eco_psychology2 = APIRouter(prefix="/api/v1/psicologia_a/eco_psychology2", tags=["psicologia_ambiental_avancada"])
router_ecological_grief = APIRouter(prefix="/api/v1/psicologia_a/ecological_grief", tags=["psicologia_ambiental_avancada"])
router_ecological_identity2 = APIRouter(prefix="/api/v1/psicologia_a/ecological_identity2", tags=["psicologia_ambiental_avancada"])
router_ecotherapy2 = APIRouter(prefix="/api/v1/psicologia_a/ecotherapy2", tags=["psicologia_ambiental_avancada"])
router_effortless_attention = APIRouter(prefix="/api/v1/psicologia_a/effortless_attention", tags=["psicologia_ambiental_avancada"])
router_environmental_comple = APIRouter(prefix="/api/v1/psicologia_a/environmental_complexity", tags=["psicologia_ambiental_avancada"])
router_environmental_identi = APIRouter(prefix="/api/v1/psicologia_a/environmental_identity", tags=["psicologia_ambiental_avancada"])
router_environmental_master = APIRouter(prefix="/api/v1/psicologia_a/environmental_mastery2", tags=["psicologia_ambiental_avancada"])
router_equine_therapy2 = APIRouter(prefix="/api/v1/psicologia_a/equine_therapy2", tags=["psicologia_ambiental_avancada"])
router_expedition_therapy = APIRouter(prefix="/api/v1/psicologia_a/expedition_therapy", tags=["psicologia_ambiental_avancada"])
router_forests_mental = APIRouter(prefix="/api/v1/psicologia_a/forests_mental", tags=["psicologia_ambiental_avancada"])
router_gardens_mental = APIRouter(prefix="/api/v1/psicologia_a/gardens_mental", tags=["psicologia_ambiental_avancada"])
router_green_exercise = APIRouter(prefix="/api/v1/psicologia_a/green_exercise", tags=["psicologia_ambiental_avancada"])
router_hard_fascination = APIRouter(prefix="/api/v1/psicologia_a/hard_fascination", tags=["psicologia_ambiental_avancada"])
router_healing_gardens = APIRouter(prefix="/api/v1/psicologia_a/healing_gardens", tags=["psicologia_ambiental_avancada"])
router_horticultural_therap = APIRouter(prefix="/api/v1/psicologia_a/horticultural_therapy2", tags=["psicologia_ambiental_avancada"])
router_houseplants_mental = APIRouter(prefix="/api/v1/psicologia_a/houseplants_mental", tags=["psicologia_ambiental_avancada"])
router_legibility = APIRouter(prefix="/api/v1/psicologia_a/legibility", tags=["psicologia_ambiental_avancada"])
router_light_pollution_ment = APIRouter(prefix="/api/v1/psicologia_a/light_pollution_mental", tags=["psicologia_ambiental_avancada"])
router_mental_fatigue2 = APIRouter(prefix="/api/v1/psicologia_a/mental_fatigue2", tags=["psicologia_ambiental_avancada"])
router_mountains_mental = APIRouter(prefix="/api/v1/psicologia_a/mountains_mental", tags=["psicologia_ambiental_avancada"])
router_natural_environment = APIRouter(prefix="/api/v1/psicologia_a/natural_environment", tags=["psicologia_ambiental_avancada"])
router_nature_based_therapy = APIRouter(prefix="/api/v1/psicologia_a/nature_based_therapy", tags=["psicologia_ambiental_avancada"])
router_nature_connectedness = APIRouter(prefix="/api/v1/psicologia_a/nature_connectedness", tags=["psicologia_ambiental_avancada"])
router_nature_experience = APIRouter(prefix="/api/v1/psicologia_a/nature_experience", tags=["psicologia_ambiental_avancada"])
router_nature_relatedness = APIRouter(prefix="/api/v1/psicologia_a/nature_relatedness", tags=["psicologia_ambiental_avancada"])
router_noise_pollution_ment = APIRouter(prefix="/api/v1/psicologia_a/noise_pollution_mental2", tags=["psicologia_ambiental_avancada"])
router_outdoor_education = APIRouter(prefix="/api/v1/psicologia_a/outdoor_education", tags=["psicologia_ambiental_avancada"])
router_parks_mental = APIRouter(prefix="/api/v1/psicologia_a/parks_mental", tags=["psicologia_ambiental_avancada"])
router_personal_space = APIRouter(prefix="/api/v1/psicologia_a/personal_space", tags=["psicologia_ambiental_avancada"])
router_place_attachment = APIRouter(prefix="/api/v1/psicologia_a/place_attachment", tags=["psicologia_ambiental_avancada"])
router_place_dependence = APIRouter(prefix="/api/v1/psicologia_a/place_dependence", tags=["psicologia_ambiental_avancada"])
router_place_familiarity = APIRouter(prefix="/api/v1/psicologia_a/place_familiarity", tags=["psicologia_ambiental_avancada"])
router_place_identity = APIRouter(prefix="/api/v1/psicologia_a/place_identity", tags=["psicologia_ambiental_avancada"])
router_pre_traumatic_stress = APIRouter(prefix="/api/v1/psicologia_a/pre_traumatic_stress", tags=["psicologia_ambiental_avancada"])
router_privacy_environmenta = APIRouter(prefix="/api/v1/psicologia_a/privacy_environmental", tags=["psicologia_ambiental_avancada"])
router_pro_environmental = APIRouter(prefix="/api/v1/psicologia_a/pro_environmental", tags=["psicologia_ambiental_avancada"])
router_restoration_green = APIRouter(prefix="/api/v1/psicologia_a/restoration_green", tags=["psicologia_ambiental_avancada"])
router_restorative_environm = APIRouter(prefix="/api/v1/psicologia_a/restorative_environments", tags=["psicologia_ambiental_avancada"])
router_restorative_experien = APIRouter(prefix="/api/v1/psicologia_a/restorative_experience", tags=["psicologia_ambiental_avancada"])
router_rivers_mental = APIRouter(prefix="/api/v1/psicologia_a/rivers_mental", tags=["psicologia_ambiental_avancada"])
router_sensory_deprivation2 = APIRouter(prefix="/api/v1/psicologia_a/sensory_deprivation2", tags=["psicologia_ambiental_avancada"])
router_sensory_overload = APIRouter(prefix="/api/v1/psicologia_a/sensory_overload", tags=["psicologia_ambiental_avancada"])
router_soft_fascination = APIRouter(prefix="/api/v1/psicologia_a/soft_fascination", tags=["psicologia_ambiental_avancada"])
router_solastalgia2 = APIRouter(prefix="/api/v1/psicologia_a/solastalgia2", tags=["psicologia_ambiental_avancada"])
router_stress_recovery_theo = APIRouter(prefix="/api/v1/psicologia_a/stress_recovery_theory", tags=["psicologia_ambiental_avancada"])
router_surf_therapy2 = APIRouter(prefix="/api/v1/psicologia_a/surf_therapy2", tags=["psicologia_ambiental_avancada"])
router_sustainable_behavior = APIRouter(prefix="/api/v1/psicologia_a/sustainable_behavior", tags=["psicologia_ambiental_avancada"])
router_territoriality = APIRouter(prefix="/api/v1/psicologia_a/territoriality", tags=["psicologia_ambiental_avancada"])
router_thermal_comfort_ment = APIRouter(prefix="/api/v1/psicologia_a/thermal_comfort_mental2", tags=["psicologia_ambiental_avancada"])
router_topophilia = APIRouter(prefix="/api/v1/psicologia_a/topophilia", tags=["psicologia_ambiental_avancada"])
router_urban_green = APIRouter(prefix="/api/v1/psicologia_a/urban_green", tags=["psicologia_ambiental_avancada"])
router_urban_green_health = APIRouter(prefix="/api/v1/psicologia_a/urban_green_health", tags=["psicologia_ambiental_avancada"])
router_urban_nature = APIRouter(prefix="/api/v1/psicologia_a/urban_nature", tags=["psicologia_ambiental_avancada"])
router_wayfinding = APIRouter(prefix="/api/v1/psicologia_a/wayfinding", tags=["psicologia_ambiental_avancada"])
router_wilderness_adventure = APIRouter(prefix="/api/v1/psicologia_a/wilderness_adventure", tags=["psicologia_ambiental_avancada"])
router_wilderness_therapy2 = APIRouter(prefix="/api/v1/psicologia_a/wilderness_therapy2", tags=["psicologia_ambiental_avancada"])

@router_air_pollution_mental.get("")
async def i_air_pollution_mental():
    return {"p":"psicologia_ambi_air_pollution_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_animal_assisted_gree.get("")
async def i_animal_assisted_gree():
    return {"p":"psicologia_ambi_animal_assisted_gree","s":"ativo","t":datetime.utcnow().isoformat()}
@router_attention_restoratio.get("")
async def i_attention_restoratio():
    return {"p":"psicologia_ambi_attention_restoratio","s":"ativo","t":datetime.utcnow().isoformat()}
@router_beaches_mental.get("")
async def i_beaches_mental():
    return {"p":"psicologia_ambi_beaches_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_biophilia_hypothesis.get("")
async def i_biophilia_hypothesis():
    return {"p":"psicologia_ambi_biophilia_hypothesis","s":"ativo","t":datetime.utcnow().isoformat()}
@router_biophilic_design2.get("")
async def i_biophilic_design2():
    return {"p":"psicologia_ambi_biophilic_design2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_blue_mind2.get("")
async def i_blue_mind2():
    return {"p":"psicologia_ambi_blue_mind2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_childhood_nature.get("")
async def i_childhood_nature():
    return {"p":"psicologia_ambi_childhood_nature","s":"ativo","t":datetime.utcnow().isoformat()}
@router_climate_change_adapt.get("")
async def i_climate_change_adapt():
    return {"p":"psicologia_ambi_climate_change_adapt","s":"ativo","t":datetime.utcnow().isoformat()}
@router_climate_distress.get("")
async def i_climate_distress():
    return {"p":"psicologia_ambi_climate_distress","s":"ativo","t":datetime.utcnow().isoformat()}
@router_climate_emotions.get("")
async def i_climate_emotions():
    return {"p":"psicologia_ambi_climate_emotions","s":"ativo","t":datetime.utcnow().isoformat()}
@router_climbing_therapy.get("")
async def i_climbing_therapy():
    return {"p":"psicologia_ambi_climbing_therapy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_conservation_psychol.get("")
async def i_conservation_psychol():
    return {"p":"psicologia_ambi_conservation_psychol","s":"ativo","t":datetime.utcnow().isoformat()}
@router_control_environment.get("")
async def i_control_environment():
    return {"p":"psicologia_ambi_control_environment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_crowding_mental.get("")
async def i_crowding_mental():
    return {"p":"psicologia_ambi_crowding_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_deep_ecology.get("")
async def i_deep_ecology():
    return {"p":"psicologia_ambi_deep_ecology","s":"ativo","t":datetime.utcnow().isoformat()}
@router_directed_attention.get("")
async def i_directed_attention():
    return {"p":"psicologia_ambi_directed_attention","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dolphin_therapy.get("")
async def i_dolphin_therapy():
    return {"p":"psicologia_ambi_dolphin_therapy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_eco_anxiety2.get("")
async def i_eco_anxiety2():
    return {"p":"psicologia_ambi_eco_anxiety2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_eco_psychology2.get("")
async def i_eco_psychology2():
    return {"p":"psicologia_ambi_eco_psychology2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ecological_grief.get("")
async def i_ecological_grief():
    return {"p":"psicologia_ambi_ecological_grief","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ecological_identity2.get("")
async def i_ecological_identity2():
    return {"p":"psicologia_ambi_ecological_identity2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ecotherapy2.get("")
async def i_ecotherapy2():
    return {"p":"psicologia_ambi_ecotherapy2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_effortless_attention.get("")
async def i_effortless_attention():
    return {"p":"psicologia_ambi_effortless_attention","s":"ativo","t":datetime.utcnow().isoformat()}
@router_environmental_comple.get("")
async def i_environmental_comple():
    return {"p":"psicologia_ambi_environmental_comple","s":"ativo","t":datetime.utcnow().isoformat()}
@router_environmental_identi.get("")
async def i_environmental_identi():
    return {"p":"psicologia_ambi_environmental_identi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_environmental_master.get("")
async def i_environmental_master():
    return {"p":"psicologia_ambi_environmental_master","s":"ativo","t":datetime.utcnow().isoformat()}
@router_equine_therapy2.get("")
async def i_equine_therapy2():
    return {"p":"psicologia_ambi_equine_therapy2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_expedition_therapy.get("")
async def i_expedition_therapy():
    return {"p":"psicologia_ambi_expedition_therapy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_forests_mental.get("")
async def i_forests_mental():
    return {"p":"psicologia_ambi_forests_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gardens_mental.get("")
async def i_gardens_mental():
    return {"p":"psicologia_ambi_gardens_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_green_exercise.get("")
async def i_green_exercise():
    return {"p":"psicologia_ambi_green_exercise","s":"ativo","t":datetime.utcnow().isoformat()}
@router_hard_fascination.get("")
async def i_hard_fascination():
    return {"p":"psicologia_ambi_hard_fascination","s":"ativo","t":datetime.utcnow().isoformat()}
@router_healing_gardens.get("")
async def i_healing_gardens():
    return {"p":"psicologia_ambi_healing_gardens","s":"ativo","t":datetime.utcnow().isoformat()}
@router_horticultural_therap.get("")
async def i_horticultural_therap():
    return {"p":"psicologia_ambi_horticultural_therap","s":"ativo","t":datetime.utcnow().isoformat()}
@router_houseplants_mental.get("")
async def i_houseplants_mental():
    return {"p":"psicologia_ambi_houseplants_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_legibility.get("")
async def i_legibility():
    return {"p":"psicologia_ambi_legibility","s":"ativo","t":datetime.utcnow().isoformat()}
@router_light_pollution_ment.get("")
async def i_light_pollution_ment():
    return {"p":"psicologia_ambi_light_pollution_ment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mental_fatigue2.get("")
async def i_mental_fatigue2():
    return {"p":"psicologia_ambi_mental_fatigue2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mountains_mental.get("")
async def i_mountains_mental():
    return {"p":"psicologia_ambi_mountains_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_natural_environment.get("")
async def i_natural_environment():
    return {"p":"psicologia_ambi_natural_environment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nature_based_therapy.get("")
async def i_nature_based_therapy():
    return {"p":"psicologia_ambi_nature_based_therapy","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nature_connectedness.get("")
async def i_nature_connectedness():
    return {"p":"psicologia_ambi_nature_connectedness","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nature_experience.get("")
async def i_nature_experience():
    return {"p":"psicologia_ambi_nature_experience","s":"ativo","t":datetime.utcnow().isoformat()}
@router_nature_relatedness.get("")
async def i_nature_relatedness():
    return {"p":"psicologia_ambi_nature_relatedness","s":"ativo","t":datetime.utcnow().isoformat()}
@router_noise_pollution_ment.get("")
async def i_noise_pollution_ment():
    return {"p":"psicologia_ambi_noise_pollution_ment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_outdoor_education.get("")
async def i_outdoor_education():
    return {"p":"psicologia_ambi_outdoor_education","s":"ativo","t":datetime.utcnow().isoformat()}
@router_parks_mental.get("")
async def i_parks_mental():
    return {"p":"psicologia_ambi_parks_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_personal_space.get("")
async def i_personal_space():
    return {"p":"psicologia_ambi_personal_space","s":"ativo","t":datetime.utcnow().isoformat()}
@router_place_attachment.get("")
async def i_place_attachment():
    return {"p":"psicologia_ambi_place_attachment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_place_dependence.get("")
async def i_place_dependence():
    return {"p":"psicologia_ambi_place_dependence","s":"ativo","t":datetime.utcnow().isoformat()}
@router_place_familiarity.get("")
async def i_place_familiarity():
    return {"p":"psicologia_ambi_place_familiarity","s":"ativo","t":datetime.utcnow().isoformat()}
@router_place_identity.get("")
async def i_place_identity():
    return {"p":"psicologia_ambi_place_identity","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pre_traumatic_stress.get("")
async def i_pre_traumatic_stress():
    return {"p":"psicologia_ambi_pre_traumatic_stress","s":"ativo","t":datetime.utcnow().isoformat()}
@router_privacy_environmenta.get("")
async def i_privacy_environmenta():
    return {"p":"psicologia_ambi_privacy_environmenta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pro_environmental.get("")
async def i_pro_environmental():
    return {"p":"psicologia_ambi_pro_environmental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_restoration_green.get("")
async def i_restoration_green():
    return {"p":"psicologia_ambi_restoration_green","s":"ativo","t":datetime.utcnow().isoformat()}
@router_restorative_environm.get("")
async def i_restorative_environm():
    return {"p":"psicologia_ambi_restorative_environm","s":"ativo","t":datetime.utcnow().isoformat()}
@router_restorative_experien.get("")
async def i_restorative_experien():
    return {"p":"psicologia_ambi_restorative_experien","s":"ativo","t":datetime.utcnow().isoformat()}
@router_rivers_mental.get("")
async def i_rivers_mental():
    return {"p":"psicologia_ambi_rivers_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sensory_deprivation2.get("")
async def i_sensory_deprivation2():
    return {"p":"psicologia_ambi_sensory_deprivation2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sensory_overload.get("")
async def i_sensory_overload():
    return {"p":"psicologia_ambi_sensory_overload","s":"ativo","t":datetime.utcnow().isoformat()}
@router_soft_fascination.get("")
async def i_soft_fascination():
    return {"p":"psicologia_ambi_soft_fascination","s":"ativo","t":datetime.utcnow().isoformat()}
@router_solastalgia2.get("")
async def i_solastalgia2():
    return {"p":"psicologia_ambi_solastalgia2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_stress_recovery_theo.get("")
async def i_stress_recovery_theo():
    return {"p":"psicologia_ambi_stress_recovery_theo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_surf_therapy2.get("")
async def i_surf_therapy2():
    return {"p":"psicologia_ambi_surf_therapy2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sustainable_behavior.get("")
async def i_sustainable_behavior():
    return {"p":"psicologia_ambi_sustainable_behavior","s":"ativo","t":datetime.utcnow().isoformat()}
@router_territoriality.get("")
async def i_territoriality():
    return {"p":"psicologia_ambi_territoriality","s":"ativo","t":datetime.utcnow().isoformat()}
@router_thermal_comfort_ment.get("")
async def i_thermal_comfort_ment():
    return {"p":"psicologia_ambi_thermal_comfort_ment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_topophilia.get("")
async def i_topophilia():
    return {"p":"psicologia_ambi_topophilia","s":"ativo","t":datetime.utcnow().isoformat()}
@router_urban_green.get("")
async def i_urban_green():
    return {"p":"psicologia_ambi_urban_green","s":"ativo","t":datetime.utcnow().isoformat()}
@router_urban_green_health.get("")
async def i_urban_green_health():
    return {"p":"psicologia_ambi_urban_green_health","s":"ativo","t":datetime.utcnow().isoformat()}
@router_urban_nature.get("")
async def i_urban_nature():
    return {"p":"psicologia_ambi_urban_nature","s":"ativo","t":datetime.utcnow().isoformat()}
@router_wayfinding.get("")
async def i_wayfinding():
    return {"p":"psicologia_ambi_wayfinding","s":"ativo","t":datetime.utcnow().isoformat()}
@router_wilderness_adventure.get("")
async def i_wilderness_adventure():
    return {"p":"psicologia_ambi_wilderness_adventure","s":"ativo","t":datetime.utcnow().isoformat()}
@router_wilderness_therapy2.get("")
async def i_wilderness_therapy2():
    return {"p":"psicologia_ambi_wilderness_therapy2","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_psicologia_ambiental(PluginBase):
    name = "consolidated_psicologia_ambiental_avancada"
    def setup(self, app):
        app.include_router(router_air_pollution_mental)
        app.include_router(router_animal_assisted_gree)
        app.include_router(router_attention_restoratio)
        app.include_router(router_beaches_mental)
        app.include_router(router_biophilia_hypothesis)
        app.include_router(router_biophilic_design2)
        app.include_router(router_blue_mind2)
        app.include_router(router_childhood_nature)
        app.include_router(router_climate_change_adapt)
        app.include_router(router_climate_distress)
        app.include_router(router_climate_emotions)
        app.include_router(router_climbing_therapy)
        app.include_router(router_conservation_psychol)
        app.include_router(router_control_environment)
        app.include_router(router_crowding_mental)
        app.include_router(router_deep_ecology)
        app.include_router(router_directed_attention)
        app.include_router(router_dolphin_therapy)
        app.include_router(router_eco_anxiety2)
        app.include_router(router_eco_psychology2)
        app.include_router(router_ecological_grief)
        app.include_router(router_ecological_identity2)
        app.include_router(router_ecotherapy2)
        app.include_router(router_effortless_attention)
        app.include_router(router_environmental_comple)
        app.include_router(router_environmental_identi)
        app.include_router(router_environmental_master)
        app.include_router(router_equine_therapy2)
        app.include_router(router_expedition_therapy)
        app.include_router(router_forests_mental)
        app.include_router(router_gardens_mental)
        app.include_router(router_green_exercise)
        app.include_router(router_hard_fascination)
        app.include_router(router_healing_gardens)
        app.include_router(router_horticultural_therap)
        app.include_router(router_houseplants_mental)
        app.include_router(router_legibility)
        app.include_router(router_light_pollution_ment)
        app.include_router(router_mental_fatigue2)
        app.include_router(router_mountains_mental)
        app.include_router(router_natural_environment)
        app.include_router(router_nature_based_therapy)
        app.include_router(router_nature_connectedness)
        app.include_router(router_nature_experience)
        app.include_router(router_nature_relatedness)
        app.include_router(router_noise_pollution_ment)
        app.include_router(router_outdoor_education)
        app.include_router(router_parks_mental)
        app.include_router(router_personal_space)
        app.include_router(router_place_attachment)
        app.include_router(router_place_dependence)
        app.include_router(router_place_familiarity)
        app.include_router(router_place_identity)
        app.include_router(router_pre_traumatic_stress)
        app.include_router(router_privacy_environmenta)
        app.include_router(router_pro_environmental)
        app.include_router(router_restoration_green)
        app.include_router(router_restorative_environm)
        app.include_router(router_restorative_experien)
        app.include_router(router_rivers_mental)
        app.include_router(router_sensory_deprivation2)
        app.include_router(router_sensory_overload)
        app.include_router(router_soft_fascination)
        app.include_router(router_solastalgia2)
        app.include_router(router_stress_recovery_theo)
        app.include_router(router_surf_therapy2)
        app.include_router(router_sustainable_behavior)
        app.include_router(router_territoriality)
        app.include_router(router_thermal_comfort_ment)
        app.include_router(router_topophilia)
        app.include_router(router_urban_green)
        app.include_router(router_urban_green_health)
        app.include_router(router_urban_nature)
        app.include_router(router_wayfinding)
        app.include_router(router_wilderness_adventure)
        app.include_router(router_wilderness_therapy2)


plugin = Plugin_psicologia_ambiental()
