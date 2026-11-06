# Personal Agent — Starter (Phase 1)

A first working foundation: FastAPI, OpenAI Agents SDK, SQLite conversation history,
a browser chat panel, restricted workspace file tools, and an approval-request queue.

## Run on Windows (PowerShell)
1. Install Python 3.11 or newer.
2. In this folder run:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
notepad .env
```

3. Put your OpenAI API key in `.env` (never paste it into chat).
4. Start the app:

```powershell
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

5. Open http://127.0.0.1:8000

## Included
- Chat interface and persistent SQLite conversation history.
- Restricted file tools for the `workspace/` directory.
- Pending approval request queue at `/api/approvals`.
- Health endpoint at `/api/health`.

## Safety and current limits
This is Phase 1, not yet a complete autonomous computer operator. It does not have
unrestricted shell access, email sending, purchases, or destructive file actions.
Approval requests are recorded but not executed. Keep the server bound to 127.0.0.1;
do not expose this development server directly to the public internet.

## Next milestones
Authenticated cloud deployment; secure Windows companion; browser automation;
voice input/output; integrations; durable jobs, audit logs, retries, budgets, and
granular approvals.
