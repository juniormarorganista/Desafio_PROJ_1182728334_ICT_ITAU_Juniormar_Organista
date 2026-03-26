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

## Endpoint principal
- `POST /chat`
- Exemplo de payload:
```json
{
  "session_id": "abc-123",
  "message": "Quero acompanhar meu protocolo 98765"
}
```

## Resultado esperado
O serviço identifica a intenção, seleciona o fluxo, gera resposta inicial e registra métricas simples de execução.

## Observação
O código incluído aqui tem papel demonstrativo e arquitetural. Em um projeto real, a camada de NLU, integrações, autenticação, observabilidade e critérios de segurança seriam aprofundados conforme os requisitos de negócio e as políticas da organização.
