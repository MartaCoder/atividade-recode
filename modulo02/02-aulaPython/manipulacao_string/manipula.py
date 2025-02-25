texto = "PytHon"
print(texto.upper())
print(texto.lower())


nome = "       Maria "
print(nome.strip())

frase = "Eu gosto de Java"
nova_frase = frase.replace("Java", "Python")
print(nova_frase)

nomes = "Julio, Flavio, Ana"

listar_nomes = nomes.split(", ")

print(listar_nomes)


unidos = '-'.join(listar_nomes)
print(unidos)