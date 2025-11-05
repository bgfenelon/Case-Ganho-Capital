class ProdutoDTO:
    def __init__(self, nome: str, preco: float, desconto: float):
        self.nome = nome
        self.preco = preco
        self.desconto = desconto

    def to_dict(self):
        return {"nome": self.nome, "preco": self.preco, "desconto": self.desconto}
