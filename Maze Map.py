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


def create_nodes(number):
	nodes_list = []
	for i in range(number):
		nodes_list.append(Node("node " + str(i + 1)))
	return nodes_list


x = random.randint(5, 17)
main_chain_list = create_nodes(x)
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


def create_chain(start_length, end_length):
	temp_list = create_nodes(random.randint(start_length, end_length))
	for i in range(len(temp_list)):
		if i != len(temp_list) - 1:
			attach_one(temp_list[i], temp_list[i + 1])
	return temp_list


def create_side_chain(length):
	side_chain_list = create_chain(length, length)
	for i in range(random.randint(1, 2)):
		connect(side_chain_list[random.randint(0, len(side_chain_list))], side_chain_list[random.randint(0, len(side_chain_list))])
	connect(side_chain_list[random.randint(0, len(side_chain_list))], main_chain_list[random.randint(0, len(main_chain_list))])


for i in range(len(x - 2)):
	create_side_chain(random.randint(4, x))