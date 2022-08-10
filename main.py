# import important modules
import time
import random

# set important numbers


# it's the intro. there has to be some story or else the game wouldn't be fun!
print("Welcome to the game!")
time.sleep(1)
print("It's 1852, and you have just moved across the country to find the treasure buried in those California hills.")
time.sleep(3)
print("You've taken up residence in a small boom-town, and you believe you'll be the first to hit it off.")
time.sleep(3)
print("After taking a small loan from the bank and making purchases for the bare minimum equipment, you're ready to go.")
time.sleep(3)

# here's where the fun begins!


# putting the random in the s&p 500


def market():
	pass


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
		print("How much copper would you like to buy?")
		choice = input("? ")
	elif choice == "2":
		print("How much iron would you like to buy?")
		choice = input("? ")
	elif choice == "3":
		print("How much silver would you like to buy?")
		choice = input("? ")
	elif choice == "4":
		print("How much gold would you like to buy?")
		choice = input("? ")
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
	pass


# this is the main game loop. it will run until a win/failure condition is met.


def game_loop():
	currentDay = 1
	while currentDay < 32:
		print("It is day " + str(currentDay))
		time.sleep(1)
		time.sleep(1)
		print("1. Go to the shop")
		print("2. Go to the mine")
		print("3. Skip today")
		choice = input("What would you like to do? ")
		if choice == "1":
			shop()
		elif choice == "2":
			mine()
			currentDay += 1
		elif choice == "3":
			print("You skip today.")
			time.sleep(1)
			currentDay += 1


# get the show on the road


if __name__ == '__main__':
	game_loop()
