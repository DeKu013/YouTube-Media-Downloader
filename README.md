## Version: 2.0.0

A lightweight YouTube audio and video downloader built for personal use.

It comes with 2 modes of running:
- A Web client(runs via Pythono)
- A standalone Windows desktop application(EXE application)

## Notable features:
- Download best quality YouTube video available
- Downlaod best quality audio
- Live progress tracking
- Dedicated folder for storing downloaded media, inside 'Documents' folder in the name 'YTLinkDownloads'
- EXE application is completely standalone, no dependency required

## How to use?
1 - Open the file(EXE application/Web client)
2 - The application UI opens
3 - In the blank space, paste the link of the desired Youtube video/audio/short
4 - Click on 'Download Audio' for audio download or 'Download Video' for video download
5 - Progress of the download is displayed live
6 - After successful download, click on 'Open Downloads Folder' to navigate to the downloaded media
7 - Audios are downloaded in 'audio' folder, while videos are downloaded in 'video' folder


## How to download & run?
- Clone the repository via: gh repo clone DeKu013/YouTube-Media-Downloader on Git Bash
  or just download the zip file of the repository and then extract the zip file
For Web client users:
- Open Command Prompt/PowerShell inside the repository folder
- If dependencies aren't installed yet, run: pip install requirements.txt
- When dpendencies are installed, run: python run.py
- This opens the Web client UI
For EXE application users:
- Inside the recently extracted folder open the 'dist' folder
- Double-click on the 'desktop_app.exe' file to open EXE application UI

## Tech stack used:
- Python
- FastAPI
- yt-dlp
- Uvicorn
- HTMl/CSS/JavaScript
- PyInstaller

## Notes:
- Desktop version(EXE application) bundles Python and all dependencies
- Antivirus software may flag unsigned executables
- Internet connection is required for downloads
