from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.routes import router

app = FastAPI(title="YTLink AV Downloader")

# API
app.include_router(router)

# UI
app.mount("/ui", StaticFiles(directory="app/static", html=True), name="ui")

@app.get("/")
def root():
    return {"status": "YTLink AV Downloader running"}
