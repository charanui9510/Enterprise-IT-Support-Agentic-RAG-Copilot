import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from app.core.config import get_settings

settings = get_settings()

def _get_db_path() -> str:
    raw_path = str(settings.audit_db_path).replace("sqlite:///", "")
    db_path = Path(raw_path).resolve()
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return str(db_path)

def init_db() -> None:
    con = sqlite3.connect(_get_db_path())
    con.execute(
        """CREATE TABLE IF NOT EXISTS query_audit (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL,
            question TEXT NOT NULL,
            source_used TEXT NOT NULL,
            trace_json TEXT NOT NULL
        )"""
    )
    con.commit()
    con.close()

def write_audit(question: str, source_used: str, trace: list[str]) -> None:
    con = sqlite3.connect(_get_db_path())
    con.execute(
        "INSERT INTO query_audit(created_at, question, source_used, trace_json) VALUES (?, ?, ?, ?)",
        (datetime.now(timezone.utc).isoformat(), question, source_used, json.dumps(trace)),
    )
    con.commit()
    con.close()
