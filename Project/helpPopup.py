from help import Help


# help box popup
def help_popup(window):
    print("help2")
    get_help = Help(window)
    get_help.help_text.configure(text="-To save your results please    enter your name\n-Press start"
                                      "\n-Enter result and press enter\n-Will tell u whether u were    correct"
                                      "\n-Continue for the 10    questions", bg="Gray", fg="white", font=("arial", "14"))
