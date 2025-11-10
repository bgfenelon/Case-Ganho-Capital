import sys
import os
import numpy as np

# --- Corrige o path para permitir importações como src.domain.win_of_capital ---
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# --- Import da classe ---
from src.domain.win_of_capital import WinOfCapital


# --- Exemplo de estrutura para armazenar preços e ações ---
precos_acoes = {
    "preco_pd": 0.0,
    "acoes": 0.0
}


def calculando_ganho_capital(operacao, valor, quantidade, preco_pd, acao_atual):
    ganho_cp = WinOfCapital(
        operation=operacao,
        unit_cost=valor,
        quantity=quantidade,
        weighted_discount=preco_pd,
        current_actions=acao_atual
    )

    # Cálculo principal (depende da implementação da classe)
    ganho = ganho_cp.calculo_preco_medio_ponderado_compra()

    # Atualiza valores
    precos_acoes["preco_pd"] = ganho_cp.weighted_discount
    precos_acoes["acoes"] = ganho_cp.current_actions

    return ganho


if __name__ == "__main__":
    entrada_dados = [
        {"operation": "buy", "unit_cost": 20.00, "quantity": 10},
        {"operation": "sell", "unit_cost": 10.00, "quantity": 5},
        {"operation": "buy", "unit_cost": 10.00, "quantity": 5},
    ]

    print("Calculando ganho de capital...\n")
    print("Entrada de dados:", entrada_dados)

    resultados = []

    preco_medio_ponderado = 0.0
    quantidade_acoes_atual = 0.0

    lista_preco = []
    lista_quantidade = []

    for db in entrada_dados:
        lista_preco.append(db["unit_cost"])
        lista_quantidade.append(db["quantity"])
        # resultado = calculando_ganho_capital(
        #     db["operation"],
        #     db["unit_cost"],
        #     db["quantity"],
        #     preco_medio_ponderado,
        #     quantidade_acoes_atual
        # )

        # preco_medio_ponderado = precos_acoes["preco_pd"]
        # quantidade_acoes_atual = precos_acoes["acoes"]

        # resultados.append(resultado)

    print("Resultado do cálculo:")
    print(resultados)

    #quantidade preco ponderado - 20
    #quantidade de acao atual - 5
    #nova-media-ponderada = ((quantidade-de-acoes-atual * media-ponderada-atual) 
    # + (quantidade-de-acoes-compradas * valor-de-compra)) 
    # / (quantidade-de-acoes-atual + quantidade-de-acoes-compradas)
    nova_media_ponderada = np.average(lista_preco, weights=lista_quantidade)
    print("nova media ponderada --> ",nova_media_ponderada)
