#4) Número por extenso. Escreva um programa que solicite ao
#usuário a digitação de um número até 99 e imprima-o na tela por extenso.

#Números escritos por extenso.
unidades = [
    "zero", "um", "dois", "tres", "quatro", "cinco",
    "seis", "sete", "oito", "nove"
]

coringas = [
    "dez", "onze", "doze", "treze", "quatorze", "quinze",
    "dezesseis", "dezessete", "dezoito", "dezenove"
]

dezenas = [
    "vinte", "trinta", "quarenta", "ciquenta",
    "sessenta", "setenta", "oitenta", "noventa"
]

numero = int(input("Insira um número de 0 até 99: "))

#Verificação do número inserido para realizar a saída por extenso.
if numero > 99 or numero < 0:
    print("Entrada inválida.")
elif numero // 10 < 1:
    print(f"O número por extenso é: {unidades[numero].capitalize()}")
elif numero // 10 == 1:
    ulti_dig = numero - 10 #pegando o índice
    print(f"O número por extenso é: {coringas[ulti_dig].capitalize()}")
else:
    primeiro_dig = (numero // 10) - 2
    ulti_dig = numero % 10

    if ulti_dig == 0:
        print(f"O numero por extenso é: {dezenas[primeiro_dig].capitalize()}")
    else:
        print(f"O numero por extenso é: {dezenas[primeiro_dig].capitalize()} e {unidades[ulti_dig]}")