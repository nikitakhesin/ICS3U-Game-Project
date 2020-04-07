class Node:
	def __init__(self, node_value):
		self.next_left = None
		self.next_right = None
		self.value = node_value
		self.total = 0
	
	def return_next_left(self):
		return self.next_left
	
	def return_next_right(self):
		return self.next_right
	
	def insert(self, start_Node, insert_value):
		if insert_value != start_Node.value:
			if insert_value < start_Node.value:
				if start_Node.next_left is None:
					start_Node.next_left = Node(insert_value)
				
				elif start_Node.next_left is not None:
					return self.insert(start_Node.next_left, insert_value)
			
			elif insert_value > start_Node.value:
				if start_Node.next_right is None:
					start_Node.next_right = Node(insert_value)
				
				elif start_Node.next_right is not None:
					return self.insert(start_Node.next_right, insert_value)
	
	def sum(self, start_Node):
		if start_Node == self:
			self.total = 0
		
		self.total += start_Node.value
		if start_Node.next_left is None and start_Node.next_right is None:
			return self.total
		
		elif start_Node.next_left is not None and start_Node.next_right is None:
			return self.sum(start_Node.next_left)
		
		elif start_Node.next_left is None and start_Node.next_right is not None:
			return self.sum(start_Node.next_right)
		
		elif start_Node.next_left is not None and start_Node.next_right is not None:
			return self.sum(start_Node.next_left) + self.sum(start_Node.next_right)
	
	def search(self, start_Node, search_value):
		if search_value == start_Node.value:
			return start_Node.value
		
		elif start_Node is None:
			return None
		
		elif search_value < start_Node.value:
			return self.search(start_Node.next_left, search_value)
		
		elif search_value > start_Node.value:
			return self.search(start_Node.next_right, search_value)
