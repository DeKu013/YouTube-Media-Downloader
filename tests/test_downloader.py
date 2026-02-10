from app.services.downloader import download_audio, download_video

TEST_URL = "https://www.youtube.com/watch?v=XIF9GX_6YwM"

print("Downloading audio...")
download_audio(TEST_URL)

print("Downloading video...")
download_video(TEST_URL, resolution="720")
