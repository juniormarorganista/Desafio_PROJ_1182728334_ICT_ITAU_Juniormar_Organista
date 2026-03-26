# Desafio PROJ 1182728334 - ICT ITAÚ - Juniormar Organista

Este repositório organiza a proposta conceitual de um modelo de chatbot corporativo, incluindo visão da solução, arquitetura, fluxos conversacionais, plano de testes com usuários, validação técnica e de negócio, além de um esqueleto de código para demonstrar a organização do projeto.

## Objetivo
Apresentar uma solução de chatbot orientada a atendimento digital, com foco em:
- entendimento de intenção;
- consulta a base de conhecimento e sistemas internos;
- encaminhamento para atendimento humano quando necessário;
- monitoramento contínuo da qualidade;
- governança de documentação e versionamento.

## Estrutura do repositório
- `docs/`: documentação funcional, técnica e de validação;
- `Dockerfile`: execução containerizada simples.
- `requirements.txt`: dependências mínimas;
- `src/app/`: esqueleto de código da aplicação;
- `tests/`: testes iniciais de comportamento;

## Como executar o protótipo
```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows

pip3 install -r requirements.txt
uvicorn src.app.main:app --reload
```
