import requests
import json

response = requests.get('https://api.magicthegathering.io/v1/cards')

if response:
    print("Top")
else:
    print("Fail")    


#variable = input('Numero da pagina:') 

tac = []
i = 1
while i < 30:
    busca = requests.get('https://api.magicthegathering.io/v1/cards?page=' + str(i))
    #print(type(busca.content))
    x = busca.text
    y = json.loads(x)
    z = y["cards"]
    for cards in z:
        tac.append(cards)

    print(i)
    i = i + 1

#print(tac)
for card in tac:
    print(card["name"])