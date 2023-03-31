#Quiz Game: Build a quiz game that allows users to answer multiple-choice questions and keeps track of their score. You can use a predefined set of questions and answers and store them in a text file or a database.
import random

# Quiz questions and answers
questions = {
    "Which is the capital state of South Korea?": {
        "a": "Seoul",
        "b": "Beijing",
        "c": "Chennai"
    },
    "Which is the nearest planet to sun?": {
        "a": "Mars",
        "b": "Earth",
        "c": "Venus"
    },
    "Who painted Monalisa?": {
        "a": "Leonardo da Vinci",
        "b": "Vincent van Gogh",
        "c": "Pablo Picasso"
    }
}

# Function to display a question and its multiple-choice answers
def ask_question(question, answer_choices):
    print(question)
    for choice in answer_choices:
        print(f"{choice}: {answer_choices[choice]}")
    user_answer = input("Enter your answer (a, b, or c): ")
    return user_answer

# Function to check if the user's answer is correct
def check_answer(question, user_answer):
    correct_answer = questions[question]["a"]
    if user_answer == "a":
        print("Correct!")
        return True
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")
        return False

# Main function to run the quiz game
def play_quiz():
    score = 0
    random_questions = list(questions.keys())
    random.shuffle(random_questions)
    for question in random_questions:
        user_answer = ask_question(question, questions[question])
        if check_answer(question, user_answer):
            score += 1
    print(f"Your score is {score}/{len(questions)}")

# Run the quiz game
play_quiz()
