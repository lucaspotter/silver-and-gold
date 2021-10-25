import time
import sys
import os

def tutorialScene(playedBefore):
	playedBefore = playedBefore.lower()
	if playedBefore == "y":
		print("\nwe'll skip the intro then")
		print("off you go!")
		time.sleep(1)
		os.system('clear')
		return True
	elif playedBefore == "n":
		print("\non with the tutorial then!")
		time.sleep(1)
		os.system('clear')
		print("here's the scene:")
		print("it's 1848, and the california gold rush has just started")
		print("your goal is to make as much money in a month as you can get away with")
		time.sleep(4)
		print("in order to do this, you can mine, buy, and sell various materials")
		time.sleep(2)
		print("staying true to life is our number one priority")
		print("as such, everything is dictated by luck")
		time.sleep(3)
		print("good luck!")
		return True
	else:
		print("\ndon't think that's vaild lad")
		tutorial()

def endScene(money):
	print("that's game, folks!")
	print("you ran off with", money, "dollars\n")
	time.sleep(3)
	money -= 500
	print("after paying off the pesky 500 dollar loan, you ended up with", money, "dollars!\n")
	time.sleep(3)
	#did they win?
	if money <= 0:
		print("sadly, you went broke after this whole endeavor\n")
		time.sleep(2)
		print("best of luck next time!")
		sys.exit(69)
	else:
		print("you've won the game of capitalism, my friend!")
		print("if i were you i'd just cash out now.\n")
		time.sleep(2)
		print("i'll see you next time!")
		sys.exit(420)