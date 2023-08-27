from tkinter import *
from tkinter import messagebox
import pyperclip
from random import choice, randint, shuffle
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

    password = "".join(password_list)
    pass_txt.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def find_password():
    try:
        with open("cont.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Oops", message="No Data File found")
    else:
        webs = web_txt.get()
        if webs in data:
            email = data[webs]["email"]
            password = data[webs]["password"]
            messagebox.showinfo(title="Data Found", message=f"Heres the data:\nEmail:{email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Oops", message="No data for website exist")


def save():
    website_name = web_txt.get()
    email = user_txt.get()
    password = pass_txt.get()
    new_data = {
        website_name: {
            "email" : email,
            "password" : password,
        }
    }
    
    if len(website_name) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="You cannot leave fields empty")
    else:
        try:
            with open("cont.json", mode="r") as data_file:
                print("Hello")
        except FileNotFoundError:
            with open("cont.json",mode="w") as data_file:
                json.dump(new_data,data_file, indent=4)
            
        else:
            with open("cont.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # updating old data with new data
                data.update(new_data)
            with open("cont.json",mode="w") as data_file:
                # Saving updated data
                json.dump(data,data_file, indent=4)
        finally:
                web_txt.delete(0,END)
                pass_txt.delete(0,END)
            
            
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200,highlightthickness=0)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=pass_img)
canvas.grid(column=1, row=0)

web_lab = Label(text="Website")
web_lab.grid(column=0,row=1)
web_txt = Entry(width=35)
web_txt.grid(column=1,row=1)
web_txt.focus()
search_btn = Button(text="Search", command=find_password)
search_btn.grid(column=2,row=1)

user_lab = Label(text="Email/pass")
user_lab.grid(column=0,row=2)
user_txt = Entry(width=35)
user_txt.grid(column=1,row=2,columnspan=2)
user_txt.insert(0,"razz.jazz30@gmail.com")

pass_lab = Label(text="Password")
pass_lab.grid(column=0,row=3)
pass_txt = Entry(width=21)
pass_txt.grid(column=1,row=3)
pass_btn = Button(text="Generate Password",command=generate_password)
pass_btn.grid(column=2,row=3)

add_btn = Button(text="Add",width=36, command=save)
add_btn.grid(column=1,row=4,columnspan=2)


window.mainloop()