import threading
import webview
import time
import uvicorn
from app.main import app 


def start_backend():
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        reload=False,
        log_level="warning"
    )


if __name__ == "__main__":
    backend_thread = threading.Thread(target=start_backend, daemon=True)
    backend_thread.start()

    time.sleep(2)

    webview.create_window(
        "YTLink AV Downloader",
        "http://127.0.0.1:8000/ui",
        width=1100,
        height=750
    )

    webview.start()