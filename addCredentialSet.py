

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

import tkinter as tk

# functions of this component

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

# addCredentialSet function
    # allows the user to add a new credential set to their list
def addCredentialSet():    
    # initialize variables
    name = ""
    username = ""
    password = ""
    security1_active = False
    security1 = ""
    security2_active = False
    security2 = ""
    security3_active = False
    security3 = ""
    add_info = ""
    pinned = False
    # placeholder code
    current_user = "00000000"
    # pseudo
    # tell the user that they will need x data (listed above) to create the new set
    print("Adding a new credential set...\nPlease have the following information ready:\n"
        + "   1. Service/Site name\n   2. Username\n   3. Password\n"
        + "   4. Security Questions (3 max)\n   5. Any additional information regarding the site")
    # prompt loop for the service name (alphanumerical value that is <= 32 chars)
    while(True):
        # prompt user for input of name and save their input
        print("   Please enter the name of the service: ", end = '')
        inp = input()
        # enforce type constraints and require application of a value to this field
        # is input alphanumerical?
        if not (inp.isalnum()):
            print("   This is an invalid name. Please use only letters and numbers.")
            continue
        # is input less than or equal to 32 characters but not empty?
        if (len(inp) > 32) or (len(inp) <= 0):
            print("   This is an invalid name. Please enter a name that is between 1 and 32 characters in length.")
            continue
        # the name is alphanumerical and between 1-32 chars, valid name
        # lower the input for consistency and assign it to name
        inp = inp.lower()
        name = inp
        # escape prompt loop once a valid name is given
        break
    # prompt loop for the username (variable character (a-z, 0-9, symbols) value <= 48 chars)
    while(True):
        # prompt user for input of username and save their input
        print("   Please enter the username: ", end = '')
        inp = input()
        # enforce type constraints and require application of a value to this field
        # is input less than or equal to 48 characters but not empty?
        if (len(inp) > 48) or (len(inp) <= 0):
            print("   This is an invalid username. Please enter a username that is between 1 and 48 characters in length.")
            continue
        # is input varchar?
        if isVarchar(inp) == False:
            # this is an invalid input
            print("   This is an invalid username. Please enter a username that does not use restricted characters.")
            continue
        # the input is a valid username
        # lower the input for consistency and assign it to username
        inp = inp.lower()
        username = inp
        # escape prompt loop once a valid username is given
        break
    # prompt loop for the password (variable character (a-z, 0-9, symbols) value <= 48 chars)
    while(True):
        # prompt user for input of password and save their input
        print("   Please enter the password: ", end = '')
        inp = input()
        # enforce type constraints and require application of a value to this field
        # is input less than or equal to 48 characters but not empty?
        if (len(inp) > 48) or (len(inp) <= 0):
            print("   This is an invalid password. Please enter a password that is between 1 and 48 characters in length.")
            continue
        # is input varchar?
        if isVarchar(inp) == False:
            # this is an invalid input
            print("   This is an invalid password. Please enter a password that does not use restricted characters.")
            continue
        # the input is a valid password
        # lower the input for consistency and assign it to password
        inp = inp.lower()
        password = inp
        # escape prompt loop once a valid name is given
        break
    # security questions (nested)
    # prompt loop for the activation of the 1st security question
    while(True):
        # prompt if the user wants to add the first security question
        print("   Would you like to add a security question? (Y/N): ", end = '')
        inp = input()
        inp = inp.lower()
        # check that the user input y/n
        if inp == 'n':
            # user does not need any security questions, break out of loop
            break
        elif inp == 'y':
            # user does want to add the first security question
            security1_active = True
            print("   Adding security question.")
            # prompt loop for input of the question (variable character (a-z, 0-9, symbols) value <= 128 chars)
            while(True):
                print("      Please enter the question: ", end = '')
                inp = input()
                inp = inp.lower()
                # enforce type constraints and require application of a value to this field
                # is input less than or equal to 128 but not empty?
                if (len(inp) > 0) and (len(inp) <= 128):
                    # is input varchar?
                    if isVarchar(inp) == False:
                        # this is an invalid input
                        print("      This is an invalid question. Please enter a question that does not use restricted characters.")
                        continue
                    # question is of valid format; add the question to the security 1 field
                    security1 = inp
                    break
                # otherwise the input is not valid
                else:
                    print("      This is an invalid input. Please enter a security question less than 128 characters.")
                    continue
            # prompt loop for input of the answer (variable character (a-z, 0-9, symbols) value <= 128 chars)
            while(True):
                print("      Please enter the answer to " + security1 +": ", end = '')
                inp = input()
                inp = inp.lower()
                # enforce type constraints and require application of a value to this field
                # is input less than or equal to 128 but not empty?
                if (len(inp) > 0) and (len(inp) <= 128):
                    # is input varchar?
                    if isVarchar(inp) == False:
                        # this is an invalid input
                        print("      This is an invalid answer. Please enter an answer that does not use restricted characters.")
                        continue
                    # answer is of valid format; add the answer to the security 1 field
                    security1 = security1 + " = " + inp
                    break
                # otherwise the input is not valid
                else:
                    print("      This is an invalid input. Please enter an answer less than 128 characters.")
                    continue
            # prompt loop for the activation of the 2nd security question
            while(True):
                # prompt if the user wants to add the second security question
                print("   Would you like to add a 2nd security question? (Y/N): ", end = '')
                inp = input()
                inp = inp.lower()
                # check that the user input y/n
                if inp == 'n':
                    # user does not need a second security questions, break out of loop
                    break
                elif inp == 'y':
                    # user does want to add the second security question
                    security2_active = True
                    print("   Adding 2nd security question.")
                    # prompt loop for input of the question (variable character (a-z, 0-9, symbols) value <= 128 chars)
                    while(True):
                        print("      Please enter the question: ", end = '')
                        inp = input()
                        inp = inp.lower()
                        # enforce type constraints and require application of a value to this field
                        # is input less than or equal to 128 but not empty?
                        if (len(inp) > 0) and (len(inp) <= 128):
                            # is input varchar?
                            if isVarchar(inp) == False:
                                # this is an invalid input
                                print("      This is an invalid question. Please enter a question that does not use restricted characters.")
                                continue
                            # question is of valid format; add the question to the security 1 field
                            security2 = inp
                            break
                        # otherwise the input is not valid
                        else:
                            print("      This is an invalid input. Please enter a security question less than 128 characters.")
                            continue
                    # prompt loop for input of the answer (variable character (a-z, 0-9, symbols) value <= 128 chars)
                    while(True):
                        print("      Please enter the answer to " + security2 +": ", end = '')
                        inp = input()
                        inp = inp.lower()
                        # enforce type constraints and require application of a value to this field
                        # is input less than or equal to 128 but not empty?
                        if (len(inp) > 0) and (len(inp) <= 128):
                            # is input varchar?
                            if isVarchar(inp) == False:
                                # this is an invalid input
                                print("      This is an invalid answer. Please enter an answer that does not use restricted characters.")
                                continue
                            # answer is of valid format; add the answer to the security 2 field
                            security2 = security2 + " = " + inp
                            break
                        # otherwise the input is not valid
                        else:
                            print("      This is an invalid input. Please enter an answer less than 128 characters.")
                            continue
                    # prompt loop for the activation of the 3rd security question
                    while(True):
                        # prompt if the user wants to add the third security question
                        print("   Would you like to add a 3rd security question? (Y/N): ", end = '')
                        inp = input()
                        inp = inp.lower()
                        # check that the user input y/n
                        if inp == 'n':
                            # user does not need any security questions, break out of loop
                            break
                        elif inp == 'y':
                            # user does want to add the first security question
                            security3_active = True
                            print("   Adding 3rd security question.")
                            # prompt loop for input of the question (variable character (a-z, 0-9, symbols) value <= 128 chars)
                            while(True):
                                print("      Please enter the question: ", end = '')
                                inp = input()
                                inp = inp.lower()
                                # enforce type constraints and require application of a value to this field
                                # is input less than or equal to 128 but not empty?
                                if (len(inp) > 0) and (len(inp) <= 128):
                                    # is input varchar?
                                    if isVarchar(inp) == False:
                                        # this is an invalid input
                                        print("      This is an invalid question. Please enter a question that does not use restricted characters.")
                                        continue
                                    # question is of valid format; add the question to the security 1 field
                                    security3 = inp
                                    break
                                # otherwise the input is not valid
                                else:
                                    print("      This is an invalid input. Please enter a security question less than 128 characters.")
                                    continue
                            # prompt loop for input of the answer (variable character (a-z, 0-9, symbols) value <= 128 chars)
                            while(True):
                                print("      Please enter the answer to " + security3 +": ", end = '')
                                inp = input()
                                inp = inp.lower()
                                # enforce type constraints and require application of a value to this field
                                # is input less than or equal to 128 but not empty?
                                if (len(inp) > 0) and (len(inp) <= 128):
                                    # is input varchar?
                                    if isVarchar(inp) == False:
                                        # this is an invalid input
                                        print("      This is an invalid answer. Please enter an answer that does not use restricted characters.")
                                        continue
                                    # answer is of valid format; add the answer to the security 1 field
                                    security3 = security3 + " = " + inp
                                    break
                                # otherwise the input is not valid
                                else:
                                    print("      This is an invalid input. Please enter an answer less than 128 characters.")
                                    continue
                        # otherwise the input is not valid
                        else:
                            print("   This is an invalid input. Please enter Y (yes) or N (no).")
                            continue
                        break
                # otherwise the input is not valid
                else:
                    print("   This is an invalid input. Please enter Y (yes) or N (no).")
                    continue
                break
        # otherwise the input is not valid
        else:
            print("   This is an invalid input. Please enter Y (yes) or N (no).")
            continue
        break   
    # prompt loop for the additional info (a-z 0-9 symbols <= 2048 chars)
    while(True):
        # prompt the user for input of any additional info and save the input
        # it is possible for this field to be blank
        print("   Please enter any additional information you would like to add (not required): ", end = '')
        inp = input()
        # enforce type constraints
        # is the input less than or equal to 2048?
        if (len(inp) > 2048):
            print("   This additional information exceeds the 2,048 character limit. Please enter a smaller value.")
            continue
        # is input varchar?
        if isVarchar(inp) == False:
            # this is an invalid input
            print("   This additional information is invalid. Please enter info that does not use restricted characters.")
            continue
        # the input is valid additional information
        # lower the input for consistency and assign it to add_info
        inp = inp.lower()
        add_info = inp
        # escape prompt loop once valid additional info is given
        break
    # prompt for the pinned status of the set (true/false)
    while(True):
        # prompt the user if they would like to pin the service immediately
        print("   Would you like to pin this set at creation? (Y/N): ", end = '')
        inp = input()
        inp = inp.lower()
        # check that the user input y/n
        if inp == 'n':
            # user does not want to pin the set, break
            break
        elif inp == 'y':
            # user does want to pin, set the pin value
            pinned = True
            break
        # otherwise the input is not valid
        else:
            print("   This is an invalid input. Please enter Y (yes) or N (no).")
            continue
    # feedback the new set and all of the information to the user
    print("You are adding a service with the following information:"
          + "\n   Service Name: " + name + "\n      Username: " + username + "\n      Password : " + password
          + "\n      Security questions: ", end = '')
    if security1_active:
        print("\n         Question 1: " + security1, end = '')
        if security2_active:
            print("\n         Question 2: " + security2, end = '')
            if security3_active:
                print("\n         Question 3: " + security3, end = '')
    else:
        print("\n         None.", end = '')
    print("\n      Additional information: " + add_info, end = '')
    print("\n      Pinned: " + str(pinned))
    # format the gathered information into a single CSV line
    data_line_output = ""
    # start by adding the current user's hash
    # placeholder code for now
    data_line_output += "\n" + current_user + ","
    # service name, username, password
    data_line_output += name + "," + username + "," + password + ","
    # security questions
    data_line_output += str(security1_active) + "," + security1 + ","
    data_line_output += str(security2_active) + "," + security2 + ","
    data_line_output += str(security3_active) + "," + security3 + ","
    # additional info, pinned status
    data_line_output += add_info + "," + str(pinned) + "$"
    # encrypt the line
    # 04/02 - To Do
    # open the credentials data file
    credentials = open("credentials.txt", "a")
    # append the data to the file
    credentials.write(data_line_output)
    # close the credentials data file
    credentials.close()
    # inform the user that the named credential set has been successfully created and added to their sets list.
    print("Your new service " + name + " has been added to your sets. You can now access this set at any time!")

#def main():
#    addCredentialSet()
#
#main()
