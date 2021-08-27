""" layout
26th July
Joel McKinnon
"""

# import tkinter and all its functions
from tkinter import *
import csv
from datetime import datetime
import random

global round_number
# name input,
# getting the date and time of the quiz taking place
now = datetime.now()
dt = now.strftime('%d_%m_%y%H_%M_%S')
# name input set as a string
filename = str(input("Name of file: "))
# concatenation to form file name containing name, date and time
full_path = filename + str(dt) + ".csv"
roundNumber = 0
with open(full_path, 'w') as csvfile:
    file_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

    # set headers in files (name, question, correct answer, inputted answer)
    file_writer.writerow(['QuestionNumber', 'Question', 'Correct Answer', 'Inputted Answer'])


    class Help:
        def __init__(self):
            background = "gray"
            # making a popup and removing the main window
            self.help_box = Toplevel()
            self.help_box.title("Help")
            main_window.withdraw()
            self.help_box.protocol('WM_DELETE_WINDOW', self.close_help)
            question_mark.config(state=DISABLED)

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
            self.exit_help_image = PhotoImage(file="exit.jpg")
            self.forth_image = self.exit_help_image.subsample(50, 50)  # resize image using subsample
            self.close_button = Button(self.help_frame, image=self.forth_image,
                                       command=self.close_help).grid(row=0, pady=5,
                                                                     padx=5, sticky=NW)

            # function to close help popup

        def close_help(self):
            question_mark.config(state=NORMAL)  # turning help button on
            main_window.deiconify()  # making main window visible
            self.help_box.destroy()


    # help box popup
    def help_popup():
        get_help = Help()
        get_help.help_text.configure(text="Help Text Here",
                                     fg="white", font=("arial", "14"))


    class Menu:
        def __init__(self):
            background = "gray"
            # making a popup and removing the main window
            self.menu_box = Toplevel()
            self.menu_box.title("Menu")
            main_window.withdraw()
            self.menu_box.protocol('WM_DELETE_WINDOW', self.close_menu)
            question_mark.config(state=DISABLED)

            # design for the popup
            self.menu_frame = Frame(self.menu_box, width=600, height=200, bg=background)
            self.menu_frame.grid()
            self.how_heading = Label(self.menu_frame, text="Maths Quiz",
                                     font="arial 20 bold underline", bg=background, fg="black")
            self.how_heading.grid(row=0)
            self.menu_text = Label(self.menu_frame, text="", justify=LEFT,
                                   width=40, bg=background, wrap=250)
            self.menu_text.grid(row=1, )

            # close the popup button making
            self.exit_menu_image = PhotoImage(file="exit.jpg")
            self.fifth_image = self.exit_menu_image.subsample(50, 50)  # resize image using subsample
            self.close_button = Button(self.menu_frame, image=self.fifth_image,
                                       command=self.close_menu).grid(row=0, pady=5,
                                                                     padx=5, sticky=NW)

            # function to close help popup

        def close_menu(self):
            question_mark.config(state=NORMAL)  # turning help button on
            main_window.deiconify()  # making main window visible
            self.menu_box.destroy()

    # help box popup
    def menu_popup():
        get_menu = Menu()
        get_menu.menu_text.configure(text="MenuText Here",
                                     fg="white", font=("arial", "14"))


    def questionGenerating(number):
        Units = ["x", "+", "-"]
        first_digit = random.randint(0, 10)
        second_digit = random.randint(0, 10)
        unit = random.choice(Units)
        if unit == "x":
            question_answer = first_digit * second_digit
        elif unit == "+":
            question_answer = first_digit + second_digit
        elif unit == "-":
            question_answer = first_digit - second_digit
        #print(question_answer)
        text_question = "Question {}: {} {} {} =".format(number, first_digit, unit, second_digit)
        question_short = "{} {} {}".format(first_digit, unit, second_digit)
        return text_question, question_answer, question_short


    def callback(input):
        if input.isdigit():
            return True
        elif input.startswith("-"):
            return True
        elif input == "":
            return True
        return False


    def question_running(rounds):
        question, answer, question_short = questionGenerating(rounds)
        Question_label = Label(main_window, text=question, bg="gray", font=("arial", "20", "bold"))
        Question_label.grid(row=0, column=0, sticky="NW", pady=150, padx=50)
        input4 = Entry(main_window)
        input4.grid(row=0, column=0, sticky=N, pady=150, padx=250)
        removal = Button(main_window, text="Enter", width=10, command=lambda: check(input4, answer, removal, question_short))
        removal.grid(row=0, column=0)
        print(question)
        reg = main_window.register(callback)
        input4.config(validate="key", validatecommand=(reg, '%P'))


    def check(input1, answer, removal, question):
        main_frame.grid(row=0, column=0, padx=45, pady=10)
        removal.grid_remove()
        get = float(input1.get())
        input1.destroy()
        answer = float(answer)
        print(get)
        print("answer", answer)
        inform = Label(text=answer, bg="gray", font="arial 16 bold")
        inform.grid(row=0, column=0, sticky=N, pady=152, padx=250)
        if get == answer:
            print("correct")
            incorrect("Correct", "Green")
        else:
            print("incorrect")
            incorrect("Incorrect", "Red")
        number = round_number - 1
        file_writer.writerow([number, question, answer, get])
        main_text.grid(row=0, column=0, sticky="SE", pady=100, padx=100)

    def incorrect(yes, colour):
        statement = Label(main_window, width=10, text=yes, bg="gray", fg=colour, font="arial 20 bold")
        statement.grid(row=0, column=0, pady=5)

    def next_question():
        global round_number
        main_text.grid_forget()
        if round_number > 10:
            main_text.grid_remove()
            print("yo")
            finish = Label(main_window, text="Thanks for Playing, results have been saved")
            finish.grid(row=0, column=0, sticky=N, pady=85)
            return
        question_running(round_number)

        round_number += 1


    # generate GUI
    # creating and designing main window
    main_window = Tk()
    main_window.geometry("700x425")
    # create main window
    main_window.title("Maths Quiz")
    main_window.config(bg="black")
    main_window.resizable(False, False)

    # Create Frame inside main window
    main_frame = Frame(main_window, width=600, height=400, bg="gray")
    main_frame.grid(row=0, column=0, padx=10, pady=10)

    # help button
    help_image = PhotoImage(file="help.png")
    secondary_image = help_image.subsample(60, 60)  # resize image using subsample
    question_mark = Button(main_window, image=secondary_image, command=help_popup)
    question_mark.grid(row=0, column=0, pady=15, sticky=SE, padx=15)

    # creating frame for the title design
    title_frame = Frame(main_window, width=580, height=50, bg="white")
    title_frame.grid(row=0, column=0, padx=10, sticky=N, pady=20)
    # title text
    Title = Label(main_window, text="Maths Quiz", font="Times 30 italic bold", fg="blue")
    Title.grid(row=0, column=0, sticky=N, pady=25)

    # image for title
    image = PhotoImage(file="quiz.png")
    original_image = image.subsample(17, 17)  # resize image using subsample
    Label(main_window, image=original_image).grid(row=0, column=0, pady=20.5, sticky=NE, padx=70)

    # close window button
    exit_image = PhotoImage(file="exit.jpg")
    third_image = exit_image.subsample(50, 50)  # resize image using subsample
    Button(main_window, image=third_image, command=main_window.destroy).grid(row=0, column=0,
                                                                             pady=10, sticky=NW, padx=10)
    round_number = 1

    main_text = Button(main_window, text="Next Question", command=lambda: next_question())
    main_text.grid(row=0, column=0, sticky="SE", pady=100, padx=100)
    next_question()

    menu_popup()

    # open and save csv file under the user name then time opened.

    # Game loop

    main_window.mainloop()
