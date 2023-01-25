'''
Week 4 workshop
By: Hamid NK
Version 0.0.1
'''


class User:
    '''
    User Class
    '''

    def __init__(self, name: str, pin: int, password: str):
        '''
        Initialize User Class
        '''
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name: str):
        '''
        change_name
        '''
        self.name = name

    def change_pin(self, pin: int):
        '''
        change_pin
        '''
        self.pin = pin

    def change_password(self, password: str):
        '''
        change_password
        '''
        self.password = password


# Create BankUser
class BankUser(User):
    def __init__(self, name: str, pin: int, password: int):
        super().__init__(name, pin, password)
        self.balance = 0
        self.on_hold = False

    def toggle_on_hold(self):
        if self.on_hold:
            self.on_hold = False
        else:
            self.on_hold = True

    def show_balance(self):
        '''
        show_balance
        '''
        print(f"{self.name} has balnce of ${self.balance:.2f}")

    def withdraw(self, amount: int):
        '''
        withdraw
        '''
        if self.on_hold is True:
            print("Account is On Hold,Avoid transfering ")
            return False
        self.balance -= amount
        return (amount)

    def deposit(self, amount: int):
        '''
        deposit
        '''
        if self.on_hold is True:
            print("Account is On Hold,Avoid transfering ")
            return False
        self.balance += amount
        return (amount)

    def transfer_money(self, user: User, amount: int) -> bool:
        '''
        transfer_money to another banck user
        '''
        print(f"You are Transfreing {amount} To {user.name}")
        if self.on_hold is True:
            print("!!!!!!!!!!!Account is On Hold,Avoid transfering !!!!!!!!!!!!")
            return False
        if self.pin == int(input("Enter  {} Pin: ".format(self.name))):
            try:
                val = int(amount)
                if val < 0:  # if not a positive int
                    print("Sorry, input must be a positive integer")
                elif self.balance < val:
                    print(f"Avoid!!! Insufficient Funds in Account {self.name}")
                    return False
                else:
                    self.withdraw(amount)
                    user.deposit(amount)
                    return True
            except ValueError:
                print("That's not an Interger value !")
        else:
            print("Incotrrect PIN")
            return False

    def request_money(self, user: User, amount: int) -> bool:
        '''
        request_money
        '''
        print(f"You are requesting {amount:.2f} from {user.name}")
        if self.on_hold is True:
            print("!!!!!!!!!Account is On Hold,Avoid requesting!!!!!!!!!!! ")
            return False
        if user.pin == int(input("Enter  {} Pin: ".format(user.name))):
            try:
                val = int(amount)
                if val < 0:  # if not a positive int
                    print("Sorry, input must be a positive integer")
                elif user.balance < val:
                    print(f"Avoid!!! Insufficient Funds in Account {user.name}")
                    return False
                else:
                    print(f"{user.name} balance most be {user.balance} and ${amount:.2f}")
                    user.withdraw(amount)
                    self.deposit(amount)
                    return True
            except ValueError:
                print("That's not an Interger value !")
        else:
            print("Incotrrect PIN")
            return False


# Driver Code
bankuser1 = BankUser("Bob", 1234, "“password")
bankuser2 = BankUser("Alice", 4321, "newpassword")
bankuser2.deposit(5000)
bankuser2.show_balance()
bankuser1.show_balance()
bankuser2.transfer_money(bankuser1, 2000)
bankuser2.show_balance()
bankuser1.show_balance()
bankuser1.request_money(bankuser2, 700)
bankuser1.show_balance()
bankuser2.show_balance()
print("#################################################")
bankuser1.toggle_on_hold()
bankuser2.toggle_on_hold()
transferred = bankuser2.transfer_money(bankuser1, 500)
bankuser2.show_balance()
bankuser1.show_balance()
if transferred:
    bankuser2.request_money(bankuser1, 250)
    bankuser2.show_balance()
    bankuser1.show_balance()
