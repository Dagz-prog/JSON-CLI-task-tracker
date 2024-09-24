# JSON CLI Task Tracker


# Task Tracker

This is a simple Python-based task tracker that allows you to manage your tasks, save them to a JSON file, and mark them as done, in progress, or to-do. You can also delete tasks and list them by their status.

## Features
- Add tasks with a title, description, and status
- Mark tasks as done or in progress
- Delete tasks by their ID
- List all tasks, tasks in progress, tasks that are done, or tasks still to-do
- Tasks are saved to a `task.json` file in the project directory

## Installation
1. Clone the repository or download the project files.
   
   ```bash
   git clone https://github.com/your-username/JSON_TaskTracker.git
   cd JSON_TaskTracker
   ```

2. Ensure you have Python 3 installed. You can verify this with:
   ```bash
   python --version
   ```

3. No external dependencies are required, only the standard library is used.

## Usage

1. **Run the script**:
   ```bash
   python task_tracker.py
   ```

2. Once the program starts, you will be greeted with a menu:

   ```
   *****MENU*****
   1. Add Task
   2. Mark as Done
   3. Mark as in Progress
   4. Delete Task
   5. List All Tasks
   6. List Todo Tasks
   7. List Done Tasks
   8. List Tasks in Progress
   9. Exit
   ```

3. **Add a task**:
   - Choose option 1 to add a new task.
   - You will be prompted for a title and description.
   - The task will be added with a default status of "todo."

4. **Mark a task as done**:
   - Choose option 2 and provide the task ID to mark it as done.

5. **Mark a task as in progress**:
   - Choose option 3 and provide the task ID to mark it as "in progress."

6. **Delete a task**:
   - Choose option 4 and provide the task ID to delete it.

7. **List tasks**:
   - Option 5 lists all tasks.
   - Option 6 lists tasks with the status "todo."
   - Option 7 lists tasks that are marked "done."
   - Option 8 lists tasks marked as "in progress."

8. **Exit**:
   - Choose option 9 to exit the program.

## Task JSON Structure

Tasks are stored in a `task.json` file in the following structure:

```json
[
    {
        "id": 1,
        "title": "Example Task",
        "description": "Task description goes here",
        "status": "todo",
        "createdAt": "2023-09-24T10:00:00",
        "updatedAt": "2023-09-24T10:00:00"
    }
]
```

## Example Workflow

1. **Adding a Task**:
   ```bash
   Add the title of your task: Buy groceries
   What do you want to do? Purchase vegetables, fruits, and milk
   Task 1 added
   ```

2. **Marking a Task as Done**:
   ```bash
   Task id: 1
   Task 1 done
   ```

3. **Listing All Tasks**:
   ```
   ****ALL TASKS*****
   1: Buy groceries
      Description: Purchase vegetables, fruits, and milk
      Status: Done
   ```

# Project URL
https://roadmap.sh/projects/task-tracker
