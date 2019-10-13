import json
from PIL import Image
import urllib.request
import io
from io import BytesIO
import requests

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
            url = card["imageUrl"]
            with urllib.request.urlopen(url) as url:
                f = io.BytesIO(url.read())
            img = Image.open(f)
            img.show()    
            break

def todas_imagens(carta):
    for card in tac:
        if card["name"] == str(carta):
          url = card["imageUrl"]
          with urllib.request.urlopen(url) as url:
                f = io.BytesIO(url.read())
          img = Image.open(f)
          img.show()    

def todas_edicao(edicao):
    for card in tac:
        if card["set"] == str(edicao):
            print(card["name"])

def radixSort():
    # for card in tac:
    #     print(card["name"])

    # max1 = max(tac("name"))

    # exp = 1
    # while max1/exp > 0: 
    #     countingSort(array,exp) 
    #     exp *= 10

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
print("4.Todas as Imagens da carta")
print("5.Todos os Nomes")
print("6.Cartas da edicao")
print("7.Ordenar as Cartas")

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

if caso == str(5):
    todos_nomes()

if caso == str(4):
    carta = input("Insira a carta:")
    todas_imagens(carta)

if caso == str(6):
    edicao = input("Insira a edicao: ")
    todas_edicao(edicao)

if caso == str(7):
    radixSort()

def countingSort(array, exp1):
    n = len(array)
    output =  [0] * n
    count = [0] * (10) 

    for i in range(0, n): 
        index = (array[i]/exp1) 
        count[ (index)%10 ] += 1
 
    for i in range(1,10): 
        count[i] += count[i-1] 
  
    i = n-1
    while i>=0: 
        index = (array[i]/exp1) 
        output[ count[ (index)%10 ] - 1] = array[i] 
        count[ (index)%10 ] -= 1
        i -= 1

    i = 0
    for i in range(0,len(array)): 
        array[i] = output[i] 