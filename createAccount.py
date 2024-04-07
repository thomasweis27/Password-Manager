import tkinter as tk
from tkinter import messagebox
import hashlib

def checkPasswordRequirements(usernameEntry, passwordEntry, login, createAccount):
    print("Checking requirements...")
    specalCharacters = "[!@#$%^&*()+_-=}{[]:\|,./<>?;'<>?"
    password = passwordEntry.get()
    
    #if statments that check to see if th account meets password requirements
    if len(password) < 12:
        messagebox.showinfo("Error", "Please make sure that password is 12 characters or longer.")
    elif any(char.isdigit() for char in password) == False:
        messagebox.showinfo("Error", "Please make sure that password contains a number.")
    elif any(char.isupper() for char in password) == False:
        messagebox.showinfo("Error", "Please make sure that password contains upper case letters.")
    elif any(char.islower() for char in password) == False:
        messagebox.showinfo("Error", "Please make sure that password contains a lower case letters.")
    elif any(char in specalCharacters for char in password) == False:
        messagebox.showinfo("Error", "Please make sure that password contains a special character.")
    else:
        getNewUser(usernameEntry, passwordEntry, login)
        createAccount.destroy()




def getNewUser(usernameEntry, passwordEntry, login):
    enteredUsername = usernameEntry.get()
    enteredPassword = passwordEntry.get()

    print(enteredUsername, enteredPassword)
    data = enteredUsername + enteredPassword
    hashed_data = hashlib.sha256(data.encode())
    print(hashed_data.hexdigest())

    with open("users.txt", "a") as file:
        file.write("\n" + hashed_data.hexdigest())

    messagebox.showinfo("Success", "Account created successfully!")
    login.deiconify()
    

#_________________________________________________________________________________________

def create_account(login):
    login.withdraw()
    
    createAccount = tk.Toplevel(login)  # Create a new window
    createAccount.title("Password Manager")
    createAccount.geometry("800x450")

    label = tk.Label(createAccount, text="\nCreate Account\n")
    label.pack()

    # username
    labelusername = tk.Label(createAccount, text="Create Username: ")
    labelusername.pack()
    username = tk.StringVar()
    usernameEntry = tk.Entry(createAccount, textvariable=username)
    usernameEntry.pack()

    # password
    labelPassword = tk.Label(createAccount, text="Create Password: ")
    labelPassword.pack()
    password = tk.StringVar()
    passwordEntry = tk.Entry(createAccount, textvariable=password)
    passwordEntry.pack()

    button_submit = tk.Button(createAccount, text="Create Account", command=lambda: checkPasswordRequirements(usernameEntry, passwordEntry, login, createAccount))  
    button_submit.pack()
