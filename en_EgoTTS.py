import requests
import json
from playsound import playsound
from gtts import gTTS
import os
from translate import Translator
translator = Translator(to_lang="en")
durakno = input("Station Number: ")

url = f"http://88.255.141.66/mblSrv14/service.asp?FNC=Otobusler&VER=3.1.0&LAN=en&DURAK={durakno}"

headers = {
  'User-Agent': 'EGO Genel Mudurlugu-EGO Cepte-3.1.0',
  'Host': '88.255.141.66'
}

def talk(text):
    tts = gTTS(text=text, lang="en")
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

response = requests.request("GET", url, headers=headers)
response = response.text.replace("'", '"')
response = json.loads(response)
if response['data'][0]['status'] == "TRUE":
    for item in response['data'][0]['table']:
        if not item['arac_no'] == "-":
            talk(", Number: " + translator.translate(str(item['hat_kod'])) + ", Duration: " + translator.translate(str(item['sure'])))
else:
    print(response['data'][0]['status'])