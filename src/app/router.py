from __future__ import annotations

from .knowledge_base import search_answer


def route_intent(intent: str, message: str) -> str:
    if intent == "acompanhar_solicitacao":
        return (
            "Seu pedido de acompanhamento foi identificado. "
            "Em uma versão integrada, eu consultaria o sistema de protocolos e "
            "retornaria o status atualizado."
        )
    if intent == "handoff_humano":
        return (
            "Vou encaminhar sua conversa para atendimento humano com o contexto "
            "já resumido para evitar repetição."
        )
    if intent == "faq":
        return search_answer(intent)

    return (
        "Não consegui interpretar sua solicitação com segurança. "
        "Posso transferir você para um atendente."
    )
