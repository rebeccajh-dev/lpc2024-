#2) Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda
#ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados.
#A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia
#uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

variavel = input("Por favor, insira uma palavra ou uma frase: ")

#removendo espaço
s_espaco = variavel.replace(" ","").lower()

# validação
palindromo = True

for i in range(len(s_espaco)):
    if s_espaco[i] != s_espaco[(len(s_espaco)-1) - i]:
        palindromo = False
        break

if palindromo:
    print(f"{variavel} é um palíndromo.")
else:
    print(f"{variavel} não é um palíndromo.")