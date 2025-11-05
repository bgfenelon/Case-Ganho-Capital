from src.core.entities.produto import Produto

class CalcularPrecoFinal:
    def executar(self, produto: Produto) -> float:
        if not isinstance(produto, Produto):
            raise TypeError("Objeto inválido. Esperado: Produto")
        return produto.aplicar_desconto()
