<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&pause=1000&center=true&vCenter=true&width=800&lines=Infrastructure+Readiness+Checker;Infra+%7C+DevOps+%7C+Architecture;Production+Readiness+Validation+Tool" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python" />
  <img src="https://img.shields.io/badge/FastAPI-API-green?logo=fastapi" />
  <img src="https://img.shields.io/badge/Docker-Containerized-blue?logo=docker" />
  <img src="https://img.shields.io/badge/CI-GitHub_Actions-success?logo=githubactions" />
  <img src="https://img.shields.io/badge/Infra-Production_Ready-critical" />
</p>

---

## 📌 Visão Geral

**Infrastructure Readiness Checker** é uma ferramenta focada em **infraestrutura e arquitetura**
que avalia se um sistema atende critérios mínimos para operar em **ambiente de produção**.

O objetivo não é validar regras de negócio, mas **confiabilidade, operação e escalabilidade**.

---

## 🎯 O que o projeto avalia

- Healthcheck
- Containerização
- Integração Contínua (CI)
- Orquestração
- Logging
- Escalabilidade (stateless)
- Segurança básica (TLS e secrets)

Cada critério gera:
- status técnico
- pontuação
- recomendações acionáveis

---

## 🧱 Arquitetura do Projeto

```text
infra-readiness-checker/
├── app/
│   ├── main.py        # API entrypoint
│   ├── models.py      # Data models
│   └── rules.py       # Evaluation engine
├── tests/             # Automated tests
├── docs/              # Infrastructure criteria
├── .github/workflows/ # CI pipeline
├── Dockerfile
├── requirements.txt
└── README.md

🚀 Executando localmente com Docker
Build da imagem

docker build -t infra-readiness-checker .

Subir o serviço
docker run -p 8000:8000 infra-readiness-checker

Healthcheck

curl http://localhost:8000/health

🧪 Exemplo de avaliação

curl -X POST http://localhost:8000/evaluate \
  -H "Content-Type: application/json" \
  -d '{
    "has_healthcheck": true,
    "uses_docker": true,
    "has_ci": false,
    "uses_orchestration": true,
    "has_logging": true,
    "is_stateless": true,
    "has_tls": false,
    "uses_secrets_management": false
  }'

Resposta:

{
  "score": 70,
  "status": "PARTIALLY READY",
  "checks": {
    "healthcheck": "OK",
    "containerization": "OK",
    "ci": "MISSING",
    "orchestration": "OK",
    "logging": "OK",
    "stateless": "OK",
    "security": "PARTIAL"
  },
  "recommendations": [
    "Implement a CI pipeline for automated validation",
    "Enable TLS for external communication",
    "Move secrets out of source code"
  ]
}

📄 Documentação Técnica

Critérios de avaliação estão documentados em:

docs/criteria.md

📄 Licença

Este projeto é distribuído sob a Apache License 2.0.

👤 Autoria

Raquel Souza
2025

