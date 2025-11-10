class WinOfCapital:
    def __init__(self, operation: str, unit_cost: float = 0.0, quantity: float = 0.0, 
                 weighted_discount: float = 0.0, current_actions: float = 0.0):

        self.operation = operation
        self.unit_cost = unit_cost
        self.quantity = quantity

        # Usa atributos privados para evitar loop nas properties
        self._weighted_discount = weighted_discount
        self._current_actions = current_actions

    # --- Getter e Setter de weighted_discount ---
    @property
    def weighted_discount(self):
        return self._weighted_discount

    @weighted_discount.setter
    def weighted_discount(self, valor):
        if valor < 0:
            raise ValueError("O preço médio ponderado não pode ser negativo.")
        self._weighted_discount = valor

    # --- Getter e Setter de current_actions ---
    @property
    def current_actions(self):
        return self._current_actions

    @current_actions.setter
    def current_actions(self, valor):
        if valor < 0:
            raise ValueError("A quantidade de ações não pode ser negativa.")
        self._current_actions = valor

    # --- Método de cálculo ---
    def calculo_preco_medio_ponderado_compra(self):
        """Calcula o novo preço médio ponderado após uma compra."""
        total_investido = (self._current_actions * self._weighted_discount) + (self.quantity * self.unit_cost)
        total_acoes = self._current_actions + self.quantity

        if total_acoes == 0:
            return 0.0  # evita divisão por zero

        nova_media_ponderada = total_investido / total_acoes

        # atualiza internamente o preço médio e as ações
        self._weighted_discount = nova_media_ponderada
        self._current_actions = total_acoes

        return nova_media_ponderada

    def __repr__(self):
        tipo = "Venda" if self.operation.lower() == "sell" else "Compra"
        return (f"<{tipo}: {self.quantity} unidades a R${self.unit_cost:.2f}, "
                f"PM: R${self._weighted_discount:.2f}, Ações: {self._current_actions}>")
