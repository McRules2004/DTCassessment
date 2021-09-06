"""
Joel Mckinnon
August 2021
Main Code
V2
"""
# imports
from tkinter import *
from Project import menu


# create GUI
class MyTkWindow:
    def __init__(self):
        self.main_window = Tk()  # create window
        self.main_window.geometry("700x425")  # give window size
        # window title and design
        self.main_window.title("Maths Quiz")
        self.main_window.config(bg="black")
        # make window not resizeable
        self.main_window.resizable(False, False)
        # running menu class __init__
        self.myMenu = menu.Menu(self.main_window)

    # running loop
    def start(self):
        self.main_window.mainloop()
