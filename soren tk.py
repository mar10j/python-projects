import tkinter as tko

def action_print():
    print("TKO!!!")




window = tko.Tk()

button1 = tko.Button(window, text="yo mama", command=action_print)


button1.pack()
