from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-mif __name__ == '__main__':ain code block, *hint, type main then ctrl+space to auto-completeif __name__ == '__main__':
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    number = random.randint(0, 3)

    # 2. Print your variable to the console
    print(number)
    # 3. Get the user to enter something that they think is awesome
    question1 = simpledialog.askstring(title=('cool'), prompt=('type something cool into this box'))
    # 4. If your variable is  0
    if number == 0:
        messagebox.showinfo(title=('awesome'), message=('That is awesome'))
        # -- tell the user whatever they entered is awesome!
    if number == 1:
        messagebox.showinfo(title=('ok'), message=('that is cool'))
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    if number == 2:
        messagebox.showinfo(title=('boring'), message=('That is Boring!!!!!!!'))
    
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
    if number == 3:
        messagebox.showerror(title=('Shoo shoo'), message=('Get off of the computer!!!!!!!!!!!'))
        
    # Run the window's .mainloop() method
