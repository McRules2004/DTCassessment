from tkinter import *


def exitButton(frame, window):
    exit_image = PhotoImage(file="images/exit.jpg")
    exit_image2 = exit_image.subsample(50, 50)  # resize image using subsample
    exit_button = Button(frame, image=exit_image2, command=window.destroy)
    exit_button.photo = exit_image2
    exit_button.grid(row=0, column=0, padx=2, pady=2, sticky=N)
