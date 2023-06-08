import requests


url = "https://www.ouedkniss.com/appartement-vente-f4-chlef-tenes-algerie-d35916540"
resp = requests.get(url)

print(resp.text)
