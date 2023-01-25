'''
User functions
'''
import re


def validate_username(username: str) -> bool:
    '''
        Validate Username
        Return Bool
        Credit to Jack
    '''
    regex = "^[a-zA-Z][?=.*a-zA-Z0-9]*$"
    pattern = re.compile(regex)
    if re.search(pattern, username):
        return True
    return False


def validate_passwd(password) -> str:
    '''
    Validate and Return Bool
    Credit to Jack
    '''
    _p = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,21}$"
    pattern = re.compile(_p)
    if re.search(pattern, password):
        return True
    return False


def login(database, username, password):
    '''
    User log in functionality
    '''
    if username.lower() in database.keys():
        if password in database.values():
            print(f"Welcome back {username}!")
            return username
        else:
            print(f"\nIncorrect Password for username:{username} ")
            return ""
    else:
        print("User not found.\nPlease try option 2 Register.")
        return ""


def register(database, username, password):
    '''
    User log in functionality
    '''
    if username.lower() in database.keys():
        print("Username already registered.")
        return ""
    if validate_username(username):
        print(f"{username} Accepted!")
    else:
        return print(f"Username {username} Not Valid")
    if validate_passwd(password):
        print("Strong password")
    else:
        return print("Passwords must be 8-20 characters and contain: uppercase, lowercase, number, special character.")
    print(f"Username {username} registered!!!")
    database[username.lower()] = password
    return username
