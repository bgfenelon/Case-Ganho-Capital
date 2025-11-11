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
    
    def test_case_2(self):
        entrada_dados = [{"operation":"buy", "unit-cost":10.00, "quantity": 10000},
        {"operation":"sell", "unit-cost":20.00, "quantity": 5000},
        {"operation":"sell", "unit-cost":5.00, "quantity": 5000}]

        self.calc.processar_operacoes(entrada_dados)

        resultado_esperado = [{"tax": 0.0},{"tax": 10000.0},{"tax": 0.0}]

        self.assertEqual(self.calc.get_lista_imposto(), resultado_esperado)

    def test_case_1_and_2(self):
        entrada_dados = [[{"operation":"buy", "unit-cost":10.00, "quantity": 100},
        {"operation":"sell", "unit-cost":15.00, "quantity": 50},
        {"operation":"sell", "unit-cost":15.00, "quantity": 50}],
        [{"operation":"buy", "unit-cost":10.00, "quantity": 10000},
        {"operation":"sell", "unit-cost":20.00, "quantity": 5000},
        {"operation":"sell", "unit-cost":5.00, "quantity": 5000}]]

        lista_resultado = executando_lista_entrada(entrada_dados)

        resultado_esperado = [[{"tax": 0.0},{"tax": 0.0},{"tax": 0.0}],
        [{"tax": 0.0},{"tax": 10000.0},{"tax": 0.0}]]

        self.assertEqual(lista_resultado, resultado_esperado)

    def test_case_3(self):
        entrada_dados = [{"operation":"buy", "unit-cost":10.00, "quantity": 10000},
        {"operation":"sell", "unit-cost":5.00, "quantity": 5000},
        {"operation":"sell", "unit-cost":20.00, "quantity": 3000}]

        self.calc.processar_operacoes(entrada_dados)

        resultado_esperado = [{"tax": 0.0},{"tax": 0.0},{"tax": 1000.0}]

        self.assertEqual(self.calc.get_lista_imposto(), resultado_esperado)
    
    def test_case_4(self):
        entrada_dados = [{"operation":"buy", "unit-cost":10.00, "quantity": 10000},
        {"operation":"buy", "unit-cost":25.00, "quantity": 5000},
        {"operation":"sell", "unit-cost":15.00, "quantity": 10000}]

        self.calc.processar_operacoes(entrada_dados)

        resultado_esperado = [{"tax": 0.0},{"tax": 0.0},{"tax": 0.0}]

        self.assertEqual(self.calc.get_lista_imposto(), resultado_esperado)
    
    def test_case_5(self):
        entrada_dados = [{"operation":"buy", "unit-cost":10.00, "quantity": 10000},
        {"operation":"buy", "unit-cost":25.00, "quantity": 5000},
        {"operation":"sell", "unit-cost":15.00, "quantity": 10000},
        {"operation":"sell", "unit-cost":25.00, "quantity": 5000}]

        self.calc.processar_operacoes(entrada_dados)

        resultado_esperado = [{"tax": 0.0},{"tax": 0.0},{"tax": 0.0},{"tax": 10000.0}]

        self.assertEqual(self.calc.get_lista_imposto(), resultado_esperado)

    def test_case_6(self):
        entrada_dados = [{"operation":"buy", "unit-cost":10.00, "quantity": 10000},
        {"operation":"sell", "unit-cost":2.00, "quantity": 5000},
        {"operation":"sell", "unit-cost":20.00, "quantity": 2000},
        {"operation":"sell", "unit-cost":20.00, "quantity": 2000},
        {"operation":"sell", "unit-cost":25.00, "quantity": 1000}]

        self.calc.processar_operacoes(entrada_dados)

        resultado_esperado = [{"tax": 0.0},{"tax": 0.0},{"tax": 0.0},{"tax": 0.0},{"tax": 3000.0}]

        self.assertEqual(self.calc.get_lista_imposto(), resultado_esperado)

    def test_case_7(self):
        entrada_dados = [{"operation":"buy", "unit-cost":10.00, "quantity": 10000},
        {"operation":"sell", "unit-cost":2.00, "quantity": 5000},
        {"operation":"sell", "unit-cost":20.00, "quantity": 2000},
        {"operation":"sell", "unit-cost":20.00, "quantity": 2000},
        {"operation":"sell", "unit-cost":25.00, "quantity": 1000},
        {"operation":"buy", "unit-cost":20.00, "quantity": 10000},
        {"operation":"sell", "unit-cost":15.00, "quantity": 5000},
        {"operation":"sell", "unit-cost":30.00, "quantity": 4350},
        {"operation":"sell", "unit-cost":30.00, "quantity": 650}]

        self.calc.processar_operacoes(entrada_dados)

        resultado_esperado = [{"tax": 0.0},{"tax": 0.0},{"tax": 0.0},{"tax": 0.0},{"tax": 3000.0},
        {"tax": 0.0},{"tax": 0.0},{"tax": 3700.0},{"tax": 0.0}]

        self.assertEqual(self.calc.get_lista_imposto(), resultado_esperado)

    def test_case_8(self):
        entrada_dados = [{"operation":"buy", "unit-cost":10.00, "quantity": 10000},
        {"operation":"sell", "unit-cost":50.00, "quantity": 10000},
        {"operation":"buy", "unit-cost":20.00, "quantity": 10000},
        {"operation":"sell", "unit-cost":50.00, "quantity": 10000}]

        self.calc.processar_operacoes(entrada_dados)

        resultado_esperado = [{"tax": 0.0},{"tax": 80000.0},{"tax": 0.0},{"tax": 60000.0}]

        self.assertEqual(self.calc.get_lista_imposto(), resultado_esperado)

    def test_case_9(self):
        entrada_dados = [{"operation": "buy", "unit-cost": 5000.00, "quantity": 10},
        {"operation": "sell", "unit-cost": 4000.00, "quantity": 5},
        {"operation": "buy", "unit-cost": 15000.00, "quantity": 5},
        {"operation": "buy", "unit-cost": 4000.00, "quantity": 2},
        {"operation": "buy", "unit-cost": 23000.00, "quantity": 2},
        {"operation": "sell", "unit-cost": 20000.00, "quantity": 1},
        {"operation": "sell", "unit-cost": 12000.00, "quantity": 10},
        {"operation": "sell", "unit-cost": 15000.00, "quantity": 3}]

        self.calc.processar_operacoes(entrada_dados)

        resultado_esperado = [{"tax": 0.0},{"tax": 0.0},{"tax": 0.0},{"tax": 0.0},{"tax": 0.0},
        {"tax": 0.0},{"tax": 1000.0},{"tax": 2400.0}]

        self.assertEqual(self.calc.get_lista_imposto(), resultado_esperado)

if __name__ == "__main__":
    unittest.main()
