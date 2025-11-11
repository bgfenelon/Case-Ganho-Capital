from src.domain.win_of_capital import WinOfCapital

def executando_lista_entrada(dados):

    resultado_lista_dados = []
    
    for db in dados:
        calc = WinOfCapital()
        calc.processar_operacoes(db)
        resultado_lista_dados.append(calc.get_lista_imposto())
    
    return resultado_lista_dados
