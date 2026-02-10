from pathlib import Path
import yt_dlp

# Base download directory (safe location)
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DOWNLOADS_DIR = BASE_DIR / "downloads"
AUDIO_DIR = DOWNLOADS_DIR / "audio"
VIDEO_DIR = DOWNLOADS_DIR / "video"

# Ensure folders exist
AUDIO_DIR.mkdir(parents=True, exist_ok=True)
VIDEO_DIR.mkdir(parents=True, exist_ok=True)


def download_audio(url: str, quality: str = "192"):
    """
    Download audio from YouTube and convert to MP3
    """
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": str(AUDIO_DIR / "%(title)s.%(ext)s"),
        "noplaylist": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": quality,
            }
        ],
        "quiet": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_video(url: str, resolution: str = "best"):
    """
    Download video from YouTube and merge audio + video into MP4
    """
    if resolution == "best":
        format_selector = "bv*+ba/b"
    else:
        format_selector = f"bv*[height<={resolution}]+ba/b"

    ydl_opts = {
        "format": format_selector,
        "merge_output_format": "mp4",
        "outtmpl": str(VIDEO_DIR / "%(title)s.%(ext)s"),
        "noplaylist": True,
        "quiet": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
