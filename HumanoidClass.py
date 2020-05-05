"""
Mr. Park's Notes on Classes
----------------
1) Generalized tools with arbitrary characteristics used to run processes.
	Example
		- Computers, every computer has a set of components but specific to
		certain models.
2) Useful compliments to classes- inheritance, importing modules, repetitive
calling for similar tasks.
"""


class Humanoid:
	def __init__(self, hp, archetype, attack, can_deal_damage, dmg_mult):
		"""
		Represents a character in the monster game.

		@type self: humanoid
		@type hp: float
		@type archetype: string
		@type attack: float
		@type dmg_mult: float
		@rtype: None
		"""
		self.hp = hp
		self.archetype = archetype
		self.attack = attack
		self.can_deal_damage = True
		self.dmg_mult = 1
	
	def receive_damage(self, damage):
		"""
		@type self: humanoid
		@type damage: float
		@rtype: None
		"""
		self.hp -= damage
	
	def attack_humanoid(self, character):
		"""
		Character is another humanoid class object.

		@type self: Humanoid
		@type character: Humanoid
		@rtype: String
		"""
		if self.can_deal_damage:
			print("You did", self.attack, "damage!")
			character.receive_damage(self.attack)


player1 = Humanoid(100, 'human', 10, True, 1)
monster1 = Humanoid(10, 'goblin', 5, True, 1)
monster2 = Humanoid(10, 'troll', 5, True, 1)

# player1.attack_humanoid(monster1)
# player1.attack_humanoid(monster2)


# class Item:
# 	def __init__(self, name, owned):
# 		self.name = name
# 		self.owned = owned
#
# 	def use(self):
# 		if self.owned:
# 			return self


class Player(Humanoid):
	def __init__(self, name, mp, healspell, sword, cloak, wand, can_receive_damage):
		Humanoid.__init__(self, self.hp, self.attack, self.can_deal_damage)
		"""
		Represents the Player in the monster game.

		@type self: Player
		@type name: str
		@type mp: int
		@type healspell: bool
		@type sword: bool
		@type cloak: bool
		@type wand: bool
		@type hp: float
		@type archetype: str
		@type attack: float
		@rtype: None
		"""
		# self.block = block
		# self.skill = skill
		self.name = name
		self.mp = mp
		self.healspell = healspell
		self.sword = sword
		self.cloak = cloak
		self.wand = wand
		self.can_receive_damage = can_receive_damage
	
	def cast_heal(self):
		if self.mp >= 30 and self.healspell:
			self.hp += 15
			self.mp -= 30
			self.healspell = False
	
	def show_mana(self):
		print(int(self.mp))
		
	# def check_healspell(self):
	# 	return self.healspell
	
	def swing(self, character):
		if self.sword and self.can_deal_damage:
			self.attack_humanoid(character)
			self.attack_humanoid(character)
	
	def dissolve(self, character):
		if self.wand:
			character.attack = character.attack * 0.95
	
	# def hide(self, character):
	# 	if self.cloak:
	#     prevent enemy damage?
