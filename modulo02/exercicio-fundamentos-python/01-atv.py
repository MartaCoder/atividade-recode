# Exercício 1 – Criando um Dicionário 
# Crie um dicionário chamado aluno que armazene: 
# • Nome 
# • Idade 
# • Curso 
# Depois, exiba todas as informações do aluno.

aluno = {
    'nome': 'Ana',
    'idade': 22,
    'curso': 'ADS'
}

for chave, valor in aluno.items():
    print(f'{chave}: {valor}')