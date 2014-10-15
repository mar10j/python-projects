import tkinter as tk

def action_print():
    print("hullo woorld")    
window = tk.Tk()
button1 = tk.Button(window, text="meeeh", command=action_print)
button1.size(400)
button1.pack()


