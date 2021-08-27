"""
Joel Mckinnon
August 2021
Main Code
V2
"""

from tkinter import *
from Project import menu

# create GUI
class MyTkWindow:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.geometry("700x425")
        # create main window
        self.main_window.title("Maths Quiz")
        self.main_window.config(bg="black")
        self.main_window.resizable(False, False)

        self.myMenu = menu.Menu(self.main_window)

    def start(self):
        self.main_window.mainloop()
