# Case Pilar
> https://case-pilar-eduardo-alencar-15d805dfabdd.herokuapp.com/docs

## Requisitos
- Python 3.11 ou superior;
- FastAPI;
- Poetry (Gerenciamento de dependências);
- Pytest (Testes)
- Ruff e MyPY para formatação e lint.

## Execução

Para rodar o projeto localmente:

1. Clone o repositório
2. Ative o ambiente virtual: `poetry shell`
3. Instale as dependência com Poetry: `poetry install`
4. Execute: `fastapi dev main.py` 
5. Acesse: http://localhost:8000/docs

## Comandos

1. Para rodar os testes use: `pytest -vv` na raiz do projeto;
2. Para formatar os arquivos use: `sh scripts/format.sh` na raiz do projeto;
3. Para lint use: `sh scripts/lint.sh` na raiz do projeto;

## TODO's

- [x] Setup do projeto fastapi, com uma rota hello-world 
- [x] Setup ferramental para testes (pytest)
- [x] Criar teste para rota hello-world
- [x] Validar requisição antes de processar. (Método HTTP, rota que não existe, content type deve ser application/json)
- [x] Criar rota /vowel_count- 
- [x] Criar rota /sort 
- [x] Construir pipeline com lint, testes e deploy 
