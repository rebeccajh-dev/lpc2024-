#3) Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e
#indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação.

cpf = str(input("Digite o CPF: "))

#Verificando o tamanho do CPF.
if len(cpf) != 14:
    print("FORMATO INVALIDO! POR FAVOR INSIRA NOVAMENTE")
elif (cpf[3] != ".") or (cpf[7] != ".") or (cpf[11] != "-"):
    print("FORMATO INVALIDO! POR FAVOR INSIRA NOVAMENTE.")
else:
    digitos = cpf[0:3] + cpf[4:7] + cpf[8:11] + cpf[12:14]
    print(digitos)

    #Fazendo a validação do CPF.
    if not digitos.isnumeric():
        print("CPF INVALIDO!")
    else:
        DV1 = 0
        multi = 1
        for i in range(9):
            DV1 = DV1 + int(digitos[i])*multi
            multi += 1
        DV1 = DV1 % 11
        if DV1 != int(cpf[12]):
            DV1 = 0
            print("CPF INVALIDO!")
        else:
            DV2 = 0
            multi = 0
            for i in range (10):
                DV2 = DV2 + int(digitos[i]) * multi
                multi += 1
            DV2 = DV2 % 11
            if DV2 != int(cpf[13]):
                DV2 = 0
                print("CPF INVALIDO.!")
            else:
                print("CPF VALIDADO!")
