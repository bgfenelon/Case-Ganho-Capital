class Produto:
    def __init__(self, nome: str, preco: float, desconto: float = 0.0):
        self.nome = nome
        self.preco = preco
        self.desconto = desconto

    def aplicar_desconto(self):
        return self.preco * (1 - self.desconto)
