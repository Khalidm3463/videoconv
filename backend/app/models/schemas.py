from pydantic import BaseModel
from typing import Optional

class UploadResponse(BaseModel):
    srt_file: str
    video_file: Optional[str]

class LinkProcessRequest(BaseModel):
    url: str
    target_lang: str
    burn_subs: bool = True

class UploadProcessRequest(BaseModel):
    target_lang: str
    burn_subs: bool = False
