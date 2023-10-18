# Data Storage of Accounts
accounts = [
    {
        "firstName": "Ley",
        "lastName": "Jivs",
        "age": 22,
        "username": "ley",
        "password": "ley12345",
        "email": "john@gmail.com",
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

# Display Accounts Data
def display_accounts_data():
    print("----- Data Accounts Details ------")
    sorted_accounts = sorted(accounts, key=lambda acc: acc["firstName"])
    for i, acc in enumerate(sorted_accounts):
        print(f"{i + 1}: First name: {acc['firstName']} lastname: {acc['lastName']} age: {acc['age']} username: {acc['username']} password: {acc['password']} email: {acc['email']}")

# Function for Reusable Asking User for Registration
def ask_user_registration():
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
            accounts.append({
                "firstName": ask_name,
                "lastName": ask_last_name,
                "age": ask_age,
                "username": ask_username,
                "password": ask_password,
                "email": ask_email,
            })
            print("Registration successful!")
            ask_login_or_register()  # Prompt user to log in or register again
            return  # Exit the function after registration
        else:
            print("Invalid email! Should have '@'")

# Function for Reusable Asking User for Login
def ask_user_login():
    ask_username = input("Enter username: ")
    ask_password = input("Enter password: ")

    found_account = next((account for account in accounts if account["username"] == ask_username and account["password"] == ask_password), None)

    if found_account:
        display_accounts_data()
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
