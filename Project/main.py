"""
Joel Mckinnon
August 2021
Main Code
V2
"""

from tkinter import *

def exitButton(frame):
    exit_image = PhotoImage(file="images/exit.jpg")
    exit_image2 = exit_image.subsample(50, 50)  # resize image using subsample
    exit_button = Button(frame, image=exit_image2, command=main_window.destroy)
    exit_button.photo = exit_image2
    exit_button.grid(row=0, column=0, padx=2, pady=2, sticky=N)

def helpButton(frame):
    help_image = PhotoImage(file="images/help.png")
    help_image2 = help_image.subsample(60, 60)  # resize image using subsample
    help_button = Button(frame, image=help_image2)#, command=help_popup)
    help_button.photo = help_image2
    help_button.grid(row=10, column=10)

def createMenu(main_window):
    # Create Frame inside main window
    menu_frame = Frame(main_window, width=680, height=405, bg="gray")
    menu_frame.grid(row=0, column=0, padx=10, pady=10)
    menu_frame.grid_propagate(0)

    # title
    title_image = PhotoImage(file="images/quiz.png")
    title_image2 = title_image.subsample(17, 17)  # resize image using subsample
    title = Label(menu_frame, image=title_image2, text="Maths Quiz", font="Times 30 italic bold", fg="blue", compound=RIGHT)
    title.photo = title_image2
    title.grid(row=0, column=3, columnspan=5, pady=(10, 0))

    # Help & Exit buttons
    helpButton(menu_frame)
    exitButton(menu_frame)

    # Ask for players name
    name_label = Label(menu_frame, text="Please enter your name below", fg="white", bg="grey")
    name_entry = Entry(menu_frame, fg="black", width=10)
    name_label.grid(column=3, row=1, columnspan=5, pady=5)
    name_entry.grid(column=4, row=2, columnspan=3)

    # Start Game Button
    start = Button(menu_frame, text="Start Game", fg="Black", bg="White")
    start.grid(column=4, row=4, columnspan=3, pady=(5, 0))

# create GUI
main_window = Tk()
main_window.geometry("700x425")
# create main window
main_window.title("Maths Quiz")
main_window.config(bg="black")
main_window.resizable(False, False)

createMenu(main_window)

main_window.mainloop()
