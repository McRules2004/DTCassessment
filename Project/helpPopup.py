from help import Help

# help box popup
def help_popup(window):
    get_help = Help(window)
    get_help.help_text.configure(text="Help Text Here",
                                 fg="white", font=("arial", "14"))
