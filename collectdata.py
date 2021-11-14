import requests
import json

durakno = input("Station Number: ")

url = f"http://88.255.141.66/mblSrv14/service.asp?FNC=Otobusler&VER=3.1.0&LAN=en&DURAK={durakno}"

headers = {
  'User-Agent': 'EGO Genel Mudurlugu-EGO Cepte-3.1.0',
  'Host': '88.255.141.66'
}

response = requests.request("GET", url, headers=headers)
response = response.text.replace("'", '"')
response = json.loads(response)
print(response)
