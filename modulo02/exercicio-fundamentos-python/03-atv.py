# Crie um dicionário chamado notas com 3 alunos e suas respectivas notas. 
# Depois, percorra o dicionário e mostre as informações assim: 


aluno = {
    'Ana':8.5,
    'Carlos':7.0,
    'Maria':9.2
}

for chave,valor in aluno.items():
    print(f"{chave}: {valor}")