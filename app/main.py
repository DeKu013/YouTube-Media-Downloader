import os
import sys
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.routes import router

app = FastAPI(title="YTLink AV Downloader")

app.include_router(router)

if getattr(sys, "frozen", False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

STATIC_DIR = os.path.join(BASE_DIR, "static")

app.mount("/ui", StaticFiles(directory=STATIC_DIR, html=True), name="ui")

@app.get("/")
def root():
    return {"status": "YTLink AV Downloader running"}
