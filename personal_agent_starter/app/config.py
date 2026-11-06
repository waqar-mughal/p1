import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
WORKSPACE_DIR = Path(os.getenv("WORKSPACE_DIR", str(BASE_DIR / "workspace"))).resolve()
DATABASE_PATH = Path(os.getenv("DATABASE_PATH", str(BASE_DIR / "agent.db"))).resolve()
DEMO_MODE = os.getenv("DEMO_MODE", "true").strip().lower() in {"1", "true", "yes", "on"}
AGENT_MODEL = os.getenv("AGENT_MODEL", "gpt-4.1-mini")
WORKSPACE_DIR.mkdir(parents=True, exist_ok=True)
