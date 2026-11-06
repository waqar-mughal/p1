import json, sqlite3, uuid
from datetime import datetime, timezone
from .config import DATABASE_PATH

def connect():
    db = sqlite3.connect(DATABASE_PATH)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    with connect() as db:
        db.execute("CREATE TABLE IF NOT EXISTS conversations (conversation_id TEXT PRIMARY KEY, history_json TEXT NOT NULL, updated_at TEXT NOT NULL)")
        db.execute("CREATE TABLE IF NOT EXISTS approvals (approval_id TEXT PRIMARY KEY, action TEXT NOT NULL, reason TEXT NOT NULL, status TEXT NOT NULL, created_at TEXT NOT NULL)")

def get_history(cid):
    with connect() as db:
        row = db.execute("SELECT history_json FROM conversations WHERE conversation_id=?", (cid,)).fetchone()
    return json.loads(row["history_json"]) if row else []

def save_history(cid, history):
    with connect() as db:
        db.execute(
            "INSERT INTO conversations VALUES (?, ?, ?) ON CONFLICT(conversation_id) DO UPDATE SET history_json=excluded.history_json, updated_at=excluded.updated_at",
            (cid, json.dumps(history), datetime.now(timezone.utc).isoformat())
        )

def create_approval(action, reason):
    aid = str(uuid.uuid4())
    with connect() as db:
        db.execute("INSERT INTO approvals VALUES (?, ?, ?, ?, ?)",
                   (aid, action, reason, "pending", datetime.now(timezone.utc).isoformat()))
    return aid

def list_approvals():
    with connect() as db:
        rows = db.execute("SELECT * FROM approvals ORDER BY created_at DESC").fetchall()
    return [dict(r) for r in rows]
