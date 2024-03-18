# createAccount.py

import tkinter as tk
from tkinter import messagebox
import hashlib

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
    createAccount.geometry("400x170")

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

    button_submit = tk.Button(createAccount, text="Create Account", command=lambda: [getNewUser(usernameEntry, passwordEntry, login), createAccount.destroy()])  
    button_submit.pack()
