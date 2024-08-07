# Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
# O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, 
# garantir que a entrada seja numérica, tratando qualquer ValueError. 
# Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

    # try:
    #     tempcelsius = int(input("Digite a temperatura em º Celsius:"))
    #     fahrenheit = (tempcelsius * 1.8) + 32
    #     print(f'A temperatura é Fahrenheit é : {fahrenheit}')

    # except ValueError:
    #     print("Você digitou um valor errado")

# Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo 
# (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
# Utilize try-except para garantir que a entrada seja uma string. 
# Dica: Utilize a função isinstance() para verificar o tipo da entrada.

    # try:
    #     a = input("Digite um Palíndromo: ")

    #     if isinstance(a, str):
    #         if a == a[::-1]:
    #             print(f'A palavra {a} é um palíndromo')
    #         else:
    #             print(f'A palavra {a} não é um palíndromo')
    #     else:
    #         print(f'{a} não é uma string')

    # except TypeError:
    #     print("erro") 


# Exercício 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e 
# um operador (+, -, *, /) do usuário. 
# Use try-except para lidar com divisões por zero e entradas não numéricas. 
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
# Imprima o resultado ou uma mensagem de erro apropriada.

    # try:
    #     num1 = float(input("Digite o primeiro número: "))
    #     num2 = float(input("Digite o segundo número: "))
    #     operacao = input("Escolha uma operação: Adi /  Multi / Sub / Div: ")

    #     if operacao.lower() == "adi":
    #         resultado = num1 + num2
    #     elif operacao.lower() == "multi":
    #         resultado = num1 * num2
    #     elif operacao.lower() == "sub":
    #         resultado = num1 - num2   
    #     elif operacao.lower() == "div":
    #         resultado = num1 / num2
    #     else: print("Você digitou uma operação errada.")
    #     print(resultado)
    # except ValueError:
    #     print("Você digitou um caracter inválido")

    # except ZeroDivisionError:
    #     print("Não é possível dividir um número por zero")  


# Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número.
#  Utilize try-except para assegurar que a entrada seja numérica e 
# utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". 
# Adicionalmente, identifique se o número é "par" ou "ímpar".

    # try:
    #     num = float(input("Digite um número qualquer: "))
    #     resultado = ""
    #     tipo = ""
    #     if num > 0:
    #         resultado = "Positivo"
    #     elif num < 0:
    #         resultado = "Negativo"
    #     else: 
    #         resultado = "Zero"
    #     if num % 2 == 0:
    #         tipo = "Par"
    #     else: 
    #         tipo = "Ímpar"
    
    #     print(f'O número que você digitou foi: {num} e ele é: {resultado} e {tipo}')

    # except ValueError:
    #     print("Você não digitou um número.")

# Exercício 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
# O programa deve converter a string de entrada em uma lista de números inteiros. 
# Utilize try-except para tratar a conversão de cada número e validar que cada 
# elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, 
# imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.


    # try:
    #     entrada = input("Digite vários números separados por vírgula:")
    #     lista = list(entrada.split(","))
    #     lista2 =[]
    #     for a in lista:
    #         a = int(a)
    #         lista2.append(a)
    #     for b in lista2:
    #         if isinstance(b, int):
    #             print("ok")
    #         else:
    #             print("Error")
    #     print(lista2)
    # except ValueError:
    #     print("Você digitou um valor errado")


