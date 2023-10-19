# Data Storage of Accounts
accounts = [
    {
        "firstName": "Ley",
        "lastName": "Jivs",
        "age": 22,
        "username": "ley",
        "password": "ley12345",
        "email": "ley@gmail.com",
    },
    {
        "firstName": "Zero",
        "lastName": "Johnson",
        "age": 34,
        "username": "zero",
        "password": "zero12345",
        "email": "zero@gmail.com",
    },
    {
        "firstName": "Luxus",
        "lastName": "Smith",
        "age": 27,
        "username": "luxus",
        "password": "luxus12345",
        "email": "luxus@gmail.com",
    },
]

# Function to sort and display accounts
def display_sorted_accounts():
    print("----- Data Accounts Details ------")

    # Sort all accounts by "firstName" (case-insensitive)
    sorted_accounts = sorted(accounts, key=lambda acc: acc["firstName"].lower())

    # Iterate through the sorted accounts and print the details
    for i, acc in enumerate(sorted_accounts):
        print(f"{i + 1}: First name: {acc['firstName']} lastname: {acc['lastName']} age: {acc['age']} username: {acc['username']} password: {acc['password']} email: {acc['email']}")

# Function for Reusable Asking User for Registration
def ask_user_registration():
    while True:
        ask_name = input("Enter name: ")
        ask_last_name = input("Enter last name: ")
        ask_age = int(input("Enter age: "))
        ask_username = input("Enter username: ")

        while True:
            ask_password = input("Enter password: ")
            if any(char.isdigit() for char in ask_password):
                break
            else:
                print("Invalid password! Should have a number")

        while True:
            ask_email = input("Enter email: ")
            if "@" in ask_email:
                new_account = {
                    "firstName": ask_name,
                    "lastName": ask_last_name,
                    "age": ask_age,
                    "username": ask_username,
                    "password": ask_password,
                    "email": ask_email,
                }
                accounts.append(new_account)
                print("Registration successful!")

                ask_login_or_register()  # Call the login or register function again

            else:
                print("Invalid email! Should have '@'")

# Function for Reusable Asking User for Login
def ask_user_login():
    ask_username = input("Enter username: ")
    ask_password = input("Enter password: ")

    found_account = next((account for account in accounts if account["username"] == ask_username and account["password"] == ask_password), None)

    if found_account:
        print("Login successful!")
        display_sorted_accounts()  # Display sorted accounts after login
        exit()  # End the program
    else:
        print("Invalid account!")
        ask_login_or_register()  # Prompt user to log in or register again

# Function for Reusable Asking User for Login or Register
def ask_login_or_register():
    ask_user = input("Login or Register?")

    if ask_user == "login":
        ask_user_login()
    elif ask_user == "register":
        ask_user_registration()
    else:
        print("Invalid input! Should be 'Login' or 'Register'.")
        ask_login_or_register()

# First Step: Ask User to Login or Register
ask_login_or_register()