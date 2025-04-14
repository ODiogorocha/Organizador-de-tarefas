import json
import os
from task import Task

FILE_PATH = "tasks.json"

def save_tasks(task_list):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump([task.to_dict() for task in task_list], file, ensure_ascii=False, indent=4)

def load_tasks():
    if os.path.exists(FILE_PATH):
        try:
            with open(FILE_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Task.from_dict(item) for item in data]
        except json.JSONDecodeError:
            return []
    else:
        return []

def suggest_next_task(task_list):
    priority_order = ["High", "Medium", "Low"]

    for level in priority_order:
        for task in task_list:
            if task.priority == level:
                return task
    return None
