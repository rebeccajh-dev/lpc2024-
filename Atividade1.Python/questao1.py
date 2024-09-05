#1) Dados.
#Faça um programa que simule um lançamento de dados.
#Lance o dado 100 vezes e armazene os resultados em um vetor .
#Depois, mostre quantas vezes cada valor foi conseguido.
#Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios,
#simulando os lançamentos dos dados.

import random

#Vetores
dado = []
lados = [0, 0, 0, 0, 0, 0]

#Laço de repetição para verificar
for cont in range (100):
    num_sort = random.randint(1, 6)
    dado.append(num_sort)
    if num_sort == 1:
        lados[0] += 1
    elif num_sort == 2:
        lados[1] += 1
    elif num_sort == 3:
        lados[2] += 1
    elif num_sort == 4:
        lados[3] += 1
    elif num_sort == 5:
        lados[4] += 1
    elif num_sort == 6:
        lados [5] += 1

       #Quantidade em que cada número foi sorteado
print("Essa é a frequencia que o numero 1 aparece: ", lados[0])
print("Essa é a frequencia que o numero 2 aparece: ", lados[1])
print("Essa é a frequencia que o numero 3 aparece: ", lados[2])
print("Essa é a frequencia que o numero 4 aparece: ", lados[3])
print("Essa é a frequencia que o numero 5 aparece: ", lados[4])
print("Essa é a frequencia que o numero 6 aparece: ", lados[5])