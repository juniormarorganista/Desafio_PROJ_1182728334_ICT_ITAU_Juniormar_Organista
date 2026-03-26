from __future__ import annotations


def classify_intent(message: str) -> tuple[str, float]:
    text = message.lower()

    if any(token in text for token in ["protocolo", "acompanhar", "status"]):
        return "acompanhar_solicitacao", 0.93
    if any(token in text for token in ["atendente", "humano", "reclamar", "reclamação"]):
        return "handoff_humano", 0.90
    if any(token in text for token in ["como", "o que", "ajuda", "dúvida", "duvida"]):
        return "faq", 0.78

    return "fallback", 0.45
