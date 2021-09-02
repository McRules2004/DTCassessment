"""
question generating component
Joel McKinnon
August 2021
V1
"""
import random

round_number = 3  # testing purposes


def questionGenerating(number):
    unit = ["x", "/", "+", "-"]
    first_digit = random.randint(0, 10)
    second_digit = random.randint(0, 10)
    unit = random.choice(unit)
    if unit == "x":
        question_answer = first_digit * second_digit
    elif unit == "/":
        second_digit += 1
        question_answer = first_digit / second_digit
    elif unit == "+":
        question_answer = first_digit + second_digit
    elif unit == "-":
        question_answer = first_digit - second_digit

    text_question = "Question{}: {} {} {}=".format(number, first_digit, unit, second_digit)
    return text_question, question_answer


text_question, question_answer = questionGenerating(round_number) # running function
print(text_question)
print(question_answer)

