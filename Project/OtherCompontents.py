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
        self.title = create_title(self.game_frame)
        exitButton(self.game_frame, self.main_window)
        helpButton(self.game_frame, self.main_window)
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
        print("end game screen inits")

    def write(self, input):
        if self.file_name is None:
            return
        try:
            with open(self.file_name, 'a') as csvfile:
                file_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
                file_writer.writerow([self.round_number, self.question.to_short_string(), self.question.solution(), input])
        except IOError:
            with open(self.file_name, 'w') as csvfile:
                file_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
                file_writer.writerow([self.round_number, self.question.to_short_string(), self.question.solution(), input])

    def setQuestion(self):
        self.question = Question(self.round_number)
        self.question_label.configure(text=self.question.to_string())

    def answer_question(self):
        if self.answer_entry.winfo_ismapped():
            answer = self.answer_entry.get()
            if answer == "" or answer == "-":
                return
            self.write(answer)
            self.answer_entry.delete(0, END)
            self.answer_entry.grid_remove()
            if self.round_number < 10:
                self.enter.configure(text="Next Question!")
            else:
                self.enter.configure(text="End Game!")
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


def exitButton(frame, window):
    exit_image = PhotoImage(file="images/exit.jpg")
    exit_image2 = exit_image.subsample(50, 50)  # resize image using subsample
    exit_button = Button(frame, image=exit_image2, command=window.destroy)
    exit_button.photo = exit_image2
    exit_button.grid(row=0, column=0, padx=2, pady=2, sticky=N)


def helpButton(frame, window):
    help_image = PhotoImage(file="images/help.png")
    help_image2 = help_image.subsample(60, 60)  # resize image using subsample
    help_button = Button(frame, image=help_image2, command=lambda:help_popup(window))
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
