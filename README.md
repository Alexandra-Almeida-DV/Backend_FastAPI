# 🚀 Backend FastAPI Reutilizável

Backend desenvolvido com **FastAPI**, pensado para ser **reutilizável**, escalável e servir como base para múltiplos projetos (sites institucionais, landing pages, APIs REST, formulários de contato, etc).

O projeto segue boas práticas de organização, separação de responsabilidades e configuração moderna com **Pydantic v2**.

---

## 🧱 Tecnologias Utilizadas

- Python 3.12+
- FastAPI
- Uvicorn
- Pydantic v2
- Pydantic Settings
- SMTP (envio de e-mails)
- Dotenv (`.env`)
- Arquitetura modular

---

## 📁 Estrutura do Projeto

```text
app/
├── api/
│   └── routes/
│       ├── health.py
│       ├── contact.py
│       ├── analytics.py
│       └── newsletter.py
├── core/
│   └── config.py
├── services/
│   └── email_services.py
├── schemas/
│   └── contact.py
├── db/
├── utils/
└── main.py

tests/
.env
.env.example
requirements.txt
READM.md
