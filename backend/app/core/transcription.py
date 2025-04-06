import whisper

# Load Whisper model once globally
model = whisper.load_model("base")

def transcribe_audio(video_path: str):
    """
    Transcribes audio from video using Whisper and returns a list of segments with timestamps and text.
    """
    result = model.transcribe(video_path, verbose=False)
    segments = result['segments']
    return [{"start": s['start'], "end": s['end'], "text": s['text']} for s in segments]
