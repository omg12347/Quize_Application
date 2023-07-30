import random

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

class Quiz:
    def __init__(self, quiz_name):
        self.quiz_name = quiz_name
        self.questions = []

    def add_question(self, question, options, correct_answer):
        self.questions.append(Question(question, options, correct_answer))

    def take_quiz(self):
        score = 0
        random.shuffle(self.questions)
        for idx, question in enumerate(self.questions, start=1):
            print(f"\nQuestion {idx}: {question.question}")
            for i, option in enumerate(question.options, start=1):
                print(f"{i}. {option}")

            while True:
                try:
                    user_answer = int(input("Enter the option number of your answer: "))
                    if 1 <= user_answer <= len(question.options):
                        break
                    else:
                        print("Invalid option number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a valid option number.")

            if question.options[user_answer - 1] == question.correct_answer:
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")

        total_questions = len(self.questions)
        print(f"\nYour Score: {score}/{total_questions}")

def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return User(username, password)

def login(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return users.get(username, None) if users else None

def create_quiz():
    quiz_name = input("Enter the quiz name: ")
    quiz = Quiz(quiz_name)

    while True:
        question = input("Enter the question (or type 'done' to finish): ")
        if question.lower() == 'done':
            break

        options = []
        for i in range(4):
            option = input(f"Enter option {i+1}: ")
            options.append(option)

        correct_answer = input("Enter the correct option number (1-4): ")
        quiz.add_question(question, options, options[int(correct_answer) - 1])

    return quiz

def main():
    users = {}
    quizzes = []

    while True:
        print("\n--- Quiz Application ---")
        print("1. Register")
        print("2. Login")
        print("3. Create Quiz")
        print("4. Take Quiz")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user = register()
            users[user.username] = user
            print("Registration successful!")

        elif choice == "2":
            user = login(users)
            if user:
                print(f"Welcome, {user.username}!")
            else:
                print("Invalid username or password. Please try again.")

        elif choice == "3":
            if users:
                if user:
                    quiz = create_quiz()
                    quizzes.append(quiz)
                    print(f"Quiz '{quiz.quiz_name}' created successfully!")
                else:
                    print("Please log in to create a quiz.")
            else:
                print("Please register first to create a quiz.")

        elif choice == "4":
            if users and quizzes:
                if user:
                    print("\nAvailable Quizzes:")
                    for idx, quiz in enumerate(quizzes, start=1):
                        print(f"{idx}. {quiz.quiz_name}")

                    while True:
                        try:
                            quiz_choice = int(input("Enter the quiz number to take: "))
                            if 1 <= quiz_choice <= len(quizzes):
                                break
                            else:
                                print("Invalid quiz number. Please try again.")
                        except ValueError:
                            print("Invalid input. Please enter a valid quiz number.")

                    selected_quiz = quizzes[quiz_choice - 1]
                    print(f"\nYou are about to take the quiz '{selected_quiz.quiz_name}'.")
                    take_quiz = input("Do you want to continue? (yes/no): ")
                    if take_quiz.lower() == 'yes':
                        selected_quiz.take_quiz()
                    else:
                        print("Quiz taking cancelled.")
                else:
                    print("Please log in to take a quiz.")
            else:
                print("No quizzes available. Please create a quiz first.")

        elif choice == "5":
            print("Exiting the Quiz Application...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
