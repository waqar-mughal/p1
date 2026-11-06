# P1 Personal Creator — prototype

P1 is intended to help individual creators turn ideas into content without needing to appear on camera or learn a complicated production workflow.

This repository currently contains an early FastAPI prototype with a browser dashboard, a local demo assistant, SQLite conversation history, and restricted workspace tools.

## Current status

### Works without a paid AI API
- Responsive P1 Creator dashboard in the browser.
- Demo assistant that returns a sample short-video content outline.
- Conversation history stored locally in SQLite.
- Health endpoint showing whether the app is in demo or live-AI mode.
- Existing restricted workspace file tools and approval-request recording.

### Not connected yet
- Live AI research and tailored script generation.
- AI image, video, avatar, and voice generation.
- Social account connections, scheduling, and publishing.
- User accounts, cloud database, team features, and production security.

The demo is deliberately labelled as a demo. It does not pretend to generate real videos or publish content.

## Run locally (Windows PowerShell)

Python 3.11 or newer is recommended.

```powershell
cd personal_agent_starter
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000

No API key is required for the default demo mode.

## Enable live AI later

1. Open your local `.env` file.
2. Set `DEMO_MODE=false`.
3. Add your provider key to `OPENAI_API_KEY`.
4. Set `AGENT_MODEL` to a model supported by your account.
5. Restart the app.

Never commit `.env`, paste API keys into chat, or put secrets in frontend code. The repository includes `.env.example` with blank placeholders only.

## API endpoints

- `GET /` — browser dashboard.
- `GET /api/health` — application status and current mode.
- `POST /api/chat` — demo or live-AI assistant conversation.
- `GET /api/approvals` — recorded approval requests.

## Safety and deployment notes

This is a development prototype, not ready for public customer use. It currently has no user authentication or tenant isolation. Keep it local and private; do not expose it to the public internet or enter sensitive customer information.

The existing SQLite database file is retained in the repository for now rather than deleted automatically. New local database files are ignored by Git. Before production, database ownership, migration, backup, and deployment must be addressed.

## Planned build sequence

1. Stabilize the creator workflow and add tests.
2. Add secure user accounts and cloud data storage.
3. Add provider integrations behind explicit configuration and cost controls.
4. Add media generation, preview, and export workflows.
5. Add social integrations and publishing with user confirmation.
6. Deploy a secured live version and verify it before inviting customers.
