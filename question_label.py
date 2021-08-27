from tkinter import *


def question_label(text_question, main_window):
    Question_label = Label(main_window, text=text_question, bg="gray", font=("arial", "20", "bold"))
    Question_label.grid(row=0, column=0, sticky="NW", pady=150, padx=50)
