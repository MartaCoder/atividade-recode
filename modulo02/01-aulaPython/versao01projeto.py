pets = {}
 
while True:
    print("PET SHOP MANAGER")
    print("1 - CADASTRAR PET")
    print("2 - LISTAR PETS")
    print("3 - SAIR DO SISTEMA")
 
    opcao = input("Escolha uma opção: ")
 
    if opcao == "1":
 
        nome = input("Nome do pet: ")
        especie = input("Espécie (cachorro, gato, etc.): ")
        idade = input("Idade do pet: ")
 
        pets[nome] = {"Espécie": especie, "Idade": idade}
        print(f"Pet '{nome}' cadastrado com sucesso!")
 
    elif opcao == "2":
 
        if not pets:
            print("Nenhum pet cadastrado ainda.")
        else:
            print("\nLista de Pets Cadastrados:")
            for nome, info in pets.items():
                print(f"- Nome: {nome}, Espécie: {info['Espécie']}, Idade: {info['Idade']} anos")
 
    elif opcao == "3":
        print("Saindo do sistema... Até logo!")
        break
 
    else:
        print("Opção inválida! Escolha uma opção válida.")