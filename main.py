import json
from PIL import Image
import urllib.request
import io
from io import BytesIO
import requests
import random
import time
import matplotlib.pyplot as plt
i = 1
contador = 0
tempo_corrido = 0

def read_cards():
    with open('cartas.txt', 'r') as json_file:
        return list(json.load(json_file))

def read_cardsMenor():
    with open('cartas2.txt', 'r') as json_file:
        return list(json.load(json_file))        

def ler_tempo():
    with open('tempo.txt', 'r') as json_file:
        return list(json.load(json_file))

def ler_quantidade():
    with open('quantidade.txt', 'r') as json_file:
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

def todos_id():
    for card in tac:
        print(card["multiverseid"])          

def countingSort(array, exp1):
    n = len(array)
    output =  [0] * n
    count = [0] * (10) 

    for i in range(0, n): 
        temp = array[i]
        

        index = (temp["multiverseid"]//exp1) 
        count[ (index)%10 ] += 1
 
    for i in range(1,10): 
        count[i] += count[i-1] 
  
    i = n-1
    while i>=0: 
        temp = array[i]
        index = (temp["multiverseid"]//exp1) 
        output[ count[ (index)%10 ] - 1] = array[i] 
        count[ (index)%10 ] -= 1
        i -= 1

    i = 0
    for i in range(0,len(array)): 
        array[i] = output[i] 
        
def radixSort():
    maior = 0
    start_time = time.time()
    global contador
    global tempo_corrido
    
    for card in tac:
        if card.get("multiverseid") == None:
            card["multiverseid"] = 0
        if card.get("multiverseid") > maior:
            maior = card.get("multiverseid")
        contador =  contador + 1    
    print( contador)
    
    #print(maior)
    exp = 1
    cont = 0
    while maior/exp > 0: 
        cont = cont + 1
        countingSort(tac,exp) 
        exp *= 10
    todos_id()
    tempo_corrido =  time.time() - start_time   
    print("segundos: ", tempo_corrido)

def radixSortMenor():
    maior = 0
    start_time = time.time()
    global contador
    global tempo_corrido

    tac = read_cardsMenor()

    for card in tac:
        if card.get("multiverseid") == None:
            card["multiverseid"] = 0
        if card.get("multiverseid") > maior:
            maior = card.get("multiverseid")
        contador =  contador + 1    
    print( contador)
    
    #print(maior)
    exp = 1
    cont = 0
    while maior/exp > 0: 
        cont = cont + 1
        countingSort(tac,exp) 
        exp *= 10
    tempo_corrido =  time.time() - start_time   
    print("segundos: ", tempo_corrido)
    #todos_id()
    #print(cont)    
         

# response = requests.get('https://api.magicthegathering.io/v1/cards')
# if response:
#     print("Top")
# else:
#     print("Fail")    

tac = read_cards()
tempo = ler_tempo()
quantidade = ler_quantidade()

random.shuffle(tac)
if tac == []:    

    while i <= 200:
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
print("8.Ordenar Pagina com quantidade diferente")
print("9.Plotar tempo")

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
    tempo.append(tempo_corrido)
    with open('tempo.txt', 'w')as outfile:
        json.dump(tempo, outfile)
    quantidade.append(contador)
    with open('quantidade.txt', 'w')as outfile:
        json.dump(quantidade, outfile)


if caso == str(8):
    radixSortMenor()    
    tempo.append(tempo_corrido)
    with open('tempo.txt', 'w')as outfile:
        json.dump(tempo, outfile)
    quantidade.append(contador)
    with open('quantidade.txt', 'w')as outfile:
        json.dump(quantidade, outfile)
    
if caso == str(9):
    plt.plot(tempo, quantidade, 'ro')
    plt.axis([0, 60, 0, 50000]) 
    plt.show()