import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.domain.validar_operacoes import ValidadorOperacoes
from src.domain.ganho_capital_imposto import GanhoCapitalImposto

class TestIntegracaoValidador(unittest.TestCase):

    def setUp(self):
        self.calc = GanhoCapitalImposto()

    # Caso 1 - Integração com dados válidos
    def test_integracao_dados_validos(self):
        entrada_dados = [
            {"operation": "buy", "unit-cost": 10.00, "quantity": 100},
            {"operation": "sell", "unit-cost": 15.00, "quantity": 50},
            {"operation": "sell", "unit-cost": 15.00, "quantity": 50}
        ]

        # Deve passar na validação
        ValidadorOperacoes.validar(entrada_dados)

        # Deve processar sem erro
        self.calc.processar_operacoes(entrada_dados)

        resultado = self.calc.get_lista_imposto()
        self.assertIsInstance(resultado, list)
        self.assertTrue(all("tax" in item for item in resultado))

    # Caso 2 - Faltando campo obrigatório
    def test_integracao_campo_faltando(self):
        entrada_dados = [
            {"operation": "buy", "quantity": 100}  # Falta unit-cost
        ]
        with self.assertRaises(ValueError) as contexto:
            ValidadorOperacoes.validar(entrada_dados)
        self.assertIn("faltando campos obrigatórios", str(contexto.exception))

    # Caso 3 - Operation inválida
    def test_integracao_operacao_invalida(self):
        entrada_dados = [
            {"operation": "hold", "unit-cost": 10.00, "quantity": 100}
        ]
        with self.assertRaises(ValueError) as contexto:
            ValidadorOperacoes.validar(entrada_dados)
        self.assertIn("valor inválido para 'operation'", str(contexto.exception))

    # Caso 4 - Valores negativos
    def test_integracao_valor_negativo(self):
        entrada_dados = [
            {"operation": "buy", "unit-cost": -10.00, "quantity": 100}
        ]
        with self.assertRaises(ValueError) as contexto:
            ValidadorOperacoes.validar(entrada_dados)
        self.assertIn("'unit-cost' deve ser maior que 0", str(contexto.exception))

    # Caso 5 - Tipos incorretos
    def test_integracao_tipo_incorreto(self):
        entrada_dados = [
            {"operation": "buy", "unit-cost": "dez", "quantity": "cem"}
        ]
        with self.assertRaises(TypeError) as contexto:
            ValidadorOperacoes.validar(entrada_dados)
        self.assertIn("'unit-cost' e 'quantity' devem ser números", str(contexto.exception))


if __name__ == "__main__":
    unittest.main()
