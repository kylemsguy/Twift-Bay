import requests

from watson_developer_cloud import PersonalityInsightsV2

from env_vars import get_env_var

SERVICE_USER = get_env_var('BLUEMIX_SERVICE_USER')
SERVICE_PASS = get_env_var('BLUEMIX_SERVICE_PASS')

def analyse_text(text):
    personality_insights = PersonalityInsightsV2(
        username=SERVICE_USER,
        password=SERVICE_PASS,
    )
    return personality_insights.profile(text)

