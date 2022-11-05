"""This program translates words"""
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('Vt5Gg2hdifLyh9ABdld1C-I8XRO4A-pMn9JR4JNMg5c6')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/18fc298c-9c70-478d-b6fd-ef11200609e8')

def english_to_french(english_text):
    '''Translates Eng to Fr'''
    #write the code here
    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    return translation.get("translations")[0].get("translation")

def french_to_english(french_text):
    """Translates Fr to Eng"""
    #write the code here
    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    return translation.get("translations")[0].get("translation")
    