# P1 VidPro — Colab cinematic production pipeline

P1 VidPro is the video-production component of the broader P1 project. The existing `personal_agent_starter/` is a separate application and is intentionally untouched.

## Current baseline
- 10 Stable Diffusion 1.5 scenes, generated in Colab using an NVIDIA GPU when available
- Edge TTS: `en-US-GuyNeural`, `+5%`
- Whisper base, English, word-level timestamps and short subtitle phrases
- FFmpeg H.264/AAC 720x1280 at 24 fps, 0.5-second crossfades
- Approved centered subtitles: Lato Light, 72, white, black outline 2.5, `\\an5\\pos(360,640)`
- Approved artifact: `P1_Gratitude_Exact_Middle.mp4`

## Working notebook
Use `P1_VidPro_Production_v1.ipynb` from the project handover in Google Colab. Save it under `vidpro/` in this repository. It is a new non-destructive production notebook, not a replacement for the original historical review notebook.

The notebook stores generated assets under `MyDrive/P1/vidpro/gratitude/` by default. Do not commit generated images, MP3/MP4, model weights, cached clips, API secrets or the 116 MB original notebook with embedded outputs.

## First run
1. Open the production notebook in Colab and enable GPU if image generation is needed.
2. Run setup and mount Drive.
3. Copy existing scene images, voiceover, subtitles, and videos into the project folders.
4. Inspect asset inventory before enabling generation.
5. Run caption/FFmpeg stages only if required.

## Engineering status
Notebook syntax has been checked locally, but a full Colab GPU / rendering execution has **not** been performed. Validate on Colab before treating it as production-ready. Further milestones: content-hash cache invalidation, flexible story manifests, reusable output naming, character consistency, image-to-video animation, QA tests, and agent orchestration.

## Safety
Never overwrite the approved final video. Maintain the original review notebook as an archive.
