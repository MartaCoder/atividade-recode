# Crie um programa que conte quantas vezes cada palavra aparece em uma frase. 
# Dica: use um dicionário para armazenar a contagem. 
# Entrada: 
# frase = "maçã banana maçã uva banana maçã" 
# Saída esperada: 
# {'maçã': 3, 'banana': 2, 'uva': 1}

frase = "maçã banana maçã uva banana maçã"

palavras = frase.split()  # Divide a frase em uma lista de palavras
contagem_palavras = {}   # Cria um dicionário vazio para armazenar a contagem

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1  # Incrementa a contagem se a palavra já existe
    else:
        contagem_palavras[palavra] = 1   # Adiciona a palavra com contagem 1 se for a primeira vez

print(contagem_palavras)