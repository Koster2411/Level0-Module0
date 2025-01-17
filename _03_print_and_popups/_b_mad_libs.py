from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # Put this sentence in a pop-up message box:
    # "If you find yourself having to cross a piranha-infested river, here's how to do it..."
    messagebox.showinfo(title='', message='If you find yourself having to cross a piranha-infested river, here is how you do it...')
    # Get the player to enter an adjective
    word = simpledialog.askstring(title='adjective', prompt='type an adjective into this box.')
    # Get the player to enter a type of liquid
    liquid = simpledialog.askstring(title='liquid', prompt='type a liquid into this box.')
    # Get the player to enter a body part
    body = simpledialog.askstring(title='bodypart', prompt='type an bodypart into this box.')
    # Get the player to enter a verb
    verb = simpledialog.askstring(title='verb', prompt='type a verb into this box.')
    # Get the player to enter a place
    place = simpledialog.askstring(title='place' , prompt='type a place into this box.')
    wound = simpledialog.askstring(title='noun', prompt='type a noun into this box')
    time = simpledialog.askstring(title='time', prompt='type a time into this box')
    thing = simpledialog.askstring(title='thing', prompt='type a thing into this box')
    adjective = simpledialog.askstring(title='adjective', prompt='type a adjective into this box')
    time1 = simpledialog.askstring(title='time', prompt='type am or pm into this box')
    if time1 == 'am':
        print(time1)
    elif time1 == 'pm':
        print(time1)
    else:
        messagebox.showwarning(title='wrong', message='loser loser READ THE INSTRUCTIONS PERSON!!!!')
        window.mainloop()
    # The story below has has been written as a group of Strings joined
    # together by + signs. The story contains place holders, indicated
    # by [** **] which you need to replace with the values entered by the
    # player.
    # Hint: You will need to add more + signs to join the variables to the
    #       other parts of the story.

    story = (
        "Piranhas are more "+word+" during the day, so cross the river at\n"
        ""+time+" "+time1+". Piranhas are attracted to fresh "+liquid+" and will most\n"
        "likely take a "+thing+" out of your "+body+" if you "+verb+" with them. Whatever\n"
        "you do, if you have an "+adjective+" "+wound+", try to find another way to get "
        "back to your "+place+". Good luck! Ps.I hope you get a "+thing+" on your "+body+"."
    )
    messagebox.showinfo(title='full story', message=' '+story)
    # Make a pop-up that contains the final story. The \n escape characters add
    # line breaks to the story. If you need to, move them around to make your
    # story look better in the pop-up

    # If you want to write your own Madlib story, just change the story variable
    # and ask the player different questions.
    # Run the window's .mainloop() method
    window.mainloop()
    pass
