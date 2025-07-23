from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    passwordList = ''
    password = ''
    letters = ['a','b','c','d','e','f','g', 'h', 'i', 'j']
    symbols = ['!','@','#','$','%','^','&','*','(', ')']
    number = ['1','2','4','5','6','7','8','9','0']
    passwordList 


    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_sybols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(number) for _ in range(randint(2, 4))]



    password_list = password_letter + password_sybols + password_numbers
    shuffle(password_list) 
    

    password = "".join(password_list)
    password_input.insert(0, password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
   website = web_input.get()
   email = email_input.get() 
   password = password_input.get()

   if len(website) == 0 or len(password) == 0:
       messagebox.showinfo(title="Oops",  message="Please don't leave any fields empty! ")
   else:
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{email}\nPassword:{password}\nIs it ok to save?")
    if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}" + "\n")
                web_input.delete(0, END)
                password_input.delete(0, END)





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)


web_label = Label(text="Website: ")
web_label.grid(column=0, row=1)

web_input = Entry(width=35)
web_input.grid(column=1, row=1, columnspan=2)


email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "email@gmail.com")

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)


gerner_button = Button(text="Generate Password", command=generate_password)
gerner_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)






window.mainloop()