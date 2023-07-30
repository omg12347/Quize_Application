# Daily Task Scheduler

Daily Task Scheduler is a simple command-line application that helps you manage your daily tasks efficiently. With this task scheduler, you can create, update, and delete tasks, set due dates, and receive daily reminders of tasks that are due on the current day.

## Features

- User Registration: Create a new account to start managing your tasks.
- User Login: Existing users can log in to access their task lists.
- Add Task: Easily add new tasks with a title, description, and due date.
- Delete Task: Remove completed or unnecessary tasks from your list.
- Update Task: Modify task details or change the due date of existing tasks.
- View Tasks: Display a list of all tasks associated with your account.
- Task Reminder: Get daily reminders of tasks due on the current day.
- User Logout: Securely log out of your account to protect your tasks.

## How to Use

1. **Register**: Start by registering your account. Choose a unique username and a strong password. If you already have an account, you can skip this step.

2. **Login**: If you are a registered user, log in using your credentials to access your tasks.

3. **Main Menu**: After logging in, you will be directed to the main menu. From here, you can choose various actions to manage your tasks effectively.

4. **Add Task**: Select option "1" to add a new task. Enter the title, description, and due date (in the format YYYY-MM-DD) for the new task.

5. **Delete Task**: To remove a task from your list, choose option "2". You will see a list of all your tasks with numbers. Enter the number corresponding to the task you want to delete.

6. **Update Task**: Select option "3" to update an existing task. Enter the task number you want to update and provide the new title, description, and due date (in the format YYYY-MM-DD) for the task.

7. **View Tasks**: To view all your tasks, select option "4". The tasks will be displayed with their titles and due dates.

8. **Task Reminder**: Choose option "5" to get reminders for tasks that are due today. The application will show you the tasks with their titles and due dates.

9. **Logout**: When you are done managing your tasks, select option "6" to securely log out of your account.

## Dependencies

This project uses Python and requires no external libraries apart from those provided in the standard Python library. The project uses `hashlib` for password hashing and `datetime` for managing task due dates.

## Installation

1. Clone the repository or download the source code.
2. Make sure you have Python installed on your system (Python 3.6 or higher is recommended).
3. Run the `task_scheduler.py` script using the following command:

```bash
python task_scheduler.py
```

## Feedback and Contributions

Your feedback and contributions are highly appreciated. If you encounter any issues, have suggestions, or want to contribute to the project, feel free to create a pull request or open an issue on GitHub.

Let Daily Task Scheduler help you stay organized and on top of your daily tasks! Happy task scheduling! 😊
