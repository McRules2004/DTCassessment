from Project import createTitle, finalCloseButton, exitButton
from tkinter import *
from datetime import datetime


class Final:
    def __init__(self, main_window, file_name):
        self.file_name = file_name
        self.main_window = main_window
        # Create Frame inside main window
        self.final_frame = Frame(self.main_window, width=680, height=405, bg="gray")
        self.final_frame.grid(row=0, column=0, padx=10, pady=10)
        self.final_frame.grid_propagate(0)
        self.title = createTitle.create_title(self.final_frame)

        # Help & Exit buttons
        finalCloseButton.closeButton(self.final_frame, self.main_window)
        exitButton.exitButton(self.final_frame, self.main_window)

        # Ask for players name
        self.name_label = Label(self.final_frame, text="Thanks for Playing", fg="white", bg="grey")

        if self.file_name is None:
            self.name_label2 = Label(self.final_frame, text=None, fg="white", bg="grey")
        else:
            self.name_label2 = Label(self.final_frame, text="Your Answers have been saved ", fg="white", bg="grey")

        self.name_label.grid(column=3, row=1, columnspan=5, pady=5)
        self.name_label2.grid(column=3, row=2, columnspan=5, pady=5)

        print("BEFORE")
        print("MID")
        print("AFTER")
        # Add additional frames for formatting
        self.extra_frame1 = Frame(self.final_frame, width=200, height=405, bg="grey")
        self.extra_frame1.grid(column=1, row=0, rowspan=10, columnspan=2)
        self.extra_frame2 = Frame(self.final_frame, width=190, height=405, bg="grey")
        self.extra_frame2.grid(column=8, row=0, rowspan=10)
        self.extra_frame3 = Frame(self.final_frame, height=205, bg="grey")
        self.extra_frame3.grid(column=10, row=8)
