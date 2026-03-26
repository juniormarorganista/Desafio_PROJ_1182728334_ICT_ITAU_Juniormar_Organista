# 03. Fluxos conversacionais

## Fluxo 1 - Perguntas frequentes
1. usuário envia a dúvida;
2. o classificador identifica intenção FAQ;
3. o chatbot consulta a base de conhecimento;
4. a resposta é exibida;
5. o usuário avalia se a resposta resolveu o problema.

## Fluxo 2 - Acompanhamento de solicitação
1. usuário informa número de protocolo;
2. o chatbot valida formato e contexto;
3. consulta o sistema de protocolos;
4. retorna status e próximo passo;
5. registra interação para analytics.

## Fluxo 3 - Handoff para humano
1. usuário demonstra baixa satisfação ou entra em caso complexo;
2. o chatbot registra resumo do contexto;
3. transfere para fila especializada;
4. o atendente recebe histórico resumido;
5. a conversa continua sem reinício desnecessário.
