from pydantic import BaseModel

class DownloadRequest(BaseModel):
    url: str
    quality: str = "192"
    resolution: str = "best"