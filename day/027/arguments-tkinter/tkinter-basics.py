import tkinter
# or from tkinter import *

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


# Label 
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="bottom", expand=True)


# this is how we change, configure, update  particular component
my_label["text"] = "new text"
my_label.config(text="New Text")


# Button
def button_clicked():
    new_text = user_input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click Me", command=button_clicked) # no () are needed for command
button.pack()


# Entry
user_input = tkinter.Entry(width=10)
user_input.pack()
# print(user_input.get())




window.mainloop() 
