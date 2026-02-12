from pathlib import Path
import yt_dlp
import uuid
from app.services.progress import create_task, update_task, complete_task

# Base download directory (safe location)
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DOWNLOADS_DIR = BASE_DIR / "downloads"
AUDIO_DIR = DOWNLOADS_DIR / "audio"
VIDEO_DIR = DOWNLOADS_DIR / "video"

# Ensure folders exist
AUDIO_DIR.mkdir(parents=True, exist_ok=True)
VIDEO_DIR.mkdir(parents=True, exist_ok=True)


def download_audio(url: str, quality: str = "192", task_id: str = None):
    def progress_hook(d):
        if d['status'] == 'downloading':
            downloaded = d.get('downloaded_bytes', 0)
            total = d.get('total_bytes') or d.get('total_bytes_estimate')
            speed = d.get('speed')
            eta = d.get('eta')
            if total and downloaded:
                percent = (downloaded / total) * 100
                percent = min(round(percent, 2), 99.9)  # Cap at 99.9% until finished
                update_task(
                    task_id,
                    percent,
                    round(speed /(1024 * 1024), 2) if speed else None,
                    eta
                    )
        elif d['status'] == 'finished':
            update_task(task_id, 100)
            complete_task(task_id)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": str(AUDIO_DIR / "%(title)s.%(ext)s"),
        "noplaylist": True,
        "progress_hooks": [progress_hook],
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": quality,
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_video(task_id: str, url: str, resolution: str = "best"):
    """
    Download video from YouTube and merge audio + video into MP4
    """
    if resolution == "best":
        format_selector = "bestvideo+bestaudio/best"
    else:
        format_selector = f"bestvideo[height<={resolution}]+bestaudio/best"


    
    def progress_hook(d):
        if d['status'] == 'downloading':
            downloaded = d.get('downloaded_bytes', 0)
            total = d.get('total_bytes') or d.get('total_bytes_estimate')
            speed = d.get('speed')
            eta = d.get('eta')
            if total and downloaded:
                percent = (downloaded / total) * 100
                percent = min(round(percent, 2), 99.9)  # Cap at 99.9% until finished
                update_task(
                    task_id,
                    percent,
                    round(speed /(1024 * 1024), 2) if speed else None,
                    eta
                    )
        elif d['status'] == 'finished':
            update_task(task_id, 100)
            complete_task(task_id)
    
    ydl_opts = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
        "merge_output_format": "mp4",
        #"postprocessors": [{
        #    "key": "FFmpegVideoConvertor",
        #    "preferedformat": "mp4"
        #}],
        #"postprocessor_args": [
        #    "-c:v", "copy",
        #    "-c:a", "aac",
        #    "-b:a", "192k"
        #],
        "outtmpl": str(VIDEO_DIR / "%(title)s.%(ext)s"),
        "noplaylist": True,
        "quiet": False,
        "progress_hooks": [progress_hook],
        #"js_runtimes": {
        #    "node": {}
        #},
        #"remote_components": ["ejs:github"],
        #"extractor_args": {
        #    "youtube": {
        #        "player_client": ["web"]
        #    }
        #},
        #"allow_unplayable_formats": True,
        "retries": 10,
        "fragment_retries": 10,
        "socket_timeout": 30,
        "continuedl": True,
        "concurrent_fragment_downloads": 1,
    }


    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
