def formatar_moeda(valor: float) -> str:
    return f"R${valor:.2f}".replace('.', ',')
