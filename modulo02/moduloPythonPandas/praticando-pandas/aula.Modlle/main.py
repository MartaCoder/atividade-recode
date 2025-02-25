import csv
import random
import datetime

def gerar_data_aleatoria(inicio, fim):
    """Gera uma data aleatória entre duas datas."""
    tempo_inicio = datetime.datetime.strptime(inicio, '%Y-%m-%d')
    tempo_fim = datetime.datetime.strptime(fim, '%Y-%m-%d')
    tempo_aleatorio = tempo_inicio + datetime.timedelta(
        seconds=random.randint(0, int((tempo_fim - tempo_inicio).total_seconds())),
    )
    return tempo_aleatorio.strftime('%Y-%m-%d')

def gerar_nome_aleatorio():
    """Gera um nome aleatório."""
    nomes = ['João', 'Maria', 'Pedro', 'Ana', 'Lucas', 'Sofia', 'Mateus', 'Isabela', 'Gabriel', 'Laura']
    sobrenomes = ['Silva', 'Santos', 'Oliveira', 'Pereira', 'Rodrigues', 'Gomes', 'Costa', 'Ribeiro', 'Carvalho', 'Almeida']
    return f"{random.choice(nomes)} {random.choice(sobrenomes)}"

def gerar_animal_aleatorio():
    """Gera um tipo de animal aleatório."""
    animais = ['cachorro', 'gato', 'peixe', 'pássaro', 'roedor']
    return random.choice(animais)

def gerar_produto_aleatorio():
    """Gera um produto aleatório."""
    produtos = ['ração', 'brinquedo', 'remédio', 'acessório', 'higiene']
    return random.choice(produtos)

def gerar_valor_aleatorio():
    """Gera um valor aleatório entre 10 e 500."""
    return round(random.uniform(10, 500), 2)

def gerar_pagamento_aleatorio():
    """Gera uma forma de pagamento aleatória."""
    pagamentos = ['dinheiro', 'cartão', 'pix']
    return random.choice(pagamentos)

def criar_arquivo_csv(nome_arquivo, num_linhas):
    """Cria um arquivo CSV com dados aleatórios."""
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow(['ID_Venda', 'Data_Venda', 'Cliente', 'Animal', 'Produto', 'Valor', 'Pagamento', 'Vendedor'])  # Cabeçalho

        for i in range(1, num_linhas + 1):
            id_venda = i
            data_venda = gerar_data_aleatoria('2023-01-01', '2023-12-31')
            cliente = gerar_nome_aleatorio()
            animal = gerar_animal_aleatorio()
            produto = gerar_produto_aleatorio()
            valor = gerar_valor_aleatorio()
            pagamento = gerar_pagamento_aleatorio()
            vendedor = gerar_nome_aleatorio()
            escritor_csv.writerow([id_venda, data_venda, cliente, animal, produto, valor, pagamento, vendedor])

# Criar o arquivo CSV com 200 linhas
criar_arquivo_csv('vendas_animais.csv', 200)
print("Arquivo 'vendas_animais.csv' criado com sucesso!")