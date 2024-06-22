# jetbrains sucks :)

# import important modules
import time
import random
import decimal

# set important numbers

global money
global copperPrice  # PYTHON MUST DIE
global ironPrice
global silverPrice
global goldPrice
global minedToday
global pickLevel

money = 0  # "what does the b in vitamin b stand for?" "BROKE"
copperPrice = 1
ironPrice = 2
silverPrice = 3
goldPrice = 4

minedToday = False
pickLevel = 1

# it's the intro. there has to be some story or else the game wouldn't be fun!
print("Welcome to the game!")
time.sleep(1)
print("It's 1852, and you have just moved across the country to find the treasure buried in those California hills.")
time.sleep(3)
print("You've taken up residence in a small boom-town, and you believe you'll be the first to hit it off.")
time.sleep(3)
print(
    "After taking a small loan from the bank and making purchases for the bare minimum equipment, you're ready to go.")
time.sleep(3)


# here's where the fun begins!


# putting the random in the s&p 500


def market():
    print("It's a new day...")
    time.sleep(1)
    print("You go into town and see the latest prices.")
    time.sleep(1)

    copperChange = float(decimal.Decimal(random.randrange(-20, 20)) / 100)  # thank you stack overflow
    ironChange = float(decimal.Decimal(random.randrange(-40, 40)) / 100)
    silverChange = float(decimal.Decimal(random.randrange(-60, 60)) / 100)
    goldChange = float(decimal.Decimal(random.randrange(-80, 80)) / 100)

    if copperPrice + copperChange < 1:
        copperChange = 0
        print("COPPER..." + str(copperChange) + "...NO CHANGE...")
    elif copperPrice + copperChange > 1:
        copperPrice += copperChange
        print("COPPER..." + str(copperPrice) + "..." + str(copperChange) + " CHANGE...")

    if ironPrice + ironChange < 1:
        ironChange = 0
        print("IRON..." + str(ironChange) + "...NO CHANGE...")
    elif ironPrice + ironChange > 1:
        ironPrice += ironChange
        print("IRON..." + str(ironPrice) + "CHANGE OF " + str(ironChange) + "...")

    if silverPrice + silverChange < 1:
        silverChange = 0
        print("SILVER..." + str(silverChange) + "...NO CHANGE...")
    elif silverPrice + silverChange > 1:
        silverPrice += silverChange
        print("SILVER..." + str(silverPrice) + "CHANGE OF " + str(silverChange) + "...")

    if goldPrice + goldChange < 1:
        goldChange = 0
        print("GOLD..." + str(goldChange) + "...NO CHANGE...")
    elif goldPrice + goldChange > 1:
        goldPrice += goldChange
        print("GOLD..." + str(goldPrice) + "CHANGE OF " + str(goldChange) + "...")

    return copperPrice, ironPrice, silverPrice, goldPrice


'''
this is the shopkeep loop. 
it's a little different than the other loops because it has to be a while loop.
the while loop will keep going until the player decides to leave the shop.
they can buy/sell minerals and upgrade their equipment.
'''


# here are the functions for the shop loop. nothing much.

def buy():
    print("Take your pick, miner.")
    time.sleep(1)
    print("1. Copper")
    print("2. Iron")
    print("3. Silver")
    print("4. Gold")
    print("5. Go back to the shop")
    choice = input("What would you like to buy? ")

    if choice == "1":
        print("The current price of copper is $" + str(copperPrice) + " a piece.")
        print("How much copper would you like to buy?")
        choice = input("? ")
        if int(choice) * copperPrice > money:
            print("You don't have enough money.")
            time.sleep(1)
            buy()
        else:
            money -= choice * copperPrice
            print("You have $" + str(money) + " left, and have bought " + str(choice) + " copper.")
            time.sleep(1)
            buy()

    if choice == "2":
        print("The current price of iron is $" + str(ironPrice) + " a piece.")
        print("How much iron would you like to buy?")
        choice = input("? ")
        if int(choice) * ironPrice > money:
            print("You don't have enough money.")
            time.sleep(1)
            buy()
        else:
            money -= choice * ironPrice
            print("You have $" + str(money) + " left, and have bought " + str(choice) + " iron.")
            time.sleep(1)
            buy()

    if choice == "3":
        print("The current price of silver is $" + str(silverPrice) + " a piece.")
        print("How much silver would you like to buy?")
        choice = input("? ")
        if int(choice) * silverPrice > money:
            print("You don't have enough money.")
            time.sleep(1)
            buy()
        else:
            money -= choice * silverPrice
            print("You have $" + str(money) + " left, and have bought " + str(choice) + " silver.")
            time.sleep(1)
            buy()

    if choice == "4":
        print("The current price of gold is $" + str(goldPrice) + " a piece.")
        print("How much gold would you like to buy?")
        choice = input("? ")
        if int(choice) * goldPrice > money:
            print("You don't have enough money.")
        else:
            money -= choice * goldPrice
            print("You have $" + str(money) + " left, and have bought " + str(choice) + " gold.")
            time.sleep(1)
            buy()


    elif choice == "5":
        print("You go back.")
        time.sleep(1)
    else:
        print("I don't understand.")
        time.sleep(1)
        buy()


def sell():
    print("I'll take what you have, miner.")
    time.sleep(1)
    print("1. Copper")
    print("2. Iron")
    print("3. Silver")
    print("4. Gold")
    print("5. Sell everything")
    print("6. Go back to the shop")
    choice = input("What would you like to sell? ")
    if choice == "1":
        print("How much copper would you like to sell?")
        choice = input("? ")
    elif choice == "2":
        print("How much iron would you like to sell?")
        choice = input("? ")
    elif choice == "3":
        print("How much silver would you like to sell?")
        choice = input("? ")
    elif choice == "4":
        print("How much gold would you like to sell?")
        choice = input("? ")
    elif choice == "5":
        print("You sell everything.")
        time.sleep(1)
    elif choice == "6":
        print("You go back.")
        time.sleep(1)
    else:
        print("I don't understand.")
        time.sleep(1)
        sell()


def upgrade():
    print("On the up and up, are we, miner?")
    time.sleep(1)
    print("1. Upgrade your pickaxe (50 dollars)")
    print("2. Upgrade your inventory (50 dollars)")
    print("3. Go back to the shop")
    choice = input("What would you like to upgrade? ")
    if choice == "1":
        print("You upgrade your pickaxe.")
        time.sleep(1)
    elif choice == "2":
        print("You upgrade your inventory.")
        time.sleep(1)
    elif choice == "3":
        print("You go back.")
        time.sleep(1)
    else:
        print("I don't understand.")
        time.sleep(1)
        upgrade()


def shop():
    print("Welcome to the shop, miner!")
    time.sleep(1)
    print("You can:")
    print("1. Buy minerals")
    print("2. Sell minerals")
    print("3. Upgrade equipment")
    print("4. Leave the shop")
    choice = input("What would you like to do? ")

    if choice == "1":
        buy()
    elif choice == "2":
        sell()
    elif choice == "3":
        upgrade()
    elif choice == "4":
        print("You leave the shop.")
        time.sleep(1)


'''
this is the mining loop. 
the player will get x amount of ore y every time they mine. 
it can be done once per day. the amount of ore is random.
'''


def mine():
    print("You head on down to the mines...")


# this is the main game loop. it will run until a win/failure condition is met.

def main_menu():
    print("1. Go to the shop")
    print("2. Go to the mine")
    print("3. Skip today")
    choice = input("What would you like to do? ")
    if choice == "1":
        shop()
    elif choice == "2":
        if minedToday == True:
            print("You have already mined today.")
            time.sleep(1)
        else:
            minedToday = True
            mine()
    elif choice == "3":
        print("You skip today.")
        time.sleep(1)
        currentDay += 1


def game_loop():
    currentDay = 1
    while currentDay < 32:
        print("It is day " + str(currentDay))
        minedToday = False
        main_menu()


# get the show on the road


if __name__ == '__main__':
    game_loop()

# end of game. thank you for playing!
