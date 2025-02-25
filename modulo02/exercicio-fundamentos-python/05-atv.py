# Crie um dicionário chamado estoque que armazene informações de produtos. 
# Cada produto deve ser uma chave, e o valor deve ser outro dicionário com quantidade 
# e preço. 
# Saída esperada: 
# { 
#     "Camisa": {"quantidade": 10, "preço": 50}, 
#     "Calça": {"quantidade": 5, "preço": 120}, 
#     "Tênis": {"quantidade": 8, "preço": 200} 
# } 
 
# Agora, peça ao usuário o nome de um produto e mostre suas informações.

estoque = {
    "Camisa": {"quantidade": 10, "preço": 50},
    "Calça": {"quantidade": 5, "preço": 120},
    "Tênis": {"quantidade": 8, "preço": 200}
}

print(estoque)

produto_desejado = input("Digite o nome do produto que deseja ver as informações: ")

if produto_desejado in estoque:
    print(f"Informações do produto '{produto_desejado}':")
    print(f"  Quantidade: {estoque[produto_desejado]['quantidade']}")
    print(f"  Preço: R$ {estoque[produto_desejado]['preço']:.2f}") # Formata o preço para duas casas decimais
else:
    print(f"Produto '{produto_desejado}' não encontrado no estoque.")