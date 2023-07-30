from cardHolder import cardHolder

def print_menu():
    ### Print options to the user
    print("Please choose from one of the following options...")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

def deposit(cardHolder):
    try:
        deposit = float(input("How much $$ would you like to deposit: "))
        cardHolder.set_balance(cardHolder.get_balance() + deposit)
        print("Thank you, ", cardHolder.get_firstName(), ". Your new balance is: ", str(cardHolder.get_balance()))
    except:
        print("Invalid input")

def withdraw(carHolder):
    try:
        withdraw = float(input("How much $$ would you like to withdraw: "))
        ### Check if user has enough money
        if(cardHolder.get_balance() < withdraw):
            print("Insuffeicient balance :(")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw)
            print( "You're good to go! Thank you :)")
    except:
        print("Invalid imput")

def check_balance(cardHolder):
    print("Your current balance is: ", cardHolder.get_balance())

if __name__ == "__main__":
    current_user = cardHolder("","","","","")

    ### Create a repo of cardholders
    list_of_cardHolders = []
    list_of_cardHolders.append(cardHolder("452772818527395", 1234, "John", "Griffith", 150.31))
    list_of_cardHolders.append(cardHolder("453276184132502", 4321, "Ashley", "Jones", 321.13))
    list_of_cardHolders.append(cardHolder("5128381368581872", 9999, "Frida", "Dickerson", 105.59))
    list_of_cardHolders.append(cardHolder("6011188364697109", 2468, "Muneeb", "Harding", 851.84))
    list_of_cardHolders.append(cardHolder("3490693153147110", 4826, "Dawn", "Smith", 54.27))

    ### Prompt user for debit card number
    debitCardNum = ""
    while True:
        try:
            debitCardNum = input("Please insert your debit card: ")
            ### Check against repo
            debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum == debitCardNum]
            if(len(debitMatch) > 0):
                current_user = debitMatch[0]
                break
            else: 
                print("Card number not recognized. Please try again.")
        except:
            print("Card number not recognized. Please try again.")

    ### Prompt for PIN
    while True:
        try:
            userPin = int(input("Please enter your pin: ").strip())
            if(current_user.get_pin() == userPin):
                break
            else:
                print("Invalid PIN. Please try again.")
        except:
            print("Invalid PIN. Please try again.")
    ### Print options
    print("Welcom ", current_user.get_firstName(), ":)")
    option = 0
    while (True):
        print_menu()
        try:
            option =int(input())
        except:
            print("Invalid input. Please try again.")
        
        if(option == 1):
            deposit(current_user)
        elif(option == 2):
            withdraw(current_user)
        elif(option == 3):
            check_balance(current_user)
        elif(option == 4):
            break
        else:
            option = 0
    
    print("Thank you. Have a nice day :)") 
