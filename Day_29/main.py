from distutils.cmd import Command
from email.mime import image
from tkinter import *
from tkinter import messagebox
from turtle import color
# import <pyperclip>



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def pass_gen():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [letter for letter in random.sample(letters, k=nr_letters)]
    password_list += random.sample(symbols, k=nr_symbols)
    password_list += random.sample(numbers, k=nr_numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, f"{password}")

    print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():

    if len(website_entry.get())== 0 or len(pass_entry.get()) == 0:
        messagebox.showinfo(title="Oops", message="You have not entered website or password")

    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"Theses are the details:\nUsername: {username_entry.get()}"
    f"\nPassword: {pass_entry.get()}\nIs it ok?")

        if is_ok:
            with open("./Day_29/data.txt", "a") as f:
                f.write(f"\n{website_entry.get()}, {username_entry.get()}, {pass_entry.get()}")
            website_entry.delete(0, END)
            pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

# CREATE WINDOW
window = Tk()
window.title("Passwork Manager")
window.config(padx= 50, pady=50)

# CREATE CANVAS
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="./Day_29/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=1,column=2)

# CREATE labels and buttons
website_label = Label(text="Website:")
website_label.grid(row=2, column=1)

username_label = Label(text="Email/Username:")
username_label.grid(row=3, column=1)

pass_label = Label(text="Password:")
pass_label.grid(row=4, column=1)

website_entry = Entry(width=52)
website_entry.focus()
website_entry.grid(row=2, column=2, columnspan=2)


username_entry = Entry(width=52)
username_entry.insert(0, "email@gmail.com")
# username_entry.insert(END, ".com")
username_entry.grid(row=3, column=2, columnspan=2)


pass_entry = Entry(width=33)
pass_entry.grid(row=4, column=2)

pass_generate_button = Button(text="Generate Password", command=pass_gen)
pass_generate_button.grid(row=4, column=3)


    

add_button = Button(text="Add", width=44, command=save_pass, bg="#9bdeac")
add_button.grid(row=5, column=2, columnspan=2)








window.mainloop()
