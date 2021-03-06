"""Help class which will display the help window.
window with instructions
Joel McKinnon
September 2021
"""
# imports
from tkinter import *


# class containing help frame
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
