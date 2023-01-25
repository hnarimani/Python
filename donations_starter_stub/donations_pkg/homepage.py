'''
The homepage.py include  show_homepage donate and show_donation functions

'''


def show_homepage():
    '''
    Print the welcome page with options
    '''
    print(""" 
               === DonateMe Homepage ===
     -------------------------------------------
     | 1.   Login         | 2.   Register       |
     -------------------------------------------
     | 3.   Donate        | 4.   Show Donations |
     -------------------------------------------
     |              5.      Exit                |
     -------------------------------------------""")


def donate(username, total_donation):
    '''
    Get the donation_amt and append it to donation List[],
    Also append the donation_amt into total_donation List[]
    '''
    donation_amt = float(input("Enter amount to donate: "))
    donation = f"{username} donated ${donation_amt}"
    total_donation.append(donation_amt)
    print(f"Thank you so much for your generous gift {username}!!")
    return donation


def show_donation(donations, total_donation):
    '''
    This function will be show the amount of donatios by each member and the total as well
    '''
    j = 1
    print("\n--- All Donations ---")
    if not donations:
        print("Currently, there are no donations.")
    else:
        for d in donations:
            print(f"{j}. {d}")
            j += 1
        print(f"Total Donations is : ${sum(total_donation)}")
