

lista =[]
quantidade_notas = int(input("Digite a quantidade de notas: "))

for c in range(0, quantidade_notas):
    a = int(input(f'Qual a {c + 1}ª nota: '))
    lista.append(a)
print(lista)

valor_final = sum(lista)
media = valor_final / len(lista)

if media > 7:
    print(f'Sua média foi:{media} e você está: Aprovado!')
else:
    print(f'Sua média foi:{media} e você está: Reprovado!')