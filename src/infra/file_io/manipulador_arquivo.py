import json
from typing import Any

class ManipuladorArquivo:
    def salvar_json(self, caminho: str, dados: Any):
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def ler_json(self, caminho: str):
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)
