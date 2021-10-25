import time
import sys
import random
import os

# base money
money = 501
# player inventory
coalAmount = 0
ironAmount = 0
goldAmount = 0
silverAmount = 0
copperAmount = 0
# ore pricing
coalPrice = 10
ironPrice = 20
goldPrice = 100
silverPrice = 100
copperPrice = 50 



def mine():
	# this is painful <3
	global money
	global coalAmount
	global ironAmount
	global goldAmount
	global silverAmount
	global copperAmount	
	global coalPrice
	global ironPrice
	global goldPrice
	global silverPrice
	global copperPrice

	print("you decided to go deep in the mines for the day.")
	time.sleep(3)
	print("after spending the day in the mines, you got")
	reward = random.randint(0,19)
	if reward <= 9:
		reward = random.randint(0,5)
		coalAmount += reward
		print(reward, "coal!")
	elif reward >= 9 and reward <= 12:
		reward = random.randint(0,5)
		ironAmount += reward
		print(reward, "iron!")
	elif reward >= 12 and reward <= 15:
		reward = random.randint(0,5)
		copperAmount += reward
		print(reward, "copper!")
	elif reward >= 15 and reward <= 18:
		reward = random.randint(0,5)
		silverAmount += reward
		print(reward, "silver!")
	elif reward == 19:
		reward = random.randint(0,5)
		goldAmount += reward
		print(reward, "gold!")		

def buy():
	# this is painful <3
	global money
	global coalAmount
	global ironAmount
	global goldAmount
	global silverAmount
	global copperAmount	
	global coalPrice
	global ironPrice
	global goldPrice
	global silverPrice
	global copperPrice

	print("welcome to the store!")	
	print("your actions\n1...Buy\n2...Check Prices\n")
	userAction = int(input("? "))
	while True:
		if userAction == 1:
			print("What would you like to buy?")
			print("your choices\n1...Coal\n2...Iron\n3...Copper\n4...Silver\n5...Gold")
			userAction = int(input("? "))
			while True: 
				if userAction == 1:
					print("You have", money, "dollars")
					print("How much coal would you like?")
					userAction = int(input("? "))
					value = userAction * coalPrice
					if value > money:
						print("You don't have enough money for that!\n")
						print("You have", money, "dollars")
						print("How much coal would you like?")
						userAction = int(input("? "))
						pass
					if value < money:
						print("You bought", userAction, "coal for", value,"dollars")
						coalAmount += userAction	
						money -= value
						break
				if userAction == 2:
					print("You have", money, "dollars")
					print("How much iron would you like?")
					userAction = int(input("? "))
					value = userAction * ironPrice
					if value > money:
						print("You don't have enough money for that!\n")
						print("You have", money, "dollars")
						print("How much iron would you like?")
						userAction = int(input("? "))
					if value < money:
						print("You bought", userAction, "iron for", value,"dollars")
						ironAmount += userAction	
						money -= value
						break
				if userAction == 3:
					print("You have", money, "dollars")
					print("How much copper would you like?")
					userAction = int(input("? "))
					value = userAction * copperPrice
					if value > money:
						print("You don't have enough money for that!\n")
						print("You have", money, "dollars")
						print("How much copper would you like?")
						userAction = int(input("? "))
						pass
					if value < money:
						print("You bought", userAction, "copper for", value,"dollars")
						copperAmount += userAction	
						money -= value
						break
				if userAction == 4:
					print("You have", money, "dollars")
					print("How much silver would you like?")
					userAction = int(input("? "))
					value = userAction * silverPrice
					if value > money:
						print("You don't have enough money for that!\n")
						print("You have", money, "dollars")
						print("How much silver would you like?")
						userAction = int(input("? "))
						pass
					if value < money:
						print("You bought", userAction, "silver for", value, "dollars")
						silverAmount += userAction	
						money -= value
						break
				if userAction == 5:
					print("You have", money, "dollars")
					print("How much gold would you like?")
					userAction = int(input("? "))
					value = userAction * goldPrice
					if value > money:
						print("You don't have enough money for that!\n")
						print("You have", money, "dollars")
						print("How much gold would you like?")
						userAction = int(input("? "))
						pass
					if value < money:
						print("You bought", userAction, "gold for", value,"dollars")
						goldAmount += userAction	
						money -= value
						break
			break
		elif userAction == 2:
			print("Coal is", coalPrice)
			print("Iron is", ironPrice)
			print("Copper is", copperPrice)
			print("Silver is", silverPrice)
			print("Gold is", goldPrice)												
			print("your actions\n1...Buy\n2...Check Prices\n")
			userAction = int(input("? "))
		else:
			print("'I couldn't hear ya, lad,' the shopkeeper says. 'Say again?'\n")
			print("your actions\n1...Buy\n2...Check Prices\n")
			userAction = int(input("? "))

def sell():
	print("Coming Soon™")	

def invCheck():
	print("In your bag you hold:")
	print(coalAmount, "Coal")
	print(ironAmount, "Iron")
	print(copperAmount, "Copper")
	print(silverAmount, "Silver")
	print(goldAmount, "Gold")
	print(money, "dollars\n")

#gameplay loop
def gameplayLoop():
	# this is painful <3
	global money
	global coalAmount
	global ironAmount
	global goldAmount
	global silverAmount
	global copperAmount	
	global coalPrice
	global ironPrice
	global goldPrice
	global silverPrice
	global copperPrice

	for i in range(32):
		print("~~~ DAY",i,"~~~")
		time.sleep(3)
		if i == 0:
			print("once you arrive, you rent room and board, you buy your tools, and get ready for the time to come.")
			time.sleep(3)
		else:
			while True:
				coalPrice = coalPrice + random.randint(-3,5)
				ironPrice = ironPrice + random.randint(-5,10)
				copperPrice = copperPrice + random.randint(-13,25)
				silverPrice = silverPrice + random.randint(-25,50)
				goldPrice = goldPrice + random.randint(-25,50)	
				print("\nyour actions:\n1...Mine\n2...Buy\n3...Sell\n4...Check Inventory\n5...Skip Day")
				userAction = int(input("? "))
				if userAction == 1:
					mine()
					break
				elif userAction == 2:
					buy()
					break
				elif userAction == 3:
					sell()
					break
				elif userAction == 4:
					invCheck()
				elif userAction == 5:
					break
				else:
					print("you couldn't decide what to do today, so you did nothing at all.")
					break
