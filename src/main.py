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
    entrada_dados = [{"operation":"buy", "unit_cost":10.00, "quantity": 100},
{"operation":"sell", "unit_cost":15.00, "quantity": 50},
{"operation":"sell", "unit_cost":15.00, "quantity": 50}]

    print("Calculando ganho de capital...\n")
    print("Entrada de dados:", entrada_dados)

    resultados = []

    preco_medio_ponderado = 0.0
    quantidade_acoes_atual = 0.0

    lista_preco = []
    lista_quantidade = []

    imposto_a_pagar = 0.0
    lista_imposto = []
    lucro_total = 0.0
    prejuizo_total = 0.0

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

    for db in entrada_dados:
        if (db['operation'] == "buy"):
            custo_total +=  db["unit_cost"] * db["quantity"]
            imposto_a_pagar = 0.0
        
        #quando for venda
        if (db['operation'] == "sell" ):

            if db["quantity"] == 0:
                raise ValueError("Sem ações em estoque para vender.")

            resultado = (db["unit_cost"] - nova_media_ponderada) * db["quantity"]
            print("resultado --> ",resultado)
            
            if (db["unit_cost"] <= nova_media_ponderada):
                prejuizo_total += abs(resultado)
                imposto_a_pagar = 0.0
            else:
                lucro_total += resultado
                imposto_a_pagar = db["unit_cost"] * (20 / 100)
                
        else:
            # aqui segue o jogo
            imposto_a_pagar = 0.0

        lista_imposto.append(imposto_a_pagar)

    print("calculo do imposto")
    print(lista_imposto)
         


