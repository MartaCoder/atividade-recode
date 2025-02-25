# Vários arquivos físicos

# EX: home.py, conexao.py, carrinho.py por módulo uma boa prática é de 100 linhas

import operacoes #da uma aplelido: import operacoes as op / ou uma funçao por vez: from opercacoes import somar

resultado_soma = operacoes.somar(10, 5)
print(f"Soma: {resultado_soma}")

resultado_subtracao = operacoes.subtrair(10, 5)
print(f"Subtração: {resultado_subtracao}")

resultado_multiplicacao = operacoes.multiplicar(10, 5)
print(f"Multiplicação: {resultado_multiplicacao}")

resultado_divisao = operacoes.dividir(10, 5)
print(f"Divisão: {resultado_divisao}")