from fastapi import APIRouter
from app.models.schemas import DownloadRequest
from app.services.downloader import download_audio, download_video

router = APIRouter()

@router.post("/download/audio")
def download_audio_route(req: DownloadRequest):
    download_audio(req.url, req.quality)
    return {"status": "audio downloaded"}

@router.post("/download/video")
def download_video_route(req: DownloadRequest):
    download_video(req.url, req.resolution)
    return {"status": "video downloaded"}
