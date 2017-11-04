class Node:

	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next


class LinkedList:

	def __init__(self):
		self.first = None
		self.last = None

	def addNode(self, data = None):
		new_node = Node(data)
		if self.first == None:
			self.first = new_node
			self.last = new_node
		else:
			self.last.next = new_node
			self.last = new_node

	def __str__(self):
		if self.first == None:
			return "No nodes in LL."
		else:
			temp = self.first
			string = ""
			while temp!= None:
				string += str(temp.data) + " -> "
				temp = temp.next
			else:
				string += "None"

		return string


a = LinkedList()
a.addNode(1)
a.addNode(2)
a.addNode(3)
a.addNode(5)

print a

