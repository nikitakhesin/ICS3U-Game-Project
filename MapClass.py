import random


class Node:
	def __init__(self, name):
		"""
		Initializes the Node class object taking a name for an input and giving it default attributes as well. This
		includes self.links which defines the next node. There is also a position attribute, so that we could search the
		map for a node.

		Name is the name of the node
		Next refers to a node that is linked to this node

		@type self: Node
		@type name: str
		@rtype: none

		:param self: This is the Node class object which can be used to generate a chain-link map
		:param name: This is the name of the Node
		:return: none
		"""
		self.name = name
		self.links = []
		self.position = 1
	
	def return_name(self):
		return self.name
	
	def return_links(self):
		return self.links
	
	def return_position(self):
		return self.position
	
	def search(self, name):
		if name == self.name:
			print("Node found at position", self.position)
			return self.position
		elif name != self.name and self.links is not None:
			for i in range(len(self.links)):
				return self.search(self.links[i])


nodenaming = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
				'20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36',
				'37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53',
				'54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70',
				'71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87',
				'88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103',
				'104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118',
				'119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133',
				'134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148',
				'149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163',
				'164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174', '175', '176', '177', '178',
				'179', '180', '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191', '192', '193',
				'194', '195', '196', '197', '198', '199', '200']


def create_nodes(number):
	nodes_list = []
	for i in range(number):
		nodes_list.append(Node("Room " + nodenaming[0]))
		nodenaming.remove(nodenaming[0])
	return nodes_list


# def create_nodes(number):
# 	nodes_list = []
# 	for i in range(number):
# 		nodes_list.append(Node("node " + nodenaming[i]))
# 	return nodes_list


x = random.randint(5, 17)
# main_chain_list = create_nodes(x)


# node 1 - start, node x - end


def attach_one(Node1, Node2):
	if Node1 != Node2 and Node1 not in Node2.links:
		Node2.links.append(Node1)


def attach_both(Node1, Node2):
	attach_one(Node1, Node2)
	attach_one(Node2, Node1)


def connect(Node1, Node2):
	if random.randint(1, 2) == 1:
		attach_one(Node1, Node2)
	else:
		attach_both(Node1, Node2)


def create_chain(length):
	temp_list = create_nodes(length)
	for i in range(len(temp_list)):
		if i != len(temp_list) - 1:
			attach_one(temp_list[i], temp_list[i + 1])
	return temp_list


def create_side_chain(length):
	side_chain_list = create_chain(length)
	for i in range(random.randint(1, 2)):
		connect(side_chain_list[random.randint(0, len(side_chain_list) - 1)],
				side_chain_list[random.randint(0, len(side_chain_list) - 1)])
	connect(side_chain_list[random.randint(0, len(side_chain_list) - 1)],
			main_chain_list[random.randint(0, len(main_chain_list) - 1)])


main_chain_list = create_chain(x)

for i in range(x - 2):
	create_side_chain(random.randint(4, x))

# Testing proper connections
# for i in range(len(main_chain_list)):
# 	for j in range(len(main_chain_list[i].links)):
# 		print(main_chain_list[i].links[j].name)
# print("   " + main_chain_list[-1].name)