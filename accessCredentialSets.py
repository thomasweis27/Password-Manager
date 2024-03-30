

# accessCredentialSets component
    # allows user to view all credential sets;
    # allows user to search for a 
    # specific credential by service name

import os

# functions of this component

# termedSearch function
    # allows user to enter a search term;
    # queries the data file for an entry with that term in its site_name field
def termedSearch():

    # prompt user for a search term (input loop)
    while(True):
        print("Please enter a service name to search for: ", end = '')
        inp = input()
        inp = inp.upper()
        # enforce format constraints
        # is string alphanumeric?
        if not(inp.isalnum()):
            # string is not alphanumeric
            # prompt user once more
            print("Invalid input, please enter something different")
            continue
        # save and feedback the search term, lowered for consistency with the data files
        searchTerm = inp.lower()
        print("You are searching for '" + searchTerm + ".' Continue to search?")
        # prompt for Y/N (input loop 2)
        while(True):
            print("  Y/N? - ", end = '')
            inp = input()
            inp = inp.upper()
            # enforce format constraints
            # is string alphabetical?
            if inp.isalpha():
                # is string length 1?
                if len(inp) == 1:
                    # confirm/cancel search
                    if inp == "Y":
                        print("Searching for '" + searchTerm + "'...")
                        # open the credentials.txt file
                        file = open("credentials.txt")
                        # read lines from the file
                        Lines = file.readlines()
                        # read lines and save lines where the search term is found
                        MatchingServices = []
                        for currLine in Lines:
                            print(currLine)
                            # is the line commented?
                            if currLine[0] == '$':
                                print("  Comment line")
                                # move to next line
                                continue
                            # otherwise, check the first field (the service name)
                            else:
                                # does the line's name match?
                                # if there is a match for the search term
                                if (currLine.find(searchTerm)) != -1:
                                    # the line contains the term, add it to the return list
                                    MatchingServices.append(currLine)
                                else:
                                    continue
                        # is there anything in the Matching set?
                        if not(MatchingServices):
                            # alert the user that there was no matching services
                            print("There were no matches found for " + searchTerm)
                        else:
                            # print the list of matching services
                            print("Credential sets with " + searchTerm + " in their name:")
                            for i in MatchingServices:
                                print("   " + i)
                        # close the file
                        file.close()
                        break
                    # input must be N
                    elif inp == "N":
                        print("Search cancelled.")
                        break
                    # string is not Y/N
                    else:
                        # prompt user once more
                        print("Invalid input, please enter Y (yes) or N (no).")
                        continue
                # string is too long
                else:
                    # prompt user once more
                    print("Invalid input, please enter Y (yes) or N (no). Singular character only")
                    continue
            # string is not alphabetical
            else:
                # prompt user once more
                print("Invalid input, please enter Y (yes) or N (no).")
                continue
        # end of first input loop
        # only reachable after confirmation/cancel of search
        break


# dataRestorePoint
    # DEBUG FUNCTION
    # allows the creation of a restore point on the credentials file
def dataRestorePoint():

    # notify of function    
    print("Loading Data Reset Point...")

    # set current data file contents
    Lines = ["$site_title,username,password,security1_type,security1,security2_type,security2,security3_type,security3,pinned$\n",
            "$security_status fields can be nulled to indicate no additional security on site$\n",
            "$nulled security_status fields will not require security_info and will null the following security fields$\n\n" 
            "site1,testuser,testpass,null,null,null,null,null,null,true$\n"
            "site2,testuser,testpass,question,What is the first letter of the alphabet = A,null,null,null,null,false$\n"]

    # remove old and create new credential file
    if os.path.exists("credentials.txt"):
        os.remove("credentials.txt")
        c_file = open("credentials.txt", "x")
        c_file.close()

    # open and write L lines into the credentials file
    c_file = open("credentials.txt", "w")
    c_file.writelines(Lines)
    c_file.close()

    # notify of completed function
    print("Data Reset Point Loaded.")



def main():

    # restore data
    dataRestorePoint()

    # open credentials file
    with open("credentials.txt") as file:
        for line in file:
            if not(line.startswith("$")):
                print(line.rstrip())

    # prompt for search
    while(True):
        print("\nWould you like to search for a service?")
        print("  Y/N? - ", end = '')
        inp = input()
        inp = inp.upper()
        # enforce format constraints
        # is string alphabetical?
        if inp.isalpha():
            # is string length 1?
            if len(inp) == 1:
                # is string Y/N?
                if inp == "Y" or inp == "N":
                    # confirm/cancel search
                    if inp == "Y":
                        termedSearch()
                    # input must be N
                    else:
                        print("\nNot searching. Closing system.")
                        break
                # string is not Y/N
                else:
                    # prompt user once more
                    print("Invalid input, please enter Y (yes) or N (no).")
                    continue
            # string is too long
            else:
                # prompt user once more
                print("Invalid input, please enter Y (yes) or N (no). Singular character only")
                continue
        # string is not alphabetical
        else:
            # prompt user once more
            print("Invalid input, please enter Y (yes) or N (no).")
            continue
        # reached only if proper input has been enforced and carried out
        break
    
                    
        

main()