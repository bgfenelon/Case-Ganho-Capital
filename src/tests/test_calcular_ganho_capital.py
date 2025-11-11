import unittest
import sys
import os

# Corrige o caminho para permitir importações de src.domain e src.utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.domain.win_of_capital import WinOfCapital
from src.utils.executar_lista_dados import executando_lista_entrada


class TestCalcularGanhoCapital(unittest.TestCase):

    def setUp(self):
        self.calc = WinOfCapital()

    def test_case_1(self):
        entrada_dados = [{"operation":"buy", "unit-cost":10.00, "quantity": 100},
{"operation":"sell", "unit-cost":15.00, "quantity": 50},
{"operation":"sell", "unit-cost":15.00, "quantity": 50}]

        self.calc.processar_operacoes(entrada_dados)

        resultado_esperado = [{"tax": 0.0},{"tax": 0.0},{"tax": 0.0}]

        self.assertEqual(self.calc.get_lista_imposto(), resultado_esperado)


if __name__ == "__main__":
    unittest.main()
