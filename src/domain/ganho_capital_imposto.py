class GanhoCapitalImposto:
    def __init__(self):
        self.lucro = []
        self.lista_preco = []
        self.lista_quantidade = []
        self.lista_imposto = []
        self.preco_medio = 0.0
        self.quantidade_atual = 0
        self.prejuizo_acumulado = 0.0
        self.imposto_total = 0.0

    def processar_operacoes(self, entrada_dados: list):

        for op in entrada_dados:
            tipo = op["operation"]
            preco = op["unit-cost"]
            qtd = op["quantity"]

            if tipo == "buy":
                self.comprar(preco, qtd)
            elif tipo == "sell":
                self.vender(preco, qtd)
            else:
                raise ValueError(f"Operação desconhecida: {tipo}")

    def comprar(self, preco, qtd):
        self.preco_medio = ((self.preco_medio * self.quantidade_atual) + (preco * qtd)) / (self.quantidade_atual + qtd)
        self.quantidade_atual += qtd
        imposto = 0.0
        self.lista_imposto.append({"tax": imposto})

    def vender(self, preco, qtd):
        if qtd > self.quantidade_atual:
            raise ValueError("Tentando vender mais ações do que possui!")

        valor_total_venda = preco * qtd
        resultado = (preco - self.preco_medio) * qtd


        if valor_total_venda <= 20000:
            imposto = 0.0
            if resultado < 0:
                self.prejuizo_acumulado += abs(resultado)

        elif resultado < 0:
            self.prejuizo_acumulado += abs(resultado)
            imposto = 0.0

        else:
            lucro_liquido = resultado - self.prejuizo_acumulado
            if lucro_liquido > 0:
                imposto = lucro_liquido * 0.20
                self.imposto_total += imposto
                self.prejuizo_acumulado = 0.0
            else:
                imposto = 0.0
                self.prejuizo_acumulado = abs(lucro_liquido)

        self.quantidade_atual -= qtd
        self.lista_imposto.append({"tax": imposto})
        self.lucro.append(resultado)

    def get_lista_imposto(self):
            return self.lista_imposto

