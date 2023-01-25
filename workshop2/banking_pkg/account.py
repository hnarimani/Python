
def show_balance(balance):
    print(f"\nCurrent balance:${balance}")


def deposit(balance):
    amount = float(input("Enter amount to deposit:"))
    return amount + balance


def withdraw(balance):
    withdraw = float(input("\nEnter amount to withdraw:"))
    check_balance = balance - withdraw
    if check_balance < 0:
        print("\nInsufficient Funds!!!")
        return balance
    else:
        return balance - withdraw


def logout(name):
    print(f"\nGoodbye {name}")
