from src.app.orchestrator import handle_message


def test_handle_message_returns_expected_keys() -> None:
    result = handle_message("sess-1", "Quero ajuda")
    assert "intent" in result
    assert "answer" in result
    assert "event" in result
