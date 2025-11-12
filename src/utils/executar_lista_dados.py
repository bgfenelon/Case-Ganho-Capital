import json
import os
from src.domain.ganho_capital_imposto import GanhoCapitalImposto
from src.domain.validar_operacoes import ValidadorOperacoes

def executando_lista_entrada(dados):

    resultado_lista_dados = []
    
    for db in dados:
        calc = GanhoCapitalImposto()
        calc.processar_operacoes(db)
        resultado_lista_dados.append(calc.get_lista_imposto())
    
    return resultado_lista_dados

def validar_json(linha: str):
    try:
        data = json.loads(linha)
        if not isinstance(data, list):
            raise ValueError("O JSON deve ser uma lista de operações")
        return data
    except json.JSONDecodeError as e:
        raise ValueError(f"Erro de formato JSON: {e}")

def processar_arquivo(arquivo_entrada: str):

    if not os.path.exists(arquivo_entrada):
        raise FileNotFoundError(f"Arquivo '{arquivo_entrada}' não encontrado.")

    with open(arquivo_entrada, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue  

            try:
                entrada_dados = validar_json(linha)
                operacoes = entrada_dados
                ValidadorOperacoes.validar(operacoes)
                calc = GanhoCapitalImposto()
                calc.processar_operacoes(operacoes)
                print(calc.get_lista_imposto())

            except ValueError as e:
                print(f"Erro ao processar linha: {e}")
            except Exception as e:
                print(f"Erro inesperado: {e}")
