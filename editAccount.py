import tkinter as tk
from tkinter import messagebox
import hashlib

def checkPasswordRequirements(usernameEntry, passwordEntry, login, createAccount):
    print("Checking requirements...")
    specalCharacters = "[!@#$%^&*()+_-=}{[]:\|,./<>?;'<>?"
    password = passwordEntry.get()
    
    #if statments that check to see if th account meets password requirements
    if len(password) < 12:
        messagebox.showinfo("Error", "Please make sure that the password is 12 characters or longer.")
    elif any(char.isdigit() for char in password) == False:
        messagebox.showinfo("Error", "Please make sure that the password contains a number.")
    elif any(char.isupper() for char in password) == False:
        messagebox.showinfo("Error", "Please make sure that the password contains upper case letters.")
    elif any(char.islower() for char in password) == False:
        messagebox.showinfo("Error", "Please make sure that the password contains a lower case letters.")
    elif any(char in specalCharacters for char in password) == False:
        messagebox.showinfo("Error", "Please make sure that the password contains a special character.")
    else:
        getNewUser(usernameEntry, passwordEntry, login)
        createAccount.destroy()


def checkExistingUser(usernameEntry, passwordEntry):
    enteredUsername = usernameEntry.get()
    enteredPassword = passwordEntry.get()

    print(enteredUsername, enteredPassword)
    data = enteredUsername + enteredPassword
    print("The old username password was:", data)
    hashed_data = hashlib.sha256(data.encode())
    print(hashed_data.hexdigest())
    
    with open("users.txt", "r") as file:
        for line in file:
            if hashed_data.hexdigest() == line.strip():  # Strip trailing newline
                print("True")
                return True                         #ToDo check and make sure that the user that is being edited actually exists in users.txt
        print("This didn't an existing password with that user/pass")
        return False

def checkNewAndOldUserAndPAss(usernameEntry, passwordEntry, usernameEntrynew, passwordEntrynew, login, createAccount):
    print(usernameEntry.get(), passwordEntry.get(), usernameEntrynew.get(), passwordEntrynew.get(), login, createAccount)
    if checkExistingUser(usernameEntry, passwordEntry) == True:
        print("That passed")
        checkPasswordRequirements(usernameEntrynew, passwordEntrynew, login, createAccount)


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

def edit_account(login):
    login.withdraw()
    
    createAccount = tk.Toplevel(login)  # Create a new window
    createAccount.title("Password Manager")
    createAccount.geometry("400x300")

    label = tk.Label(createAccount, text="\nEdit Existing Account\n")
    label.pack()

    # old username
    labelusername = tk.Label(createAccount, text="Current Username: ")
    labelusername.pack()
    username = tk.StringVar()
    usernameEntry = tk.Entry(createAccount, textvariable=username)
    usernameEntry.pack()

    # old password
    labelPassword = tk.Label(createAccount, text="Current Password: ")
    labelPassword.pack()
    password = tk.StringVar()
    passwordEntry = tk.Entry(createAccount, textvariable=password)
    passwordEntry.pack()

#ToDo: Make sure the username and pass hash matched what is in the users.txt site
#_____________________________________________________________________________
    # new username
    labelusernamenew = tk.Label(createAccount, text="\n\nNew Username: ")
    labelusernamenew.pack()
    usernamenew = tk.StringVar()
    usernameEntrynew = tk.Entry(createAccount, textvariable=usernamenew)
    usernameEntrynew.pack()

    # new password
    labelPasswordnew = tk.Label(createAccount, text="New Password: ")
    labelPasswordnew.pack()
    passwordnew = tk.StringVar()
    passwordEntrynew = tk.Entry(createAccount, textvariable=passwordnew)
    passwordEntrynew.pack()


    button_submit = tk.Button(createAccount, text="Update Account", command=lambda: checkNewAndOldUserAndPAss(usernameEntry, passwordEntry, usernameEntrynew, passwordEntrynew, login, createAccount))  
    button_submit.pack()
