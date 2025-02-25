'''
Desafio: Sistema de Venda de Ingressos em Python
Desenvolva um sistema orientado a objetos em Python para simular a venda de ingressos de um evento. 
O sistema deverá permitir a compra de ingressos de dois tipos: Normal e VIP, e calcular o total acumulado de vendas no dia.

Requisitos do Sistema:
Classe Ingresso:
Deve armazenar o tipo do ingresso e seu valor.
Os valores dos ingressos são fixos:
Ingresso Normal: R$ 50,00
Ingresso VIP: R$ 100,00

Classe VendaIngressos:
Deve conter um método vender_ingresso(tipo, quantidade) que receba os seguintes parâmetros:
tipo: Tipo do ingresso ("normal" ou "vip").
quantidade: Quantidade de ingressos a serem comprados.
Esse método deve calcular o valor total da compra e registrar a venda.

Controle de Vendas:
O sistema deve manter um registro acumulado das vendas do dia.
Criar um método exibir_total_vendas() que exiba o total de ingressos vendidos e o valor total arrecadado.
Exemplo de saída esperada:
yamlCopiarEditar

'''

class Ingresso:
    def __init__(self):
        self.total_vendas = 0
        self.total_ingresso = 0
    def venda_ing(self, tipo, quantidade):
        if tipo == 'normal':
            self.total_vendas += (quantidade * 50)
            self.total_ingresso += quantidade

        elif tipo == 'vip':
            self.total_vendas += (quantidade * 100)
            self.total_ingresso += quantidade
            
    def info(self):
        print(f"Total de venda: {self.total_vendas}")
        print(f"Total de ingresso: {self.total_ingresso}")
    

sistema = Ingresso()

sistema.venda_ing('normal', 1)


sistema.info()



# class Vendas:
#     def __init__(self):
#         self.totalVendas = 0
#         self.totalVip = 0
#         self.totalNormal = 0
    
#     def vender(self, qtd, tipo ):
#         if tipo == "n":
#             self.totalVendas += (qtd * 50)
#             self.totalNormal += qtd
#         elif tipo=="v":
#             self.totalVendas += (qtd * 100)
#             self.totalVip += qtd

#     def informacoes(self):
#         print(f"Total em vendas R$ {self.totalVendas}")
#         print(f"Total de ingresso vendidos NORMAIS {self.totalNormal}")
#         print(f"Total de ingresso vendidos VIPS {self.totalVip}")


# print(" ----------- Dados do sistema 1 -----------")
# sistema1 = Vendas()
# sistema1.vender(10,"n")
# sistema1.vender(5,"v")
# sistema1.informacoes()

# print(" ---------- Dados do sistema 2 ---------------- ")

# sistema2 = Vendas()
# sistema2.vender(100,"v")
# sistema2.informacoes()
 