import hashlib
import os
import json
import datetime


class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]

    def update_task(self, task_index, updated_task):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index] = updated_task


class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def save_users(users):
    with open('users.json', 'w') as f:
        json.dump(users, f, indent=2)


def load_users():
    if os.path.exists('users.json'):
        with open('users.json', 'r') as f:
            return json.load(f)
    else:
        return {}


def register():
    while True:
        username = input("Enter a username: ")
        password = input("Enter a password: ")

        if username and password:
            users = load_users()
            if username in users:
                print("Username already exists. Try a different one.")
            else:
                user = User(username, password)
                users[username] = {
                    "password_hash": user.password_hash,
                    "tasks": []
                }
                save_users(users)
                print("Registration successful.")
                break
        else:
            print("Please enter a valid username and password.")


def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username and password:
            users = load_users()
            if username in users and users[username]["password_hash"] == hashlib.sha256(password.encode()).hexdigest():
                user = User(username, password)
                user.tasks = [Task(**task) for task in users[username]["tasks"]]
                print(f"Welcome back, {username}!")
                return user
            else:
                print("Invalid username or password. Please try again.")
        else:
            print("Please enter a valid username and password.")


def add_task(user):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    try:
        due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    task = Task(title, description, due_date)
    user.add_task(task)
    save_users(users)


def delete_task(user):
    if not user.tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(user.tasks):
        print(f"{index + 1}. {task.title} (Due: {task.due_date})")

    task_index = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_index < len(user.tasks):
        user.delete_task(task_index)
        save_users(users)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")


def update_task(user):
    if not user.tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(user.tasks):
        print(f"{index + 1}. {task.title} (Due: {task.due_date})")

    task_index = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_index < len(user.tasks):
        title = input("Enter updated task title: ")
        description = input("Enter updated task description: ")
        due_date = input("Enter updated due date (YYYY-MM-DD): ")

        try:
            due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

        updated_task = Task(title, description, due_date)
        user.update_task(task_index, updated_task)
        save_users(users)
        print("Task updated successfully.")
    else:
        print("Invalid task number.")


def display_tasks(user):
    if not user.tasks:
        print("No tasks found.")
        return

    print("Your Task List:")
    for index, task in enumerate(user.tasks, start=1):
        print(f"{index}. {task.title} (Due: {task.due_date})")


def task_reminder(user):
    today = datetime.datetime.now().date()
    reminder_tasks = [task for task in user.tasks if task.due_date.date() == today]

    if not reminder_tasks:
        print("No tasks due today.")
        return

    print("🔔 Today's Task Reminder 🔔")
    for task in reminder_tasks:
        print(f"Task: {task.title} (Due: {task.due_date})")


if __name__ == "__main__":
    users = load_users()

    while True:
        clear_screen()

        print("Welcome to Daily Task Scheduler!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            while user:
                clear_screen()
                print("Welcome to Daily Task Scheduler!")
                print("1. Add Task")
                print("2. Delete Task")
                print("3. Update Task")
                print("4. View Tasks")
                print("5. Task Reminder")
                print("6. Logout")

                choice = input("Enter your choice: ")

                if choice == "1":
                    add_task(user)
                elif choice == "2":
                    delete_task(user)
                elif choice == "3":
                    update_task(user)
                elif choice == "4":
                    display_tasks(user)
                elif choice == "5":
                    task_reminder(user)
                elif choice == "6":
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "3":
            print("Thank you for using Daily Task Scheduler. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
