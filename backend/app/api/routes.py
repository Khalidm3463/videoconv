from fastapi import APIRouter, UploadFile, File, Form
from app.core.downloader import download_video_from_url
from app.core.transcription import transcribe_audio
from app.core.translation import translate_text
from app.core.subtitle_generator import create_srt
from app.core.video_processor import burn_subtitles
import uuid

router = APIRouter()

# @router.post("/process_upload/")
# @router.post("/process_link")
@router.post("/process_upload/")

async def process_uploaded_video(
    file: UploadFile = File(...),
    target_lang: str = Form(...),
    burn_subs: bool = Form(False)
):
    uid = str(uuid.uuid4())
    upload_path = f"media/uploads/{uid}_{file.filename}"
    with open(upload_path, "wb") as f:
        f.write(await file.read())

    srt_path, final_path = await handle_transcription_translation(upload_path, target_lang, burn_subs)
    return {
        "srt_file": srt_path,
        "video_file": final_path if burn_subs else None
    }

@router.post("/process_link")
async def process_video_from_link(
    url: str = Form(...),
    target_lang: str = Form(...),
    burn_subs: bool = Form(True)
):
    video_path = download_video_from_url(url)
    srt_path, final_path = await handle_transcription_translation(video_path, target_lang, burn_subs)
    return {
        "srt_file": srt_path,
        "video_file": final_path if burn_subs else None
    }

async def handle_transcription_translation(video_path: str, target_lang: str, burn_subs: bool):
    transcript = transcribe_audio(video_path)
    translated_lines = [translate_text(line['text'], target_lang) for line in transcript]
    srt_path = create_srt(translated_lines, transcript, video_path)
    final_video_path = burn_subtitles(video_path, srt_path) if burn_subs else None
    return srt_path, final_video_path
