# Tkinter Layout Managers: pack(), place(), grid()
# pack() = it is difficult to specify exact position
# place() = precise positioning
# grid() = columns and rows
# grid() and pack() are incompatible so you have to choose between them

import tkinter
# or from tkinter import *

# Button Function
def button_clicked():
    new_text = user_input.get()
    my_label.config(text=new_text)

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)


# Label 
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# this is how we change, configure, update  particular component
my_label["text"] = "new text"
my_label.config(text="New Text")
# my_label.pack(side="bottom", expand=True)
# my_label.place(x=0, y=0) # left corner
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)



# Button
button = tkinter.Button(text="Click Me", command=button_clicked) # no () are needed for command
# button.pack()
button.grid(column=1, row=1)

# New Button
new_button = tkinter.Button(text="New Button", command=button_clicked) # no () are needed for command
new_button.grid(column=2, row=0)

# Entry
user_input = tkinter.Entry(width=10)
print(user_input.get())
# user_input.pack()
user_input.grid(column=3, row=2)



window.mainloop() 
