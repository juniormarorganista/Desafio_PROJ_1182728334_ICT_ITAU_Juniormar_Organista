FAQ = {
    "faq": (
        "Posso ajudar com dúvidas frequentes, acompanhamento de solicitações e "
        "encaminhamento para atendimento humano quando necessário."
    )
}


def search_answer(intent: str) -> str:
    return FAQ.get(intent, "Não encontrei uma resposta direta para essa solicitação.")
