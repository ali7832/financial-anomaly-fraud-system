from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


def write_audit_event(event: dict, path: str) -> None:
    payload = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        **event,
    }
    with Path(path).open('a', encoding='utf-8') as handle:
        handle.write(json.dumps(payload) + '\n')
