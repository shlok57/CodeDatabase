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

    
class BinomialHeap:

	def __init__(self):
		self.roots = []

	@staticmethod
	def merge_Tree(n1, n2):
		if n1.data > n2.data:
			n1, n2 = n2, n1
		n2.parent = n1
		n2.sibling = n1.child
		n1.child = n2
		n1.degree += 1
		return n1

	def insert(self, data):
		tempNode = Node(data)
		self._insert_Heap(tempNode)

	def _insert_Heap(self, n):
		tempHeap = BinomialHeap()
		tempHeap.roots.append(n)
		# print tempHeap.roots
		self._union_Heaps(tempHeap)
		# print self.roots
		# print "while inserting ", n.data
		self.adjust()
		# print self.roots

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
			# print i, " ", j, " ", k, " ", size
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
			# print "complete while"
	
	def make_Heap(self, l):
		for i in l:
			self.insert(i)

	def print_Heap(self):
		# print self.roots
		for i in self.roots:
			i.printNode(i)
		print

	def get_Minimum(self):
		size = len(self.roots)
		mini = 999999
		for i in range(size):
			temp = self.roots[i]
			if temp.data < mini:
				mini = temp.data
		return mini


A = BinomialHeap()
A.make_Heap([2, 1, 3, 4, 9, 6, 8])
# A.insert(2)
# A.insert(1)
# A.insert(3)
# A.insert(4)
# A.insert(9)
# A.insert(6)
# A.insert(8)
# A.insert(7)
A.print_Heap()
print A.get_Minimum()