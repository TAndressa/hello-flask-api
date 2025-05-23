# Hello Flask API 🚀

Primeira API desenvolvida com Flask como parte do meu roadmap de migração de QA para desenvolvedora back-end.

## 📌 Objetivo

Este projeto é uma introdução ao desenvolvimento de APIs REST com Flask, focando em:

- Estrutura básica de uma aplicação Flask
- Criação de rotas simples
- Retorno de dados em formato JSON

## 🔧 Tecnologias

- Python 3.10+
- Flask

## 🚀 Como executar

```bash
# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Instale as dependências
pip install flask

# Rode a aplicação
python app.py

# A API estará disponível em: http://localhost:5000/
```
## 🔁 Rotas disponíveis

| Rota      | Método | Descrição                          |
| --------- | ------ | ---------------------------------- |
| `/`       | GET    | Mensagem de boas-vindas            |
| `/status` | GET    | Exibe o status da API              |
| `/sobre`  | GET    | Informações sobre a desenvolvedora |

## ✅ Testes Automatizados
Este projeto possui testes automatizados utilizando pytest, garantindo que as rotas da API estejam funcionando corretamente.

## 📁 Arquivo de testes

Os testes estão localizados no arquivo:
```bash
test_app.py
```

## ▶️ Como rodar os testes

```bash
# 1.Ative o ambiente virtual:

venv\Scripts\activate   # Windows
source venv/bin/activate  # macOS/Linux

# 2. Execute os testes:

python -m pytest

```

## ✔️ O que é testado

- Rota / → Verifica a mensagem de boas-vindas.
- Rota /status → Verifica status e versão da API.
- Rota /sobre → Verifica informações sobre a desenvolvedora.

Você verá um resultado como:

**================ test session starts =================
collected 3 items

test_app.py ...                                  [100%]

================ 3 passed in 0.05s ====================
**
