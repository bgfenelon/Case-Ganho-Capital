class ValidadorOperacoes:

    CAMPOS_OBRIGATORIOS = {"operation", "unit-cost", "quantity"}
    OPERACOES_VALIDAS = {"buy", "sell"}

    @staticmethod
    def validar(entrada_dados: list):

        if not isinstance(entrada_dados, list):
            raise TypeError("A entrada deve ser uma lista de operações.")

        for i, operacao in enumerate(entrada_dados, start=1):
            if not isinstance(operacao, dict):
                raise TypeError(f"Operação {i} deve ser um dicionário.")

            # Verifica campos obrigatórios
            faltando = ValidadorOperacoes.CAMPOS_OBRIGATORIOS - operacao.keys()
            if faltando:
                raise ValueError(f"Operação {i} faltando campos obrigatórios: {faltando}")

            tipo = operacao["operation"]
            preco = operacao["unit-cost"]
            qtd = operacao["quantity"]

            # Verifica tipo da operação
            if tipo not in ValidadorOperacoes.OPERACOES_VALIDAS:
                raise ValueError(f"Operação {i}: valor inválido para 'operation' ({tipo}).")

            # Verifica tipos numéricos
            if not isinstance(preco, (int, float)) or not isinstance(qtd, (int, float)):
                raise TypeError(f"Operação {i}: 'unit-cost' e 'quantity' devem ser números.")

            # Verifica valores positivos
            if preco <= 0:
                raise ValueError(f"Operação {i}: 'unit-cost' deve ser maior que 0.")
            if qtd <= 0:
                raise ValueError(f"Operação {i}: 'quantity' deve ser maior que 0.")

        return True
