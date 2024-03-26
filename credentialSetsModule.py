#This was a basic proof of concept modual starting point, 
#Cale, feel free to change any of this, its a basic proof of concept and 
#was mostly for me to make sure that I could pass over log in 
#credentials to the credential screen.

#imports
import tkinter as tk
from tkinter import messagebox

def return_to_login():
    exit()

def removeSiteData():
    selected_item = listbox.get(tk.ACTIVE)
    print("Item to Remove:", selected_item)
    lines_to_keep = []

    with open('sites.txt', 'r') as file:
        for line in file:
            if line.split(',')[0] == selected_item:
                pass
            else:
                lines_to_keep.append(line.strip())
    with open('sites.txt', 'w') as file:
        file.write('\n'.join(lines_to_keep))


def getNewSite():
    enteredNewSite = newSiteEntry.get()
    enteredNewUsername = newusername.get()
    enteredNewPassword = newpassword.get()
    #"a" - append - add to the end
    with open("sites.txt", "a") as file:
        file.write("\n" + enteredNewSite + "," + enteredNewUsername + "," +
                   enteredNewPassword)
    addSitemenu.withdraw()
    SUPmenu.deiconify()

def addSite():
    addSitemenu.deiconify()
    SUPmenu.withdraw()

def readSiteData():
    selected_item = listbox.get(tk.ACTIVE)
    print("Selected Item:", selected_item)
    with open('sites.txt', 'r') as file:
        for line in file:
            if line.split(',')[0] == selected_item:
                userAndPass = "Username: " + line.split(
                    ',')[1] + "\nPassword: " + line.split(',')[2]
                print(userAndPass)
                show_message(line.split(',')[0], userAndPass)

#___________________________________________________________________________________
def data_menu_function(password):
    # Place your data menu functionality here
    print("Accessing data menu functionality")
    SUPmenu = tk.Tk()
    SUPmenu.title("Username and Password Menu")
    SUPmenu.geometry("400x400")
    SUPmenu.deiconify()  # Hide the window initially

    #label
    label = tk.Label(SUPmenu, text="The sites you have passwords for:")
    label.pack(side=tk.TOP)
    # Open the file
    sites = []
    with open('sites.txt', 'r') as file:
        for line in file:
            sites.append(line.split(',')[0])

    print(sites)
    listbox = tk.Listbox(SUPmenu)
    for item in sites:
        listbox.insert(tk.END, item)
        listbox.pack()
    label = tk.Label(SUPmenu, text="Select one and the select an option below:")
    label.pack(side=tk.TOP)

    buttonAdd = tk.Button(SUPmenu, text="Add", command=addSite)
    buttonRead = tk.Button(SUPmenu, text="Read", command=readSiteData)
    buttonRemove = tk.Button(SUPmenu, text="Remove", command=removeSiteData)
    buttonlogout = tk.Button(SUPmenu, text="Log Out", command=return_to_login)

    buttonlogout.pack(side=tk.BOTTOM)
    #make the menu buttons:
    buttonAdd.pack()
    buttonRead.pack()
    buttonRemove.pack()

    #add site menu:
    #_______________________________________________________________
    addSitemenu = tk.Toplevel(SUPmenu)
    addSitemenu.title("Add a site:")
    addSitemenu.geometry("200x200")
    addSitemenu.withdraw()

    #site
    labelNewSite = tk.Label(addSitemenu, text="Site Name: ")
    labelNewSite.pack()
    newSite = tk.StringVar()
    newSiteEntry = tk.Entry(addSitemenu, textvariable=newSite)
    newSiteEntry.pack()

    #username
    labelnewusername = tk.Label(addSitemenu, text="Username: ")
    labelnewusername.pack()
    newusername = tk.StringVar()
    newusernameEntry = tk.Entry(addSitemenu, textvariable=newusername)
    newusernameEntry.pack()

    #password
    labelnewPassword = tk.Label(addSitemenu, text="Password: ")
    labelnewPassword.pack()
    newpassword = tk.StringVar()
    newpasswordEntry = tk.Entry(addSitemenu, textvariable=newpassword)
    newpasswordEntry.pack()

    button_submit = tk.Button(addSitemenu, text="Submit", command=getNewSite)
    button_submit.pack()
    
