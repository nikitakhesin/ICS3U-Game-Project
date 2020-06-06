class Combat:
	def __init__(self):
		self.player_turn = True
		# Potential improvements
		self.player_vulnerabe = True
		self.player_dmg_mult = 1
		self.enemy_dmg_mult = 1
	
	def fight(self, Player, Enemy):
		if (Enemy.hp > 0) and (Player.hp <= 0):
			print("You lost the fight!")
			return None
		elif (Enemy.hp <= 0) and (Player.hp > 0):
			print("You won the fight!")
			return None
		
		elif self.player_turn:
			self.player_turn = False
			Player.attack_humanoid(Enemy)
			return self.fight(Player, Enemy)
		else:
			self.player_turn = True
			Enemy.attack_humanoid(Player)
			return self.fight(Player, Enemy)
	
	@staticmethod
	def print_stats(Player, Enemy):
		print("Currently fighting:", Enemy.archetype)
		print("Your health:", Player.hp)
		print("Enemy health:", Enemy.hp)
		print("Your damage multiplier:", Player.dmg_mult)
		print("Enemy damage multiplier:", Enemy.dmg_mult)
 
