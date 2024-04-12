
#_____________________________________________________________________________________________________
## COMPONENT DESCRIPTION AND HISTORY

# viewCredentialSets component
    # allows user to view the information on a set;
    # allows user to edit their set or delete it
# 04/12 - Initial implementation; full UI design
        # module's UI is fully implemented but some aspects are WIP
        # user can view all the information attached to a set;
        # can interact with edit/delete options, confirm or cancel a deletion.
        # TO DO: Implement all of editCredentialSet() function;
        # complete implementation of deleteCredentialSet() function
            # all that is needed is the actual deletion after confirmation

#_____________________________________________________________________________________________________

import tkinter as tk

## helper functions of this component

#_____________________________________________________________________________________________________


# returnToPrevious function
    # allows user to return to the previous screen
def returnToPrevious(currentWindow, previousWindow):
    # minimize the current window
    currentWindow.withdraw()
    # show the previous window
    previousWindow.deiconify()


#_____________________________________________________________________________________________________

## Main Component Functions
## flow of program: viewCredentialSet() <-> editCredentialSet() <-> deleteCredentialSet()
## viewCredentialSet() will interface with accessCredentialSets()
## deleteCredentialSet() allows user to delete sets from their list; forces confirmation
## segments are declared and defined in reverse order

#_____________________________________________________________________________________________________


# editCredentialSet function
    # allows user to update or remove any information fields of the set
    # user can move directly from edit to delete
def editCredentialSet():
    print("editCredentialSet(): WIP function")


# deleteCredentialSet function
    # confirms the deletion with the user;
    # searches the file for the selected set and removes it
def deleteCredentialSet(user_hash, viewCredentialScreen, selected_set):
    # create new popup for user to confirm or deny deletion
    confirmPopup = tk.Tk()
    confirmPopup.title("Password Manager")
    confirmPopup.geometry("400x225")
    # inform the user of their choice's effects
    confirmLabel = tk.Label(confirmPopup, text = "Are you sure you want to delete " 
        + selected_set[1] + "?\nThis action cannot be undone and the set will be lost forever.")
    confirmLabel.pack()
    # confirm/cancel buttons
    confirmButton = tk.Button(confirmPopup, text = "Confirm Deletion",
        # TO DO: finalize deletion
        command = lambda:tk.messagebox.showinfo("Error", "This button is WIP"))
    confirmButton.pack()
    cancelButton = tk.Button(confirmPopup, text = "Cancel Deletion", 
        # minimizes the popup
        command = lambda:confirmPopup.withdraw())
    cancelButton.pack()


# viewCredentialSet function
    # opens a window showing the user all of the information on this specific set
def viewCredentialSet(user_hash, previousWindow, selected_set):
    # close previous window
    previousWindow.withdraw()
    # create new window through tk; assign attributes
    viewCredentialScreen = tk.Tk()
    viewCredentialScreen.title("Password Manager")
    viewCredentialScreen.geometry("800x450")
    # create label for the UI
    viewCredLabel = tk.Label(viewCredentialScreen, text = selected_set[1])
    # package this into the UI
    viewCredLabel.pack()
    # tell the user what they are seeing
    infoLabel = tk.Label(viewCredentialScreen, text = "Click 'Edit' to change"
        + " any attribute of this set. \nClick 'Delete' to remove the set from your list.")
    infoLabel.pack()
    # display all information
    # username
    usernameLabel = tk.Label(viewCredentialScreen, text = "Username: " + selected_set[2])
    usernameLabel.pack()
    # password
    passwordLabel = tk.Label(viewCredentialScreen, text = "Password: " + selected_set[3])
    passwordLabel.pack()
    # security 1 (only if the security question is active)
    if selected_set[4] == "True":
        security1Label = tk.Label(viewCredentialScreen, text = "Security Question 1:\n" 
            + selected_set[5])
        security1Label.pack()
    # security 2 (only if the security question is active)
    if selected_set[6] == "True":
        security2Label = tk.Label(viewCredentialScreen, text = "Security Question 2:\n" 
            + selected_set[7])
        security2Label.pack()
    # security 3 (only if the security question is active)
    if selected_set[8] == "True":
        security3Label = tk.Label(viewCredentialScreen, text = "Security Question 3:\n" 
            + selected_set[9])
        security3Label.pack()
    # additional information
    addInfoLabel = tk.Label(viewCredentialScreen, text = "Additional Info:\n"
        + selected_set[10])
    addInfoLabel.pack()
    # pinned status
    pinnedStatusLabel = tk.Label(viewCredentialScreen, text = "Pinned?: " 
        # removes the $ end of string symbol
        + (selected_set[11]).replace("$", ""))
    pinnedStatusLabel.pack()
    # return to previous screen
    returnButton = tk.Button(viewCredentialScreen, text = "<- Back", 
        command = lambda:returnToPrevious(viewCredentialScreen, previousWindow))
    returnButton.pack(side = tk.BOTTOM)
    # edit button
    editSetButton = tk.Button(viewCredentialScreen, text = "Edit Set",
        # TO DO: implement edit functionality
        command = lambda:tk.messagebox.showinfo("Error", "This button is WIP"))
    editSetButton.pack()
    # delete button
    deleteSetButton = tk.Button(viewCredentialScreen, text = "Delete Set",
        command = lambda:deleteCredentialSet(user_hash, viewCredentialScreen, selected_set))
    deleteSetButton.pack()
    # move to next segment