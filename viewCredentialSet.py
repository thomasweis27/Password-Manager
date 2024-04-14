
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
# 04/12-2 - Delete functionality completed
        # TO DO: Implement all of editCredentialSet() function
# 04/13 - Edit Functionality partially implemented
        # UI is fully implemented; backend needs work.
        # TO DO: Implement retrieval of new info
        # check for blank entries and don't overwrite them.
        # write new credential set information line to the set's position in file
        # fix pinned status function on UI (checkbutton)

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


# pinnedStatusToggle function
    # toggles the setting of the pinned status on checkbox interaction
def pinnedStatusToggle(pinned_status):
    if pinned_status.get() == False:
        pinned_status.set(True)
    else:
        pinned_status.set(False)


#_____________________________________________________________________________________________________

## Main Component Functions
## flow of program: viewCredentialSet() <-> editCredentialSet() <-> deleteCredentialSet()
## viewCredentialSet() will interface with accessCredentialSets()
## editCredentialSet() allows the user to edit any field on the set and save the changes
## deleteCredentialSet() allows user to delete sets from their list; forces confirmation
## segments are declared and defined in reverse order

#_____________________________________________________________________________________________________


# editCredentialSet function
    # allows user to update or remove any information fields of the set
    # user can move directly from edit to delete
def editCredentialSet(user_hash, viewCredentialScreen, selected_set):
    print("editCredentialSet(): WIP function")
    # close previous window
    viewCredentialScreen.withdraw()
    # create new window through tk; assign attributes
    editCredentialScreen = tk.Tk()
    editCredentialScreen.title("Password Manager")
    editCredentialScreen.geometry("800x675")
    # create label for the UI
    editCredLabel = tk.Label(editCredentialScreen, text = selected_set[1])
    # package this into the UI
    editCredLabel.pack()
    # tell the user what they are seeing
    infoLabel = tk.Label(editCredentialScreen, text = "Enter text in any of the boxes"
        + " to change that piece of information.\nClick 'Save' when you have finished your edits.")
    infoLabel.pack()
    # entry fields for each info field
    # username
    usernameLabel = tk.Label(editCredentialScreen, text = "Current Username: " + selected_set[2])
    usernameLabel.pack()
    usernameField = tk.Entry(editCredentialScreen)
    usernameField.pack()
    usernameFieldEntry = tk.StringVar()
    # password
    passwordLabel = tk.Label(editCredentialScreen, text = "Current Password: " + selected_set[3])
    passwordLabel.pack()
    passwordField = tk.Entry(editCredentialScreen)
    passwordField.pack()
    passwordFieldEntry = tk.StringVar()
    # security 1
    security1Label = tk.Label(editCredentialScreen, text = "Current Security Question 1:\n" 
        + selected_set[5])
    security1Label.pack()
    security1Field = tk.Entry(editCredentialScreen)
    security1Field.pack()
    security1FieldEntry = tk.StringVar()
    # security 2
    security2Label = tk.Label(editCredentialScreen, text = "Current Security Question 2:\n" 
        + selected_set[7])
    security2Label.pack()
    security2Field = tk.Entry(editCredentialScreen)
    security2Field.pack()
    security2FieldEntry = tk.StringVar()
    # security 3
    security3Label = tk.Label(editCredentialScreen, text = "Current Security Question 3:\n" 
        + selected_set[9])
    security3Label.pack()
    security3Field = tk.Entry(editCredentialScreen)
    security3Field.pack()
    security3FieldEntry = tk.StringVar()
    # additional information
    addInfoLabel = tk.Label(editCredentialScreen, text = "Current Additional Info:\n"
        + selected_set[10])
    addInfoLabel.pack()
    addInfoField = tk.Entry(editCredentialScreen)
    addInfoField.pack()
    addInfoFieldEntry = tk.StringVar()
    # pinned status
    pinnedStatusField = tk.Label(editCredentialScreen, text = "Currently Pinned?: " 
        # removes the $ end of string symbol
        + (selected_set[11]).replace("$", ""))
    pinnedStatusField.pack()
    pinned_status = selected_set[11].replace("$", "")
    if pinned_status == "True":
        pinned_status = tk.BooleanVar()
        pinned_status.set(True)
    else:
        pinned_status = tk.BooleanVar()
        pinned_status.set(False)
    pinnedButton = tk.Checkbutton(editCredentialScreen,
        variable = pinned_status, onvalue = True, offvalue = False, 
        command = lambda:pinnedStatusToggle(pinned_status))
    pinnedButton.pack()
    # return to previous screen
    returnButton = tk.Button(viewCredentialScreen, text = "<- Back", 
        command = lambda:returnToPrevious(editCredentialScreen, viewCredentialScreen))
    returnButton.pack(side = tk.BOTTOM)


# removeFromDatabase function
    # takes the passed (selected) credential set
    # finds and removes the set from the data file
def removeFromDatabase(user_hash, credentialsMainScreen, viewCredentialScreen, confirmPopup, selected_set):
    # line index memory variable
    target_index = 1
    # text lines memory for later use
    text_lines = []
    # open the credentials file
    with open("credentials.txt", "r") as readfile:
        # read all the lines of the file into memory
        text_lines = readfile.readlines()
        # read every line of the file
        for line in text_lines:
            # decrypt the line
            #
            # ignore any commented lines
            if not(line.startswith("$")):
                # get the line's hash
                split_line = line.split(",")
                # ignore lines that don't match hashes
                if split_line[0] == user_hash:
                    # ignore lines that don't match names
                    if split_line[1] == selected_set[1]:
                        # this is the line that needs to be removed
                        break
            # one of the three checks failed; increment line index & continue
            target_index += 1
            continue
        # close the read file
        readfile.close()
    # target line is known; re-open the file in writing mode
    with open("credentials.txt", "w") as writefile:
        # writefile index memory variable
        current_index = 1
        # go through each line and find the matching line index
        for line in text_lines:
            # re-write every line UNLESS the indexes match
            if not(current_index == target_index):
                # rewrite the line
                writefile.write(line)
            # increment line index
            current_index += 1
    # close the file
    writefile.close()
    # minimize the confirm popup
    confirmPopup.withdraw()
    # notify that the set has been deleted
    tk.messagebox.showinfo("Error", "Your set '" + selected_set[1] + "' has been deleted.")
    # maximize the credentialsMainScreen
    credentialsMainScreen.deiconify()
    # minimize the view window
    viewCredentialScreen.withdraw()


# deleteCredentialSet function
    # confirms the deletion with the user;
    # searches the file for the selected set and removes it
def deleteCredentialSet(user_hash, credentialsMainScreen, viewCredentialScreen, selected_set):
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
        command = lambda:removeFromDatabase(user_hash, credentialsMainScreen, viewCredentialScreen, confirmPopup, selected_set))
    confirmButton.pack()
    cancelButton = tk.Button(confirmPopup, text = "Cancel Deletion", 
        # minimizes the popup
        command = lambda:confirmPopup.withdraw())
    cancelButton.pack()


# viewCredentialSet function
    # opens a window showing the user all of the information on this specific set
def viewCredentialSet(user_hash, credentialsMainScreen, previousWindow, selected_set):
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
        command = lambda:editCredentialSet(user_hash, viewCredentialScreen, selected_set))
    editSetButton.pack()
    # delete button
    deleteSetButton = tk.Button(viewCredentialScreen, text = "Delete Set",
        command = lambda:deleteCredentialSet(user_hash, credentialsMainScreen, viewCredentialScreen, selected_set))
    deleteSetButton.pack()
    # move to next segment