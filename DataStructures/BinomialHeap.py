# single node object 
class Node:

    def __init__(self, data):
    	self.data = data
    	self.degree = 0
    	self.child = None
    	self.sibling = None
    	self.parent = None

    def printNode(self, node):
    	while node:
    		print str(node.data) + " ",
    		self.printNode(node.child)
    		node = node.sibling

# Binomial Heap main structure
class BinomialHeap:

	def __init__(self):
		self.roots = []

	# merge heaps given two root nodes
	@staticmethod
	def merge_Tree(n1, n2):
		if n1.data > n2.data:
			n1, n2 = n2, n1
		n2.parent = n1
		n2.sibling = n1.child
		n1.child = n2
		n1.degree += 1
		return n1

	# insert a new node with given data in the heap
	def insert(self, data):
		tempNode = Node(data)
		self._insert_Heap(tempNode)

	# internal function to insert node in heap
	def _insert_Heap(self, n):
		tempHeap = BinomialHeap()
		tempHeap.roots.append(n)
		# print tempHeap.roots
		self._union_Heaps(tempHeap)
		# print self.roots
		# print "while inserting ", n.data
		self.adjust()
		# print self.roots

	# union of two heap structures into one
	def _union_Heaps(self, b2):
		b1 = self
		tempHeap = BinomialHeap()
		temp = []
		while len(b1.roots) and len(b2.roots):
			if b1.roots[0].degree > b2.roots[0].degree:
				temp.append(b2.roots.pop(0))
			else:
				temp.append(b1.roots.pop(0))
		if len(b1.roots) != 0:
			temp.extend(b1.roots)
		if len(b2.roots) != 0:
			temp.extend(b2.roots)

		self.roots = temp

	# maintain binomial heap property and merge heaps of same degree
	def adjust(self):
		size = len(self.roots)
		if size <= 1:
			return
		i=0
		j=0
		k=0
		if size == 2:
			j = 1
			k = size
		else:
			j = 1
			k = 2
		while i != size:
			if j == size:
				i += 1
			elif self.roots[i].degree < self.roots[j].degree:
				i += 1
				j += 1
				if k != (size - 1):
					k += 1
			elif k != size and self.roots[i].degree == self.roots[j].degree \
					and self.roots[j].degree == self.roots[k].degree:
				i += 1
				j += 1
				k += 1
			elif self.roots[i].degree == self.roots[j].degree:
				self.roots[i] = self.merge_Tree(self.roots[i], self.roots[j])
				# self.roots[j] = None
				self.roots.pop(j)
				size -= 1
				if k < size:
					k += 1
				else:
					k = size
	
	# make heap by inserting nodes with given data 	
	def make_Heap(self, l):
		for i in l:
			self.insert(i)

	# print Heap
	def print_Heap(self):
		# print self.roots
		for i in self.roots:
			i.printNode(i)
		print

	# get the minimum node of the heap
	def get_Minimum(self):
		size = len(self.roots)
		mini = 999999
		minNode = None
		for i in range(size):
			temp = self.roots[i]
			if temp.data < mini:
				mini = temp.data
				minNode = temp
		return minNode

	# extract (pop) the minimum node from the tree 
	def extract_Minimum(self):
		minNode = self.get_Minimum()
		self.roots.remove(minNode)
		tempHeap = BinomialHeap()
		next_root = minNode.child
		while next_root:
			tempHeap.roots.insert(0,next_root)
			next_root = next_root.sibling
		for i in tempHeap.roots:
			i.sibling = None
			i.parent = None
		self._union_Heaps(tempHeap)
		minNode.child = minNode.parent = minNode.sibling = None
		return minNode

	# decrese data for a given node and mantain the heap
	def decrease_Key(self, node, val):
		if val > node.data:
			return -1
		node.data = val
		y = node
		z = y.parent
		while z and y.data < z.data:
			y.data, z.data = z.data, y.data
			y = z
			z = z.parent

	# delete the given node from the heap
	def delete(self, node):
		self.decrease_Key(node, -99999)
		self.extract_Minimum()

# declare a new binomial heap instance
A = BinomialHeap()

# insert values into the heap
A.make_Heap([2, 1, 3, 4, 9, 6, 8, 7])

########## DEBUG STATEMENTS ###############

A.print_Heap()
print A.get_Minimum().data
print A.extract_Minimum().data
A.print_Heap()
A.decrease_Key(A.roots[2].child.child, 5)
print A.roots[2].child.child.data
A.delete(A.roots[1].child)
A.print_Heap()

# A.make_Heap([2, 1, 3, 4, 9, 6, 8])
# A.insert(2)
# A.insert(1)
# A.insert(3)
# A.insert(4)
# A.insert(9)
# A.insert(6)
# A.insert(8)
# A.insert(7)
# print A.get_Minimum().data
# print A.extract_Minimum().data
# B = A.extract_Minimum()
# B.print_Heap()
# print "Child ", B.roots[0].child.data
# print "Child-child ", B.roots[0].child.child.data
# print "Child-sibling-1 ", B.roots[0].child.sibling.data
# print "Child-sibling-2 ", B.roots[0].child.sibling.sibling.data
# print "Child-sibling-3 ", B.roots[0].child.sibling.sibling.sibling.data