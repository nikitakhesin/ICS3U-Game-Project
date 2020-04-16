import random


class Event:
	def __init__(self):
		"""
		Intializes a random event

		5 events in total

		1) Item
		2) monster
		3) trap
		4) blessing
		5) Your choice
		"""
		event_choice = random.randint(1, 5)
		if event_choice == 1:
			self.event = self.event_item()
		elif event_choice == 2:
			self.event = self.event_enemy()
		elif event_choice == 3:
			self.event = self.event_trap()
	
	def event_item(self):
		"""
		1) Potion
		2) Weapon
		3) Movement
		"""
		item_choice = random.randint(1, 4)
		item_dict = {1: 'Potion', 2: 'Weapon', 3: 'Movement', 4: 'No item'}
		
		return item_dict[item_choice]
	
	def event_enemy(self):
		"""
		1) Zombie 55%
		2) KoopaTroopa 30%
		3) Primeval 5%
		4) Shadow (fake enemy, 1hp) 10%
		"""
		enemy_choice = random.randint(1, 100)
		if enemy_choice <= 55:
			enemy_choice = 1
		elif enemy_choice <= 85:
			enemy_choice = 2
		elif enemy_choice <= 90:
			enemy_choice = 3
		else:
			enemy_choice = 4
		
		enemy_dict = {1: 'Zombie', 2: 'KoopaTroopa', 3: 'Primeval', 4: 'Shadow'}
		
		return enemy_dict[enemy_choice]
	
	def event_trap(self):
		"""
		1) Stub Toe 70%
		2) Prick Hand "Bleed" (maybe damage over time?) 28%
		3) Crushed (death) 2%
		# Y) Fall Through Floor
		# X) Drop An Item
		# Z) Get Startled (nothing happens)
		"""
		trap_choice = random.randint(1, 100)
		if trap_choice <= 70:
			trap_choice = 1
		elif trap_choice <= 98:
			trap_choice = 2
		else:
			trap_choice = 3
		
		trap_dict = {1: 'Stub Toe', 2: 'Prick Hand', 3: 'Crushed'}
		
		return trap_dict[trap_choice]
	
	def event_blessing(self):
		"""
		1) Restore
		2) Minor Overall Stat Raise
		3) Major Single Stat Boost
		# 4) Enchant Item/Improve weapon
		"""
		blessing_choice = input("A Wizard Wishes To Help You, He Offers To Bless You With His Wisdom"
								"Choose Your Blessing:"
								"1 - Restore"
								"2 - Minor Overall Stat Raise"
								"3 - Major Single Stat Boost")
		
		blessing_dict = {1: 'Restore', 2: 'Minor Overall Stat Raise', 3: 'Major Single Stat Boost'}
		
		return blessing_dict[int(blessing_choice)]
