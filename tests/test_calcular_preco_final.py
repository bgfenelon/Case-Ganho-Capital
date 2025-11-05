import pytest
from src.core.entities.produto import Produto
from src.core.use_cases.calcular_preco_final import CalcularPrecoFinal

def test_calculo_preco_final():
    produto = Produto("Camiseta", 100, 0.1)
    use_case = CalcularPrecoFinal()
    assert use_case.executar(produto) == 90
