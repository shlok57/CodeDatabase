class HashTable:

	def __init__(self):
		self.hash_array = [HashNode(i) for i in range(10000)]

	def get_hash(self, word):
		result = 0
		for c in word:
			result = (result * 131 + ord(c)) % 10000
		return result

	def insert(self, key, value = -1):
		key_hash = self.get_hash(key)
		hash_node = self.hash_array[key_hash]

		key_node = None
		# search if exists
		while hash_node:
			if hash_node.word == key:
				key_node = hash_node
				break
			hash_node = hash_node.next
		if key_node:
			if value == -1:
				key_node.increase_count()
			else:
				key_node.count = value
		else:
			temp_next = self.hash_array[key_hash].next
			self.hash_array[key_hash].next = HashNode(key)
			self.hash_array[key_hash].next.next = temp_next

	def delete(self,key):
		key_hash = self.get_hash(key)
		hash_node = self.hash_array[key_hash]

		key_node = None
		next_node = hash_node.next
		# search if exists
		while next_node:
			if next_node.word == key:
				break
			key_node = next_node
			next_node = next_node.next
		if next_node:
			key_node = next_node.next		
		else:
			print "Key Error"
	
	def print_hash(self):
		for i in range(10000):
			temp = self.hash_array[i].next
			if temp != None:
				while temp:
					print "|| ", temp.word, "|" , str(temp.count), "|| -> ",
					temp = temp.next
				print
			


class HashNode:

	def __init__(self, word):
		self.word = word
		self.count = 1
		self.next = None

	def increase_count(self):
		self.count += 1

H = HashTable()
A = "Output the list of words together with their counts on an output file.\
	 For this problem,you cannot use built-in-language datastuctures that \
	 can index by strings (like hashtables). Use a language that easily \
	 implements linked lists, like C/C++"
# B = A.split()
# for i in B:
# 	H.insert(i)

print H.get_hash('6')
print H.get_hash('Lb')

H.insert('6')
H.insert('Lb')
H.print_hash()
H.delete('Lb')
H.print_hash()