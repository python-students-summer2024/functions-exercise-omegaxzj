import app_functions


def main():
    print("Welcome to the Math App!!!")
    print("")

    die1 = app_functions.roll_die()
    die2 = app_functions.roll_die()

    question_type = app_functions.get_question_type()

    app_functions.print_question(die1, die2, question_type)

    user_answer = app_functions.input_answer()

    if user_answer == -1:
        app_functions.print_error_message()
    elif app_functions.is_correct_answer(die1, die2, question_type, user_answer):
        app_functions.print_congratulations(question_type)
    else:
        app_functions.print_correct_answer(die1, die2, question_type)

    print("")
    print("Game over!!!")
    print("Thank you for playing!!!\n")


if __name__ == "__main__":
    main()
