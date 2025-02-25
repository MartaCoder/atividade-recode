with open("03-aulaPython/manipulacao-de-arquivos/arquivo.txt", 'a') as arquivo:
    arquivo.write('Linha de conteudo\n')
    
with open("03-aulaPython/manipulacao-de-arquivos/arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)