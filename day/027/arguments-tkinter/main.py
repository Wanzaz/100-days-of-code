# Keyword Arguments
# Advanced Arguments
# Arguments with Default Values
def my_function(a=1, b=2, c=3):
    pass

# Calling function with default values
my_function()


import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


# Label 

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="bottom", expand=True)


"""
# comparing pack() to turtle write()
import turtle

tim = turtle.Turtle()
# Function write() has some optional and compulsary arguments
tim.write("Some text")
"""







# Always on the bottom of the program
window.mainloop() 
