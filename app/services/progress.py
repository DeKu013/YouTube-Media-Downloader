tasks = {}

def create_task(task_id: str):
    tasks[task_id] = {
        "status": "downloading",
        "progress": 0,
        "speed": None,
        "eta": None
    }

def update_task(task_id: str, progress: float, speed=None, eta=None):
    if task_id in tasks:
        tasks[task_id]["progress"] = progress
        tasks[task_id]["speed"] = speed
        tasks[task_id]["eta"] = eta

def complete_task(task_id: str):
    if task_id in tasks:
        tasks[task_id]["status"] = "completed"
        tasks[task_id]["progress"] = 100

def get_task(task_id: str):
    return tasks.get(task_id, {"status": "not_found"})
