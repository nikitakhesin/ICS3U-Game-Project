from HumanoidClass import *
from EventClass import *
from CombatClass import *
from MapClass import *
import sys
import time

story = "Hello! Welcome to the haunted forest. Your objective is to either survive until dawn or find the gemstone which " \
		"harnesses the power of a million suns, and banish the evils within the forest."


def typing(string):
	char: str
	for char in string:
		time.sleep(.21)
		print(char, end='')


typing(story)

Player1 = Player(input(typing("What is your name? ")), 100, True, False, False, False, True)
