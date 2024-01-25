def calculadoraNumerica (num1, num2, operacao):
    if(operacao == 1):
        return num1 + num2
    elif(operacao == 2):
        return num1 - num2
    elif(operacao == 3):
        return num1 * num2
    elif(operacao == 4):
        return num1 / num2
    else:
        return 0
    
teste = calculadoraNumerica(5, 5, 1)
print(teste)