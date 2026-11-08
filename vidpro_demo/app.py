"""P1 VidPro integration proof of concept. No AI API or Colab automation claimed."""
import os
import uuid
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel, Field

app = FastAPI(title="P1 VidPro Demo")
VIDEO_PATH = Path(os.getenv("P1_DEMO_VIDEO", "sample.mp4")).resolve()
jobs = {}

class VideoRequest(BaseModel):
    prompt: str = Field(min_length=3, max_length=2000)

@app.get("/", response_class=HTMLResponse)
def home():
    return Path(__file__).with_name("index.html").read_text(encoding="utf-8")

@app.get("/api/health")
def health():
    return {"status": "ok", "mode": "demo", "video_available": VIDEO_PATH.is_file()}

@app.post("/api/videos")
def create_video(request: VideoRequest):
    job_id = str(uuid.uuid4())
    # Explicit demo: do not pretend that this creates a new video.
    jobs[job_id] = {"id": job_id, "prompt": request.prompt,
                    "status": "sample_ready" if VIDEO_PATH.is_file() else "sample_missing",
                    "mode": "demo", "message": "This is a prerecorded sample, not a generated video."}
    return jobs[job_id]

@app.get("/api/videos/{job_id}")
def get_video_job(job_id: str):
    if job_id not in jobs:
        raise HTTPException(404, "Job not found")
    return jobs[job_id]

@app.get("/api/sample")
def sample():
    if not VIDEO_PATH.is_file():
        raise HTTPException(404, "Place your existing MP4 at P1_DEMO_VIDEO to enable playback.")
    return FileResponse(VIDEO_PATH, media_type="video/mp4", filename="P1_VidPro_Sample.mp4")
