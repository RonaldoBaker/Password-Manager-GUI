from tkinter import *
from tkinter import messagebox
import random
import pyperclip

PERSONAL_EMAIL = "r.remario.baker@gmail.com"
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 
           'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(LETTERS) for _ in range(nr_letters)]
    password_list += [random.choice(NUMBERS) for _ in range(nr_numbers)]
    password_list += [random.choice(SYMBOLS) for _ in range(nr_symbols)]

    random.shuffle(password_list)
    password = ''.join(password_list)

    if len(password_input.get()) > 0:
        password_input.delete(0, END)
    
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_account():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0: # Fields are empty
        messagebox.showinfo(title='Oops!', message='Please do not leave any fields empty')
    
    else:
        details_correct = messagebox.askokcancel(title=website, 
        message=f'These are the details entered: \nEmail: {email}\nPassword: {password}\n\n OK to save?')

        if details_correct:
            with open('password_data.txt', mode='a') as data_file:
                data_file.write(f'{website} | {email} | {password}\n')
                website_input.delete(0, END)
                password_input.delete(0, END)
            messagebox.showinfo(title="System Message", message="Account details saved successfully!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Personal Password Manager')  
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
bg_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=bg_image)
canvas.grid(column=1, row=0)

#LABELS
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

#INPUTS
website_input = Entry(width=45)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

email_input = Entry(width=45)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, PERSONAL_EMAIL)

password_input = Entry(width=27)
password_input.grid(column=1, row=3)


#BUTTONS
add_button = Button(text='Add', width=38, command=add_account)
add_button.grid(column=1, row=4, columnspan=2)

generate_button = Button(text='Generate Password',command=generate_password)
generate_button.grid(column=2,row=3)

window.mainloop()
