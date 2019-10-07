import requests
import json
from PIL import Image
import urllib.request as urllib
import io
from io import BytesIO

def read_cards():
    with open('cartas.txt', 'r') as json_file:
        return list(json.load(json_file))


def find_rule(carta):
    for card in tac:
      if card["name"] == str(carta):
         print(card["text"])
         break        

def find_cmc(carta):
    for card in tac:
      if card["name"] == str(carta):
         print(card["manaCost"])
         break        

def find_type(carta):
    for card in tac:
      if card["name"] == str(carta):
         print(card["type"])
         break       

def todos_nomes():
    for card in tac:
        print(card["name"])

def acha_cartas(palavra):
    nomes = []
    for card in tac:
            nomes.append(card["name"])
            nome = [i for i in nomes if palavra in i]
    print(nome)

def Imagem(carta):
    for card in tac:
        if card["name"] == str(carta):
            response = requests.get(card["imageUrl"])
            img = Image.open(BytesIO(response.content))
            break

# response = requests.get('https://api.magicthegathering.io/v1/cards')
# if response:
#     print("Top")
# else:
#     print("Fail")    
tac = []
i = 1
tac = read_cards()
 
if tac == []:    

    while i <= 476:
        busca = requests.get('https://api.magicthegathering.io/v1/cards?page=' + str(i))
        #print(type(busca.content))
        x = busca.text
        y = json.loads(x)
        z = y["cards"]
        for cards in z:
            tac.append(cards)

        print(i)
        i = i + 1

    for card in tac:
        print(card["name"])

    print(len(tac))


    with open('cartas.txt', 'w')as outfile:
        json.dump(tac, outfile)


print("--------menu----------")
print("1.Achar carta")
print("2.Regras da carta")
print("3.Imagem da carta")
print("4.Todos os Nomes")

caso = input("Selecione modo:")

if caso == str(2):
    carta = input("insira a carta: ")
    find_cmc(carta)
    find_type(carta)    
    find_rule(carta)

if caso == str(1):
    palavra = input("Palavra para achar: ")
    acha_cartas(palavra)

if caso == str(3):
    carta = input("insira a carta: ")
    Imagem(carta)

if caso == str(4):
    todos_nomes()


