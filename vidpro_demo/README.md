# P1 VidPro — integration demonstration

This is a **working FastAPI website scaffold**, not a complete video generator. It accepts text and optional browser speech-to-text, creates a demo job, and plays/downloads an **existing** MP4. No paid AI API is required.

## Local test

From the repository root:

```powershell
cd vidpro_demo
python -m pip install -r requirements.txt
$env:P1_DEMO_VIDEO="C:\path\to\P1_Gratitude_Clean_Subtitles.mp4"
python -m uvicorn app:app --reload
```

Open http://127.0.0.1:8000 . The sample must be present on the machine running the server. Do **not** commit MP4 files or credentials to GitHub.

## Integration milestones

1. Extract Colab sections into a Python video engine accepting a job manifest and writing a final MP4.
2. Replace in-memory jobs with a durable job queue and job status updates.
3. Implement a worker adapter for supported cloud compute; free Colab is **not** a dependable unattended public worker.
4. Add authentication, rate limits, safe storage, and signed download URLs before publishing publicly.
5. Deploy website and backend; configure object storage and a real production worker.

Free website hosting alone does not make GPU rendering available 24/7. The current demo makes no claim of generating fresh videos.
