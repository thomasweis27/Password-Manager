
#_____________________________________________________________________________________________________
## COMPONENT DESCRIPTION AND HISTORY

# accessCredentialSets component
    # allows user to view all credential sets;
    # allows user to search for a 
    # specific credential by service name
# 04/01 - this will be modified to plug into the system more modularly once we know
        # how we want to set everything up (possibly after a driver, etc.)
# 04/07 - UI setup and rework. 
        # replacing proof-of-concept console ui with Tkinter
        # fixing component flow to work with main system

#_____________________________________________________________________________________________________

import os
import tkinter as tk

## helper functions of this component

#_____________________________________________________________________________________________________


#_____________________________________________________________________________________________________

## Main Component Functions
## flow of program: 
## 
## termedSearch() will take the given search term and find any matches in the database file
##
## segments are declared and defined in reverse order

#_____________________________________________________________________________________________________



# termedSearch function
    # takes a search term entered by the user;
    # queries the data file for an entry with that term in any of its fields
def termedSearch(user_hash, accessCredentialsScreen):
    # open the credentials file and save every line that is not commented
    with open("credentials.txt") as file:
        for line in file:
            if not(line.startswith("$")):
                print(line.rstrip())





    # # prompt user for a search term (input loop)
    # while(True):
    #     print("Please enter a service name to search for: ", end = '')
    #     inp = input()
    #     inp = inp.upper()
    #     # enforce format constraints
    #     # is string alphanumeric?
    #     if not(inp.isalnum()):
    #         # string is not alphanumeric
    #         # prompt user once more
    #         print("Invalid input, please enter something different")
    #         continue
    #     # save and feedback the search term, lowered for consistency with the data files
    #     searchTerm = inp.lower()
    #     print("You are searching for '" + searchTerm + ".' Continue to search?")
    #     # prompt for Y/N (input loop 2)
    #     while(True):
    #         print("  Y/N? - ", end = '')
    #         inp = input()
    #         inp = inp.upper()
    #         # enforce format constraints
    #         # is string alphabetical?
    #         if inp.isalpha():
    #             # is string length 1?
    #             if len(inp) == 1:
    #                 # confirm/cancel search
    #                 if inp == "Y":
    #                     print("Searching for '" + searchTerm + "'...")
    #                     # open the credentials.txt file
    #                     file = open("credentials.txt")
    #                     # read lines from the file
    #                     Lines = file.readlines()
    #                     # read lines and save lines where the search term is found
    #                     MatchingServices = []
    #                     for currLine in Lines:
    #                         print(currLine)
    #                         # is the line commented?
    #                         if currLine[0] == '$':
    #                             print("  Comment line")
    #                             # move to next line
    #                             continue
    #                         # not a comment; check that the hash in the line matches current user's
    #                         # elif hash != currentUserHash:
    #                             # continue
    #                         # line isn't commented out and the hashes match
    #                         else:
    #                             # does the line's name match?
    #                             # if there is a match for the search term
    #                             if (currLine.find(searchTerm)) != -1:
    #                                 # the line contains the term, add it to the return list
    #                                 MatchingServices.append(currLine)
    #                             else:
    #                                 continue
    #                     # is there anything in the Matching set?
    #                     if not(MatchingServices):
    #                         # alert the user that there was no matching services
    #                         print("There were no matches found for " + searchTerm)
    #                     else:
    #                         # print the list of matching services
    #                         print("Credential sets with " + searchTerm + " in their name:")
    #                         for i in MatchingServices:
    #                             print("   " + i)
    #                     # close the file
    #                     file.close()
    #                     break
    #                 # input must be N
    #                 elif inp == "N":
    #                     print("Search cancelled.")
    #                     break
    #                 # string is not Y/N
    #                 else:
    #                     # prompt user once more
    #                     print("Invalid input, please enter Y (yes) or N (no).")
    #                     continue
    #             # string is too long
    #             else:
    #                 # prompt user once more
    #                 print("Invalid input, please enter Y (yes) or N (no). Singular character only")
    #                 continue
    #         # string is not alphabetical
    #         else:
    #             # prompt user once more
    #             print("Invalid input, please enter Y (yes) or N (no).")
    #             continue
    #     # end of first input loop
    #     # only reachable after confirmation/cancel of search
    #     break


def accessCredentialSets(user_hash, loginScreen):
    # minimize previous screen
    loginScreen.withdraw()
    # create new window through tk; assign attributes
    # this window is a child of (mastered by) the main login screen
    accessCredentialScreen = tk.Toplevel(loginScreen)
    accessCredentialScreen.title("Password Manager")
    accessCredentialScreen.geometry("800x450")
    # create label for the UI
    accessCredLabel = tk.Label(accessCredentialScreen, text = "Access Your Credentials")
    # package this into the UI
    accessCredLabel.pack()
    # tell the user that they will need x data (listed above) to create the new set
    infoLabel = tk.Label(accessCredentialScreen, text = "Please enter a search term below.\n"
        + "Any service that includes that term will show up.")
    infoLabel.pack()

    # # prompt for search
    # while(True):
    #     print("\nWould you like to search for a service?")
    #     print("  Y/N? - ", end = '')
    #     inp = input()
    #     inp = inp.upper()
    #     # enforce format constraints
    #     # is string alphabetical?
    #     if inp.isalpha():
    #         # is string length 1?
    #         if len(inp) == 1:
    #             # is string Y/N?
    #             if inp == "Y" or inp == "N":
    #                 # confirm/cancel search
    #                 if inp == "Y":
    #                     termedSearch()
    #                 # input must be N
    #                 else:
    #                     print("\nNot searching. Closing system.")
    #                     break
    #             # string is not Y/N
    #             else:
    #                 # prompt user once more
    #                 print("Invalid input, please enter Y (yes) or N (no).")
    #                 continue
    #         # string is too long
    #         else:
    #             # prompt user once more
    #             print("Invalid input, please enter Y (yes) or N (no). Singular character only")
    #             continue
    #     # string is not alphabetical
    #     else:
    #         # prompt user once more
    #         print("Invalid input, please enter Y (yes) or N (no).")
    #         continue
    #     # reached only if proper input has been enforced and carried out
    #     break
    
                    
        

#main()
