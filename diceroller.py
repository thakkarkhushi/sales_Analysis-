import tkinter as tk
import random
dice_faces = {
    1: " You rolled: 1\n\n┌───────┐\n│       │\n│   ●   │\n│       │\n└───────┘",
    2: " You rolled: 2\n\n┌───────┐\n│ ●     │\n│       │\n│     ● │\n└───────┘",
    3: " You rolled: 3\n\n┌───────┐\n│ ●     │\n│   ●   │\n│     ● │\n└───────┘",
    4: " You rolled: 4\n\n┌───────┐\n│ ●   ● │\n│       │\n│ ●   ● │\n└───────┘",
    5: " You rolled: 5\n\n┌───────┐\n│ ●   ● │\n│   ●   │\n│ ●   ● │\n└───────┘",
    6: " You rolled: 6\n\n┌───────┐\n│ ●   ● │\n│ ●   ● │\n│ ●   ● │\n└───────┘"
}
root=tk.Tk()
root.title("\n\ndigital Dice roller")
root.geometry("300x300")
label=tk.Label(root,text="Cilck 'rolr dice' to start!",font=("Courier",12),justify="left")
label.pack(pady=20)
def roll_dice():
    Dice=random.randint(1,6)
    label.config(text=dice_faces[Dice])
button=tk.Button(root,text="Roll dice",font=("Areal",14), command=roll_dice) 
button.pack(pady=10) 
exit_btn=tk.Button(root,text="Exit",font=("Areal",12), command=root.destroy)
exit_btn.pack()

root.mainloop()