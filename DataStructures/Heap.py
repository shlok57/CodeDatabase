class Heap:

	def __init__(self, lst = []):
		self.heap = lst
		self.heapify()

	def size(self):
		return len(self.heap)

	def __str__(self):
		return str(self.heap)

	def heapify(self):
		
		n = self.size()		
		for i in range(n,-1,-1):
			self.make_heap(i)

	def make_heap(self, i):

		n = self.size()
		index = i
		l = 2 * index + 1
		r = 2 * index + 2

		if l < n and self.heap[i] > self.heap[l]:
			index = l
		if r < n and self.heap[index] > self.heap[r]:
			index = r

		if index != i:
			self.swap(i, index)
			self.make_heap(index)


	def swap(self, i, j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

	def push(self, num):
		i = self.size()
		self.heap.append(num)
		if i != 1 and self.heap[i] < self.heap[(i-1)/2]:
			j = i
			while j!= 0:
				if self.heap[j] < self.heap[(j-1)/2]:
					self.swap(j,(j-1)/2)
				j = (j-1)/2	

	def pop(self):
		result = self.heap.pop(0)
		self.heap = [self.heap[-1]] + self.heap[:-1]
		self.heapify()
		return result

h = Heap([7,500,5,10,8,2,3])
print h

h.push(0)
print h

print h.pop()
print h

print h.pop()
print h