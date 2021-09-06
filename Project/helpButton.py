""" help button method,
used to display the help class
Joel McKinnon
September2021
"""
# imports
from tkinter import *
from helpPopup import help_popup


# function to create help button
def helpButton(frame, window):
    # getting image to use as button
    help_image = PhotoImage(file="images/help.png")
    help_image2 = help_image.subsample(60, 60)  # resize image using subsample
    help_button = Button(frame, image=help_image2, command=lambda: help_popup(window))
    help_button.photo = help_image2
    help_button.grid(row=9, column=9)
