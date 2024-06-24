#Exercícios

#Inteiros (int)

#Escreva um programa que soma dois números inteiros inseridos pelo usuário.

   ## a = int(input("Digite um número: "))
   ## b = int(input("Digite um número: "))
   ## soma = a + b
   ## print(f'O primeiro número digitado foi: {a} e o segundo foi {b}. A soma é igual a: {soma}')

#Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

   ##c = int(input("Digite um número: "))
   ##resto = c % 5
   ##print(f'Você digitou o número {c} e o resto da divisão dele por 5 é: {resto}')

#Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

   ## num1 = int(input("Digite um número: "))
   ## num2 = int(input("Digite um número: "))
   ## multi = num1 * num2
   ## print(f'O primeiro número digitado foi: {num1} e o segundo foi {num2}. A soma é igual a: {multi}')

#Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
    # num1 = int(input("Digite um número: "))
    # num2 = int(input("Digite um número: "))
    # divi  = num1 / num2
    # print(f'O primeiro número digitado foi: {num1} e o segundo foi {num2}. A divisão é igual a: {divi}')


#Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

   # num3 = int(input("Digite um número:"))
   # quadrado = num3 ** 2
   # print(quadrado)

#Números de Ponto Flutuante (float)

#Escreva um programa que receba dois números flutuantes e realize sua adição.
    # num1 = float(input("Digite um número: "))
    # num2 = float(input("Digite um número: "))
    # soma = num1 + num2
    # print(f'O primeiro número digitado foi: {num1} e o segundo foi: {num2}. A soma dos dois é: {soma:.1f}')


#Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
    # num1 = float(input("Digite um número: "))
    # num2 = float(input("Digite um número: "))
    # media = (num1 + num2) / 2
    # print(f'O primeiro número digitado foi: {num1} e o segundo foi: {num2}. A média dos dois é: {media:.1f}')

#Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
    # from math import pow
    # num = float(input("Digite um número: "))
    # potencia =  float(input("Digite a potência: "))
    # x = pow(num, potencia)
    # print(x)

#Faça um programa que converta a temperatura de Celsius para Fahrenheit.
    # num1 = float(input("Digite sua temperatura em Celsius: "))
    # fahrenheit = (num1 * 1.8) + 32
    # print(f'Você informou que você está com {num1}° Celsius. A sua temperatura em Fahrenheit é: {fahrenheit:.2f} °F')

#Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
    # from math import pi
    # num1 = float(input("Digite o raio do círculo: "))
    # diametro = pi * num1 ** 2
    # print(f'Você digitou o raio de : {num1} e o diâmetro é : {diametro:.2f}')


# Strings (str)

#Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
    # texto = input("Digite seu nome: ")
    # print(texto.upper())

#Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
    # texto = input("Digite seu nome: ")
    # print(texto.lower())

#Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
    # texto = input("Digite um texto: ")
    # print(texto.strip())

#Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
    # texto = input("Digite uma data dd/mm/aaaa: ")
    # lista = texto.split("/")
    # print(lista[0])
    # print(lista[1])
    # print(lista[2])

#Escreva um programa que concatene duas strings fornecidas pelo usuário.
texto1 = input("Digite um texto: ")
texto2 = input("Digite outro texto: ")
concatenado = texto1 + texto2 
print(concatenado)
#Booleanos (bool)

#Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
#Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
#Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
#Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
#Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.