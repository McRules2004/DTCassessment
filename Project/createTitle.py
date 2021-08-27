from tkinter import *


def create_title(frame):
    title_image = PhotoImage(file="images/quiz.png")
    title_image2 = title_image.subsample(17, 17)  # resize image using subsample
    title = Label(frame, image=title_image2, text="Maths Quiz", font="Times 30 italic bold", fg="blue",
                  compound=RIGHT)
    title.photo = title_image2
    title.grid(row=0, column=3, columnspan=5, pady=(10, 0))
    return title
