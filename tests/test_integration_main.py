import unittest
import os
from src.utils.executar_lista_dados import processar_arquivo

class TestIntegrationMain(unittest.TestCase):
    
    def setUp(self):
        self.valid_file = "entrada_valida.txt"
        with open(self.valid_file, "w", encoding="utf-8") as f:
            f.write('[{"operation":"buy", "unit-cost":10.00, "quantity":100}]')

        self.invalid_file = "entrada_invalida.txt"
        with open(self.invalid_file, "w", encoding="utf-8") as f:
            f.write('não é json')

    def tearDown(self):
        for f in [self.valid_file, self.invalid_file]:
            if os.path.exists(f):
                os.remove(f)

    def test_processar_arquivo_valido(self):
        try:
            resultado = processar_arquivo("tests/entrada_invalida.txt")
            self.assertFalse(resultado)

        except Exception as e:
            self.fail(f"O teste falhou ao processar um JSON válido: {e}")

    def test_processar_arquivo_invalido(self):
        try:
            resultado = processar_arquivo("tests/entrada_invalida.txt")
            self.assertFalse(resultado)

        except Exception as e:
            self.fail(f"O teste falhou ao processar um JSON invalido: {e}")

    def test_arquivo_inexistente(self):
        with self.assertRaises(FileNotFoundError):
            processar_arquivo("arquivo_nao_existe.txt")

if __name__ == "__main__":
    unittest.main()
