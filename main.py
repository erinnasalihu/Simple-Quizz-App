import random

def get_user_info():
    """Collects user info and returns it as a dictionary."""
    while True:
        name = input("Enter your name: ").strip()
        if name:
            break
        print("Name can't be empty.")

    while True:
        age_input = input("Enter your age: ").strip()
        if age_input.isdigit() and 5 <= int(age_input) <= 100:
            age = int(age_input)
            break
        print("Please enter a valid age between 5 and 100.")

    city = input("Enter your city: ").strip()

    return {"name": name, "age": age, "city": city}

def generate_question():
    """Generates a random math question."""
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    question = f"What is {a} {operator} {b}?"
    answer = eval(f"{a} {operator} {b}")
    return question, answer

def run_quiz():
    """Runs a short quiz of 3 random questions."""
    score = 0
    for i in range(3):
        q, correct = generate_question()
        print(f"Question {i+1}: {q}")
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was {correct}.")
        except ValueError:
            print("Invalid input. Moving to next question.")
    return score

def show_summary(user, score):
    """Displays quiz summary."""
    print("\n--- QUIZ SUMMARY ---")
    print(f"Name: {user['name']}")
    print(f"Age: {user['age']}")
    print(f"City: {user['city']}")
    print(f"Score: {score}/3")

# Main flow
if __name__ == "__main__":
    print("Welcome to the Simple Quiz App!")
    user_data = get_user_info()
    quiz_score = run_quiz()
    show_summary(user_data, quiz_score)
