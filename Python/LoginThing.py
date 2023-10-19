from time import sleep

list_of_accounts_details = []   # list of accounts
running = True  # program will keep running until this is false

# examples of accounts
example_account1 = ["Meliodas", "Yaiba", 72, "meliodas72", "password1", "meliodas72@gmail.com"]
example_account2 = ["Coppenheigan", "Dmitri", 1, "cop1", "password2", "coppenheigan@yahoo.com"]
example_account3 = ["Blah", "Bleh", 10, "blah", "password3", "blahbleh10@yandex.com"]

list_of_accounts_details.extend([example_account1, example_account2, example_account3]) # add the accounts to the database


# function for login
def funcLogin():
    print("================================")
    print("=============LOGIN==============")
    print("================================")

    while True: # Keep asking for username and password until one is successful
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if checkLogin(username, password):  # go to checkLogin() function to see if username and password are valid
            funcSuccessfulLogin()
            break
        else:
            print("ERROR: INVALID USERNAME OR PASSWORD")


# Go through each profile list in list_of_accounts_details to see if "username" and "password" are valid
def checkLogin(username, password):
    for list_of_accounts in list_of_accounts_details:
        if username == list_of_accounts[3] and password == list_of_accounts[4]:
            return True
        else:
            continue

    return False


# This is run when username and password are valid
def funcSuccessfulLogin():
    global running 

    list_of_accounts_details_sorted = sort_list()   # sort the list_of_accounts_details in alphabetic order

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~LOGIN SUCCESSFUL!!~~~~~~~~~~~~~~~~~~", sep='')
    print('-----------------------------------------------------------------------')
    print("FIRSTNAME | ", "LASTNAME | ", "AGE | ", "USERNAME | ", "PASSWORD | ", "EMAIL | ", end='')

    for userprofile in list_of_accounts_details_sorted: # loop through all profiles in the list_of_accounts_details_sorted (to be printed)
        print('\n-----------------------------------------------------------------------')
        for element in userprofile: # loop through all information in the profile
            print(element, end=' | ')
    print('\n-----------------------------------------------------------------------')

    print("~~PROGRAM QUITTING...~~")
    running = False # Stops the program
   
# Function to sort the list of profiles in alphabetical order based on the first name
def sort_list():
    sorted_list = []

    firstnames = [profile_details[0] for profile_details in list_of_accounts_details] # creates a list of first names (which will be sorted)
    firstnames = sorted(firstnames) # sorts the list of firstnames by alphabetical order

    # this will sort list_of_accounts_details based on the sorted firstnames
    for firstname in firstnames:
        for profile_details in list_of_accounts_details:
            if firstname in profile_details:
                if profile_details in sorted_list:  # IF THE FIRST NAME IS A DUPLICATE, IT WILL SKIP IT UNTIL IT FINDS A UNIQUE ONE
                    continue
                else:
                    sorted_list.append(profile_details)
            else:
                continue
    return sorted_list


# function to input information
def getInfoRegistration():
    array_for_some_reason = []

    while True:
        firstname = input("Input FIRSTNAME: ")
        try:# TRY AND CAPITALIZE THE FIRST LETTER OF THE NAME
            firstname = firstname[0].capitalize() + firstname[1:]
        except:
            pass

        if firstname.isalpha():
            break
        else:
            if " " in firstname: # This checks if the illegal character is just a space
                break
            userinput = input("ERROR: NAME CONTAINS NUMBERS OR LETTERS (Are you sure that's your name?) y/n: ")
            if userinput.upper() == "Y":
                break

    while True:
        lastname = input("Input LASTNAME: ")        
        try:# TRY AND CAPITALIZE THE FIRST LETTER OF THE NAME
            lastname = lastname[0].capitalize() + lastname[1:]
        except:
            pass

        if lastname.isalpha():
            break
        else:
            if " " in lastname: # This checks if the illegal character is just a space
                break
            userinput = input("ERROR: NAME CONTAINS NUMBERS OR LETTERS (Are you sure that's your name?) y/n: ")
            if userinput.upper() == "Y":

                break

    while True:
        age = input("Input AGE: ")
        if age.isnumeric():
            break
        else:
            print("ERROR: PLEASE ENTER A VALID AGE")
            sleep(0.5)

    while True:
        username = input("Input USERNAME: ")  

        for account in list_of_accounts_details:
            if username == account[3]:
                print("ERROR: USERNAME IS TAKEN")
                sleep(0.5)
                continue
        break

    while True:
        password = input("Input PASSWORD: ")
        if any(char.isdigit() for char in password): # Checks to see if password contains a digit
            break
        else:
            print("ERROR: PASSWORD DOES NOT CONTAIN A NUMBER")
            sleep(0.5)

    while True:
        email = input("Input EMAIL: ")
        if any(char == "@" for char in email): # Checks to see if email contains an @
            break
        else:
            print("ERROR: PLEASE ENTER A VALID EMAIL")
            sleep(0.5)
        
    userinput = input(f'''
❚❚====================================================
❚❚ FIRSTNAME: {firstname}
❚❚ LASTNAME: {lastname}
❚❚ AGE: {age}
❚❚ USERNAME: {username}
❚❚ PASSWORD: {password}
❚❚ EMAIL: {email}
❚❚====================================================
are you sure the information above is correct? y/n) ''')
    if userinput.upper() == "Y":
        pass
    else:
        getInfoRegistration()
        return

    array_for_some_reason.extend([firstname, lastname, age, username, password, email])
    list_of_accounts_details.append(array_for_some_reason)


def main_function():
    print("WELCOME TO HACKATON LOGIN")
    while running:
        UserInput = input("LogIn or Register: ")

        if UserInput.upper() == "LOGIN":
            funcLogin()
            break

        elif UserInput.upper() == "REGISTER":
            print("================================")
            print("==========REGISTRATION==========")
            print("================================")

            getInfoRegistration()

            print("====REGISTRATION SUCCESSFUL!====")
            sleep(0.6)

            print("...automatically going to LOGIN page")
            sleep(0.8)

            funcLogin()

        else:
            print("ERROR: That was not an option (please inpit 'register' or 'login')")
            sleep(0.5)

main_function()