# main.py

import tkinter as tk
from tkinter import messagebox
import hashlib
from credentialSetsModule import data_menu_function
from createAccount import create_account

def loginPage():
    login = tk.Tk()
    login.title("Password Manager")
    login.geometry("400x200")

    def getValue():
        enteredUsername = usernameEntry.get()
        enteredPassword = passwordEntry.get()

        print(enteredUsername, enteredPassword)
        data = enteredUsername + enteredPassword
        hashed_data = hashlib.sha256(data.encode())
        print(hashed_data.hexdigest())

        with open("users.txt", "r") as file:
            for line in file:
                if hashed_data.hexdigest() == line.strip():  # Strip trailing newline
                    print("Login successful")
                    login.withdraw()
                    data_menu_function(enteredPassword)
                    break

    label = tk.Label(login, text="\nPassword Manager\n")
    label.pack()

    #username
    labelusername = tk.Label(login, text="Username: ")
    labelusername.pack()
    username = tk.StringVar()
    usernameEntry = tk.Entry(login, textvariable=username)
    usernameEntry.pack()

    #password
    labelPassword = tk.Label(login, text="Password: ")
    labelPassword.pack()
    password = tk.StringVar()
    passwordEntry = tk.Entry(login, textvariable=password)
    passwordEntry.pack()

    button_submit = tk.Button(login, text="Submit", command=getValue)
    button_submit.pack()

    #menu buttons
    button1 = tk.Button(login, text="About Us", command=show_creaters)
    button2 = tk.Button(login, text="Create Account", command=lambda: create_account(login))  

    # Pack the buttons side by side
    button1.pack(side=tk.RIGHT)
    button2.pack(side=tk.LEFT)

    login.mainloop()

def show_creaters():
    messagebox.showinfo("About us", "Cale, Thomas, Mason Senior Project (add more as needed)")

loginPage()
