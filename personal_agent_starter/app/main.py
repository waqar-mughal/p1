import uuid

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

from agents import Runner
from .agent import agent
from .config import DEMO_MODE
from .ui import HTML
from .store import init_db, get_history, save_history, list_approvals

app = FastAPI(
    title="P1 Personal Creator",
    description="A personal workspace for planning and producing social content.",
    version="0.2.0",
)


@app.on_event("startup")
def startup():
    init_db()


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=12000)
    conversation_id: str | None = None


def demo_reply(message: str) -> str:
    """A predictable local response so the product can be explored without paid APIs."""
    subject = message.strip().rstrip(".!?") or "your idea"
    return (
        "Here is a starter content plan based on your request. This is a local demo; "
        "connect an AI provider later for tailored research and generation.\n\n"
        f"CONTENT IDEA\n{subject}\n\n"
        "FORMAT\nA 30–45 second vertical video (9:16). You do not need to appear on camera.\n\n"
        "HOOK\n“Have you ever wondered why this matters?”\n\n"
        "SCRIPT\n1. Open with the hook.\n"
        "2. Explain one useful idea in simple language.\n"
        "3. Give one practical example.\n"
        "4. End with a clear takeaway and a gentle call to action.\n\n"
        "PRODUCTION PLAN\n"
        "• Visuals: use relevant stock-style or AI-generated scenes.\n"
        "• Voice: choose a natural narration voice.\n"
        "• Captions: add readable on-screen subtitles.\n"
        "• Review: check facts, spelling and media rights before publishing.\n\n"
        "NEXT STEP\nTell me your topic, audience and preferred platform, and this demo "
        "can help you shape a more specific draft. Actual AI research, avatar/video "
        "generation and publishing integrations are not connected in this version."
    )


@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "product": "P1 Personal Creator",
        "version": app.version,
        "mode": "demo" if DEMO_MODE else "live_ai",
        "ai_connected": not DEMO_MODE,
    }


@app.post("/api/chat")
async def chat(payload: ChatRequest):
    cid = payload.conversation_id or str(uuid.uuid4())
    history = get_history(cid)
    try:
        if DEMO_MODE:
            reply = demo_reply(payload.message)
            history.extend([
                {"role": "user", "content": payload.message},
                {"role": "assistant", "content": reply},
            ])
        else:
            result = await Runner.run(
                agent,
                history + [{"role": "user", "content": payload.message}],
            )
            history = result.to_input_list()
            reply = result.final_output
        save_history(cid, history)
        return {
            "conversation_id": cid,
            "reply": reply,
            "mode": "demo" if DEMO_MODE else "live_ai",
        }
    except Exception as exc:
        # Do not send credentials, provider payloads, or internal tracebacks to the browser.
        raise HTTPException(
            status_code=503,
            detail=f"Assistant unavailable ({type(exc).__name__}). Check server configuration.",
        )


@app.get("/api/approvals")
def approvals():
    return {"items": list_approvals()}


@app.get("/", response_class=HTMLResponse)
def home():
    return HTML
