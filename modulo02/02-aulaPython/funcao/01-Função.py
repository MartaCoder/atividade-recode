#Função com Paremetros e sem parametros

def somar():
    x = 50 + 60
    print(x)
somar()


def somar(x,y):
    z = x + y
    print(f"A soma é {z}")

somar(10,20)


def nome_e_sobrenome(nome, sobrenome):
    print(f"Meu nome completo: {nome} {sobrenome}")

nome_e_sobrenome("Julio", "Lima")


#Função com return

def somar(p1, p2):
    x = p1+p2
    return x

somar(10,5)


#Função retorno multiplo (não é tao usual)

def calcular_dobro_e_triplo(numero):
    return numero * 2, numero * 3

dobro, triplo = calcular_dobro_e_triplo(3)
print(f"Dobre: {dobro}, Triplo:{triplo}")



# # Criar uma função que receba como parâmetro nome e sobrenome e com a função join retorne o nome completo

# def nome_sobrenome(nome, sobrenome):
#     return " ".join([nome, sobrenome])

# print(nome_sobrenome('Júlio', 'Lima'))
