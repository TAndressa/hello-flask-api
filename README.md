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

## 🔁 Rotas disponíveis

| Rota      | Método | Descrição                          |
| --------- | ------ | ---------------------------------- |
| `/`       | GET    | Mensagem de boas-vindas            |
| `/status` | GET    | Exibe o status da API              |
| `/sobre`  | GET    | Informações sobre a desenvolvedora |

