from tkinter import *


def closeButton(frame, window):
    close_button = Button(frame, text="Close Quiz", command=window.destroy)
    close_button.grid(row=4, column=3, columnspan=5)
