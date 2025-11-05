from src.core.entities.produto import Produto
from src.core.use_cases.calcular_preco_final import CalcularPrecoFinal

def main():
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    desconto = float(input("Desconto (0 a 1): "))

    produto = Produto(nome, preco, desconto)
    use_case = CalcularPrecoFinal()
    preco_final = use_case.executar(produto)

    print(f"Preço final do produto '{nome}': R${preco_final:.2f}")
