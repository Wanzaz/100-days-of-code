from tkinter import *


# Creating a new window and configurations
window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)


# Button Function
def convert_miles_to_km():
    miles = float(user_input_entry.get())
    km = round(miles * 1.609, 2)
    kilometer_result_label.config(text=km)


# Labels
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)


# Button
calculate_button = Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(column=1, row=2)


# Entry
user_input_entry = Entry(width=7)
user_input_entry.grid(column=1, row=0)





window.mainloop()
