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
day = 1


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    global day
    print("What would you like to do?")
    print("1. Go to the store\n2. Go to the mines\n3. Go to the bank\n4. Have a day off\n5. Quit")

    choice = input("? ")

    if choice == "1":
        store()
    elif choice == "2":
        mines()
    elif choice == "3":
        bank()
    elif choice == "4":
        print("♪ ...searching for my lost shaker of salt... ♫")
        day += 1
    elif choice == "5":
        print("\"Alrighty then, bye bye then!\"")
        quit()
    else:
        print("I don't understand.")


def store():
    print("You go into town and see the latest prices.")
    time.sleep(1)


def mines():
    print("You head on down to the mines...")


def bank():
    print("You head on down to the bank...")


# intro
print("Welcome to the game!")
time.sleep(1.5)
print("It's 1852, and you have just moved across the country to find the treasure buried in those California hills.")
time.sleep(3)
clear()
# gayming

while day <= 31:
    print("It is a new day. Day " + str(day) + ", in fact.")
    print("You have $" + str(money) + " in your pocket. You still have a loan of $" + str(loan) + " to pay off.\n")
    time.sleep(5)

    if day >= 2:
        print("Prices have changed! Go to the store for more information.")
        time.sleep(3)

    clear()
    menu()
