import uuid
import os
import subprocess
from pathlib import Path
from fastapi import APIRouter, BackgroundTasks
from app.models.schemas import DownloadRequest
from app.services.downloader import download_audio, download_video
from app.services.progress import create_task, get_task

router = APIRouter()

DOWNLOAD_DIR = Path("downloads").resolve()

@router.post("/download/audio")
def download_audio_route(req: DownloadRequest, bg: BackgroundTasks):
    task_id = str(uuid.uuid4())
    create_task(task_id)
    bg.add_task(download_audio, req.url, req.quality, task_id)
    return {"task_id": task_id}

@router.post("/download/video")
def download_video_route(req: DownloadRequest, bg: BackgroundTasks):
    task_id = str(uuid.uuid4())
    create_task(task_id)
    bg.add_task(download_video, task_id, req.url, req.quality)
    return {"task_id": task_id}

@router.get("/downloads")
def open_downloads():
    try:
        if os.name == "nt":
            subprocess.run(
                ["explorer", str(DOWNLOAD_DIR)],
                shell=True
            )
        else:
            subprocess.Popen(["xdg-open", str(DOWNLOAD_DIR)])

        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@router.get("/status/{task_id}")
def get_status(task_id: str):
    return get_task(task_id)
