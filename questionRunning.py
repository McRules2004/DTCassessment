from question_label import question_label
from tkinter import *

import random


# function to generate random question
def questionGenerating(number):
    Units = ["x", "/", "+", "-"]
    first_digit = random.randint(0, 10)
    second_digit = random.randint(0, 10)
    unit = random.choice(Units)
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


def question_running(main_window):
    round_number = 0
    question, answer = questionGenerating(round_number)
    Question_label = Label(main_window, text=question, bg="gray", font=("arial", "20", "bold"))
    Question_label.grid(row=0, column=0, sticky="NW", pady=150, padx=50)

    print (question)
