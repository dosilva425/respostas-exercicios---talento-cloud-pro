execucao = True

while(execucao == True):
    try:
        print('Informe seu nome completo:')
        nome = input()

        print('Informe seu ano de nascimento (só funciona para anos entre 1922 e 2021)')
        anoNascimento = int(input())

        if(anoNascimento < 1922 or anoNascimento > 2021):
            print('O ano do nascimento precisa estar entre 1922 e 2021')
        else:
            idade = 2022 - anoNascimento
            print(f'{nome} completará {idade} anos em 2022.')
            execucao = False
    except:
        print('Erro: Você precisa informar um número para o ano do nascimento')