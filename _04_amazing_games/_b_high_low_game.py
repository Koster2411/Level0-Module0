from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    Random = random.randint(1, 10)

    # 2. Print out the random variable that you made in step #1
    print(Random)
    # 3. Code a for loop to run steps 4-10, 10 times
    for i in range(4):
        question1 = simpledialog.askinteger(title=('number'), prompt=('type a number from on to ten into this box.'))
        # 4. Ask the user for a guess using a pop-up window, and save their response
        if question1 == Random:
            messagebox.showinfo(title=('win'), message=('You won'))
            sys.exit(0)
        # 5. If the guess is correct
            # 6. Win. Use 'sys.exit(0)' to end the program
        if question1 > Random:
            messagebox.showinfo(title=('to high'), message=('your guess was too high'))
        # 7. if the guess is high
            # 8. Tell them it's too high
        if question1 < Random:
            messagebox.showinfo(title=('to low'), message=('your guess was too low'))
        # 9. Else if the guess is low
            # 10. Tell them it's too low

    #11. Outside of the loop, tell the user they lost
    messagebox.showerror(title=('loser'), message=('loser loser loser!!!'))

    window.mainloop()
