from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = []

# -------------------------
# ADD TASK
# -------------------------
def add_task(title, description, due_date):
    if not validate_task_title(title):
        raise ValueError

    if not validate_task_description(description):
        raise ValueError

    if not validate_due_date(due_date):
        raise ValueError

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    return task


# -------------------------
# MARK TASK AS COMPLETE
# -------------------------
def mark_task_as_complete(index, tasks_list=None):
    if tasks_list is None:
        tasks_list = tasks

    if index < 0 or index >= len(tasks_list):
        raise ValueError

    tasks_list[index]["completed"] = True
    return tasks_list[index]


# -------------------------
# VIEW PENDING TASKS
# -------------------------
def view_pending_tasks(tasks_list=None):
    if tasks_list is None:
        tasks_list = tasks

    return [
        task for task in tasks_list
        if not task["completed"]
    ]


# -------------------------
# CALCULATE PROGRESS
# -------------------------
def calculate_progress(tasks_list=None):
    if tasks_list is None:
        tasks_list = tasks

    if len(tasks_list) == 0:
        return 0

    completed = sum(1 for task in tasks_list if task["completed"])
    return (completed / len(tasks_list)) * 100