'''
Hamid
'''


from donations_pkg.homepage import show_homepage, donate, show_donation
from donations_pkg.user import login, register

database = {  # This dictionary hold Username and passowrd key/value pair
    "admin": "123",
    "hamid": "123"
}

donations = []  # Empty list initiated
authorized_user = ""
running = True
total_donation = []

while running:
    show_homepage()
    if authorized_user == "":
        print("You must be logged in.")
    else:
        print(f"Logged in as: {authorized_user}")
    choice = input("Choose your option: ")
    if choice == "1":
        username = input("Username: ")
        password = input("Password: ")
        authorized_user = login(database, username, password)
    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")
        authorized_user = register(database, username, password)
        if authorized_user:
            database[authorized_user] = password
    elif choice == "3":
        if not authorized_user:
            print("You are not logged in!")
        else:
            donation = donate(authorized_user, total_donation)
            donations.append(donation)
    elif choice == "4":
        show_donation(donations, total_donation)

    elif choice == "5":
        print(f"Thank you {username}, Goodbye!")
        running = False
    else:
        print("Please choose valid option from Home Page ")
