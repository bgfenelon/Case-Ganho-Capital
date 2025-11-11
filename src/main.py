import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.domain.win_of_capital import WinOfCapital
from src.utils.executar_lista_dados import executando_lista_entrada

    


if __name__ == "__main__":
    entrada_dados = [{"operation":"buy", "unit-cost":10.00, "quantity": 100},
        {"operation":"sell", "unit-cost":15.00, "quantity": 50},
        {"operation":"sell", "unit-cost":15.00, "quantity": 50}]
    calc = WinOfCapital()
    calc.processar_operacoes(entrada_dados)
    print("calculo do imposto")
    print(calc.get_lista_imposto())
         


