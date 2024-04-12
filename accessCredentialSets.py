
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
        # TO DO: finish up the UI implementation. Works for now but no functionality
# 04/08 - More UI functionality
        # TO DO: allow user to select sites and pop-up the credential info.
            # possibly needs a new module
        # Fix issue with search term case sensitivity and consecutivity.
# 04/09 - Even More UI
        # Broke down the screens to allow for better & faster UI
        # Fixes for case sensitivity and consecutivity on searches
        # TO DO: Still need to set up selection and set information screen
# 04/10-11 - Final steps on access. 
        # Added "Select" button that interfaces with the view screen
        # allows user to select a site, open the info, and edit or delete
        # Component is complete at this point.
        # FINAL: go to view screen in the selectCredential helper function
# 04/12 - Interface with viewCredentialScreen implemented
        # small documentation and program layout tweaks.
        # NO TO DO

#_____________________________________________________________________________________________________

import tkinter as tk
import Decrypt as dec
from viewCredentialSet import viewCredentialSet

## helper functions of this component

#_____________________________________________________________________________________________________


# returnToPrevious function
    # allows user to return to the previous screen
def returnToPrevious(currentWindow, previousWindow):
    # minimize the current window
    currentWindow.withdraw()
    # show the previous window
    previousWindow.deiconify()


# clearSearch function
    # fixes issue with duplication of accessCredential window upon clearing search
def clearSearch(user_hash, previousWindow, accessCredentialScreen):
    # withdraw the existing accessCredential window
    accessCredentialScreen.withdraw()
    # call back to the beginning of the accessCredential component
    accessCredentialSets(user_hash, previousWindow)


#_____________________________________________________________________________________________________

## Main Component Functions
## flow of program: accessCredentialSets() -> searchCredentials() -> 
##      enforceConstraints() -> termedSearch() <-> searchCredentials() -> selectCredentialSet()
## accessCredentialSets() will interface with the main system driver
## searchCredentials() will get a search term from the user and separate searching from initializing
## enforceConstraints() will make sure the search term is within the constraints of the data type
## termedSearch() will take the given search term and find any matches in the database file
## selectCredentialSet() is the final step in the component; gets the selected set and passes it on
## segments are declared and defined in reverse order

#_____________________________________________________________________________________________________


# selectCredentialSet function
    # validates that there is a site selected before moving to viewCredentialSet module
def selectCredentialSet(user_hash, previousWindow, accessCredentialScreen, credential_set_name, user_sites):
    # get the entire credential from the list of user's sites
    for site in user_sites:
        if site[1] == credential_set_name:
            full_credential_set = site
    # move to the next component
    viewCredentialSet(user_hash, previousWindow, accessCredentialScreen, full_credential_set)


# termedSearch function
    # takes a search term entered by the user;
    # queries the data file for an entry with that term in any of its fields
def termedSearch(user_hash, previousWindow, accessCredentialScreen, siteList, searchButton, term, user_sites):
    # verify the search term to the user
    tk.messagebox.showinfo("Error", "Searching for sites with " + term)
    # clear the site list box
    siteList.delete(0, siteList.size())
    # lowercase the term
    term = term.lower()
    # set up lists that will be used to hold sites
    matches = []
    # check each user site
    for site in user_sites:
        # does the name contain the term at all
        if (site[1].find(term)) != -1:
            # the term is somewhere in the name; add to matches
            matches.append(site)
        # otherwise it doesn't match; continue to next site
        continue
    # add each site name to the list on screen
    for site in matches:        
        siteList.insert(tk.END, site[1])
    siteList.pack()
    # allow for change of the search term (searchCredentials <-> termedSearch segment)
    searchButton.command = lambda:enforceConstraints(user_hash, previousWindow, 
        accessCredentialScreen, siteList, searchButton, term, user_sites)
    searchButton.pack()    


# enforceConstraints function
    # forces the user to input a search term that is alphanumeric and 1 - 32 chars
def enforceConstraints(user_hash, previousWindow, accessCredentialScreen, siteList, searchButton, term, user_sites):
    # check the length
    if not((len(term) > 0) and (len(term) <= 32)):
        # term is invalid, alert user
        tk.messagebox.showinfo("Error", "Please enter a search term that is 1-32 characters in length.")
        # call back to the searchCredentials segment
        accessCredentialSets(user_hash, previousWindow, accessCredentialScreen)
    # otherwise length is fine; check format
    elif not(all((char.isalnum()) or (char.isspace()) for char in term)):
        # the term is not alphanumeric
        tk.messagebox.showinfo("Error", "Please enter a search term that is alphanumeric (no special characters).")
        # call back to the searchCredentials segment
        accessCredentialSets(user_hash, previousWindow, accessCredentialScreen)
    # term is valid length and format, continue to search
    else:
        # otherwise the term is valid
        termedSearch(user_hash, previousWindow, accessCredentialScreen, siteList, searchButton, term, user_sites)


# searchCredentials function
    # establishes the ability to search with the button;
    # separates the initialization of the window from the
    # repeatable search function.
def searchCredentials(user_hash, previousWindow, accessCredentialScreen, siteList, user_sites):
    # get the search term from the user
    searchbarLabel = tk.Label(accessCredentialScreen, text = "Enter a term: ")
    searchbarLabel.pack()
    searchterm = tk.StringVar()
    searchtermEntry = tk.Entry(accessCredentialScreen, textvariable = searchterm)
    searchtermEntry.pack()
    # search button
    searchButton = tk.Button(accessCredentialScreen, text = "Search", 
        command = lambda:enforceConstraints(user_hash, previousWindow, 
        accessCredentialScreen, siteList, searchButton, searchtermEntry.get(), user_sites))
    searchButton.pack()
    # clear search button
    clearButton = tk.Button(accessCredentialScreen, text = "Clear", 
        command = lambda:clearSearch(user_hash, previousWindow, accessCredentialScreen))
    clearButton.pack()
    # select site button
    selectButton = tk.Button(accessCredentialScreen, text = "Select", 
        command = lambda:selectCredentialSet(user_hash, previousWindow, 
            accessCredentialScreen, siteList.get(tk.ACTIVE), user_sites))
    selectButton.pack()


# accessCredentialSets function
    # initial functionality of this component
    # establishes windows, base ui, etc.
def accessCredentialSets(user_hash, previousWindow):
    # close previous window
    previousWindow.withdraw()
    # create new window through tk; assign attributes
    accessCredentialScreen = tk.Tk()
    accessCredentialScreen.title("Password Manager")
    accessCredentialScreen.geometry("800x675")
    # create label for the UI
    accessCredLabel = tk.Label(accessCredentialScreen, text = "Access Your Credentials")
    # package this into the UI
    accessCredLabel.pack()
    # tell the user how the search will function
    infoLabel = tk.Label(accessCredentialScreen, text = "All of your sites will appear below.\n"
        + "To search for a specific site, enter a search term and click 'Search'.\n"
        + "Any service that includes that term will show.")
    infoLabel.pack()
    # create the site list element
    siteList = tk.Listbox(accessCredentialScreen)
    siteList.delete(0, siteList.size())
    # add every one of the user's sites to the sitelist element
    user_sites = []
    # open the credentials file
    with open("credentials.txt") as file:
        for line in file:
            # decrypt the line
            #
            # remove any commented lines
            if not(line.startswith("$")):
                # check the hash
                split_line = line.split(",")
                if split_line[0] == user_hash:
                    # the hash matches, add to the list of user sites
                    user_sites.append(split_line)
                # otherwise the hashes don't match; continue to next site
                continue
    # close the file
    file.close()
    # add each site name to the list on screen
    for site in user_sites:        
        siteList.insert(tk.END, site[1])
    siteList.pack()
    # move to next segment, searchCredentials
    searchCredentials(user_hash, previousWindow, accessCredentialScreen, siteList, user_sites)
    # return to previous screen
    returnButton = tk.Button(accessCredentialScreen, text = "<- Back", 
        command = lambda:returnToPrevious(accessCredentialScreen, previousWindow))
    returnButton.pack(side = tk.BOTTOM)