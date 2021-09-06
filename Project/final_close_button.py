""" final close button, this is the bigger close button on final frame
used to close application
Joel McKinnon
September 2021
"""
# imports
from tkinter import *


# function to close window
def close_button(frame, window):
    # close window button
    close_button2 = Button(frame, text="Close Quiz", command=window.destroy)
    close_button2.grid(row=4, column=3, columnspan=5)
