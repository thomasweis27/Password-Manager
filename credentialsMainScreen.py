import tkinter as tk
from tkinter import messagebox
from addCredentialSet import addCredentialSet
from accessCredentialSets import accessCredentialSets
from Decrypt import decrypt


def logout(login, window):
    messagebox.showinfo("Success", "You have logged out!")
    login.deiconify()
    window.withdraw()

def addPinnedToList(enteredPassword, currentHash, pinnedListbox):
    userSites = []
    with open("credentials.txt") as file:
        for line in file:
            try:
                dictionary = eval(line)
                line  = decrypt(dictionary, enteredPassword)
                line = "$"+str(line)
                if currentHash in line:
                    split_line = line.split(",")
                    # Search for pinned credential sets
                    if split_line[-1] == "True$'":
                        userSites.append(split_line)
                    else:
                        continue
            except:
                pass
    # Close file
    file.close()
    # Add each site name to the listbox
    for site in userSites:
        pinnedListbox.insert(tk.END, site[1])

def addRecentToList(enteredPassword, currentHash, recentListbox):
    userSites = []
    with open("credentials.txt") as file:
        for line in file:
            try:
                dictionary = eval(line)
                line  = decrypt(dictionary, enteredPassword)
                line = "$"+str(line)     
                if currentHash in line:
                    split_line = line.split(",")
                    userSites.append(split_line)
            except:
                pass
    # Close file
    file.close()
    # Add each site name to the listbox
    if len(userSites) < 5:
        for site in userSites:
            recentListbox.insert(tk.END, site[1])
    else:
        for i in range(5):
            recentListbox.insert(tk.END, userSites[i-5][1])
    

#TODO: create function that takes the old hash and replaces it with the new hash


# enteredPassword, hashed_data.hexdigest() will be used to figure out if this is one of the current user's sites
# oldhash will be used only if the user will be changing their login info.
# login is the login screen.
def credentialsMainScreen(enteredPassword, currentHash, oldHash, login):
    login.withdraw()
    print(enteredPassword, currentHash, oldHash)

    window = tk.Tk()
    window.geometry("800x450")
    window.title("Password Manager")

    frmSideBar = tk.Frame(window, relief = tk.RAISED, bd = 2, height=window.winfo_height())
    frmSideBar.grid(row=0, column=0)

    frmRecentPin = tk.Frame(window, relief = tk.RAISED, bd = 2, height=window.winfo_height())
    frmRecentPin.grid(row=0, column=1)

    addBtn = tk.Button(master = frmSideBar, text = "Add", height=2, command=lambda: addCredentialSet(currentHash, enteredPassword, window))
    searchBtn = tk.Button(master = frmSideBar, text = "Search", height=2, command=lambda: accessCredentialSets(currentHash, enteredPassword, window))#changed to add encryption!!!!!!
    logoutBtn = tk.Button(master = frmSideBar, text = "Logout", height=2, command=lambda: logout(login, window))

    recentLabel = tk.Label(master=frmRecentPin, text="Recently Added Credentials")
    recentListbox = tk.Listbox(master=frmRecentPin, height=10, width=20)
    pinnedLabel = tk.Label(master=frmRecentPin, text="Pinned Credentials")
    pinnedListbox = tk.Listbox(master=frmRecentPin, height=10, width=20)

    # Here is where recently searched/looked at credentials are added to the list box
    addRecentToList(enteredPassword, currentHash, recentListbox)

    # Here is where pinned credentials are added to the list box
    addPinnedToList(enteredPassword, currentHash, pinnedListbox)

    recentLabel.grid(row=0, column=0)
    recentListbox.grid(row=1, column=0)
    pinnedLabel.grid(row=0, column=1)
    pinnedListbox.grid(row=1, column=1)

    addBtn.grid(row=0, column=0, sticky="ew")
    searchBtn.grid(row=1, column=0, sticky="ew")
    logoutBtn.grid(row=2, column=0, sticky="ew")

