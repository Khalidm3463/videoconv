import subprocess

def burn_subtitles(video_path: str, srt_path: str) -> str:
    """
    Uses ffmpeg to embed subtitles into the video.
    """
    output_path = video_path.replace("uploads", "processed").replace(".mp4", "_subtitled.mp4")
    command = [
        "ffmpeg", "-y", "-i", video_path,
        "-vf", f"subtitles={srt_path}",
        output_path
    ]
    subprocess.run(command, check=True)
    return output_path
