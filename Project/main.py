"""
Joel Mckinnon
August 2021
Main Code
V2
"""

from tkinter import *
import csv
from question import Question

class Help:
    def __init__(self, main_window):
        self.main_window = main_window
        background = "grey"
        # making a popup and removing the main window
        self.help_box = Toplevel()
        self.help_box.title("Help")
        main_window.withdraw()
        self.help_box.protocol('WM_DELETE_WINDOW', self.close_help)

        # design for the popup
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()
        self.how_heading = Label(self.help_frame, text="Help/Instructions",
                                 font="arial 20 bold underline", bg=background, fg="black")
        self.how_heading.grid(row=0)
        self.help_text = Label(self.help_frame, text="", justify=LEFT,
                               width=40, bg=background, wrap=250)
        self.help_text.grid(row=1, )

        # close the popup button making
        self.exit_help_image = PhotoImage(file="../Project/images/exit.jpg")
        self.forth_image = self.exit_help_image.subsample(50, 50)  # resize image using subsample
        self.close_button = Button(self.help_frame, image=self.forth_image,
                                   command=self.close_help).grid(row=0, pady=5,
                                                                 padx=5, sticky=NW)

    # function to close help popup
    def close_help(self):
        self.main_window.deiconify()  # making main window visible
        self.help_box.destroy()

class GameScreen:
    def __init__(self, main_window, file_name):
        self.file_name = file_name
        self.round_number = 1
        self.question = None
        self.main_window = main_window
        # Create Frame inside main window
        self.game_frame = Frame(main_window, width=680, height=405, bg="gray")
        self.game_frame.grid(row=0, column=0, padx=10, pady=10)
        self.game_frame.grid_propagate(0)
        # Add title, exit button and help button
        self.title = create_title(self.game_frame)
        exitButton(self.game_frame)
        helpButton(self.game_frame)
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
        self.extra_frame2 = Frame(self.game_frame, width=242, height=405, bg="grey")
        self.extra_frame2.grid(column=9, row=0, rowspan=10)
        self.extra_frame3 = Frame(self.game_frame, height=205, bg="grey")
        self.extra_frame3.grid(column=10, row=8)
        registration = self.game_frame.register(self.callback)
        self.answer_entry.config(validate="key", validatecommand=(registration, '%P'))
        self.setQuestion()

    def setQuestion(self):
        self.question = Question(self.round_number)
        self.question_label.configure(text=self.question.to_string())

    def answer_question(self):
        if self.answer_entry.winfo_ismapped():
            answer = self.answer_entry.get()
            if answer == "" or answer == "-":
                return
            self.answer_entry.delete(0, END)
            self.answer_entry.grid_remove()
            self.enter.configure(text="Next Question!")
            self.answer_label.grid()
            if self.question.checks(answer): #true/correct
                self.answer_label.configure(text="Correct!", fg="green")
            else:
                self.answer_label.configure(text="Incorrect!", fg="red")
        else:
            self.round_number += 1
            if self.round_number > 10:
                self.game_frame.destroy()
                return
            self.setQuestion()
            self.answer_entry.grid()
            self.answer_label.grid_remove()
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

# help box popup
def help_popup(window):
    get_help = Help(window)
    get_help.help_text.configure(text="Help Text Here",
                                 fg="white", font=("arial", "14"))


def exitButton(frame):
    exit_image = PhotoImage(file="images/exit.jpg")
    exit_image2 = exit_image.subsample(50, 50)  # resize image using subsample
    exit_button = Button(frame, image=exit_image2, command=main_window.destroy)
    exit_button.photo = exit_image2
    exit_button.grid(row=0, column=0, padx=2, pady=2, sticky=N)


def helpButton(frame):
    help_image = PhotoImage(file="images/help.png")
    help_image2 = help_image.subsample(60, 60)  # resize image using subsample
    help_button = Button(frame, image=help_image2, command=lambda:help_popup(main_window))
    help_button.photo = help_image2
    help_button.grid(row=9, column=10)


def create_title(frame):
    title_image = PhotoImage(file="images/quiz.png")
    title_image2 = title_image.subsample(17, 17)  # resize image using subsample
    title = Label(frame, image=title_image2, text="Maths Quiz", font="Times 30 italic bold", fg="blue",
                  compound=RIGHT)
    title.photo = title_image2
    title.grid(row=0, column=3, columnspan=5, pady=(10, 0))
    return title


def createMenu(main_window):
    # Create Frame inside main window
    menu_frame = Frame(main_window, width=680, height=405, bg="gray")
    menu_frame.grid(row=0, column=0, padx=10, pady=10)
    menu_frame.grid_propagate(0)

    title = create_title(menu_frame)

    # Help & Exit buttons
    helpButton(menu_frame)
    exitButton(menu_frame)

    # Ask for players name
    name_label = Label(menu_frame, text="Please enter your name below", fg="white", bg="grey")
    name_entry = Entry(menu_frame, fg="black", width=10)
    name_label.grid(column=3, row=1, columnspan=5, pady=5)
    name_entry.grid(column=4, row=2, columnspan=3)

    # Start Game Button
    start = Button(menu_frame, text="Start Game", fg="Black", bg="White", command=lambda:startGame(menu_frame, main_window))
    start.grid(column=4, row=4, columnspan=3, pady=(5, 0))

    # Add additional frames for formatting
    extra_frame1 = Frame(menu_frame, width=200, height=405, bg="grey")
    extra_frame1.grid(column=1, row=0, rowspan=10, columnspan=2)
    extra_frame2 = Frame(menu_frame, width=242, height=405, bg="grey")
    extra_frame2.grid(column=9, row=0, rowspan=10)
    extra_frame3 = Frame(menu_frame, height=205, bg="grey")
    extra_frame3.grid(column=10, row=8)

    return menu_frame

def close_menu(menu):
    menu.destroy()

def startGame(menu, main_window):
    close_menu(menu)
    file_name = "text.csv"
    GameScreen(main_window, file_name)

# create GUI
main_window = Tk()
main_window.geometry("700x425")
# create main window
main_window.title("Maths Quiz")
main_window.config(bg="black")
main_window.resizable(False, False)

menu = createMenu(main_window)

main_window.mainloop()
