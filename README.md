# api-simples

> Projeto exemplo simples em Python para demonstração e testes.

## Requisitos

- Python 3.10+ (recomendo 3.11)
- Dependências em `requirements.txt` (se presente)

## Como instalar

- Crie e ative um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

- Instale dependências:

```bash
pip install -r requirements.txt
```

## Executando o projeto

```bash
python main.py
```

## Testes

Os testes usam `pytest`.

```bash
pytest -q
```

## CI

Há um workflow do GitHub Actions em `.github/workflows/ci.yml` que roda os testes em pushes e pull requests.
