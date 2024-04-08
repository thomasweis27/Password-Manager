
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

#_____________________________________________________________________________________________________

import os
import tkinter as tk

## helper functions of this component

#_____________________________________________________________________________________________________


#_____________________________________________________________________________________________________

## Main Component Functions
## flow of program: accessCredentialSets() -> enforceConstraints() -> termedSearch() ->
## accessCredentialSets() will interface with the main system driver and get a search term
## enforceConstraints() will make sure the search term is within the constraints of the data type
## termedSearch() will take the given search term and find any matches in the database file
## segments are declared and defined in reverse order

#_____________________________________________________________________________________________________


# termedSearch function
    # takes a search term entered by the user;
    # queries the data file for an entry with that term in any of its fields
def termedSearch(user_hash, accessCredentialScreen, siteList, searchButton, term, user_sites):
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
    # allow for change of the search term (accessCredentials <-> termedSearch segment)
    searchButton.command = lambda:enforceConstraints(user_hash, accessCredentialScreen, 
        siteList, searchButton, term, user_sites)


# enforceConstraints function
    # forces the user to input a search term that is alphanumeric and 1 - 32 chars
def enforceConstraints(user_hash, accessCredentialScreen, siteList, searchButton, term, user_sites):
    # check the length
    if not((len(term) > 0) and (len(term) <= 32)):
        # term is invalid, alert user
        tk.messagebox.showinfo("Error", "Please enter a search term that is 1-32 characters in length.")
        # call back to the main accessCredentials segment
        accessCredentialScreen.withdraw()
        accessCredentialSets(user_hash)
    # otherwise length is fine; check format
    elif not(all((char.isalnum()) or (char.isspace()) for char in term)):
        # the term is not alphanumeric
        tk.messagebox.showinfo("Error", "Please enter a search term that is alphanumeric (no special characters).")
        # call back to the main accessCredentials segment
        accessCredentialScreen.withdraw()
        accessCredentialSets(user_hash)
    # term is valid length and format, continue to search
    else:
        # otherwise the term is valid
        termedSearch(user_hash, accessCredentialScreen, siteList, searchButton, term, user_sites)


def accessCredentialSets(user_hash):
    # create new window through tk; assign attributes
    accessCredentialScreen = tk.Toplevel()
    accessCredentialScreen.title("Password Manager")
    accessCredentialScreen.geometry("800x450")
    # create label for the UI
    accessCredLabel = tk.Label(accessCredentialScreen, text = "Access Your Credentials")
    # package this into the UI
    accessCredLabel.pack()
    # tell the user how the search will function
    infoLabel = tk.Label(accessCredentialScreen, text = "All of your sites will appear below.\n"
        + "To search for a specific site, enter a search term and click 'Search'.\n"
        + "Any service that includes that term will show.")
    infoLabel.pack()
    # get the search term from the user
    searchbarLabel = tk.Label(accessCredentialScreen, text = "Enter a term: ")
    searchbarLabel.pack()
    searchterm = tk.StringVar()
    searchtermEntry = tk.Entry(accessCredentialScreen, textvariable = searchterm)
    searchtermEntry.pack()
    # search button
    searchButton = tk.Button(accessCredentialScreen, text = "Search", 
        command = lambda:enforceConstraints(user_hash, accessCredentialScreen, 
        siteList, searchButton, searchtermEntry.get(), user_sites))
    searchButton.pack()
    # create the site list element
    siteList = tk.Listbox(accessCredentialScreen)
    # add every one of the user's sites to the sitelist element
    user_sites = []
    # open the credentials file
    with open("credentials.txt") as file:
        for line in file:
            # remove any commented lines
            if not(line.startswith("$")):
                # check the hash
                split_line = line.split(",")
                if split_line[0] == user_hash:
                    # the hash matches, add to the list of user sites
                    print(line.rstrip())
                    user_sites.append(split_line)
                # otherwise the hashes don't match; continue to next site
                continue
    # close the file
    file.close()
    # add each site name to the list on screen
    for site in user_sites:        
        siteList.insert(tk.END, site[1])
    siteList.pack()
