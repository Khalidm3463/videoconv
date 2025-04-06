import yt_dlp
import uuid

def download_video_from_url(url: str) -> str:
    """
    Downloads a video using yt-dlp and returns the file path.
    """
    uid = str(uuid.uuid4())
    output_path = f"media/uploads/{uid}.mp4"
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_path,
        'quiet': True,
        'noplaylist': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return output_path
