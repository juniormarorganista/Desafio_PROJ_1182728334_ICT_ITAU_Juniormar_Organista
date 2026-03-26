from __future__ import annotations

from datetime import datetime


def build_event(session_id: str, intent: str, confidence: float, handoff: bool) -> dict:
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "session_id": session_id,
        "intent": intent,
        "confidence": confidence,
        "handoff": handoff,
    }
