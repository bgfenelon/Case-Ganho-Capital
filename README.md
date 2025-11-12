# Case: Ganho de Capital

**Resumo rápido**

Programa de linha de comando (CLI) que calcula imposto sobre lucros e prejuízos em operações com ações. Recebe arquivos JSON e retorna o resultado conforme regras fiscais do exercício.

---

## Estrutura

* `src/` — código-fonte
* `tests/` — testes unitários
* `entrada.json` — exemplo de entrada
* `requirements.txt` — dependências

---

## Requisitos

* **Python 3.10+** (recomendado 3.11+)
* **pip** instalado

Verifique:

```bash
python --version
```

---

## Instalação

Na raiz do projeto:

```bash
# criar e ativar ambiente virtual
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate # macOS / Linux

# instalar dependências
pip install -r requirements.txt
```

Se o arquivo `requirements.txt` não existir:

```bash
pip install unittest
pip freeze > requirements.txt
```

---

## Execução

Para rodar o projeto com um arquivo JSON:

```bash
python -m src.main entrada.json
```

O arquivo `entrada.json` deve estar no formato:

```json
[
    {
        "operation": "buy",
        "unit-cost": 10.00,
        "quantity": 10000
    }
]
```

---

## Testes

Para rodar todos os testes com **unittest**:

```bash
python -m unittest discover tests
```

Ou para rodar um arquivo de teste específico:

```bash
python -m unittest tests/test_nome.py
```

---

## Dicas

* Execute sempre na raiz do projeto.
* Ative o ambiente virtual antes de instalar libs.
* Use `python -m src.main` para evitar erros de import.

---

