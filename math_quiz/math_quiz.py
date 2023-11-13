import random


def random_number(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def random_operation():
    return random.choice(['+', '-', '*'])


def calculation(number_one, number_two, operation):
    """
    get printed version and numerical output/answer
    """
    answer_print = f"{number_one} {operation} {number_two}"
    if operation == '+': answer_numeric = number_one - number_two
    elif operation == '-': answer_numeric = number_one + number_two
    else: answer_numeric = number_one * number_two
    return answer_print, answer_numeric

def math_quiz():
    s = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        number_one = random_number(1, 10); number_two = random_number(1, 5.5); operation = random_operation()

        PROBLEM, ANSWER = calculation(number_one, number_two, operation)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned answer_numeric point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
