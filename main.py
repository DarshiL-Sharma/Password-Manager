from tkinter import *
from tkinter import messagebox
from random import choice , randint , shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8,10)) ]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]


    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    Password_input.insert(0,password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_input.get()
    email = Email_username_input.get()
    password = Password_input.get()


    if Email_username_input.get() == "":
        messagebox.showinfo(title = "Ooops ", message="You Leave  Email Field")
    elif website_input.get() == "":
        messagebox.showinfo(title = "Ooops ", message="You Leave Website Field")

    elif Password_input.get()=="":
        messagebox.showinfo(title = "Ooops ", message="You Leave Password Field")
    elif len(Password_input.get()) <=7:
        messagebox.showinfo(title = "Ooops ", message="Your Password is Too Short\n Password should be greater then 8 character")


    else:
        is_ok = messagebox.askokcancel(title = website, message = f"These are the details entered: \nEmail: {email} \nPassword:  {password}  \n Is it ok to save? ")

        if is_ok:

            with open("data.txt","a") as data_file:
                 data_file.write(f"{website} | {email} | {password}\n")
            website_input.delete(0,END)
            # Email_username_input.delete(0,END)
            Password_input.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(width =500 , height=500 )
window.config(padx=50,pady=50)


canvas = Canvas(width = 200, height= 200 )
logo_img = PhotoImage(file ="logo.png")
canvas.create_image(100,100,image = logo_img)
canvas.grid(column = 1 , row = 0)

label_1 = Label(text ="Website:",font = ("Arial",10,"bold") )
label_1.grid(column= 0, row=1 )

label_2 = Label(text="Email/Username:" , font = ("Arial",10, "bold"))
label_2.grid(column = 0, row=2 )

label_3 = Label(text= "Password:", font = ("Arial", 10 , "bold"))
label_3.grid(column = 0 , row =3 )

website_input = Entry(width = 35 )
website_input.grid(column= 1 , row= 1, columnspan=2)
website_input.focus()



Email_username_input = Entry(width = 35)
Email_username_input.grid(column =1 , row =2 , columnspan=2)
Email_username_input.insert(0, "darshil@gmail.com")

Password_input  = Entry(width = 21 )
Password_input.grid(column = 1, row=3 )

Generate_password_button = Button(text = "Generate Password",command=generate_password )
Generate_password_button.grid(column =2 , row = 3)

Add_button = Button(text = "Add",width = 36, command = save)
Add_button.grid(column = 1, row =4 ,columnspan=2)

window.mainloop()

