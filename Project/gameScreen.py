from tkinter import *
import csv
from Project import question, help, createTitle, exitButton, helpButton, final
import os


class GameScreen:
    def __init__(self, main_window, file_name):
        print("start game screen init")
        self.file_name = file_name
        self.round_number = 1
        self.question = None
        self.main_window = main_window
        # Create Frame inside main window
        self.game_frame = Frame(main_window, width=680, height=405, bg="gray")
        self.game_frame.grid(row=0, column=0, padx=10, pady=10)
        self.game_frame.grid_propagate(0)
        # Add title, exit button and help button
        self.title = createTitle.create_title(self.game_frame)
        exitButton.exitButton(self.game_frame, self.main_window)
        helpButton.helpButton(self.game_frame, self.main_window)
        # Question label
        self.question_label = Label(self.game_frame, text=self.question, fg="white", bg="grey")
        self.question_label.grid(column=3, row=1, columnspan=5, pady=5)
        self.answer_entry = Entry(self.game_frame, fg="black", width=10)
        self.answer_entry.grid(column=4, row=2, columnspan=3)
        self.answer_label = Label(self.game_frame, text="empty", fg="white", bg="grey", width=10)
        self.answer_label.grid(column=4, row=2, columnspan=3)
        self.answer_label.grid_remove()
        # Button
        self.enter = Button(self.game_frame, text="Enter", fg="Black", bg="White", command=self.answer_question)
        self.enter.grid(column=4, row=4, columnspan=3, pady=(5, 0))
        # Add additional frames for formatting
        self.extra_frame1 = Frame(self.game_frame, width=200, height=405, bg="grey")
        self.extra_frame1.grid(column=1, row=0, rowspan=10, columnspan=2)
        self.extra_frame2 = Frame(self.game_frame, width=190, height=405, bg="grey")
        self.extra_frame2.grid(column=8, row=0, rowspan=10)
        self.extra_frame3 = Frame(self.game_frame, height=205, bg="grey")
        self.extra_frame3.grid(column=10, row=8)
        registration = self.game_frame.register(self.callback)
        self.answer_entry.config(validate="key", validatecommand=(registration, '%P'))
        self.correct_answer = Label(self.game_frame, text=None, fg="white", bg="gray")
        self.setQuestion()
        print("end game screen inits")

    def write(self, input):
        if self.file_name is None:
            return
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as csvfile:
                file_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
                file_writer.writerow(['QuestionNumber', 'Question', 'Correct Answer', 'Inputted Answer'])

        with open(self.file_name, 'a') as csvfile:
            file_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

            file_writer.writerow(
                [self.round_number, self.question.to_short_string(), self.question.solution(), input])

    def setQuestion(self):
        self.question = question.Question(self.round_number)
        self.question_label.configure(text=self.question.to_string())

    def answer_question(self):
        if self.answer_entry.winfo_ismapped():
            answer = self.answer_entry.get()
            if answer == "" or answer == "-":
                return
            self.write(answer)
            self.answer_entry.delete(0, END)
            self.answer_entry.grid_remove()
            self.correct_answer.configure(text=self.question.solution())
            self.correct_answer.grid(column=6, row=1, sticky=E)
            if self.round_number < 10:
                self.enter.configure(text="Next Question!")
            else:
                self.enter.configure(text="End Game!")
            self.answer_label.grid()
            if self.question.checks(answer):  # true/correct
                self.answer_label.configure(text="Correct!", fg="green")
            else:
                self.answer_label.configure(text="Incorrect!", fg="red")
        else:
            self.round_number += 1
            if self.round_number > 10:
                self.game_frame.destroy()
                final.Final(self.main_window, self.file_name)
                return
            self.setQuestion()
            self.answer_entry.grid()
            self.answer_label.grid_remove()
            self.correct_answer.grid_remove()
            self.enter.configure(text="Enter")

    def callback(self, input):
        if input.isdigit():
            return True
        elif input.startswith("--"):
            return False
        elif input.startswith("-"):
            return True
        elif input == "":
            return True
        return False
