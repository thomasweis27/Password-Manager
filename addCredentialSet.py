
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
# 04/09 - More UI Implementation;
        # All UI elements present. Full functionality
        # TO DO: fix issues with security questions clearing even with values
            # fix functionality of pinned radial button
# 04/09-2 - Fixes for security question issues
        # Security questions hold their appropriate values
        # Pinned status properly toggles

#_____________________________________________________________________________________________________

import tkinter as tk
import Encrypt as enc

## helper functions of this component

#_____________________________________________________________________________________________________


# returnToPrevious function
    # allows user to return to the previous screen
def returnToPrevious(currentWindow, previousWindow):
    # minimize the current window
    currentWindow.withdraw()
    # show the previous window
    previousWindow.deiconify()


# clearInformation function
    # fixes issue with duplication of addCredential window upon clearing input
def clearInformation(user_hash, previousWindow, addCredentialScreen):
    # withdraw the existing addCredential window
    addCredentialScreen.withdraw()
    # call back to the beginning of the addCredential component
    addCredentialSet(user_hash, previousWindow)


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


# pinnedStatusToggle function
    # toggles the setting of the pinned status on checkbox interaction
def pinnedStatusToggle(pinned_status):
    if pinned_status.get() == False:
        pinned_status.set(True)
    else:
        pinned_status.set(False)


#_____________________________________________________________________________________________________

## Main Component Functions
## flow of program: addCredentialSet() -> gatherInfo() -> enforceConstraints() -> writeToData()
## addCredentialSets() will setup the UI
## gatherInfo() separates UI initialization from gathering of user info
## enforceConstraints() will make sure that the gathered info is valid
## writeToData() will format the information and add it to the database file
## segments are declared and defined in reverse order

#_____________________________________________________________________________________________________


# writeToData function
    # takes the successful credential set;
    # formats it to the proper data format;
    # writes that line to the database file
def writeToData(user_hash, name, username, password, security1_active, security1, 
        security2_active, security2, security3_active, security3, add_info, pinned_status):
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
    data_line_output += add_info + "," + str(pinned_status) + "$"
    # open the credentials data file
    credentials = open("credentials.txt", "a")
    # encrypt the line
    # data_line_output = enc.encrypt(data_line_output, "placeholder")
    # append the data to the file
    credentials.write(str(data_line_output))
    # close the credentials data file
    credentials.close()


# enforceConstraints function
    # single function call to enforce the constraints on
    # all fields of a credential set
def enforceConstraints(user_hash, name, username, password, 
    security1question, security1answer, security2question, security2answer, 
    security3question, security3answer, add_info, pinned_status):
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
    if not(validateInput(security1question, 128, "varchar", False)):
        # return failed security 1
        tk.messagebox.showinfo("Error", "Please make sure that security question 1 is 0-128 characters.")
        return False
    # check security answer 1
    if not(validateInput(security1answer, 128, "varchar", False)):
        # return failed security 1
        tk.messagebox.showinfo("Error", "Please make sure that security answer 1 is 0-128 characters.")
        return False
    # check security question 2
    if not(validateInput(security2question, 128, "varchar", False)):
        # return failed security 2
        tk.messagebox.showinfo("Error", "Please make sure that security question 2 is 0-128 characters.")
        return False
    # check security answer 2
    if not(validateInput(security2answer, 128, "varchar", False)):
        # return failed security 2
        tk.messagebox.showinfo("Error", "Please make sure that security answer 2 is 0-128 characters.")
        return False
    # check security question 3
    if not(validateInput(security3question, 128, "varchar", False)):
        # return failed security 3
        tk.messagebox.showinfo("Error", "Please make sure that security question 3 is 0-128 characters.")
        return False
    # check security answer 3
    if not(validateInput(security3answer, 128, "varchar", False)):
        # return failed security 3
        tk.messagebox.showinfo("Error", "Please make sure that security answer 3 is 0-128 characters.")
        return False
    # check additional info
    if not(validateInput(add_info, 2048, "varchar", False)):
        # return failed additional info
        tk.messagebox.showinfo("Error", "Please make sure that the additional info is less than 2048 characters.")
        return False
    # all fields are passed
    # process security questions
    if security1question:
        security1 = security1question + " = " + security1answer
        security1_active = True
    else:
        security1 = ""
        security1_active = False
    if security2question:
        security2 = security2question + " = " + security2answer
        security2_active = True
    else:
        security2 = ""
        security2_active = False
    if security3question:
        security3 = security3question + " = " + security3answer
        security3_active = True
    else:
        security3 = ""
        security3_active = False
    # show the user their new credential set
    tk.messagebox.showinfo("Add Set", "Success!\nAdding a new set:\n" 
        + name + "\nUsername: " + username + "\nPassword: " + password 
        + "\nSecurity questions:\n" + security1 + "\n" + security2 + "\n" + security3 
        + "\nAdditional info: " + add_info + "\nPinned: " + str(pinned_status))
    # last step - format line and write to data
    writeToData(user_hash, name, username, password, security1_active, security1, 
        security2_active, security2, security3_active, security3, add_info, pinned_status)


# gatherInformation function
    # separates the gathering of information from the initialization
    # prompts the user for information regarding their new set
def gatherInformation(user_hash, previousWindow, addCredentialScreen):
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
    # prompt for security 1
    security1Label = tk.Label(addCredentialScreen, text = "Enter Security Question & Answer (opt)")
    security1Label.pack()
    security1question = tk.StringVar()
    security1answer = tk.StringVar()
    security1questionEntry = tk.Entry(addCredentialScreen, textvariable = security1question)
    security1questionEntry.pack()
    security1answerEntry = tk.Entry(addCredentialScreen, textvariable = security1answer)
    security1answerEntry.pack()
    # prompt for security 2
    security2Label = tk.Label(addCredentialScreen, text = "Enter 2nd Security Question & Answer (opt)")
    security2Label.pack()
    security2question = tk.StringVar()
    security2answer = tk.StringVar()
    security2questionEntry = tk.Entry(addCredentialScreen, textvariable = security2question)
    security2questionEntry.pack()
    security2answerEntry = tk.Entry(addCredentialScreen, textvariable = security2answer)
    security2answerEntry.pack()
    # prompt for security 3
    security3Label = tk.Label(addCredentialScreen, text = "Enter 3rd Security Question & Answer (opt)")
    security3Label.pack()
    security3question = tk.StringVar()
    security3answer = tk.StringVar()
    security3questionEntry = tk.Entry(addCredentialScreen, textvariable = security3question)
    security3questionEntry.pack()
    security3answerEntry = tk.Entry(addCredentialScreen, textvariable = security3answer)
    security3answerEntry.pack()
    # prompt for the additional information
    # add additional info input
    addInfoLabel = tk.Label(addCredentialScreen, text = "Additional Info")
    addInfoLabel.pack()
    add_info = tk.StringVar()
    addInfoEntry = tk.Entry(addCredentialScreen, textvariable = add_info)
    addInfoEntry.pack()
    # pinned status radial here
    pinned_status = tk.BooleanVar()
    pinned_status.set(False)
    pinnedButton = tk.Checkbutton(addCredentialScreen, text = "Pin Set on Creation?",
        variable = pinned_status, onvalue = True, offvalue = False, 
        command = lambda:pinnedStatusToggle(pinned_status))
    pinnedButton.pack()
    # add credential button (finalize)
    finalizeButton = tk.Button(addCredentialScreen, text = "Submit", 
        command = lambda:enforceConstraints(user_hash, 
        nameEntry.get(), usernameEntry.get(), passwordEntry.get(),
        security1questionEntry.get(), security1answerEntry.get(), security2questionEntry.get(), 
        security2answerEntry.get(), security3questionEntry.get(), security3answerEntry.get(), 
        addInfoEntry.get(), pinned_status.get()))
    finalizeButton.pack()
    # add clear button
    clearButton = tk.Button(addCredentialScreen, text = "Clear",
        command = lambda:clearInformation(user_hash, previousWindow, addCredentialScreen))
    clearButton.pack()


# primary function (component driver, called from system driver)
def addCredentialSet(user_hash, previousWindow):    
    # minimize previous screen
    previousWindow.withdraw()
    # create new window through tk; assign attributes
    addCredentialScreen = tk.Tk()
    addCredentialScreen.title("Password Manager")
    addCredentialScreen.geometry("800x675")
    # create label for the UI
    addCredLabel = tk.Label(addCredentialScreen, text = "Add New Credentials")
    # package this into the UI
    addCredLabel.pack()
    # return to previous screen
    returnButton = tk.Button(addCredentialScreen, text = "<- Back", 
        command = lambda:returnToPrevious(addCredentialScreen, previousWindow))
    returnButton.pack(side = tk.BOTTOM)
    # move to next segment (gather info)
    gatherInformation(user_hash, previousWindow, addCredentialScreen)
