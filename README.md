# Quiz Application

This is a simple command-line Python quiz application that allows users to register, login, create quizzes, take quizzes, and display the results. The application is designed to be user-friendly and interactive.

## Features

- User Registration: New users can register with a username and password to create an account.
- User Login: Registered users can log in with their credentials.
- Quiz Creation: Logged-in users can create quizzes by adding questions with multiple-choice options and specifying the correct answer.
- Quiz Taking: Users can choose from available quizzes and take them, answering questions and receiving instant feedback on their answers.
- Quiz Results: After completing a quiz, users will receive their total score.

## How to Use

1. Run the `quiz_app.py` script using Python (e.g., `python quiz_app.py`).
2. Choose from the available options:
   - Register a new account (Option 1) or login (Option 2).
   - Create a quiz (Option 3) if logged in as a registered user.
   - Take a quiz (Option 4) from the available quizzes if logged in.
   - Exit the application (Option 5).
3. If you choose to create a quiz, provide the quiz name and add questions along with multiple-choice options. Indicate the correct option number for each question.
4. If you choose to take a quiz, select a quiz from the list and proceed with answering the questions.

## Note

- The application does not store data permanently. All user accounts and quizzes are stored in memory during the runtime of the program.
- User accounts are case-sensitive, and passwords are stored securely using hashing techniques.

## Requirements

- Python 3.x

## Author

This quiz application was created by [Your Name].

Feel free to explore, modify, and enhance this quiz application according to your requirements. Happy quizzing!
