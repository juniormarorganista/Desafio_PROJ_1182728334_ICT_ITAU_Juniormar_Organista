from src.app.nlu import classify_intent


def test_classify_acompanhamento() -> None:
    intent, confidence = classify_intent("Quero acompanhar meu protocolo 123")
    assert intent == "acompanhar_solicitacao"
    assert confidence > 0.8


def test_classify_handoff() -> None:
    intent, confidence = classify_intent("Quero falar com um atendente humano")
    assert intent == "handoff_humano"
    assert confidence > 0.8
