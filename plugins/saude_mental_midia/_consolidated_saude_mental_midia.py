from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router_FOMO_mental = APIRouter(prefix="/api/v1/saude_mental/FOMO_mental", tags=["saude_mental_midia"])
router_JOMO_mental = APIRouter(prefix="/api/v1/saude_mental/JOMO_mental", tags=["saude_mental_midia"])
router_Werther_effect2 = APIRouter(prefix="/api/v1/saude_mental/Werther_effect2", tags=["saude_mental_midia"])
router_ability_comparison = APIRouter(prefix="/api/v1/saude_mental/ability_comparison", tags=["saude_mental_midia"])
router_agenda_setting_menta = APIRouter(prefix="/api/v1/saude_mental/agenda_setting_mental", tags=["saude_mental_midia"])
router_anti_stigma_campaign = APIRouter(prefix="/api/v1/saude_mental/anti_stigma_campaign", tags=["saude_mental_midia"])
router_appearance_compariso = APIRouter(prefix="/api/v1/saude_mental/appearance_comparison", tags=["saude_mental_midia"])
router_art_mental_health2 = APIRouter(prefix="/api/v1/saude_mental/art_mental_health2", tags=["saude_mental_midia"])
router_bell_lets_talk = APIRouter(prefix="/api/v1/saude_mental/bell_lets_talk", tags=["saude_mental_midia"])
router_bibliotherapy2 = APIRouter(prefix="/api/v1/saude_mental/bibliotherapy2", tags=["saude_mental_midia"])
router_blog_mental_health2 = APIRouter(prefix="/api/v1/saude_mental/blog_mental_health2", tags=["saude_mental_midia"])
router_book_mental_health = APIRouter(prefix="/api/v1/saude_mental/book_mental_health", tags=["saude_mental_midia"])
router_celebrity_mental_hea = APIRouter(prefix="/api/v1/saude_mental/celebrity_mental_health", tags=["saude_mental_midia"])
router_cluster_suicide_medi = APIRouter(prefix="/api/v1/saude_mental/cluster_suicide_media", tags=["saude_mental_midia"])
router_comedy_mental = APIRouter(prefix="/api/v1/saude_mental/comedy_mental", tags=["saude_mental_midia"])
router_comics_mental = APIRouter(prefix="/api/v1/saude_mental/comics_mental", tags=["saude_mental_midia"])
router_contagion_media = APIRouter(prefix="/api/v1/saude_mental/contagion_media", tags=["saude_mental_midia"])
router_criminalization_ment = APIRouter(prefix="/api/v1/saude_mental/criminalization_mental", tags=["saude_mental_midia"])
router_cultivation_theory = APIRouter(prefix="/api/v1/saude_mental/cultivation_theory", tags=["saude_mental_midia"])
router_dance_mental = APIRouter(prefix="/api/v1/saude_mental/dance_mental", tags=["saude_mental_midia"])
router_destigmatization_med = APIRouter(prefix="/api/v1/saude_mental/destigmatization_media", tags=["saude_mental_midia"])
router_discord_mental = APIRouter(prefix="/api/v1/saude_mental/discord_mental", tags=["saude_mental_midia"])
router_documentary_mental = APIRouter(prefix="/api/v1/saude_mental/documentary_mental", tags=["saude_mental_midia"])
router_downward_social_comp = APIRouter(prefix="/api/v1/saude_mental/downward_social_compariso", tags=["saude_mental_midia"])
router_facebook_mental_heal = APIRouter(prefix="/api/v1/saude_mental/facebook_mental_health", tags=["saude_mental_midia"])
router_fiction_mental_healt = APIRouter(prefix="/api/v1/saude_mental/fiction_mental_health", tags=["saude_mental_midia"])
router_film_mental_health = APIRouter(prefix="/api/v1/saude_mental/film_mental_health", tags=["saude_mental_midia"])
router_framing_mental_healt = APIRouter(prefix="/api/v1/saude_mental/framing_mental_health", tags=["saude_mental_midia"])
router_gallery_mental = APIRouter(prefix="/api/v1/saude_mental/gallery_mental", tags=["saude_mental_midia"])
router_graphic_novel_mental = APIRouter(prefix="/api/v1/saude_mental/graphic_novel_mental2", tags=["saude_mental_midia"])
router_heads_together = APIRouter(prefix="/api/v1/saude_mental/heads_together", tags=["saude_mental_midia"])
router_humor_health = APIRouter(prefix="/api/v1/saude_mental/humor_health", tags=["saude_mental_midia"])
router_imitation_media = APIRouter(prefix="/api/v1/saude_mental/imitation_media", tags=["saude_mental_midia"])
router_influencer_mental_he = APIRouter(prefix="/api/v1/saude_mental/influencer_mental_health", tags=["saude_mental_midia"])
router_instagram_mental_hea = APIRouter(prefix="/api/v1/saude_mental/instagram_mental_health", tags=["saude_mental_midia"])
router_lateral_social_compa = APIRouter(prefix="/api/v1/saude_mental/lateral_social_comparison", tags=["saude_mental_midia"])
router_laughter_therapy2 = APIRouter(prefix="/api/v1/saude_mental/laughter_therapy2", tags=["saude_mental_midia"])
router_lifestyle_comparison = APIRouter(prefix="/api/v1/saude_mental/lifestyle_comparison", tags=["saude_mental_midia"])
router_linkedin_mental = APIRouter(prefix="/api/v1/saude_mental/linkedin_mental", tags=["saude_mental_midia"])
router_media_campaign_menta = APIRouter(prefix="/api/v1/saude_mental/media_campaign_mental", tags=["saude_mental_midia"])
router_media_effects_mental = APIRouter(prefix="/api/v1/saude_mental/media_effects_mental", tags=["saude_mental_midia"])
router_media_intervention = APIRouter(prefix="/api/v1/saude_mental/media_intervention", tags=["saude_mental_midia"])
router_media_literacy_menta = APIRouter(prefix="/api/v1/saude_mental/media_literacy_mental", tags=["saude_mental_midia"])
router_memoir_mental = APIRouter(prefix="/api/v1/saude_mental/memoir_mental", tags=["saude_mental_midia"])
router_mental_health_awaren = APIRouter(prefix="/api/v1/saude_mental/mental_health_awareness", tags=["saude_mental_midia"])
router_mental_health_month = APIRouter(prefix="/api/v1/saude_mental/mental_health_month", tags=["saude_mental_midia"])
router_museum_mental = APIRouter(prefix="/api/v1/saude_mental/museum_mental", tags=["saude_mental_midia"])
router_music_festival_menta = APIRouter(prefix="/api/v1/saude_mental/music_festival_mental", tags=["saude_mental_midia"])
router_music_mental_health = APIRouter(prefix="/api/v1/saude_mental/music_mental_health", tags=["saude_mental_midia"])
router_newsletter_mental = APIRouter(prefix="/api/v1/saude_mental/newsletter_mental", tags=["saude_mental_midia"])
router_online_connection = APIRouter(prefix="/api/v1/saude_mental/online_connection", tags=["saude_mental_midia"])
router_opera_mental = APIRouter(prefix="/api/v1/saude_mental/opera_mental", tags=["saude_mental_midia"])
router_opinion_comparison = APIRouter(prefix="/api/v1/saude_mental/opinion_comparison", tags=["saude_mental_midia"])
router_papageno_effect2 = APIRouter(prefix="/api/v1/saude_mental/papageno_effect2", tags=["saude_mental_midia"])
router_parasocial_mental = APIRouter(prefix="/api/v1/saude_mental/parasocial_mental", tags=["saude_mental_midia"])
router_pinterest_mental = APIRouter(prefix="/api/v1/saude_mental/pinterest_mental", tags=["saude_mental_midia"])
router_podcast_mental2 = APIRouter(prefix="/api/v1/saude_mental/podcast_mental2", tags=["saude_mental_midia"])
router_priming_mental = APIRouter(prefix="/api/v1/saude_mental/priming_mental", tags=["saude_mental_midia"])
router_public_education_cam = APIRouter(prefix="/api/v1/saude_mental/public_education_campaign", tags=["saude_mental_midia"])
router_public_figure_disclo = APIRouter(prefix="/api/v1/saude_mental/public_figure_disclosure", tags=["saude_mental_midia"])
router_reddit_mental = APIRouter(prefix="/api/v1/saude_mental/reddit_mental", tags=["saude_mental_midia"])
router_representation_menta = APIRouter(prefix="/api/v1/saude_mental/representation_mental", tags=["saude_mental_midia"])
router_responsible_reportin = APIRouter(prefix="/api/v1/saude_mental/responsible_reporting2", tags=["saude_mental_midia"])
router_safe_messaging_guide = APIRouter(prefix="/api/v1/saude_mental/safe_messaging_guidelines", tags=["saude_mental_midia"])
router_schema_media = APIRouter(prefix="/api/v1/saude_mental/schema_media", tags=["saude_mental_midia"])
router_sensationalism_menta = APIRouter(prefix="/api/v1/saude_mental/sensationalism_mental", tags=["saude_mental_midia"])
router_snapchat_mental = APIRouter(prefix="/api/v1/saude_mental/snapchat_mental", tags=["saude_mental_midia"])
router_social_comparison_me = APIRouter(prefix="/api/v1/saude_mental/social_comparison_media", tags=["saude_mental_midia"])
router_social_comparison_or = APIRouter(prefix="/api/v1/saude_mental/social_comparison_orienta", tags=["saude_mental_midia"])
router_social_media_anxiety = APIRouter(prefix="/api/v1/saude_mental/social_media_anxiety", tags=["saude_mental_midia"])
router_social_media_depress = APIRouter(prefix="/api/v1/saude_mental/social_media_depression", tags=["saude_mental_midia"])
router_social_media_lonelin = APIRouter(prefix="/api/v1/saude_mental/social_media_loneliness", tags=["saude_mental_midia"])
router_stand_up_mental = APIRouter(prefix="/api/v1/saude_mental/stand_up_mental", tags=["saude_mental_midia"])
router_stereotypes_media = APIRouter(prefix="/api/v1/saude_mental/stereotypes_media", tags=["saude_mental_midia"])
router_storytelling_mental = APIRouter(prefix="/api/v1/saude_mental/storytelling_mental", tags=["saude_mental_midia"])
router_suicide_reporting2 = APIRouter(prefix="/api/v1/saude_mental/suicide_reporting2", tags=["saude_mental_midia"])
router_theater_mental2 = APIRouter(prefix="/api/v1/saude_mental/theater_mental2", tags=["saude_mental_midia"])
router_tiktok_mental_health = APIRouter(prefix="/api/v1/saude_mental/tiktok_mental_health", tags=["saude_mental_midia"])
router_time_to_change = APIRouter(prefix="/api/v1/saude_mental/time_to_change", tags=["saude_mental_midia"])
router_twitch_mental = APIRouter(prefix="/api/v1/saude_mental/twitch_mental", tags=["saude_mental_midia"])
router_twitter_mental = APIRouter(prefix="/api/v1/saude_mental/twitter_mental", tags=["saude_mental_midia"])
router_upward_social_compar = APIRouter(prefix="/api/v1/saude_mental/upward_social_comparison", tags=["saude_mental_midia"])
router_world_mental_health_ = APIRouter(prefix="/api/v1/saude_mental/world_mental_health_day", tags=["saude_mental_midia"])
router_youtube_mental = APIRouter(prefix="/api/v1/saude_mental/youtube_mental", tags=["saude_mental_midia"])

@router_FOMO_mental.get("")
async def i_FOMO_mental():
    return {"p":"saude_mental_mi_FOMO_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_JOMO_mental.get("")
async def i_JOMO_mental():
    return {"p":"saude_mental_mi_JOMO_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_Werther_effect2.get("")
async def i_Werther_effect2():
    return {"p":"saude_mental_mi_Werther_effect2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_ability_comparison.get("")
async def i_ability_comparison():
    return {"p":"saude_mental_mi_ability_comparison","s":"ativo","t":datetime.utcnow().isoformat()}
@router_agenda_setting_menta.get("")
async def i_agenda_setting_menta():
    return {"p":"saude_mental_mi_agenda_setting_menta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_anti_stigma_campaign.get("")
async def i_anti_stigma_campaign():
    return {"p":"saude_mental_mi_anti_stigma_campaign","s":"ativo","t":datetime.utcnow().isoformat()}
@router_appearance_compariso.get("")
async def i_appearance_compariso():
    return {"p":"saude_mental_mi_appearance_compariso","s":"ativo","t":datetime.utcnow().isoformat()}
@router_art_mental_health2.get("")
async def i_art_mental_health2():
    return {"p":"saude_mental_mi_art_mental_health2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bell_lets_talk.get("")
async def i_bell_lets_talk():
    return {"p":"saude_mental_mi_bell_lets_talk","s":"ativo","t":datetime.utcnow().isoformat()}
@router_bibliotherapy2.get("")
async def i_bibliotherapy2():
    return {"p":"saude_mental_mi_bibliotherapy2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_blog_mental_health2.get("")
async def i_blog_mental_health2():
    return {"p":"saude_mental_mi_blog_mental_health2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_book_mental_health.get("")
async def i_book_mental_health():
    return {"p":"saude_mental_mi_book_mental_health","s":"ativo","t":datetime.utcnow().isoformat()}
@router_celebrity_mental_hea.get("")
async def i_celebrity_mental_hea():
    return {"p":"saude_mental_mi_celebrity_mental_hea","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cluster_suicide_medi.get("")
async def i_cluster_suicide_medi():
    return {"p":"saude_mental_mi_cluster_suicide_medi","s":"ativo","t":datetime.utcnow().isoformat()}
@router_comedy_mental.get("")
async def i_comedy_mental():
    return {"p":"saude_mental_mi_comedy_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_comics_mental.get("")
async def i_comics_mental():
    return {"p":"saude_mental_mi_comics_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_contagion_media.get("")
async def i_contagion_media():
    return {"p":"saude_mental_mi_contagion_media","s":"ativo","t":datetime.utcnow().isoformat()}
@router_criminalization_ment.get("")
async def i_criminalization_ment():
    return {"p":"saude_mental_mi_criminalization_ment","s":"ativo","t":datetime.utcnow().isoformat()}
@router_cultivation_theory.get("")
async def i_cultivation_theory():
    return {"p":"saude_mental_mi_cultivation_theory","s":"ativo","t":datetime.utcnow().isoformat()}
@router_dance_mental.get("")
async def i_dance_mental():
    return {"p":"saude_mental_mi_dance_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_destigmatization_med.get("")
async def i_destigmatization_med():
    return {"p":"saude_mental_mi_destigmatization_med","s":"ativo","t":datetime.utcnow().isoformat()}
@router_discord_mental.get("")
async def i_discord_mental():
    return {"p":"saude_mental_mi_discord_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_documentary_mental.get("")
async def i_documentary_mental():
    return {"p":"saude_mental_mi_documentary_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_downward_social_comp.get("")
async def i_downward_social_comp():
    return {"p":"saude_mental_mi_downward_social_comp","s":"ativo","t":datetime.utcnow().isoformat()}
@router_facebook_mental_heal.get("")
async def i_facebook_mental_heal():
    return {"p":"saude_mental_mi_facebook_mental_heal","s":"ativo","t":datetime.utcnow().isoformat()}
@router_fiction_mental_healt.get("")
async def i_fiction_mental_healt():
    return {"p":"saude_mental_mi_fiction_mental_healt","s":"ativo","t":datetime.utcnow().isoformat()}
@router_film_mental_health.get("")
async def i_film_mental_health():
    return {"p":"saude_mental_mi_film_mental_health","s":"ativo","t":datetime.utcnow().isoformat()}
@router_framing_mental_healt.get("")
async def i_framing_mental_healt():
    return {"p":"saude_mental_mi_framing_mental_healt","s":"ativo","t":datetime.utcnow().isoformat()}
@router_gallery_mental.get("")
async def i_gallery_mental():
    return {"p":"saude_mental_mi_gallery_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_graphic_novel_mental.get("")
async def i_graphic_novel_mental():
    return {"p":"saude_mental_mi_graphic_novel_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_heads_together.get("")
async def i_heads_together():
    return {"p":"saude_mental_mi_heads_together","s":"ativo","t":datetime.utcnow().isoformat()}
@router_humor_health.get("")
async def i_humor_health():
    return {"p":"saude_mental_mi_humor_health","s":"ativo","t":datetime.utcnow().isoformat()}
@router_imitation_media.get("")
async def i_imitation_media():
    return {"p":"saude_mental_mi_imitation_media","s":"ativo","t":datetime.utcnow().isoformat()}
@router_influencer_mental_he.get("")
async def i_influencer_mental_he():
    return {"p":"saude_mental_mi_influencer_mental_he","s":"ativo","t":datetime.utcnow().isoformat()}
@router_instagram_mental_hea.get("")
async def i_instagram_mental_hea():
    return {"p":"saude_mental_mi_instagram_mental_hea","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lateral_social_compa.get("")
async def i_lateral_social_compa():
    return {"p":"saude_mental_mi_lateral_social_compa","s":"ativo","t":datetime.utcnow().isoformat()}
@router_laughter_therapy2.get("")
async def i_laughter_therapy2():
    return {"p":"saude_mental_mi_laughter_therapy2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_lifestyle_comparison.get("")
async def i_lifestyle_comparison():
    return {"p":"saude_mental_mi_lifestyle_comparison","s":"ativo","t":datetime.utcnow().isoformat()}
@router_linkedin_mental.get("")
async def i_linkedin_mental():
    return {"p":"saude_mental_mi_linkedin_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_media_campaign_menta.get("")
async def i_media_campaign_menta():
    return {"p":"saude_mental_mi_media_campaign_menta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_media_effects_mental.get("")
async def i_media_effects_mental():
    return {"p":"saude_mental_mi_media_effects_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_media_intervention.get("")
async def i_media_intervention():
    return {"p":"saude_mental_mi_media_intervention","s":"ativo","t":datetime.utcnow().isoformat()}
@router_media_literacy_menta.get("")
async def i_media_literacy_menta():
    return {"p":"saude_mental_mi_media_literacy_menta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_memoir_mental.get("")
async def i_memoir_mental():
    return {"p":"saude_mental_mi_memoir_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mental_health_awaren.get("")
async def i_mental_health_awaren():
    return {"p":"saude_mental_mi_mental_health_awaren","s":"ativo","t":datetime.utcnow().isoformat()}
@router_mental_health_month.get("")
async def i_mental_health_month():
    return {"p":"saude_mental_mi_mental_health_month","s":"ativo","t":datetime.utcnow().isoformat()}
@router_museum_mental.get("")
async def i_museum_mental():
    return {"p":"saude_mental_mi_museum_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_music_festival_menta.get("")
async def i_music_festival_menta():
    return {"p":"saude_mental_mi_music_festival_menta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_music_mental_health.get("")
async def i_music_mental_health():
    return {"p":"saude_mental_mi_music_mental_health","s":"ativo","t":datetime.utcnow().isoformat()}
@router_newsletter_mental.get("")
async def i_newsletter_mental():
    return {"p":"saude_mental_mi_newsletter_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_online_connection.get("")
async def i_online_connection():
    return {"p":"saude_mental_mi_online_connection","s":"ativo","t":datetime.utcnow().isoformat()}
@router_opera_mental.get("")
async def i_opera_mental():
    return {"p":"saude_mental_mi_opera_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_opinion_comparison.get("")
async def i_opinion_comparison():
    return {"p":"saude_mental_mi_opinion_comparison","s":"ativo","t":datetime.utcnow().isoformat()}
@router_papageno_effect2.get("")
async def i_papageno_effect2():
    return {"p":"saude_mental_mi_papageno_effect2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_parasocial_mental.get("")
async def i_parasocial_mental():
    return {"p":"saude_mental_mi_parasocial_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_pinterest_mental.get("")
async def i_pinterest_mental():
    return {"p":"saude_mental_mi_pinterest_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_podcast_mental2.get("")
async def i_podcast_mental2():
    return {"p":"saude_mental_mi_podcast_mental2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_priming_mental.get("")
async def i_priming_mental():
    return {"p":"saude_mental_mi_priming_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_public_education_cam.get("")
async def i_public_education_cam():
    return {"p":"saude_mental_mi_public_education_cam","s":"ativo","t":datetime.utcnow().isoformat()}
@router_public_figure_disclo.get("")
async def i_public_figure_disclo():
    return {"p":"saude_mental_mi_public_figure_disclo","s":"ativo","t":datetime.utcnow().isoformat()}
@router_reddit_mental.get("")
async def i_reddit_mental():
    return {"p":"saude_mental_mi_reddit_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_representation_menta.get("")
async def i_representation_menta():
    return {"p":"saude_mental_mi_representation_menta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_responsible_reportin.get("")
async def i_responsible_reportin():
    return {"p":"saude_mental_mi_responsible_reportin","s":"ativo","t":datetime.utcnow().isoformat()}
@router_safe_messaging_guide.get("")
async def i_safe_messaging_guide():
    return {"p":"saude_mental_mi_safe_messaging_guide","s":"ativo","t":datetime.utcnow().isoformat()}
@router_schema_media.get("")
async def i_schema_media():
    return {"p":"saude_mental_mi_schema_media","s":"ativo","t":datetime.utcnow().isoformat()}
@router_sensationalism_menta.get("")
async def i_sensationalism_menta():
    return {"p":"saude_mental_mi_sensationalism_menta","s":"ativo","t":datetime.utcnow().isoformat()}
@router_snapchat_mental.get("")
async def i_snapchat_mental():
    return {"p":"saude_mental_mi_snapchat_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_social_comparison_me.get("")
async def i_social_comparison_me():
    return {"p":"saude_mental_mi_social_comparison_me","s":"ativo","t":datetime.utcnow().isoformat()}
@router_social_comparison_or.get("")
async def i_social_comparison_or():
    return {"p":"saude_mental_mi_social_comparison_or","s":"ativo","t":datetime.utcnow().isoformat()}
@router_social_media_anxiety.get("")
async def i_social_media_anxiety():
    return {"p":"saude_mental_mi_social_media_anxiety","s":"ativo","t":datetime.utcnow().isoformat()}
@router_social_media_depress.get("")
async def i_social_media_depress():
    return {"p":"saude_mental_mi_social_media_depress","s":"ativo","t":datetime.utcnow().isoformat()}
@router_social_media_lonelin.get("")
async def i_social_media_lonelin():
    return {"p":"saude_mental_mi_social_media_lonelin","s":"ativo","t":datetime.utcnow().isoformat()}
@router_stand_up_mental.get("")
async def i_stand_up_mental():
    return {"p":"saude_mental_mi_stand_up_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_stereotypes_media.get("")
async def i_stereotypes_media():
    return {"p":"saude_mental_mi_stereotypes_media","s":"ativo","t":datetime.utcnow().isoformat()}
@router_storytelling_mental.get("")
async def i_storytelling_mental():
    return {"p":"saude_mental_mi_storytelling_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_suicide_reporting2.get("")
async def i_suicide_reporting2():
    return {"p":"saude_mental_mi_suicide_reporting2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_theater_mental2.get("")
async def i_theater_mental2():
    return {"p":"saude_mental_mi_theater_mental2","s":"ativo","t":datetime.utcnow().isoformat()}
@router_tiktok_mental_health.get("")
async def i_tiktok_mental_health():
    return {"p":"saude_mental_mi_tiktok_mental_health","s":"ativo","t":datetime.utcnow().isoformat()}
@router_time_to_change.get("")
async def i_time_to_change():
    return {"p":"saude_mental_mi_time_to_change","s":"ativo","t":datetime.utcnow().isoformat()}
@router_twitch_mental.get("")
async def i_twitch_mental():
    return {"p":"saude_mental_mi_twitch_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_twitter_mental.get("")
async def i_twitter_mental():
    return {"p":"saude_mental_mi_twitter_mental","s":"ativo","t":datetime.utcnow().isoformat()}
@router_upward_social_compar.get("")
async def i_upward_social_compar():
    return {"p":"saude_mental_mi_upward_social_compar","s":"ativo","t":datetime.utcnow().isoformat()}
@router_world_mental_health_.get("")
async def i_world_mental_health_():
    return {"p":"saude_mental_mi_world_mental_health_","s":"ativo","t":datetime.utcnow().isoformat()}
@router_youtube_mental.get("")
async def i_youtube_mental():
    return {"p":"saude_mental_mi_youtube_mental","s":"ativo","t":datetime.utcnow().isoformat()}
class Plugin_saude_mental_midia(PluginBase):
    name = "consolidated_saude_mental_midia"
    def setup(self, app):
        app.include_router(router_FOMO_mental)
        app.include_router(router_JOMO_mental)
        app.include_router(router_Werther_effect2)
        app.include_router(router_ability_comparison)
        app.include_router(router_agenda_setting_menta)
        app.include_router(router_anti_stigma_campaign)
        app.include_router(router_appearance_compariso)
        app.include_router(router_art_mental_health2)
        app.include_router(router_bell_lets_talk)
        app.include_router(router_bibliotherapy2)
        app.include_router(router_blog_mental_health2)
        app.include_router(router_book_mental_health)
        app.include_router(router_celebrity_mental_hea)
        app.include_router(router_cluster_suicide_medi)
        app.include_router(router_comedy_mental)
        app.include_router(router_comics_mental)
        app.include_router(router_contagion_media)
        app.include_router(router_criminalization_ment)
        app.include_router(router_cultivation_theory)
        app.include_router(router_dance_mental)
        app.include_router(router_destigmatization_med)
        app.include_router(router_discord_mental)
        app.include_router(router_documentary_mental)
        app.include_router(router_downward_social_comp)
        app.include_router(router_facebook_mental_heal)
        app.include_router(router_fiction_mental_healt)
        app.include_router(router_film_mental_health)
        app.include_router(router_framing_mental_healt)
        app.include_router(router_gallery_mental)
        app.include_router(router_graphic_novel_mental)
        app.include_router(router_heads_together)
        app.include_router(router_humor_health)
        app.include_router(router_imitation_media)
        app.include_router(router_influencer_mental_he)
        app.include_router(router_instagram_mental_hea)
        app.include_router(router_lateral_social_compa)
        app.include_router(router_laughter_therapy2)
        app.include_router(router_lifestyle_comparison)
        app.include_router(router_linkedin_mental)
        app.include_router(router_media_campaign_menta)
        app.include_router(router_media_effects_mental)
        app.include_router(router_media_intervention)
        app.include_router(router_media_literacy_menta)
        app.include_router(router_memoir_mental)
        app.include_router(router_mental_health_awaren)
        app.include_router(router_mental_health_month)
        app.include_router(router_museum_mental)
        app.include_router(router_music_festival_menta)
        app.include_router(router_music_mental_health)
        app.include_router(router_newsletter_mental)
        app.include_router(router_online_connection)
        app.include_router(router_opera_mental)
        app.include_router(router_opinion_comparison)
        app.include_router(router_papageno_effect2)
        app.include_router(router_parasocial_mental)
        app.include_router(router_pinterest_mental)
        app.include_router(router_podcast_mental2)
        app.include_router(router_priming_mental)
        app.include_router(router_public_education_cam)
        app.include_router(router_public_figure_disclo)
        app.include_router(router_reddit_mental)
        app.include_router(router_representation_menta)
        app.include_router(router_responsible_reportin)
        app.include_router(router_safe_messaging_guide)
        app.include_router(router_schema_media)
        app.include_router(router_sensationalism_menta)
        app.include_router(router_snapchat_mental)
        app.include_router(router_social_comparison_me)
        app.include_router(router_social_comparison_or)
        app.include_router(router_social_media_anxiety)
        app.include_router(router_social_media_depress)
        app.include_router(router_social_media_lonelin)
        app.include_router(router_stand_up_mental)
        app.include_router(router_stereotypes_media)
        app.include_router(router_storytelling_mental)
        app.include_router(router_suicide_reporting2)
        app.include_router(router_theater_mental2)
        app.include_router(router_tiktok_mental_health)
        app.include_router(router_time_to_change)
        app.include_router(router_twitch_mental)
        app.include_router(router_twitter_mental)
        app.include_router(router_upward_social_compar)
        app.include_router(router_world_mental_health_)
        app.include_router(router_youtube_mental)


plugin = Plugin_saude_mental_midia()
