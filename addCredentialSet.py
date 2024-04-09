
#_____________________________________________________________________________________________________
## COMPONENT DESCRIPTION AND HISTORY

# addCredentialSet component
    # allows user to create a new credential set;
    # prompts the user for all possible information on the set
    # service name, username, password
    # 3 possible security questions with a type and "question = answer" field
    # additional info, and whether the user would like to set the set as "pinned"
# 04/01 - this will be modified to plug into the system more modularly once we know
        # how we want to set everything up (possibly after a driver, etc.)
# 04/01 - working on enforcing the [A-Z a-z 0-9 common special character] 
        # input constraints. More research...
        # 04/03 - resolved with isVarchar function
# 04/05-07 - UI implementation; 
        # proof-of-concept console program replaced by proper UI program
        # broken into 3 main segments
        # TO DO: need to add radial buttons for security questions and inputs;
            # pinned status as well

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


# isVarchar function
    # checks that the passed value (string) is a varchar
def isVarchar(string):
    # regexpression for symbols
    varchar_regex = " !@#$%^&*()+_-=}{[]:\|,./<>?;'<>?"
    # iterate over every character in the string
    for char in string:
        # check that the character is alphanumeric OR symbol
        if not(char.isalnum() or (char in varchar_regex)):
            # this passed string is not a varchar
            return False
    # if the function passes over all chars and does not encounter issues
    # passed string is indeed a varchar
    return True


# validateInput function
    # checks the passed value against a pair of constraints
    # maximum length constraint and format constraint
        # format modes are alphanumeric and varchar
    # forcedEntry field indicates that the length cannot be 0
def validateInput(value, max_length, format_mode, forced_entry):
    value = str(value)
    print("Testing " + value + " as " + format_mode + " with length " + str(max_length) + " and requirement as " + str(forced_entry))
    # test length of input string
    if forced_entry:
        # if entry is forced, length of value must be between 1 and max_length
        if not((len(value) > 0) and (len(value) < max_length)):
            # value does not pass length requirement
            return False
    # entry isn't required, 0 - max length
    else:
        if not(len(value) < max_length):
            # value is too large
            return False
    # test formatting
    # alphanumeric mode
    if format_mode == "alphanumeric":
        # test for alphanumeric formatting
        if not(all(char.isalnum() or char.isspace() for char in value)):
            # value isn't alphanumeric
            return False
    # varchar mode
    else:
        # test varchar formatting
        if not(isVarchar(value)):
            # value isn't varchar
            return False
    # both checks are passed, valid value
    return True


#_____________________________________________________________________________________________________

## Main Component Functions
## flow of program: addCredentialSet() -> enforceConstraints() -> writeToData()
## addCredentialSets() will setup the UI and gather the info from the user
## enforceConstraints() will make sure that the gathered info is valid
## writeToData() will format the information and add it to the database file
## segments are declared and defined in reverse order

#_____________________________________________________________________________________________________


# writeToData function
    # takes the successful credential set;
    # formats it to the proper data format;
    # writes that line to the database file
def writeToData(addCredentialScreen, user_hash, name, username, password, security1_active, security1, security2_active, security2, 
                security3_active, security3, add_info, pinned):
    # force the entire input into a lowercase form
    # the boolean value fields (security questions active & pinned status) can't be;
    # True and False must be capitalized
    name = name.lower()
    username = username.lower()
    password = password.lower()
    security1 = security1.lower()
    security2 = security2.lower()
    security3 = security3.lower()
    add_info = add_info.lower()
    # format the gathered information into a single CSV line
    data_line_output = ""
    # start by adding the current user's hash
    # placeholder code for now
    data_line_output += "\n" + user_hash + ","
    # service name, username, password
    data_line_output += name + "," + username + "," + password + ","
    # security questions
    data_line_output += str(security1_active) + "," + security1 + ","
    data_line_output += str(security2_active) + "," + security2 + ","
    data_line_output += str(security3_active) + "," + security3 + ","
    # additional info, pinned status
    data_line_output += add_info + "," + str(pinned) + "$"
    # encrypt the line
    #
    # open the credentials data file
    credentials = open("credentials.txt", "a")
    # append the data to the file
    credentials.write(data_line_output)
    # close the credentials data file
    credentials.close()


# enforceConstraints function
    # single function call to enforce the constraints on
    # all fields of a credential set
def enforceConstraints(addCredentialScreen, user_hash, name, username, password, security1, security2, security3, add_info, pinned):
    # check the name
    if not(validateInput(name, 32, "alphanumeric", True)):
        # return failed site name
        tk.messagebox.showinfo("Error", "Please make sure that the site name is 1-32 characters and alphanumeric.")
        return False
    # check the username
    if not(validateInput(username, 48, "varchar", True)):
        # return failed username
        tk.messagebox.showinfo("Error", "Please make sure that the username is 1-48 characters.")
        return False
    # check the password
    if not(validateInput(password, 48, "varchar", True)):
        # return failed password
        tk.messagebox.showinfo("Error", "Please make sure that the password is 1-48 characters.")
        return False
    # check security question 1
    if not(validateInput(security1, 256, "varchar", True)):
        # return failed security 1
        tk.messagebox.showinfo("Error", "Please make sure that security question 1 is 1-256 characters.")
        return False
    # check security question 2
    if not(validateInput(security2, 256, "varchar", True)):
        # return failed security 2
        tk.messagebox.showinfo("Error", "Please make sure that security question 2 is 1-256 characters.")
        return False
    # check security question 3
    if not(validateInput(security3, 256, "varchar", True)):
        # return failed security 3
        tk.messagebox.showinfo("Error", "Please make sure that security question 3 is 1-256 characters.")
        return False
    # check additional info
    if not(validateInput(add_info, 256, "varchar", False)):
        # return failed additional info
        tk.messagebox.showinfo("Error", "Please make sure that the additional info is less than 2048 characters.")
        return False
    # all fields are passed
    tk.messagebox.showinfo("Error", "Success\nAdding " + name + " with " + username + " and " + password + "\n" + " security questions " + security1 + ", " + security2 + ", " + security3 + "\nAdditional info: " + add_info)
    # set the security question status fields
    security1_active = False
    security2_active = False
    security3_active = False
    if security1:
        security1_active = True
        if security2:
            security2_active = True
            if security3:
                security3_active = True
    # last step - format line and write to data
    writeToData(addCredentialScreen, user_hash, name, username, password, security1_active, security1, 
                security2_active, security2, security3_active, security3, add_info, pinned)


# primary function (component driver, called from system driver)
def addCredentialSet(current_user, previousWindow):    
    # minimize previous screen
    previousWindow.withdraw()
    # create new window through tk; assign attributes
    addCredentialScreen = tk.Tk()
    addCredentialScreen.title("Password Manager")
    addCredentialScreen.geometry("800x450")
    # create label for the UI
    addCredLabel = tk.Label(addCredentialScreen, text = "Add New Credentials")
    # package this into the UI
    addCredLabel.pack()
    # tell the user that they will need x data (listed above) to create the new set
    infoLabel = tk.Label(addCredentialScreen, text = "Please have the following information ready:\n"
        + "Service/Site name, Username, Password\n"
        + "Any Security Questions (3 max), and Any additional information regarding the site.")
    infoLabel.pack()
    # prompt for the service name
    # add service name input
    nameLabel = tk.Label(addCredentialScreen, text = "Site Name")
    nameLabel.pack()
    name = tk.StringVar()
    nameEntry = tk.Entry(addCredentialScreen, textvariable = name)
    nameEntry.pack()
    # prompt for the username
    # add username input
    usernameLabel = tk.Label(addCredentialScreen, text = "Username")
    usernameLabel.pack()
    username = tk.StringVar()
    usernameEntry = tk.Entry(addCredentialScreen, textvariable = username)
    usernameEntry.pack()
    # prompt for the password
    # add password input
    passwordLabel = tk.Label(addCredentialScreen, text = "Password")
    passwordLabel.pack()
    password = tk.StringVar()
    passwordEntry = tk.Entry(addCredentialScreen, textvariable = password)
    passwordEntry.pack()
    # security 1 radial here
    # prompt for the input of security 1
    # add security question input
    security1 = "test"
    # security 2 radial here
    # prompt for the input of security 2
    # add security question input
    security2 = "test"
    # security 3 radial here
    # prompt for the input of security 3
    # add security question input
    security3 = "test"
    # prompt for the additional information
    # add additional info input
    addInfoLabel = tk.Label(addCredentialScreen, text = "Additional Info")
    addInfoLabel.pack()
    add_info = tk.StringVar()
    addInfoEntry = tk.Entry(addCredentialScreen, textvariable = add_info)
    addInfoEntry.pack()
    # pinned status radial here
    pinned = False
    # add credential button (finalize)
    finalizeButton = tk.Button(addCredentialScreen, text = "Submit", 
        command = lambda:enforceConstraints(addCredentialScreen, current_user, nameEntry.get(), usernameEntry.get(), passwordEntry.get(),
        security1, security2, security3, addInfoEntry.get(), pinned))
    finalizeButton.pack()
    # return to previous screen
    returnButton = tk.Button(addCredentialScreen, text = "<- Back", 
        command = lambda:returnToPrevious(addCredentialScreen, previousWindow))
    returnButton.pack(side = tk.BOTTOM)
