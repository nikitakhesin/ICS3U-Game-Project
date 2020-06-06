from HumanoidClass import *
from EventClass import *
from CombatClass import *
from MapClass import *
import sys
import time
import random

story = "Hello! Welcome to the haunted forest. Your objective is to either survive until dawn or find the gemstone which " \
		"harnesses the power of a million suns, and banish the evils within the forest.\n"
lore = "I was brushing my teeth, getting ready for bed"  # This was going to be a more detailed story with background and plot


def typing(string):
	char: str
	for char in string:
		time.sleep(.02)
		print(char, end='')
	print("")

print(story)
#typing(story)

# name = input("Input: ")
# The user enters a name for the Player class object
name = input("Please enter your name: ")
Player1 = Player(name, 100, 100, "player_char", 10)

# The map is made
Map1 = main_chain_list

# The Player's location is set at the begining of the map
Player1.location = Map1[0]

# These are conditions for the while loop to end instead of running infinitely, this is a personal style of programming, I do not know of another way to accomplish the same thing
move_condition = True
win_condition = True

# The game is started and will end on the condition that the player is in the final room
while win_condition:
	# The player is prompted to enter his action of choice from a list of choices
	action = input("What would you like to do? Below are possible options, type exactly as below to preform an action:\n"
					"1 - MOVE\n"
					"2 - What is my goal?\n")
	# Should the player choose to "MOVE", he will be directed here
	if action == "MOVE":
		# Starts a similar while loop for the MOVE 'state'
		move_condition = True
		while move_condition:
			# I am not sure why this happens, but my map sometimes does not work
			if Player1.location.links == []:
				print("Please re-run the program (the map sometimes does not generate correctly)")
			# Shows the options for where to move to
			for i in range(len(Player1.location.links)):
				print(Player1.location.links[i].name)
			# Asks for an input
			next_room_choice = input("What room would you like to move to? Or CANCEL\n")
			# Checks if the user decided to CANCEL movement
			if next_room_choice == "CANCEL":
				# Makes this nested while loop stop looping
				move_condition = False
			# This is to make sure that the movement from one room to another is not premature
			move_verification = False
			# Starts a for loop with the number of possible next rooms as the range
			for i in range(len(Player1.location.links)):
				# Checks that the user correctly picked an option for the next room
				if next_room_choice == Player1.location.links[i].name:
					# Confirms the move
					move_verification = True
					# sets the next room to be the one the player is moving to
					next_room = Player1.location.links[i]
			# Once verified, allows the player to move to the chosen room
			if move_verification:
				Player1.location = next_room
				# An event occurs in the next room
				Event()
	
	# If the player would like to know a spoiler and be told what number the final room is, the player can ask
	if action == "What is my goal?":
		# The goal is printed on screen
		print("Your goal is to get to " + Map1[-1].name)
	# This checks every loop to see if the player is in the last room, if he is, it exits the while loop
	if Player1.location == Map1[-1]:
		win_condition = False

# Congratulations! You won
print("You Won!")