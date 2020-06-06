from HumanoidClass import *
from EventClass import *
from CombatClass import *
from MapClass import *
import sys
import time
import random

story = "Hello! Welcome to the haunted forest. Your objective is to either survive until dawn or find the gemstone which " \
		"harnesses the power of a million suns, and banish the evils within the forest.\n"
lore = "I was brushing my teeth, getting ready for bed"


def typing(string):
	char: str
	for char in string:
		time.sleep(.02)
		print(char, end='')
	print("")


#typing(story)

# name = input("Input: ")
name = "Nikita"
Player1 = Player(name, 100, 100, "player_char", 10)

Map1 = main_chain_list

Player1.location = Map1[0]

move_condition = True
win_condition = True

while win_condition:
	action = input("What would you like to do? Below are possible options, type exactly as below to preform an action:\n"
					"1 - MOVE\n"
					"2 - What is my goal?\n")
	if action == "MOVE":
		move_condition = True
		while move_condition:
			if Player1.location.links == []:
				print("Please re-run the program (the map sometimes does not generate correctly)")
			for i in range(len(Player1.location.links)):
				print(Player1.location.links[i].name)
			next_room_choice = input("What room would you like to move to? Or CANCEL\n")
			if next_room_choice == "CANCEL":
				move_condition = False
			move_verification = False
			for i in range(len(Player1.location.links)):
				if next_room_choice == Player1.location.links[i].name:
					move_verification = True
					next_room = Player1.location.links[i]
			if move_verification:
				Player1.location = next_room
		
	if action == "What is my goal?":
		print("Your goal is to get to " + Map1[-1].name)
	if Player1.location == Map1[-1]:
		win_condition = False

print("You Won!")