# 02. Arquitetura da solução

## Camadas
### 1. Canais
WhatsApp, aplicativo, webchat e canais futuros.

### 2. Entrada e segurança
API Gateway, autenticação, controle de tráfego, logs e auditoria.

### 3. Núcleo conversacional
- classificador de intenção;
- gerenciador de contexto;
- orquestrador de fluxo;
- mecanismo de handoff humano.

### 4. Integrações
- base de conhecimento;
- CRM e protocolos;
- catálogo de serviços;
- motor de notificações.

### 5. Observabilidade e governança
- dashboards operacionais;
- monitoramento de qualidade;
- trilha de decisão;
- conformidade com LGPD.

## Princípio de operação
Usuário -> gateway -> entendimento da intenção -> consulta a fontes -> resposta ou transferência.
