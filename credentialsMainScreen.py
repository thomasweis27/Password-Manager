import tkinter as tk
from tkinter import messagebox
from addCredentialSet import addCredentialSet
from accessCredentialSets import main


def logout(login, window):
    messagebox.showinfo("Success", "You have logged out!")
    login.deiconify()
    window.withdraw()


# enteredPassword, hashed_data.hexdigest() will be used to figure out if this is one of the current user's sites
# oldhash will be used only if the user will be changing their login info.
# login is the login screen.
def credentialsMainScreen(enteredPassword, curreentHash, oldHash, login):
    login.withdraw()
    print(enteredPassword, curreentHash, oldHash)

    window = tk.Tk()
    window.geometry("600x600")
    window.title("Password Manager")

    frmSideBar = tk.Frame(window, relief = tk.RAISED, bd = 2, height=window.winfo_height())
    frmSideBar.grid(row=0, column=0)

    mainBtn = tk.Button(master = frmSideBar, text = "Main", width=10, height=2)
    searchBtn = tk.Button(master = frmSideBar, text = "Search", height=2, command=lambda: addCredentialSet())
    addBtn = tk.Button(master = frmSideBar, text = "Add", height=2, command=lambda: addCredentialSet())
    editBtn = tk.Button(master = frmSideBar, text = "Edit", height=2)
    accountBtn = tk.Button(master = frmSideBar, text = "Button", height=2)
    logoutBtn = tk.Button(master = frmSideBar, text = "Logout", height=2, command=lambda: logout(login, window))

    mainBtn.grid(row=0, column=0, sticky="ew")
    searchBtn.grid(row=1, column=0, sticky="ew")
    addBtn.grid(row=2, column=0, sticky="ew")
    editBtn.grid(row=3, column=0, sticky="ew")
    accountBtn.grid(row=4, column=0, sticky="ew")
    logoutBtn.grid(row=5, column=0, sticky="ew")

    window.mainloop()

