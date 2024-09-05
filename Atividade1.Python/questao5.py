#5) Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto
#e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
#Digite uma letra: A
#-> Você errou pela 1ª vez. Tente de novo!
#Digite uma letra: O
#A palavra é: _ _ _ _ O
#Digite uma letra: E
#A palavra é: _ E _ _ O
#Digite uma letra: S
#-> Você errou pela 2ª vez. Tente de novo!

from random import randint
import sys

#Verifica se o arquivo foi passado como argumento
if len(sys.argv) < 2:
    print("Por favor, forneça o nome do arquivo como argumento.")
    sys.exit(1)

#Lê o arquivo e extrai as palavras
arquivo = sys.argv[1]
jogos = []
with open(arquivo, 'r') as f:
    for linha in f:
        jogos.append(linha.strip())

#Escolhe uma palavra aleatoria da lista
palavra = jogos[randint(0, len(jogos)-1)].upper()
jogo_disfarcado = ["_"] * len(palavra)

#Começo do jogo
novo_jogo = ' '.join(jogo_disfarcado)
print(f"Bem vindo/a ao JOGO DA FORCA! Descubra a palavra:\n\n  {novo_jogo} Você terá 6 tentativas!\n")

#Verificação de tentativas
tentativas = 6
while tentativas > 0:
    letra = input("Digite uma letra: ")
    verify = False

    #Verifica se a letra esta na palavra
    for i, char in enumerate(palavra):
        if letra == char:
            jogo_disfarcado[i] = letra
            verify = True

    novo_jogo = ' '.join(jogo_disfarcado)
    print(f"A palavra é {novo_jogo}.\n")

    if not verify:
        tentativas -= 1
        print(f"Poxa :( restam apenas {tentativas}! por favor, insira uma outra letra!")
    elif "_" not in jogo_disfarcado:
        print("PARABÉNS!! VOCÊ VENCEU")
        break

if "_" in jogo_disfarcado:
    print(f"VOCE PERDEU. A PALAVRA ERA {palavra.capitalize()}")
