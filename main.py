# main.py
import tkinter as tk
from tkinter import messagebox
import hashlib
from credentialsMainScreen import credentialsMainScreen
from createAccount import create_account
from editAccount import edit_account

def return_to_login():
    exit()

def loginPage():
    login = tk.Tk()
    login.title("Password Manager")
    login.geometry("800x450")

    def getValue():
        oldHash = ""

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
                    credentialsMainScreen(enteredPassword, hashed_data.hexdigest(), oldHash, login)
                    break

    labelheader = tk.Label(login, text="\nPassword Manager\n")
    label = tk.Label(login, text="\nLogin:\n")
    labelheader.pack()
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
    spaceRight = tk.Label(login, text="    ")
    spaceLeft = tk.Label(login, text="    ")
    button2 = tk.Button(login, text="Create Account", command=lambda: create_account(login))
    button3 = tk.Button(login, text="Edit Account", command=lambda: edit_account(login))  

    # Pack the buttons side by side
    spaceRight.pack(side=tk.RIGHT)
    button3.pack(side=tk.RIGHT)
    spaceLeft.pack(side=tk.LEFT)
    button2.pack(side=tk.LEFT)

    buttonlogout = tk.Button(login, text="Quit", command=return_to_login)
    spaceBottom = tk.Label(login, text="    ")
    spaceBottom.pack(side=tk.BOTTOM)
    buttonlogout.pack(side=tk.BOTTOM)
    button1.pack(side=tk.BOTTOM)
    

    login.mainloop()

def show_creaters():
    messagebox.showinfo("About us", "Cale, Thomas, Mason are seniors at Wittenberg University and this is their Senior Project.")



loginPage()
