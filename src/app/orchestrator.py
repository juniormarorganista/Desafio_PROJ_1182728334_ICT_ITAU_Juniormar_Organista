from __future__ import annotations

from .handoff import should_handoff
from .metrics import build_event
from .nlu import classify_intent
from .router import route_intent


def handle_message(session_id: str, message: str) -> dict:
    intent, confidence = classify_intent(message)
    handoff = should_handoff(intent, confidence)
    answer = route_intent(intent, message)
    event = build_event(session_id, intent, confidence, handoff)

    return {
        "session_id": session_id,
        "intent": intent,
        "answer": answer,
        "confidence": confidence,
        "handoff": handoff,
        "event": event,
    }
