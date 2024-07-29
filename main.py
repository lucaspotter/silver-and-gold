import os
import time
import random
import decimal

# all variables

copperPrice = 1
ironPrice = 2
silverPrice = 3
goldPrice = 4
money = 3
loan = 50
minedToday = False
pickLevel = 1
inventory = [0, 0, 0, 0]  # [copper, iron, silver, gold]
day = 1


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    global day
    print("What would you like to do?")
    print("1. Go to the store\n2. Go to the mines\n3. Go to the bank\n4. End the day\n5. Quit")

    choice = input("? ")

    if choice == "1":
        print("You go into town and see the latest prices.")
        time.sleep(1)
        store()
    elif choice == "2":
        if minedToday:
            print("You have already mined today.")
            time.sleep(1)
        else:
            print("You head on down to the mines...")
            time.sleep(1)
            mines()
    elif choice == "3":
        print("You head on down to the bank...")
        time.sleep(1)
        bank()
    elif choice == "4":
        print("You hit the hay, hoping for fortune tomorrow.")
        day += 1
    elif choice == "5":
        print("\"Alrighty then, bye bye then!\"")
        quit()
    else:
        print("I don't understand.")


def store():
    global money
    global inventory
    print("Copper: $" + str(copperPrice))
    print("Iron: $" + str(ironPrice))
    print("Silver: $" + str(silverPrice))
    print("Gold: $" + str(goldPrice))
    print("\nWhat would you like to do?\n1. Buy\n2. Sell\n3. Upgrade\n4. Go back")
    choice = input("? ")

    if choice == "1":  # buy
        print("What resource would you like to buy?\n1.Copper\n2.Iron\n3.Silver\n4.Gold\n5. Never mind.")
        choice = input("? ")
        if choice == "1":
            print("The current price of copper is $" + str(copperPrice) + " a piece.")
            print("How much copper would you like to buy?")
            choice = input("? ")
            if int(choice) * copperPrice > money:
                print("You don't have enough money.")
                time.sleep(1)
                store()
            else:
                money -= int(choice) * copperPrice
                inventory[0] += int(choice)
                print("You have $" + str(money) + " left, and have bought " + str(choice) + " copper.")
                time.sleep(1)
                store()
        elif choice == "2":
            print("The current price of iron is $" + str(ironPrice) + " a piece.")
            print("How much iron would you like to buy?")
            choice = input("? ")
            if int(choice) * ironPrice > money:
                print("You don't have enough money.")
                time.sleep(1)
                store()
            else:
                money -= int(choice) * ironPrice
                inventory[1] += int(choice)
                print("You have $" + str(money) + " left, and have bought " + str(choice) + " iron.")
                time.sleep(1)
                store()
        elif choice == "3":
            print("The current price of silver is $" + str(silverPrice) + " a piece.")
            print("How much silver would you like to buy?")
            choice = input("? ")
            if int(choice) * silverPrice > money:
                print("You don't have enough money.")
                time.sleep(1)
                store()
            else:
                money -= int(choice) * silverPrice
                inventory[2] += int(choice)
                print("You have $" + str(money) + " left, and have bought " + str(choice) + " silver.")
                time.sleep(1)
                store()
        elif choice == "4":
            print("The current price of gold is $" + str(goldPrice) + " a piece.")
            print("How much gold would you like to buy?")
            choice = input("? ")
            if int(choice) * goldPrice > money:
                print("You don't have enough money.")
            else:
                money -= int(choice) * goldPrice
                inventory[3] += int(choice)
                print("You have $" + str(money) + " left, and have bought " + str(choice) + " gold.")
                time.sleep(1)
                store()
        else:
            print("I don't understand.")
            time.sleep(1)
            store()
    elif choice == "2":  # sell
        print("What resource would you like to sell?\n1.Copper\n2.Iron\n3.Silver\n4.Gold\n5. Never mind.")
        choice = input("? ")
        if choice == "1":
            print("How much copper would you like to sell?")
            choice = input("? ")
            if int(choice) > int(inventory[0]):
                print("You don't have that many copper.")
            else:
                money += int(choice) * copperPrice
                inventory[0] -= int(choice)
                print("You now have $" + str(money) + ", and have sold " + str(choice) + " copper.")
                time.sleep(1)
                store()
        elif choice == "2":
            print("How much iron would you like to sell?")
            choice = input("? ")
            if int(choice) > int(inventory[1]):
                print("You don't have that many iron.")
            else:
                money += int(choice) * ironPrice
                inventory[1] -= int(choice)
                print("You now have $" + str(money) + ", and have sold " + str(choice) + " iron.")
                time.sleep(1)
                store()
        elif choice == "3":
            print("How much silver would you like to sell?")
            choice = input("? ")
            if int(choice) > int(inventory[2]):
                print("You don't have that many silver.")
            else:
                money += int(choice) * silverPrice
                inventory[2] -= int(choice)
                print("You now have $" + str(money) + ", and have sold " + str(choice) + " silver.")
                time.sleep(1)
                store()
        elif choice == "4":
            print("How much gold would you like to sell?")
            choice = input("? ")
            if int(choice) > int(inventory[3]):
                print("You don't have that many gold.")
            else:
                money += choice * goldPrice
                inventory[3] -= int(choice)
                print("You now have $" + str(money) + ", and have sold " + str(choice) + " gold.")
                time.sleep(1)
                store()
        else:
            print("I don't understand.")
            time.sleep(1)
            store()
    elif choice == "3":  # upgrade
        global pickLevel
        if pickLevel == 1:
            print("You currently have a level one pickaxe, allowing you to mine copper.")
            print("To upgrade your pickaxe, you will need to pay $20. Do you want to upgrade your pickaxe?")
            choice = input("Y/N? ")
            if choice.lower() == "y":
                if money >= 20:
                    money -= 20
                    pickLevel = 2
                    print("You now have a level two pickaxe.")
                    time.sleep(1)
                    store()
                else:
                    print("You don't have enough money.")
                    time.sleep(1)
                    store()
            else:
                print("Ok.")
                time.sleep(1)
                store()
        if pickLevel == 2:
            print("You currently have a level two pickaxe, allowing you to mine copper, and iron.")
            print("To upgrade your pickaxe, you will need to pay $50. Do you want to upgrade your pickaxe?")
            choice = input("Y/N? ")
            if choice.lower() == "y":
                if money >= 50:
                    money -= 50
                    pickLevel = 3
                    print("You now have a level three pickaxe.")
                    time.sleep(1)
                    store()
                else:
                    print("You don't have enough money.")
                    time.sleep(1)
                    store()
            else:
                print("Ok.")
                time.sleep(1)
                store()
        if pickLevel == 3:
            print("You currently have a level three pickaxe, allowing you to mine copper, iron, and silver.")
            print("To upgrade your pickaxe, you will need to pay $100. Do you want to upgrade your pickaxe?")
            choice = input("Y/N? ")
            if choice.lower() == "y":
                if money >= 100:
                    money -= 100
                    pickLevel = 4
                    print("You now have a level four pickaxe.")
                    time.sleep(1)
                    store()
                else:
                    print("You don't have enough money.")
                    time.sleep(1)
                    store()
            if pickLevel == 4:
                print("You currently have a level four pickaxe, allowing you to mine copper, iron, silver, and gold.")
                print("You've hit the top - there is no better pickaxe than the one you have.")
                time.sleep(5)
                store()
            else:
                print("Ok.")
                time.sleep(1)
                store()
    elif choice == "4":
        menu()
    else:
        print("I don't understand.")
        time.sleep(1)
        store()


def mines():
    global inventory
    global minedToday
    if pickLevel >= 1:
        minedCopper = random.randint(5, 9)
        inventory[0] += minedCopper
        print("You mined " + str(minedCopper) + " copper.")
    if pickLevel >= 2:
        minedIron = random.randint(5, 7)
        inventory[1] += minedIron
        print("You mined " + str(minedIron) + " iron.")
    if pickLevel >= 3:
        minedSilver = random.randint(3, 5)
        inventory[2] += minedSilver
        print("You mined " + str(minedSilver) + " silver.")
    if pickLevel == 4:
        minedGold = random.randint(1, 3)
        inventory[3] += minedGold
        print("You mined " + str(minedGold) + " gold.")
    minedToday = True
    menu()


def bank():
    global loan
    global money
    print("You currently have $" + str(money) + ", and an active loan of $" + str(loan) + ".")
    print("What would you like to do?\n1. Pay off your loan\n2. Take out a loan\n3. Go back")
    choice = input("? ")
    if choice == "1":  # pay off
        if loan == 0:
            print("You don't have a loan.")
            time.sleep(1)
            bank()
        else:
            print("How much would you like to pay off?")
            choice = input("? ")
            if int(choice) > money:
                print("You can't afford that.")
                time.sleep(1)
                bank()
            else:
                money -= int(choice)
                loan -= int(choice)
                print("Your new loan balance is $" + str(loan) + ", leaving you with $" + str(money) + ".")
                time.sleep(1)
                menu()
    elif choice == "2":
        if loan > 0:
            print("You already have a loan.")
            time.sleep(1)
            bank()
        else:
            print("You may take out a loan of up to 200% your current balance. This is currently $" + str(money * 2) + ".")
            print("How much would you like to take out?")
            choice = input("? ")
            if int(choice) > money * 2:
                print("The bank won't give you that kind of money.")
                time.sleep(1)
                bank()
            else:
                money += int(choice)
                loan += int(choice)
                print("Your new loan balance is $" + str(loan) + ", leaving you with $" + str(money) + ".")
                time.sleep(1)
                menu()
            time.sleep(1)
            menu()
    elif choice == "3":
        menu()
    else:
        print("I don't understand.")
        time.sleep(1)
        bank()


def newDay():
    global copperPrice
    global ironPrice
    global silverPrice
    global goldPrice

    copperChange = int(decimal.Decimal(random.randrange(-20, 20)) / 100)  # thank you stack overflow
    ironChange = int(decimal.Decimal(random.randrange(-40, 40)) / 100)
    silverChange = int(decimal.Decimal(random.randrange(-60, 60)) / 100)
    goldChange = int(decimal.Decimal(random.randrange(-80, 80)) / 100)

    if copperPrice + copperChange < 1:
        copperChange = 0
    elif copperPrice + copperChange > 1:
        copperPrice += copperChange

    if ironPrice + ironChange < 1:
        ironChange = 0
    elif ironPrice + ironChange > 1:
        ironPrice += ironChange

    if silverPrice + silverChange < 1:
        silverChange = 0
    elif silverPrice + silverChange > 1:
        silverPrice += silverChange

    if goldPrice + goldChange < 1:
        goldChange = 0
    elif goldPrice + goldChange > 1:
        goldPrice += goldChange

    return copperPrice, ironPrice, silverPrice, goldPrice


print("Welcome to the game!") # intro
time.sleep(1.5)
print("It's 1852, and you have just moved across the country to find the treasure buried in those California hills.")
time.sleep(3)
clear()


while day <= 31: # gayming
    minedToday = False
    print("It is a new day. Day " + str(day) + ", in fact.")
    print("You have $" + str(money) + " in your pocket. You still have a loan of $" + str(loan) + " to pay off.\n")
    time.sleep(5)

    if day >= 2:
        print("Prices have changed! Go to the store for more information.")
        time.sleep(3)

    clear()
    menu()
    newDay()

if day == 32:
    print("Your month long stint in town is over.")
    time.sleep(3)
    if loan > 0:
        print("The bank won't let you leave with that loan of $" + str(loan) + " you have yet. They take your money and an extra 20% for the pleasure.")
        money -= int(loan * 1.2)
        print("This leaves you with $" + str(money) + ".")
        loan = 0

    if money < 0:
        print("You have nothing left. You leave California behind, without a single gold nugget...")

    if 0 < money < 5:
        print("You leave California with $" + str(money) + ", walking away just barely with what you came with.")

    if 5 < money < 15:
        print("You leave California with $" + str(money) + ", walking away a little more then that what you came with.")

    if 15 < money < 30:
        print("You leave California with $" + str(money) + ", walking away with a solid stake in your back pocket.")

    if money < 30:
        print("You leave California with $" + str(money) + ", walking away with gold in your pocket.")

    time.sleep(3)

    clear()
    print("-------------------------------------")
    print("   SILVER & GOLD - BY LUCAS POTTER")
    print("-------------------------------------\n")
    print("Score of " + str(money) + " points!\nSubmit your score at github.com/lucaspotter/silver-and-gold")

