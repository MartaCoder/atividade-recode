'''
1.	Escreva um programa que peça dois números ao usuário e exiba qual é o maior.
2.	Faça um programa que pergunte a idade do usuário e informe se ele pode dirigir (maior de 18 anos).
3.	Crie um programa que peça um número e informe se ele é par ou ímpar.
'''

n1 = input("Digite o primeiro numero: ")
n2 = input("Digite o suegundo numero: ")

if n1 > n2:
    print(n1)
else :
    print(n2)


idade = int(input("Digite sua idade: "))

if idade > 18:
    print("Pode dirigir")
else:
    print("Nao pode dirigir")

num = int(input("Digite um numero: "))

if num % 2 == 0:
    print("Par")
else:
    print("Impar")