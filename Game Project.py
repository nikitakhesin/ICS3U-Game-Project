"""
ICS3U1/4U1 2020-04-02



Notes on Classes
----------------

1) Generalized tools with arbitrary characteristics used to run processes.

	Example
		- Computers, every computer has a set of components but specific to
		certain models.

2) Useful compliments to classes- inheritance, importing modules, repetitive
calling for similar tasks.
"""

## Example

class iphone6:

	def __init__(self, owner, date, time, sin, lang): # <- called parameters
		self.owner = owner
		self.date = date
		self.time = time
		self.sin_number = sin
		self.language = lang

	def __repr__(self):
		return("This is " +  str(self.owner) + "''s iphone")

Sasha_iphone = iphone6("korol", '2020-04-02', 1234, 416967111, 'english')
lewons_iphone = iphone6("lewon", '2020-04-02', 4321, 416111111, 'english')



## Humanoid Class

class humanoid:

	def __init__(self, hp, attack):
		"""
		Represents a character in the monster game.

		@type self: humanoid
		@type hp: float
		@type type: string
		@type attack: float
		@rtype: None
		"""
		self.hp = hp
		self.attack = attack


	def receive_damage(self, damage):
		"""
		@type self: humanoid
		@type damage: int
		@rtype: None
		"""
		self.hp -= damage


	def attack_player(self, character):
		"""
		Character is another humanoid class object.

		@type self: Humanoid
		@rtype: String
		"""
		print("You did a total damage of", self.attack)
		character.receive_damage(self.attack)


player1 = humanoid(100, 'human', 10)
monster1 = humanoid(10, 'goblin', 5)
monster2 = humanoid(10, 'troll', 5)

player1.attack_player(monster1)
player1.attack_player(monster2)

class player(humanoid):
	def __init__(self, skill, block):
		humanoid.__init__(self, hp, attack)
		self.skill = skill
		self.block = block