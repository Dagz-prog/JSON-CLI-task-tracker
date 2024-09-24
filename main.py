import datetime
import json
import os
from asyncio import tasks


def serialize_datetime(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")

def load_tasks(filename='task.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []

    return []


def save_tasks(tasks, filename='task.json'):
    with open (filename, 'w') as file:
        json.dump(tasks, file, indent=4, default=serialize_datetime)

def delete_task(task_id:int, filename = 'task.json'):
    tasks=load_tasks(filename)
    tasks.pop(task_id-1)
    save_tasks(tasks, filename)
    print(f"Task {task_id} deleted")

def get_next_id(tasks):
    if not tasks:
        return 1
    # Find the maximum ID in the existing tasks and add 1
    max_id = max(task['id'] for task in tasks)
    return max_id + 1



def add_task(title: str,description:str,status:str,filename = 'task.json'):
    tasks = load_tasks(filename)
    task_id = get_next_id(tasks)
    new_task = {
        "id": task_id,
        "title": title,
        "description": description,
        "status": status,
        "createdAt": datetime.datetime.now(),
        "updatedAt": datetime.datetime.now(),
    }
    tasks.append(new_task)
    save_tasks(tasks, filename)
    print(f"Task {task_id} added\n")






def mark_as_done(id,filename = 'task.json'):
    tasks=load_tasks(filename)
    for task in tasks:
        if task['id'] == id:
            task['status'] = "Done"
            task['updatedAt'] = datetime.datetime.now()
            save_tasks(tasks, filename)
            print(f"Task {task['id']} done\n")

def mark_as_in_progress(id,filename = 'task.json'):
    tasks=load_tasks(filename)
    for task in tasks:
        if task['status']== "Done":
            print(f"Task {task['id']} is already done\n")
            return
        if task['id'] == id:
            task['status'] = "In progress"
            task['updatedAt'] = datetime.datetime.now()
            save_tasks(tasks, filename)
            print(f"Task {task['id']} marked as in progress\n")

def print_tasks(tasks: list[dict]):
    for task in tasks:
        print(f"{task['id']}: {task['title']}\n\tDescription: {task['description']}\n\tStatus: {task['status']}")

def print_tasks_in_progress(tasks: list[dict]):
    for task in tasks:
        if task['status'] == "In progress":
            print(f"{task['id']}: {task['title']}\n\tDescription: {task['description']}\n\tStatus: {task['status']}")

def print_tasks_done(tasks: list[dict]):
    for task in tasks:
        if task['status'] == "Done":
            print(f"{task['id']}: {task['title']}\n\tDescription: {task['description']}\n\tStatus: {task['status']}")

def print_tasks_todo(tasks: list[dict]):
    for task in tasks:
        if task['status'] == "todo":
            print(f"{task['id']}: {task['title']}\n\tDescription: {task['description']}\n\tStatus: {task['status']}")

def menu():
    print("*****MENU*****")
    print("1. Add Task")
    print("2. Mark as Done")
    print("3. Mark as in progress")
    print("4. Delete Task")
    print("5. List Task")
    print("6. List todo Tasks")
    print("7. List Done Tasks")
    print("8. List Task In Progress")
    print("9. Exit")

    opt = int(input("\nWhat do yo want to do? "))
    match opt:
        case 1:
            title = input("Add the title of your task: ")
            description = input("What do you want to do? ")
            status = "todo"
            add_task(title,description,status)
            menu()
        case 2:
            task_id = int(input("Task id: "))
            mark_as_done(task_id)
            menu()

        case 3:
            task_id = int(input("Task id: "))
            mark_as_in_progress(task_id)
            menu()
        case 4:
            print("Delete Task")
            del_task = int(input("What do you want to delete? "))
            delete_task(del_task)

            menu()


        case 5:
            print("****ALL TASKS*****")
            print_tasks(load_tasks())
            print("\n")
            menu()

        case 6:
            print("****TODO TASKS*****")
            print_tasks_todo(load_tasks())
            print("\n")
            menu()
            return
        case 7:
            print("****COMPLETED TASKS*****")
            print_tasks_done(load_tasks())
            print("\n")
            menu()
            return
        case 8:
            print("****TASKS IN PROGRESS*****")
            print_tasks_in_progress(load_tasks())
            print("\n")
            menu()
            return


        case 9:
            return






print(f"Welcome to the Task tracker!\n")



menu()







