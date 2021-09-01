from Project import helpButton, gameScreen, exitButton, createTitle
from tkinter import *
from datetime import datetime


class Menu:
    def __init__(self, main_window):
        self.main_window = main_window
        # Create Frame inside main window
        self.menu_frame = Frame(self.main_window, width=680, height=405, bg="gray")
        self.menu_frame.grid(row=0, column=0, padx=10, pady=10)
        self.menu_frame.grid_propagate(0)
        self.title = createTitle.create_title(self.menu_frame)

        # Help & Exit buttons
        helpButton.helpButton(self.menu_frame, self.main_window)
        exitButton.exitButton(self.menu_frame, self.main_window)

        # Ask for players name
        self.name_label = Label(self.menu_frame, text="Please enter your name below", fg="white", bg="grey")
        self.name_entry = Entry(self.menu_frame, fg="black", width=10)
        self.name_label.grid(column=3, row=1, columnspan=5, pady=5)
        self.name_entry.grid(column=4, row=2, columnspan=3)
        print("BEFORE")
        # Start Game Button
        self.start = Button(self.menu_frame, text="Start Game", fg="Black", bg="White", command=self.startGame)
        print("MID")
        self.start.grid(column=4, row=4, columnspan=3, pady=(5, 0))
        print("AFTER")
        # Add additional frames for formatting
        self.extra_frame1 = Frame(self.menu_frame, width=200, height=405, bg="grey")
        self.extra_frame1.grid(column=1, row=0, rowspan=10, columnspan=2)
        self.extra_frame2 = Frame(self.menu_frame, width=242, height=405, bg="grey")
        self.extra_frame2.grid(column=9, row=0, rowspan=10)
        self.extra_frame3 = Frame(self.menu_frame, height=205, bg="grey")
        self.extra_frame3.grid(column=10, row=8)

    def close_menu(self):
        self.menu_frame.grid_remove()

    def startGame(self):
        self.close_menu()
        name = self.name_entry.get()
        if name != "":
            filename = name + datetime.now().strftime("%m.%d.%Y,%H,%M,%S") + '.csv'
        else:
            filename = None
        gameScreen.GameScreen(self.main_window, filename)
