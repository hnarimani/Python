from banking_pkg import account


def registration():
    global name
    global pin
    global balance
    print("          === Automated Teller Machine ===          ")
    while True:
        name = input("Enter name to register: ").lower()
        if len(name) == 1 or len(name) > 10:
            print('the maximum name  length 10 char')
            continue
        elif name == "":
            print('Please Enter your name')
            continue
        else:
            break
    while True:
        try:
            # only accept integers
            pin = int(input("Enter PIN: "))
            if len(str(pin)) < 4 or len(str(pin)) > 4:
                print("PIN must contain 4 number!")
                continue
            break
        except ValueError:
            print('Please enter a number.')

    balance = 0
    print(f"{name} has been registered with a staring balance of 0 {balance}")


def login():
    global balance
    while True:
        print("          === Automated Teller Machine ===          ")
        name_to_validate = str(input("Enter Name:"))
        pin_to_validate = int(input("Enter PIN:"))
        if name == name_to_validate and pin == pin_to_validate:
            print("Login successful! ")
            break
        else:
            print("Invalid credentials!")
            continue
    while True:
        atm_menu(name)
        option = int(input("\nChoose an option:"))
        if option == 1:
            account.show_balance(balance)
        elif option == 2:
            balance = account.deposit(balance)
            account.show_balance(balance)
        elif option == 3:
            if balance == 0:
                print(f"\nWithdraw Not allowed!")
            else:
                balance = account.withdraw(balance)
            account.show_balance(balance)
        elif option == 4:
            account.logout(name)
            break
        else:
            continue


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


registration()
login()
