import sys
import json
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.utils.executar_lista_dados import processar_arquivo



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python -m src.main <arquivo_entrada>")
    else:
        processar_arquivo(sys.argv[1])

