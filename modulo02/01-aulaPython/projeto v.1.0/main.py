
n1 = 0
pets = []
while n1 != 3:
    print("Pet shop")
    print("1 - Cadastrar Pet")
    print("2 - Listar Pets")
    print("3 - Sair")
    n1 = int(input("Escolha uma opcao: "))
    print("")
    print("")

    if n1 == 1:
        nome = input('Nome do pet: ')
        especie = input('Espécie (Cachorro, Gato, etc.): ')
        idade_pet = int(input("Idade do Pet: "))
        saude = input("Pet saudavel (s/n): ")
        print("")
        print("Pet " + nome + " cadastrado com sucesso")
        print("")

    
        pet = {
        'Nome': nome,
        'Especie': especie,
        'Idade': idade_pet,
        "Saudavel": saude 
        }
        pets.append(pet)

    elif n1 == 2: 
        print("Lista de Pets Cadastrados:")
        for pet in pets:
            print(f"Nome: {pet['Nome']}, Espécie: {pet['Especie']}, Idade: {pet['Idade']}, Saudável: {pet['Saudavel']}")

    elif n1 == 3:
        print("Saindo...")
print("Fim")
