import tkinter as tk

def action_print():
    print("hullo woorld")    

def dip_print():
    print("Why must you be so rude")


window = tk.Tk()

button1 = tk.Button(window, text="meeeh", command=action_print)
button2 = tk.Button(window, text="Don't Press me.", command=dip_print)

button1.pack()
button2.pack()

