from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    new_password = "".join(password_list)
    password.insert(0, new_password)
    pyperclip.copy(new_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web = web_name.get()
    psword = password.get()
    user_email = email_user.get()
    new_data = {
        web: {
            "email": user_email,
            'password': psword,
        }
    }

    if len(web) < 1 or len(psword) < 1:
        messagebox.showinfo(message=f'Please fill in all fields: \n Website:{web} '
                                    f' \n Email/User:{user_email}\n Password:{psword}')
    else:
        try:
            with open('data.json', mode='r') as file:
                # Reading old data
                data_file = json.load(file)
                # Updating old data with new data
                data_file.update(new_data)
        except FileNotFoundError:
            with open('data.json', mode='w') as file:
                json.dump(new_data, file, indent=4)
        else:
            with open('data.json', mode='w') as file:
                # Saving Updated Data
                json.dump(data_file, file, indent=4)


        web_name.delete(0, 'end')
        password.delete(0, 'end')

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    web = web_name.get()
    try:
        with open('data.json', mode='r') as file:
            data_file = json.load(file)
            data = data_file[web]
    except KeyError:
        messagebox.showinfo(title=f'Site Not Found', message=f'No details for {web} exist')
    except FileNotFoundError:
        messagebox.showinfo(title=f'Site Not Found', message=f'Please save a website first')
    else:
        messagebox.showinfo(title=f'{web}', message=f'Email:{data["email"]} \n Password:{data["password"]}')



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

web_label = Label(text='Website:')
web_label.grid(row=1, column=0)

web_name = Entry(width=21)
web_name.grid(row=1, column=1)
web_name.focus()

email_user_label = Label(text='Email/Username:')
email_user_label.grid(row=2, column=0)

email_user = Entry(width=35)
email_user.grid(row=2, column=1, columnspan=2)
email_user.insert(0, 'jeremiah.d.wise@gmail.com')

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

password = Entry(width=21)
password.grid(row=3, column=1)

password_button = Button(text='Generate Password', command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text='Add', width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text='Search', width=13, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
