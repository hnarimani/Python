'''
Week 5 workshop
By: Hamid NK
Version 0.0.1
'''
import random


def guess_random_number(tries, start, stop):
    '''Generate a random number, then have a User to guess it. '''
    same_guess = []
    targetNum = random.randint(start, stop)
    while tries > 0:
        print(f"Number of tries letf: {tries}")
        while True:
            try:  # Only integer allowed Bonus Task 1
                userGuess = int(input(f"Guess Number between {start} and {stop}: "))
                if userGuess is not int:
                    break
            except ValueError:
                print("That's not an Interger value!!!")
        if userGuess in same_guess:  # Not permitted to enter the same guess more than once. Bonus Task 3
            print(f"You can not enter same number again, Please try another number between {start} to {stop}!!!!!")
            continue
        if targetNum == userGuess:
            print("WOW You win")
            return True
        elif targetNum < userGuess:
            print(f"Guess lower than {userGuess}!!!")
        else:
            print(f"Guess higher than {userGuess}!!!")
        tries -= 1
        same_guess.append(userGuess)  # Save all the user guess in list

    else:
        print(f"You lost, the Traget was {targetNum}")
        return False


def guess_random_num_linear(tries, start, stop):
    """ Generate a random number, then have a User to guess it using linear serach """
    targetNum = random.randint(start, stop)
    print(f"The Number For Program To Guess: {targetNum}")
    # List = list(range(start, stop))
    for i in range(start, stop+1):
        if tries < 1:
            break
        print(f"Number of tries left: {tries}")
        print(f"program_Gussing {i}")
        if i == targetNum:
            print("you win")
            return True
        tries -= 1
    print("Not Found")
    return False


def guess_random_num_binary(tries, start, stop):
    """ Generate a random number, then have a User to guess it using Binary serach """
    targetNum = random.randint(start, stop)
    # List = list(range(start, stop))
    print(f"Random Number to find is {targetNum}")
    lower_list = start
    upper_list = stop
    while tries:
        pivot = (lower_list+upper_list)//2
        if pivot == targetNum:
            print("Found it")
            return True
        elif pivot > targetNum:
            print(f"{pivot} Gussing Lower List!")
            upper_list = pivot - 1
        else:
            print(f"{pivot} Gussing Higer List")
            lower_list = pivot + 1
        tries -= 1
    print("Program Failed to find the number")
    return False

#
# Bonus Task 4


def gambling_game():
    '''Gambling Game bet and win or lose'''
    money = int(10)

    while money and money <= 50:
        print("You have $" + str(money) + " left.")
        while True:
            bet = int(input("How much do you wish to bet that the computer will guess correctly?: "))

            if bet < 1 or bet > money:

                print("You can't bet that amount!")

            else:
                break

        if guess_random_num_linear(10, 1, 10):
            print(f"Wow, You win ${bet}")
            money += bet
        else:
            print(f"Opps ,You lose ${bet}")
            money -= bet

    if money:
        fun = '\U0001f600'
        print(f"Heartfelt congratulations, you win ${money} .\nOkay game is over Go back to your room please!!!!.")
        print(fun*25)
    else:
        print(f"Please Cash in more money your have ${money}!")


# Bonus Task 2
def userInput():
    """ This function that, when called, will ask the user to input the number of tries, and the range (start and stop values).
Then have the user choose whether to guess a random number using user input, linear search, or binary search.
Then run the chosen variation with the provided arguments. """

    tries, start, stop, = [int(x) for x in input("Please enter Tries,Start and Stop Number one by one:\n").split()]
    guess_random = int(input("Please Select which Guess the number function to be use:\n1- User input \n2- Linear search\n3- Binary search\n"))
    if guess_random == 1:
        guess_random_number(tries, start, stop)
        return True
    elif guess_random == 2:
        guess_random_num_linear(tries, start, stop)
        return True
    elif guess_random == 3:
        guess_random_num_binary(tries, start, stop)
        return True
    else:
        print("Please select valid number!!!")


""" Driver Code for Task One :
guess_random_number(5, 0, 10) """

""" Driver Code for Task Two :
guess_random_num_linear(5,0,10) """

""" Driver Code for Task Three :
guess_random_num_binary(5, 0, 100) """

""" Bonus Task 2 :
userInput() """

""" Bonus Task 4 :
gambling_game() """

# userInput()
# gambling_game()
