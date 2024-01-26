def calculadora():
    menuOpcoes = ('''Para prosseguir, é preciso escolher uma das seguintes opções:
          1. Soma
          2. Subtração
          3. Multiplicação
          4. Divisão 
          0. Sair''')
    print(menuOpcoes)
    opcaoEscolhida = int(input('Digite a opção desejada: '))

    if((opcaoEscolhida != 1) and (opcaoEscolhida != 2) and (opcaoEscolhida != 3) and (opcaoEscolhida != 4) and (opcaoEscolhida != 0)):
        print('Esta opção não existe')
        print(menuOpcoes)
        opcaoEscolhida = int(input('Digite a opção desejada: '))

    if(opcaoEscolhida == 0):
        print("Programa finalizado")
    else:
        num1Escolhido = int(input('Digite o primeiro valor da operação: '))
        num2Escolhido = int(input('Digite o segundo valor da operação: '))

        if(opcaoEscolhida == 1):
            soma = num1Escolhido + num2Escolhido
            print('Resultado:', soma)
            return calculadora()
        elif(opcaoEscolhida == 2):
            subtracao = num1Escolhido - num2Escolhido
            print('Resultado:', subtracao)
            return calculadora()
        elif(opcaoEscolhida == 3):
            multiplicacao = num1Escolhido * num2Escolhido
            print('Resultado:', multiplicacao)
            return calculadora()
        elif(opcaoEscolhida == 4):
            divisao = num1Escolhido / num2Escolhido
            print('Resultado:', divisao)
            return calculadora()
        
calculadora()