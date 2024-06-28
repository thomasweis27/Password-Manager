
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
# 04/14 - More edit functionality
        # fix for pinned status on UI checkbutton
        # introduced new segment updateCredentialSet that will format new line;
        # and overwrite the previous credential set line in data
        # TO DO: write updateCredentialSet() function
# 04/14-2 - viewCredentialSet() tentatively complete
        # completed updateCredentialSet; 
        # new helpers to get a credential's index in data & overwrite it;
        # reformated removeFromDatabase() to work with these helpers
        # currently NO TO DO:
            # needs to be evaluated for efficiency;
            # lots of repeating code that may be tweaked if possible
# 04/16 - restored code from merge request #2
        # TO DO: review encryption on the following blocks:
            # editCredentialSet()
            # updateCredentialSet()
            # Subsequently:
                # wipeBlankLines()
                # findLineInFile()
                # overwriteLineInFile()

#_____________________________________________________________________________________________________

import tkinter as tk
from Decrypt import decrypt as dec

## helper functions of this component

#_____________________________________________________________________________________________________


# wipeBlankLines function
    # removes any blank lines from a passed file
def wipeBlankLines(file_dir):
    # text lines for later use
    text_lines = []
    # open the credentials file
    with open(file_dir, "r") as readfile:
        # read all the lines of the file into memory
        text_lines = readfile.readlines()
    # close the file
    readfile.close()
    # open data file in writing mode
    with open(file_dir, "w") as writefile:
        # write all non-whitespace lines
        for line in text_lines:
            # is line not whitespace?
            if not(line.isspace()):
                # write it into file
                writefile.write(line)
    # close the file
    writefile.close()


# findLineInData function
    # takes a user has and credential set name; 
    # finds that set in the file & returns its position (int)
def findLineInFile(user_hash, set_name):
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
                    if split_line[1] == set_name:
                        # this is the line that needs to be removed
                        break
            # one of the three checks failed; increment line index & continue
            target_index += 1
            continue
        # close the read file
        readfile.close()
    # return the target index
    return target_index


# overwriteLineInFile function
    # takes a target index and a credential set (in csv line format);
    # overwrites the existing line with the passed CSV line
def overwriteLineInFile(target_index, credential_csv):
    # text lines for later use
    text_lines = []
    # open the credentials file
    with open("credentials.txt", "r") as readfile:
        # read all the lines of the file into memory
        text_lines = readfile.readlines()
    # close file
    readfile.close()
    # open data file in writing mode
    with open("credentials.txt", "w") as writefile:
        # writefile index memory variable
        current_index = 1
        # go through each line and find the matching line index
        for line in text_lines:
            # do the indexes match
            if current_index == target_index:
                # yes; overwrite line
                writefile.write(credential_csv)
            # the indexes don't match
            else:
                # rewrite the original text
                writefile.write(line)
            # increment line index
            current_index += 1
    # close the file
    writefile.close()
    # cleanup any blank space in file
    wipeBlankLines("credentials.txt")


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
## flow of program: viewCredentialSet() <-> editCredentialSet() -> 
##                  updateCredentialSet() || 
##                  viewCredentialSet() <-> deleteCredentialSet() -> removeFromDatabase() 
## viewCredentialSet() will interface with accessCredentialSets()
## editCredentialSet() allows the user to edit any field on the set and save the changes
## deleteCredentialSet() allows user to delete sets from their list; forces confirmation
## updateCredentialSet() takes values input by the user in editCredentialSet() and writes it to data
## removeFromDatabase() takes a credential set and removes it from the database file
## segments are declared and defined in reverse order

#_____________________________________________________________________________________________________


# updateCredentialSet function
    # takes gathered information from the edit screen;
    # checks for any edited values and updates the set in data
def updateCredentialSet(user_hash, editCredentialScreen, credentialsMainScreen, 
        selected_set, new_username, new_password, new_security1, new_security2, 
        new_security3, new_add_info, new_pinned_status):
    # check for changes in each field
    # username
    if new_username == "":
        # the user has not made a change to the username; set new_username to original
        new_username = selected_set[2]
    # password
    if new_password == "":
        # the user has not made a change to the password; set new_password to original
        new_password = selected_set[3]
    # security1
    if new_security1 == "":
        # the user has not made a change to security1; set new_security1 to original
        new_security1 = selected_set[5]
    # security2
    if new_security2 == "":
        # the user has not made a change to security2; set new_security2 to original
        new_security2 = selected_set[7]
    # security3
    if new_security3 == "":
        # the user has not made a change to security3; set new_security3 to original
        new_security3 = selected_set[9]
    # additional info
    if new_add_info == "":
        # the user has not made a change to additional info; set new_add_info to original
        new_add_info = selected_set[10]
    # pinned status
    selected_set[11] = new_pinned_status
    # show the user the edited credential set
    tk.messagebox.showinfo("Edit Set", "Edited Information for " + selected_set[1] 
        + "\nUsername: " + new_username + "\nPassword: " + new_password 
        + "\nSecurity questions:\n" + new_security1 + "\n" + new_security2 + "\n" + new_security3 
        + "\nAdditional info: " + new_add_info + "\nPinned: " + str(new_pinned_status))
    # format the new credential into csv
    new_username = new_username.lower()
    new_password = new_password.lower()
    new_security1 = new_security1.lower()
    new_security2 = new_security2.lower()
    new_security3 = new_security3.lower()
    new_add_info = new_add_info.lower()
    # format the gathered information into a single CSV line
    data_line_output = ""
    # start by adding the current user's hash
    # placeholder code for now
    data_line_output += "\n" + user_hash + ","
    # service name, username, password
    data_line_output += selected_set[1] + "," + new_username + "," + new_password + ","
    # security questions
    # set active flags for each security question
    if new_security1:
        security1_active = True
    else:
        security1_active = False
    if new_security2:
        security2_active = True
    else:
        security2_active = False
    if new_security3:
        security3_active = True
    else:
        security3_active = False
    data_line_output += str(security1_active) + "," + new_security1 + ","
    data_line_output += str(security2_active) + "," + new_security2 + ","
    data_line_output += str(security3_active) + "," + new_security3 + ","
    # additional info, pinned status
    data_line_output += new_add_info + "," + str(new_pinned_status) + "$"
    # find the credential in the data file
    target_index = findLineInFile(user_hash, selected_set[1])
    # overwrite the set
    overwriteLineInFile(target_index, data_line_output)
    # return to the credential main screen
    # maximize the credentialsMainScreen
    credentialsMainScreen.deiconify()
    # minimize the view window
    editCredentialScreen.withdraw()


# editCredentialSet function
    # allows user to update or remove any information fields of the set
    # user can move directly from edit to delete
def editCredentialSet(user_hash, inputtedPassword, viewCredentialScreen, credentialsMainScreen, selected_set):
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
    usernameFieldEntry = tk.StringVar()
    usernameField = tk.Entry(editCredentialScreen, textvariable = usernameFieldEntry)
    usernameField.pack()
    # password
    passwordLabel = tk.Label(editCredentialScreen, text = "Current Password: " + selected_set[3])
    passwordLabel.pack()
    passwordFieldEntry = tk.StringVar()
    passwordField = tk.Entry(editCredentialScreen, textvariable = passwordFieldEntry)
    passwordField.pack()
    # security 1
    security1Label = tk.Label(editCredentialScreen, text = "Current Security Question 1:\n" 
        + selected_set[5])
    security1Label.pack()
    security1FieldEntry = tk.StringVar()
    security1Field = tk.Entry(editCredentialScreen, textvariable = security1FieldEntry)
    security1Field.pack()
    # security 2
    security2Label = tk.Label(editCredentialScreen, text = "Current Security Question 2:\n" 
        + selected_set[7])
    security2Label.pack()
    security2FieldEntry = tk.StringVar()
    security2Field = tk.Entry(editCredentialScreen, textvariable = security2FieldEntry)
    security2Field.pack()
    # security 3
    security3Label = tk.Label(editCredentialScreen, text = "Current Security Question 3:\n" 
        + selected_set[9])
    security3Label.pack()
    security3FieldEntry = tk.StringVar()
    security3Field = tk.Entry(editCredentialScreen, textvariable = security3FieldEntry)
    security3Field.pack()
    # additional information
    addInfoLabel = tk.Label(editCredentialScreen, text = "Current Additional Info:\n"
        + selected_set[10])
    addInfoLabel.pack()
    addInfoFieldEntry = tk.StringVar()
    addInfoField = tk.Entry(editCredentialScreen, textvariable = addInfoFieldEntry)
    addInfoField.pack()
    # pinned status
    pinnedStatusLabel = tk.Label(editCredentialScreen, text = "Currently Pinned?: ")
    pinnedStatusLabel.pack()
    # remove the $ end of string symbol from pinned_status
    # get a temporary value of pinned and create a status boolean variable
    temp_pinned = selected_set[11].replace("$", "")
    pinned_status = tk.BooleanVar()
    # add the checkbox to the UI, toggled on if set is already pinned
    pinnedButton = tk.Checkbutton(editCredentialScreen,
        variable = pinned_status, onvalue = True, offvalue = False, 
        command = lambda:pinnedStatusToggle(pinned_status))
    # if currently pinned
    if temp_pinned == "True":
        # set pinned_status button var to true; select box
        pinned_status.set(True)
        pinnedButton.select()
    else:
        # set pinned_status button var to false; deselect box
        pinned_status.set(False)
        pinnedButton.deselect()
    pinnedButton.pack()
    # save button (collect info)
    saveButton = tk.Button(editCredentialScreen, text = "Save",
        command = lambda:updateCredentialSet(user_hash, editCredentialScreen, 
        credentialsMainScreen, selected_set, usernameField.get(), 
        passwordField.get(), security1Field.get(), security2Field.get(), 
        security3Field.get(), addInfoField.get(), pinned_status.get()))
    saveButton.pack()
    # return to previous screen
    returnButton = tk.Button(editCredentialScreen, text = "<- Back", 
        command = lambda:returnToPrevious(editCredentialScreen, viewCredentialScreen))
    returnButton.pack(side = tk.BOTTOM)


# removeFromDatabase function
    # takes the passed (selected) credential set
    # finds and removes the set from the data file
def removeFromDatabase(inputtedPassword, credentialsMainScreen, viewCredentialScreen, confirmPopup, selected_set):
    # line index memory variable
    target_index = 1 #not 0??
    # text lines memory for later use
    text_lines = []
    # open the credentials file
    with open("credentials.txt", "r") as readfile:
        # read all the lines of the file into memory
        text_lines = readfile.readlines()
        # read every line of the file
        for line in readfile:
            print(line)
            try:
                print(line)
                dictionary = eval(line)
                #print(type(dictionary), "\n\n")
                #print(dictionary['salt'], "\n\n", dictionary['cipher_text'], "\n\n" , dictionary['nonce'], "\n\n", dictionary['tag'], "\n\n\n\n\n\n\n\n")
                line  = dec(dictionary, inputtedPassword)
                line = "$"+str(line)
                print(line)
                if selected_set in line:
                    # this is the line that needs to be removed
                        break
                else: 
                    #wrong line, find the right one
                    target_index += 1
            except:
                pass
    readfile.close()
    # close the read file
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
    tk.messagebox.showinfo("Delete Set", "Your set '" + selected_set[1] + "' has been deleted.")
    # maximize the credentialsMainScreen
    credentialsMainScreen.deiconify()
    # minimize the view window
    viewCredentialScreen.withdraw()


# deleteCredentialSet function
    # confirms the deletion with the user;
    # searches the file for the selected set and removes it
def deleteCredentialSet(inputtedPassword, credentialsMainScreen, viewCredentialScreen, selected_set):
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
        command = lambda:removeFromDatabase(inputtedPassword, credentialsMainScreen, viewCredentialScreen, confirmPopup, selected_set))
    confirmButton.pack()
    cancelButton = tk.Button(confirmPopup, text = "Cancel Deletion", 
        # minimizes the popup
        command = lambda:confirmPopup.withdraw())
    cancelButton.pack()


# viewCredentialSet function
    # opens a window showing the user all of the information on this specific set
def viewCredentialSet(user_hash, inputtedPassword, credentialsMainScreen, previousWindow, selected_set):
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
        command = lambda:editCredentialSet(user_hash, inputtedPassword, viewCredentialScreen, credentialsMainScreen, selected_set))
    editSetButton.pack()
    # delete button
    deleteSetButton = tk.Button(viewCredentialScreen, text = "Delete Set",
        command = lambda:deleteCredentialSet(inputtedPassword, credentialsMainScreen, viewCredentialScreen, selected_set))
    deleteSetButton.pack()


def swapSet(enteredPassword, currentHash, userSites):
    with open("credentials.txt") as file:
        for line in file:
            print(line)
            try:
                dictionary = eval(line)
                line  = dec(dictionary, enteredPassword)
                line = "$"+str(line)
                if currentHash in line:
                    split_line = line.split(",")
                    userSites.append(split_line)
            except:
                pass
    # Close file
    file.close()