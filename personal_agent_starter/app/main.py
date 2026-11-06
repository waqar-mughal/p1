import uuid
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from agents import Runner
from .agent import agent
from .ui import HTML
from .store import init_db, get_history, save_history, list_approvals

app = FastAPI(title="Personal Agent", version="0.1.0")

@app.on_event("startup")
def startup():
    init_db()

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=12000)
    conversation_id: str | None = None

@app.get("/api/health")
def health():
    return {"status": "ok", "version": "0.1.0"}

@app.post("/api/chat")
async def chat(payload: ChatRequest):
    cid = payload.conversation_id or str(uuid.uuid4())
    history = get_history(cid)
    try:
        result = await Runner.run(agent, history + [{"role": "user", "content": payload.message}])
        save_history(cid, result.to_input_list())
        return {"conversation_id": cid, "reply": result.final_output}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Agent run failed: {type(exc).__name__}")

@app.get("/api/approvals")
def approvals():
    return {"items": list_approvals()}

@app.get("/", response_class=HTMLResponse)
def home():
    return HTML
