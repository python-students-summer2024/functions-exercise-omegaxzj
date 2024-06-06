import random


def roll_die():
    return random.randint(1, 6)


def get_question_type():
    return "sum" if random.randint(1, 6) <= 3 else "difference"


def print_question(die_1_value, die_2_value, question_type):
    operation = "sum" if question_type == "sum" else "difference"
    noun ="of" if operation=="sum" else "between"
    question = f"You rolled a {die_1_value} and a {die_2_value}... What is the {operation} {noun} {die_1_value} and {die_2_value}?"
    print(question)


def input_answer():
    answer = input("Enter your answer: ").strip()
    return int(answer) if answer.isdigit() else -1


def is_correct_answer(die_1_value, die_2_value, question_type, given_answer):
    correct_answer = die_1_value + die_2_value if question_type == "sum" else abs(die_1_value - die_2_value)
    return given_answer == correct_answer


def print_congratulations(question_type):
    if question_type == "sum":
        print("Yes! Congratulations on the successful addition!")
    else:
        print("Yes! Congratulations on the successful subtraction!")


def print_correct_answer(die_1_value, die_2_value, question_type):
    correct_answer = die_1_value + die_2_value if question_type == "sum" else abs(die_1_value - die_2_value)
    answer_text = "sum" if question_type == "sum" else "difference"
    noun ="of" if answer_text=="sum" else "between"
    print(f"No! The {answer_text} {noun} {die_1_value} and {die_2_value} is {correct_answer}!")


def print_error_message():
    print("Sorry - that is an invalid answer.  Bye Bye!")
