# Infrastructure Readiness Criteria

Este documento define os critérios técnicos utilizados para avaliar se um
sistema está apto para rodar em ambiente de produção do ponto de vista de
infraestrutura, confiabilidade e operação.

O objetivo não é validar regras de negócio, mas sim requisitos mínimos de
operação segura e escalável.

---

## 1. Healthcheck

**Descrição**  
O sistema deve expor um endpoint de saúde que permita verificar se a aplicação
está operacional.

**Objetivo**
- Permitir monitoramento
- Permitir reinício automático em caso de falha
- Integrar com orquestradores e load balancers

**Critério**
- Deve existir endpoint dedicado (ex.: `/health`)
- Deve responder rapidamente
- Não deve depender de recursos externos críticos

---

## 2. Containerização

**Descrição**  
O sistema deve ser empacotado em container para garantir reprodutibilidade.

**Objetivo**
- Padronizar execução
- Facilitar deploy
- Reduzir dependência de ambiente

**Critério**
- Dockerfile presente
- Imagem reproduzível
- Configuração via variáveis de ambiente

---

## 3. Integração Contínua (CI)

**Descrição**  
O sistema deve possuir pipeline automatizado para validação de código.

**Objetivo**
- Reduzir erros manuais
- Garantir qualidade mínima
- Automatizar validações básicas

**Critério**
- Pipeline de build automatizado
- Execução de testes ou validações
- Falha do pipeline bloqueia deploy

---

## 4. Orquestração

**Descrição**  
O sistema deve estar preparado para rodar em ambiente orquestrado.

**Objetivo**
- Escalabilidade
- Auto-recuperação
- Atualizações sem indisponibilidade

**Critério**
- Manifests de orquestração definidos (ex.: Kubernetes)
- Suporte a múltiplas instâncias
- Aplicação stateless

---

## 5. Logging

**Descrição**  
O sistema deve gerar logs adequados para operação e diagnóstico.

**Objetivo**
- Diagnóstico de falhas
- Auditoria
- Análise de comportamento

**Critério**
- Logs estruturados
- Níveis de log definidos (INFO, WARN, ERROR)
- Logs enviados para stdout/stderr

---

## 6. Escalabilidade

**Descrição**  
O sistema deve suportar crescimento de carga sem alterações estruturais.

**Objetivo**
- Suportar picos de acesso
- Crescer horizontalmente

**Critério**
- Escala por replicação
- Sem dependência de estado local
- Configurações externas ao código

---

## 7. Segurança Básica

**Descrição**  
O sistema deve atender a requisitos mínimos de segurança operacional.

**Objetivo**
- Proteger dados
- Reduzir superfície de ataque
- Evitar exposição acidental

**Critério**
- Secrets fora do código
- Comunicação segura na borda (TLS)
- Princípio do menor privilégio
