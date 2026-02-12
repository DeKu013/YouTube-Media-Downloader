function resetUI() {
  const bar = document.getElementById("bar");
  const percentText = document.getElementById("percentText");
  const speedText = document.getElementById("speedText");
  const etaText = document.getElementById("etaText");

  bar.style.width = "0%";
  bar.style.background = "linear-gradient(90deg,#22c55e,#16a34a)";
  percentText.innerText = "0%";
  speedText.innerText = "Speed: --";
  etaText.innerText = "ETA: --";
}

async function downloadAudio() {
  startDownload("/download/audio");
}

async function downloadVideo() {
  startDownload("/download/video");
}

async function startDownload(endpoint) {
  const url = document.getElementById("url").value;

  if (!url) {
    alert("Please enter a YouTube URL");
    return;
  }

  resetUI();

  try {
    const res = await fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url })
    });

    const data = await res.json();

    if (!data.task_id) {
      alert("Failed to start download.");
      return;
    }

    pollStatus(data.task_id);

  } catch (error) {
    alert("Error starting download.");
  }
}

async function pollStatus(taskId) {
  const bar = document.getElementById("bar");
  const percentText = document.getElementById("percentText");
  const speedText = document.getElementById("speedText");
  const etaText = document.getElementById("etaText");

  const interval = setInterval(async () => {
    try {
      const res = await fetch(`/status/${taskId}`);
      const data = await res.json();

      if (!data || data.status === "not_found") {
        clearInterval(interval);
        return;
      }

      const progress = data.progress || 0;

      bar.style.width = progress + "%";
      percentText.innerText = progress.toFixed(1) + "%";

      if (data.speed)
        speedText.innerText = "Speed: " + data.speed + " MB/s";

      if (data.eta)
        etaText.innerText = "ETA: " + data.eta + "s";

      if (data.status === "completed") {
        bar.style.background = "#1976d2";
        percentText.innerText = "Completed ✔";
        speedText.innerText = "";
        etaText.innerText = "";
        clearInterval(interval);
      }

    } catch {
      clearInterval(interval);
    }
  }, 1000);
}

async function openDownloads() {
  try {
    await fetch("/downloads");
  } catch {
    alert("Failed to open folder");
  }
}
