class Node:

	def __init__(self,val):
		self.key = val
		self.parent = None
		self.left = None
		self.right = None
		self.color = None
		self.oc = None

	def __str__(self):
		return str(self.key)

class BST:

	def __init__(self, val = None):
		if val != None:
			self.root = Node(val)
		else:
			self.root = None

	def insert_BST(self, val):
		tempP = None
		tempN = self.root
		NewNode = Node(val)

		while tempN != None:
			tempP = tempN
			if NewNode.key < tempN.key:
				tempN = tempN.left
			else:
				tempN = tempN.right

		NewNode.parent = tempP
		if tempP == None:
			self.root = NewNode
		elif NewNode.key < tempP.key:
			tempP.left = NewNode
		else:
			tempP.right = NewNode

	def minimum(self, node):
		temp = node
		if temp == None:
			return "Tree Empty"
		while temp.left:
			temp = temp.left
		return temp

	def maximum(self, node):
		temp = node
		if temp == None:
			return "Tree Empty"
		while temp.right:
			temp = temp.right
		return temp

	def successor(self, x):
		if x.right != None:
			return self.minimum(x.right)
		y = x.parent
		while y != None and x == y.right:
			x = y
			y = y.parent
		return y

	def predecessor(self, x):
		if x.left != None:
			return self.maximum(x.left)
		y = x.parent
		while y != None and x == y.left:
			x = y
			y = y.parent
		return y

	def search(self, x, key):
		if x == None:
			return -1
		if key == x.key:
			return x
		if key < x.key:
			return self.search(x.left, key)
		else:
			return self.search(x.right, key)

	def __str__(self):
		result = ""
		result = self.print_inorder(self.root, result)
		return result

	def print_inorder(self, node, res):
		if node.left:
			res = self.print_inorder(node.left, res)
		res = res + str(node.key) + " "
		if node.right:
			res = self.print_inorder(node.right, res)
		return res

	def dprint_inorder(self, node):
		if node.left:
			self.dprint_inorder(node.left)
		print str(node.key) + " " + node.color
		if node.right:
			self.dprint_inorder(node.right)

	def _left_rotate(self, x):
		y = x.right
		x.right = y.left
		if y.left != None:
			y.left.parent = x
		y.parent = x.parent
		if x.parent == None:
			self.root = y
		elif x == x.parent.left:
			x.parent.left = y
		else:
			x.parent.right = y
		y.left = x
		x.parent = y

	def _right_rotate(self, y):
		x = y.left
		y.left = x.right
		if x.right != None:
			x.right.parent = y
		x.parent = y.parent
		if y.parent == None:
			self.root = x
		elif y == y.parent.right:
			y.parent.right = x
		else:
			y.parent.left = x
		x.right = y
		y.parent = x

	def insert(self, val):
		z = Node(val)
		y = None
		x = self.root
		while x != None:
			y = x
			if z.key < x.key:
				x = x.left
			else:
				x = x.right
		z.parent = y
		if y == None:
			self.root = z
		elif z.key < y.key:
			y.left = z
		else:
			y.right = z
		z.left = None
		z.right = None
		z.color = RED
		self._insert_fixup(z)

	def _insert_fixup(self, z):
		while z.parent != None and z.parent.parent != None and z.parent.color == RED:
			if z.parent == z.parent.parent.left:
				y = z.parent.parent.right
				if y != None and y.color == RED:
					z.parent.color = BLACK
					y.color = BLACK
					z.parent.parent.color = RED
					z = z.parent.parent
				elif z == z.parent.right:
					z = z.parent
					self._left_rotate(z)
				else:
					if z.parent != None:
						z.parent.color = BLACK
						if z.parent.parent != None:
							z.parent.parent.color = RED 
							self._right_rotate(z.parent.parent)
			else:
				y = z.parent.parent.left
				if y != None and y.color == RED:
					z.parent.color = BLACK
					y.color = BLACK
					z.parent.parent.color = RED
					z = z.parent.parent
				elif z == z.parent.left:
					z = z.parent
					self._right_rotate(z)
				else:
					if z.parent != None:
						z.parent.color = BLACK
						if z.parent.parent != None:
							z.parent.parent.color = RED 
							self._left_rotate(z.parent.parent)

		self.root.color = BLACK

	def _transplant(self, u, v):
		if u.parent == None:
			self.root = v
		elif u == u.parent.left:
			u.parent.left = v
		else:
			u.parent.right = v
		v.parent = u.parent

	def delete(self, z):
		y = z
		y.oc = y.color
		if z.left == None:
			x = z.right
			self._transplant(z, z.right)
		elif z.right == None:
			x = z.left
			self._transplant(z,z.left)
		else:
			y = self.minimum(z.right)
			y.oc = y.color
			x = y.right
			if y.parent == z:
				x.parent = y
			else:
				self._transplant(y,y.right)
				y.right = z.right
				y.right.parent = y
			self._transplant(z,y)
			y.left = z.left
			y.left.parent = y
			y.color = z.color
		if y.oc == BLACK:
			self._delete_fixup(x)

	def _delete_fixup(self, x):
		while x != self.root and x.color == BLACK:
			if x == x.parent.left:
				w = x.parent.right
				if w.color == RED:
					w.color = BLACK
					x.parent.color = RED
					self._left_rotate(x.parent)
					w = x.parent.right
				if w.left.color == BLACK and w.right.color == BLACK:
					w.color = RED
					x = x.parent
				elif w.right.color == BLACK:
					w.left.color = BLACK
					w.color = RED
					self._right_rotate(w)
					w = x.parent.right
				w.color = x.parent.color
				x.parent.color = BLACK
				w.right.color = BLACK
				self._left_rotate(x.parent)
				x = self.root
			else:
				w = x.parent.left
				if w.color == RED:
					w.color = BLACK
					x.parent.color = RED
					self._right_rotate(x.parent)
					w = x.parent.left
				if w.right.color == BLACK and w.left.color == BLACK:
					w.color = RED
					x = x.parent
				elif w.left.color == BLACK:
					w.right.color = BLACK
					w.color = RED
					self._left_rotate(w)
					w = x.parent.left
				w.color = x.parent.color
				x.parent.color = BLACK
				w.left.color = BLACK
				self._right_rotate(x.parent)
				x = self.root
		x.color = BLACK



RED = "Red"
BLACK = "Black"

if __name__ == "__main__":
	inp = raw_input().split()
	if (len(inp) > 0):
		A = BST(int(inp[0]))
		for i in inp[1:]:
			A.insert(int(i))	
		A.dprint_inorder(A.root)
	else:
		print "Provide input"
		exit(0)
	cont = 1
	while (cont):
		print ""
		print "Choose Option: "
		print "1. Insert x"
		print "2. Search x"
		print "3. Delete x"
		print "4. Minimum"
		print "5. Maximum"
		print "6. Successor of x"
		print "7. Predecessor of x"
		print "8. Sort"
		print "9. Exit"
		print ""
		ans = raw_input()
		answer = int(ans[0])
		print ""
		if answer == 1:
			i = int(raw_input("Enter a num to be inserted: "))
			A.insert(i)
			print str(i) + " inserted"
		elif answer == 2:
			i = int(raw_input("Enter a num to be searched: "))
			i = A.search(A.root, i)
			if i != -1:
				print str(i) + " found"
			else:
				print "Not Found"
		elif answer == 3:
			i = int(raw_input("Enter a num to be deleted: "))
			temp = A.search(A.root, i)
			if temp != -1:
				print A.delete(temp)
			else:
				print "Not Found"
		elif answer == 4:
			print "Minimum - ",
			print A.minimum(A.root)
		elif answer == 5:
			print "Maximum - ",
			print A.maximum(A.root)
		elif answer == 6:
			i = int(raw_input("Enter a num to get the successor of: "))
			temp = A.search(A.root, i)
			if temp != -1:
				temp = A.successor(temp)
				print "Successor - " + str(temp)
			else:
				print "Not Found"
		elif answer == 7:
			i = int(raw_input("Enter a num to get the predecessor of: "))
			temp = A.search(A.root, i)
			if temp != -1:
				temp = A.predecessor(temp)
				print "Predecessor - " + str(temp)
			else:
				print "Not Found"
		elif answer == 8:
			print "Sorted Array: ", A
		elif answer == 0:
			A.dprint_inorder(A.root)
		else:
			cont = 0

	# A = BST()
	# A.insert(101)
	# A.insert(100)
	# A.insert(99)
	# A.insert(87)
	# A.insert(30)
	# A.insert(33)
	# A.insert(24)
	# # A.insert(30)
		
	# print A.root ,  " ", A.root .color
	# # print A.root.parent ,  " ", A.root.parent.color
	# print A.root.left,  " ", A.root.left.color
	# print A.root.left.left,  " ", A.root.left.left.color
	# print A.root.left.left.left,  " ", A.root.left.left.left.color
	# print A.root.left.right,  " ", A.root.left.right.color
	# print A.root.right,  " ", A.root.right.color
	# print A.root.right.left,  " ", A.root.right.left.color
	# print A.root.right.right,  " ", A.root.right.right.color
	# print A.root.right.right.right,  " ", A.root.right.right.right.color
	# print A.root.right.left.right,  " ", A.root.right.left.right.color
	# print A.root.right.left.left,  " ", A.root.right.left.left.color
	# print A.root.left.left
	A.

	# A.insert(2)
	# A.insert(3)
	# A.insert(6)
	# A.insert(8)
	# A.insert(9)
	# A.insert(10)
	# A.insert(11)
	# A.insert(7)
	# A.dprint_inorder(A.root)
	# print "---------------------------------"
	# A.delete(A.root.right)
	# A.dprint_inorder(A.root)
	# print "---------------------------------"
	# A.insert(9)
	# print "Predecessor - ", A.predecessor(A.root.right)
	# print "Successor - ", A.successor(A.root.right.left.right)
	# print "Minimum - ", A.minimum(A.root)
	# print "Maximum - ", A.maximum(A.root)
	# print "---------------------------------"
	# print "Search 7 - ", A.search(A.root, 7)
	# print "FSearch 1 - ", A.search(A.root, 1)
	# print "---------------------------------"