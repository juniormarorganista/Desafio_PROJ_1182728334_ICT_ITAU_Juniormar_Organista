def should_handoff(intent: str, confidence: float) -> bool:
    if intent == "handoff_humano":
        return True
    if intent == "fallback" or confidence < 0.55:
        return True
    return False
