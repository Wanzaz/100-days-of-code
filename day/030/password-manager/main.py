import json
import pyperclip
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    # Or we could put them into separated lists and then do this: password_list = list1 + list2 + list3

    shuffle(password_list)

    password = "".join(password_list)
    password_input_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_input_entry.get()
    email = email_input_entry.get()
    password = password_input_entry.get()
    new_data = {
            website: {
                "email": email,
                "password": password,
            }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Error', message="Please don't leave any fields empty")
    else:
        try:
            with open('data.json', 'r') as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                # Saving new data and creating new file
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open('data.json', 'w') as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input_entry.delete(0, END)
            password_input_entry.delete(0, END)
            website_input_entry.focus()


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_input_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Website: {website}\n Email: {email}, Password: {password}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website exists")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Buttons
gen_pass_button = Button(text='Generate Password', command=generate_password, width=14)
gen_pass_button.grid(column=2, row=3)
add_button = Button(text='Add', width=38, command=save)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text='Search', command=find_password, width=14)
search_button.grid(column=2, row=1)

# Entries
website_input_entry = Entry(width=22)
website_input_entry.grid(column=1, row=1)
website_input_entry.focus()
email_input_entry = Entry(width=40)
email_input_entry.grid(column=1, row=2, columnspan=2)
email_input_entry.insert(0, "name@email.com")
password_input_entry = Entry(width=22)
password_input_entry.grid(column=1, row=3)

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)


window.mainloop()

