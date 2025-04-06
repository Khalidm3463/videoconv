import os

def create_srt(translated_lines, segments, video_path: str) -> str:
    """
    Creates an .srt subtitle file using timestamps and translated text.
    """
    srt_path = video_path.replace("uploads", "processed").replace(".mp4", ".srt")
    with open(srt_path, "w", encoding="utf-8") as f:
        for idx, (line, seg) in enumerate(zip(translated_lines, segments)):
            start = format_timestamp(seg['start'])
            end = format_timestamp(seg['end'])
            f.write(f"{idx+1}\\n{start} --> {end}\\n{line}\\n\\n")
    return srt_path

def format_timestamp(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds - int(seconds)) * 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"
