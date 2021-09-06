"""Menu class, this will create the menu frame to start the game
Name entry plus validation
Joel McKinnon
September 2021
"""
# imports
from Project import helpButton, gameScreen, exitButton, createTitle
from tkinter import *
from datetime import datetime


# class containing menu frame
class Menu:
    def __init__(self, main_window):
        self.main_window = main_window
        # Create Frame inside main window
        self.menu_frame = Frame(self.main_window, width=680, height=405, bg="gray")
        self.menu_frame.grid(row=0, column=0, padx=10, pady=10)
        self.menu_frame.grid_propagate(0)
        self.title = createTitle.create_title(self.menu_frame)
        # Help & Exit buttons
        helpButton.help_button(self.menu_frame, self.main_window)
        exitButton.exitButton(self.menu_frame, self.main_window)
        # Ask for players name and name entry
        self.name_label = Label(self.menu_frame, text="Please enter your name below", fg="white", bg="grey")
        self.name_entry = Entry(self.menu_frame, fg="black", width=10)
        self.name_label.grid(column=3, row=1, columnspan=5, pady=5)
        self.name_entry.grid(column=4, row=2, columnspan=3)
        # Start Game Button
        self.start = Button(self.menu_frame, text="Start Game", fg="Black", bg="White", command=self.start_game)
        self.start.grid(column=4, row=4, columnspan=3, pady=(5, 0))
        # label to make sure users are aware does not save without name
        self.inform = Label(self.menu_frame,
                            text="for answers to save you must entire your name\n otherwise they WILL NOT be saved",
                            fg="white", bg="gray")
        self.inform.grid(row=5, column=3, columnspan=5)
        # Add additional frames for formatting
        self.extra_frame1 = Frame(self.menu_frame, width=200, height=405, bg="grey")
        self.extra_frame1.grid(column=1, row=0, rowspan=10, columnspan=2)
        self.extra_frame2 = Frame(self.menu_frame, width=190, height=405, bg="grey")
        self.extra_frame2.grid(column=8, row=0, rowspan=10)
        self.extra_frame3 = Frame(self.menu_frame, height=205, bg="grey")
        self.extra_frame3.grid(column=10, row=8)
        # validation of name entry
        registration = self.menu_frame.register(self.callback2)
        self.name_entry.config(validate="key", validatecommand=(registration, '%P'))

    # function to close menu
    def close_menu(self):
        self.menu_frame.grid_remove()

    # function to start the quiz
    def start_game(self):
        self.close_menu()
        # getting name from entry box
        name = self.name_entry.get()
        if name != "":
            filename = name + datetime.now().strftime("%m.%d.%Y,%H,%M,%S") + '.csv'  # create filename
        else:
            filename = None
        gameScreen.GameScreen(self.main_window, filename)

    # callback function to validate name entry
    def callback2(self, entry_box):
        name = ["#", "<", "$", "+", "%", ">", "!", "'", '"', "&", "*", "|", "{", "}", "?", "=", "/", ":", "\\", " ",
                "@"]  # list of invalid characters
        for i in name:
            if i in entry_box:
                return False
        return True
